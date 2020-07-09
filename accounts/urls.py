from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.indexView,name="home"),
    path('dashboard/',views.dashboardView,name="dashboard"),
    path('login/',LoginView.as_view(),name="login_url"),
    path('register/',views.registerView,name="register_url"),
    path('logout/',LogoutView.as_view(next_page='home'),name="logout"),
    path('create_class/',views.createClass,name="create_class"),
    path('join_class/',views.joinClass,name="join_class"),
    path('class_page/<str:class_code>/',views.classView,name="class_page"),
    path('upload_notes/<str:class_code>/',views.noteUpload,name="upload_note")
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
