import time

class TimeElapsed:

    @staticmethod
    def measure(fn):
        start_time = time.process_time()
        # run the targetted function
        result = fn()
        time_lapse = time.process_time() - start_time
        return result, '%.5f' % time_lapse
