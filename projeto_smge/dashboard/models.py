# Modelos das tabelas do banco projeto_sge
from __future__ import unicode_literals
import datetime

from django.db import models
from django.utils import timezone


from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(_('email address'), unique=True)
	first_name = models.CharField(_('first name'), max_length=30, blank=True)
	last_name = models.CharField(_('last name'), max_length=30, blank=True)
	date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
	is_active = models.BooleanField(_('active'), default=True)
	is_staff = models.BooleanField(_('staff'), default=True)
	avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

	objects = UserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	class Meta:
		verbose_name = _('user')
		verbose_name_plural = _('users')

	def get_full_name(self):
		'''
		Returns the first_name plus the last_name, with a space in between.
		'''
		full_name = '%s %s' % (self.first_name, self.last_name)
		return full_name.strip()

	def get_short_name(self):
		'''
		Returns the short name for the user.
		'''
		return self.first_name

	def email_user(self, subject, message, from_email=None, **kwargs):
		'''
		Sends an email to this User.
		'''
		send_mail(subject, message, from_email, [self.email], **kwargs)
		
		



class Concessionaria(models.Model):
	def __str__(self):
		return self.nome
	nome = models.CharField(max_length=255)
	hp_inicio = models.DateTimeField('hp inicio')
	hp_fim = models.DateTimeField('hp fim')
	

class Cliente_has_concessionaria(models.Model):
	id_cliente = models.ForeignKey(User, on_delete=models.CASCADE)
	id_concessionaria = models.ForeignKey(Concessionaria, on_delete=models.CASCADE)
	
	
class Classificacao(models.Model):
	def __str__(self):
		return self.nome
	nome = models.CharField(max_length=255)
	id_concessionaria = models.ForeignKey(Concessionaria, on_delete=models.CASCADE)
	
	
class Transdutor(models.Model):
	def __str__(self):
		return (self.numero_serie)
	data_instalacao = models.DateTimeField('Data instalacao')
	numero_serie = models.CharField(max_length=255)
	id_cliente = models.ForeignKey(User, on_delete=models.CASCADE)
	id_classificacao = models.ForeignKey(Classificacao, on_delete=models.CASCADE)
	
	
class Servico(models.Model):
	def __str__(self):
		return self.descricao
	descricao = models.CharField(max_length=255)
	valor = models.CharField(max_length=255)
	id_classificacao = models.ForeignKey(Classificacao, on_delete=models.CASCADE)
	

class Coleta(models.Model):
	data_instalacao = models.DateTimeField('data')
	hora_instalacao = models.DateTimeField('hora')
	saida1 = models.CharField(max_length=255)
	saida2 = models.CharField(max_length=255)
	saida3 = models.CharField(max_length=255)
	saida4 = models.CharField(max_length=255)
	saida5 = models.CharField(max_length=255)
	saida6 = models.CharField(max_length=255)
	saida7 = models.CharField(max_length=255)
	saida8 = models.CharField(max_length=255)
	id_transdutor = models.ForeignKey(Transdutor, on_delete=models.CASCADE)
	

class Conta_contrato(models.Model):
	conta_contrato = models.CharField(max_length=255)
	id_cliente = models.ForeignKey(User, on_delete=models.CASCADE)
	
	
class Imposto(models.Model):
	def __str__(self):
		return self.nome
	nome = models.CharField(max_length=255)
	estado = models.CharField(max_length=255)
	valor = models.CharField(max_length=255)
	

class Constante(models.Model):
	def __str__(self):
		return self.nome
	nome = models.CharField(max_length=255)
	valor = models.CharField(max_length=255)