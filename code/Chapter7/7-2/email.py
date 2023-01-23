import csv

with open("user_info.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    user_info = list(reader)

with open("user_email.csv", "w", newline="\n") as file:
    writer = csv.writer(file)
    writer.writerow(["ID", "First Name", "Last Name", "Email"])
    for user in user_info:
        id, first_name, last_name = user

        writer.writerow([
            id, first_name, last_name,
            (last_name[0] + first_name + id + "@gmail.com").lower()
        ])