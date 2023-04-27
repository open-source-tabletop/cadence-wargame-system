# Calculates a SQUADRONS ship cost based on cumulative upgrade cost
# Base cost is 15, or 20 if it has 5 or more upgrades
# Command upgrade is a multiplier, enter 0 for none

COMMAND1 = 2
COMMAND2 = 4
SPEED1 = 1
SPEED2 = 3
SKILLED1 = 1
SKILLED2 = 4
SKILLED3 = 9
ARMOUR1 = 4
ARMOUR2 = 9
TOUGH1 = 1
TOUGH2 = 4
TOUGH3 = 10
HP1 = 4
HP2 = 10
AGILITY = 1
BOOST = 1
SHIELD1 = 2
SHIELD2 = 4
SHIELD3 = 10
STEALTH1 = 4
STEALTH2 = 7
JAMMING = 3
COUNTERMEASURES = 2
WEAPONPLATFORM = 10
ENERGYCANNONS = 1
TWINENERGYCANNONS = 3
HEAVYENERGYCANNONS = 4
DISRUPTORS = 1
HEAVYDISRUPTORS = 2
KINETICCANNONS = 2
HEAVYKINETICCANNONS = 3
CONCUSSIONMISSILES = 6
HEAVYCONCUSSIONMISSILES = 8
UNGUIDEDBOMBS = 6
HEAVYENERGYTURRET = 8
HEAVYKINETICTURRET = 9

def calcShipCost(command: int, upgrades: list):
    cost = 15 # base cost
    if len(upgrades) >= 5:
        cost += 5 # +5 if 5 or more upgrades
    elif command > 0 and len(upgrades) >= 4:
        cost += 5
    for item in upgrades:
        cost += item # add up upgrades cost
    if command > 0:
        cost += command * len(upgrades) # add command cost
    print(cost)

calcShipCost(0,[ARMOUR2,TOUGH2,HP2,HEAVYKINETICCANNONS,HEAVYCONCUSSIONMISSILES,])
