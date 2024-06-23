from django import forms
from .models import Genre, Book, Checkout, Checkin

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'level', 'isbn_code', 'genre']

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Checkout
        fields = ['student_id', 'book', 'checkout_date']
        widgets = {
            'checkout_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['book'].queryset = Book.objects.filter(available_copies__gt=0)

class CheckinForm(forms.ModelForm):
    class Meta:
        model = Checkin
        fields = ['student_id', 'book', 'checkin_date']
        widgets = {
            'checkin_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        student_id = kwargs.pop('student_id', None)
        super().__init__(*args, **kwargs)
        if student_id:
            self.fields['book'].queryset = Checkout.objects.filter(
                student_id=student_id,
                checkin__isnull=True
            ).select_related('book').values_list('book', flat=True)
        else:
            self.fields['book'].queryset = Checkout.objects.none()