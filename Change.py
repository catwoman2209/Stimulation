#File for Quick Change game code
import random


def get_total():
    return round(random.uniform(0.99, 199.99), 2)
def get_payment(total, size):
    return round(random.uniform(total, total + size), 2)
