from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('table_overview/', include('table_overview.urls'))
]
