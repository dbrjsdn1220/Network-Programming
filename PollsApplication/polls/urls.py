from django.urls import path
from . import views
from .views import MyView

app_name = 'polls'

urlpatterns = [
    path('', MyView.index, name='index'),
    path('<int:question_id>/', MyView.detail, name='detail'),
    path('<int:question_id>/results/', MyView.results, name='results'),
    path('<int:question_id>/vote', MyView.vote, name='vote')
]
