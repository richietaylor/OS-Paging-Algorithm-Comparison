# TYLRIC007 - Richard Taylor
# OS Assignment 1 - Paging Techniques

from random import randint
import sys


'''
First in first out algorithim 
    Parameters:
        size (int) : Frame size
        pages (int[]) : List of pages
    Returns:
        faults (int) : Number of faults
'''


def FIFO(size, pages):
    # page frame
    frames = []
    # num page faults
    faults = 0

    # populates the frames with pages
    for x in range(size):
        if pages[x] not in frames:
            faults += 1
        frames = [pages[x]] + frames

    # loop through the rest of the array
    for x in range(size, len(pages)):
        # if the next "page" is not in the "memory", activate a page fault
        if pages[x] not in frames:
            faults += 1
            # this shifts the elements by one unit to the right
            frames = [pages[x]] + frames
            frames.pop()
    # returns number of faults
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

    # this int keeps track of the page faults
    faults = 0

    frames = []
    # this array (or stack) sits parallel to the main "stack"
    refBits = []

    # count - keeps track of victim frame
    count = 0
    # iterate throuhg page list
    for x in range(len(pages)):

        # reseting count - keeps it looking for victim page
        if count > size-1:
            count = 0

        # if page in frame stack set refbit to one to let alg know it is receently used
        if pages[x] in frames:
            pos = frames.index(pages[x])
            refBits[pos] = 1

        else:
            # fill up tge frame list for the few instancesto fill frames
            if len(frames) < size:
                frames.append(pages[x])
                refBits.append(0)

            # keep going through the reference bits, until you find a victim page and replace its
            replaced = False
            while replaced == False:

                # reset count to keep it keeping track of which page to check for replacement next
                if count > size-1:
                    count = 0

                # if the potential victim page has a reference bit of 1, set it to zero and move on
                if refBits[count] == 1:
                    refBits[count] = 0
                    count += 1

                    # reset count to keep it keeping track of which page to check for replacement next
                    if count > size-1:
                        count = 0

                else:
                    # remove the victim page
                    faults += 1
                    frames.pop(count)
                    refBits.pop(count)

                    # add a new page into "memory"
                    frames = frames[:count] + [pages[x]] + frames[count:]
                    refBits = refBits[:count] + [0] + refBits[count:]
                    replaced = True

                    count += 1
    # returns number of faults
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
    size = 4

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
