#Created by Kamil Krawczyk
#03/08/2020

#Problem 5.3
#This program looks at the required items needed to complete a tasks and outputs if it can or cannot be done


def write_a_book():

  item_list = ["pan", "paper", "idea", "rope", "groceries"]
  debuff_list = ["slow"]
  
  if "pen" in item_list:
    if "paper" and "idea" in item_list and "confusion" not in debuff_list:
      print("You have met all of the requirements to write a book. Congratulations!")
    else:
      print("Sorry, but you did not have the requiremets to write a book. You are missing 'pen' ")
  else:
    print("Sorry, but you did not have the requiremets to write a book. You are missing 'pen' ")


write_a_book()