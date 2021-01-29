from django.shortcuts import render, get_object_or_404
from .models import Post, Activity, Picture, Review, Reservation
from .forms import ReviewForm, ReservationForm
from django.db import IntegrityError


def homepage_view(request):
    posts = Post.published.all()
    activities = Activity.published.all()
    reviews = Review.objects.all()[:3]
    pictures = Picture.objects.all()[:4]
    return render(request,
                  'glemping/home.html',
                  {'section': 'home',
                   'posts': posts,
                   'activities': activities,
                   'reviews': reviews,
                   'pictures': pictures})


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


def booking(request):
    if request.method == 'POST':
        reservation_form = ReservationForm(request.POST)
        try:
            if reservation_form.is_valid():
                reservation_form.save(commit=True)
                Reservation.available = False

                return render(request,
                              'glemping/booking/success.html',
                              {'section': 'booking'})
        except IntegrityError:
            return render(request,
                          'glemping/booking/error.html',
                          {'section': 'booking'})

    else:
        reservation_form = ReservationForm()
        return render(request,
                      'glemping/booking/booking.html',
                      {'section': 'booking', 'reservation_form': reservation_form})


def about(request):
    return render(request, 'glemping/about/about_us.html', {'section': 'about'})
