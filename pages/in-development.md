---
title: Game Modules in Development
permalink: /in-development/
---

The following projects are in a state of early development and may not be suitable for playing, however you may be able to get involved or play early versions of them.

{% for nav in site.data.wip_modules %}
<div class="box">
    <h3>{{ nav.name }}</h3>
    <p>{{ nav.description }}</p>
    <ul class="actions">
        <li><a href="{{ nav.link }}" class="button">{{ nav.name }}</a></li>
    </ul>
</div>
{% endfor %}