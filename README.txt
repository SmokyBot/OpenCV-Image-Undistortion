Author: Michael Debenjak

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


To calibrate (If you haven't generated the calibrationdata.json for your camera yet):
Put your calibration images into the calibration folder inside the project folder.

1. Open the command line
2. Navigate to the project folder
cd /path/to/project/folder
3. run the calibration script
python calculateCalibrationParameters.py
4. calibrationdata.json file is generated inside the project folder.


To undistory (requires existing calibrationdata.json for your camera):
Put your images into the images folder inside the project folder.

1. Open the command line
2. Navigate to the project folder
cd /path/to/project/folder
3. run the undistortion script
python undistortImages.py
4. a new "results" folder appears in the project folder with the undistorted images inside.

Test images thanks to OpenCV Camera Calibration.

