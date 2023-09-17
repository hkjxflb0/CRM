from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .models import *
from .forms import OrderForm,CreateUserForm	,CustomerForm
from .filters import OrderFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user,allowed_users,admin_only
from django.contrib.auth.models import Group



@unauthenticated_user
def registration(request):

	form = CreateUserForm()
	if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				user = form.save()
				username = form.cleaned_data.get('username')


				messages.success(request,'Account was created for '+username)
				return redirect('login')
		
	context={'form':form}
	return render(request,'accounts/register.html',context)

		


@unauthenticated_user
def loginpage(request):

	if request.method == 'POST':
		username=request.POST.get('username')
		password=request.POST.get('password')
		user = authenticate(request,username=username,password=password)
		if user is not None:
			login(request,user)
			return redirect('home')
		else:
			messages.info(request,'Username or password is incorrect')
	context = {}
	return render(request,'accounts/login.html',context)

@login_required(login_url='login')
def logoutUser(request):

	logout(request)
	return redirect('login')

@login_required(login_url='login')
def home(request):

	customers = Customer.objects.all()
	orders = Order.objects.all()
	totalorder = orders.count()
	delivered = orders.filter(status="Delivered").count()
	pending = orders.filter(status="Pending").count()
	context = {'customers':customers,'orders':orders,
	    'totalorder':totalorder,'delivered':delivered,'pending':pending}
	return render(request,'accounts/dash.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Customer'])
def userPage(request):

	orders = request.user.customer.order_set.all()
	totalorder = orders.count()
	delivered = orders.filter(status="Delivered").count()
	pending = orders.filter(status="Pending").count()
	context={'orders':orders,'totalorder':totalorder,'delivered':delivered,'pending':pending}
	return render(request,'accounts/user.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Customer'])
def accountSettings(request):

	customer = request.user.customer
	form = CustomerForm(instance=customer)
	if request.method == 'POST':
		form = CustomerForm(request.POST,request.FILES,instance=customer)
		if form.is_valid():
			form.save()

	context={'form':form}
	return render(request,'accounts/account_settings.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def product(request):

	products = Product.objects.all()
	return render(request,'accounts/prod.html',{'products':products})


@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def customer(request,pk_test):

	customer = Customer.objects.get(id = pk_test)
	orders = customer.order_set.all()
	countorder = orders.count()

	myFilter = OrderFilter(request.GET,queryset=orders)
	orders = myFilter.qs
	context = {'customer':customer,'orders':orders,'count':countorder,'myFilter':myFilter}
	return render(request,'accounts/cus.html',context)



@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def orderform(request,pk):

	OrderFormSet = inlineformset_factory(Customer,Order, fields=('product','status',),extra=5)
	customer = Customer.objects.get(id=pk)
	formset = OrderFormSet(queryset=Order.objects.all(),instance=customer)
	if request.method == 'POST':
		formset = OrderFormSet(request.POST,instance=customer)
		if formset.is_valid():
			formset.save()
			return redirect('/')
		# print('Printing post',request.POST)
	context = {'formset':formset}
	return render(request,'accounts/order_form.html',context)



@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def update(request,pk):

	order = Order.objects.get(id=pk)
	formset = OrderForm(instance=order)
	if request.method == 'POST':
		formset = OrderForm(request.POST,instance=order)
		if formset.is_valid():
			formset.save()
			return redirect('/')
			
	context = {'formset':formset}
	return render(request,'accounts/order_form.html',context)



@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def deleteorder(request,pk):

	order = Order.objects.get(id=pk)
	if request.method == 'POST':
		order.delete()
		return redirect('/')
	context = {'item':order}
	return render(request,'accounts/delete.html',context)