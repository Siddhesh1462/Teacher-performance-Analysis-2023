from django.shortcuts import render,redirect
from .forms import ContactForm,Student_RegistrationForm,Student_LoginForm,FeedbackForm,Mechanics_Feedback,CP_Feedback,BE_Feedback,DIP_Feedback,AttendanceForm,CP_AttendanceForm,MECH_AttendanceForm,DIP_AttendanceForm,BE_AttendanceForm,CA1Form,CA2Form,MidSemesterForm,EndSemesterForm
from .models import Contact,Student,Feedback,Mechanics_Table,CP_Table,BE_Table,DIP_Table,Attendance,CP_Attendance,MECH_Attendance,DIP_Attendance,BE_Attendance,CA1,CA2,MidSemester,EndSemester
from django.contrib import messages


# from django.contrib.auth.models import User
from django.contrib.auth import login
import logging
logger = logging.getLogger(__name__)





# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Do something with the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Save the form data to the database
            # Assuming you have a Contact model in your models.py file
            contact = Contact(name=name, email=email, message=message)
            contact.save()
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

# registration
from django.contrib.auth.hashers import make_password

def student_registration(request):
    print("Student registration view function called")
    
    # Check the number of registered students
    registered_students_count = Student.objects.count()
    if registered_students_count > 60:
        messages.error(request, 'Registration limit reached. Please try again later.')
        return redirect('student_login')
    
    if request.method == 'POST':
        form = Student_RegistrationForm(request.POST)
        print("Form data:", request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            prn = form.cleaned_data['prn']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            hashed_password = make_password(password)
            # Save the hashed password to the database
            
            student = Student(name=name, prn=prn, email=email, password=hashed_password)
            student.save()
            
            # msg to display
            messages.success(request, 'Registration successful!')
            
            return redirect('student_login')
    else:
        form = Student_RegistrationForm()
    
    return render(request, 'student_registration.html', {'form': form})






# student login
from django.contrib.auth.hashers import check_password

def student_login(request):
    if request.method == 'POST':
        form = Student_LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            # Check if the user with the entered email exists
            try:
                student = Student.objects.get(email=email)
            except Student.DoesNotExist:
                student = None
            
            if student is not None and check_password(password, student.password):
                # Passwords match, log in the user
                login(request, student)
                
                # Store the student's name in a variable for the welcome message
                student_name = student.name
                
                # Pass the student_name to the template context
                return render(request, 'student_home.html', {'student_name': student_name})
            else:
                # Passwords don't match or user doesn't exist, display error message
                form.add_error(None, 'Incorrect email or password.')
    else:
        form = Student_LoginForm()
    return render(request, 'student_login.html', {'form': form})   



# student home page


def student_home(request):
    return render(request, 'student_home.html')

# student feedback page
def student_feedback(request):
    return render(request,"student_feedback.html")

from datetime import datetime

def mathematics_one(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            form_data = form.cleaned_data

            prn = form_data['prn']
            date = form_data['date']
            
            # Check if the student has already given feedback for today
            feedback_count = Feedback.objects.filter(prn=prn, date=date).count()
            if feedback_count > 0:
                # Student has already given feedback for today
                messages.success(request, 'You have already given feedback for today!')
                return render(request, 'student_home.html')

            feedback = Feedback(
                prn=form_data['prn'],
                date=form_data['date'],
                question1=form_data['question1'],
                question2=form_data['question2'],
                question3=form_data['question3'],
                question4=form_data['question4'],
                question5=form_data['question5'],
                question6=form_data['question6'],
            )
            feedback.save()
            messages.success(request, 'Your feedback is successfully submited!')
            return redirect('student_home')  # Redirect to a success page
    else:
        form = FeedbackForm()
    
    return render(request, 'mathematics_one.html', {'form': form})


def mechanics(request):
    if request.method == 'POST':
        form = Mechanics_Feedback(request.POST)
        if form.is_valid():
            # Save the form data to the database
            form_data = form.cleaned_data

            prn = form_data['prn']
            date = form_data['date']

            # Check if the student has already given feedback this week
            feedback_count = Mechanics_Table.objects.filter(prn=prn, date=date).count()
            if feedback_count > 0:
                # Student has already given feedback this week
                messages.success(request, 'You already given a feedback for today!')
                return render(request, 'student_home.html')
            mechanics_table = Mechanics_Table(
                prn=form_data['prn'],
                date=form_data['date'],
                question1=form_data['question1'],
                question2=form_data['question2'],
                question3=form_data['question3'],
                question4=form_data['question4'],
                question5=form_data['question5'],
                question6=form_data['question6'],
            )
            mechanics_table.save()
            messages.success(request, 'Your feedback is successfully submited!')
            return redirect('student_home')  # Redirect to a success page
    else:
        form = Mechanics_Feedback()
    
    return render(request, 'mechanics.html', {'form': form})

def comp_programming(request):
    if request.method == 'POST':
        form = CP_Feedback(request.POST)
        if form.is_valid():
            # Save the form data to the database
            form_data = form.cleaned_data

            prn = form_data['prn']
            date = form_data['date']

            # Check if the student has already given feedback this week
            feedback_count = CP_Table.objects.filter(prn=prn, date=date).count()
            if feedback_count > 0:
                # Student has already given feedback this week
                messages.success(request, 'You already given a feedback for today!')
                return render(request, 'student_home.html')
            cp_table = CP_Table(
                prn=form_data['prn'],
                date=form_data['date'],
                question1=form_data['question1'],
                question2=form_data['question2'],
                question3=form_data['question3'],
                question4=form_data['question4'],
                question5=form_data['question5'],
                question6=form_data['question6'],
            )
            cp_table.save()
            messages.success(request, 'Your feedback is successfully submited!')
            return redirect('student_home')  # Redirect to a success page
    else:
        form = CP_Feedback()
    
    return render(request, 'comp_programming.html', {'form': form})

def basic_electronics(request):
    if request.method == 'POST':
        form = BE_Feedback(request.POST)
        if form.is_valid():
            # Save the form data to the database
            form_data = form.cleaned_data

            prn = form_data['prn']
            date = form_data['date']

            # Check if the student has already given feedback this week
            feedback_count = BE_Table.objects.filter(prn=prn, date=date).count()
            if feedback_count > 0:
                # Student has already given feedback this week
                messages.success(request, 'You already given a feedback for today!')
                return render(request, 'student_home.html')
            be_table = BE_Table(
                prn=form_data['prn'],
                date=form_data['date'],
                question1=form_data['question1'],
                question2=form_data['question2'],
                question3=form_data['question3'],
                question4=form_data['question4'],
                question5=form_data['question5'],
                question6=form_data['question6'],
            )
            be_table.save()
            messages.success(request, 'Your feedback is successfully submited!')
            return redirect('student_home')  # Redirect to a success page
    else:
        form = BE_Feedback()
    
    return render(request, 'basic_electronics.html', {'form': form})

def dip(request):
    if request.method == 'POST':
        form = DIP_Feedback(request.POST)
        if form.is_valid():
            # Save the form data to the database
            form_data = form.cleaned_data

            prn = form_data['prn']
            date = form_data['date']

            # Check if the student has already given feedback this week
            feedback_count = DIP_Table.objects.filter(prn=prn, date=date).count()
            if feedback_count > 0:
                # Student has already given feedback this week
                messages.success(request, 'You already given a feedback for today!')
                return render(request, 'student_home.html')
            dip_table = DIP_Table(
                prn=form_data['prn'],
                date=form_data['date'],
                question1=form_data['question1'],
                question2=form_data['question2'],
                question3=form_data['question3'],
                question4=form_data['question4'],
                question5=form_data['question5'],
                question6=form_data['question6'],
            )
            dip_table.save()
            messages.success(request, 'Your feedback is successfully submited!')
            return redirect('student_home')  # Redirect to a success page
    else:
        form = BE_Feedback()
    
    return render(request, 'dip.html', {'form': form})


# Teachers_login

from django.db import connection

def teacher_login(request):
    if request.method == 'POST':
        subject_code = request.POST['subject_code']
        password = request.POST['password']
        
        # Query the database to check if the provided subject code and password match
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, name FROM Teachers WHERE subject_code=%s AND password=%s", [subject_code, password])
            result = cursor.fetchone()
        
        if result is None:
            return render(request, 'index.html', {'error': 'Invalid subject code or password.'})
        
        teacher_id = result[0]
        teacher_name = result[1]
        
        # Store the teacher's ID in the session for authentication
        request.session['teacher_id'] = teacher_id
        
        # Render different templates based on the subject code
        if subject_code == 'EXTCCP':
            return render(request, 'cp_teacher_home.html', {'teacher_name': teacher_name})
        elif subject_code == 'EXTCBE':
            return render(request, 'be_teacher_home.html', {'teacher_name': teacher_name})
        elif subject_code == 'EXTCM1':
            return render(request, 'm1_teacher_home.html', {'teacher_name': teacher_name})
        elif subject_code == 'EXTCDIP':
            return render(request, 'dip_teacher_home.html', {'teacher_name': teacher_name})
        elif subject_code == 'EXTCMECH':
            return render(request, 'mech_teacher_home.html', {'teacher_name': teacher_name})
        else:
            return render(request, 'index.html', {'error': 'Invalid subject code.'})
    
    return render(request, 'teacher_login.html')



from .models import Student

def m1_teacher_home(request):
    num_students = Student.objects.all().count()
    return render(request, 'm1_teacher_home.html', {'num_students': num_students})

def cp_teacher_home(request):
    num_students = Student.objects.all().count()
    return render(request, 'cp_teacher_home.html', {'num_students': num_students})

def mech_teacher_home(request):
    num_students = Student.objects.all().count()
    return render(request, 'mech_teacher_home.html', {'num_students': num_students})

def be_teacher_home(request):
    num_students = Student.objects.all().count()
    return render(request, 'be_teacher_home.html', {'num_students': num_students})

def dip_teacher_home(request):
    num_students = Student.objects.all().count()
    return render(request, 'dip_teacher_home.html', {'num_students': num_students})

# attendance form
def add_attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            attendance = Attendance(
                date=form.cleaned_data['date'],
                present_students=form.cleaned_data['present_students'],
                total_students=form.cleaned_data['total_students']
            )
            attendance.save()

            # Display success message
            messages.success(request, 'Attendance added successfully!')

            return redirect('attendance')  # Replace 'home' with your desired redirect URL
    else:
        form = AttendanceForm()

    return render(request, 'attendance.html', {'form': form})

def cp_attendance(request):
    if request.method == 'POST':
        form = CP_AttendanceForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            cp_attendance = CP_Attendance(
                date=form.cleaned_data['date'],
                present_students=form.cleaned_data['present_students'],
                total_students=form.cleaned_data['total_students']
            )
            cp_attendance.save()

            # Display success message
            messages.success(request, 'Attendance added successfully!')

            return redirect('cp_attendance')  # Replace 'home' with your desired redirect URL
    else:
        form = CP_AttendanceForm()

    return render(request, 'cp_attendance.html', {'form': form})

def mech_attendance(request):
    if request.method == 'POST':
        form = MECH_AttendanceForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            mech_attendance = MECH_Attendance(
                date=form.cleaned_data['date'],
                present_students=form.cleaned_data['present_students'],
                total_students=form.cleaned_data['total_students']
            )
            mech_attendance.save()

            # Display success message
            messages.success(request, 'Attendance added successfully!')

            return redirect('mech_attendance')  # Replace 'home' with your desired redirect URL
    else:
        form = MECH_AttendanceForm()

    return render(request, 'mech_attendance.html', {'form': form})

def dip_attendance(request):
    if request.method == 'POST':
        form = DIP_AttendanceForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            dip_attendance = DIP_Attendance(
                date=form.cleaned_data['date'],
                present_students=form.cleaned_data['present_students'],
                total_students=form.cleaned_data['total_students']
            )
            dip_attendance.save()

            # Display success message
            messages.success(request, 'Attendance added successfully!')

            return redirect('dip_attendance')  # Replace 'home' with your desired redirect URL
    else:
        form = DIP_AttendanceForm()

    return render(request, 'dip_attendance.html', {'form': form})

def be_attendance(request):
    if request.method == 'POST':
        form = BE_AttendanceForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            be_attendance = BE_Attendance(
                date=form.cleaned_data['date'],
                present_students=form.cleaned_data['present_students'],
                total_students=form.cleaned_data['total_students']
            )
            be_attendance.save()

            # Display success message
            messages.success(request, 'Attendance added successfully!')

            return redirect('be_attendance')  # Replace 'home' with your desired redirect URL
    else:
        form = BE_AttendanceForm()

    return render(request, 'be_attendance.html', {'form': form})

from django.shortcuts import render, redirect
from .forms import CA1Form, CA2Form, MidSemesterForm, EndSemesterForm
from .models import CA1, CA2, MidSemester, EndSemester

def add_results(request):
    if request.method == 'POST':
        form_name = request.POST.get('form_name')
        
        if form_name == 'ca1':
            form = CA1Form(request.POST)
            if form.is_valid():
                prn_ca1 = form.cleaned_data['prn_ca1']
                marks_ca1 = form.cleaned_data['marks_ca1']
                out_of_ca1 = form.cleaned_data['out_of_ca1']
                
                ca1_instance = CA1(prn_ca1=prn_ca1, marks_ca1=marks_ca1, out_of_ca1=out_of_ca1)
                ca1_instance.save()
                
                return redirect('results')
                
        elif form_name == 'ca2':
            form = CA2Form(request.POST)
            if form.is_valid():
                prn_ca2 = form.cleaned_data['prn_ca2']
                marks_ca2 = form.cleaned_data['marks_ca2']
                out_of_ca2 = form.cleaned_data['out_of_ca2']
                
                ca2_instance = CA2(prn_ca2=prn_ca2, marks_ca2=marks_ca2, out_of_ca2=out_of_ca2)
                ca2_instance.save()
                
                return redirect('results')
                
        elif form_name == 'mid_semester':
            form = MidSemesterForm(request.POST)
            if form.is_valid():
                prn_midsem = form.cleaned_data['prn_midsem']
                marks_midsem = form.cleaned_data['marks_midsem']
                out_of_midsem = form.cleaned_data['out_of_midsem']
                
                midsem_instance = MidSemester(prn_midsem=prn_midsem, marks_midsem=marks_midsem, out_of_midsem=out_of_midsem)
                midsem_instance.save()
                
                return redirect('results')
                
        elif form_name == 'end_semester':
            form = EndSemesterForm(request.POST)
            if form.is_valid():
                prn_endsem = form.cleaned_data['prn_endsem']
                marks_endsem = form.cleaned_data['marks_endsem']
                out_of_endsem = form.cleaned_data['out_of_endsem']
                
                endsem_instance = EndSemester(prn_endsem=prn_endsem, marks_endsem=marks_endsem, out_of_endsem=out_of_endsem)
                endsem_instance.save()
                print(form.errors)

                return redirect('results')
                
    else:
        form_ca1 = CA1Form()
        form_ca2 = CA2Form()
        form_mid_semester = MidSemesterForm()
        form_end_semester = EndSemesterForm()

    return render(request, 'results.html', {
        'form_ca1': form_ca1 if 'form_ca1' in locals() else None,
        'form_ca2': form_ca2 if 'form_ca2' in locals() else None,
        'form_mid_semester': form_mid_semester if 'form_mid_semester' in locals() else None,
        'form_end_semester': form_end_semester if 'form_end_semester' in locals() else None
    })

from .forms import CP_CA1Form,CP_CA2Form,CP_MidSemesterForm,CP_EndSemesterForm
from .models import CP_CA1,CP_CA2,CP_MidSemester,CP_EndSemester


def cp_results(request):
    if request.method == 'POST':
        form_name = request.POST.get('cp')
        
        if form_name == 'ca1':
            form = CP_CA1Form(request.POST)
            if form.is_valid():
                prn_ca1 = form.cleaned_data['prn_ca1']
                marks_ca1 = form.cleaned_data['marks_ca1']
                out_of_ca1 = form.cleaned_data['out_of_ca1']
                
                ca1_instance = CP_CA1(prn_ca1=prn_ca1, marks_ca1=marks_ca1, out_of_ca1=out_of_ca1)
                ca1_instance.save()
                
                return redirect('cp_results')
                
        elif form_name == 'ca2':
            form = CP_CA2Form(request.POST)
            if form.is_valid():
                prn_ca2 = form.cleaned_data['prn_ca2']
                marks_ca2 = form.cleaned_data['marks_ca2']
                out_of_ca2 = form.cleaned_data['out_of_ca2']
                
                ca2_instance = CP_CA2(prn_ca2=prn_ca2, marks_ca2=marks_ca2, out_of_ca2=out_of_ca2)
                ca2_instance.save()
                
                return redirect('cp_results')
                
        elif form_name == 'mid_semester':
            form = CP_MidSemesterForm(request.POST)
            if form.is_valid():
                prn_midsem = form.cleaned_data['prn_midsem']
                marks_midsem = form.cleaned_data['marks_midsem']
                out_of_midsem = form.cleaned_data['out_of_midsem']
                
                midsem_instance = CP_MidSemester(prn_midsem=prn_midsem, marks_midsem=marks_midsem, out_of_midsem=out_of_midsem)
                midsem_instance.save()
                
                return redirect('cp_results')
                
        elif form_name == 'end_semester':
            form = CP_EndSemesterForm(request.POST)
            if form.is_valid():
                prn_endsem = form.cleaned_data['prn_endsem']
                marks_endsem = form.cleaned_data['marks_endsem']
                out_of_endsem = form.cleaned_data['out_of_endsem']
                
                endsem_instance = CP_EndSemester(prn_endsem=prn_endsem, marks_endsem=marks_endsem, out_of_endsem=out_of_endsem)
                endsem_instance.save()
                print(form.errors)

                return redirect('cp_results')
                
    else:
        form_ca1 = CP_CA1Form()
        form_ca2 = CP_CA2Form()
        form_mid_semester = CP_MidSemesterForm()
        form_end_semester = CP_EndSemesterForm()

    return render(request, 'cp_results.html', {
        'form_ca1': form_ca1 if 'form_ca1' in locals() else None,
        'form_ca2': form_ca2 if 'form_ca2' in locals() else None,
        'form_mid_semester': form_mid_semester if 'form_mid_semester' in locals() else None,
        'form_end_semester': form_end_semester if 'form_end_semester' in locals() else None
    })


from .forms import MECH_CA1Form,MECH_CA2Form,MECH_MidSemesterForm,MECH_EndSemesterForm
from .models import MECH_CA1,MECH_CA2,MECH_MidSemester,MECH_EndSemester

def mech_results(request):
    if request.method == 'POST':
        form_name = request.POST.get('mech')
        
        if form_name == 'ca1':
            form = MECH_CA1Form(request.POST)
            if form.is_valid():
                prn_ca1 = form.cleaned_data['prn_ca1']
                marks_ca1 = form.cleaned_data['marks_ca1']
                out_of_ca1 = form.cleaned_data['out_of_ca1']
                
                ca1_instance = MECH_CA1(prn_ca1=prn_ca1, marks_ca1=marks_ca1, out_of_ca1=out_of_ca1)
                ca1_instance.save()
                
                return redirect('mech_results')
                
        elif form_name == 'ca2':
            form = MECH_CA2Form(request.POST)
            if form.is_valid():
                prn_ca2 = form.cleaned_data['prn_ca2']
                marks_ca2 = form.cleaned_data['marks_ca2']
                out_of_ca2 = form.cleaned_data['out_of_ca2']
                
                ca2_instance = MECH_CA2(prn_ca2=prn_ca2, marks_ca2=marks_ca2, out_of_ca2=out_of_ca2)
                ca2_instance.save()
                
                return redirect('mech_results')
                
        elif form_name == 'mid_semester':
            form = MECH_MidSemesterForm(request.POST)
            if form.is_valid():
                prn_midsem = form.cleaned_data['prn_midsem']
                marks_midsem = form.cleaned_data['marks_midsem']
                out_of_midsem = form.cleaned_data['out_of_midsem']
                
                midsem_instance = MECH_MidSemester(prn_midsem=prn_midsem, marks_midsem=marks_midsem, out_of_midsem=out_of_midsem)
                midsem_instance.save()
                
                return redirect('mech_results')
                
        elif form_name == 'end_semester':
            form = MECH_EndSemesterForm(request.POST)
            if form.is_valid():
                prn_endsem = form.cleaned_data['prn_endsem']
                marks_endsem = form.cleaned_data['marks_endsem']
                out_of_endsem = form.cleaned_data['out_of_endsem']
                
                endsem_instance = MECH_EndSemester(prn_endsem=prn_endsem, marks_endsem=marks_endsem, out_of_endsem=out_of_endsem)
                endsem_instance.save()
                print(form.errors)

                return redirect('mech_results')
                
    else:
        form_ca1 = MECH_CA1Form()
        form_ca2 = MECH_CA2Form()
        form_mid_semester = MECH_MidSemesterForm()
        form_end_semester = MECH_EndSemesterForm()

    return render(request, 'mech_results.html', {
        'form_ca1': form_ca1 if 'form_ca1' in locals() else None,
        'form_ca2': form_ca2 if 'form_ca2' in locals() else None,
        'form_mid_semester': form_mid_semester if 'form_mid_semester' in locals() else None,
        'form_end_semester': form_end_semester if 'form_end_semester' in locals() else None
    })

# DIP

from .forms import DIP_CA1Form,DIP_CA2Form,DIP_MidSemesterForm,DIP_EndSemesterForm
from .models import DIP_CA1,DIP_CA2,DIP_MidSemester,DIP_EndSemester

def dip_results(request):
    if request.method == 'POST':
        form_name = request.POST.get('dip')
    
        if form_name == 'ca1':
            form = DIP_CA1Form(request.POST)
            if form.is_valid():
                prn_ca1 = form.cleaned_data['prn_ca1']
                marks_ca1 = form.cleaned_data['marks_ca1']
                out_of_ca1 = form.cleaned_data['out_of_ca1']
                
                ca1_instance = DIP_CA1(prn_ca1=prn_ca1, marks_ca1=marks_ca1, out_of_ca1=out_of_ca1)
                ca1_instance.save()
                
                return redirect('dip_results')
                
        elif form_name == 'ca2':
            form = DIP_CA2Form(request.POST)
            if form.is_valid():
                prn_ca2 = form.cleaned_data['prn_ca2']
                marks_ca2 = form.cleaned_data['marks_ca2']
                out_of_ca2 = form.cleaned_data['out_of_ca2']
                
                ca2_instance = DIP_CA2(prn_ca2=prn_ca2, marks_ca2=marks_ca2, out_of_ca2=out_of_ca2)
                ca2_instance.save()
                
                return redirect('dip_results')
                
        elif form_name == 'mid_semester':
            form = DIP_MidSemesterForm(request.POST)
            if form.is_valid():
                prn_midsem = form.cleaned_data['prn_midsem']
                marks_midsem = form.cleaned_data['marks_midsem']
                out_of_midsem = form.cleaned_data['out_of_midsem']
                
                midsem_instance = DIP_MidSemester(prn_midsem=prn_midsem, marks_midsem=marks_midsem, out_of_midsem=out_of_midsem)
                midsem_instance.save()
                
                return redirect('dip_results')
                
        elif form_name == 'end_semester':
            form = DIP_EndSemesterForm(request.POST)
            if form.is_valid():
                prn_endsem = form.cleaned_data['prn_endsem']
                marks_endsem = form.cleaned_data['marks_endsem']
                out_of_endsem = form.cleaned_data['out_of_endsem']
                
                endsem_instance = DIP_EndSemester(prn_endsem=prn_endsem, marks_endsem=marks_endsem, out_of_endsem=out_of_endsem)
                endsem_instance.save()
                print(form.errors)

                return redirect('dip_results')
                
    else:
        form_ca1 = DIP_CA1Form()
        form_ca2 = DIP_CA2Form()
        form_mid_semester = DIP_MidSemesterForm()
        form_end_semester = DIP_EndSemesterForm()

    return render(request, 'dip_results.html', {
        'form_ca1': form_ca1 if 'form_ca1' in locals() else None,
        'form_ca2': form_ca2 if 'form_ca2' in locals() else None,
        'form_mid_semester': form_mid_semester if 'form_mid_semester' in locals() else None,
        'form_end_semester': form_end_semester if 'form_end_semester' in locals() else None
    })

# be

from .forms import BE_CA1Form,BE_CA2Form,BE_MidSemesterForm,BE_EndSemesterForm
from .models import BE_CA1,BE_CA2,BE_MidSemester,BE_EndSemester

def be_results(request):
    if request.method == 'POST':
        form_name = request.POST.get('be')
    
        if form_name == 'ca1':
            form = BE_CA1Form(request.POST)
            if form.is_valid():
                prn_ca1 = form.cleaned_data['prn_ca1']
                marks_ca1 = form.cleaned_data['marks_ca1']
                out_of_ca1 = form.cleaned_data['out_of_ca1']
                
                ca1_instance = BE_CA1(prn_ca1=prn_ca1, marks_ca1=marks_ca1, out_of_ca1=out_of_ca1)
                ca1_instance.save()
                
                return redirect('be_results')
                
        elif form_name == 'ca2':
            form = BE_CA2Form(request.POST)
            if form.is_valid():
                prn_ca2 = form.cleaned_data['prn_ca2']
                marks_ca2 = form.cleaned_data['marks_ca2']
                out_of_ca2 = form.cleaned_data['out_of_ca2']
                
                ca2_instance = BE_CA2(prn_ca2=prn_ca2, marks_ca2=marks_ca2, out_of_ca2=out_of_ca2)
                ca2_instance.save()
                
                return redirect('be_results')
                
        elif form_name == 'mid_semester':
            form = BE_MidSemesterForm(request.POST)
            if form.is_valid():
                prn_midsem = form.cleaned_data['prn_midsem']
                marks_midsem = form.cleaned_data['marks_midsem']
                out_of_midsem = form.cleaned_data['out_of_midsem']
                
                midsem_instance = BE_MidSemester(prn_midsem=prn_midsem, marks_midsem=marks_midsem, out_of_midsem=out_of_midsem)
                midsem_instance.save()
                
                return redirect('be_results')
                
        elif form_name == 'end_semester':
            form = BE_EndSemesterForm(request.POST)
            if form.is_valid():
                prn_endsem = form.cleaned_data['prn_endsem']
                marks_endsem = form.cleaned_data['marks_endsem']
                out_of_endsem = form.cleaned_data['out_of_endsem']
                
                endsem_instance = BE_EndSemester(prn_endsem=prn_endsem, marks_endsem=marks_endsem, out_of_endsem=out_of_endsem)
                endsem_instance.save()
                print(form.errors)

                return redirect('be_results')
                
    else:
        form_ca1 = BE_CA1Form()
        form_ca2 = BE_CA2Form()
        form_mid_semester = BE_MidSemesterForm()
        form_end_semester = BE_EndSemesterForm()

    return render(request, 'be_results.html', {
        'form_ca1': form_ca1 if 'form_ca1' in locals() else None,
        'form_ca2': form_ca2 if 'form_ca2' in locals() else None,
        'form_mid_semester': form_mid_semester if 'form_mid_semester' in locals() else None,
        'form_end_semester': form_end_semester if 'form_end_semester' in locals() else None
    })

# data anlysis
import datetime
from TPAapp.models import Feedback,Mechanics_Table,CP_Table,DIP_Table,BE_Table
def feedback_analysis(request):
    processed_data = {
        'question1': {'poor': 0, 'good': 0, 'very-good': 0, 'excellent': 0},
        'question2': {'poor': 0, 'good': 0, 'very-good': 0, 'excellent': 0},
        'question3': {'poor': 0, 'good': 0, 'very-good': 0, 'excellent': 0},
        'question4': {'poor': 0, 'good': 0, 'very-good': 0, 'excellent': 0},
        'question5': {'poor': 0, 'good': 0, 'very-good': 0, 'excellent': 0},
        'question6': {'poor': 0, 'good': 0, 'very-good': 0, 'excellent': 0},
    }

    feedbacks = Feedback.objects.filter(date__gte=datetime.date.today() - datetime.timedelta(days=6))

    for feedback in feedbacks:
        processed_data['question1'][feedback.question1] += 1
        processed_data['question2'][feedback.question2] += 1
        processed_data['question3'][feedback.question3] += 1
        processed_data['question4'][feedback.question4] += 1
        processed_data['question5'][feedback.question5] += 1
        processed_data['question6'][feedback.question6] += 1

    return render(request, 'feedback_analysis.html', {'processed_data': processed_data})

def mech_feedback_analysis(request):
    processed_data = {
        'question1': {'poor': 0, 'good': 0, 'very-good': 0, 'excellent': 0},
        'question2': {'poor': 0, 'good': 0, 'very-good': 0, 'excellent': 0},
        'question3': {'poor': 0, 'good': 0, 'very-good': 0, 'excellent': 0},
        'question4': {'poor': 0, 'good': 0, 'very-good': 0, 'excellent': 0},
        'question5': {'poor': 0, 'good': 0, 'very-good': 0, 'excellent': 0},
        'question6': {'poor': 0, 'good': 0, 'very-good': 0, 'excellent': 0},
    }

    feedbacks = Mechanics_Table.objects.filter(date__gte=datetime.date.today() - datetime.timedelta(days=6))

    for mechanics_table in feedbacks:
        processed_data['question1'][mechanics_table.question1] += 1
        processed_data['question2'][mechanics_table.question2] += 1
        processed_data['question3'][mechanics_table.question3] += 1
        processed_data['question4'][mechanics_table.question4] += 1
        processed_data['question5'][mechanics_table.question5] += 1
        processed_data['question6'][mechanics_table.question6] += 1

    return render(request, 'mech_feedback_analysis.html', {'processed_data': processed_data})


def dip_feedback_analysis(request):
    processed_data = {
        'question1': {'poor': 0, 'good': 0, 'very-good': 0, 'excellent': 0},
        'question2': {'poor': 0, 'good': 0, 'very-good': 0, 'excellent': 0},
        'question3': {'poor': 0, 'good': 0, 'very-good': 0, 'excellent': 0},
        'question4': {'poor': 0, 'good': 0, 'very-good': 0, 'excellent': 0},
        'question5': {'poor': 0, 'good': 0, 'very-good': 0, 'excellent': 0},
        'question6': {'poor': 0, 'good': 0, 'very-good': 0, 'excellent': 0},
    }

    feedbacks = DIP_Table.objects.filter(date__gte=datetime.date.today() - datetime.timedelta(days=6))

    for dip_table in feedbacks:
        processed_data['question1'][dip_table.question1] += 1
        processed_data['question2'][dip_table.question2] += 1
        processed_data['question3'][dip_table.question3] += 1
        processed_data['question4'][dip_table.question4] += 1
        processed_data['question5'][dip_table.question5] += 1
        processed_data['question6'][dip_table.question6] += 1

    return render(request, 'dip_feedback_analysis.html', {'processed_data': processed_data})



def cp_feedback_analysis(request):
    processed_data = {
        'question1': {'poor': 0, 'good': 0, 'very-good': 0, 'excellent': 0},
        'question2': {'poor': 0, 'good': 0, 'very-good': 0, 'excellent': 0},
        'question3': {'poor': 0, 'good': 0, 'very-good': 0, 'excellent': 0},
        'question4': {'poor': 0, 'good': 0, 'very-good': 0, 'excellent': 0},
        'question5': {'poor': 0, 'good': 0, 'very-good': 0, 'excellent': 0},
        'question6': {'poor': 0, 'good': 0, 'very-good': 0, 'excellent': 0},
    }

    feedbacks = CP_Table.objects.filter(date__gte=datetime.date.today() - datetime.timedelta(days=6))

    for cp_table in feedbacks:
        processed_data['question1'][cp_table.question1] += 1
        processed_data['question2'][cp_table.question2] += 1
        processed_data['question3'][cp_table.question3] += 1
        processed_data['question4'][cp_table.question4] += 1
        processed_data['question5'][cp_table.question5] += 1
        processed_data['question6'][cp_table.question6] += 1

    return render(request, 'cp_feedback_analysis.html', {'processed_data': processed_data})


def be_feedback_analysis(request):
    processed_data = {
        'question1': {'poor': 0, 'good': 0, 'very-good': 0, 'excellent': 0},
        'question2': {'poor': 0, 'good': 0, 'very-good': 0, 'excellent': 0},
        'question3': {'poor': 0, 'good': 0, 'very-good': 0, 'excellent': 0},
        'question4': {'poor': 0, 'good': 0, 'very-good': 0, 'excellent': 0},
        'question5': {'poor': 0, 'good': 0, 'very-good': 0, 'excellent': 0},
        'question6': {'poor': 0, 'good': 0, 'very-good': 0, 'excellent': 0},
    }

    feedbacks = BE_Table.objects.filter(date__gte=datetime.date.today() - datetime.timedelta(days=6))

    for be_table in feedbacks:
        processed_data['question1'][be_table.question1] += 1
        processed_data['question2'][be_table.question2] += 1
        processed_data['question3'][be_table.question3] += 1
        processed_data['question4'][be_table.question4] += 1
        processed_data['question5'][be_table.question5] += 1
        processed_data['question6'][be_table.question6] += 1

    return render(request, 'be_feedback_analysis.html', {'processed_data': processed_data})


# attendance analysis
import datetime
from django.shortcuts import render
from .models import Attendance

def attendance_analysis(request):
    processed_data = {
        'present_students': [],  # Number of present students for each day (last 7 days)
        'total_students': [],  # Total number of students for each day (last 7 days)
    }

    # Calculate the date range for the last 7 days
    end_date = datetime.date.today()
    start_date = end_date - datetime.timedelta(days=6)

    # Query the attendance data for the last 7 days
    attendance_data = Attendance.objects.filter(date__range=(start_date, end_date))

    # Process the data
    for attendance in attendance_data:
        processed_data['present_students'].append(attendance.present_students)
        processed_data['total_students'].append(attendance.total_students)

    return render(request, 'attendance_analysis.html', {'processed_data': processed_data})


def cp_attendance_analysis(request):
    processed_data = {
        'present_students': [],  # Number of present students for each day (last 7 days)
        'total_students': [],  # Total number of students for each day (last 7 days)
    }

    # Calculate the date range for the last 7 days
    end_date = datetime.date.today()
    start_date = end_date - datetime.timedelta(days=6)

    # Query the attendance data for the last 7 days
    attendance_data = CP_Attendance.objects.filter(date__range=(start_date, end_date))

    # Process the data
    for cp_attendance in attendance_data:
        processed_data['present_students'].append(cp_attendance.present_students)
        processed_data['total_students'].append(cp_attendance.total_students)

    return render(request, 'cp_attendance_analysis.html', {'processed_data': processed_data})



def dip_attendance_analysis(request):
    processed_data = {
        'present_students': [],  # Number of present students for each day (last 7 days)
        'total_students': [],  # Total number of students for each day (last 7 days)
    }

    # Calculate the date range for the last 7 days
    end_date = datetime.date.today()
    start_date = end_date - datetime.timedelta(days=6)

    # Query the attendance data for the last 7 days
    attendance_data = DIP_Attendance.objects.filter(date__range=(start_date, end_date))

    # Process the data
    for dip_attendance in attendance_data:
        processed_data['present_students'].append(dip_attendance.present_students)
        processed_data['total_students'].append(dip_attendance.total_students)

    return render(request, 'dip_attendance_analysis.html', {'processed_data': processed_data})



def mech_attendance_analysis(request):
    processed_data = {
        'present_students': [],  # Number of present students for each day (last 7 days)
        'total_students': [],  # Total number of students for each day (last 7 days)
    }

    # Calculate the date range for the last 7 days
    end_date = datetime.date.today()
    start_date = end_date - datetime.timedelta(days=6)

    # Query the attendance data for the last 7 days
    attendance_data = MECH_Attendance.objects.filter(date__range=(start_date, end_date))

    # Process the data
    for mech_attendance in attendance_data:
        processed_data['present_students'].append(mech_attendance.present_students)
        processed_data['total_students'].append(mech_attendance.total_students)

    return render(request, 'mech_attendance_analysis.html', {'processed_data': processed_data})


def be_attendance_analysis(request):
    processed_data = {
        'present_students': [],  # Number of present students for each day (last 7 days)
        'total_students': [],  # Total number of students for each day (last 7 days)
    }

    # Calculate the date range for the last 7 days
    end_date = datetime.date.today()
    start_date = end_date - datetime.timedelta(days=6)

    # Query the attendance data for the last 7 days
    attendance_data = BE_Attendance.objects.filter(date__range=(start_date, end_date))

    # Process the data
    for be_attendance in attendance_data:
        processed_data['present_students'].append(be_attendance.present_students)
        processed_data['total_students'].append(be_attendance.total_students)

    return render(request, 'be_attendance_analysis.html', {'processed_data': processed_data})




# result analysis
import datetime
from django.shortcuts import render
from .models import CA1, CA2, MidSemester, EndSemester

def result_analysis(request):
    processed_data = {
        'prn': [],  # PRN (unique identifier)
        'ca1_marks': [],  # CA1 marks
        'ca1_out_of': [],  # CA1 total marks
        'ca2_marks': [],  # CA2 marks
        'ca2_out_of': [],  # CA2 total marks
        'midsem_marks': [],  # MidSemester marks
        'midsem_out_of': [],  # MidSemester total marks
        'endsem_marks': [],  # EndSemester marks
        'endsem_out_of': [],  # EndSemester total marks
    }

    # Query the data from the tables
    ca1_data = CA1.objects.all()
    ca2_data = CA2.objects.all()
    midsem_data = MidSemester.objects.all()
    endsem_data = EndSemester.objects.all()

    # Process the data
    for data in zip(ca1_data, ca2_data, midsem_data, endsem_data):
        processed_data['prn'].append(data[0].prn_ca1)
        processed_data['ca1_marks'].append(data[0].marks_ca1)
        processed_data['ca1_out_of'].append(data[0].out_of_ca1)
        processed_data['ca2_marks'].append(data[1].marks_ca2)
        processed_data['ca2_out_of'].append(data[1].out_of_ca2)
        processed_data['midsem_marks'].append(data[2].marks_midsem)
        processed_data['midsem_out_of'].append(data[2].out_of_midsem)
        processed_data['endsem_marks'].append(data[3].marks_endsem)
        processed_data['endsem_out_of'].append(data[3].out_of_endsem)

    return render(request, 'result_analysis.html', {'processed_data': processed_data})



def cp_result_analysis(request):
    processed_data = {
        'prn': [],  # PRN (unique identifier)
        'ca1_marks': [],  # CA1 marks
        'ca1_out_of': [],  # CA1 total marks
        'ca2_marks': [],  # CA2 marks
        'ca2_out_of': [],  # CA2 total marks
        'midsem_marks': [],  # MidSemester marks
        'midsem_out_of': [],  # MidSemester total marks
        'endsem_marks': [],  # EndSemester marks
        'endsem_out_of': [],  # EndSemester total marks
    }

    # Query the data from the tables
    ca1_data = CP_CA1.objects.all()
    ca2_data = CP_CA2.objects.all()
    midsem_data = CP_MidSemester.objects.all()
    endsem_data = CP_EndSemester.objects.all()

    # Process the data
    for data in zip(ca1_data, ca2_data, midsem_data, endsem_data):
        processed_data['prn'].append(data[0].prn_ca1)
        processed_data['ca1_marks'].append(data[0].marks_ca1)
        processed_data['ca1_out_of'].append(data[0].out_of_ca1)
        processed_data['ca2_marks'].append(data[1].marks_ca2)
        processed_data['ca2_out_of'].append(data[1].out_of_ca2)
        processed_data['midsem_marks'].append(data[2].marks_midsem)
        processed_data['midsem_out_of'].append(data[2].out_of_midsem)
        processed_data['endsem_marks'].append(data[3].marks_endsem)
        processed_data['endsem_out_of'].append(data[3].out_of_endsem)

    return render(request, 'result_analysis.html', {'processed_data': processed_data})


def dip_result_analysis(request):
    processed_data = {
        'prn': [],  # PRN (unique identifier)
        'ca1_marks': [],  # CA1 marks
        'ca1_out_of': [],  # CA1 total marks
        'ca2_marks': [],  # CA2 marks
        'ca2_out_of': [],  # CA2 total marks
        'midsem_marks': [],  # MidSemester marks
        'midsem_out_of': [],  # MidSemester total marks
        'endsem_marks': [],  # EndSemester marks
        'endsem_out_of': [],  # EndSemester total marks
    }

    # Query the data from the tables
    ca1_data = DIP_CA1.objects.all()
    ca2_data = DIP_CA2.objects.all()
    midsem_data = DIP_MidSemester.objects.all()
    endsem_data = DIP_EndSemester.objects.all()

    # Process the data
    for data in zip(ca1_data, ca2_data, midsem_data, endsem_data):
        processed_data['prn'].append(data[0].prn_ca1)
        processed_data['ca1_marks'].append(data[0].marks_ca1)
        processed_data['ca1_out_of'].append(data[0].out_of_ca1)
        processed_data['ca2_marks'].append(data[1].marks_ca2)
        processed_data['ca2_out_of'].append(data[1].out_of_ca2)
        processed_data['midsem_marks'].append(data[2].marks_midsem)
        processed_data['midsem_out_of'].append(data[2].out_of_midsem)
        processed_data['endsem_marks'].append(data[3].marks_endsem)
        processed_data['endsem_out_of'].append(data[3].out_of_endsem)

    return render(request, 'dip_result_analysis.html', {'processed_data': processed_data})


def be_result_analysis(request):
    processed_data = {
        'prn': [],  # PRN (unique identifier)
        'ca1_marks': [],  # CA1 marks
        'ca1_out_of': [],  # CA1 total marks
        'ca2_marks': [],  # CA2 marks
        'ca2_out_of': [],  # CA2 total marks
        'midsem_marks': [],  # MidSemester marks
        'midsem_out_of': [],  # MidSemester total marks
        'endsem_marks': [],  # EndSemester marks
        'endsem_out_of': [],  # EndSemester total marks
    }

    # Query the data from the tables
    ca1_data = BE_CA1.objects.all()
    ca2_data = BE_CA2.objects.all()
    midsem_data = BE_MidSemester.objects.all()
    endsem_data = BE_EndSemester.objects.all()

    # Process the data
    for data in zip(ca1_data, ca2_data, midsem_data, endsem_data):
        processed_data['prn'].append(data[0].prn_ca1)
        processed_data['ca1_marks'].append(data[0].marks_ca1)
        processed_data['ca1_out_of'].append(data[0].out_of_ca1)
        processed_data['ca2_marks'].append(data[1].marks_ca2)
        processed_data['ca2_out_of'].append(data[1].out_of_ca2)
        processed_data['midsem_marks'].append(data[2].marks_midsem)
        processed_data['midsem_out_of'].append(data[2].out_of_midsem)
        processed_data['endsem_marks'].append(data[3].marks_endsem)
        processed_data['endsem_out_of'].append(data[3].out_of_endsem)

    return render(request, 'be_result_analysis.html', {'processed_data': processed_data})

def mech_result_analysis(request):
    processed_data = {
        'prn': [],  # PRN (unique identifier)
        'ca1_marks': [],  # CA1 marks
        'ca1_out_of': [],  # CA1 total marks
        'ca2_marks': [],  # CA2 marks
        'ca2_out_of': [],  # CA2 total marks
        'midsem_marks': [],  # MidSemester marks
        'midsem_out_of': [],  # MidSemester total marks
        'endsem_marks': [],  # EndSemester marks
        'endsem_out_of': [],  # EndSemester total marks
    }

    # Query the data from the tables
    ca1_data = MECH_CA1.objects.all()
    ca2_data = MECH_CA2.objects.all()
    midsem_data = MECH_MidSemester.objects.all()
    endsem_data = MECH_EndSemester.objects.all()

    # Process the data
    for data in zip(ca1_data, ca2_data, midsem_data, endsem_data):
        processed_data['prn'].append(data[0].prn_ca1)
        processed_data['ca1_marks'].append(data[0].marks_ca1)
        processed_data['ca1_out_of'].append(data[0].out_of_ca1)
        processed_data['ca2_marks'].append(data[1].marks_ca2)
        processed_data['ca2_out_of'].append(data[1].out_of_ca2)
        processed_data['midsem_marks'].append(data[2].marks_midsem)
        processed_data['midsem_out_of'].append(data[2].out_of_midsem)
        processed_data['endsem_marks'].append(data[3].marks_endsem)
        processed_data['endsem_out_of'].append(data[3].out_of_endsem)

    return render(request, 'mech_result_analysis.html', {'processed_data': processed_data})



from django.db import connection
def admin_login(request):
    if request.method == 'POST':
        dept_code = int(request.POST['dept_code'])
        password = request.POST['password']
        
        # Query the database to check if the provided dept_code and password match
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, name FROM Admin WHERE dept_code=%s AND password=%s", [dept_code, password])
            result = cursor.fetchone()
        
        if result is None:
            return render(request, 'admin_login.html', {'error': 'Invalid department code or password.'})
        
        admin_id = result[0]
        admin_name = result[1]
        
        # Store the admin's ID in the session for authentication
        request.session['admin_id'] = admin_id
          
        # Redirect to a different view or page
        return redirect('admin_home')

    return render(request, 'admin_login.html')

# admin home
def admin_home(request):
    return render(request, 'admin_home.html')

from django.shortcuts import render, redirect
from .models import Student

def student_list(request):
    search_prn = request.GET.get('search_prn')
    if search_prn:
        students = Student.objects.filter(prn__icontains=search_prn).order_by('prn')
    else:
        students = Student.objects.all().order_by('prn')
    
    return render(request, 'student_list.html', {'students': enumerate(students, start=1)})

def delete_student(request, student_id):
    if request.method == 'POST':
        student = Student.objects.get(id=student_id)
        student.delete()
    return redirect('student_list')


# admin teacher
from django.shortcuts import render
from django.db import connection

def teacher_list(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT name, subject_code FROM teachers")
        teachers = cursor.fetchall()

    context = {'teachers': teachers}
    return render(request, 'teacher_list.html', context)
