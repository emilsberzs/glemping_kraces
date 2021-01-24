from django.shortcuts import render, get_object_or_404
from .models import Post, Activity, Picture, Review
from .forms import ReviewForm


def homepage_view(request):
    return render(request, 'glemping/home.html', {'section': 'home'})


def post_list(request):
    posts = Post.published.all()
    return render(request,
                  'glemping/news/list.html',
                  {'posts': posts, 'section': 'news'})


def post_detail(request, post):
    post = get_object_or_404(Post, slug=post, status='published')
    return render(request, 'glemping/news/detail.html', {'post': post, 'section': 'news'})


def activity_list(request):
    activities = Activity.published.all()
    return render(request,
                  'glemping/activities/list.html',
                  {'activities': activities,
                   'section': 'activities'})


def gallery_list(request):
    pictures = Picture.published.all()
    return render(request,
                  'glemping/gallery/list.html',
                  {'pictures': pictures,
                   'section': 'gallery'})


def review_view(request):
    reviews = Review.objects.all()
    review_form = ReviewForm()
    return render(request,
                  'glemping/reviews/review.html',
                  {'reviews': reviews,
                   'review_form': review_form,
                   'section': 'reviews'})
