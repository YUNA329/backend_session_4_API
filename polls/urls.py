from django.urls import path
from .views import poll_list, poll_detail, poll_agree, poll_disagree

urlpatterns = [
    path('poll/', poll_list),
    path('poll/<int:id>/', poll_detail),
    path('poll/<int:id>/agree/', poll_agree),
    path('poll/<int:id>/disagree/', poll_disagree),
]