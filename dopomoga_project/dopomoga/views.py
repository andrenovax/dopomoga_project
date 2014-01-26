from django.shortcuts import get_object_or_404, render, render_to_response, redirect 
from django.http import HttpResponse, HttpResponseRedirect 
from django.template import RequestContext 
from dopomoga.models import *
from datetime import datetime 
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required 

def about(request):
    context_dict={}
    return render_to_response('dopomoga/about.html', context_dict, RequestContext(request))

def index(request):
    project_inneed_all = ProjectInneed.objects.order_by('-date_started')[:6]
    project_inneed_all = urlator(project_inneed_all)
    project_helper_all = ProjectHelper.objects.order_by('-date_started')[:6]
    project_helper_all = urlator(project_helper_all)
    context_dict = {'project_inneed_all': project_inneed_all, 'project_helper_all': project_helper_all}
    return render_to_response('dopomoga/index.html', context_dict, RequestContext(request))

"""================================
          LISTS
================================"""

def project_inneed_all(request):
    project_inneed_all = ProjectInneed.objects.order_by('-date_started')
    project_inneed_all = urlator(project_inneed_all)
    context_dict = {'project_inneed_all': project_inneed_all}
    return render_to_response('dopomoga/project_inneed_allpage.html', context_dict, RequestContext(request))

def project_helper_all(request):
    context = RequestContext(request)
    project_helper_all = ProjectHelper.objects.order_by('-date_started')
    project_helper_all = urlator(project_helper_all)
    context_dict = {'project_helper_all': project_helper_all}
    return render_to_response('dopomoga/project_helper_allpage.html', context_dict, RequestContext(request))

def userinneed_all(request):
    userinneed_all = UserInneedProfile.objects.order_by('-date_joined')
    for user in userinneed_all:
        user.numOfproject_inneed_all = user.projects_supported.all().count()#projects in need supported by user
        user.project_part_all = ProjectInneed.objects.filter(users_inneed=user).count()#unique: projects in need user participates    
        """
        Needed? 
        user.numOfproject_helper_all = ProjectHelper.objects.filter(project_author=user).count() #projects helpers created by user
        user.numOfcauses_all = user.causes.all().count() #causes user needs
        user.numOfresources_all = user.resources.all().count() #resources user needs
        # number of users supported
        """
    context_dict = {'userinneed_all': userinneed_all}
    return render_to_response('dopomoga/userinneed_all.html', context_dict, RequestContext(request))

def userhelper_all(request):
    userhelper_all = UserProfile.objects.order_by('-date_joined') #order_by('-number of projects_helper')
    for user in userhelper_all:
        user.numOfcauses_all = user.causes.all().count() #causes user supports
        user.numOfresources_all = user.resources.all().count() #resources user supports
        user.numOfproject_inneed_all = user.projects_supported.all().count()
        """
        Needed? 
        user.numOfproject_helper_all = ProjectHelper.objects.filter(project_author=user).count() #projects helpers created by user
        # number of users supported
        """
    context_dict={'userhelper_all': userhelper_all}
    return render_to_response('dopomoga/userhelper_all.html', context_dict, RequestContext(request))

def resource_all(request):
    resource_all = Resource.objects.all() #order_by('-number of projects_inneed')
    resource_all = urlator(resource_all)
    #count number of
    for resource in resource_all:
        resource.numOfcauses_all = resource.cause_set.all().count() #causes where resource participates
        resource.numOfproject_inneed_all = ProjectInneed.objects.filter(resource=resource).count() #projects inneed that need this resource
        resource.numOfproject_helper_all = ProjectHelper.objects.filter(resource=resource).count() #projects helpers that share this resource
        resource.numOfusers_inneed = UserInneedProfile.objects.filter(projectinneed__resource=resource).count() #users in need
        resource.numOfusers_supported = UserProfile.objects.filter(resources=resource).count() #users supported
    context_dict={'resource_all': resource_all}
    return render_to_response('dopomoga/resource_all.html', context_dict, RequestContext(request))

