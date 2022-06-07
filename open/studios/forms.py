from django import forms
from django.forms import ModelForm
from django.forms.widgets import HiddenInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class ImageForm(forms.Form):
    name = forms.CharField(max_length = 255, required = True)
    upload = forms.ImageField(required = False)
    featured = forms.BooleanField(widget = forms.CheckboxInput, required = False)
    
    class Meta:
        parent_model = Image
        fields = (
            'name', 
            'upload',
            'featured')


class CommentForm(forms.Form):
    comment = forms.CharField(max_length = 500, widget = forms.Textarea, required = False)
    author = forms.CharField(max_length = 255, required = False)
    
    class Meta:
        parent_model = Comment
        model = Exhibit
        fk_name = 'comments'
        fields = ('comment', 'author')


class TagForm(forms.Form):
    name = forms.CharField(max_length = 255)
    
    class Meta:
        parent_model = Tag
        model = Exhibit
        fk_name = 'tags'
        fields = ('name')
        min_num = 1


class ExhibitForm(forms.Form):
    artist_name = forms.CharField(max_length = 255, required = True)
    email = forms.EmailField(max_length = 254, required = True)
    website = forms.URLField(max_length = 200, required = False)
    bio = forms.CharField(widget = forms.Textarea, required = True)
    
    exhibit_name = forms.CharField(max_length = 255, required = True)
    description = forms.CharField(max_length = 500, widget = forms.Textarea, required=True)
    featured = forms.BooleanField().hidden_widget
    featured_date = forms.DateField().hidden_widget
    
    choices = []
    for tag in Tag.objects.all():
        choices.append((tag.tag_id, tag.name))
    tags = forms.MultipleChoiceField(choices = choices, required = False)
    class Meta:
        model = Exhibit
        fields = ['artist_name', 'email', 'website', 'bio', 'exhibit_name', 'description']
    # description = forms.CharField(max_length = 500, widget = forms.Textarea, required=True)

# Customize inherited default Django user creation form 
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']