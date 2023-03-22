from threading import Thread, Lock
import time
from typing import Any


class ThreadSafeList(list):
    """
    An object that encapsulates a list object and provides methods to add items
    in a thread-safe manner.
    """
    def __init__(self, *args, **kwargs):
        super(ThreadSafeList, self).__init__(*args, **kwargs)

        # the lock used to ensure thread-safety
        self.lock = Lock()

    def append(self, item: Any) -> None:
        """
        Overrides the default list <append> method to first acquire the lock
        then adds an item to the collection.
        Args:
            item: Numeric object to be added to the collection.
        """
        with self.lock:
            super().append(item)


class Sleeper(Thread):
    """
    Object model for a worker thread that sleeps for a specified time, then
    adds its item to the shared output container.
    """
    def __init__(self, num: int, output: ThreadSafeList):
        super(Sleeper, self).__init__()

        # the value to be sorted
        self.num = num

        # reference to the output container
        self.output = output

    def run(self) -> None:
        """
        Implements the abstract method to define this object's behavior when the
        thread.start() method is called.
        """
        # sleeps for a period, in seconds, proportional to 1/100th of the value
        # Note: higher values start causing issues with wait times being too short.
        time.sleep(self.num / 100)

        # adds the value to the shared output list
        self.output.append(self.num)
