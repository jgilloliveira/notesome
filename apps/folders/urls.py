from apps.folders.views import FolderView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', FolderView, basename='folders')

urlpatterns = router.urls


# from django.urls import path
# from apps.folders.views import FolderView
# from api_rest.urls import LIST_CREATE_VIEW_ARGS, BY_ID_VIEW_ARGS

# urlpatterns = [
#   path('', FolderView.as_view(LIST_CREATE_VIEW_ARGS)),
#   path('<pk>/', FolderView.as_view(BY_ID_VIEW_ARGS)),
# ]