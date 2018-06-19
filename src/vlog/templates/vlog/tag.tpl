{% extends 'core/base.tpl' %}

{% block title %}{{ tag.title }}{% endblock %}
{% block sidebar %}
<nav aria-label="breadcrumb">
  <ol class="breadcrumb">
    <li class="breadcrumb-item"><a href="{{ url('vlog:index') }}">{{ _('Blog') }}</a></li>
    <li class="breadcrumb-item"><a href="{{ url('vlog:tags') }}">{{ _('Tags') }}</a></li>
    <li class="breadcrumb-item active" aria-current="page">{{ tag.title }}</li>
  </ol>
</nav>
{% endblock %}
{% block content %}
    <h1>{{ tag.title }}</h1>
    <br>
    {% for article in tag.articles.all() %}
        <h2>{{ article.title }}</a></h2>
        <hr>
    {% endfor %}
{% endblock %}