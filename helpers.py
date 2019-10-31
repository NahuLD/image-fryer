import os

import numpy


# return the length of vector v
def length(v):
    return numpy.sqrt(numpy.sum(numpy.square(v)))


# returns the unit vector in the direction of v
def normalise(v):
    return v / length(v)


def random_file(path):
    return path + numpy.random.choice(os.listdir(path))