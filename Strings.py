"""Three double quoted strings are mainly used for
multi line comment"""
'Single quotes can also be used'
"Double quotes can also be used"

#Representation of String 
#Declaring a variable , all variables should be lower case and aslo we can double underscore '_'in between variables
#Example: message,message_descrption,

message='Strings Lesson '

#print is a method to print out text
print(message)

#print(dir(message))   #Uncomment these when you want to see more deatils and how to use them
#print(help(str))
#print(help(str.replace))
"""There are some cases where strings can get apostrophes like String's Lesson,
 Here we use escape sequences or  Double quotes """
print('String\'s Lesson')
print("String's Lesson")

#There are some inbuilt methods for string we can take advantage of them
print(message.upper())
print(message.lower())

message = message.replace('s','z')
print(message)
print(message.find('z'))

print(len(message))
message_description='Finished'
#This is a way to format strings
print(f'{message}')
print( '%s is %s' % (message,message_description))

#Working with string concate and slicing
print(message[:])
print(message[0:])
print(message[:8])
print(message[2:8]) 
print(message[:-2]) 
print(message[-2:])