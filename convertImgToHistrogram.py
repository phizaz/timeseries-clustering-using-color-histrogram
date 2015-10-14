import File
import skimage.io
import skimage.color
import os
import TimeElapsed
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
def convert_files_to_histograms():
    bucket_count = 256
    histograms = {}

    for color, file_names in file_list.items():
        print('working on:', color)
        histograms[color] = []

        for file_number, file_name in enumerate(file_names):
            print('percent:', file_number / len(file_names) * 100)

            image = skimage.io.imread(file_name)
            # convert to hsv
            hsv_image = skimage.color.convert_colorspace(image, 'RGB', 'HSV')

            # convert to histogram based on the H value
            def creating_histogram():
                return Histogram.Histogram.create_from_hsv(hsv_image, bucket_count)
            histogram, time_creating_histogram = TimeElapsed.TimeElapsed.measure(creating_histogram)
            histograms[color].append(histogram)

            print('creating a histogram:', time_creating_histogram)

    return histograms

histograms, time_creating_histograms = TimeElapsed.TimeElapsed.measure(convert_files_to_histograms)
print('time creating histograms total:', time_creating_histograms)

print('writing to json file')
File.File.save(histograms, '_histograms.json')