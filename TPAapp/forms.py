from django import forms
from .models import Student,Feedback


# contact form
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)

# student registration form
class Student_RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(max_length=255, widget=forms.PasswordInput())

    class Meta: 
        model = Student
        fields = ['name', 'prn', 'email', 'password']

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords don't match")
        return confirm_password
 

class Student_LoginForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=255)
    password = forms.CharField(label='Password', max_length=255, widget=forms.PasswordInput())


class FeedbackForm(forms.Form):
    prn = forms.CharField(max_length=20)
    date = forms.DateField()
    question1 = forms.CharField(max_length=10)
    question2 = forms.CharField(max_length=10)
    question3 = forms.CharField(max_length=10)
    question4 = forms.CharField(max_length=10)
    question5 = forms.CharField(max_length=10)
    question6 = forms.CharField(max_length=10)


class Mechanics_Feedback(forms.Form):
    prn = forms.CharField(max_length=20)
    date = forms.DateField()
    question1 = forms.CharField(max_length=10)
    question2 = forms.CharField(max_length=10)
    question3 = forms.CharField(max_length=10)
    question4 = forms.CharField(max_length=10)
    question5 = forms.CharField(max_length=10)
    question6 = forms.CharField(max_length=10)

class CP_Feedback(forms.Form):
    prn = forms.CharField(max_length=20)
    date = forms.DateField()
    question1 = forms.CharField(max_length=10)
    question2 = forms.CharField(max_length=10)
    question3 = forms.CharField(max_length=10)
    question4 = forms.CharField(max_length=10)
    question5 = forms.CharField(max_length=10)
    question6 = forms.CharField(max_length=10)
    
class BE_Feedback(forms.Form):
    prn = forms.CharField(max_length=20)
    date = forms.DateField()
    question1 = forms.CharField(max_length=10)
    question2 = forms.CharField(max_length=10)
    question3 = forms.CharField(max_length=10)
    question4 = forms.CharField(max_length=10)
    question5 = forms.CharField(max_length=10)
    question6 = forms.CharField(max_length=10)
    
class DIP_Feedback(forms.Form):
    prn = forms.CharField(max_length=20)
    date = forms.DateField()
    question1 = forms.CharField(max_length=10)
    question2 = forms.CharField(max_length=10)
    question3 = forms.CharField(max_length=10)
    question4 = forms.CharField(max_length=10)
    question5 = forms.CharField(max_length=10)
    question6 = forms.CharField(max_length=10)
    
    
# Teachers Pages

class Teacher_LoginForm(forms.Form):
    email = forms.CharField(label='subject_code', max_length=255)
    password = forms.CharField(label='Password', max_length=255, widget=forms.PasswordInput())
    
# attendance 

class AttendanceForm(forms.Form):
    date = forms.DateField(label='Date', widget=forms.DateInput(attrs={'type': 'date'}))
    present_students = forms.IntegerField(label='Present Students', widget=forms.NumberInput(attrs={'placeholder': 'Present Students'}))
    total_students = forms.IntegerField(label='Total Students', initial=60, widget=forms.NumberInput(attrs={'readonly': 'readonly'}))
    
class CP_AttendanceForm(forms.Form):
    date = forms.DateField(label='Date', widget=forms.DateInput(attrs={'type': 'date'}))
    present_students = forms.IntegerField(label='Present Students', widget=forms.NumberInput(attrs={'placeholder': 'Present Students'}))
    total_students = forms.IntegerField(label='Total Students', initial=60, widget=forms.NumberInput(attrs={'readonly': 'readonly'}))

class MECH_AttendanceForm(forms.Form):
    date = forms.DateField(label='Date', widget=forms.DateInput(attrs={'type': 'date'}))
    present_students = forms.IntegerField(label='Present Students', widget=forms.NumberInput(attrs={'placeholder': 'Present Students'}))
    total_students = forms.IntegerField(label='Total Students', initial=60, widget=forms.NumberInput(attrs={'readonly': 'readonly'}))

class DIP_AttendanceForm(forms.Form):
    date = forms.DateField(label='Date', widget=forms.DateInput(attrs={'type': 'date'}))
    present_students = forms.IntegerField(label='Present Students', widget=forms.NumberInput(attrs={'placeholder': 'Present Students'}))
    total_students = forms.IntegerField(label='Total Students', initial=60, widget=forms.NumberInput(attrs={'readonly': 'readonly'}))

class BE_AttendanceForm(forms.Form):
    date = forms.DateField(label='Date', widget=forms.DateInput(attrs={'type': 'date'}))
    present_students = forms.IntegerField(label='Present Students', widget=forms.NumberInput(attrs={'placeholder': 'Present Students'}))
    total_students = forms.IntegerField(label='Total Students', initial=60, widget=forms.NumberInput(attrs={'readonly': 'readonly'}))



# results


class CA1Form(forms.Form):
    prn_ca1 = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'PRN Number'}))
    marks_ca1 = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Marks'}))
    out_of_ca1 = forms.IntegerField(initial=10, widget=forms.NumberInput(attrs={'readonly': 'readonly'}))

