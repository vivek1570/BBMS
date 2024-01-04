from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from . models import person,donor,receive





class EditProfileForm(UserChangeForm):
	
	password = forms.CharField(label="", widget=forms.TextInput(attrs={'type':'hidden'}))
	class Meta:
		model = User
		#excludes private information from User
		fields = ('username', 'first_name', 'last_name', 'email','password',)
		  



class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}), )
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))
	
	
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

		def __init__(self, *args, **kwargs):
			super(SignUpForm, self).__init__(*args, **kwargs)
			self.fields['username'].widget.attrs['class'] = 'form-control'
			self.fields['username'].widget.attrs['placeholder'] = 'User Name'
			self.fields['username'].label = ''
			self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

			self.fields['password1'].widget.attrs['class'] = 'form-control'
			self.fields['password1'].widget.attrs['placeholder'] = 'Password'
			self.fields['password1'].label = ''
			self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

			self.fields['password2'].widget.attrs['class'] = 'form-control'
			self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
			self.fields['password2'].label = ''
			self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'						



class DateInput(forms.DateInput):
    input_type = 'date'

class person_form(forms.ModelForm):
    # Define the gender choices
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    # Add the gender field to the form
    p_gender = forms.ChoiceField(choices=GENDER_CHOICES, label='Gender')

    class Meta:
        model = person
        fields = '__all__'
       
        labels = {
            'p_name': "Name",
            'p_phone': "Phone Number",
            'p_b_group': "Blood Group",
            'p_add': "Address",
            'p_age': "Age",
            'p_loc': "Location",
        }
class donor_form(forms.ModelForm):
    class Meta:
        model=donor
        fields=['p_id','d_quantity']
        widgets={
            'booking_date':DateInput(),
        }

        labels={
            'd_name':"Name",
            'd_phone':"Phone Number",
            'd_b_group':"Blood Group",
            'd_quantity':"Blood Units",
            'p_id':"Person Id",
        }

class receive_form(forms.ModelForm):
    class Meta:
        model=receive
        fields=['r_b_group','r_quantity']
        labels={
            'r_b_group':"Blood Group",
            'r_quantity':"Blood Units",
        }

class search_form(forms.ModelForm):
      class Meta:
            model=donor
            fields=['d_b_group']
        #     widgets = {
        #     'd_b_group': forms.Select(attrs={'style': 'font-weight: bold;'}),
        # }
        #     d_b_group = forms.ChoiceField(
        #     choices=[('A', 'A'), ('B', 'B'), ('AB', 'AB'), ('O', 'O')],
        #     widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select Blood Group'}),
        #     required=False  # Set required to False to remove the asterisk
        # )
            labels={
                  'd_b_group':"Blood Group",
            }

            
