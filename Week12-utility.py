#Ambryn Fortier
#CSCI 102
#Week 12 A


def PrintOutput(string):
    print("OUTPUT " + string)
    return

def LoadFile(filename):
    readme = open(filename, 'r')
    for line in readme.strip().split("\n"):
        print line

    return

def UpdateString(s1, s2, ind):
    s1(ind) = s2
    return

def FindWordCount(lt, st):
    count = 0
    for i in lt:
        if lt(i) = st
            count = count + 1;
    return
