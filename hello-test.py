import unittest
from hello import hello
class testHello(unittest.TestCase):
     def testhello(self):
         self.assertEqual(hello('prakash'),"hello prakash") 
if __name__== '__main__':
      unittest.main()