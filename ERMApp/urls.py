from django.urls import path
from . import views
urlpatterns = [
    #re_path(r'^$', views.emp_form),
    #re_path(r'^list$', views.emp_list),
    path(' ', views.emp_form, name='employee_insert'),
    path('<int:id>/', views.emp_form, name='employee_update'),
    path('list/', views.emp_list, name='employee_list'),
    path('delete<int:id>/', views.emp_delete, name='employee_delete'),
]