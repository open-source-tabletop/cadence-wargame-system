---
title: Modules
subtitle: Find a game to play
permalink: /modules/
---

{% for module in site.modules %}
  <h2>{{ module.title }}</h2>
  <p>{{ module.excerpt | markdownify }}</p>
  <p><a href="{{ mod.url }}">Go to module</a></p>
{% endfor %}
