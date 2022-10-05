from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenicated_user(view_func):
  def wrapper_func(request, *args, **kwargs):
    if request.user.is_authenticated: 
      return redirect('home')
    else:
      return view_func(request, *args, **kwargs)
  return wrapper_func

def allowed_users(allowed_roles=[]):
  def decorator(cbv_func):
    def wrapper_func(request, *args, **kwargs):

      group = None
      if request.user.groups.exists():
        group = request.user.group.all()[0]
      if group in allowed_roles:
        return cbv_func
      else:
        return HttpResponse('You are not authorised to view this page')
    print('Working', allowed_roles)
    return wrapper_func
  return decorator 