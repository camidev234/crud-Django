from django.urls import path
from . import views as v
urlpatterns = [
    path('', v.indexUser, name='index'),
    path('indexLounge/', v.indexLounge, name='indexLounge'),
    path('authError/', v.login_required_error, name='userAuthError'),
    path('signUpForm/', v.signUpView, name='signUpView'),
    path('loginForm/', v.loginUser, name='loginUser'),
    path('logout/', v.logout_view, name='logout'),
    path('createLoungeForm/', v.createLoungeView, name='createLoungeView'),
    path('saveLounge/', v.createLounge, name='createLounge'),
    path('deleteLounge/<int:id>', v.deleteLounge, name='deleteLounge'),
    path('updateLoungeF/<int:id>', v.updateLoungeView, name='updateLoungeForm'),
    path('updateLounge/<int:id>', v.updateLounge, name='updateLounge'),
    path('viewAllLT/', v.indexLoungesTeachers, name='indexLt'),
    path('assignLt/', v.createLoungeTeacherView, name='assignLt'),
    path('assignLounge/', v.assignLounge, name='saveAssignLt'),
    path('viewTeachersFromLounge/<int:id_lounge>', v.viewTeachersLounges, name='filterTeachers'),
]