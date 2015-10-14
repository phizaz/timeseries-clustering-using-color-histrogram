import time

class TimeLapse:

    @staticmethod
    def measure(fn):
        start_time = time.process_time()
        # run the targetted function
        fn()
        time_lapse = time.process_time() - start_time
        return '%.5f' % time_lapse
