import skimage.io
import skimage.color
import os
import TimeLapse
import Histogram

# get file names
training_path = "_training_data"
base_colors = ['red', 'green', 'blue']

file_list = {}
for color in base_colors:
    current_path = os.path.join(training_path, color)
    file_list[color] = []
    for file_name in os.listdir(current_path):
        current_path_with_file = os.path.join(current_path, file_name)
        # this is a file
        if os.path.isfile(current_path_with_file):
            file_list[color].append(current_path_with_file)

print("file_list:", file_list)


# convert files to histogram
bucket_count = 256
histograms = []
for color, file_names in file_list.items():
    for file_name in file_names:
        image = skimage.io.imread(file_name)
        # convert to hsv
        hsv_image = skimage.color.convert_colorspace(image, 'RGB', 'HSV')

        # convert to histogram based on the H value
        histogram = None
        def creating_histrogram():
            global histogram
            histogram = Histogram.Histogram.createFromHSV(hsv_image, bucket_count)
        time_creating_histogram = TimeLapse.TimeLapse.measure(creating_histrogram)


        histograms.append(histogram)
        print('time_creating_histogram: ', time_creating_histogram)
        print('histogram:', histogram)
