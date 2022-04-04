from time import sleep

def ticker(interval: float):
    i = 0
    while True:
        yield i
        i += 1
        sleep(interval)
        