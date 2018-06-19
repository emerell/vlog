{% extends 'core/base.tpl' %}

{% block title %}Categories{% endblock %}
{% block sidebar %}
<nav aria-label="breadcrumb">
  <ol class="breadcrumb">
    <li class="breadcrumb-item"><a href="/">{{ _('Блог') }}</a></li>
    <li class="breadcrumb-item active" aria-current="page">{{ _('Категории') }}</li>
  </ol>
</nav>
{% endblock %}
{% block content %}
    <h1>{{ _('Categories') }}</h1>
    <br>
    {% for category in categories %}
        <h2><a href="/categories/{{ category.slug }}/">{{ category.title }}</a></h2>
        <hr>
    {% endfor %}
{% endblock %}
