from django.contrib import admin

from .models import Post, Activity, Picture, Review, Reservation

admin.site.register(Post)
admin.site.register(Activity)
admin.site.register(Picture)
admin.site.register(Review)


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'date', 'phone_number', 'email')
    list_filter = ('date',)
