
from django.shortcuts import render, redirect
from django.views import View
from . models import Product, Customer, Cart, Wishlist, Comment
from django.db.models import Count
from . forms import CustomerRegistrationForm, CustomerProfileForm, CommentForm
from django.contrib import messages
from django.contrib.auth import aauthenticate, logout
from django.http import JsonResponse
from django.db.models import Q

# Create your views here.
def get_total_cart_items(request):
    totalitem = 0 
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user = request.user))
      
    return totalitem

def get_total_wish_items(request):
    wishtotalitem = 0 
    if request.user.is_authenticated:
        wishtotalitem = len(Wishlist.objects.filter(user = request.user))
      
    return wishtotalitem


def home(request):
    totalitem = get_total_cart_items(request)
    wishtotalitem = get_total_wish_items(request)
    return render(request, "app/index.html", locals())

def about(request):
    totalitem = get_total_cart_items(request)
    return render(request, "app/about.html", locals())

def contact(request):
    totalitem = get_total_cart_items(request)
    return render(request, "app/contact.html", locals())


class CategoryView(View):
    def get(self, request, val):
        totalitem = get_total_cart_items(request)
        wishtotalitem = get_total_wish_items(request)
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category = val).values('title')#to display the title of the category, use .annotate(total=Count('title')) to count the number of titles
        return render(request, "app/category.html", locals())

class CategoryTitle(View):
    def get(self, request, val):
        totalitem = get_total_cart_items(request)
        wishtotalitem = get_total_wish_items(request)
        product = Product.objects.filter(title=val)# to retrieve multiple products
        title = Product.objects.filter(category = product[0].category).values('title')
        print('title list',title)
        return render(request, "app/category.html", locals())
    
class ProductDetail(View):
    def get(self, request, pk):
        totalitem = get_total_cart_items(request)
        wishtotalitem = get_total_wish_items(request)
        product = Product.objects.get(id=pk)# get was used bcos only one product details is required at a time 
        wishlist = Wishlist.objects.filter(Q(product = product ) & Q(user = request.user))
        return render(request, "app/productdetail.html", locals())
    
class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        totalitem = get_total_cart_items(request)
        wishtotalitem = get_total_wish_items(request)
        return render(request, 'app/customerregistration.html', locals())
    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Congratulations! User Register Successfully")
        else:
            messages.warning(request, "Invalid Input Data")
        return render(request, 'app/customerregistration.html', locals())
    
class Comment(View):
    def get(self, request):
        form = CommentForm()
        totalitem = get_total_cart_items(request)
        wishtotalitem = get_total_wish_items(request)
        return render(request, 'app/comments.html', locals())
    def post(self, request):
        form = CommentForm(request.POST)
        if form.is_valid():
            user = request.user
            print("user",user)
            print("comment", form)
            comment = form.save(commit=False)
            # Assign the current logged-in user
            comment.user = request.user
            # Save the comment to the database
            comment.save()
            form.save()
         

            messages.success(request, "Comment submitted successfully!")
        else:
            messages.warning(request, "Invalid Input Data")
        return render(request, 'app/comments.html', locals())
    
class ProfileView(View):
    def get(self, request):
        totalitem = get_total_cart_items(request)
        wishtotalitem = get_total_wish_items(request)

        form = CustomerProfileForm()
        return render(request, 'app/profile.html', locals())
    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            firstname = form.cleaned_data['firstname'] 
            lastname = form.cleaned_data['lastname']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg = Customer(user=user, firstname=firstname, lastname = lastname, city =city, mobile = mobile, state = state,
                           zipcode = zipcode)
            reg.save()          
            
            
            messages.success(request, "Congratulations! Profile Save Successfully")
        else:
            messages.warning(request, "invalid Input Data")
        return render(request, 'app/profile.html', locals())

#use def function when u just want to fetch records from the db
#use class when u want to display an index page and post with it 
def address(request):
    totalitem = get_total_cart_items(request)
    wishtotalitem = get_total_wish_items(request)
    add = Customer.objects.filter(user=request.user)
    return render(request, 'app/address.html', locals())

