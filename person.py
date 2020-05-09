class Person:
     def  __repr__(self):
         return 'Person(firstname=%s,lastname=%s,task=%s)' % (self.first,self.last,self.task)
     def __init__(self,firstname,lastname,task='worker'):
         self.first=firstname
         self.last=lastname
         self.task=task
         
p=Person('Prakash','Kokkiligadda')
print(p)
