# TYLRIC007 - Richard Taylor
# OS Assignment 1 - Paging Techniques

from random import randint, seed
import sys

seed(420)


'''
First in first out algorithim 
    Parameters:
        size (int) : Frame size
        pages (int[]) : List of pages
    Returns:
        faults (int) : Number of faults
'''


def FIFO(size, pages):
    faults = 0
    frames = []

    for x in range(len(pages)):
        if pages[x] not in frames:
            faults += 1
            if len(frames) < size:
                frames.append(pages[x])
            else:
                frames.append(pages[x])
                frames.pop(0)
    return faults


'''
Least Recentely used algorithim 

    Parameters:
        size (int) : Frame size
        pages (int[]) : List of pages
    Returns:
        faults (int) : Number of faults

'''


def LRU(size, pages):
    faults = 0
    frames = []

    for x in range(len(pages)):
        if pages[x] not in frames:
            faults += 1
            if len(frames) < size:
                frames.insert(0, pages[x])
            else:
                frames.insert(0, pages[x])
                frames.pop(-1)
        else:
            frames.pop(frames.index(pages[x]))
            frames.insert(0, pages[x])

    return faults


''' 
Optimal page replacement algorithim 

    Parameters:
        size (int) : Frame size
        pages (int[]) : List of pages
    Returns:
        faults (int) : Number of faults

'''


def OPT(size, pages):
    #
    frames = []
    # var keeps track of page faults
    faults = 0

    # loop through all pages
    for x in range(len(pages)):
        if pages[x] not in frames:
            # page fault if frame not in memory
            faults += 1

            # first few pages coming in will not be memory
            if len(frames) < size:
                frames.append(pages[x])
            else:
                # creates a subset of all pages referenced in the future
                seek = pages[x:len(pages)]
                # the int referenced the futhurest in the future
                maximum = -1
                # index of victim page
                victim = -1

                for y in range(len(frames)):
                    if frames[y] in seek:
                        # find indices of all future references of items in memory
                        ind = seek.index(frames[y])
                    else:
                        # else set index to unreasonably high number so it will always be paged if it is referenced
                        ind = 99999999999
                    # victim page = page referenced futherest into the future (or never referenced again)
                    if ind > maximum:
                        maximum = ind
                        victim = frames[y]

                # remove victim page and add optimal page
                victimPos = frames.index(victim)
                frames.pop(victimPos)
                frames.append(pages[x])
    # returns number of faults
    return faults


def main():

    # command line argument sets the number of pages to be referenced in sequence
    pageLength = int(sys.argv[1])

    # page size - can be manually set from 1 to 7
    size = 3

    # Random number generator -
    # generates a list of random ints from 0 to 9
    pages = []
    print("Frame Size: ", size)
    print("Reference String: ")
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
