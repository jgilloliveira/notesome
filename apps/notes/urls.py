from apps.notes.views import NoteView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', NoteView, basename='notes')

urlpatterns = router.urls


# from django.urls import path
# from apps.notes.views import NoteView
# from api_rest.urls import LIST_CREATE_VIEW_ARGS, BY_ID_VIEW_ARGS

# urlpatterns = [
#   path('', NoteView.as_view(LIST_CREATE_VIEW_ARGS)),
#   path('<pk>/', NoteView.as_view(BY_ID_VIEW_ARGS)),
# ]