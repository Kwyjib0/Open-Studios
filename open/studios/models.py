from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Tag(models.Model):
    tag_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 255)
    
    class Meta:
        verbose_name_plural = 'Tags'
    
    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete = models.CASCADE)
    profile_image = models.ImageField(
        null=True, blank=True, upload_to='images/profiles/', default="images/profiles/user-default.png")


    class Meta:
        verbose_name_plural = 'Profiles'
    
    def __str__(self):
        return self.user.username

class Exhibit(models.Model):
    exhibit_id = models.AutoField(primary_key = True)
    exhibit_name = models.CharField(max_length = 255)
    description = models.TextField()
    timestamp = models.DateField(auto_now = False, auto_now_add = True)
    featured_date = models.DateField(auto_now = False, blank = True, null = True)
    featured = models.BooleanField(default = False, blank = True)
    revealed = models.BooleanField(default = False, blank = True)
    
    # Linked class
    tags = models.ManyToManyField(Tag, blank = False)
    
    # potentially will be moved to User model
    artist_name = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 254)
    website = models.URLField(max_length = 200, blank = True, null = True)
    bio = models.TextField()
    profile = models.ForeignKey(Profile, related_name='exhibits', null = True, on_delete = models.DO_NOTHING)
    
    class Meta:
        verbose_name_plural = 'Exhibits'
    
    def __str__(self):
        return self.exhibit_name
    
    def add_featured(self):
        self.featured = True
        self.featured_date = datetime.date.today()
    
    def remove_featured(self):
        self.featured = False
        self.revealed = True

class Image(models.Model):
    image_id = models.AutoField(primary_key = True)
    featured = models.BooleanField(default = False)
    name = models.CharField(max_length = 255)
    # File Upload
    upload = models.ImageField(blank = True, null = True, upload_to='images/art')
    
    # Linked class
    exhibit_name = models.ForeignKey(Exhibit, related_name = 'pics', null = True, on_delete = models.DO_NOTHING)
    
    
    class Meta:
        verbose_name_plural = 'Images'
    
    def __str__(self):
        return self.name


class Comment(models.Model):
    comment_id = models.AutoField(primary_key = True)
    comment = models.TextField(blank = True, null = True)
    created = models.DateTimeField(auto_now_add = True)
    author = models.CharField(max_length = 255, blank = True, null = True)
    
    # Linked class
    exhibit = models.ForeignKey(Exhibit, related_name="responses", blank = True, null = True, on_delete = models.DO_NOTHING)
    
    class Meta:
        verbose_name_plural = 'Comments'
    
    def __str__(self):
        return self.comment