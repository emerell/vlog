{% extends 'core/base.tpl' %}
{% import 'core/macros.tpl' as macro %}

{% block title %}Categories{% endblock %}
{% block sidebar %}
{{ macro.breadcrumps(crumbs, 'Категории') }}
{% endblock %}
{% block content %}
    <h1>{{ _('Categories') }}</h1>
    <br>
    {% for category in categories %}
        <h2><a href="/categories/{{ category.slug }}/">{{ category.title }}</a></h2>
        <hr>
    {% endfor %}
{% endblock %}
