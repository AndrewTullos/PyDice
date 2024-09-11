import random

def dice_roll():
   print(f"({random.randrange(1,6)}, {random.randrange(1,6)})")


def play():
   roll = input("Roll the dice? (y/n):").strip().lower()

   if roll == "y":
      dice_roll()
      play()
   elif roll == "n":
      print("Thanks for wasting my time!")
      exit()
   else:
      print("Invalid choice!")
      play()

play() 