#Created by Kamil Krawczyk
#03/04/2020

#Problem 3
#This program takes a list and outputs if the number 5 is in the list or not

def list_check():
  the_list = [1,2,4,23,34,5,7,2,1,9,8,7]

  for x in the_list:
    if(x == 5):
      print("The number 5 is in this list")


list_check()