---
title: "Dark Millenium: Shadow War"
---

Dark Millenium: Shadow War takes the combat of Dark Millenium into smaller, more intense battles, featuring a small number of infantry scale models per player.

## Module Rules

| Weapon Special Rules | Description |
| :------------------- | :---------- |
| Blast | When this weapon makes at least one hit against it's target it also counts as having 1 successful hit against every model, friendly or enemy, within 2 inches of the original target that is not completely obscured by terrain from the point of view of the original target. |
| Supercharge | You may add 1 to this weapon’s Attacks and Damage attributes, however if you do so, any Attack Rolls of 1 count as hitting the attacking model instead. |

## Building an Army

To build your army for Shadow War you select a number of units and their equipment from your chosen army list up to an agreed number of points. Games are typically played at 100 or 150 points. There are 4 types of model to choose from: Command, Standard, Specialist, and Elite. Your army should be made up of the following:

- 1 Command model.
- 2+ Standard models.
- 0-3 Specialist models.
- 0-2 Elite models.

Included in each army list is a number of upgrades, these may be purchased for models in your army following the restrictions given in the upgrade description. In addition you may not spend more than 10 points on upgrades and may not take the same upgrade more than 3 times unless indicated.


### Human Army Lists

{% assign human_lists = site.shadow-war | where: 'category', 'human' %}
{% for list in human_lists %}
- [{{list.title}}]({{list.url}}){% endfor %}

### Demonic Army Lists

{% assign demonic_lists = site.shadow-war | where: 'category', 'demonic' %}
{% for list in demonic_lists %}
- [{{list.title}}]({{list.url}}){% endfor %}

### Alien Army Lists

{% assign alien_lists = site.shadow-war | where: 'category', 'alien' %}
{% for list in alien_lists %}
- [{{list.title}}]({{list.url}}){% endfor %}