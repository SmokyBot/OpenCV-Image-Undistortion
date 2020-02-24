Requires a function python 3 installation.
https://www.python.org/downloads/

Requires the cv2 library https://pypi.org/project/opencv-python/
Can be installed by executing: pip install opencv-python



calculateCalibrationParameters.py:
Calculates the calibration parameters based on the images in the calibration folder ('calibration/*.jpg'), can be changed. 
Writes the result in the calibrationdata.json file

undistortImages.py:
Requires an existing calibrationdata.json file
Iterates over all jpg images in the images folder ('images/*.jpg'), can be changed, undistorts them based on the parameters, and then writes the undistorted .png files to the results folder. 


Test images thanks to OpenCV Camera Calibration.