import csv

def generate_report(filename, data):
    with open(filename, "w", newline='\n') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "BMI", "Category"])
        for index, bmi in enumerate(data):
            if bmi < 18.5:
                category = "Underweight"
            elif bmi < 25:
                category = "Normal"
            elif bmi < 30:
                category = "Overweight"
            else:
                category = "Obese"
            
            writer.writerow([index + 1, "%.2f" % bmi, category])

with open("weights_and_heights.csv") as file:
    reader = csv.reader(file)
    next(reader)
    
    male = []
    female = []

    for row in reader:
        sex = row[1]
        weight, height = float(row[2]), float(row[3])
        bmi = weight / (height / 100) ** 2

        if sex == 'M':
            male.append(bmi)
        else:
            female.append(bmi)
    
generate_report("male_report.csv", male)
generate_report("female_report.csv", female)