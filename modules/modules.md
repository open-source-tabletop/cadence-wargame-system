---
title: Modules
subtitle: Find a game to play
permalink: /modules/
---

{% for module in site.data.module_list %}

### [{{module.name}}]({{module.link}})

{{module.description}}


{% endfor %}