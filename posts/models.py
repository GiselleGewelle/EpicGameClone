from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from category.models import Category
from ckeditor.fields import RichTextField

User = get_user_model()


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.RESTRICT,
                              related_name='posts', default=None)
    title_of_game = models.CharField(max_length=150)
    title_of_publisher = models.CharField(max_length=50, blank=True)
    name_of_developer = models.CharField(max_length=50, blank=True)
    date_of_issue = models.DateField()
    short_description = RichTextField(default='')
    image_for_short = models.ImageField(upload_to='images', default=None)
    category = models.ForeignKey(Category, related_name='posts',
                                 on_delete=models.RESTRICT)
    full_description = RichTextField(default='')
    image_for_full = models.ImageField(upload_to='images')
    price = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    link_on_game = models.URLField()
    link_on_discord = models.URLField(blank=True)
    link_on_instagram = models.URLField(blank=True)
    link_on_twitter = models.URLField(blank=True)
    link_on_facebook = models.URLField(blank=True)
    slug = models.SlugField(max_length=50, primary_key=True, default=None)
    video = models.FileField(upload_to='videos', default=None)

    # class PostItem(models.Model):
    #     category = models.ForeignKey(Post, related_name='items', on_delete=models.CASCADE)

    def __str__(self):
        return self.title_of_game


@receiver(pre_save, sender=Post)
def category_slug_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title_of_game)
