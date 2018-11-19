# Libraries and dependencies
import numpy as numpy
import matplotlib.pyplot as plt
import cv2

# ? Configuration. 
# ! directory use this "/" slash
directory = "D:/Project/datacomm-assignment/image-processing/"
target = directory + "img-1.bmp"
threshold = 127

def process():
    img = cv2.imread(target, 0)

    (h, w) = img.shape[:2]

    # print('==== Image Properties(before rotate) ====')
    # print('all bit pixel')
    # print(img)
    # print('Size ', h, w)
    # print('Total pixel ', img.size)
    # print('Datatype ',img.dtype)
    # print('========================================')

    # Convert to binary image.
    ret, binaryImg = cv2.threshold(img, threshold, 256, cv2.THRESH_BINARY)

    # Crop the image to 4 parts.
    upperLeft = binaryImg[0:int(h/2) , 0:int(w/2)]
    upperRight = binaryImg[0:int(h/2), int(w/2):w]
    lowerLeft = binaryImg[int(h/2):h, 0:int(w/2)]
    lowerRight = binaryImg[int(h/2):h, int(w/2):w]

    splited = [upperRight, upperLeft, lowerLeft, lowerRight]
    result = ""
    # Get occurance in binary image.
    for i in range(4):
        unique, counts = numpy.unique(splited[i], return_counts=True)
        occurance = dict(zip(unique, counts))
        
        print('Part ',i+1,' : ', occurance)
        
        try:
            result = result + ("0" if occurance[0] > occurance[255] else "1")
        except KeyError:
            keys = list(occurance.keys())
            result = result + ("0" if keys[0] == 0 else "1")

    return result
    # Display image
    # cv2.imshow('Testing image', img)

    # cv2.imshow('Binary Image', binaryImg)

    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    
pr = process()
print(pr)