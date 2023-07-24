from django.shortcuts import redirect
from django.urls import reverse

def login_required(redirect_to='/login/'):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated:
                return view_func(request, *args, **kwargs)
            else:
                if redirect_to is None:
                    return redirect('login')  # Redirect to the login page by default
                else:
                    return redirect(reverse(redirect_to))
        return _wrapped_view
    return decorator