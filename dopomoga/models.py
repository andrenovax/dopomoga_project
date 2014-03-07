from django.db import models

#  Create your models here.
from django.contrib.auth.models import User
from dopomoga_project.settings.basic import STATIC_URL
import os


DEFAULT_IMAGE_PATH = os.path.join(STATIC_URL, 'img/default.jpg')
"""
CONTENT:
1. Project
2. Review
3. Comment

4. Project inneed + Review + Comment
5. Project inneed + Review + Comment

6. Resource + Comment
7. Cause + Comment
8. UserProfile
9. UserInneed  + Comment
10. UserHelper + Comment
"""

# ======================================
     # PROJECT
# ======================================


class Project(models.Model):
     # relations
    project_author = models.ForeignKey(User)
    resource = models.ManyToManyField('Resource')
    cause = models.ManyToManyField('Cause')
     # description
    name = models.CharField(max_length=128, unique=True)
    descr = models.CharField(max_length=2048)
    how_to_help = models.CharField(max_length=2048, null=True, blank=True, default="")
    picture = models.ImageField(upload_to='project_images', blank=True, default=DEFAULT_IMAGE_PATH)
    website = models.URLField(null=True, blank=True)
    phone = models.IntegerField(default=0, null=True, blank=True)
    place = models.CharField(max_length=256)
     # status
    res_qnt = models.IntegerField(default=0)
    funded = models.BooleanField(default=False)
    date_started = models.DateField(auto_now_add=True)
    date_finished = models.DateField(auto_now=True)
    votes = models.IntegerField(default=0)  # aka likes up and down sum
     # bad project?
    reports = models.IntegerField(default=0)  # number of reports to prioritize the problem

    def __unicode__(self):
        return self.name


class Review(models.Model):
     # relations
    project = models.ForeignKey(Project)
     # description
    title = models.CharField(max_length=128, null=True, blank=True)
    descr = models.CharField(max_length=2048, null=True, blank=True)
    pictures = models.ImageField(upload_to='project_descr_images', null=True, blank=True, default=DEFAULT_IMAGE_PATH)
     # status
    date_updated = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.title


class Comment(models.Model):
     # relations
    author = models.ForeignKey(User)
     # description
    comment = models.CharField(max_length=512)
     # status
    date_commented = models.DateField(auto_now_add=True)
    votes = models.IntegerField(default=0)  # aka likes, up and down sum
     # bad comment?
    reports = models.IntegerField(default=0)  # number of reports to prioritize the problem

    def __unicode__(self):
        return self.id


#PROJECT IN NEED
class ProjectInneed(Project):
     # relations
    users_inneed = models.ManyToManyField('UserInneedProfile', null=True, blank=True)  # users in need supported by this project
     # documents
    docs_descr = models.CharField(max_length=2048, blank=True)
    docs_pics = models.ImageField(upload_to='project_docs_images', blank=True)

    def __unicode__(self):
        return self.name


class ProjectInneedReview(Review):
    def __unicode__(self):
        return self.title


class ProjectInneedComment(Comment):
     # relations
    project = models.ForeignKey(Project)

    def __unicode__(self):
        return self.id


#PROJECT HELPER
class ProjectHelper(Project):
    def __unicode__(self):
        return self.name


class ProjectHelperReview(Review):
    def __unicode__(self):
        return self.title


class ProjectHelperComment(Comment):
     # relations
    project = models.ForeignKey(Project)

    def __unicode__(self):
        return self.id

#======================================
    #RESOURCE models
#======================================


class Resource(models.Model):
     # description
    name = models.CharField(max_length=128, unique=True)
    descr = models.CharField(max_length=2048, blank=True)
    picture = models.ImageField(upload_to='resource_images', blank=True, default=DEFAULT_IMAGE_PATH)
    icon = models.ImageField(upload_to='icons', blank=True)

    def __unicode__(self):
        return self.name


class ResourceComment(Comment):
     # relations
    resource = models.ForeignKey(Resource)

    def __unicode__(self):
        return self.id

#======================================
    #CAUSES models
#======================================


class Cause(models.Model):
     # relations
    resources = models.ManyToManyField(Resource, null=True, blank=True)  # delete it
     # description
    name = models.CharField(max_length=128, unique=True)
    descr = models.CharField(max_length=2048, blank=True)
    picture = models.ImageField(upload_to='cause_images', blank=True, default=DEFAULT_IMAGE_PATH)

    def __unicode__(self):
        return self.name


class CauseComment(Comment):
     # relations
    cause = models.ForeignKey(Cause)

    def __unicode__(self):
        return self.id

#======================================
        #USERS models
#======================================


class UserProfile(models.Model):
    #  relations
    user = models.OneToOneField(User)
    resources = models.ManyToManyField(Resource, null=True, blank=True)  # that user supports
    causes = models.ManyToManyField(Cause, null=True, blank=True)  # that user supports
    projects_supported = models.ManyToManyField(ProjectInneed, null=True, blank=True)  # that user supported
    # description
    first_name = models.CharField(max_length=128, blank=True)
    second_name = models.CharField(max_length=128, blank=True)
    descr = models.CharField(max_length=2048, blank=True)
    picture = models.ImageField(upload_to='project_images', null=True, blank=True, default=DEFAULT_IMAGE_PATH)
    website = models.URLField(blank=True)
    phone = models.IntegerField(default=0, null=True, blank=True)
    place = models.CharField(max_length=256, blank=True)
    # status
    date_joined = models.DateField(auto_now_add=True)
    # bad user? number of reports to prioritize the problem
    reports = models.IntegerField(default=0)

    def __unicode__(self):
        return self.user.username


class UserProfileComment(Comment):
     #  relations
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.id


class UserInneedProfile(UserProfile):
    #  relations
    projects_asked = models.ManyToManyField(ProjectHelper, null=True, blank=True)  # that user asked for support

    def __unicode__(self):
        return self.user.username


class UserInneedComment(Comment):
     #  relations
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.id
