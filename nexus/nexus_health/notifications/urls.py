# from django.urls import path
# from .views import NotificationListView, NotificationDetailView

# urlpatterns = [
#     path('', NotificationListView.as_view(), name='notification-list'),
#     path('<int:pk>/', NotificationDetailView.as_view(), name='notification-detail'),
# ]
# from django.urls import path
# from .views import NotificationListView, NotificationDetailView

# urlpatterns = [
#     path('', NotificationListView.as_view(), name='notification-list'),
#     path('<int:pk>/', NotificationDetailView.as_view(), name='notification-detail'),
# ]
# urls.py

# from django.urls import path
# from .views import NotificationListView, NotificationDetailView, NotificationCreateView, NotificationUpdateView, NotificationDeleteView

# urlpatterns = [
#     path('', NotificationListView.as_view(), name='notification-list'),
#     path('<int:pk>/', NotificationDetailView.as_view(), name='notification-detail'),
#     path('create/', NotificationCreateView.as_view(), name='notification-create'),
#     path('<int:pk>/update/', NotificationUpdateView.as_view(), name='notification-update'),
#     path('<int:pk>/delete/', NotificationDeleteView.as_view(), name='notification-delete'),
# ]
from django.urls import path
from .views import (
    NotificationListView, 
    NotificationDetailView, 
    NotificationCreateView, 
    NotificationUpdateView, 
    NotificationDeleteView,
    NotificationToggleView
)

urlpatterns = [
    path('', NotificationListView.as_view(), name='notification-list'),
    path('<int:pk>/', NotificationDetailView.as_view(), name='notification-detail'),
    path('create/', NotificationCreateView.as_view(), name='notification-create'),
    path('<int:pk>/update/', NotificationUpdateView.as_view(), name='notification-update'),
    path('<int:pk>/delete/', NotificationDeleteView.as_view(), name='notification-delete'),
    path('<int:pk>/toggle/', NotificationToggleView.as_view(), name='notification-toggle'),
]