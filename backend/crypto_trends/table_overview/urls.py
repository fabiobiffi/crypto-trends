from django.urls import path, include
from .views import ajax_table_overview

urlpatterns = [
    path('ajax_table_overview/', ajax_table_overview, name="ajax_table_overview")
]
