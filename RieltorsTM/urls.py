from django.contrib import admin
from django.urls import path
from Modelapp import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v.person_create),
    path('about/', v.about),
    path('persons/', v.person),
    path('persons/delete/<id>/', v.persons_delete),
    path('persons/update/<id>/<name>/<password>/', v.person_update),
]