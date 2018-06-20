{% extends 'core/base.tpl' %}
{% import 'core/macros.tpl' as macro %}

{% block title %}Articles{% endblock %}
{% block sidebar %}
{{ macro.breadcrumps(crumbs, 'Статьи') }}
{% endblock %}
{% block content %}
    <h1>{{ _('Articles') }}</h1>
    <br>
    {% for article in articles %}
        <h2><a href="/categories/{{ article.category.slug}}/articles/{{ article.slug }}/">{{ article.title }}</a></h2>
        <hr>
    {% endfor %}
{% endblock %}