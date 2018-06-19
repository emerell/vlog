{% extends 'core/base.tpl' %}

{% block title %}Tags{% endblock %}
{% block sidebar %}
<nav aria-label="breadcrumb">
  <ol class="breadcrumb">
    <li class="breadcrumb-item"><a href="/">{{ _('Blog') }}</a></li>
    <li class="breadcrumb-item active" aria-current="page">{{ _('Tags') }}</li>
  </ol>
</nav>
{% endblock %}
{% block content %}
    <h1>{{ _('Tags') }}</h1>
    <br>
    {% for tag in tags %}
        <h4><a href="/tags/{{ tag.slug }}/">{{ tag.title }}</a></h4>
        <hr>
    {% endfor %}
    <h2>3 most commented articles: </h2>
    {% for article in articles %}
        <h4>{{ article.title }}</h4>
        <hr>
    {% endfor %}
{% endblock %}
