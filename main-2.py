#by yaheli
itemlist = ["Ray Gun and Futuristic Armor", "The Mysterious Red Button", "The Lightsaber and Heavy Metal Armor"]

def NumItems(num = itemlist):
  return len(num)

def weapon(choice, weapons = itemlist):
  if choice == str(itemlist[0]):
    return str(itemlist[0])
  elif choice == str(itemlist[1]):
    return str(itemlist[1])
  elif choice == str(itemlist[2]):
    return str(itemlist[2])
  else:
    print("Invalid choice, try again.")
    choice_6()

def listItems(stuff = itemlist):
  for i in stuff:
    print(i)

def start_game():
  print("You are Mbugwa, a farmer living in a small village in Africa.")
  print("One day, while tending to your fields, you are suddenly kidnapped by a group of aliens who are huge fans of     Imagine Dragons.")
  print("You are taken to their spaceship and tortured with       nonstop Imagine Dragons music.")
  start_menu()
  

def start_menu():
  start = input("Can you escape and make it back home safely? (ansewer Y/N) ")
  if start == "Y":
    choice_1()
  elif start == "N":
    print("Ok then, come back when you feel like playing.")
    exit()
  else:
    print("Invalid choice, please remember to answer with a capital letter.")
    start_menu()

def restart():
  print("Thanks for playing! Please leave feedback in the comment section!")
  start = input("Do you want to play again? (ansewer Y/N) ")
  if start == "Y":
    choice_1()
  elif start == "N":
    print("Ok then, come back when you fe el like playing.")
    exit()
  else:
    print("Invalid choice, please remember to answer with a capital letter.")
    restart()

def choice_1():
  print("You are locked in a small room on the spaceship, with no apparent way out.")
  print("Do you try to find a way to escape or do you try to      communicate with the aliens?")
  choice = input("Enter 1 to try to escape or 2 to communicate with the    aliens: ")
  if choice == "1":
      choice_2()
  elif choice == "2":
      choice_5()
  else:
    print("Invalid choice. Please try again.")
    choice_1()

def choice_2():
  print("You start to search the room for any possible exits or weaknesses in the walls.")
  print("After a while, you find a vent that you might be able to crawl through.")
  print("Do you try to escape through the vent or do you keep searching for other options?")
  choice = input("Enter 1 to try the vent or 2 to keep searching: ")
  if choice == "1":
    print("You manage to squeeze through the vent and make your way through the spaceship.")
    choice_4()
  elif choice == "2":
    print("You keep searching but are unable to find any other options.")
    print("Just as you are about to give up, the aliens open the door and offer you a deal.")
    choice_3()
  else:
    print("Invalid choice. Please try again.")
    choice_2()

def choice_3():
  print("The aliens explain that they will let you go if you agree to perform at their next Imagine Dragons concert.")
  print("Do you accept the deal and perform at the concert or do you try to find another way to escape?")
  choice = input("Enter 1 to accept the deal or 2 to try to escape: ")
  
  if choice == "1":
    print("You agree to perform at the concert and are released   back to your village.")
    print("You return home a hero and the aliens even send you tickets to their next concert as a thank you.")
    restart()
  elif choice == "2":
    print("You refuse the deal and the aliens become angry. They decide to imprison you and torture you until you die on their spaceship.")
    print("They torture you the only way they know how, blasting Imagine Dragons. The aliens eventually get bored with you and expirement on you. You become Superman for 5 minutes and obliterate the alien spaceship, but you spontaneously combust after those 5 minutes.")
    restart()
  else:
    print("Invalid choice. Please try again.")
    choice_3()

def choice_4():
  print("You manage to make it to the control room of the spaceship and find the controls to fly the ship.")
  print("Do you try to fly the ship back to Earth or do you try to find a way to communicate with your village for help?")
  choice = input("Enter 1 to fly the ship or 2 to communicate with your village: ")
  
  if choice == "1":
    print("You try to fly the ship but are unable to operate it properly.")
    print("The ship crashes and you are killed upon impact.")
    restart()
  elif choice == "2": 
    print("After several attempts you succesfully make contact with your village. Without you realizing the aliens walk in and hear your conversation.")
    print("The aliens get angry and decide the only fitting punishment is to imprison your whole village and torture them with Imagine Dragons.")
    restart()
  else:
    print("Invalid choice. Please try again.")
    choice_4()

def choice_5():
  print("After hours of talking to yourslef you hear a noise and the doors of the room open slowly. They say they want to propose an offer to you.")
  print("Do you want to hear out their offer or do you make a run for it through the door they just opened?")
  choice = input("Enter 1 to hear them out and 2 to make a break for it: ")

  if choice == "1":
    choice_3()
  elif choice == "2":
    print("You run and succesfully get past the aliens. As your run through the corridors you see an open door and          instantly run into that room. Luckily you have just          wandered into the armory. However you can hear the aliens, who are now angry and hunting you down.")
    choice_6()
  else:
    print("Invalid choice. Please try again.")
    choice_5()

def choice_6():
  print("You see " + str(NumItems()) + " different types of weapons all around you but must      make a choice as you cannot carry them all. You see the:")
  listItems()
  weapon_choice = str(input("Choose one of the " + str(NumItems()) + " weapons: (Copy the name of the weapon exactly as it appears above) "))
  if str(itemlist[0]) == weapon(weapon_choice,):
    print("You put on the armor and walk out of the armory. Instantly you are faced with 3 aliens, when you shoot the ray gun you get an error, and your armor's shields won't activate. You need a fingerprint to activate both the armor and ray gun. You hide behind a desk helplessly as they close in.")
    choice_7()
  elif str(itemlist[1]) == weapon(weapon_choice,):
    print("You take the red button, leave the armory, and are      almost instantly face to face wtih a couple of aliens. You     push the button and hear SELF NUKE SEQUENCE INITIATED. The button set off a nuke that blew up the entire ship to        smithereens, leaving no debris or evidence that anything used to ever exist there.")
    restart()
  elif str(itemlist[2]) == weapon(weapon_choice,):
    print("Coming from Africa, you have zero expirience with lightsabers. You struggle to turn the lightsaber on and accidentally turn it on while it is facing you, stabbing yourself.")
    restart()
  else:
    print("Invalid choice. Please try again.")
    choice_6()

def choice_7():
  print("In a crazy series of events you melee the 3 aliens with your ray gun and pieces of armor and knock them out. Then an alien with a minigun and extra armor comes down but you throw the raygun right at his head and knock him out.")
  print("Do you keep trying to get the ray gun to work or do you take this aliens minigun?")
  choice = input("Enter 1 to keep trying the ray gun and 2 to pick up the minigun: ")

  if choice == "1":
    print("Unsurprisingly the ray gun still doesn't work and you are quickly surrounded by the rest of the aliens. They capture you, and torture you with Imagine Dragons for the rest of your life.")
    restart()
  elif choice == "2":
    print("In a montage (with Imagine Dragons playing in the background) you mow down the rest of the Imagine Dragon loving aliens and fatlly injure their leader. As his dying wish he requests that you play his favorite Imagine Dragons song so he can die in peace. You then find a manual that details how to fly the ship and use it to fly the ship back home.")
    restart()
  else:
    print("Invalid choice. Please try again.")
    choice_7()
  
if __name__ == "__main__":
  start_game()