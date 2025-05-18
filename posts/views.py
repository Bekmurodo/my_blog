from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, CreateView

from .forms import PostReviewForm, PostAddForm
from .models import Post, PostReview, Category


class PostView(ListView):
     template_name = 'posts/list.html'
     queryset = Post.objects.all()
     context_object_name = 'posts'
     #paginate_by = 2


class PostDetailView(View):

    def get(self, request, id):
        post = Post.objects.get(id=id)
        #review_form = BookReviewForm()

        context = {
            'post': post,
        }
        return render(request, 'posts/detail.html', context)


class AddReviewView(LoginRequiredMixin, View):
    def post(self, request, id):
        post = Post.objects.get(id=id)
        review_form = PostReviewForm(data=request.POST)

        if review_form.is_valid():
            PostReview.objects.create(
                post=post,
                user=request.user,
                stars_given=review_form.cleaned_data['stars_given'],
                comment=review_form.cleaned_data['comment']
            )
            return redirect(reverse('posts:detail', kwargs={'id': post.id}))

        return render(request, 'posts/detail.html', {'post':post, 'review_form': review_form})


class AddPostView(View):
    def get(self, request):
        post_form = PostAddForm()
        return render(request, 'posts/add_post.html', {'post_form': post_form})

    def post(self, request):
        post_form = PostAddForm(request.POST, request.FILES)

        if post_form.is_valid():

            new_post = post_form.save(commit=False)

            # Если в модели Post есть поле author, привязываем текущего пользователя
            if hasattr(new_post, 'author'):
                new_post.author = request.user

            new_post.save()
            post_form.save_m2m()

            return redirect(reverse('posts:list'))

        return render(request, 'posts/add_post.html', {'post_form': post_form})

class GovernmentViews(ListView):
    model = Post
    template_name = 'posts/government.html'
    context_object_name = 'govern'

    def get_queryset(self):
        return self.model.objects.filter(category_id=1)

class SportViews(ListView):
    model = Post
    template_name = 'posts/sport.html'
    context_object_name = 'sport'

    def get_queryset(self):
        return self.model.objects.filter(category_id=2)

class LocalViews(ListView):
    model = Post
    template_name = 'posts/local.html'
    context_object_name = 'local'

    def get_queryset(self):
        return self.model.objects.filter(category_id=4)


class ShowViews(ListView):
    model = Post
    template_name = 'posts/show.html'
    context_object_name = 'show'

    def get_queryset(self):
        return self.model.objects.filter(category_id=3)

def homePageView(request):
    categories = Category.objects.all()
    last_posts = Post.objects.all().order_by("-created_time")[:15]

    context = {
        'last_posts': last_posts,
        'categories': categories

    }

    return render(request, 'home.html', context)

