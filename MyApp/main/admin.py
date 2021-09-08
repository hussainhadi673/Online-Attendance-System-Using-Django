from django.contrib import admin
from .models import Employees
from .models import Profile
from .models import Leave_Request

admin.site.register(Employees)
admin.site.register(Profile)
admin.site.register(Leave_Request)


# Register your models here.
