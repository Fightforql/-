import cv2
import numpy as np
from typing import List


def get_objectpoints(size,square_size:int):
    objp = []
    for i in range(size[1]):  
        for j in range(size[0]): 
            objp.append([square_size * j, square_size * i, 0])

    return objp


def readimage(global_num:int)-> List[np.ndarray]:
        images=[]
        for i in range(1,global_num):
                filename = f"Image{i}.tif" 
                img = cv2.imread(filename, flags=cv2.IMREAD_COLOR)
                if img is None:
                        print(f"Failed to load {filename}")
                else:
                        print(f"Successfully loaded {filename}")
                        images.append(img)
        return images

def FindandDraw_Corners(images:List[np.ndarray],global_num:int,size:tuple,square_size:int):
        imgpoints = []
        objectpoints=[]
        objp = np.zeros((1, size[0] * size[1], 3), np.float32)
        objp[0, :, :2] = np.mgrid[0:size[0], 0:size[1]].T.reshape(-1, 2)*square_size
        #print(objp)
        for i in range(1,global_num):
                img=images[i-1]
                filename = f"Image{i}.tif" 
                ret,corners=cv2.findChessboardCorners(img,size)
                if ret !=0:
                        #print(corners)
                        imgpoints.append(corners)
                        objectpoints.append(objp)
                        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                        print(f"Successfully found {filename}'s corners")
                        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
                        corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
                        cv2.drawChessboardCorners(img, size, corners2, ret)
                        cv2.imshow(winname="image title", mat=img)
                        cv2.waitKey(700)
                else:
                        print(f"Failed to find {filename}'s corners")
        return imgpoints,objectpoints,gray.shape



