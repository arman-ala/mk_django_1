from django import forms
from.models import Contact, Newsletter


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        # widgets = {
        #     'name': forms.CharField(attrs={'class': 'common-input mb-20 form-control'}),
        #     'email': forms.CharField(attrs={'class': 'common-input mb-20 form-control'}),
        #     'subject': forms.CharField(attrs={'class': 'common-input mb-20 form-control'}),
        #     'message': forms.TextField(attrs={'class': 'common-textarea form-control'}),
        # }


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'