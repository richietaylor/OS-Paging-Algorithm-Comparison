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

                    # add new page into memory
                    frames = frames[:count] + [pages[x]] + frames[count:]
                    refBits = refBits[:count] + [0] + refBits[count:]
                    replaced = True

                    count += 1

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
    # keep track of page faults
    faults = 0
    frames = []

    # loop through the pages
    for x in range(len(pages)):
        if pages[x] not in frames:
            # page fault since the page is not in memory
            faults += 1

            # this is to account for the first few pages
            if len(frames) < size:
                frames.append(pages[x])
            else:
                # create a subset of all future referenced pages
                seek = pages[x:len(pages)]

                # the int used futherest in the future
                maxx = -1
                # the index of the frame to be paged
                victim = -1

                for y in range(len(frames)):
                    if frames[y] in seek:
                        # find indices of all future references of items in memory
                        ind = seek.index(frames[y])

                    else:
                        # set index (ind) ridicoulsy high so if an int is never used again, it will always be paged
                        ind = 10000000000

                    # find the page that will be used the latest, or not at all
                    if ind > maxx:
                        maxx = ind
                        victim = frames[y]

                # page the victim frame out the stack, add recently referenced int
                vicpos = frames.index(victim)
                frames.pop(vicpos)
                frames.append(pages[x])

    return faults


def main():

    # command line argument sets the number of pages to be referenced in sequence
    pageLength = int(sys.argv[1])

    # page size - can be manually set from 1 to 7
    size = 4

    # Random number generator -
    # generates a list of random ints from 0 to 9
    pages = []
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
