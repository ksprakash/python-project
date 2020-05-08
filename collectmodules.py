
# A way to write a regular tuple 

x,y,z=(1,2,'similar')
print(x,y,z)

user=('bob','coder')
print(f'{user[0]} is a {user[1]}')

for i in user:
    print(i)

print(type(user))

from collections import namedtuple
# Way to go for namedtuple

User=namedtuple(typename='User',field_names='name role')

student =User(name='Prakash',role='Student')

print(f"{student.name} is a {student.role}")


from collections import defaultdict
users={'bob': 'coder'}
users['bob']
users.get('prakash') is None

user_dict ={('bob',1),('prakash',3),('bob',2),('prakash',4), ('bob',3),('prakash',5), ('bob',4),('prakash',6), ('bob',5),('prakash',7), ('mike',10)}

challenges=defaultdict(list)
for name, challenge in user_dict:
    challenges[name].append(challenge)
print(challenges)
print(user_dict)