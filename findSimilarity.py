import File
import Histogram
import skimage.io
import skimage.color
import TimeLapse
import os


training_histograms = File.File.open('_histograms.json')
bucket_count = 256
n_for_classify = 7

def classify_by_n(n, data):
    bucket = {
        'red': 0,
        'green': 0,
        'blue': 0
    }

    for i in range(0,n):
        bucket[data[i][1]] += 1

    M = -1
    for color, count in bucket.items():
        if count > M:
            max_color = color
            M = count

    return max_color

def finding_distance_by_euclidiean_method(data1, data2):
    square_distance = 0

    for index in range(len(data1)):
        square_distance += (data1[index]-data2[index])*(data1[index]-data2[index])

    return square_distance

def cal_all_distance(data):
    distance = []
    index = 0

    for color, trainingSet in training_histograms.items():
        for each_training in trainingSet:
            dis = finding_distance_by_euclidiean_method(each_training, data)
            distance.append((dis, color))
            index = index + 1;

    sorted_dis = sorted(distance, key=lambda tup: tup[0])    

    return sorted_dis

# get file names
testing_path = "_testing_data"

file_list = []
current_path = os.path.join(testing_path)

for file_name in os.listdir(current_path):
    current_path_with_file = os.path.join(current_path, file_name)
    # this is a file
    if os.path.isfile(current_path_with_file):
        file_list.append(current_path_with_file)

print("file_list:", file_list)

# convert files to histogram
histograms = []
for file_name in file_list:
    image = skimage.io.imread(file_name)
    # convert to hsv
    hsv_image = skimage.color.convert_colorspace(image, 'RGB', 'HSV')

    # convert to histogram based on the H value
    histogram = None    
    histogram = Histogram.Histogram.create_from_hsv(hsv_image, bucket_count)
    distance_with_color = cal_all_distance(histogram)
    final_color = classify_by_n(n_for_classify, distance_with_color)

    print ('FILE NAME: ',file_name, final_color)

