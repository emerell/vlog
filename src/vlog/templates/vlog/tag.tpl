{% extends 'core/base.tpl' %}
{% import 'core/macros.tpl' as macro %}

{% block title %}{{ tag.title }}{% endblock %}
{% block sidebar %}
{{ macro.breadcrumps(crumbs, tag.title) }}
{% endblock %}
{% block content %}
    <h1>{{ tag.title }}</h1>
    <br>
    {% for article in tag.articles.all() %}
        <h2>{{ article.title }}</a></h2>
        <hr>
        <h4>({{article.category}})</h4>
    {% endfor %}
{% endblock %}