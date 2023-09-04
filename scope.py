
"""
# scope 

enemies = 1

def increase_enemies():

    enemies = 2

    print(f"enemies inside function: {enemies}")

increase_enemies()

print(f"enemies outside function: {enemies}")

"""

# global scope

player_health = 10

def game(): 

  def drink_potion():

      #local scope
      potion_strength = 2 

      print(player_health)

      drink_potion()

print(player_health)


if 3 > 2:

    a_variable = 10

    


