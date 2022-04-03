from time import sleep

def ticker(interval: float):
    while True:
        sleep(interval)
        yield