import threading


def task1():
   
    for i in range(1, 4):
        print("Task 1 - Counting:", i)


def task2():
   
    for i in range(1, 4):
        print("Task 2 - Counting:", i)


def task3():
    
    for i in range(1, 4):
        print("Task 3 - Counting:", i)


t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)
t3 = threading.Thread(target=task3)


t1.start()
t2.start()
t3.start()


t1.join()
t2.join()
t3.join()


print("All tasks completed!")
