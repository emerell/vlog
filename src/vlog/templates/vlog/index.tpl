{% extends 'core/base.tpl' %}
{% import 'core/macros.tpl' as macro %}

{% block title %}Index{% endblock %}
{% block sidebar %}
{{ macro.breadcrumps(active='Блог') }}
{% endblock %}
{% block content %}
    <h1>{{ _('Blog') }}</h1>
    <br><h4>The most populated categories:</h4>
    {% for category in categories %}
        <h2><a href="/categories/{{category.slug}}">{{ category.title }}</a></h2>
        <hr>
    {% endfor %}
    <hr width="60%">
    <h4>The most commented articles:</h4>
    {% for article in articles %}
        <h2><a href="/categories/{{ article.category.slug}}/articles/{{ article.slug }}/">{{ article.title }}</a></h2>
        <hr>
    {% endfor %}
    <hr width="60%">
    <h4>The most populated tags:</h4>
    {% for tag in tags %}
        <h2><a href="/tags/{{ tag.slug }}/">{{ tag.title }}</a></h2>
        <hr>
    {% endfor %}
{% endblock %}