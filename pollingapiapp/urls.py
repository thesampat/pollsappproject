from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'questions', QuestionViewSet, basename='questions')
router.register(r'questions', QuestionViewSet, basename='questions')
router.register(r'votes', VotesViewSet, basename='votes')

urlpatterns = router.urls



