from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField

class Post(models.Model):
	title = models.CharField(max_length=50)
	content = RichTextField()
	auther = models.ForeignKey(User, on_delete = models.CASCADE)
	image = models.ImageField(upload_to = 'blog/',blank = True,null = True)
	tags = TaggableManager(blank=True)
	category = models.ForeignKey('Category',on_delete = models.SET_NULL,null = True)
	created = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name='Post'
		verbose_name_plural = 'Posts'

class Category(models.Model):
	category_name = models.CharField(max_length=50)

	def __str__(self):
		return self.category_name

	class Meta:
		verbose_name='category'
		verbose_name_plural = 'categories'

class Comment(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	post = models.ForeignKey(Post, on_delete = models.CASCADE)
	content = models.TextField(default='')
	created = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.post.title

		
