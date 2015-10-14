import math
import numpy

class Histogram:

    @staticmethod
    def createFromHSV(hsv_image, histogram_size):
        # convert to histogram based on the H value
        pixel_count = hsv_image.size
        histogram = [0 for i in range(histogram_size)]
        for row_number, row in enumerate(hsv_image):
            # print('progress:', row_number / hsv_image.shape[0] * 100)
            for col in row:
                # get hue value
                h = col[0]

                scaled_h = h * histogram_size
                target_bucket_number = int(math.floor(scaled_h))

                histogram[target_bucket_number] += 1

        # normalize histogram
        for bucket_number in range(histogram_size):
            histogram[bucket_number] /= pixel_count

        # convert to ndarray
        histogram = numpy.array(histogram)

        return histogram
    