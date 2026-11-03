
import gc
import tracemalloc
import time


class Node:
    def __init__(self):
        self.reference = None


tracemalloc.start()


def create_cycles(number):
    for i in range(number):
        # Create two objects
        a = Node()
        b = Node()

        # Create a reference cycle
        a.reference = b
        b.reference = a


create_cycles(10000)


current_before, peak_before = tracemalloc.get_traced_memory()

print("Memory before GC:", round(current_before / 1024, 2), "KB")

start_time = time.perf_counter()


collected = gc.collect()

gc_time = time.perf_counter() - start_time


current_after, peak_after = tracemalloc.get_traced_memory()


print("Objects collected:", collected)

print("Memory after GC:", round(current_after / 1024, 2), "KB")

print("Peak traced memory:", round(peak_after / 1024, 2), "KB")

print("GC execution time:", round(gc_time, 6), "seconds")

tracemalloc.stop()
