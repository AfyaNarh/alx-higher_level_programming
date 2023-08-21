#!/usr/bin/python3
""" 13-main """
from models.square importquare

if __name__ == "__main__":

    s1 =quare(10, 2, 1)
    print(s1)
    s1_dictionary = s1.to_dictionary()
    print(s1_dictionary)
    print(type(s1_dictionary))

    s2 =quare(1, 1)
    print(s2)
    s2.update(**s1_dictionary)
    print(s2)
    print(s1 == s2)

