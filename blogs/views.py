from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
import datetime
from .form import SignUpForm, ContactForm
from .models import SignUp
# Create your views here.


def home(request):
    form = SignUpForm(request.POST or None)

    now = datetime.datetime.now()
    title = "Welcome you are new user"
    myName = "You are %s" % request.user
    user = request.user

    if request.user.is_authenticated:
        title = "Welcome %s" % request.user.first_name
        myName = "Your name is %s" % request.user.first_name + " " + request.user.last_name

    context = {
        "title": title,
        "myName": myName,
        "form": form,
        "user": user,
        'current_date': now,
    }

    if form.is_valid():

        print(request.POST['email'])
        instance = form.save(commit=False)
        full_name = form.cleaned_data.get("full_name")

        if not full_name:
            full_name = "Fuck"

        instance.full_name = full_name
        instance.save()

        context = {
            "title": "Thanks for registration",
            "myName": myName,
            "user": user,
            'current_date': now,
        }

    if request.user.is_authenticated and request.user.is_staff:
        queryset = SignUp.objects.all()

        # i = 1
        # for instance in SignUp.objects.all():
        #     print(str(i)+".", instance.full_name, ":", instance)
        #     i += 1

        context = {
            'current_date': now,
            "queryset": queryset,
        }

    return render(request, "home.html", context)


def contact(request):
    form = ContactForm(request.POST or None)
    title = "Contact us"

    if form.is_valid():
        form_email = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("message")
        form_full_name = form.cleaned_data.get("full_name")

        Subject = "Mail from Django"
        from_email = settings.EMAIL_HOST_USER
        to_email = [form_email, "example@gmail.com"]

        contact_message = "%s: %s via %s" % (
            form_full_name,
            form_message,
            form_email)

        send_mail(Subject,
                  contact_message,
                  from_email,
                  to_email,
                  fail_silently=True)

    context = {
        "form": form,
        "title": title,
    }

    return render(request, "forms.html", context)


def about(request):
    now = datetime.datetime.now()
    context = {
        "current_date": now
    }
    return render(request, "about.html", context)
