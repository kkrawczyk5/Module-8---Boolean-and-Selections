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