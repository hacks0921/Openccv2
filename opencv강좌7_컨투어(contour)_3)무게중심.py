import cv2 as cv


img_color = cv.imread('contour.png')
img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)
ret, img_binary = cv.threshold(img_gray, 127, 255, 0)
contours, hierarchy = cv.findContours(img_binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    cv.drawContours(img_color, [cnt], 0, (255, 0, 0), 3)  # blue
cv.imshow("result", img_color)
cv.waitKey(0)

for cnt in contours:
    M = cv.moments(cnt)
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    cv.circle(img_color, (cx, cy), 10, (0,0,255), -1)
cv.imshow("result", img_color)
cv.waitKey(0)