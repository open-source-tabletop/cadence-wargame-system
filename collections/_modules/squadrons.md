---
title: Squadrons
---

Squadrons is a game of high speed combat between small fighter or bomber scale ships. Each player commands a squadron of around 5 to 15 ships as they try to take down their opponents ships.

### Modules Rules

- [Squadrons Modules Rules](/squadrons/module-rules/)

### Premade Fleets

The following fleets have been pre-made using the provided ship construction rules. These are fan creations and not official products.

{% assign fleets = site.squadrons | where: 'category', 'fleet' %}
{% for item in fleets %}
- [{{ item.title }}]({{ item.url }}){% endfor %}