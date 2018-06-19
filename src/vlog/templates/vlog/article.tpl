{% extends 'core/base.tpl' %}

{% block title %}{{ article.title }}{% endblock %}
{% block sidebar %}
<nav aria-label="breadcrumb">
  <ol class="breadcrumb">
    <li class="breadcrumb-item"><a href="{{ url('vlog:index') }}">{{ _('Блог') }}</a></li>
    <li class="breadcrumb-item"><a href="{{ url('vlog:categories') }}">{{ _('Категории') }}</a></li>
      <li class="breadcrumb-item"><a href="{{ url('vlog:category', article.category.slug) }}">{{ article.category.title }}</a></li>
    <li class="breadcrumb-item active" aria-current="page">{{ article.title }}</li>
  </ol>
</nav>
{% endblock %}
{% block content %}
    <h1>{{ article.title }}</h1>
    <br>
     <p>{{ article.content|safe }}</p>
{% endblock %}