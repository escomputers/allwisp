"""allwisp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path('smartinvoice/', admin.site.urls),
	path('todo/', include('todo.urls', namespace="todo")),
	path('password_reset/',auth_views.PasswordResetView.as_view(), name='admin_password_reset'),
	path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done',),
	path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm',),
	path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete',),
	path('password_change/',auth_views.PasswordChangeView.as_view(),name='password_change',),
	path('password_change/done',auth_views.PasswordChangeDoneView.as_view(),name='password_change_done',),
	#modifica per notekeeper
   	path('appunti/', include('notes.urls')),
	#aggiunta per pagina verifica copertura
	#path('copertura/', TemplateView.as_view(template_name="mappa.html"), name="copertura"),
	#cms urls
	re_path(r'^', include('cms.urls'))
	
	
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""
	path('frontend/index/', TemplateView.as_view(template_name="index.html"), name="index"),
	path('frontend/about/', TemplateView.as_view(template_name="about.html"), name="about"),
	path('frontend/service/', TemplateView.as_view(template_name="service.html"), name="service"),
	path('frontend/portfolio/', TemplateView.as_view(template_name="portfolio.html"), name="portfolio"),
	path('frontend/team/', TemplateView.as_view(template_name="team.html"), name="team"),
	path('frontend/pricing/', TemplateView.as_view(template_name="pricing.html"), name="pricing"),
	path('frontend/contact/', TemplateView.as_view(template_name="contact.html"), name="contact"),
	path('frontend/404/', TemplateView.as_view(template_name="404.html"), name="404"),
	path('frontend/success/', TemplateView.as_view(template_name="success.html"), name="success"),
	path('frontend/blog/', TemplateView.as_view(template_name="blog.html"), name="blog"),
	path('frontend/singlepost/', TemplateView.as_view(template_name="single-post.html"), name="single-post"),
"""
