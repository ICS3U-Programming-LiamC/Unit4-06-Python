#!/usr/bin/env python3

# Created by: Liam Csiffary
# Created on: May 28, 2021
# This program lists a butt load of numbers, in the form of RGB numbers
# theres going to be way to many numbers itll probably crash my computer


# so that i can have the dramatic delay
import time


def main():
    # make sure all the counters are 0
    counterRed = 0
    counterBlue = 0
    counterGreen = 0

    # the delay and warning
    print("It may take a while to get through them all")
    print("starting in 3")
    time.sleep(1)
    print("starting in 2")
    time.sleep(1)
    print("starting in 1")
    time.sleep(1)
    # the blob of for loops, all the stuff happens here
    for counterRed in range(0, 256):
        for counterGreen in range(0, 256):
            for counterBlue in range(0, 256):
                print("{0}, {1}, {2}".format(counterRed,
                      counterGreen, counterBlue))


if __name__ == "__main__":
    main()
