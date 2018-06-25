{% extends 'core/base.tpl' %}
{% import 'core/macros.tpl' as macro %}

{% block title %}{{ _('Index') }}{% endblock %}
{% block sidebar %}
{{ macro.breadcrumps(active= _('Blog')) }}
{% endblock %}
{% block content %}
    <h1>{{ _('Blog') }}</h1>
    <br><h4>{{ _('The most populated categories:') }}</h4>
    {% for category in categories %}
        <h2><a href="{{ url('vlog:category', category.slug ) }}">{{ category.title }}</a></h2>
        <hr>
    {% endfor %}
    <hr width="60%">
    <h4>{{ _('The most commented articles:') }}</h4>
    {% for article in articles %}
        <h2><a href="{{ url('vlog:article', article.category.slug, article.slug) }}">{{ article.title }}</a></h2>
        <hr>
    {% endfor %}
    <hr width="60%">
    <h4>{{ _('The most populated tags:') }}</h4>
    {% for tag in tags %}
        <h2><a href="/tags/{{ tag.slug }}/">{{ tag.title }}</a></h2>
        <hr>
    {% endfor %}
{% endblock %}

<!--{{ url('vlog:tag', tag.slug ) }}-->