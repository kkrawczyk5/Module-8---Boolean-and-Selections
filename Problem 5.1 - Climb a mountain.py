#Created by Kamil Krawczyk
#03/08/2020

#Problem 5.1 
#This program looks at the required items needed to complete a tasks and outputs if it can or cannot be done



def climb_a_mountain():
  
  item_list = ["pan", "paper", "idea", "rope", "groceries"]
  debuff_list = ["slow"]
  
  if "rope" and "coat" and "first aid kit" in item_list and "slow" not in debuff_list:
    print("You have met all of the requirements to climb this mountain. Congratulations!")
  else:
    print("Sorry, you do not meet the requirements to climb this mountain :(")




climb_a_mountain()

#characterInventory = ["pan","paper","idea","rope","groceries"]
#characterStat = ["slow"]

#def task(characterInventory,characterStat):
#    if "rope" in characterInventory and "coat" in characterInventory and "first_aid_kit" in characterInventory:
#        if "slow" in characterStat:
#            print("Cannot climb a mountain while slow!")
#        else:
#            print("Prepared to climb a mountain!")
#    else:
#        print("Not equipped to climb a mountain!")
        
#    if "pan" in characterInventory and "groceries" in characterInventory:
#        if "small" in characterStat:
#           print("Cannot cook a meal while small!")
#        else:
#            print("Prepared to cook a meal!")
            
#    else:
#        print("Not equipped to cook a meal!")
#    if "pen" in characterInventory and "paper" in characterInventory and "idea" in characterInventory:
#        if "confusion" in characterStat:
#            print("Cannot write a book while confused!")
#        else:
#            print("Prepared to write a book!")
#    else:
#        print("Not equipped to write a book!")
        
#    return()
#task(characterInventory, characterStat)
