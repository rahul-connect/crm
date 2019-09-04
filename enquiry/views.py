from django.shortcuts import render
from .models import Enquiry,Course,Follow_ups,account,Batch
from django.contrib import messages
from django.shortcuts import redirect
from user.models import CustomUser
from datetime import datetime
from django.db.models import Count,Sum
from random import randint
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

# Insert an Enquiry
def enquiry(request):
	if request.method == 'POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		gender = request.POST['gender']
		date_of_birth = request.POST['date_of_birth']
		qualification = request.POST['qualification']
		address = request.POST['address']
		experience = request.POST['work_experience']
		contact = request.POST['contact']
		email = request.POST['email']
		course = request.POST['course']
		course_type = request.POST['course_type']
		expected_date = request.POST['expected_date']
		follow_up = request.POST['follow_up']
		lead_sourse = request.POST['lead_sourse']
		lead_date = request.POST['lead_date']

		counsellor = CustomUser.objects.get(id=request.user.id)

		course_instance = Course.objects.get(id=course)

		insert = Enquiry(first_name=first_name,last_name=last_name,gender=gender,date_of_birth=date_of_birth,qualification=qualification,address=address,experience=experience,contact=contact,email=email,course=course_instance,course_type=course_type,expected_date=expected_date,follow_up=follow_up,lead_sourse=lead_sourse,lead_date=lead_date,counsellor=counsellor)
		insert.save()
		messages.success(request,'Successfully Submitted!!')
		return redirect('enquiry')

	courses = Course.objects.all()
	context = {
	'courses':courses,
	'active_link':'new_enquiry'
	}
	return render(request,'profile/enquiry.html',context)


# View all enquirey 
def all_enquires(request):
	counsellor = CustomUser.objects.get(id=request.user.id)

	all_enquires = Enquiry.objects.filter(counsellor=counsellor,status=0).order_by('-id')
	context = {
		'enquiries':all_enquires,
		'active_link':'all_enquiry'
	}
	return render(request,'profile/all_enquiries.html',context)


def view_enquiry(request,id):
	fetch = Enquiry.objects.get(id=id)
	fetch_followup = Follow_ups.objects.filter(enquiry=id).order_by('date')
	fetch_account = account.objects.filter(enquiry_id=id).order_by('date')
	course_fee=int(fetch.course_fee)
	paid=0
	date=''


	for i in fetch_account:
		paid += int(i.amount)

	balance = course_fee-paid

	batch = Batch.objects.filter(center=request.user.select_center.id,status=0)

	if fetch.batch:
		batch_start = Batch.objects.get(id=fetch.batch.id)
		date = batch_start.start_date
	

	context = {
		'data':fetch,
		'follow_ups':fetch_followup,
		'accounts':fetch_account,
		'balance':balance,
		'course_fee':course_fee,
		'batchs':batch,
		'start_date':date
	}
	return render(request,'profile/view_enquiry.html',context)


def follow_up(request,e_id):
	fetch = Enquiry.objects.get(id=e_id)
	description = request.POST['follow_up']
	date = request.POST['date']
	status = request.POST['status']
	


	course_fee = request.POST['course_fee']
	#if(date==''):
		#date = datetime.now() 

	if status != '0':
		fetch.status = status
		if status == '2':
			batch = request.POST['batch']
			batch_instance = Batch.objects.get(id=batch)
			fetch.course_fee = course_fee
			fetch.batch = batch_instance
		fetch.save()

	
	insert = Follow_ups(enquiry=fetch,description=description,date=date)
	insert.save();
	messages.success(request,'Successfully Submitted!!')

	fetch_followup = Follow_ups.objects.filter(enquiry=e_id).order_by('date')
	fetch_account = account.objects.filter(enquiry_id=e_id).order_by('date')
	course_fee=int(fetch.course_fee)
	paid=0;

	for i in fetch_account:
		paid += int(i.amount)

	balance = course_fee-paid

	batch = Batch.objects.filter(center=request.user.select_center.id,status=0)

	date=''
	if fetch.batch:
		batch_start = Batch.objects.get(id=fetch.batch.id)
		date = batch_start.start_date


	context = {
		'data':fetch,
		'follow_ups':fetch_followup,
		'accounts':fetch_account,
		'balance':balance,
		'course_fee':course_fee,
		'batchs':batch,
		'start_date':date
	}
	return render(request,'profile/view_enquiry.html',context)




def accounts(request,e_id):
	fetch = Enquiry.objects.get(id=e_id)
	details = request.POST['details']
	date = request.POST['date_time']
	amount = request.POST['amount']
	
	insert = account(enquiry_id=fetch,detail=details,date=date,amount=amount)
	insert.save();

	messages.success(request,'Successfully Submitted!!')

	fetch_followup = Follow_ups.objects.filter(enquiry=e_id).order_by('date')
	fetch_account = account.objects.filter(enquiry_id=e_id).order_by('date')
	course_fee=int(fetch.course_fee)
	paid=0;

	for i in fetch_account:
		paid += int(i.amount)

	balance = course_fee-paid

	batch = Batch.objects.filter(center=request.user.select_center.id,status=0)

	date=''
	if fetch.batch:
		batch_start = Batch.objects.get(id=fetch.batch.id)
		date = batch_start.start_date

	context = {
		'data':fetch,
		'follow_ups':fetch_followup,
		'accounts':fetch_account,
		'balance':balance,
		'course_fee':course_fee,
		'batchs':batch,
		'start_date':date
	}
	return render(request,'profile/view_enquiry.html',context)




def status_filter(request,s_id):
	counsellor = CustomUser.objects.get(id=request.user.id)

	fetch_data = Enquiry.objects.filter(counsellor=counsellor,status=s_id).order_by('-id')

	context = {
		'enquiries':fetch_data,
		'status':s_id,
		
	}
	return render(request,'profile/status_filter.html',context)


def create_user(request,u_id):
	student = Enquiry.objects.get(id=u_id)
	random_num = str(randint(100000, 999999))
	generate_id = student.first_name.lower() + random_num
	username = generate_id.replace(" ", "")
	password = CustomUser.objects.make_random_password(length=14)

	create_user = CustomUser.objects.create_user(username=username,email=student.email,password=password,role=3,phone=student.contact,first_name=student.first_name,last_name=student.last_name)
	create_user.is_staff = False
	create_user.save

	student.lms_id=1
	student.lms_username=username
	student.save()

	subject = 'Congratulation ! ID has been created for your Course'
	message = 'Your Credentials to login to Golearn \n Username: '+username+'\nPassword: '+password+'\n\n You can Change the password later in the account section after logging in'
	email_from = settings.EMAIL_HOST_USER
	recipient_list = [student.email,]
	send_mail( subject, message, email_from, recipient_list )

	messages.success(request,'LMS ID Successfully Created !!')
	return redirect('dashboard')

	

	