---
title: Guilds and Glory
---

Welcome to Guilds and Glory, a game of narrative fantasy adventures. A brave party of heroes. members of The Guild of Adventurers, fight fierce battles against monsters, delve into treacherous dungeons against all odds, all in the hope of glory and untold treasures.

Guilds and Glory is an asymmetric adventure game for 2 or more players. 1 player will play as the overlord - controlling a host of deadly creatures, as a brave party of adventurers make their way through a selection of narrative campaigns.

<span class="image main">
![Guilds and Glory](/images/dungeon.png "Dungeon by u/pidgeonpete")
</span>

## Module Rules

### Overview

#### The Adventurers

In Guilds and Glory, one player or a group of players controls a party of 4 heroes, members of the Guild of Adventurers, who have been hired for a dangerous job. Each campaign will see these heroes face several battles as they fight towards a final showdown.

#### The Overlord

The other player takes the role of the Overlord, controlling hordes of monsters and minions as they try to thwart the Adventurers at every turn. The Overlord is also responsible for running the game, including relating the narrative elements and any events that happen within the game.

#### Asymmetric Play

This game is designed to be asymmetric, with the focus of the story being the goals of the Adventurers. While the game is intended to be balanced in each battle, it is ultimately designed to allow the Adventurers to try again until they prevail against the Overlord. This does not mean that the Overlord player should allow the Adventurers to win, rather they should understand that their role is that of the storyteller and antagonist, similar to the role of a Dungeon Master in roleplaying games.

#### Battlefield

Different campaigns may require a broad range of terrain. If you do not wish to make or buy terrain, having a surface that measures around 2ft by 2ft, on which you can draw basic terrain, will work for most games. When using 2d terrain like this you need to imagine that any walls or obscuring terrain extends vertically up from the board when calculating line of sight.

### The Grid

Movement in Guilds and Glory occurs on a grid, with each square measuring approximately 1 inch. 

Models should be based so that they can occupy a single square on the grid, whenever possible. In the case of larger models, they can be based to take up a 2x2 block of squares - though they still only move 1 square at a time. Only one model can occupy a square at any given time.

Models may only move to adjacent squares, with diagonal movement being disallowed. Rather than measuring movement in inches, players count the number of squares traversed.

The distance between two models, for the purposes of range, is determined by the number of squares between the models calculated in the same way as for movement.

### Gameplay

#### Initiative

Guilds and Glory uses a fixed initiative order for the Adventurers, which is determined by rolling-off for each Adventurer and noting down the order. Initiative always begins with the Adventurers, and after each of their activations, the Overlord may activate one of their units.

#### Status Effects

During a game, models may be affected by various effects such as being stunned or poisoned. This typically occurs as a result of being hit by a weapon or spell, and applies a special rule to the model. As these effects can be temporary, it is recommended to use tokens to represent them, which can be placed next to the affected model. Unless otherwise indicated, a model suffering from a status effect rolls a d6 at the end of their activation, on a roll of a 2+ the effect is removed.

Status   | Effect
:------- | :-----
Stunned  | This model may only take 1 action on it's next activation.
Burning  | This model takes d6 damage at the start of it's activation, it may make Defence Rolls as normal.
Poisoned | This model has a -1 modifier to its Movement and Toughness.
Slowed   | This model may only move 1 space during a Move or Advance action.
Blinded  | This model must re-roll successful Attack Rolls.
Fear     | This model must spend an additional Command Point to move closer to an enemy or to make an Attack action.

## Playing the game

To play a game of Guilds and Glory you will need 3 things: Your characters, a campaign, and rules for the monsters and minions you will face. These sections are separated out into their own expansions that provide you with a great variety of options.

### Choose your Adventurers

{% assign heroes = site.guilds-and-glory | where: 'category', 'heroes' %}
{% for item in heroes %}
#### [{{ item.title }}]({{ item.url }})

{{item.excerpt | strip_html }}

{% endfor %}


### Monsters and Minions

{% assign minions = site.guilds-and-glory | where: 'category', 'minions' %}
{% for item in minions %}
#### [{{ item.title }}]({{ item.url }})

{{item.excerpt | strip_html }}

{% endfor %}

### Campaigns

{% assign campaign = site.guilds-and-glory | where: 'category', 'campaign' %}
{% for item in campaign %}
#### [{{ item.title }}]({{ item.url }})

{{item.excerpt | strip_html }}

{% endfor %}
