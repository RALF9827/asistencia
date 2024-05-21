from django.shortcuts import redirect

class Mx_Superuser(object):
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return redirect('index')
    
class Mx_General(object):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if (request.user.is_active and request.user.is_superuser == False and request.user.is_staff == False) or request.user.is_superuser:
                return super().dispatch(request, *args, **kwargs)
        return redirect('index')
