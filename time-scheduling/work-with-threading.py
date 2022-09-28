import time, datetime, threading

# Rather than having all of your code wait until the time.sleep() function finishes, you can execute
# the delayed or scheduled code in a separate thread using Python’s threading module. The separate
# thread will pause for the time.sleep calls. Meanwhile, your program can do other work in the
# original thread. To make a separate thread, you first need to make a Thread object by calling
# the threading.Thread() function.

some_time = datetime.datetime.now()
print(some_time)

# 1st thread
print("START OF PROGRAM.")


# define a function to use in a new thread.
def take_nap():
    time.sleep(5)
    print("WAKE UP!!!!!!!!")


# creating a Thread object, calling threading.Thread() and passing it the keyword argument which is the
# function you want to call in the new thread
threading_obj = threading.Thread(target=take_nap)

# calling threading_obj.start() to create the new thread and start executing the target function in
# the new thread.
# 2nd thread
threading_obj.start()

print("END OF PROGRAM.")

# A Python program will not terminate until all its threads have terminated.
