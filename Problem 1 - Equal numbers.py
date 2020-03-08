#Created by Kamil Krawczyk
#03/04/2020

#Problem 1
#This program asks the user for two numbers and tells the user if the two numbers are exual or not.

def equal_num():
  print("Input the first number - ")
  x = int(input())
  print("Input the second number - ")
  y = int(input())
  if x == y:
    print("Those two numbers are equal!")
  else:
    print("Those two numbers are not equal")


equal_num()