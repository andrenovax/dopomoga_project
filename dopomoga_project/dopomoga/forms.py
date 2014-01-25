from django import forms
from dopomoga.models import *
from django.contrib.auth.models import User
from django.utils import timezone

class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class UserProfileForm(forms.ModelForm):
    # description
    first_name = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'placeholder': 'First Name'}), required=False)
    second_name = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'placeholder': 'Second Name'}), required=False)
    picture = forms.ImageField(help_text="Your photo", required=False)
    descr = forms.CharField(max_length=2048, widget=forms.Textarea(attrs={'placeholder': 'Tell us more about you', 'style':'resize:none;width:200px','rows':'10'}), required=False)
    website = forms.URLField(widget=forms.TextInput(attrs={'placeholder': 'Website'}), required=False)
    phone = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Phone'}), required=False)
    place = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'City'}), required=False)
    # characteristics and filters
    resources = forms.ModelMultipleChoiceField(queryset=Resource.objects.all(),widget=forms.CheckboxSelectMultiple()) # Resource,support and needs
    causes = forms.ModelMultipleChoiceField(queryset=Cause.objects.all(),widget=forms.CheckboxSelectMultiple()) # support and needs    

    #LATER
    #AUTO? date_joined = models.DateField(auto_now_add=True)
    #votes = models.IntegerField(default=0)
    #reports = models.IntegerField(default=0) #boolean+number of reports to prioritize the problem

    class Meta:
        model = UserProfile
        fields = ['first_name', 'second_name', 'picture', 'descr', 'website', 'phone', 'place', 'resources', 'causes']

"""
def clean(self):
    cleaned_data = self.cleaned_data
    url = cleaned_data.get('url')

    # If url is not empty and doesn't start with 'http://', prepend 'http://'.
    if url and not url.startswith('http://'):
        url = 'http://' + url
        cleaned_data['url'] = url

    return cleaned_data
class CommentForm(forms.ModelForm):
    comment = forms.CharField(max_length=1024, help_text="Add comment...")
    date_commented = forms.DateField(widget=forms.HiddenInput(), auto_now=False, auto_now_add=True)
    class Meta:
        model = ProjectInneedComment
        fields = ['comment']

class ReviewForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the page.")
    descr = forms.URLField(max_length=2048, help_text="Please enter the URL of the page.")
    date_updated = forms.DateField(widget=forms.HiddenInput(), auto_now=False, auto_now_add=True)
    picture = forms.ImageField(help_text="Select images to upload.", required=False)
    class Meta:
        model = ProjectInneedReview
        fields = ('title', 'descr', 'picture')

"""
