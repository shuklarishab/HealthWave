"""MinorProject2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from HealthyWave import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home),
    path('appointment/',views.appointment),
    path('appointmentData/',views.appointmentData),
    path('donate/',views.donate),
    path('donationSubmit/',views.donationSubmit),
    path('login/',views.login),
    path('loginsubmit/',views.loginsubmit),
    path('about/',views.about),
    path('contact/',views.contact),
    path('department/',views.department),
    path('Ophthalmology/',views.ophthalmology),
    path('Orthopedics/',views.orthopedics),
    path('Cardiology/',views.cardiology),
    path('Nephrology/',views.nephrology),
    path('Pathology/',views.pathology),
    path('Neurology/',views.neurology),
    path('Oncology/',views.oncology),
    path('admins/',views.admin),
    path('departmentAdminPage/',views.departmentAdminPage),
    path('showDepartmentInsertPageAdmin/',views.showDepartmentInsertPageAdmin),
    path('insertDepartmentInfo/',views.insertDepartmentInfo),
    path('showDepartmentRecordsInfoPageAdmin/',views.showDepartmentRecordsInfoPageAdmin),
    path('showUpdateDepartmentInfoPage/',views.showUpdateDepartmentInfoPage),
    path('UpdateDepartmentDataAdmin/',views.UpdateDepartmentDataAdmin),
    path('deleteDepartmentData/',views.deleteDepartmentData),
    path('doctorAdminPage/',views.doctorAdminPage),
    path('showDoctorInsertPageAdmin/',views.showDoctorInsertPageAdmin),
    path('insertDoctorInfo/',views.insertDoctorInfo),
    path('showDoctorRecordsInfoPageAdmin',views.showDoctorRecordsInfoPageAdmin),
    path('showUpdateDoctorInfoPage/',views.showUpdateDoctorInfoPage),
    path('UpdateDoctorDataAdmin/',views.UpdateDoctorDataAdmin),
    path('deleteDoctorData/',views.deleteDoctorData),
    path('appointmentAdminPage/',views.appointmentAdminPage),
    path('showAppointmentRecordsInfoPageAdmin/',views.showAppointmentRecordsInfoPageAdmin),
    path('showUpdateAppointmentInfoPage/',views.showUpdateAppointmentInfoPage),
    path('UpdateAppointmentDataAdmin/',views.UpdateAppointmentDataAdmin),
    path('deleteAppointmentData/',views.deleteAppointmentData),
    path('loginAdminPage/',views.loginAdminPage),
    path('showLoginRecordsInfoPageAdmin/',views.showLoginRecordsInfoPageAdmin),
    path('showUpdateLoginInfoPage/',views.showUpdateLoginInfoPage),
    path('UpdateLoginDataAdmin/',views.UpdateLoginDataAdmin),
    path('deleteLoginData/',views.deleteLoginData),
    path('donationAdminPage/',views.donationAdminPage),
    path('showDonationRecordsInfoPageAdmin/',views.showDonationRecordsInfoPageAdmin),
    path('showUpdateDonationInfoPage/',views.showUpdateDonationInfoPage),
    path('UpdateDonationDataAdmin/',views.UpdateDonationDataAdmin),
    path('deleteDonationData/',views.deleteDonationData),
    path('signup/',views.signup),
    path('signupAdmin/',views.signupAdmin),
    # path('showDonationData/',views.showDonationData),
]
