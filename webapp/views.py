from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from .models import Feedback
from django.shortcuts import render, get_object_or_404, redirect
from .models import Tour
from .forms import TourForm



def coursedetails(request,courseid):
    return HttpResponse(courseid)

def homepage(request):
    tours = Tour.objects.all()
    return render(request, 'index.html', {'tours': tours})
    # return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == "POST":
        email = request.POST.get('email')
        description = request.POST.get('des')

         # Ensure both fields are filled out
        if email and description:
            contact = Feedback(email=email, description=description)
            contact.save()
            messages.success(request, "data send successfully")
        else:
            return HttpResponse("Error: Please fill out all fields.")

    # Render the HTML form when method is GET
    return render(request, 'contact.html')

def login(request):
    if request.method == 'POST':
        # Retrieve the form data
        username = request.POST.get('name')  # Use 'name' because your input field's name attribute is 'name'
        password = request.POST.get('password')  # Use 'password' because your input field's name attribute is 'password'

         # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:    
            auth_login(request, user)  # Log in the user
            return redirect('dashboard')  # Redirect to the dashboard
        else:
            # If authentication fails, send an error message
            messages.error(request, "Invalid username or password")
            return redirect('login')
    
    return render(request, 'templates/login.html')  # Render the login page for GET requests
    
@login_required(login_url='/login/') # Redirects to login page if not authenticated
def dashboard(request):
     if request.user.is_superuser:  # Check if the logged-in user is a superuser
        # users = User.objects.all()  # Fetch all users from the database
        
        # Fetch all users excluding superusers
        users = User.objects.filter(is_superuser=False)
        return render(request, 'dashboard.html', {'users': users})  # Render the dashboard with    
     else:
        users = None  # Non-superusers won't see any data
        return render(request, 'templates/dashboard.html', {'users': users})

def signin(request):
    if request.method == 'POST':
        # Get form data from the request
        username = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        number = request.POST.get('number')
        confirm_password = request.POST.get('cpassword')
        
        # Validate the form data
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('signin')
        
        try:
            # Create a new user
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, "Account created successfully!")
            
        except IntegrityError:
            messages.error(request, "Username already exists. Please choose another one.")
            return redirect('signin')
        
        else:
            # If authentication fails, send an error message
            messages.error(request, "fill up the field")
            return redirect('signin')

    return render(request, 'templates/signin.html')

def logout_view(request):
    logout(request)
    return redirect('homepage')

def feedback(request):
            feedbacks = Feedback.objects.all()  # Fetch all feedbacks from the database
            return render(request, 'feedback.html', {'feedbacks': feedbacks})
            # return render(request,'feedback.html')

def delete_feedback(request, pk):
    feedback = get_object_or_404(Feedback, pk=pk)
    feedback.delete()
    return redirect('feedback')  # Redirect to the feedback list page after deleting




def about(request):
    return render(request,'about.html')

@login_required(login_url='/login/')
def tour(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        title = request.POST.get('title')
        description = request.POST.get('description')

        # Save the tour data to the database
        Tour.objects.create(image=image, title=title, description=description)

        # Redirect to the viewtour page after saving
        return redirect('viewtour')

    # Fetch all tours to display in a table
    tours = Tour.objects.all()

    # Render the page with the tours and form
    return render(request, 'tour.html', {'tours': tours})

@login_required(login_url='/login/')
def viewtour(request):
    tours = Tour.objects.all()
    return render(request, 'viewtour.html', {'tours': tours})


@login_required(login_url='/login/')
def book(request):
    # return render(request,'book.html')
    # tour = Tour.objects.all().values('title')
    # return render(request, 'book.html', {'tours': tours})
    title = request.GET.get('title')  # Extract title from query parameter
    tour = Tour.objects.filter(title=title).first() if title else None

    context = {'tour': tour}
    return render(request, 'book.html', context)



def delete_tour(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    tour.delete()  # This deletes the tour from the database
    return redirect('viewtour')  # Redirect to the list page after deletion




def update_tour(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)  # Fetch the tour instance by ID

    if request.method == 'POST':
        form = TourForm(request.POST, request.FILES, instance=tour)  # Pass instance to the form
        if form.is_valid():
            form.save()
            return redirect('viewtour')  # Redirect after updating
    else:
        form = TourForm(instance=tour)  # Pre-populate form with tour data

    return render(request, 'tour.html', {'form': form, 'tour': tour})
