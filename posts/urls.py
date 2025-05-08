from django.urls import path

from posts.models import PostReview
from posts.views import PostView, PostDetailView, AddReviewView, AddPostView

app_name='posts'

urlpatterns = [
    path('list/', PostView.as_view(), name='list'),
    path('add-post/', AddPostView.as_view(), name='add-post'),
    path('<int:id>/', PostDetailView.as_view(), name='detail'),
    path('<int:id>/reviews/', AddReviewView.as_view(), name='reviews')

]