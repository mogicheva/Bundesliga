from django.urls import path

from web.views import show_index, show_table, show_weekend, show_upcoming, show_finished

urlpatterns = [
    path('', show_index,name='show home'),
    path('table', show_table, name='table'),
    path('show-weekend', show_weekend, name='weekend'),
    path('show-upcoming', show_upcoming, name='upcoming'),
    path('show-finished', show_finished, name='finished'),
]