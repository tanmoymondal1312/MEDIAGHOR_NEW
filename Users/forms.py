from django import forms
from .models import CourseRegistration

class CourseRegistrationForm(forms.ModelForm):
    class Meta:
        model = CourseRegistration
        fields = ['full_name', 'age', 'phone_number', 'email', 
                  'educational_qualification', 'programming_experience', 'message']
        
        widgets = {
            'full_name': forms.TextInput(attrs={
                'placeholder': 'আপনার নাম লিখুন',
                'required': True
            }),
            'age': forms.NumberInput(attrs={
                'min': 13,
                'max': 100,
                'placeholder': 'বয়স',
                'required': True
            }),
            'phone_number': forms.TextInput(attrs={
                'placeholder': '01XXXXXXXXX',
                'pattern': '[0-9]{11}',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'your@email.com',
                'required': True
            }),
            'educational_qualification': forms.Select(attrs={
                'required': True
            }),
            'programming_experience': forms.Select(),
            'message': forms.Textarea(attrs={
                'placeholder': 'আপনার কোনো প্রশ্ন থাকলে লিখুন...',
                'rows': 3
            }),
        }
        
        labels = {
            'full_name': 'পূর্ণ নাম *',
            'age': 'বয়স *',
            'phone_number': 'ফোন নাম্বার *',
            'email': 'ইমেইল *',
            'educational_qualification': 'শিক্ষাগত যোগ্যতা *',
            'programming_experience': 'প্রোগ্রামিং অভিজ্ঞতা',
            'message': 'বার্তা বা প্রশ্ন',
        }
    
    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number')
        if phone and len(phone) != 11:
            raise forms.ValidationError('ফোন নাম্বারটি অবশ্যই 11 ডিজিটের হতে হবে।')
        return phone
    
    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age and (age < 13 or age > 100):
            raise forms.ValidationError('বয়স 13 থেকে 100 বছরের মধ্যে হতে হবে।')
        return age