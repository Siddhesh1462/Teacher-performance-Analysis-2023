from django.db import models

# Create your models here.

# contact form
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name


from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        # Specify any dependencies here
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=255, unique=True),
        ),
    ]


# student registration form
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class StudentManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        # Create and save a regular student user
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email, unique=True)
        student = self.model(email=email, **extra_fields)
        student.set_password(password)
        student.save(using=self._db)
        return student

    def create_superuser(self, email, password=None, **extra_fields):
        # Create and save a superuser
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class Student(AbstractBaseUser):
    name = models.CharField(max_length=255)
    prn = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)  # Add unique=True here
    password = models.CharField(max_length=255)
    last_login = models.DateTimeField(auto_now=True)
    # Add other fields as needed
    def __str__(self):
        return self.name
    USERNAME_FIELD = 'email'

    objects = StudentManager()


class Student_User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    prn_no = models.CharField(max_length=20, unique=True)
    
# feedback form

class Feedback(models.Model):
    prn = models.CharField(max_length=20)
    date = models.DateField()
    question1 = models.CharField(max_length=10)
    question2 = models.CharField(max_length=10)
    question3 = models.CharField(max_length=10)
    question4 = models.CharField(max_length=10)
    question5 = models.CharField(max_length=10)
    question6 = models.CharField(max_length=10)


class Mechanics_Table(models.Model):
    prn = models.CharField(max_length=20)
    date = models.DateField()
    question1 = models.CharField(max_length=10)
    question2 = models.CharField(max_length=10)
    question3 = models.CharField(max_length=10)
    question4 = models.CharField(max_length=10)
    question5 = models.CharField(max_length=10)
    question6 = models.CharField(max_length=10)

class CP_Table(models.Model):
    prn = models.CharField(max_length=20)
    date = models.DateField()
    question1 = models.CharField(max_length=10)
    question2 = models.CharField(max_length=10)
    question3 = models.CharField(max_length=10)
    question4 = models.CharField(max_length=10)
    question5 = models.CharField(max_length=10)
    question6 = models.CharField(max_length=10)

class BE_Table(models.Model):
    prn = models.CharField(max_length=20)
    date = models.DateField()
    question1 = models.CharField(max_length=10)
    question2 = models.CharField(max_length=10)
    question3 = models.CharField(max_length=10)
    question4 = models.CharField(max_length=10)
    question5 = models.CharField(max_length=10)
    question6 = models.CharField(max_length=10)
    
class DIP_Table(models.Model):
    prn = models.CharField(max_length=20)
    date = models.DateField()
    question1 = models.CharField(max_length=10)
    question2 = models.CharField(max_length=10)
    question3 = models.CharField(max_length=10)
    question4 = models.CharField(max_length=10)
    question5 = models.CharField(max_length=10)
    question6 = models.CharField(max_length=10)



# Attendance Table

class Attendance(models.Model):
    date = models.DateField()
    present_students = models.IntegerField()
    total_students = models.IntegerField(default=60)

    def __str__(self):
        return str(self.date)
    
class CP_Attendance(models.Model):
    date = models.DateField()
    present_students = models.IntegerField()
    total_students = models.IntegerField(default=60)

    def __str__(self):
        return str(self.date)

class MECH_Attendance(models.Model):
    date = models.DateField()
    present_students = models.IntegerField()
    total_students = models.IntegerField(default=60)

    def __str__(self):
        return str(self.date)

class DIP_Attendance(models.Model):
    date = models.DateField()
    present_students = models.IntegerField()
    total_students = models.IntegerField(default=60)

    def __str__(self):
        return str(self.date)

class BE_Attendance(models.Model):
    date = models.DateField()
    present_students = models.IntegerField()
    total_students = models.IntegerField(default=60)

    def __str__(self):
        return str(self.date)

# results

class CA1(models.Model):
    prn_ca1 = models.CharField(max_length=20)
    marks_ca1 = models.IntegerField()
    out_of_ca1 = models.IntegerField(default=10)

class CA2(models.Model):
    prn_ca2 = models.CharField(max_length=20)
    marks_ca2 = models.IntegerField()
    out_of_ca2 = models.IntegerField(default=10)

class MidSemester(models.Model):
    prn_midsem = models.CharField(max_length=20)
    marks_midsem = models.IntegerField()
    out_of_midsem = models.IntegerField(default=20)

class EndSemester(models.Model):
    prn_endsem = models.CharField(max_length=20)
    marks_endsem = models.IntegerField()
    out_of_endsem = models.IntegerField(default=60)

# CP_RESULTS

class CP_CA1(models.Model):
    prn_ca1 = models.CharField(max_length=20)
    marks_ca1 = models.IntegerField()
    out_of_ca1 = models.IntegerField(default=10)

class CP_CA2(models.Model):
    prn_ca2 = models.CharField(max_length=20)
    marks_ca2 = models.IntegerField()
    out_of_ca2 = models.IntegerField(default=10)

class CP_MidSemester(models.Model):
    prn_midsem = models.CharField(max_length=20)
    marks_midsem = models.IntegerField()
    out_of_midsem = models.IntegerField(default=20)

class CP_EndSemester(models.Model):
    prn_endsem = models.CharField(max_length=20)
    marks_endsem = models.IntegerField()
    out_of_endsem = models.IntegerField(default=60)

# MECH RESULTS

class MECH_CA1(models.Model):
    prn_ca1 = models.CharField(max_length=20)
    marks_ca1 = models.IntegerField()
    out_of_ca1 = models.IntegerField(default=10)

class MECH_CA2(models.Model):
    prn_ca2 = models.CharField(max_length=20)
    marks_ca2 = models.IntegerField()
    out_of_ca2 = models.IntegerField(default=10)

class MECH_MidSemester(models.Model):
    prn_midsem = models.CharField(max_length=20)
    marks_midsem = models.IntegerField()
    out_of_midsem = models.IntegerField(default=20)

class MECH_EndSemester(models.Model):
    prn_endsem = models.CharField(max_length=20)
    marks_endsem = models.IntegerField()
    out_of_endsem = models.IntegerField(default=60)

# DIP

class DIP_CA1(models.Model):
    prn_ca1 = models.CharField(max_length=20)
    marks_ca1 = models.IntegerField()
    out_of_ca1 = models.IntegerField(default=10)

class DIP_CA2(models.Model):
    prn_ca2 = models.CharField(max_length=20)
    marks_ca2 = models.IntegerField()
    out_of_ca2 = models.IntegerField(default=10)

class DIP_MidSemester(models.Model):
    prn_midsem = models.CharField(max_length=20)
    marks_midsem = models.IntegerField()
    out_of_midsem = models.IntegerField(default=20)

class DIP_EndSemester(models.Model):
    prn_endsem = models.CharField(max_length=20)
    marks_endsem = models.IntegerField()
    out_of_endsem = models.IntegerField(default=60)

# BE
class BE_CA1(models.Model):
    prn_ca1 = models.CharField(max_length=20)
    marks_ca1 = models.IntegerField()
    out_of_ca1 = models.IntegerField(default=10)

class BE_CA2(models.Model):
    prn_ca2 = models.CharField(max_length=20)
    marks_ca2 = models.IntegerField()
    out_of_ca2 = models.IntegerField(default=10)

class BE_MidSemester(models.Model):
    prn_midsem = models.CharField(max_length=20)
    marks_midsem = models.IntegerField()
    out_of_midsem = models.IntegerField(default=20)

class BE_EndSemester(models.Model):
    prn_endsem = models.CharField(max_length=20)
    marks_endsem = models.IntegerField()
    out_of_endsem = models.IntegerField(default=60)


