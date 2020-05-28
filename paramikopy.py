import paramiko
import os
import pytz
from datetime import datetime
from pprint import pprint

today=datetime.now(tz=pytz.timezone('US/Eastern'))
os.chdir('C:/Users/KSP/Downloads')
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

hostnames=['3.84.239.85','100.25.37.82']
username='ec2-user'
key_filename='practice'  #To make this work converted ppk to openssh file format
port=22
#password='securepassword'
for hostname in hostnames:
    try:
        print(hostname)
        print("Memory,Cpu,Disk List Available As on ",str(today))
        ssh.connect(hostname, username=username,port=port,key_filename=key_filename)
        stdin,stdout,stderr=ssh.exec_command('free -mh')
        pprint(stdout.readlines())
        stdin,stdout,stderr=ssh.exec_command('df -ah')
        pprint(stdout.readlines())
        print('\n')
      
    except Exception as err:
        pprint(err) 
    ssh.close()