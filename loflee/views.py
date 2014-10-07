from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from dating import settings
from loflee.forms import CustomUserCreationForm
from loflee.models import User


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def register(request):
    if request.method == 'POST':
        print request.FILES.keys()
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            print form.cleaned_data
            # form.save()

            #send email to thank registring
            user = form.save()
            print user.profile_image

            # user.email_user("Welcome!", "Thank you for signing up for our website.")
            text_content = 'Thank you for signing up for our website, {}'.format(user.username)
            html_content = '<h2>Thanks {} for signing up!</h2> <div>I hope you enjoy using our site</div>'.format(user.username)
            msg = EmailMultiAlternatives("Welcome!", text_content, settings.DEFAULT_FROM_EMAIL, [user.email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            # messages.info(request, "Thanks for registering. You are now logged in.")
            new_user = authenticate(username=request.POST['username'],
                                    password=request.POST['password1'])
            login(request, new_user)

            return redirect("profile")
    else:
        form = CustomUserCreationForm()

    return render(request, "registration/register.html", {
        'form': form,
    })


@login_required
def profile(request):

    data = {'current_user': request.user, 'viewed_user': request.user}
    return render(request, 'profile.html', data)


@login_required
def seeprofiles(request):
    userdata = User.objects.all()
    names = []
    # for row in userdata:
    #     names.append(row.name)
    #names = [row.name for row in userdata]
    data = {"userdata": userdata}
    return render(request, 'seeprofiles.html', data)

@login_required
def seeprofile(request, user_id):
    user = User.objects.get(id=user_id)
    data = {'current_user': request.user, 'viewed_user': user}
    # data ={"user":user}
    return render(request, 'profile.html', data)

@login_required
def chat(request, sender, receiver):

    data = {"sender": sender, "receiver": receiver}
    return render(request, 'chat.html', data)