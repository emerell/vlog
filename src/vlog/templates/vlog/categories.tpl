{% extends 'core/base.tpl' %}
{% import 'core/macros.tpl' as macro %}
{% block title %}{{ _('Categories') }}{% endblock %}
{% block sidebar %}
{{ macro.breadcrumps(crumbs, _('Categories')) }}
{% endblock %}
{% block content %}
    <h1>{{ _('Categories') }}</h1>
    <br>
    {% for category in categories %}
        <h2><a href="{{ url('vlog:category', category.slug ) }}">{{ category.title }}</a></h2>
        <hr>
    {% endfor %}
{% endblock %}