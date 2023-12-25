from django.contrib import admin
from .models import Profile, UserReview


class UserReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'phone', 'sent_at', 'approved')
    list_display_links = ('user',)
    list_filter = ('user', 'phone', 'email')
    list_editable = ('approved',)












admin.site.register(Profile)
admin.site.register(UserReview, UserReviewAdmin)
