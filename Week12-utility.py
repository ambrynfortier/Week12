#Ambryn Fortier
#CSCI 102
#Week 12 A

def PrintOutput(string):
    print("OUTPUT " + string)
    return

def LoadFile(filename):
    readme = open(filename, 'r')
    lines=readme.readlines() 
    return lines


def UpdateString(s1, s2, ind):
    newstring = s1[0:ind] + s2 + s1[ind+1: len(s1)]
    print("OUTPUT " + newstring)
    
    return 

def FindWordCount(lt, st):
    count = 0
    for i in lt:
        if lt(i) == st:
            count = count + 1;
    return

#def ScoreFinder(players):
    #return

#def Union(list1,list2):
    #return

#def Intersection(list1,list2):
    #return

#def Notln(list1,list2):
    #return


