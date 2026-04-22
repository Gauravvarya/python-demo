my_str_1 = 'Hello'
my_str_2 = "World"

my_str_3 = """multiline string"""
my_str_4 = '''Another multiline string'''


msg = "It's a sunny day"
quote = 'she said, "Hello World!"'

msg = "It\'s a sunny day"
quote = 'She said,"Hello world!"'

my_str = 'Hello World'
print('Hello' in my_str)
print('hey' in my_str)
print('hi' in my_str)
print('e' in my_str)
print('f' in my_str)

#length
my_str = 'Hello world'
print(len(my_str))

#string position
my_str = 'hello world'
print(my_str[0]) #h
print(my_str[6]) #w

greeting = 'hi'
greeting = 'hello'
print(greeting) #hello

#greeting = 'hi'
#greeting[0] = 'h' #TypeError: 'str' object does not support item assignment

#String concatination
my_str_1 = 'hello'
my_str_2 = 'world'
str_plus_str = my_str_1 +''+ my_str_2
print(str_plus_str) #helloworld 

# error of concatenation of string and no.
name = 'Alice'
age = 30
#name_and_age = name + age
#print(name_and_age)
#
# F-string start with f
name = 'Alice' 
age = 26
name_and_age = f'My name is {name} and I am {age} years old.'
print(name_and_age)

num1 = 5
num2 = 10
print(f'The sum of {num1} and {num2} is {num1 + num2}')