def cause_all(request):
    cause_all = Cause.objects.all() #order_by('-number of projects_inneed')
    cause_all = urlator(cause_all)
    #count number of
    for cause in cause_all:
        cause.numOfresources_all = cause.resources.all().count() #resources where cause participates
        cause.numOfproject_inneed_all = ProjectInneed.objects.filter(cause=cause).count() #projects inneed that need this cause
        cause.numOfproject_helper_all = ProjectHelper.objects.filter(cause=cause).count() #projects helpers that share this cause
        cause.numOfusers_inneed = UserInneedProfile.objects.filter(projectinneed__cause=cause).count() #users in need
        cause.numOfusers_supported = UserProfile.objects.filter(causes=cause).count() #users supported
    context_dict = {'cause_all': cause_all}
    return render_to_response('dopomoga/cause_all.html', context_dict, RequestContext(request))

"""================================
          ITEMS
================================"""

def project_inneed_item(request, project_name_url):
    project_name = decode_url(project_name_url)
    try:
        project = ProjectInneed.objects.get(name=project_name)
        project = gathered_left_resources(project)
        #relations
        resources_all = project.resource.all()
        causes_all = project.cause.all()
        #create dictionary from realtions
        context_dict={'resources_all':resources_all, 'causes_all':causes_all}       
        context_dict=cd_urlator(context_dict)#add urls to context_dict items
        #add users
        users_inneed = project.users_inneed.all()
        context_dict['users_inneed'] = users_inneed 
        users_supported = UserProfile.objects.filter(projects_supported=project)
        context_dict['users_supported'] = users_supported 
        #comments and reviews
        comments = ProjectInneedComment.objects.filter(project=project)
        context_dict['comments'] = comments
        reviews = ProjectInneedReview.objects.filter(project=project)
        context_dict['reviews'] = reviews 
        #count number of context_dict items
        context_dict=item_counter(context_dict)
        #finally add project to context_dict
        context_dict['project']=project
    except ProjectInneed.DoesNotExist:
        pass
    context_dict['project_name'] = project_name
    context_dict['project_name_url']=project_name_url
    return render_to_response('dopomoga/project_inneed_item.html', context_dict, RequestContext(request))

def project_helper_item(request, project_name_url):
    project_name = decode_url(project_name_url)
    try:
        project = ProjectHelper.objects.get(name=project_name)
        project = gathered_left_resources(project)
        #relations
        resources_all = project.resource.all()
        causes_all = project.cause.all()
        #create dictionary from realtions
        context_dict={'resources_all':resources_all, 'causes_all':causes_all}
        context_dict=cd_urlator(context_dict)#add urls to context_dict items
        #add users
        users_asked = UserInneedProfile.objects.filter(projects_asked=project)
        context_dict['users_asked'] = users_asked 
        #comments and reviews
        comments = ProjectHelperComment.objects.filter(project=project)
        context_dict['comments'] = comments
        reviews = ProjectHelperReview.objects.filter(project=project)
        context_dict['reviews'] = reviews 
        #count number of context_dict items
        context_dict=item_counter(context_dict)
        #add author to dict
        author = project.project_author
        context_dict['author'] = author
        #finally add project to context_dict
        context_dict['project']=project
    except ProjectHelper.DoesNotExist:
        pass
    context_dict['project_name'] = project_name
    context_dict['project_name_url']=project_name_url
    return render_to_response('dopomoga/project_helper_item.html', context_dict, RequestContext(request))

