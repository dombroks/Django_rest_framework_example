from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from employeeApp import views

router = routers.DefaultRouter()

router.register('employees', views.EmployeeAPI)
router.register('departments', views.DepartmentsAPI)
router.register('deptemp', views.DeptEmpAPI)
router.register('deptmanager', views.SalariesAPI)
router.register('salaries', views.SalariesAPI)
router.register('titles', views.TitlesAPI)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
