import logging
import threading
import time


# logs messages with a delay in between
def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)


if __name__ == "__main__":

    # initialize logging stuff
    formatting = "%(asctime)s: %(message)s"
    logging.basicConfig(format=formatting, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")
    # creates the thread
    # executes target() with args given when started
    x = threading.Thread(target=thread_function, args=(1,), daemon=False)

    logging.info("Main    : before running thread")
    # starts the thread
    x.start()

    # logging.info("Main    : wait for the threads to finish")
    # forces the program to wait for the thread to finish
    # x.join()

    logging.info("Main    : all done")
