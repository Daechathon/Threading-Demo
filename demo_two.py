import concurrent.futures
import logging
from demo_one import thread_function
import time


# example for race issues
class TheSenate:
    def __init__(self):
        self.value = 0

    def update(self, name):
        logging.info('Thread %s: starting update', name)

        # make a copy of the value
        local_copy = self.value

        # alter the copy
        local_copy += 1

        # reassign the value after a delay
        time.sleep(0.1)
        self.value = local_copy

        logging.info('Thread %s: finishing update', name)


def init_emperor():
    palpatine = TheSenate()
    logging.info('Testing update. Starting value is %d.', palpatine.value)
    return palpatine


if __name__ == '__main__':
    # initialize logging
    formatting = '%(asctime)s: %(message)s'
    logging.basicConfig(format=formatting, level=logging.INFO, datefmt='%H:%M:%S')

    # func_to_execute = thread_function

    func_to_execute = TheSenate.update
    palpatine = init_emperor()

    # number of threads
    workers = 2

    # 'with' forces a join() on each thread in the pool
    # this is nicer for running lots of threads
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as execute_order_66:
        # tells each thread to do the function
        # execute_order_66.map(func_to_execute, range(workers))

        # tells each thread to k̶i̶l̶l̶ ̶t̶h̶e̶ ̶j̶e̶d̶i̶  update the value cause a race issue
        for i in range(workers):
            execute_order_66.submit(palpatine.update, i)

    logging.info('Testing update. Ending value is %d.', palpatine.value)
