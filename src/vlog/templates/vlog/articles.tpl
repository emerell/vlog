{% extends 'core/base.tpl' %}
{% import 'core/macros.tpl' as macro %}

{% block title %}{{ _('Articles') }}{% endblock %}
{% block sidebar %}
{{ macro.breadcrumps(crumbs, _('Статьи')) }}
{% endblock %}
{% block content %}
    <h1>{{ _('Articles') }}</h1>
    <br>
    {% for article in articles %}
        <h2><a href="{{ url('vlog:article', article.category.slug, article.slug) }}">
            {{ article.title }}</a></h2>
        <hr>
    {% endfor %}
{% endblock %}