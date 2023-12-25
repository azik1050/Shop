from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = ResizedImageField(upload_to='profile_pics/', default='profile_pics/default.jpg', size=[500, 500])
    bio = models.TextField(default='User has not added any bio yet...')

    def __str__(self):
        return f'Profile - {self.user}'

class UserReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Name', max_length=50)
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(verbose_name='Phone number', max_length=50)
    text = models.TextField(verbose_name='Message', max_length=500)
    sent_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False, verbose_name='Activeness status')

    def __str__(self):
        return f'From {self.user}'

    class Meta:
        verbose_name = 'Message'