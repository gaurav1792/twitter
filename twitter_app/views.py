from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.contrib.auth.models import User
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from twitter_app.forms import Login, SignUp, TweetForm
from twitter_app.models import Tweet

# Create your views here.

def index(request, auth_form=None, user_form=None):
    # User is logged in
    if request.user.is_authenticated():
        tweet_form = TweetForm()
        user = request.user
        tweets_self = Tweet.objects.filter(user=user.id)
        tweets_followers = Tweet.objects.filter(user__userprofile__in=user.profile.follows.all)
        tweets = tweets_self | tweets_followers
        return render(request,
                      'dashboard.html',
                      {'tweet_form': tweet_form, 'user': user,
                       'tweets': tweets,
                       'next_url': '/', })
    else:
        # User is not logged in
        auth_form = auth_form or Login()
        user_form = user_form or SignUp()
 
        return render(request,
                      'home.html',
                      {'auth_form': auth_form, 'user_form': user_form, })

def login_view(request):
    if request.method == 'POST':
        form = Login(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            # Success
            return redirect('/')
        else:
            # Failure
            return index(request, auth_form=form)
    return redirect('/')
 
 
def logout_view(request):
    logout(request)
    return redirect('/')


def signup(request):
    user_form = SignUp(data=request.POST)
    if request.method == 'POST':
        if user_form.is_valid():
            username = user_form.clean_username()
            password = user_form.clean_password2()
            user_form.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            return index(request, user_form=user_form)
    return redirect('/')

	
@login_required
def public(request, tweet_form=None):
    tweet_form = tweet_form or TweetForm()
    tweets = Tweet.objects.reverse()[:10]
    return render(request,
                  'public.html',
                  {'tweet_form': tweet_form, 'next_url': '/tweets',
                   'tweets': tweets, 'username': request.user.username})


@login_required
def submit(request):
    if request.method == "POST":
        tweet_form = TweetForm(data=request.POST)
        next_url = request.POST.get("next_url", "/")
        if tweet_form.is_valid():
            tweet = tweet_form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect(next_url)
        else:
            return public(request, tweet_form)
    return redirect('/')


def get_latest(user):
    try:
        return user.tweet_set.order_by('id').reverse()[0]
    except IndexError:
        return ""


@login_required
def users(request, username="", tweet_form=None):
    if username:
        # Show a profile
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise Http404
        tweets = Tweet.objects.filter(user=user.id)
        if username == request.user.username or request.user.profile.follows.filter(user__username=username):
            # Self Profile
            return render(request, 'user.html', {'user': user, 'tweets': tweets, })
        return render(request, 'user.html', {'user': user, 'tweets': tweets, 'follow': True, 'unfollow': True, })
    users = User.objects.all().annotate(tweet_count=Count('tweet'))
    tweets = map(get_latest, users)
    obj = zip(users, tweets)
    tweet_form = tweet_form or TweetForm()
    return render(request,
                  'profiles.html',
                  {'obj': obj, 'next_url': '/users/',
                   'tweet_form': tweet_form,
                   'username': request.user.username, 'follow': True, 'unfollow': True,})


@login_required
def following(request, auth_form=None, user_form=None):
    # User is logged in
    #if request.user.is_authenticated():
        tweet_form = TweetForm()
        user = request.user
        tweets_self = Tweet.objects.filter(user=user.id)
        user_followers = user__userprofile__in=user.profile.follows.all
        tweets = user_followers
        return render(request,
                      'following.html',
                      {'tweet_form': tweet_form, 'user': user,
                       'tweets': tweets,
                       'next_url': '/', })
    #else:
        # User is not logged in
    #    auth_form = auth_form or Login()
     #   user_form = user_form or SignUp()
 
      #  return render(request,
       #               'home.html',
        #              {'auth_form': auth_form, 'user_form': user_form, })


				   
@login_required
def follow(request):
    if request.method == "POST":
        follow_id = request.POST.get('follow', False)
        if follow_id:
            try:
                user = User.objects.get(id=follow_id)
                request.user.profile.follows.add(user.profile) #adding user in follow list
            except ObjectDoesNotExist: #if user does not exist more
                return redirect('/users/') #redirecting after unsuccessful follow
    return redirect('/users/') #redirecting after successful follow

	
@login_required
def retweet(request):
    if request.method == "POST":
        tweet_form = TweetForm(data=request.POST)
        next_url = request.POST.get("next_url", "/")
        if tweet_form.is_valid():
            tweet = tweet_form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('/users/')
        else:
            return redirect(next_url)
    
	
@login_required	
def unfollow(request): #unfollow any user
    if request.method == "POST":
        unfollow_id = request.POST.get('unfollow', False) 
        if unfollow_id:
            try:
                user = User.objects.get(id=unfollow_id) # geting user to unfollow
                request.user.profile.follows.remove(user.profile) #removing user 
            except ObjectDoesNotExist:
                return redirect('/users/') 
    return redirect('/users/')	