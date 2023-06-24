---
title: Halo Firefight
---

Halo Firefight is a fan made game module set in the Halo universe that allows you to enact battles from any era in the Halo timeline.

> "In the 26th century, humankind has colonized hundreds of worlds in Earth's interstellar neighborhood, only to stumble upon a hostile alliance of aliens known as the Covenant. Motivated by the Prophets' promises of ascension to godhood in the form of the eponymous Halos, a series of ring-shaped superweapons built by the ancient race of the Forerunners, the Covenant are bent on humanity's destruction. With the apocalyptic Human-Covenant War concluded, members of both sides are faced with an uncertain future in a politically complex environment of numerous different factions and affiliations, while ancient Forerunner entities and technologies continue to involve themselves with the galaxy's affairs."

\- [Halopedia Entry on the Halo Universe](https://www.halopedia.org/)

This is an unofficial game but you can find out more about Halo at [Halo Waypoint: The Official Halo Website](https://www.halowaypoint.com/).

<span class="image main">
![Halo ODSTs](/images/halo-firefight-odsts.jpg "ODSTs by u/pidgeonpete")
</span>

## Module Rules

### Playing Halo Firefight

Halo Firefight is best played on a battlefield around 3ft by 4ft or larger and is designed for 28mm, individually based miniatures.

### Building an Army

Building an army for Halo Firefight simply requires choosing the units you wish to use from any of the provided army lists, adding up the points to an agreed total for each model, their weapons, and equipment. Small games are typically played at 100 points, standard games at 200 points, and large games from 300. There are no restrictions to which models you may use and it is up to players to agree on what would make a satisfying battle.

### Special Rules

The following special rules are used in Halo Firefight games:

| Model Special Rules | Effect |
| :------------------ | :----- |
| Active Camo | When a model targets this model for an attack from more than 6 inches away, it must roll a d6 first. On a roll of a 6 it is able to make the attack. All attacks against this model suffer -1 to their Attack Rolls. If this model is hit by any attacks it loses the Active Camo rule for the remainder of the round. |
| Weak Point (Arc) | This model counts as having a Toughness of 1 against attacks in the specified Arc. |
| Vehicle | This model may not use climbable terrain. In addition this model may make a free attack action against any unit it comes into base contact with using the Vehicle Ram weapon. |

| Weapon Special Rules | Effect |
| :------------------- | :----- |
| Barrage | This weapon may split its attacks between two targets, so long as they are both valid targets, and are within 3 inches of each other. Decide how many of the attacks are targeting each of the targets before making any Attack Rolls. |
| Dual Wield (X) | If a model is equipped with two of these weapons it may add X to the Attacks attribute. |

### Weapons

| Human Weapons        | Rng | Att | Dmg | Prc | Special Rules                    | Points |
| :------------------- | :-: | :-: | :-: | :-: | :------------------------------- | :----- |
| BR55 Service Rifle   | 28" |  3  |  4  |  1  |                                  | 1      |
| M41 Rocket Launcher  | 24" |  4  |  6  |  3  | Heavy, Shred                     | 3      |
| M6 Pistol            | 8"  |  2  |  4  |  1  | Dual Wield (1)                   | 0      |
| M7 SMG               | 18" |  5  |  2  |  0  | Dual Wield (2)                   | 0      |
| M79 MLRS             | 18" |  7  |  5  |  2  | Barrage, Heavy, Indirect         | 10     |
| M9 Grenade           | 8"  |  3  |  6  |  3  | One Use, Indirect                | 0      |
| M90 Shotgun          | 12" |  4  |  5  |  1  | Rending (2)                      | 2      |
| MA5 Assault Rifle    | 20" |  4  |  3  |  0  | Rapid Fire (1)                   | 0      |
| Melee Strike (X)     | 1"  |  3  |  X  |  1  | Assault                          | 0      |
| SRS99 Sniper Rifle   | 48" |  1  |  10 |  3  | Accurate, Rending (1)            | 3      |
| Vehicle Ram          | 1"  |  *  |  4  |  0  | Accurate, Rending (4), Shred     | 0      |
| Vulcan "Chaingun"    | 24" |  6  |  3  |  2  | Heavy, Rapid Fire (3)            | 12     |

* The number of attacks for a Vehicle Ram is equal to the number of models in the target unit on the same height level as the attacker.

| Covenant Weapons     | Rng | Att | Dmg | Prc | Special                               | Points |
| :------------------- | :-: | :-: | :-: | :-: | :------------------------------------ | :----- |
| Assault Cannon       | 18" |  3  |  6  |  2  | Heavy, Shred, Volley                  | 3      |
| Beam Rifle           | 48" |  2  |  6  |  1  | Accurate, Rending (1)                 | 1      |
| Covenant Carbine     | 16" |  4  |  3  |  0  |                                       | 0      |
| Energy Sword         | 1"  |  3  |  8  |  4  | Assault, Shred                        | 5      |
| Fuel Rod Gun         | 30" |  2  |  8  |  3  | Heavy, Shred, Volley                  | 3      |
| Hunter Combat Shield | 1"  |  4  |  4  |  1  | Assault                               | 0      |
| Needle Rifle         | 32" |  3  |  3  |  0  | Rending (2)                           | 1      |
| Needler              | 18" |  8  |  1  |  0  | Accurate, Rending (2), Dual Wield (4) | 1      |
| Plasma Grenade       | 8"  |  3  |  5  |  1  | One Use, Accurate                     | 0      |
| Plasma Pistol        |     |     |     |     |                                       | 0      |
| - Standard           | 16" |  3  |  2  |  0  | Dual Wield (1)                        | -      |
| - Overcharge         | 12" |  2  |  5  |  2  | Heavy, Rending (1)                    | -      |
| Plasma Rifle         | 20" |  5  |  2  |  1  |                                       | 0      |

## Army Lists

{% for item in site.halo-firefight %}
[{{ item.title }}]({{ item.url }})
{% endfor %}