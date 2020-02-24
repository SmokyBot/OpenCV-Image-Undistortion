import numpy as np
import cv2 as cv
import glob
import json
import os

#define path to images to be calibrated here
images = glob.glob('images/*.jpg')
#Folder where results are saved.
resultsFolder = 'results'

if not os.path.exists(resultsFolder):
    os.makedirs(resultsFolder)


#Read parameters from file:
with open('calibrationdata.json') as json_file:
    dictionary = json.load(json_file)
    mtx = np.array(dictionary['mtx'])
    dist = np.array(dictionary['dist'])
    rvecs = [np.array(rvec) for rvec in dictionary['rvecs']]
    tvecs = [np.array(tvec) for tvec in dictionary['tvecs']]
    objpoints = [np.array(list) for list in dictionary['objpoints']]
    imgpoints = [np.array(list) for list in dictionary['imgpoints']]

for imagename in images:
    image = cv.imread(imagename)
    h,  w = image.shape[:2]
    newcameramtx, roi = cv.getOptimalNewCameraMatrix(mtx, dist, (w,h), 1, (w,h))
    # undistort
    dst = cv.undistort(image, mtx, dist, None, newcameramtx)
    # crop the image
    x, y, w, h = roi
    dst = dst[y:y+h, x:x+w]
    head, tail = os.path.split(imagename)
    cv.imwrite(resultsFolder + '/' + tail + '.png', dst)
    mean_error = 0
    for i in range(len(objpoints)):
        imgpoints2, _ = cv.projectPoints(objpoints[i], rvecs[i], tvecs[i], mtx, dist)
        error = cv.norm(imgpoints[i], imgpoints2, cv.NORM_L2)/len(imgpoints2)
        mean_error += error
    print( "total error: {}".format(mean_error/len(objpoints)) )