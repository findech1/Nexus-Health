# from rest_framework import generics
# from .models import Notification
# from .serializers import NotificationSerializer

# class NotificationListView(generics.ListCreateAPIView):
#     queryset = Notification.objects.all()
#     serializer_class = NotificationSerializer

# class NotificationDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Notification.objects.all()
#     serializer_class = NotificationSerializer
# views.py

# from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# from django.urls import reverse_lazy
# from .models import Notification

# class NotificationListView(ListView):
#     model = Notification
#     template_name = 'notifications/notification_dashboard.html'
#     context_object_name = 'notifications'

# class NotificationDetailView(DetailView):
#     model = Notification
#     template_name = 'notifications/notification_detail.html'

# class NotificationCreateView(CreateView):
#     model = Notification
#     template_name = 'notifications/notification_form.html'
#     fields = ['user', 'message', 'read']
#     success_url = reverse_lazy('notification-list')

# class NotificationUpdateView(UpdateView):
#     model = Notification
#     template_name = 'notifications/notification_form.html'
#     fields = ['user', 'message', 'read']
#     success_url = reverse_lazy('notification-list')

# class NotificationDeleteView(DeleteView):
#     model = Notification
#     template_name = 'notifications/notification_confirm_delete.html'
#     success_url = reverse_lazy('notification-list')
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from django.db.models import Q
from .models import Notification

class NotificationListView(ListView):
    model = Notification
    template_name = 'notifications/notification_dashboard.html'
    context_object_name = 'notifications'

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_param = self.request.GET.get('filter', 'all')
        search_query = self.request.GET.get('search', '')

        if filter_param == 'read':
            queryset = queryset.filter(read=True)
        elif filter_param == 'unread':
            queryset = queryset.filter(read=False)

        if search_query:
            queryset = queryset.filter(message__icontains=search_query)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.request.GET.get('filter', 'all')
        context['search'] = self.request.GET.get('search', '')
        return context

class NotificationDetailView(DetailView):
    model = Notification
    template_name = 'notifications/notification_detail.html'

class NotificationCreateView(CreateView):
    model = Notification
    template_name = 'notifications/notification_form.html'
    fields = ['user', 'message', 'read']
    success_url = reverse_lazy('notification-list')

class NotificationUpdateView(UpdateView):
    model = Notification
    template_name = 'notifications/notification_form.html'
    fields = ['user', 'message', 'read']
    success_url = reverse_lazy('notification-list')

class NotificationDeleteView(DeleteView):
    model = Notification
    template_name = 'notifications/notification_confirm_delete.html'
    success_url = reverse_lazy('notification-list')

class NotificationToggleView(UpdateView):
    model = Notification
    fields = ['read']

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.read = not self.object.read
        self.object.save()
        return redirect(self.get_success_url())

    def get_success_url(self):
        return self.request.POST.get('next', reverse('notification-list'))