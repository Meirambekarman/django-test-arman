from django.shortcuts import render

# Create your views here.

from .models import Employee, Department, Location


def index(request):
    num_departments = Department.objects.count()
    num_employees = Employee.objects.all().count()
    num_locations = Location.objects.count()

    return render(
        request,
        'index.html',
        context={'num_employees': num_employees, 'num_departments': num_departments, 'num_locations': num_locations},
    )


from django.views import generic


class DepartmentListView(generic.ListView):
    model = Department
    paginate_by = 2


class DepartmentDetailView(generic.DetailView):
    model = Department


class EmployeeListView(generic.ListView):
    model = Employee
    paginate_by = 2


class EmployeeDetailView(generic.DetailView):
    model = Employee

class LocationListView(generic.ListView):
    model = Location
    paginate_by = 2


class LocationDetailView(generic.DetailView):
    model = Location