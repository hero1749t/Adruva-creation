from django.shortcuts import render,get_object_or_404,redirect
from .models import Service,Portfolio,Testimonial
from django.http import HttpResponse
# Create your views here.


def home(request):
    services = Service.objects.all()[:3]
    portfolios = Portfolio.objects.all()[:3]
    testimonials = Testimonial.objects.filter(is_approved=True)[:4]

    return render(request, 'home.html', {
        'services': services,
        'portfolios': portfolios,
        'testimonials': testimonials
    })


def services_list(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})


def service_detail(request, id):
    service = get_object_or_404(Service, id=id)
    return render(request, 'service_detail.html', {'service': service})

def portfolio_list(request):
    portfolios = Portfolio.objects.all()
    return render(request, 'portfolio.html', {'portfolios': portfolios})

def portfolio_detail(request, id):
    portfolio = get_object_or_404(Portfolio, id=id)
    return render(request, 'portfolio_detail.html', {'portfolio': portfolio})
# All Testimonials Page
def all_testimonials(request):
    testimonials = Testimonial.objects.filter(is_approved=True)
    return render(request, 'all_testimonials.html', {'testimonials': testimonials})


# Add Feedback Page
def add_feedback(request):
    if request.method == "POST":
        name = request.POST.get('name')
        company = request.POST.get('company')
        message = request.POST.get('message')
        rating = request.POST.get('rating')
        image = request.FILES.get('image')

        Testimonial.objects.create(
            name=name,
            company=company,
            message=message,
            rating=rating,
            image=image,
            is_approved=False
        )

        return redirect('home')

    return render(request, 'add_feedback.html')
from .models import Contact

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        Contact.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message
        )

        return render(request, 'contact.html', {'success': True})

    return render(request, 'contact.html')
