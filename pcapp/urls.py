from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    # path('basic/', views.basic, name='index'),

    # student urls
    path('student/', views.student, name='student'),
    path('student/saccount/', views.SaccountSettings, name="saccount"),
    path('company/caccount/', views.CaccountSettings, name="caccount"),
    path('student/student_dashboard/', views.student_dashboard, name='student_dashboard'),
    path('student/student_form/', views.student_form, name='student_form'),
    path('student/update_student_form/<int:book_id>/', views.update_student_form, name='update_student_form'),
    path('student/view_student_form/', views.view_student_form, name='view_student_form'),
    path('student/view_vaccancy/', views.view_vaccancy, name='view_vaccancy'),
    path('student/view_vaccancy_details/<int:myid>/', views.view_vaccancy_details, name='view_vaccancy_details'),
    path('student/selected_student_list/', views.selected_student_list, name='selected_student_list'),
    path('student/applied_job_list/', views.applied_job_list, name='applied_job_list'),
    path('student/student_profile/', views.student_profile, name='student_profile'),
    path('student/successStory/', views.successStory, name='successStory'),
    path('student/view_successStory/', views.view_successStory, name='view_successStory'),

    # company urls
    path('company/', views.company, name='company'),
    path('company/company_dashboard/', views.company_dashboard, name='company_dashboard'),
    path('company/add_vacancy/', views.add_vacancy, name='add_vacancy'),
    path('company/view_company_vacancy/', views.view_company_vacancy, name='view_company_vacancy'),
    path('company/update_vacancy/<int:book_id>/', views.update_vacancy, name='update_vacancy'),
    path('company/view_apply_student_list/', views.view_apply_student_list, name='view_apply_student_list'),
    path('company/add_selected_student/', views.add_selected_student, name='add_selected_student'),
    path('company/selected_student_list/', views.selected_student_list, name='selected_student_list'),
    path('company/view_apply_student_list/', views.view_apply_student_list, name='view_apply_student_list'),

    # admin urls
    path('pcadmin/', views.admin, name='admin'),
    path('pcadmin/admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('pcadmin/manage_tpo_update/', views.manage_tpo_update, name='manage_tpo_update'),
    path('pcadmin/view_tpo_update/', views.view_tpo_update, name='view_tpo_update'),
    path('pcadmin/delete_tpo_update/<int:myid>/', views.delete_tpo_update, name='delete_tpo_update'),
    path('pcadmin/manage_student_update/', views.manage_student_update, name='manage_student_update'),
    path('pcadmin/view_student_update/', views.view_student_update, name='view_student_update'),
    path('pcadmin/delete_student_update/<int:myid>/', views.delete_student_update, name='delete_student_update'),
    path('pcadmin/new_students_register/', views.new_students_register, name='new_students_register'),
    path('pcadmin/new_company_register/', views.new_company_register, name='new_company_register'),
    path('pcadmin/view_list_student_form/', views.view_list_student_form, name='view_list_student_form'),
    path('pcadmin/delete_student_form/<int:book_id>', views.delete_student_form, name='delete_student_form'),
    path('pcadmin/delete_vacancy/<int:book_id>/', views.delete_vacancy, name='delete_vacancy'),
    path('pcadmin/admin_view_vacancy/', views.admin_view_vacancy, name='admin_view_vacancy'),
    path('pcadmin/admin_view_vacancy_details/<int:myid>/', views.admin_view_vacancy_details,
         name='admin_view_vacancy_details'),
    path('pcadmin/view_apply_student_list/', views.view_apply_student_list, name='view_apply_student_list'),
    path('pcadmin/delete_apply_student_list/', views.delete_apply_student_list, name='delete_apply_student_list'),
    path('pcadmin/delete_selected_student/', views.delete_selected_student, name='delete_selected_student'),

    # users testing
    path('register/', views.register, name='register'),
    path('login/', views.loginview, name='login'),
    path('logout/', views.logoutview, name='logout'),

    # Password Reset

    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
         name="reset_password"),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"),
         name="password_reset_confirm"),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="passsword_reset_done.html"),
         name="password_reset_complete"),

    # search function

    path('search/', views.search, name='search'),
    path('contactus/', views.contactus, name='contactus'),
    path('aboutus/', views.aboutus, name='aboutus'),
]
