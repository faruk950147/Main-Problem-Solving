from django.shortcuts import render
from django.views import generic
# Create your views here.

class Sign_up(generic.View):
    def get(self, request):
        return render(request, 'account/sign_up.html')
class Sign_in(generic.View):
    def get(self, request):
        return render(request, 'account/sign_in.html')
class Sign_out(generic.View):
    def get(self, request):
        return render(request, 'account/sign_out.html')
