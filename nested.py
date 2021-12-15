#!/usr/bin/env python3

# Created by: Abdul Basit
# Created on: Dec 2021
# This program uses nested loops


def main():
    # this function uses nested loops

    counter1 = 0
    counter2 = 0
    counter3 = 0

    # process + output
    for counter1 in range(256):
        for counter2 in range(256):
            for counter3 in range(256):
                print("RGB({},{},{})".format(counter1, counter2, counter3))


if __name__ == "__main__":
    main()
