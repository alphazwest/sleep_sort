import random
from sleep_sort import Sleeper, ThreadSafeList


if __name__ == "__main__":

    # get a list of 20 random numbers in range [0, 100]
    nums = [random.choice(list(range(100))) for _ in range(20)]
    print("Starting Nums:", nums)

    # create a thread-safe list object
    sorted_list = ThreadSafeList()

    # keeps a reference to all threads
    threads = []

    # starts a Sleeper thread for each item in the numbers list
    for n in nums:
        # creates the thread
        sleeper = Sleeper(n, sorted_list)

        # starts the thread
        sleeper.start()

        # adds reference to thread to collection
        threads.append(sleeper)

    # waits on all threads to finish before exiting
    for thread in threads:
        thread.join()

    # display the resulting sorted items
    print("Sorted Nums:", sorted_list)
