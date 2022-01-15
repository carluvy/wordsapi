from django.urls import path

from .views import *

path(" ", ProverbListAPIView.as_view(), name="proverb_list"),
path("create/", CreateProverbAPIView.as_view(), name="create_proverb"),
path("update/<int:pk>/", UpdateProverbAPIView.as_view(), name="update_proverb"),
path("delete/<int:pk>/", DeleteProverbAPIView.as_view(), name="delete_proverb")