from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, CreateView

from .forms import PostReviewForm, PostAddForm
from .models import Post, PostReview


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
        postt = Post.objects.get(id=id)
        review_form = PostReviewForm(data=request.POST)

        if review_form.is_valid():
            PostReview.objects.create(
                post=postt,
                user=request.user,
                stars_given=review_form.cleaned_data['stars_given'],
                comment=review_form.cleaned_data['comment']
            )
            return redirect(reverse('posts:detail', kwargs={'id': postt.id}))

        return render(request, 'posts/detail.html', {'post':postt, 'review_form': review_form})


class AddPostView(View):
    def get(self, request):
        post_form = PostAddForm()
        return render(request, 'posts/add_post.html', {'post_form': post_form})

    def post(self, request):
        post_form = PostAddForm(data=request.POST)

        if post_form.is_valid():
            Post.objects.create(
                title=post_form.cleaned_data['title'],
                text=post_form.cleaned_data['text'],
                image=post_form.cleaned_data['image']
            )
            return redirect(reverse('posts:list'))
        return render(request, 'posts/list.html', {'post_form': post_form})



