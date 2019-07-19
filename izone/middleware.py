from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect,HttpResponseRedirect
class CustomAuthMiddleware(MiddlewareMixin):
    def process_view(self,request,*args,**kwargs):
        if not request.user.is_authenticated() and request.path != "/accounts/login/":
            return HttpResponseRedirect('/accounts/login/')
