from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from .models import Step, Cycle, Program, MotorSetting, GeneralSetting
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm, ProgramFormClass, CycleFormClass, StepFormClass
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProgramSerializer



class AllProgramsView (LoginRequiredMixin, generic.ListView):
    template_name = 'programs/index.html'
    context_object_name = 'programs_list'

    def get_queryset(self):
         user = self.request.user
         queryset = Program.objects.filter(user=user)
         return queryset


class ProgramDetailView (LoginRequiredMixin, generic.DetailView):
    model = Program
    template_name = 'programs/program.html'


@login_required
def favourite(request, program_id):
    program = get_object_or_404(Program, pk=program_id)
    program.is_favourite=True;
    program.save()
    return render(request, 'programs/program.html', {'program': program})

@login_required
def unfavourite(request, program_id):
    program = get_object_or_404(Program, pk=program_id)
    program.is_favourite=False;
    program.save()
    return render(request, 'programs/program.html', {'program': program})


class ProgramCreate(LoginRequiredMixin, CreateView):
    model = Program
    form_class = ProgramFormClass


class ProgramUpdate(LoginRequiredMixin, UpdateView):
    model = Program
    form_class = ProgramFormClass


class ProgramDelete(LoginRequiredMixin,DeleteView):
    model = Program
    success_url = reverse_lazy('programs:index')


class CycleCreate(LoginRequiredMixin, CreateView):
    model = Cycle
    form_class = CycleFormClass


class CycleUpdate(LoginRequiredMixin, UpdateView):
    model = Cycle
    form_class = CycleFormClass


class CycleDelete(LoginRequiredMixin, DeleteView):
    model = Cycle
    success_url = reverse_lazy('programs:index')


class StepCreate(LoginRequiredMixin, CreateView):
    model = Step
    form_class = StepFormClass


class StepUpdate(LoginRequiredMixin, UpdateView):
    model = Step
    form_class = StepFormClass


class StepDelete(LoginRequiredMixin,DeleteView):
    model = Step
    success_url = reverse_lazy('programs:index')

#the following view regulates users registration
class UserFormView(View):
    form_class = UserForm
    template_name = 'programs/registration_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    #process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            #storing the data but NOT SAVING them to db yet
            user = form.save(commit=False)

            #cleaning and normalizing data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            #saving to db
            user.save()

            #if credentials are correct, this returns a user object
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:

                    login(request, user)
                    return redirect('programs:index')

        return render(request, self.template_name, {'form': form})

#class che gestisce la richiesta API di tipo GET e POST (post al momento non attivato, vedi pass) per tutti i programmi associati ad un Utente
class AllProgramsApi(APIView):

    def get(self, request):
        user = self.request.user
        userprograms = Program.objects.filter(user=user)
        serializer = ProgramSerializer(userprograms, many=True)
        return Response(serializer.data)

    def post(self):
        pass
