from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

User = settings.AUTH_USER_MODEL

# Create your models here.

class Category(models.Model):
    name =  models.CharField(_('post category'), max_length=200, null=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    status_options = (
        ('draft', 'Draft'),
        ('publish', 'Publish')
    )
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='category_posts')
    title = models.CharField(_('post title'), max_length=100, blank=False, null=False)
    excerpt = models.CharField(max_length=150, blank=True, null=True)
    content = models.TextField(_('post content'), blank=False, null=False)
    created = models.DateTimeField(default=timezone.now)
    status = models.CharField(default='publish', max_length=10, choices=status_options)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_posts')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        ordering = ['-created']