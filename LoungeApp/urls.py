from django.urls import path
from . import views as v
urlpatterns = [
    path('', v.indexLounge, name='indexLounge'),
    path('createLoungeForm/', v.createLoungeView, name='createLoungeView'),
    path('saveLounge/', v.createLounge, name='createLounge'),
]