def user_inneed_item(request, user_name_url):
    user_name = decode_url(user_name_url)
    try:
        #userprofile
        usermore = User.objects.get(username=user_name)
        user=UserInneedProfile.objects.get(user=usermore)
        user.password=usermore.password
        user.username=usermore.username
        user.email=usermore.email
        #relations
        project_part_all = ProjectInneed.objects.filter(users_inneed=usermore) #unique: projects in need user participates       
        project_asked_all = user.projects_asked.all() #unique: projects helpers user asked for       
        project_inneed_all = user.projects_supported.all() #projects in need supported by user       
        project_helper_all = ProjectHelper.objects.filter(project_author=usermore) #projects helpers created by user        
        causes_all = user.causes.all()#causes user supports       
        resources_all = user.resources.all()#resources user supports
        #create dictionary from realtions
        context_dict={'project_part_all': project_part_all, 'project_asked_all': project_asked_all, 'project_inneed_all':project_inneed_all,'project_helper_all':project_helper_all, 'causes_all':causes_all, 'resources_all':resources_all}
        context_dict=cd_urlator(context_dict)#add urls to context_dict items
        #comments
        comments = UserInneedComment.objects.filter(author=user)
        context_dict['comments']=comments
        #count number of context_dict items
        context_dict=item_counter(context_dict)
        #finally add user to context_dict
        context_dict['user']=user

    except UserInneedProfile.DoesNotExist:
        pass
    context_dict['user_name'] = user_name
    context_dict['user_name_url'] = user_name_url
    return render_to_response('dopomoga/user_inneed_item.html', context_dict, RequestContext(request))

def user_helper_item(request, user_name_url):
    user_name = decode_url(user_name_url)
    try:
        #userprofile
        usermore = User.objects.get(username=user_name)
        user=UserProfile.objects.get(user=usermore)
        user.password=usermore.password
        user.username=usermore.username
        user.email=usermore.email
        #relations
        project_inneed_all = user.projects_supported.all()#projects in need supported by user
        project_helper_all = ProjectHelper.objects.filter(project_author=usermore)#projects helpers created by user
        causes_all = user.causes.all()#causes user supports
        resources_all = user.resources.all()#resources user supports
        #create dictionary from realtions
        context_dict={ 'project_inneed_all':project_inneed_all,'project_helper_all':project_helper_all, 'causes_all':causes_all, 'resources_all':resources_all}
        context_dict=cd_urlator(context_dict)#add urls to context_dict items
        #comments
        comments = UserProfileComment.objects.filter(author=user)
        context_dict['comments']=comments
        #count number of context_dict items
        context_dict=item_counter(context_dict)
        #finally add user to context_dict
        context_dict['user'] = user
    except UserProfile.DoesNotExist:
        pass
    context_dict['user_name'] = user_name
    context_dict['user_name_url'] = user_name_url
    return render_to_response('dopomoga/user_helper_item.html', context_dict, RequestContext(request))

def resource_item(request, resource_name_url):
    resource_name = decode_url(resource_name_url)
    try:
        resource = Resource.objects.get(name=resource_name)
        project_inneed_all = ProjectInneed.objects.filter(resource=resource)#projects inneed that need this resource
        project_helper_all = ProjectHelper.objects.filter(resource=resource)#projects helpers that share this resource
        causes_all = resource.cause_set.all()#causes in
        #create dictionary from relations
        context_dict={'project_inneed_all':project_inneed_all,'project_helper_all':project_helper_all, 'causes_all':causes_all}
        context_dict=cd_urlator(context_dict)#add urls to context_dict items
        #add users
        users_supported = UserProfile.objects.filter(resources=resource)#users supported
        context_dict['users_supported']=users_supported
        users_inneed = UserInneedProfile.objects.filter(projectinneed__resource=resource)#users in need
        context_dict['users_inneed']=users_inneed
        #comments
        comments = ResourceComment.objects.filter(resource=resource)
        context_dict['comments']=comments
        #count number of context_dict items
        context_dict=item_counter(context_dict)
        #finally add resource to context_dict
        context_dict['resource'] = resource
    except Resource.DoesNotExist:
        pass
    context_dict['resource_name']=resource_name
    context_dict['resource_name_url']=resource_name_url
    return render_to_response('dopomoga/resource_item.html', context_dict, RequestContext(request))

