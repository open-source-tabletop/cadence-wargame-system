---
title: Guilds and Glory
subtitle: A Wild West Skirmish game in the lawless town of Devil's Bluff
---

Welcome to Guilds and Glory, a game of narrative fantasy adventures. A brave party of heroes. members of The Guild of Adventurers, fight fierce battles against monsters, delve into treacherous dungeons against all odds, all in the hope of glory and untold treasures.

Guilds and Glory is an asymmetric adventure game for 2 or more players. 1 player will play as the overlord - controlling a host of deadly creatures, as a brave party of adventurers make their way through a selection of narrative campaigns.

## Module Rules

### Overview

#### The Adventurers

In Guilds and Glory, one player or a group of players controls a party of 4 heroes, members of the Guild of Adventurers, who have been hired for a dangerous job. Each campaign will see these heroes face several battles as they fight towards a final showdown.

#### The Overlord

The other player takes the role of the Overlord, controlling hordes of monsters and minions as they try to thwart the Adventurers at every turn. The Overlord is also responsible for running the game, including relating the narrative elements and any events that happen within the game.

#### Asymmetric Play

This game is designed to be asymmetric, with the focus of the story being the goals of the Adventurers. While the game is intended to be balanced in each battle, it is ultimately designed to allow the Adventurers to regroup, change their characters or equipment, and try again until they prevail against the Overlord. This does not mean that the Overlord player should allow the Adventurers to win, rather they should understand that their role is that of the storyteller and antagonist, similar to the role of a Dungeon Master in roleplaying games.

#### Battlefield

Different campaigns may require a broad range of terrain. If you do not wish to make or buy terrain, having a surface that measures around 2ft by 2ft, on which you can draw basic terrain, will work for most games.

### Gameplay

#### Initiative

Guilds and Glory uses a fixed initiative order for the Adventurers, which is determined by rolling-off for each Adventurer and noting down the order. Initiative always begins with the Adventurers, and after each of their activations, the Overlord may activate one of their units. 

TODO

- Magic System
- Status Effects
- Experience
- Gold and its uses
- Explain Books

### Create your Adventurers

{% assign heroes = site.guilds-and-glory | where: 'category', 'heroes' %}
{% for item in heroes %}
- [{{ item.title }}]({{ item.url }}){% endfor %}

### Monsters and Minions

{% assign minions = site.guilds-and-glory | where: 'category', 'minions' %}
{% for item in minions %}
- [{{ item.title }}]({{ item.url }}){% endfor %}

### Campaigns

{% assign campaign = site.guilds-and-glory | where: 'category', 'campaign' %}
{% for item in campaign %}
- [{{ item.title }}]({{ item.url }}){% endfor %}