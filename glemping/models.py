from django.db import models
from django.utils import timezone
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20,
                              choices=STATUS_CHOICES, default='draft')
    image = models.ImageField(blank=True)
    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('glemping:post_detail', args=[self.slug])


class Activity(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(blank=True)
    season = models.CharField(max_length=100)
    status = models.CharField(max_length=20,
                              choices=STATUS_CHOICES, default='draft')
    objects = models.Manager()
    published = PublishedManager()
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title


class Picture(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    title = models.CharField(max_length=100)
    image = models.ImageField()

    status = models.CharField(max_length=20,
                              choices=STATUS_CHOICES, default='draft')
    publish = models.DateTimeField(default=timezone.now)
    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title


class Review(models.Model):
    name = models.CharField(max_length=50)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Review by {self.name}'


class Reservation(models.Model):
    name = models.CharField(max_length=20, default='First name')
    surname = models.CharField(max_length=20, default='Last name')
    phone_number = models.CharField(max_length=8, default='12345678')
    email = models.EmailField(default='We need this to send booking data')
    date = models.DateField(default=timezone.now)
    available = models.BooleanField(default=True)

    class Meta:
        unique_together = ("date", "available")

    def __str__(self):
        return f'{self.name} {self.surname} on {self.date}'
