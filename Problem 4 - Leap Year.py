#Created by Kamil Krawczyk
#03/04/2020

#Problem 4
#This program calculates if a given year is a leap year or not

def leap_year(year):
  if year % 4 == 0 and year % 100 != 0:
    return(True)
  elif year % 100 == 0 and year % 400 == 0:
    return(True)
  else:
    return(False)

print (leap_year(2020))