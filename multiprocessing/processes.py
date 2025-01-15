import time
from threading import Thread


def do_cpu_work():
    print("Starting CPU work")
    x = 0
    for _ in range(10**6):
        x += 1
    print("Finished CPU work")