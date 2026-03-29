from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Complaint
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

def file_complaint(request):
    if request.method == 'POST':
        complaint = Complaint.objects.create(
            name=request.POST['name'],
            village=request.POST['village'],
            category=request.POST['category'],
            description=request.POST['description'],
            mobile=request.POST['mobile']
        )
        return render(request, 'success.html', {'id': complaint.complaint_id})
    return render(request, 'complaint_form.html')

def track_status(request):
    if request.method == 'POST':
        cid = request.POST['cid']
        try:
            complaint = Complaint.objects.get(complaint_id=cid)
            return render(request, 'status.html', {'complaint': complaint})
        except:
            return render(request, 'status.html', {'error': 'Invalid ID'})
    return render(request, 'track.html')

def dashboard(request):
    complaints = Complaint.objects.all().order_by('-created_at')
    return render(request, 'dashboard.html', {'complaints': complaints})

def officer_login(request):
    if request.method == 'POST':
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('officer_dashboard')
        else:
            return render(request, 'officer_login.html', {'error': 'Invalid Login'})
    return render(request, 'officer_login.html')

@login_required
def officer_dashboard(request):
    complaints = Complaint.objects.all()
    if request.method == 'POST':
        cid = request.POST['cid']
        status = request.POST['status']
        complaint = Complaint.objects.get(id=cid)
        complaint.status = status
        complaint.save()
    return render(request, 'officer_dashboard.html', {'complaints': complaints})

def officer_logout(request):
    logout(request)
    return redirect('home')