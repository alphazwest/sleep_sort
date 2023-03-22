# Sleep Sort
Are you *tired* of determining the time complexity of sorting algorithms? Are you *tired* of being asked which sorting algorithm is the best? Are you *tired* of wondering if your favorite programming language implements sorting in the most efficient manner?

If you answered "yes" to any of these questions then *Sleep Sort* is for you!

## Example Usage

```python  
import random
from sleep_sort import Sleeper, ThreadSafeList

# a list of 20 random integers in the range [0, 100]
nums = [6, 85, 7, 17, 85, 56, 73, 41, 3, 84, 65, 43, 61, 69, 91, 96, 72, 14, 52, 83]

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
print(sorted_list)
[3, 6, 7, 14, 17, 41, 43, 52, 56, 61, 65, 69, 72, 73, 83, 84, 85, 85, 91, 96]
```
**disclaimer**: The models, methods, and general approach seen here are overly complex for the sake of clarity.
