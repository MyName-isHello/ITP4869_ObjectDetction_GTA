import numpy as np
from PIL import ImageGrab
import cv2


def draw_lines(img,lines):
    try:
        for line in lines:
            coords = line[0]
            cv2.line(img,(coords[0],coords[1]),(coords[2],coords[3]),[255,255,255],2)

    except:
        pass

def process_img(og_image):
    processed_img = cv2.cvtColor(og_image,cv2.COLOR_BGR2GRAY)
    processed_img = cv2.GaussianBlur(processed_img,(5,5),1)
    processed_img = cv2.Canny(
            processed_img,
            threshold1=50,
            threshold2=100)
    #vertices = np.array(([[10,500],
    #                    [10,300],
    #                    [300,200],
    #                    [500,200],
    #                    [800,300],
    #                    [800,500]]))    
    #processed_img = roi(processed_img,[vertices])
#                           edges
    #lines = cv2.HoughLinesP(processed_img,1,np.pi/180,180,20,15)
    #draw_lines(processed_img,lines)
    
    return processed_img


def roi(img,certices):
    mask=np.zeros_like(img)
    cv2.fillPoly(mask,certices,255)
    masked = cv2.bitwise_and(img, mask)
    return masked
def main():

    while(True):
        screen =  np.array(ImageGrab.grab(bbox=(0,40,800,640)))
        screen2=process_img(screen)
        #cv2.imshow('window',cv2.cvtColor(screen,cv2.COLOR_BGR2RGB))
        cv2.imshow("window",screen2)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
main()
