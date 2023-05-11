from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.hashers import check_password  # , make_password
from .forms import ProfileForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.contrib.auth import get_user_model
User = get_user_model()
class SignupFormView(View):

	def get_next(self, pop=True):
		if pop:
			return self.request.session.pop('next', '/')
		else:
			return self.request.session.get('next', '/')

	@property
	def _get_username(self):
		return self.request.POST.get('username')
    
	@property
	def _get_genders(self):
		return self.request.POST.get('genders')
    
	
	@property
	def _get_institute(self):
		return self.request.POST.get('institute')

	@property
	def _get_degree_of_studies(self):
		return self.request.POST.get('degree_of_studies')


	def get(self, request, *args, **kwargs):
		email = ''
		next = self.get_next(pop=False)
		return render(request, 'registers.html', locals())

	@method_decorator(csrf_protect)
	def post(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect(reverse('home'))
    
		email = request.POST.get('email')
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		password1 = request.POST.get('password')
		password2 = request.POST.get('password2')
		birthday= request.POST.get('birthday')
		username = request.POST.get('username')    
        
		if not (email and first_name and last_name):
			msg = _('Falta algun campo')
			messages.error(request, msg)
		elif not (password1 and password2 and password1 == password2):
			msg = _('Contraseña no coincide')
			messages.error(request, msg)
		else:
            
                #Añade la propiedad de genero
			if self._get_genders == 'gender_female':
				gender = '1'
			elif self._get_genders == 'gender_male':
				gender = '2'
			elif self._get_genders == 'gender_other':
				gender = '3'
                

			#Añade la propiedad de instituto
			if self._get_institute == 'inst':
				institute = '1'
			elif self._get_institute == 'org':
				institute = '2'
			elif self._get_institute == 'none':
				institute = '3'

			#Añade la propiedad de estudios
			if self._get_degree_of_studies == 'primaria':
				studies = '1'
			elif self._get_degree_of_studies == 'secundaria':
				studies = '2'
			elif self._get_degree_of_studies == 'preparatoria':
				studies = '3'
			elif self._get_degree_of_studies == 'universidad':
				studies = '4'
			elif self._get_degree_of_studies == 'maestria':
				studies = '5'
			elif self._get_degree_of_studies == 'postgrado':
				studies = '6'
               
			user = User.objects.create(email=email,
										username=username,
										first_name=first_name, 
										last_name=last_name, 
										birthday=birthday,
										genders=gender, 
										institute=institute, 
										degree_of_studies=studies)
			user.set_password(password1)
			user.save()
			login(request, user)
			return redirect('home')
            
		return render(request, 'register.html', locals())
        


class LoginView(View):

    def get_next(self, pop=True):
        if pop:
            return self.request.session.pop('next', '/')
        else:
            return self.request.session.get('next', '/')

    def get(self, request, *args, **kwargs):
        next = self.get_next(pop=False)
        return render(request, 'login.html', locals())

    @method_decorator(csrf_protect)
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse('home'))
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.filter(email=email).first()
        if not user:
            msg = _('Email no registrado')
            messages.error(request, msg)
        elif not user.is_active:
            msg = _('Email no validado')
            messages.error(request, msg)
        elif not check_password(password, user.password):
            msg = _('Contraseña incorrecta')
            messages.error(request, msg)
        else:
            login(request, user, backend="django.contrib.auth.backends.ModelBackend")
            next = self.get_next()
            return redirect(next)
        return render(request, 'login.html', locals())

class LogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        next = request.GET.get('next', '/')
        return redirect(next)

class ProfileView(View):

	@method_decorator(login_required)
	def get(self, request, *args, **kwargs):
		user = User.objects.get(id=request.user.id)
		relationships = Relationship.objects.filter(user=user)
			
		for relationship in relationships:
			print(relationship.work)

		return render(request, 'profile.html', locals())


def follow(request):
	current_user = request.user
	to_work = Work.objects.get()
	to_user_id = to_work
	rel = Relationship(user=current_user, work=to_user_id)
	rel.save()
	messages.success(request, f'sigues a {to_work}')
	return redirect('profile')


def unfollow(request):
	current_user = request.user
	to_work = Work.objects.get()
	to_user_id = to_work
	rel = Relationship.objects.filter(user=current_user.id, work=to_user_id).get()
	rel.delete()
	messages.success(request, f'Ya no sigues a {to_work}')
	return redirect('profile')


class ProfileFormView(View):

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
    	return render(request, 'form_perfil.html', locals())

    @method_decorator(login_required)
    @method_decorator(csrf_protect)
    def post(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user = form.save()
            messages.success(request, ('Información guardada'))
        return render(request, 'profile.html', locals())


