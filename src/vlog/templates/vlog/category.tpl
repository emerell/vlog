{% extends 'core/base.tpl' %}

{% block title %}{{ category.title }}{% endblock %}
{% block sidebar %}
<nav aria-label="breadcrumb">
  <ol class="breadcrumb">
    <li class="breadcrumb-item"><a href="{{ url('index') }}">{{ _('Blog') }}</a></li>
    <li class="breadcrumb-item"><a href="{{ url('categories') }}">{{ _('Categories') }}</a></li>
    <li class="breadcrumb-item active" aria-current="page">{{ category.title }}</li>
  </ol>
</nav>
{% endblock %}
{% block content %}
    <h1>{{ category.title }}</h1>
    <br>
    {% for article in articles %}
        <h2><a href="categories/{{ category.id}}/articles/{{ article.title }}/">{{ article.title }}</a></h2>
        <hr>
    {% endfor %}
{% endblock %}