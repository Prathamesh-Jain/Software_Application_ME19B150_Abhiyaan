import cv2
import numpy as np
from matplotlib import pyplot as plt

original_image = cv2.imread("abhiyaan.png")
hsv_original = cv2.cvtColor(original_image, cv2.COLOR_BGR2HSV)

roi = cv2.imread("drum.png")
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

hue, saturation, value = cv2.split(hsv_roi)

# Histogram ROI
roi_hist = cv2.calcHist([hsv_roi], [0, 1], None, [180, 256], [0, 180, 0, 256])
mask = cv2.calcBackProject([hsv_original], [0, 1], roi_hist, [0, 180, 0, 256], 1)

# Filtering remove noise
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
mask = cv2.filter2D(mask, -1, kernel)
_, mask = cv2.threshold(mask, 100, 255, cv2.THRESH_BINARY)
contours,_ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # not copying here will throw an error
'''for cnt in contours:
    rect = cv2.minAreaRect(cnt) # basically you can feed this rect into your classifier
    (x,y),(w,h), a = rect # a - angle

    box = cv2.boxPoints(rect)
    box = np.int0(box) #turn into ints
    cv2.drawContours(original_image,[box],0,(0,255,0),3)'''



rects = []

# Bool array indicating which initial bounding rect has
# already been used
rectsUsed = []

for cnt in contours:
    rects.append(cv2.boundingRect(cnt))
    rectsUsed.append(False)

# Sort bounding rects by x coordinate
def getXFromRect(item):
    return item[0]

rects.sort(key = getXFromRect)

# Array of accepted rects
acceptedRects = []

# Merge threshold for x coordinate distance
xThr = 5

# Iterate all initial bounding rects
for supIdx, supVal in enumerate(rects):
    if (rectsUsed[supIdx] == False):

        # Initialize current rect
        currxMin = supVal[0]
        currxMax = supVal[0] + supVal[2]
        curryMin = supVal[1]
        curryMax = supVal[1] + supVal[3]

        # This bounding rect is used
        rectsUsed[supIdx] = True

        # Iterate all initial bounding rects
        # starting from the next
        for subIdx, subVal in enumerate(rects[(supIdx+1):], start = (supIdx+1)):

            # Initialize merge candidate
            candxMin = subVal[0]
            candxMax = subVal[0] + subVal[2]
            candyMin = subVal[1]
            candyMax = subVal[1] + subVal[3]

            # Check if x distance between current rect
            # and merge candidate is small enough
            if (candxMin <= currxMax + xThr):

                # Reset coordinates of current rect
                currxMax = candxMax
                curryMin = min(curryMin, candyMin)
                curryMax = max(curryMax, candyMax)

                # Merge candidate (bounding rect) is used
                rectsUsed[subIdx] = True
            else:
                break

        # No more merge candidates possible, accept current rect
        acceptedRects.append([currxMin, curryMin, currxMax - currxMin, curryMax - curryMin])

for rect in acceptedRects:
    img = cv2.rectangle(original_image, (rect[0], rect[1]), (rect[0] + rect[2], rect[1] + rect[3]), (0,255,0), 3)




mask = cv2.merge((mask, mask, mask))
#rect = cv2.minAreaRect(contours[0]) # basically you can feed this rect into your classifier
#(x,y),(w,h), a = rect # a - angle

#box = cv2.boxPoints(rect)
#box = np.int0(box) #turn into ints
#rect2 = cv2.drawContours(img.copy(),[box],0,(0,0,255),10)

#plt.imshow(rect2)
#plt.show()
result = cv2.bitwise_and(original_image, mask)

cv2.imshow("Original image", original_image)
cv2.waitKey(0)
cv2.destroyAllWindows()