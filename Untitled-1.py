# TYLRIC007 - Richard Taylor
# OS Assignment 1 - Paging Techniques

from random import randint
import sys


def FIFO(size, pages):
    # keep track of page faults
    faults = 0
    return faults


def LRU(size, pages):
    # keep track of page faults
    faults = 0
    return faults


def OPT(size, pages):
    # keep track of page faults
    faults = 0
    return faults


def main():

    # command line argument sets the number of pages to be referenced in sequence
    pageLength = int(sys.argv[1])

    # page size - can be manually set from 1 to 7
    size = 7

    # Random number generator -
    # generates a list of random ints from 0 to 9
    pages = []
    for x in range(pageLength):
        pages.append(randint(0, 9))
    print(pages[:])

    # call to our paging algorithms
    print("FIFO", FIFO(size, pages), 'page faults.')
    print('LRU', LRU(size, pages), 'page faults.')
    print('OPT', OPT(size, pages), 'page faults.')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python paging.py [number of pages]")
    else:
        main()
