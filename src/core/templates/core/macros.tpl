{% macro breadcrumps(crumbs, active) -%}
    <nav aria-label="breadcrumb">
        <ol class="breadcrumb">
            {% for crumb in crumbs %}
                <li class="breadcrumb-item"><a href="{{ crumb.url }}">{{ crumb.title }}</a></li>
            {% endfor %}
            <li class="breadcrumb-item active" aria-current="page">{{ active }}</li>
        </ol>
    </nav>
{%- endmacro %}