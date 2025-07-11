name = "Sanjay"
#print(name[0:4])    
#print(name[4:0])
#upper_case =name.upper() #change all letters into cappital letters
#print(upper_case) 
#lower_case =name.lower() #change all leters into smaller latters
#print(lower_case)
# print(name.count("a")) # count letter in name 
#print(name)
#print("my name is ",name)
#print ("name dtypes:-",type(name)) check the class of the words example- string, character,float, int
#print(name[0]) indexing
#print(name[2]) check the word no and print which no come at which placeor index 
#print(name[len(name)-1])
#name = "Sanjay"
#last = "YADAV"
#print(name.title())
#print(name.capitalize()) first letter capital other small
#print(last.capitalize())
#print(name+last) add two name
#Age = 22
#print(Age) print value of string




#>>>>>>>>>>>>>>>>>>>>>>>>>>> list>>>>>>>>>>>>>>
#lst = [1,2,3,4,5,7,8]
#print(lst)
#lst.reverse() print the list unti inverse
#lst.remove(2,3) remove no. from the list
#lst.pop()  remove somithing
#lst.append(100) add somthing
#lst.sort() sort the list
#print(lst.count(2)) count the number in the list
#copy_lst =lst.copy() copy the list 
#print(copy_lst) print the list
#print(lst[5]) print the 5th no from the list
#print ("mr first list:- ",lst)
#print("len of list:-",(lst))
#print("type of list:-",type(lst))
#print(lst[0:5]) print the number bstart from 0 and end with in next 5 digit

# HOMEWORK
#lst = [1,2,3,4,[5,6],7,8]
#print(lst[4][1])
# Complete

# <<<<<<<<<<<<<  Tupple  >>>>>>>>>>>>>>>>>

#tpl = (1,2,3,5,667,8, "sanjay", 9.1)
#print("my first tupple:-",tpl)
#print("len of tuple:- ",len(tpl))
#print("type of tuple:- ",type(tpl))

# indexing
#print(tpl[0])
#print(tpl[2])
#print(tpl[0:6])

# build
#a= 1,25,6,99,9,1,5,6,88,99,9,36
#print(a)
#print(type(a))
#print(len(a))

#a,b,c = (1,2,3)
#print(a)
#print(b)
#print(c)

#print("max of tuple",max(tpl))
#print("min of tupple",min(tpl))
#print("sum of tuple",sum(tpl))


#<<<<<<<<<<<<< Dictionary >>>>>>>>>>>>>>

#my_dict = {
 #   "name" : "Sanjay",## name,class,roll no., address are keys
   # "class": "4th year", ## sanjay,4th year,021220087ccse,haryana are values
   # "Roll number": "02101222087cCSE",
  #  "Address":"Haryana","name" : "Sanjay"

# "name":"Sanjay" item
#}

#print("my firts dict :-",my_dict)
#print("len of dict :-",len(my_dict))
#print("type of dict :-",type(my_dict))
#print(my_dict['name'])
#print(my_dict['class'])
#print(my_dict['Roll number'])
#print(my_dict['Address'])
#my_dict['Address']="Jaipur"
#print(my_dict)

#my_dict = {
   # "name" : "Sanjay",## name,class,roll no., address are keys
  #  "class": "4th year", ## sanjay,4th year,021220087ccse,haryana are values
  #  "Roll number": "02101222087cCSE",
  #  "Address":"Haryana","name" : "Sanjay"  # "name":"Sanjay" item

#}

#my_dict['branch']="CSE"
#print(my_dict)

#>>>>>>>>>>>>>> taST 1 >>>>>>>USE OF  UPDATE FUNCTION
# 5 EXAMPLE OF gaTE FUNCTION
# USE OF [] SQUARE BRACKET

#print(my_dict.keys())
#print(my_dict.values())
#print(my_dict.items())

#copy_dict =my_dict.copy()
#print(copy_dict)

#a = input("enter a number")
#b = input("enter a number")

#print (a*b)
#print(type(a))
#print(type(b))

#>>>>>>. Type Casting

# = input("enter a number")
#b = input("enter second number")
#print(a*b)

#lst = [1,2,3,4,5,88,6]
#print("this is my first list:-",lst)
#print("type of list",type(lst))
#tpl = tuple(lst)
#print("type of tuple",type(tpl))
#print("this is my first tuple:-",tpl)

#>>>>>>>>>>>> set
#my_set = {1,2,4,5,7,22,44,"Sanjay",1}
#print("this is my first set ",my_set)
#print("len of my set",my_set)
#print("type of set",type(my_set))

#>>>>>>Task
# my_set.union()
# my_set.intersection()
# my_set.difference()

#lst = list(my_set)

#>>>>>Operator by self

#lst.append(1000)
#print(set(lst))



#>>>>>>>>>.... TAsk >>>>>>>..
# update function 

#my_dict = {
 #   "name" : "Sanjay",## name,class,roll no., address are keys
  #  "class": "4th year", ## sanjay,4th year,021220087ccse,haryana are values
   # "Roll number": "02101222087cCSE",
    #"Address":"Haryana","name" : "Sanjay"  # "name":"Sanjay" item

#}

#new_data = {
 #   "name": "Sourab",
  #  "Class": "2nd",
   # "Roll number": "0212220041ccsse"
#}

#my_dict.update(new_data)
#print(my_dict)


## GATE FUNCTIONS

#def AND(a, b):
 #   return a and b
#print(AND(1, 1))               1

#def OR(a, b):
 #   return a or b
 #print(OR(1, 0))               1

#def NOT(a):
 #   return int(not a)

#print(NOT(1))                0  

#def NAND(a, b):
 #   return int(not (a and b))

#print(NAND(1, 1))            0

#def NOR(a, b):
#    return int(not (a or b))

#print(NOR(0, 0))             1

#def XOR(a, b):
 #   return a ^ b  

#print(XOR(1, 0))             1

#def XNOR(a, b):
#    return int(not (a ^ b))   

#print(XNOR(1, 1))        1

#set1 = {1, 2, 3, 4, 5}
#set2 = {3, 4, 5, 6}
#result = set1.union(set2)         {1, 2, 3, 4, 5, 6}
#result = set1.intersection(set2)  {3, 4, 5}
#result = set1.difference(set2)    {1, 2}
#print(result)