def cause_item(request, cause_name_url):
    cause_name = decode_url(cause_name_url)
    try:
        cause = Cause.objects.get(name=cause_name)
        project_inneed_all = ProjectInneed.objects.filter(cause=cause)#projects inneed that need this cause        
        project_helper_all = ProjectHelper.objects.filter(cause=cause)#projects helpers that share this cause
        resources_all=cause.resources.all()
        #create dictionary from relations
        context_dict={'project_inneed_all':project_inneed_all,'project_helper_all':project_helper_all, 'resources_all':resources_all}        
        context_dict=cd_urlator(context_dict)#add urls to context_dict items
        #add users
        users_supported = UserProfile.objects.filter(causes=cause)#users supported
        context_dict['users_supported']=users_supported
        users_inneed = UserInneedProfile.objects.filter(projectinneed__cause=cause)#users in need
        context_dict['users_inneed']=users_inneed
        #comments
        comments = CauseComment.objects.filter(cause=cause)
        context_dict['comments'] = comments
        #count number of context_dict items
        context_dict=item_counter(context_dict)
        #finally add cause to context_dict
        context_dict['cause'] = cause
    except Cause.DoesNotExist:
        pass
    context_dict['cause_name']= cause_name
    context_dict['cause_name_url']=cause_name_url
    return render_to_response('dopomoga/cause_item.html', context_dict, RequestContext(request))

"""================================
          USER AUTH
================================"""

from dopomoga.forms import UserForm, UserProfileForm

"""REGISTER"""
def register(request):
    logged=False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            login(request, user)
            logged=True
            return HttpResponseRedirect('/dopomoga/')
        else:
            print user_form.errors
            return render_to_response('dopomoga/login.html', {'logged':logged, 'user_form': user_form}, RequestContext(request))
    else:
        user_form = UserForm()
        return render_to_response('dopomoga/login.html', {'logged':logged, 'user_form': user_form}, RequestContext(request))

"""LOGIN"""
def user_login(request):
    logged=False
    if request.method == 'POST':
        username = request.POST['username_login']
        password = request.POST['password_login']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                logged=True
                return HttpResponseRedirect('/dopomoga/')
            else:
                return HttpResponse("Activate your account to sign in")
        else:
            return HttpResponse("Cant find username with this password:(. Please, check your username or password")
    else:
        user_form = UserForm()
        return render_to_response('dopomoga/login.html', {'logged':logged, 'user_form': user_form}, RequestContext(request))

"""LOGOUT"""
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/dopomoga/')

"""================================
          HELP FUNCTIONS
================================"""

def decode_url(encoded_url):
    decoded_url=encoded_url.replace('_', ' ')
    return decoded_url

def encode_url(decoded_url):
    encoded_url=decoded_url.replace(' ', '_')
    return encoded_url


def gathered_left_resources(project):
    """
    under development...
    counts progress of resources gathered for this object

    input: ...
    output: ...
    """
    project.gathered=0#finish later count transactions
    project.res_qnt=1#finish later count transactions
    project.gathered_percent=int(project.gathered)/int(project.res_qnt)
    project.left=int(project.res_qnt)-int(project.gathered)
    return project

def urlator(itemlist):  
    """
    adds urls to every object in list

    input: list of objects
    output: list of objects with urls
    """
    for item in itemlist:
        item.url=item.name.replace(' ', '_')
    return itemlist

def cd_urlator(context_dictionary):
    """
    adds urls to every object in list of objects in context_dictionary

    input: context_dictionary
    output: context_dictionary
    """
    for item in context_dictionary.itervalues():
        item=urlator(item)
    return context_dictionary

def item_counter(context_dictionary):
    """
    counts number of items (resources, causes, projects, etc) related to the particular object

    input: context_dictionary
    output: context_dictionary
    """
    cd_iter=context_dictionary.copy()
    for key,value in cd_iter.iteritems():
        result=value.count()
        num='numOf'+str(key)
        context_dictionary[str(num)] = result
    return context_dictionary