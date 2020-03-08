#Created by Kamil Krawczyk
#03/08/2020

#Problem 5.2
#This program looks at the required items needed to complete a tasks and outputs if it can or cannot be done



def cook_a_meal():

  item_list = ["pan", "paper", "idea", "rope", "groceries"]
  debuff_list = ["slow"]

  if "pan" and "groceries" in item_list and "small" not in debuff_list:
    print("You have met all of the requirements to cook a meal. Congratulations!")
  else:
    print("Sorry, but you do not meet the requirements to cook a meal.")


cook_a_meal()