from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('', views.index, name="index"),
 	path('single/<int:pk>', views.single, name="single"),
    path('download/', views.download_file, name="download_file"),
    path('index/', views.index1, name="index1"),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)