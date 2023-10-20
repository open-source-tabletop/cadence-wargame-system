---
title: Game Modules
permalink: /modules/
---

The following game modules have been released for general use, however these games may still require playtesting and may be seeking additional contributors.

{% for nav in site.data.finished_modules %}
<div class="box">
    <h3>{{ nav.name }}</h3>
    <p>{{ nav.description }}</p>
    <ul class="actions">
        <li><a href="{{ nav.link }}" class="button">{{ nav.name }}</a></li>
    </ul>
</div>
{% endfor %}