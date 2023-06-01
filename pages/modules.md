---
title: Game Modules
permalink: /modules/
---

{% for nav in site.data.modules_nav %}
### {{ nav.name }}

{{ nav.description }}

<a href="{{ nav.link }}" class="button primary">View the {{ nav.name }} module</a>

-----
{% endfor %}