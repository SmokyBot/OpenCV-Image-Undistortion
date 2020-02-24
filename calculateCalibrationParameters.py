import numpy as np
import cv2 as cv
import glob
import json

#define path to images used for calibration here
calibration_images = glob.glob('calibration/*.jpg')


# termination criteria
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((6*7,3), np.float32)
objp[:,:2] = np.mgrid[0:7,0:6].T.reshape(-1,2)
# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.
for filename in calibration_images:
    calibrationimage = cv.imread(filename)
    gray = cv.cvtColor(calibrationimage, cv.COLOR_BGR2GRAY)
    # Find the chess board corners
    ret, corners = cv.findChessboardCorners(gray, (7,6), None)
    # If found, add object points, image points (after refining them)
    if ret == True:
        objpoints.append(objp)
        corners2 = cv.cornerSubPix(gray,corners, (11,11), (-1,-1), criteria)
        imgpoints.append(corners)
        # Draw and display the corners
        cv.drawChessboardCorners(calibrationimage, (7, 6), corners2, ret)
        cv.imshow('img', calibrationimage)
        cv.waitKey(500)
cv.destroyAllWindows()
ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
print (ret, mtx, dist, rvecs, tvecs)

#save all parameters in a dictionary (a map of key->value)
dictionary = {
    'ret': ret
}

# We need to convert all ndarrays to lists, because the json library cannot handle ndarrays.
# We do not use pickles, because they are unsafe and could be used to execute malicious code :(
dictionary['mtx'] = mtx.tolist()
dictionary['dist'] = dist.tolist()
dictionary['rvecs'] = [ndarray.tolist() for ndarray in rvecs]
dictionary['tvecs'] = [ndarray.tolist() for ndarray in tvecs]
dictionary['objpoints'] = [ndarray.tolist() for ndarray in objpoints]
dictionary['imgpoints'] = [ndarray.tolist() for ndarray in imgpoints]

#Write the dictionary to a json
with open('calibrationdata.json', 'w') as outfile:
    json.dump(dictionary, outfile)

