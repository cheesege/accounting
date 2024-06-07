import pytesseract as tess
import cv2
import os


def solve_captcha():
    path = os.getcwd()
    image = cv2.imread(path+"\\part\\captcha.png")
    image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    ret, image = cv2.threshold(image,150,255,cv2.THRESH_BINARY)
    size = image.shape
    for x in range(size[0]-1):
        for y in range(size[1]-1):
            if (image[x,y] == 0):
                if (image[x-1,y] ==255):
                    if (image[x+1,y] == 255):
                        if (image[x,y-1] == 255):
                            if (image[x,y+1] == 255):
                                image[x,y] = 255
                                #print("change on " + str(x) + ' ' + str(y))
    cv2.namedWindow("blur",0)
    cv2.imshow("blur",image)
    cv2.waitKey(0)
    result = tess.image_to_string(image)
    #result.replace(" ","")
    #print("".join(result.split()))
    return("".join(result.split()))
solve_captcha()