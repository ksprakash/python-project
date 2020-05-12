import logging
format='%(created)f: %(filename)s:%(funcName)s:%(levelname)s:%(message)s'
logging.basicConfig(filename='logs.log',level=logging.INFO,format=format)
class Hero:
   def __init__(self,first,last):
       self.firstname=first
       self.lastname=last
       self.email=self.firstname+"."+self.lastname+"@gmail.com"
       self.fullname=self.firstname+","+self.lastname
       logging.info("Created Employee: {}:{}".format(self.fullname,self.email))


emp1=Hero("Prakash","kokkiligadda")
emp2=Hero("Ravi","Kokkiligadda")