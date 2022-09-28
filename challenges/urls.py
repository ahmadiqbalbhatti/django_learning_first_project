from django.urls import path
# Path function is used to define the path or Url of the specific View
from . import views

urlpatterns = [
    path("<int:month>", views.monthly_challenge_by_month),
    path("<str:month>", views.monthly_challenge, name='month-challenge'),
    # path("january", views.january),
    # path("february", views.february),
    # path("march", views.march),
    # path("april", views.april),
    # path("may", views.may),
    # path("june", views.june),
    # path("july", views.july),
    # path("august", views.august),
    # path("september", views.september),
    # path("october", views.october),
    # path("november", views.november),
    # path("december", views.december),

]
