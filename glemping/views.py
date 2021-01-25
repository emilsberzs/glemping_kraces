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
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review_form.save(commit=True)
            reviews = Review.objects.all()
            return render(request,
                          'glemping/reviews/review_added.html',
                          {'section': 'reviews', 'reviews': reviews})
    else:
        review_form = ReviewForm()

    reviews = Review.objects.all()
    return render(request,
                  'glemping/reviews/review.html',
                  {'review_form': review_form, 'reviews': reviews, 'section': 'reviews'})


def about(request):
    return render(request, 'glemping/about/about_us.html', {'section': 'about'})


def booking(request):
    return render(request, 'glemping/booking/booking.html', {'section': 'booking'})
