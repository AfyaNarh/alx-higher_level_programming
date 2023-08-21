#!/usr/bin/python3
""" 9-main """
from models.square importquare

if __name__ == "__main__":

    s1 =quare(5)
    print(s1)
    print(s1.area())
    s1.display()

    print("---")

    s2 =quare(2, 2)
    print(s2)
    print(s2.area())
    s2.display()

    print("---")

    s3 =quare(3, 1, 3)
    print(s3)
    print(s3.area())
    s3.display()

