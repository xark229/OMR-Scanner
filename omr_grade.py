import cv2
import numpy as np
import os

que=os.listdir("question_box")
totalq=int(input("Enter total questions "))
ques=int(totalq/len(que))
choices=4
correctans=[3, 1, 4, 3, 2, 2, 1, 4, 1, 2, 4, 3, 4, 1, 1, 1, 1, 4, 3, 3, 3, 3, 3, 2, 3, 4, 3,
            3, 1, 3, 3, 2, 3, 4, 1, 1, 2, 2, 3, 4, 2, 1, 3, 1, 1, 4, 3, 1, 3, 3, 3, 1, 3, 1,
            1, 4, 3, 2, 3, 1, 4, 4, 2, 3, 4, 3, 3, 4, 6, 3, 3, 3, 4, 2, 1, 2, 4, 4, 2, 1, 3,
            2, 3, 3, 1, 3, 4, 3, 2, 3, 4, 3, 3, 1, 3, 2, 4, 1, 4, 1, 1, 3, 3, 1, 2, 4, 3, 2,
            3, 3, 3, 3, 4, 2, 2, 4, 2, 2, 2, 2, 4, 1, 3, 4, 2, 1, 1, 3, 1, 1, 2, 3, 1, 2, 1, 2, 3, 2, 1, 3, 2, 2, 1, 4, 3, 1, 1, 4, 3, 3]

def grades(boxes,ques,choices):
    pix = np.zeros((ques, choices))
    countC = 0
    countR = 0

    for images in boxes:
        totalPixel = cv2.countNonZero(images)
        pix[countR][countC] = totalPixel
        countC += 1
        if countC == choices:
            countC = 0
            countR += 1

    # finding max pixel for each question/ticked answer
    myIndex = []
    for x in range(0, ques):
        arr = pix[x]
        myIndexVal = np.where(arr == np.amax(arr))  # finding index of max pixel in array arr
        #print(myIndexVal[0])
        myIndex.append(myIndexVal[0][0]+1)
    return myIndex


def splitbox(image,que,ch):
    rows=np.array_split(image,que,axis=0)
    boxes=[]
    for r in rows:
        cols=np.array_split(r,ch,axis=1)
        for box in cols:
            boxes.append(box)
    return boxes

def getmarks(img):
    imgWGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgThresh = cv2.threshold(imgWGray, 170, 255, cv2.THRESH_BINARY_INV)[1]
    boxes=splitbox(imgThresh,ques,choices)
    myans=grades(boxes,ques,choices)
    return myans


ansList=[]
for q in que:
    path='question_box/'+q
    img=cv2.imread(path)
    list=getmarks(img)
    ansList=ansList+list

marks=0
for i in range(len(ansList)):
    if correctans[i]==ansList[i]:
        marks=marks+4
    else:
        marks-=1
wrongAns=(totalq*4-marks)/5
print ("Total marks scored ",marks)
print ("Wrong Answer ",int(wrongAns))
print ("Correct Answer ",int(totalq-wrongAns))