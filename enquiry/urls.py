from django.urls import path
from . import views

urlpatterns = [
	path('',views.enquiry,name='enquiry'),
	path('all/',views.all_enquires,name='all_enquires'),
	path('view/<int:id>',views.view_enquiry,name='view_enquiry'),
	path('follow_up/<int:e_id>',views.follow_up,name='follow_up'),
	path('status/<int:s_id>',views.status_filter,name='status'),
	path('accounts/<int:e_id>',views.accounts,name='accounts'),
	path('create_user/<int:u_id>',views.create_user,name='create_user')
]