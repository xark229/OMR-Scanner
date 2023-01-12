import cv2
import os


def getGrade(event, x,y, flags, param):
    if event==cv2.EVENT_LBUTTONDOWN:
        pointlist.append([x, y])
        cv2.circle(img, (x, y), 5, (0, 255, 0), cv2.FILLED)
        if len(pointlist) == 2:
            x1, y1 = pointlist[0]
            x2, y2 = pointlist[1]
            imgcr = img[y1:y2, x1:x2]
            cv2.imwrite("question_box/que_box"+str(count)+".jpg",imgcr)
path='Res/OMR.png'


count=len(os.listdir("question_box"))

pointlist=[]
img = cv2.imread(path)
while True:
    img = cv2.resize(img, (800, 600))
    cv2.setMouseCallback("image", getGrade)
    cv2.imshow("image", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    elif cv2.waitKey(1) & 0xFF == ord('r'):
        img=cv2.imread(path)
        count+=1
        continue



cv2.destroyWindow("image")
