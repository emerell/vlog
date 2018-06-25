{% extends 'core/base.tpl' %}
{% import 'core/macros.tpl' as macro %}

{% block title %}{{ category.title }}{% endblock %}
{% block sidebar %}
{{ macro.breadcrumps(crumbs, category.title) }}
{% endblock %}
{% block content %}
    <h1>{{ category.title }}</h1>
    <br>
    <img src="{{ category.image.url }}">
    <h2>{{ _('2 most commented articles: ') }}</h2>
    {% for article in top_articles %}
        <h2><a href="{{ url('vlog:article', article.category.slug, article.slug) }}">{{ article.title }}</a></h2>
        <h4>{{article.description}}</h4>
        <hr>
    {% endfor %}
    <br>
    <h2>{{ _('All articles: ') }}</h2>
    {% for article in articles %}
        <h2><a href="{{ url('vlog:article', article.category.slug, article.slug) }}">{{ article.title }}</a></h2>
    {% endfor %}
    {% block pagination %}
            {% include 'vlog/category_pagination.tpl' %}
    {% endblock %}
{% endblock %}

