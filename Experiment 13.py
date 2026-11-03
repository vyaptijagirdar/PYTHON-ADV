import threading

# Step 2: Define the first task
def task1():
    # Print messages to show that Task 1 is running
    for i in range(1, 4):
        print("Task 1 - Counting:", i)

# Step 3: Define the second task
def task2():
    # Print messages to show that Task 2 is running
    for i in range(1, 4):
        print("Task 2 - Counting:", i)

# Step 4: Define the third task
def task3():
    # Print messages to show that Task 3 is running
    for i in range(1, 4):
        print("Task 3 - Counting:", i)

# Step 5: Create separate threads for the three tasks
t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)
t3 = threading.Thread(target=task3)

# Step 6: Start all threads
# start() allows each thread to begin execution.
t1.start()
t2.start()
t3.start()

# Step 7: Wait until all threads finish
# join() prevents the main program from finishing too early.
t1.join()
t2.join()
t3.join()

# Step 8: Print the final message
print("All tasks completed!")
