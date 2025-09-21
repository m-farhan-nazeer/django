from django.urls import path
from . import views

urlpatterns = [
    path('', views.JobListView.as_view(), name='job_list'),
    path('job/<int:pk>/', views.JobDetailView.as_view(), name='job_detail'),
    path('job/create/', views.JobCreateView.as_view(), name='job_create'),
    path('job/<int:pk>/update/', views.JobUpdateView.as_view(), name='job_update'),
    path('job/<int:pk>/delete/', views.JobDeleteView.as_view(), name='job_delete'),
    path('api/jobs/', views.JobListCreateAPIView.as_view(), name='api_job_list_create'),
    path('api/jobs/<int:pk>/', views.JobRetrieveUpdateDestroyAPIView.as_view(), name='api_job_detail'),
]
