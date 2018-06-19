{% extends 'core/base.tpl' %}
{% import 'core/macros.tpl' as macro %}

{% block title %}{{ category.title }}{% endblock %}
{% block sidebar %}
{{ macro.breadcrumps(crumbs, category.title) }}
{% endblock %}
{% block content %}
    <h1>{{ category.title }}</h1>
    <br>
    {% for article in articles %}
        <h2><a href="/categories/{{ category.slug}}/articles/{{ article.slug }}/">{{ article.title }}</a></h2>
        <hr>
    {% endfor %}
{% endblock %}