from django.contrib import admin
from .models import Course,Enquiry,City,Center,Follow_ups,account,Batch
# Register your models here.

	
admin.site.register(Course)
admin.site.register(Enquiry)
admin.site.register(Batch)
admin.site.register(City)
admin.site.register(Center)
admin.site.register(Follow_ups)
admin.site.register(account)
