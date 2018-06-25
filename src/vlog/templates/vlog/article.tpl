{% extends 'core/base.tpl' %}
{% import 'core/macros.tpl' as macro %}

{% block title %}{{ article.title }}{% endblock %}
{% block sidebar %}
{{ macro.breadcrumps(crumbs, article.category.title) }}
{% endblock %}
{% block content %}
    <h1>{{ article.title }}</h1>
    <br>
    <p>{{ article.content|safe }}</p>
{% endblock %}
