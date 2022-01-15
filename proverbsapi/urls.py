from django.urls import path

from . import views
from .views import *

app_name = 'proverbs'
urlpatterns = [
    path('', views.ProverbListAPIView.as_view(), name='proverbs_list'),
    path("create/", CreateProverbAPIView.as_view(), name="create_proverb"),
    path("update/<int:pk>/", UpdateProverbAPIView.as_view(), name="update_proverb"),
    path("delete/<int:pk>/", DeleteProverbAPIView.as_view(), name="delete_proverb")
]
