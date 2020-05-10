tuple=(1,2,3,4,5,6)

print(tuple)
x=1
for item in tuple:
    print(item,x)
    x +=1

#tuples can never be changed 

tupl=tuple
tupl1=()
lis=list()
lis1=[]
dict={}
set=set()

setlist={1,2,3,4,5,6,7,8,9,6,5,4,5,5,5,7,6,4,1}
print(setlist)
setlist1={"hello","world",2,3,4,5,0}
print(setlist.difference(setlist1))
print(setlist.intersection(setlist))
print(setlist.union(setlist1))