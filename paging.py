# TYLRIC007 - Richard Taylor
# OS Assignment 1 - Paging Techniques

from random import randint, seed
import sys

# seed(69)


'''
First in first out algorithim 
    Parameters:
        size (int) : Frame size
        pages (int[]) : List of pages
    Returns:
        faults (int) : Number of faults
'''


def FIFO(size, pages):
    # keeps track of page faults
    faults = 0
    # keeps track of pages in memory
    frames = []

    # loop through all pages in reference string
    for x in range(len(pages)):
        # if our current page is not in "memory", add a fault and continue
        if pages[x] not in frames:
            faults += 1
            # This is to account for the first few pages
            if len(frames) < size:
                frames.append(pages[x])
            else:
                # swap out victim for new
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
    # keeps track of page faults
    faults = 0
    # keeps track of pages in memory
    frames = []

# loop through all pages in reference string
    for x in range(len(pages)):
        # if our current page is not in "memory", add a fault and continue
        if pages[x] not in frames:
            faults += 1
            # This is to account for the first few pages
            if len(frames) < size:
                frames.insert(0, pages[x])
            else:
                # swap out victim for new, keep most recently used to front of stack
                frames.insert(0, pages[x])
                frames.pop(-1)
        else:
            # move recently used to front of stack
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
    # faults keeps track of page faults
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
                        # find indices (poisitions) of all future references of items in memory
                        pos = seek.index(frames[y])
                    else:
                        # else set index to unreasonably high number so it will always be paged if it is referenced
                        pos = 99999999999
                    # victim page = page referenced futherest into the future (or never referenced again)
                    if pos > maximum:
                        maximum = pos
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

    # page size - user can manually set this from 1 to 7
    size = 7

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
