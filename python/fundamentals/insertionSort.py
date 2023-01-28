
list= [12,11,13,5,6 ]
def insertionsort(anylist):
    for i in range (1,len(anylist)):
        key = anylist[i]
        j = i-1
        while j >=0 and key < anylist[j]:
            anylist[j+1] = anylist[j]
            j-=1
        anylist[j+1] = key
    sortedlist = [] 
    for i in range (len(anylist)):
        sortedlist.append(anylist[i])
    print(anylist)

insertionsort(list)
