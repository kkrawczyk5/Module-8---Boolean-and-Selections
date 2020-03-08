#Created by Kamil Krawczyk
#03/04/2020

#Problem 2
#This program asks the user for two numbers and tells the user if the sum of the numbers is greater than, less than, or equal to 10.

def num_equation():
  print("Input the first number - ")
  x = int(input())
  print("Input the second number - ")
  y = int(input())

  num_calc = (x+y)

  if num_calc > 10:
    print(num_calc, " is greater than 10!")
  elif num_calc < 10:
    print(num_calc, "is less than 10!")
  elif num_calc == 10:
    print(num_calc, " is equal to 10!")


num_equation()
