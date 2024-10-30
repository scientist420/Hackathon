from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import Hackathon
from .forms import HackathonForm

def home(request):
    return render(request,'index.html')

def hackathon_details(request, pk):
    # Fetch the hackathon by its primary key
    hackathon = get_object_or_404(Hackathon, pk=pk)

    # Pass the hackathon object to the template
    context = {
        'hackathon': hackathon,
    }

    return render(request, 'hackathon_details.html', context)

@login_required(login_url='/login/')
def register_hackathon(request):
    return render(request,'register.html')

from django.shortcuts import render, redirect
from .forms import RegistrationForm  # Or the form you're using

from django.shortcuts import render, redirect
from .forms import RegistrationForm  


def submit_registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Process the form data (e.g., save it to the database)
            return redirect('home')  # Redirect to a success page or home
    else:
        form = RegistrationForm()
    
    return render(request, 'register.html', {'form': form})



def view_submission(request):
    return render(request,'view_submisions.html')


def create_hackathon(request):
    if request.method == 'POST':
        form = HackathonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('some_view_name')  # Redirect to a success page or another view
    else:
        form = HackathonForm()

    return render(request, 'create_hackathon.html', {'form': form})