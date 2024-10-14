from django.contrib import admin
from django.urls import path
from toDos.views import todo_list

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", todo_list),
]
