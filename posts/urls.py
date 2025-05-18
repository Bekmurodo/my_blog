from django.urls import path

from posts.models import PostReview
from posts.views import (PostView,
                         PostDetailView,
                         AddReviewView,
                         AddPostView,
                         GovernmentViews,
                         SportViews,
                         LocalViews,
                         ShowViews, homePageView
                         )

app_name='posts'

urlpatterns = [
    path('last-posts/', homePageView, name='last'),
    path('list/', PostView.as_view(), name='list'),
    path('add-post/', AddPostView.as_view(), name='add-post'),
    path('<int:id>/', PostDetailView.as_view(), name='detail'),
    path('<int:id>/reviews/', AddReviewView.as_view(), name='reviews'),
    path('category/gov/', GovernmentViews.as_view(), name='gov'),
    path('category/sport/', SportViews.as_view(), name='sport'),
    path('category/show/', ShowViews.as_view(), name='show'),
    path('category/local/', LocalViews.as_view(), name='local'),


]