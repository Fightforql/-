import json
import cv2
from task1 import readimage,FindandDraw_Corners,get_objectpoints
def main():
        print("第一部分—————————————————————")
        with open('config.json', 'r') as file:
                config = json.load(file)

        global_num = config['global_num']
        size = config['size']
        square_size = config['square_size']
        images=readimage(global_num)
        imgpoints,objectpoints,img_size=FindandDraw_Corners(images,global_num,size,square_size)
        ret,mtx,dist,rvecs,tvecs=cv2.calibrateCamera(objectpoints,imgpoints,img_size,None,None)
        print("Ret:", ret)
        print("Camera Matrix:\n", mtx)
        print("Distortion Coefficients:\n", dist)
        print("Rotation Vectors:\n", rvecs)
        print("Translation Vectors:\n", tvecs)
        #得到每个旋转向量的旋转矩阵
        Rotation_matrix=[]
        for i, rvec in enumerate(rvecs):
               rotation_matrix, _ = cv2.Rodrigues(rvec)
               Rotation_matrix.append(rotation_matrix)
        print("Rotation Matrix:\n",Rotation_matrix)
        print("*********分界线**********")
        print("第二部分————————————————————")
        print("选取image7")
        cur_img=cv2.imread("Image7.tif", flags=cv2.IMREAD_COLOR)
        dst = cv2.undistort(cur_img, mtx, dist, dst=None, newCameraMatrix=None)
        if dst is None:
                print("Error: Undistortion failed.")
                return
        else:
                cv2.imshow('Distorted Image', cur_img)
                cv2.imshow('Undistorted Image', dst)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

if __name__ == "__main__":
    main()