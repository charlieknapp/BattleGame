import os, time

def dice(sides):
  import random
  roll = random.randint(1, sides)
  return roll
def health():
  hp = (dice(6) * dice(12))/2 + 10
  return hp

def strength():
  str = (dice(6) * dice(8))/2 + 12
  return str

def creation():
  print()
  name = input("Name your Legend: ")
  print()
  print(name)
  hp = health()
  str = strength()
  print("HEALTH:", hp)
  print("STRENGTH:", str)
  time.sleep(1)
  return name, hp, str
  

(name1,hp1,str1) = creation()
(name2,hp2,str2) = creation()

os.system("clear")

def battle(name1, hp1, str1, name2, hp2, str2):
  rounds = 0
  print("Battle time")
  time.sleep(1.5)
  os.system("clear")
  while True:
    if hp1 <= 0:
      print(name1, "has died")
      print(name2, "has won in", rounds, "rounds")
      break
    elif hp2 <= 0:
      print(name2, "has died")
      print(name1, "has won in", rounds, "rounds")
      break
    else:
      rounds +=1
      if rounds>1:
        print("The battle continues")
      time.sleep(1.5)
      roll1 = dice(6)
      roll2 = dice(6)
      if roll1 > roll2:
        print(name1, "wins the round")
        time.sleep(1.5)
        damage = abs(str1 - str2) + 1
        hp2 -= damage
        print(name1, "deals", damage, "damage to", name2, "(", hp2, "hp left)")
        time.sleep(2)
        os.system("clear")
      elif roll2 > roll1:
        print(name2, "wins the round")
        time.sleep(1.5)
        damage = abs(str1 - str2) + 1
        hp1 -= damage
        print(name2, "deals", damage, "damage to", name1, "(", hp1, "hp left)")
        time.sleep(1.5)
        os.system("clear")
      else:
        print("The round is a draw")
        time.sleep(1.5)
        os.system("clear")

battle(name1,hp1,str1,name2,hp2,str2)