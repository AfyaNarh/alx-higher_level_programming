#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    result = tuple(first + second for first, second in zip(tuple_a, tuple_b))
    return result
