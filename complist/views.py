from django.views import generic
from .models import Comp
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm

class IndexView(generic.ListView):
    template_name = 'complist/index.html'

    def get_queryset(self):
        return Comp.objects.all()

class DetailView(generic.DetailView):
    model = Comp
    template_name = 'complist/detail.html'

class UserFormView(View):
    form_class = UserForm
    template_name = 'complist/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(email=email, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('complist:templates')

        return render(request, self.template_name, {'form': form})









