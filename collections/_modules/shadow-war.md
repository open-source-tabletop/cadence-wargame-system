---
title: "Dark Millenium: Shadow War"
---

Dark Millenium: Shadow War takes the combat of Dark Millenium into smaller, more intense battles, featuring a small number of infantry scale models per player.

<span class="image main">
![Guardian Vanguard](/images/armoured.png "Guardian Vanguard by u/pidgeon_pete")
</span>

### Module Rules

- [Dark Millenium: Shadow War Module Rules](/shadow-war/module-rules/)
- [View Shadow War Missions](/shadow-war/missions/)

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