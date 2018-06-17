{% extends 'core/base.tpl' %}

{% block title %}Index{% endblock %}
{% block sidebar %}
<nav aria-label="breadcrumb">
  <ol class="breadcrumb">
    <li class="breadcrumb-item active" aria-current="page">{{ _('Blog') }}</li>
  </ol>
</nav>
{% endblock %}
{% block content %}
    <h1>{{ _('Blog') }}</h1>
    <br><h4>The most populated categories:</h4>
    {% for category in categories %}
        <h2><a href="{{ url('vlog:category') }}">{{ category.title }}</a></h2>
        <hr>
    {% endfor %}
    <hr width="60%">
    <h4>The most commented articles:</h4>
    {% for article in articles %}
        <h2><a href="/{{ article.id }}/">{{ article.title }}</a></h2>
        <hr>
    {% endfor %}
    <hr width="60%">
    <h4>The most populated tags:</h4>
    {% for tag in tags %}
        <h2><a href="#">{{ tag.title }}</a></h2>
        <hr>
    {% endfor %}
{% endblock %}