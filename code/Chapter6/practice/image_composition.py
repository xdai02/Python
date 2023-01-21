import imageio
import matplotlib.pyplot as plt

def image_composition(filename1, filename2):
    pic1 = imageio.imread(filename1)
    pic2 = imageio.imread(filename2)
    row = len(pic1)
    col = len(pic1[0])

    for i in range(row):
        for j in range(col):
            R = pic1[i][j][0]
            G = pic1[i][j][1]
            B = pic1[i][j][2]
            if G > R and G > B and G > 110:
                pic1[i][j] = pic2[i][j]
    
    plt.axis('off')
    plt.imshow(pic1)
    plt.savefig("merge.jpg")
    plt.show()

image_composition("avenger.jpg", "background.jpg")