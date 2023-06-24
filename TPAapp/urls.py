from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('home/', views.index,name='home'),
    path('about/', views.about,name='about'),
    path('contact/', views.contact,name='contact'),
    path('student_registration/', views.student_registration, name='student_register'),
    path('student_login/', views.student_login, name='student_login'),
    path('student_home/', views.student_home,name='student_home'),
    path('student_feedback/', views.student_feedback,name='student_feedback'),
    path('mathematics_one/', views.mathematics_one,name='mathematics_one'),
    path('mechanics/', views.mechanics,name='mechanics'),
    path('comp_programming/', views.comp_programming,name='comp_programming'),
    path('basic_electronics/', views.basic_electronics,name='basic_electronics'),
    path('dip/', views.dip,name='dip'),
    
    path('teacher_login/', views.teacher_login,name='teacher_login'),
    path('m1_teacher_home/', views.m1_teacher_home,name='m1_teacher_home'),
    path('cp_teacher_home/', views.cp_teacher_home,name='cp_teacher_home'),
    path('mech_teacher_home/', views.mech_teacher_home,name='mech_teacher_home'),
    path('dip_teacher_home/', views.dip_teacher_home,name='dip_teacher_home'),
    path('be_teacher_home/', views.be_teacher_home,name='be_teacher_home'),
    
    path('attendance/', views.add_attendance,name='attendance'),
    path('cp_attendance/', views.cp_attendance,name='cp_attendance'),
    path('mech_attendance/', views.mech_attendance,name='mech_attendance'),
    path('dip_attendance/', views.dip_attendance,name='dip_attendance'),
    path('be_attendance/', views.be_attendance,name='be_attendance'),

    path('results/', views.add_results,name='results'),
    path('cp_results/', views.cp_results,name='cp_results'),
    path('mech_results/', views.mech_results,name='mech_results'),
    path('dip_results/', views.dip_results,name='dip_results'),
    path('be_results/', views.be_results,name='be_results'),
    
    path('admin_login/', views.admin_login,name='admin_login'),
    path('admin_home/', views.admin_home,name='admin_home'),
    

    #  path('accounts/login/', LoginView.as_view(), name='login'),
    
    path('feedback_analysis/', views.feedback_analysis,name='feedback_analysis'),
    path('mech_feedback_analysis/', views.mech_feedback_analysis,name='mech_feedback_analysis'),
    path('dip_feedback_analysis/', views.dip_feedback_analysis,name='dip_feedback_analysis'),
    path('cp_feedback_analysis/', views.cp_feedback_analysis,name='cp_feedback_analysis'),
    path('be_feedback_analysis/', views.be_feedback_analysis,name='be_feedback_analysis'),
    
    
    # attendance analysis
    path('attendance_analysis/', views.attendance_analysis,name='attendance_analysis'),
    path('cp_attendance_analysis/', views.cp_attendance_analysis,name='cp_attendance_analysis'),
    path('dip_attendance_analysis/', views.dip_attendance_analysis,name='dip_attendance_analysis'),
    path('mech_attendance_analysis/', views.mech_attendance_analysis,name='mech_attendance_analysis'),
    path('be_attendance_analysis/', views.be_attendance_analysis,name='be_attendance_analysis'),
    
    
    # result analysis
    path('result_analysis/', views.result_analysis,name='result_analysis'),
    path('cp_result_analysis/', views.cp_result_analysis,name='cp_result_analysis'),
    path('dip_result_analysis/', views.dip_result_analysis,name='dip_result_analysis'),
    path('be_result_analysis/', views.be_result_analysis,name='be_result_analysis'),
    path('mech_result_analysis/', views.mech_result_analysis,name='mech_result_analysis'),
    
    
    # admin
    path('student_list/', views.student_list,name='student_list'),
    path('students/delete/<int:student_id>/', views.delete_student, name='delete_student'),
    path('teacher_list/', views.teacher_list,name='teacher_list'),
]

