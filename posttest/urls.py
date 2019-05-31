from django.urls import path
from posttest import views


app_name = 'posttest'

urlpatterns = [
    path(
        'api/posttest/',
        views.ApiPosttestView.as_view(),
        name='api_posttest',
    ),
]

