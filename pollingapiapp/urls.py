from rest_framework.routers import DefaultRouter
from .views import *
from django.urls import path, include

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'questions', QuestionViewSet, basename='questions')
router.register(r'questions', QuestionViewSet, basename='questions')
router.register(r'votes', VotesViewSet, basename='votes')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]



