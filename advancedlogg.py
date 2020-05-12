import logging
logger=logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter=logging.Formatter('%(created)f: %(filename)s:%(funcName)s:%(levelname)s:%(message)s')
file_handler=logging.FileHandler('log.txt')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

class Hero:
   def __init__(self,first,last):
       self.firstname=first
       self.lastname=last
       self.email=self.firstname+"."+self.lastname+"@gmail.com"
       self.fullname=self.firstname+","+self.lastname
       logger.info("Created Employee: {}:{}".format(self.fullname,self.email))


emp1=Hero("Prakash","kokkiligadda")
emp2=Hero("Ravi","Kokkiligadda")