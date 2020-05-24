from django import forms 

class ContactFrom(forms.Form):
	subject = forms.CharField()
	#phone = forms.CharField()
	from_email = forms.EmailField(required=True)
	message = forms.CharField(widget=forms.Textarea, required=True)
