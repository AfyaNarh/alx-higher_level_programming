#!/usr/bin/python3
""" 10-main """
from models.square importquare

if __name__ == "__main__":

    s1 =quare(5)
    print(s1)
    print(s1.size)
    s1.size = 10
    print(s1)

    try:
        s1.size = "9"
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

