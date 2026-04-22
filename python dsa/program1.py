#Datatypes in python
name = "john Doe" #python knows its string
int = 25 #python knows its a integer
#Integer
my_integer_var = 10
print('Interger:',my_integer_var) #Integr:10
#float
my_float_var = 4.50
print('float:', my_float_var)#float = 4.50
# #string
my_string_var = 'hello'
print('String:',my_string_var)#String:hello
#boolean
my_boolean_var = True
print('Boolean:',my_boolean_var)#Boolean
#set
my_set_var = {7,'hello',8.5}
print('set',my_set_var)
#Disctionary(collection of key value pairs)
my_dict_var = {'name':'Alice','age':24}
print('Disctionary:',my_dict_var)
#tuple
my_Tuple_var = (7,'apple',6.5)
print('Tuple:', my_Tuple_var)
#Range
my_range_var = range(5)
print('Range:', my_range_var)
my_list_var = [22, 'helloworld',3.24,True]
print('List:', my_list_var)
my_none_var = None
print('None:', my_none_var)
my_none_var = None
print(type(my_none_var))
# #isinstance
isinstance('Hello world',str)

import random
# list = [1,2,3,4,5]
# random.shuffle(list)
# print(list)
print(random.randint(0,5))