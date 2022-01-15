from django.urls import path

from . import views
from .views.proverbs import *

# router = routers.DefaultRouter()
# router.register(r'words', WordViewSet)
from .views.word import *

urlpatterns = [
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),


    path("", views.word.WordListAPIView.as_view(), name="words_list"),
    path("create/", views.word.CreateWordAPIView.as_view(), name="word_create"),
    path("update/<int:pk>/", views.word.UpdateWordAPIView.as_view(), name="update_word"),
    path("delete/<int:pk>/", views.word.DeleteWordAPIView.as_view(), name="delete_word"),


    path("", ProverbListAPIView.as_view(), name="proverb_list"),
    path("create/", CreateProverbAPIView.as_view(), name="create_proverb"),
    path("update/<int:pk>/", UpdateProverbAPIView.as_view(), name="update_proverb"),
    path("delete/<int:pk>/", DeleteProverbAPIView.as_view(), name="delete_proverb")
]
