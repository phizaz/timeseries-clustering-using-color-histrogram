# Time series classification on a hue histogram using kNN and Euclidean distance

This repository is made to be a part of "Converting Images to Time-series Data For Color Tone Classification" project to show that it works.

The details of that project will be given below.

Note: this repo contains impages retrived from google.com which may contain some kind of copyrights, we intend to use in an offline environtment only.

## Converting Images to Time-series Data For Color Tone Classification

### Introduction

Color tone classification has a cool application and is used widely nowadays. We can see its application in websites such as google.com and possibly many more search engines. The application is quite straightforward select a color and get results as a collection of images that mainly contain that color. Yet, this kind of application is not that hard to build. We will show that with converting the images to time-series data and using some techniques of time-series data mining, we can solve this task quite easily and quite accurately.

### Background

#### HSV color space
Normally, every image stored digitally has its way to represent pixels in that image i.e. RGB, a pixel is represented in 3-tuple of red, green and blue by which it can recall the true color of the pixel. In this case, it is represented using in 3-tuple of hue, saturation and value, actually it is just another way to describe a pixel.

We use HSV in this work because we mainly focus on color-tone classification. That means we do not want any kind of light condition, wether underexposure or overexposure, to interfere the color. In HSV, we simply can use its hue value to describe the color of a pixel alone. This will greatly ease out most of the difficulties.

### Converting images to hue-based histograms
The process consists of six steps described as follows:
1. Having an image of any kind.
2. Transform that image into a bitmap, say a two-dimensional array.
3. Convert each pixel of that array from RGB to HSV and take only the hue part of the result.
4. Create 256 hue-bins in which each pixel will be thrown according to the hue of the pixel and the label of the bin. A series of 256 hue-bins is for one image. This process is called binning
5. Normalize each series of the hue-bins so that the summation of the series is equal to 1.
6. Serialize each series of hue-bins. Now, we have a histogram to represent that image.

### Experiment
To show the proposed algorithm also works in real life condition, we conducted an experiment that used this algorithm in an image classification say color-tone classification.

We used kNN (k-nearest neighbor) as a classifier and used euclidean distance as a distance measure. (between a pair of histograms) We knew that the best k in kNN can be very subjective and might not be easy to find using theoretical analysis alone. Thus, we tried many k’s to see which one perform ed best.

In the experiment, we had 2 sets of data, first was training data and second was testing data. The training data set contained 150 image samples of three color tones, red green and blue, the number of each of which was 50. The testing data set contained 25 images of 8 red’s 8 green’s and 9 blue’s. There are no duplicate images, and the images can be of any kind from views to cartoon posters.