class updateAddress(View):
    def get(self, request, pk):
        totalitem = get_total_cart_items(request)
        wishtotalitem = get_total_wish_items(request)
        add = Customer.objects.get(pk=pk) # to retrieve only one address
        form = CustomerProfileForm(instance = add)# this helps to display the information in a form
        return render(request, 'app/updateAddress.html', locals())
    def post(self, request, pk):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            add = Customer.objects.get(pk=pk)
            add.firstname = form.cleaned_data['firstname'] 
            add.lastname = form.cleaned_data['lastname']
            add.city = form.cleaned_data['city']
            add.mobile = form.cleaned_data['mobile']
            add.state = form.cleaned_data['state']
            add.zipcode = form.cleaned_data['zipcode']
            add.save()
        else:
            messages.warning(request,"Invalid Input Data")
        return redirect("address") #to show the address page

def logout_user(request):
    logout(request)
    messages.success(request, ("You  logged out"))
    return redirect('/accounts/login/')

def add_to_cart(request):
    totalitem = get_total_cart_items(request)
    wishtotalitem = get_total_wish_items(request)
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user,products=product).save()
    #return render(request, 'app/addtocart.html', locals())
    return redirect("/cart")

def show_cart(request):
    totalitem = get_total_cart_items(request)
    wishtotalitem = get_total_wish_items(request)
    user = request.user
    cart = Cart.objects.filter(user = user)
    amount = 0
    for p in cart:
        value = p.quantity * p.products.discounted_price
        amount = amount + value
    totalamount = amount + 40
    return render(request, 'app/addtocart.html', locals())

def plus_cart(request):
    if request.method == "GET":
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(products = prod_id) & Q(user = request.user)) #Q is used for multiple request
        c.quantity +=1 #by default one quantity , until u increase it
        c.save() #then save it 
        user = request.user
        cart =  Cart.objects.filter(user = user) # retrive the item after update 
     
        amount = 0 
        for p in cart:
            value = p.quantity * p.products.discounted_price
            amount = amount + value 
        totalamount = amount + 40
        print(prod_id)
        print(p.products.discounted_price)
        print(p.products)
        data = {
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount

        }
        return JsonResponse(data)
    
def minus_cart(request):
    if request.method == "GET":
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(products = prod_id) & Q(user = request.user)) #Q is used for multiple request
        c.quantity -=1 #by default one quantity , until u increase it
        c.save() #then save it 
        user = request.user
        cart =  Cart.objects.filter(user = user) # retrive the item after update 
    
 
        amount = 0 
        for p in cart:
            value = p.quantity * p.products.discounted_price
            amount = amount + value 
        totalamount = amount + 40
        print(prod_id)
        print(p.products.discounted_price)
        print(p.products)
        data = {
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount

        }
        return JsonResponse(data)
    
def remove_cart(request):
    if request.method == "GET":
        prod_id = request.GET['prod_id']
        c = Cart.objects.filter(Q(products = prod_id) & Q(user = request.user)) #Q is used for multiple request
      
        c.delete()
       
        user = request.user
        cart =  Cart.objects.filter(user = user) # retrive the item after update 
        c.quantity = len(cart)
        amount = 0 
        for p in cart:
            value = p.quantity * p.products.discounted_price
            amount = amount + value 
        totalamount = amount + 40
      
        data = {
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount

        }
        return JsonResponse(data)


class checkout(View):
    def get(self, request):
        totalitem = get_total_cart_items(request)
        user= request.user
        add = Customer.objects.filter(user = user)
        cart_items = Cart.objects.filter(user = user)
        famount = 0
        for p in cart_items:
            value = p.quantity * p.products.discounted_price
            famount = famount + value
        totalamount = famount + 40
        return render(request, 'app/checkout.html', locals())
def orders(request):
    pass
    #order_placed = OrderPlaced.objects.filter(user = request.user)
    #return render(request, 'app/orders.html', locals())

def plus_wishlist(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        product = Product.objects.get(id = prod_id)
        user = request.user
        Wishlist(user = user, product = product).save()
       
        quantity = len(Wishlist.objects.filter(user = user))
  
        data = {
            'quantity':quantity,
            'message':'Wishlist Added Successfully',

        }
        return JsonResponse(data)
    
def minus_wishlist(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        product = Product.objects.get(id = prod_id)
        user = request.user
        Wishlist.objects.filter(user = user, product = product).delete()
           
        quantity = len(Wishlist.objects.filter(user = user))
  
        data = {
          
            'quantity':quantity,
            'message':'Wishlist removed Successfully',

        }
        return JsonResponse(data)
    

