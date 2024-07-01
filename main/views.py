from .forms import CustomUserCreationForm, ReservationForm, ReviewForm, BranchForm, ServiceForm
from .models import Review, Reservation, Service, Branch
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.http import require_http_methods

# Tambahkan variabel global untuk menyimpan ulasan
reviews = []

# Create your views here.

def home(request):
    if request.method == 'POST':
        if 'reservation_submit' in request.POST:
            reservation_form = ReservationForm(request.POST)
            if reservation_form.is_valid():
                reservation = reservation_form.save(commit=False)
                reservation.user = request.user
                reservation.save()
                messages.success(request, 'Reservation submitted successfully!')
                return redirect('home')
        elif 'review_submit' in request.POST:
            review_form = ReviewForm(request.POST)
            if review_form.is_valid():
                review_form.save()
                messages.success(request, 'Review submitted successfully!')
                return redirect('home')
    else:
        reservation_form = ReservationForm()
        review_form = ReviewForm()

    reviews = Review.objects.all().order_by('-created_at')
    context = {
        'reservation_form': reservation_form,
        'review_form': review_form,
        'reviews': reviews,
    }
    return render(request, 'main/home.html', context)

def add_review(request):
    if request.method == "POST":
        customer_name = request.POST.get("customerName")
        star_rating = request.POST.get("starRating")
        comment = request.POST.get("comment")
        
        review = {
            "customerName": customer_name,
            "starRating": star_rating,
            "comment": comment
        }
        
        reviews.append(review)
        messages.success(request, "Review added successfully!")
        return redirect("home")
    return redirect("home")

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def customer_dashboard(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'main/customer_dashboard.html', {'reservations': reservations})

def is_admin(user):
    return user.is_authenticated and user.role == 'admin'

def make_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            messages.success(request, 'Reservation made successfully!')
            return redirect('customer_dashboard')
    else:
        form = ReservationForm()
        form.fields['service'].queryset = Service.objects.all()
    
    return render(request, 'main/make_reservation.html', {'form': form})

def get_services(request):
    branch_id = request.GET.get('branch')
    print(f"Received request for branch_id: {branch_id}")
    services = Service.objects.filter(branch_id=branch_id)
    print(f"Services found: {list(services.values('id', 'name'))}")
    return JsonResponse(list(services.values('id', 'name')), safe=False)

@user_passes_test(is_admin)
def admin_dashboard(request):
    branch_form = BranchForm()
    service_form = ServiceForm()

    if request.method == 'POST':
        if 'add_branch' in request.POST:
            branch_form = BranchForm(request.POST)
            if branch_form.is_valid():
                branch_form.save()
                messages.success(request, 'Branch added successfully!')
                return redirect('admin_dashboard')
        elif 'add_service' in request.POST:
            service_form = ServiceForm(request.POST)
            if service_form.is_valid():
                service_form.save()
                messages.success(request, 'Service added successfully!')
                return redirect('admin_dashboard')
        elif 'delete_branch' in request.POST:
            branch_id = request.POST.get('delete_branch')
            Branch.objects.filter(id=branch_id).delete()
            messages.success(request, 'Branch deleted successfully!')
            return redirect('admin_dashboard')
        elif 'delete_service' in request.POST:
            service_id = request.POST.get('delete_service')
            Service.objects.filter(id=service_id).delete()
            messages.success(request, 'Service deleted successfully!')
            return redirect('admin_dashboard')
    
    branches = Branch.objects.all()
    services = Service.objects.all()
    context = {
        'branch_form': branch_form,
        'service_form': service_form,
        'branches': branches,
        'services': services,
    }
    return render(request, 'main/admin_dashboard.html', context)

def get_services(request):
    branch_id = request.GET.get('branch')
    print(f"Received request for branch_id: {branch_id}")
    services = Service.objects.filter(branch_id=branch_id).values('id', 'name')
    print(f"Services found: {list(services)}")
    return JsonResponse(list(services), safe=False)

def get_branch_hours(request):
    branch_id = request.GET.get('branch')
    branch = Branch.objects.get(id=branch_id)
    return JsonResponse({
        'opening_time': branch.opening_time.strftime('%H:%M'),
        'closing_time': branch.closing_time.strftime('%H:%M'),
    })

@require_http_methods(["GET", "POST"])
def custom_logout(request):
    logout(request)
    return redirect('home')