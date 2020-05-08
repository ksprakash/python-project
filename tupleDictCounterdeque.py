from collections import namedtuple,defaultdict,Counter,deque

user=('Bob','coder')
print(user[0] +" is a " +user[1])

User=namedtuple(typename='User',field_names='name role')
student1=User(name='prakash',role='teamleader')
student2=User(name='Sai', role='Unpredictable')
print(student1.name,student1.role,student2.name,student2.role)


Users={'bob' : 'coder'}

Users['bob']
print(Users.get('bob'))
print(Users.get('Prakash')) 

challenges_done={('bob',1),('bob',10),('prakash',1)}

challenges=defaultdict(list)
for name, challenge in challenges_done:
    challenges[name].append(challenge)
print(challenges)

words="""A text file is a computer file that only contains text and has no special formatting such as bold text, italic text, images, etc. With Microsoft Windows computers text files are identified with the . txt file extension, as shown in the example picture.""".split()
print(words)

common_words=Counter(words).most_common(5)
print(common_words)

D=defaultdict(int)
for word in words:
    D[word] += 1
print(D)
