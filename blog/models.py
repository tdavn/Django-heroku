from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return reverse('article-detail', args=(str(self.id)))  # id is the same as pk
        return reverse("blog_index")

class Post(models.Model):
    title = models.CharField(max_length=255)
    # body = models.TextField()
    # body = RichTextField(blank=True, null=True)
    introduction = models.CharField(max_length=400, default='Add an introduction for the post!')
    body = RichTextUploadingField(blank=True, null=True, config_name='special')
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog_index")
        # return reverse('blog_detail', args=(str(self.id)))  # id is the same as pk

class Comment(models.Model):
    author = models.CharField(max_length=60)
    # body = models.TextField()
    body = RichTextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
