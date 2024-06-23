from django.shortcuts import render,redirect
from .models import Teacher,Student
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from .forms import GenreForm, BookForm, CheckoutForm, CheckinForm
from .models import Genre, Book, Checkout, Checkin
import logging
from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Count
from .models import Checkout, Genre
from datetime import datetime

# Create your views here.
def signup(request):
    if request.method == 'POST':
        Username = request.POST['Username']
        teacher_name = request.POST['teacher_name']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            return redirect('signup')

        if Teacher.objects.filter(Username=Username).exists():
            return redirect('signup')

        user = Teacher.objects.create(Username=Username, teacher_name=teacher_name,password=password) # Use Django's method to set the password
        user.save()

        return redirect('login')
        
    return render(request,'teacher_form.html')

def login(request):
    if request.method=='POST':
        Username = request.POST['Username']
        password = request.POST['password']

        user=Teacher.objects.get(Username=Username,password=password)
        if user:
            return redirect(dashboard)
        else:
            return render(request,'login.html')
        
    return render(request,'login.html')

def student_form(request):
    if request.method=='POST':
        name=request.POST.get('name')
        grade=request.POST.get('grade')
        level=request.POST.get('level')
        teacher=request.POST.get('teacher')

        tech=Teacher.objects.get(id=teacher)
        print(tech)
        user=Student.objects.create(name=name,grade=grade,level=level,teacher=tech)
        user.save()
        if user:
            return redirect(dashboard)
        else:
            return HttpResponse("error")
    teachers = Teacher.objects.all()
    return render(request, 'student_form.html', {'teachers': teachers})


def home(request):
    return render(request,'index.html')


logger = logging.getLogger(__name__)

def add_genre(request):
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = GenreForm()
    return render(request, 'add_genre.html', {'form': form})

def dashboard(request):
    return render(request,'dashboard.html')

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(dashboard)
    else:
        form = BookForm()
    genres = Genre.objects.all()
    return render(request, 'add_book.html', {'form': form, 'genres': genres})

def checkout_view(request):
    checkout_form = CheckoutForm()
    if request.method == 'POST':
        checkout_form = CheckoutForm(request.POST)
        if checkout_form.is_valid():
            check = checkout_form.save(commit=False)
            book = check.book
            if book.available_copies > 0:
                book.available_copies -= 1
                book.save()
                check.save()
                logger.debug(f"Checked out: {check}")
            return redirect(dashboard)
    return render(request, 'checkout.html', {'checkout_form': checkout_form})

def checkin_view(request):
    checkin_form = CheckinForm()
    if request.method == 'POST':
        if 'search_student' in request.POST:
            student_id = request.POST.get('student_id')
            checkin_form = CheckinForm(student_id=student_id)
            checkin_form.fields['student_id'].initial = student_id
            return render(request, 'checkin.html', {'checkin_form': checkin_form})
        elif 'checkin_submit' in request.POST:
            checkin_form = CheckinForm(request.POST)
            if checkin_form.is_valid():
                student_id = checkin_form.cleaned_data['student_id']
                book = checkin_form.cleaned_data['book']
                checkin_date = checkin_form.cleaned_data['checkin_date']
                logger.debug(f"Check-in submit: student_id={student_id}, book={book}, checkin_date={checkin_date}")
                try:
                    checkout_instance = Checkout.objects.get(
                        student_id=student_id,
                        book=book,
                        checkin__isnull=True
                    )
                    checkin_instance = Checkin(
                        student_id=student_id,
                        book=book,
                        checkin_date=checkin_date
                    )
                    checkin_instance.save()
                    book.available_copies += 1
                    book.save()
                    logger.debug(f"Checked in: {checkin_instance}")
                except ObjectDoesNotExist:
                    logger.error(f"No such checkout record found for student_id={student_id}, book={book}")
                    checkin_form.add_error(None, 'No such checkout record found for check-in.')
                return redirect('checkin_view')
    return render(request, 'checkin.html', {'checkin_form': checkin_form})




def get_checkouts_by_genre(request):
    if request.method == 'GET' and 'from_date' in request.GET and 'to_date' in request.GET:
        from_date = request.GET.get('from_date')
        to_date = request.GET.get('to_date')

        if not from_date or not to_date:
            return JsonResponse({'status': 'error', 'message': 'Both from_date and to_date are required.'})

        try:
            from_date = datetime.strptime(from_date, '%Y-%m-%d')
            to_date = datetime.strptime(to_date, '%Y-%m-%d')
        except ValueError:
            return JsonResponse({'status': 'error', 'message': 'Invalid date format. Use YYYY-MM-DD.'})

        checkouts = Checkout.objects.filter(checkout_date__range=(from_date, to_date)) \
                    .values('book__genre__name') \
                    .annotate(checkout_count=Count('id')) \
                    .order_by('book__genre__name')

        data = {
            'genres': [checkout['book__genre__name'] for checkout in checkouts],
            'checkout_counts': [checkout['checkout_count'] for checkout in checkouts]
        }

        return JsonResponse({'status': 'success', 'data': data})

    return render(request, 'checkouts_by_genre.html')


def profile(request):
    return render(request,'studentprofile.html')

