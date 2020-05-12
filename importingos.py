import os
import datetime
print(os.getenv('OS'))
print(os.environ.get('PATH'))


print(os.chdir('D:/VMDK'))
print(os.getcwd())

#To find out a directory exists or file exists os.path.isfile or os.path.isdir
print(os.path.isfile('../Education/python/test.txt'))
print(os.listdir())

print(os.stat('../Education/python/test.txt'))


#To get a size or date propely go for os.stat
timestamp=os.stat('../Education/python/test.txt').st_ctime
print(datetime.datetime.fromtimestamp(timestamp))


#os.walk() provides a tuple including 3 values dirpath,dirname, filename

for dirpath,dirname,filename  in os.walk("D:/Education"):
       print(dirpath)
       print(dirname)
       print(filename) 

