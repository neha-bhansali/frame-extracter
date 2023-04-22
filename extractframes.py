import cv2 as cv

l = ['6']
for i in l:
    cap = cv.VideoCapture(str(i) + ".mp4")
    ret , frame = cap.read()
    cv.imshow('vid' , frame)
    cv.waitKey(0)
    c = 0
    while(ret == True):
        c = c+1
        ret , frame = cap.read()
        cv.imwrite(str(i) + "\\" + str(int(c)) + ".jpg"  , frame)
    cap.release()

cap.release()


