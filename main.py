class Pet():
   def __init__(self, name, hunger = 5, age= 0, boredom = 3, sleepiness = 3):
       self.dead = False
       self.name = name
       self.hunger = hunger
       self.boredom = boredom
       self.sleepiness = sleepiness
       self.age = age
  


   def feed(self):
       if self.dead == True:
           return
       self.hunger -=3
       if self.hunger <0:
           self.hunger = 0




   def wait(self):
       if self.dead == True:
           return
       self.age += 1
       self.sleepiness += 1
       self.hunger += 1
       self.boredom += 1






   def sleep(self):
       if self.dead == True:
           return
       self.sleepiness -=5
       if self.sleepiness <0:
           self.sleepiness = 0




   def play(self):
       if self.dead == True:
           return
       self.boredom -=3
       if self.boredom <0:
           self.boredom = 0


   def is_dead(self):
       if self.sleepiness >= 10:
           self.dead = True
       if self.boredom >= 10:
           self.dead = True
       if self.hunger >= 10:
           self.dead = True
       if self.hunger >= 15:
           self.dead = True
   def __str__(self):
    return (f"{self.name} - Age: {self.age}, Hunger: {self.hunger}, "
            f"Boredom: {self.boredom}, Sleepiness: {self.sleepiness}")
   
   def check_death(self):
    if self.sleepiness >= 10 or self.boredom >= 10 or self.hunger >= 10 or self.age >= 15:
        return True
    return False

gravestone = '''
     _______
    /       \\
   /         \\
  |           |
  |   RIP     |
  |           |
  |___________|
'''


def main():
    pet = Pet(input("what is the name of your pet: "))

    while not pet.check_death():
        print(pet)
        action = input("Choose an action (feed/play/sleep/wait/quit): ").lower()

        if action == "feed":
            pet.feed()
        elif action == "play":
            pet.play()
        elif action == "sleep":
            pet.sleep()
        elif action == "wait":
            pet.wait()
        elif action == "quit":
            print("Exiting the game.")
            break
        else:
            print("Invalid action. Please choose again.")

    if pet.check_death():
        print(f"{pet.name} has died!")
        print(gravestone)
        return

if __name__ == "__main__":
    main()



####----Task 1----####
#Set up your pet with the following attributes:
#name (make this mandatory), age (default:0), hunger (default: 5), boredom (default:3), sleepiness(default:3)

####----Task 2----####
#instantiate your pet object with the name of your choice

####----Task 3----#### 
# We need to add the following methods to our Virtual Pet:
# 1. Feed - which will reduce hunger by 3
# use a selection to make sure if hunger goes below zero it gets reset to 0 (we don’t want any negative numbers.)
# 2. Play - which will reduce boredom by 3
# 3. Sleep - which will reduce sleepiness by 5
# 4. Wait - which will increase age, and increase hunger, boredom and sleepiness
# 5. Is_dead - which will check to see if the Pet has hit the thresholds we have set as the
# maximum possible hunger, boredom and sleepiness

###----Task 4----####
# Make a new method called check_death() that checks when a pet dies.
# These are the conditions I have chosen to use to determine if the pet should be dead.
# (Note: you can change these to make your pet harder or easier to keep alive)
    # ● Boredom is at 10
    # ● Sleepiness is at 10
    # ● Hunger is at 10
    # ● Age is at a random age between 15 and 20 or more


####---Task 5----####
#make it so that the feed, sleep, play and wait will check if the pet
#is dead before you upadate those properties.

####---Task 6----####
#Use Python's predefined __str__ method to produce a string output
#for your pet. refer to page 4 of the tutorial if you don't know
#what I'm talking about.

#Go to page 9 of the tutorial to learn how to make the mainline (https://classroom.google.com/w/NzE2NTQ0NzA2MTYx/t/all)

####---Task 7----####
#Use Python's name mangling strategy to convert the death attribute to be private
