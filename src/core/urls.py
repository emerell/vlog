from django.contrib import admin
from django.urls import path, re_path, include
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    re_path(r'^login/$', LoginView.as_view(template_name='core/login.tpl'), name='login'),
    re_path(r'^logout/$', LogoutView.as_view(), name='logout'),
    re_path(r'', include(('vlog.urls', 'vlog'), namespace='vlog')),
    re_path(r'^api/(?P<version>(v1|v2))/', include(('api.urls', 'api'), namespace='api')),

]
# re_path(r'^api/(?P<version>(v1|v2))/', include('endpoint.urls'), namespace='endpoint'),
# re_path(r'', include(('endpoint.urls', 'endpoint'), namespace='endpoint')),
#: TODO: While development. Code below is pretty fucking far from ok.
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        re_path(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
