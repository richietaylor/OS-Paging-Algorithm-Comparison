# Paging.py README

This program simulates how three different page replacement algorithms work in the real world: 
       - First in First out (FIFO)
       - Least Recently Used (LRU)
       - Optimal Page Replacement (OPT)

It does this using a randomly generated string of integers (0-9)

## Running the Program

To run the program you enter the following command in the terminal:

```bash
python paging.py [number of pages]
```

The argument `number of pages` should be an integer value that determines the length of the reference string, a simulation of real computer pages.

You can also change the size of memory (pages that can be stored at once) in the main method using the variable named "size".


## Program Output

After running the program, the output will display the reference string and the number of page faults for each algorithm.

```bash
Reference String:
[4, 9, 4, 8, 2, 4, 4, 4, 4, 0, 1, 1, 9, 3, 7, 0, 3, 6, 8, 8]
FIFO 11 page faults.
LRU 11 page faults.
OPT 6 page faults.
```

In the above example, the reference string is a sequence of 20 pages (randomly generated between the values 0 and 9), also note the frame size is set to 7. The program output shows the number of page faults for each of the three algorithms. The OPT algorithm unsprisingly produces the least number of page faults.
