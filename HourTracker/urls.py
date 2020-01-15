from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from graphene_django.views import GraphQLView
from django.views.generic import TemplateView


urlpatterns = [
    path("", TemplateView.as_view(template_name='index.html')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('graphql/', GraphQLView.as_view(graphiql=True)),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
    