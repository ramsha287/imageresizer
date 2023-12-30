import cv2

source="scene.jpg"
destination="resizedimg.jpg"
size=50

oimg=cv2.imread(source,cv2.IMREAD_UNCHANGED)
nwidth=int(oimg.shape[0]*size/100)
nheight=int(oimg.shape[1]*size/100)
nimg=cv2.resize(oimg,(nwidth,nheight))
cv2.imwrite(destination,nimg)
