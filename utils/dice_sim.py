import random
import math

def simulate_attack(skill, attacks, damage, defense, piercing, toughness):

    # Roll the attack dice
    attack_rolls = [random.randint(1, 6) for _ in range(attacks)]
    hits = sum(1 for roll in attack_rolls if roll >= skill)
    
    # Roll the defense dice
    defense_rolls = [random.randint(1, 6) for _ in range(hits*damage)]
    defense_value = defense + piercing
    damage_taken = sum(1 for roll in defense_rolls if roll < defense_value)
    
    # Calculate damage
    hp_lost = math.floor(damage_taken / toughness)
    return hp_lost

results = []
for i in range(10000):
    results.append(simulate_attack(3, 9, 2, 4, 1, 3))

# Find the unique values in the rolls list using the set() function
unique_values = set(results)

# Count the number of occurrences of each unique value in the rolls list
for value in unique_values:
    count = results.count(value) / 100
    print(f"{value} wounds {count}% of the time.")