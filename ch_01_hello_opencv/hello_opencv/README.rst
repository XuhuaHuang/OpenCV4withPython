===========
HelloOpenCV
===========
OpenCV and Python first example.This first project loads an image from a specified path. Afterwards, this image is converted to grayscale.
Finally, the grayscale image is saved to a specified file. Additionally, the two images (both the original and the grayscale one) are shown. 

***************
Installation
***************
.. code:: python

   python setup.py install

*****************
Development setup
*****************
To install all development dependencies:

.. code:: python

   pip install -r requirements.txt

To run the tests (verbose):

.. code:: python

   python -m pytest -s -v hello_opencv_tests.py

***************
Usage example
***************
This example can be used as follows:

.. code:: python

   python hello_opencv.py

This script loads the image from "images/logo.png" and it is converted to grayscale, writing it in "images/gray_logo.png"
