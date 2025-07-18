from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.core.mail import EmailMessage

User = get_user_model()
import logging
logger = logging.getLogger(__name__)

# Create your views here.

class TasksView(LoginRequiredMixin, generic.View):
    def get(self, request):
        try:
            pass
        except Exception as e:
            logger.error(f"{e}")
            return redirect('taskview')
        
        return render(request, 'tasks/tasks.html')