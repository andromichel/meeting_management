from django.shortcuts import redirect

def root_redirect(request):
    return redirect('login')  # Adjust the URL name as needed
