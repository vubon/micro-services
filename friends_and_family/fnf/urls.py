from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^add-family-member/', views.AddFamilyMemberView.as_view()), 
]