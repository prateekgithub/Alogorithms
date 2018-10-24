#!python

def tower_of_hanoi(numOfDisks, startPeg=1, endPeg=3):
    if numOfDisks:
        tower_of_hanoi(numOfDisks-1, startPeg, 6-startPeg-endPeg)
        print("Move disk %d from peg %d to peg %d"%(numOfDisks, startPeg, endPeg))
        tower_of_hanoi(numOfDisks-1, 6-startPeg-endPeg, endPeg)

tower_of_hanoi(numOfDisks=4)
