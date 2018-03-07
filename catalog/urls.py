from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
	path('departments/', views.DepartmentListView.as_view(), name='departments'),
    path('department/<int:pk>', views.DepartmentDetailView.as_view(), name='department-detail'),
	path('employees/', views.EmployeeListView.as_view(), name='employees'),
	path('employee/<int:pk>', views.EmployeeDetailView.as_view(), name='employee-detail'),
    path('locations/', views.LocationListView.as_view(), name='locations'),
	path('location/<int:pk>', views.LocationDetailView.as_view(), name='location-detail'),
]
