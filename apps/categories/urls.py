from apps.categories.views import CategoryView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', CategoryView, basename='categories')

urlpatterns = router.urls


# from django.urls import path
# from apps.categories.views import CategoryView
# from api_rest.urls import LIST_CREATE_VIEW_ARGS, BY_ID_VIEW_ARGS

# urlpatterns = [
#   path('', CategoryView.as_view(LIST_CREATE_VIEW_ARGS)),
#   path('<pk>/', CategoryView.as_view(BY_ID_VIEW_ARGS)),
# ]
