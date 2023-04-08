from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from authentication.models import User, Warn
from .forms import SignUpForm, LoginForm

group, created = Group.objects.get_or_create(name='verified')

def can_verify(user):
    return user.groups.filter(name__in=['moderator', 'administrator']).exists()

def can_assignmod(user):
    return user.groups.filter(name__in=['administrator']).exists()

@login_required
@user_passes_test(can_verify, login_url='/feeds/')
def verify_user(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        verified_group = Group.objects.get(name='verified')
        if user.groups.filter(name='verified').exists():
            user.groups.remove(verified_group)
        else:
            user.groups.add(verified_group)
        return redirect('user_group', user.id)
    else:
        return render(request, 'authentication/user_group_verify.html', {'user': user})

@login_required
@user_passes_test(can_assignmod, login_url='/feeds/')
def assignmod(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        moderator_group = Group.objects.get(name='moderator')
        if user.groups.filter(name='moderator').exists():
            user.groups.remove(moderator_group)
        else:
            user.groups.add(moderator_group)
        return redirect('user_group', user.id)
    else:
        return render(request, 'authentication/user_group_moderator.html', {'user': user})



def logout_view(request):
    logout(request)


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "authentication/signup.html"


@login_required
def custom_logout(request):
    logout(request)
    return redirect("login")


def sign_in(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect("/")
        form = LoginForm()
        return render(request, 'authentication/login.html', {'form': form})

    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                messages.success(request, f'Erfolgreich angemeldet!')
                return redirect('feeds')

        messages.error(request, f'Benutzername oder Passwort ist falsch.')
        return render(request, 'authentication/login.html', {'form': form})


class UsersView(generic.ListView):
    model = User
    fields = ['first_name', 'last_name', 'username', 'email', 'password', 'birthdate', 'verified']
    template_name = 'authentication/users.html'


class UserView(generic.DetailView):
    model = User
    template_name = 'authentication/user.html'


class UserCommentariesView(generic.DetailView):
    model = User
    template_name = 'authentication/user_commentaries.html'


class UserWarnsView(generic.DetailView):
    model = User
    template_name = 'authentication/user_warns.html'


def redirectURL(request):
    return redirect('feeds')


class UserUpdateView(generic.UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'username', 'email', 'birthdate']
    template_name = "authentication/user_update.html"

    def get_success_url(self):
        return reverse_lazy('user', args=[self.object.pk])

    def form_valid(self, form):
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update'] = True
        return context


def user_delete(request, pk):
    user = User.objects.get(pk=pk)

    if request.method == 'POST':
        user.delete()
        return redirect('feeds')
    return (request, 'authentication/user_delete.html', {'user': user})


class WarnCreateView(generic.CreateView):
    model = Warn
    fields = ['reason']
    template_name = "authentication/warn_create.html"

    def get_success_url(self):
        return reverse_lazy('user_warns', kwargs={"pk": self.kwargs.get('user_id')})

    def get_current_user(self, **kwargs):
        return User.objects.get(id=self.kwargs.get('user_id'))

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        user = self.get_current_user(**kwargs)
        data.update({'user': user})
        return data

    def form_valid(self, form):
        form.instance.user = self.get_current_user(**self.kwargs)
        return super().form_valid(form)


def warn_delete(request, pk):
    warn = get_object_or_404(Warn, pk=pk)

    if request.method == 'POST':
        user_id = warn.user.id
        warn.delete()
        return redirect('user_warns', pk=user_id)
    return JsonResponse({'success': False})


class UserUpdateGroupDetail(generic.DetailView):
    model = User
    template_name = 'authentication/user_group.html'