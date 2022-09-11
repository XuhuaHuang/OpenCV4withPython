"""
Testing OpenCV installation
Xuhua Huang
Aug 23, 2022
Execute the following in the terminal:
$ cd ./ch_01_hello_opencv/test_installation
$ python test_opencv_installation.py
"""

# import the necessary packages (in this case, OpenCV package)
import cv2

# Use the function cv2.imread() to read an image.
# The image should be in the working directory or a full path of image should be provided.
# load OpenCV logo image:
image = cv2.imread("./logo.png")

# Use cv2.cvtColor() to convert an image from one color format to another
# In this case we use cv2.cvtColor() to convert the loaded image to grayscale (BGR to GRAY):
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Use the function cv2.imshow() to show an image in a window.
# The window automatically fits to the image size.
# First argument is the window name.
# Second argument is the image to be displayed.
# Each created window should have different window names.
# Show original image:
cv2.namedWindow("OpenCV logo", cv2.WINDOW_KEEPRATIO)
cv2.imshow("OpenCV logo", image)
# Use the resizeWindow() to optimize the display.
# The first argument is the name of the named window.
cv2.resizeWindow("OpenCV logo", 200, 200)

# Show grayscale image:
cv2.namedWindow("OpenCV logo gray format", cv2.WINDOW_KEEPRATIO)
cv2.imshow("OpenCV logo gray format", gray_image)
cv2.resizeWindow("OpenCV logo gray format", 200, 200)

# cv2.waitKey() is a keyboard binding function.
# The argument is the time in milliseconds.
# The function waits for specified milliseconds for any keyboard event.
# If any key is pressed in that time, the program continues.
# If 0 is passed, it waits indefinitely for a key stroke.
# Wait indefinitely for a key stroke (in order to see the created window):
cv2.waitKey(0)

# To destroy all the windows we created call cv2.destroyAllWindows()
cv2.destroyAllWindows()
