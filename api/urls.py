from django.urls import path, include
from rest_framework import routers

from .views import WordViewSet, WordListAPIView, CreateWordAPIView, UpdateWordAPIView, DeleteWordAPIView

router = routers.DefaultRouter()
router.register(r'words', WordViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),


    path("", WordListAPIView.as_view(), name="words_list"),
    path("create/", CreateWordAPIView.as_view(), name="word_create"),
    path("update/<int:pk>/", UpdateWordAPIView.as_view(), name="update_word"),
    path("delete/<int:pk>/", DeleteWordAPIView.as_view(), name="delete_word")
]