class CA2Form(forms.Form):
    prn_ca2 = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'PRN Number'}))
    marks_ca2 = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Marks'}))
    out_of_ca2 = forms.IntegerField(initial=10, widget=forms.NumberInput(attrs={'readonly': 'readonly'}))

class MidSemesterForm(forms.Form):
    prn_midsem = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'PRN Number'}))
    marks_midsem = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Marks'}))
    out_of_midsem = forms.IntegerField(initial=20, widget=forms.NumberInput(attrs={'readonly': 'readonly'}))

class EndSemesterForm(forms.Form):
    prn_endsem = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'PRN Number'}))
    marks_endsem = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Marks'}))
    out_of_endsem = forms.IntegerField(initial=60, widget=forms.NumberInput())

# cp_results

class CP_CA1Form(forms.Form):
    prn_ca1 = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'PRN Number'}))
    marks_ca1 = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Marks'}))
    out_of_ca1 = forms.IntegerField(initial=10, widget=forms.NumberInput(attrs={'readonly': 'readonly'}))

class CP_CA2Form(forms.Form):
    prn_ca2 = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'PRN Number'}))
    marks_ca2 = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Marks'}))
    out_of_ca2 = forms.IntegerField(initial=10, widget=forms.NumberInput(attrs={'readonly': 'readonly'}))

class CP_MidSemesterForm(forms.Form):
    prn_midsem = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'PRN Number'}))
    marks_midsem = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Marks'}))
    out_of_midsem = forms.IntegerField(initial=20, widget=forms.NumberInput(attrs={'readonly': 'readonly'}))

class CP_EndSemesterForm(forms.Form):
    prn_endsem = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'PRN Number'}))
    marks_endsem = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Marks'}))
    out_of_endsem = forms.IntegerField(initial=60, widget=forms.NumberInput())

# mech_results


class MECH_CA1Form(forms.Form):
    prn_ca1 = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'PRN Number'}))
    marks_ca1 = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Marks'}))
    out_of_ca1 = forms.IntegerField(initial=10, widget=forms.NumberInput(attrs={'readonly': 'readonly'}))

class MECH_CA2Form(forms.Form):
    prn_ca2 = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'PRN Number'}))
    marks_ca2 = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Marks'}))
    out_of_ca2 = forms.IntegerField(initial=10, widget=forms.NumberInput(attrs={'readonly': 'readonly'}))

class MECH_MidSemesterForm(forms.Form):
    prn_midsem = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'PRN Number'}))
    marks_midsem = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Marks'}))
    out_of_midsem = forms.IntegerField(initial=20, widget=forms.NumberInput(attrs={'readonly': 'readonly'}))

class MECH_EndSemesterForm(forms.Form):
    prn_endsem = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'PRN Number'}))
    marks_endsem = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Marks'}))
    out_of_endsem = forms.IntegerField(initial=60, widget=forms.NumberInput())

# dip results
class DIP_CA1Form(forms.Form):
    prn_ca1 = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'PRN Number'}))
    marks_ca1 = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Marks'}))
    out_of_ca1 = forms.IntegerField(initial=10, widget=forms.NumberInput(attrs={'readonly': 'readonly'}))

class DIP_CA2Form(forms.Form):
    prn_ca2 = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'PRN Number'}))
    marks_ca2 = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Marks'}))
    out_of_ca2 = forms.IntegerField(initial=10, widget=forms.NumberInput(attrs={'readonly': 'readonly'}))

class DIP_MidSemesterForm(forms.Form):
    prn_midsem = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'PRN Number'}))
    marks_midsem = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Marks'}))
    out_of_midsem = forms.IntegerField(initial=20, widget=forms.NumberInput(attrs={'readonly': 'readonly'}))

class DIP_EndSemesterForm(forms.Form):
    prn_endsem = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'PRN Number'}))
    marks_endsem = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Marks'}))
    out_of_endsem = forms.IntegerField(initial=60, widget=forms.NumberInput())

# be

class BE_CA1Form(forms.Form):
    prn_ca1 = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'PRN Number'}))
    marks_ca1 = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Marks'}))
    out_of_ca1 = forms.IntegerField(initial=10, widget=forms.NumberInput(attrs={'readonly': 'readonly'}))

class BE_CA2Form(forms.Form):
    prn_ca2 = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'PRN Number'}))
    marks_ca2 = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Marks'}))
    out_of_ca2 = forms.IntegerField(initial=10, widget=forms.NumberInput(attrs={'readonly': 'readonly'}))

class BE_MidSemesterForm(forms.Form):
    prn_midsem = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'PRN Number'}))
    marks_midsem = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Marks'}))
    out_of_midsem = forms.IntegerField(initial=20, widget=forms.NumberInput(attrs={'readonly': 'readonly'}))

class BE_EndSemesterForm(forms.Form):
    prn_endsem = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'PRN Number'}))
    marks_endsem = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Marks'}))
    out_of_endsem = forms.IntegerField(initial=60, widget=forms.NumberInput())



class Admin_LoginForm(forms.Form):
    dept_code = forms.IntegerField(label='dept_code')
    password = forms.CharField(label='Password', max_length=255, widget=forms.PasswordInput())