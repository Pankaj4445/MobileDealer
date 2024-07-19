from django.contrib import admin
from django.urls import include, path
from mobile.views import mobile_list  # Import the view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mobiles/', include('mobile.urls')),
    path('', mobile_list, name='home'),  # Add this line
]
