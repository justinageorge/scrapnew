from django.shortcuts import render,redirect
from django.views.generic import View
from scrapapp.models  import Scraps,Category, ScrapsFeauture,WishList,Order,OrderItem
from scrapapp.forms import  ScrapForm,RegistraionForm,LoginForm,ScrapFeautureForm  ,ReviewForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib .auth import authenticate,login,logout
from django.utils.decorators import method_decorator
from collections import defaultdict





def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            messages.error(request,"invalid session")
            return redirect("signin")
        else:
            return fn(request,*args,**kwargs)
    return wrapper    

#def method_decorator(decorator name,name=none)
@method_decorator(signin_required,name="dispatch")
class ScrapListView(View):
    def get(self,request,*args,**kwargs):
        qs=Scraps.objects.all()

        
       
        if "location"in request.GET:
            location=request.GET.get("location")
            qs=qs.filter(location__iexact=location)
        if "price_gt" in request.GET:
            amount=request.GET.get("price_gt")
            qs=qs.filter(price__gt=amount)
        if "category" in request.GET:
            category=request.GET.get("category")   
            qs=qs.filter(category__iexact=category)
        return render(request,"scrap_list.html",{"data":qs})
        


# localhost:8000/scraps/{id}    
@method_decorator(signin_required,name="dispatch")
class ScrapDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Scraps.objects.get(id=id)
        return render(request,"scrap_detail.html",{"data":qs})    
@method_decorator(signin_required,name="dispatch")  
class ScrapDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk") 
        Scraps.objects.get(id=id).delete() 
        messages.success(request,"deleted successfully")  
        return redirect("scrap-all")
@method_decorator(signin_required,name="dispatch") 
class ScrapCreateView(View):
    def get(self,request,*args,**kwargs):
        form= ScrapForm()  
        return render(request,"scrap_add.html",{"form":form})  
     
    def post(self,request,*args,**kwargs):
        form=ScrapForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.instance.user=request.user
            form.save()
            
            messages.success(request,"successfully created")
            return redirect("scrap-all")
        else:
            messages.error(request,"created successfully")
            return render(request,"scrap_add.html",{"form":form})  
@method_decorator(signin_required,name="dispatch")       
class ScrapUpdateView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")  
        obj=Scraps.objects.get(id=id)
        form=ScrapForm(instance=obj)
        return render(request,"scrap_edit.html",{"form":form})    
  
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Scraps.objects.get(id=id)
        form=ScrapForm(request.POST,instance=obj,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"updated successfully")
            return redirect("scrap-all")
        else:
            return render(request,"scrap_edit.html",{"form":form}) 

class SignUpView(View):
    def get(self,request,*args,**kwargs):
        form=RegistraionForm()
        return render(request,"register.html",{"form":form})   
    def post(self,request,*args,**kwargs):
        form=RegistraionForm(request.POST)
        if form.is_valid():
            #form.save()
            User.objects.create_user(**form.cleaned_data)
            print("success")
            messages.success(request,"account created successfully")
            return redirect("signin")  
        else:
            messages.error(request,"failed to create the account")  
            return render(request,"register.html",{"form":form})    
      
class SignInView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"login.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)#initializing using value in post
        if form.is_valid():
            uname=form.cleaned_data.get("username")#extracting username and password
            pwd=form.cleaned_data.get("password")
            user_object=authenticate(username=uname,password=pwd)#checking whether credentials are correct
            if user_object:#if there is user object
                print("valid credentials")
                login(request,user_object)#start user session if user is valid
                print(request.user)#fetch user details
                print("success")
                return redirect("scrap-all")#redircting to listing page
            else:
                print("invalid credentials")    
            return render(request,"register.html",{"form":form})   
        else:
           
           return render(request,"register.html",{"form":form})   
        
@method_decorator (signin_required,name="dispatch")   
class SignOutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("signin")
    


def category_list_view(request):
    categories=Category.objects.all()
    context={
        "categories":categories
    }
    return render(request,"category_list.html",context)


@method_decorator(signin_required,name="dispatch")   
class filterView(View):
    template_name="category_filter.html"
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        
        cat_object=Category.objects.get(id=id)
        category_items=Scraps.objects.filter(category=cat_object)
        
        
        return render(request,"category_filter.html",{"data1":category_items})  
    
@method_decorator(signin_required,name="dispatch")
class ScrapFeautureView(View):
    def get(self,request,*args,**kwargs):
        form=ScrapFeautureForm()
        return render(request,"feauture.html",{"form":form})    
    
    def post(self,request,*args,**kwargs):
        form=ScrapFeautureForm(request.POST,files=request.FILES)
        
        
        if form.is_valid():
            form.instance.user=request.user
            
            form.save()
            messages.success(request,"successfully created")
            return redirect("scrap-all")
        else:
            messages.error(request,"failed to insert the feauture")
            return render(request,"feauture.html",{"form":form})
@method_decorator(signin_required,name="dispatch")
class ScrapFeautureViews(View):
    def get(self,request,*args,**kwargs):
         id=kwargs.get("pk")
         qs=Scraps.scrap_user.objects.get(id=id)
         print(qs)
         return render(request,"feauture_display.html",{"info":qs})
    
@method_decorator(signin_required,name="dispatch")
class ReviewView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        scrap_object=Scraps.objects.get(id=id)
        form=ReviewForm()
        
        return render(request,"review.html",{"data":scrap_object,"form":form})
    
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        scrap_object=Scraps.objects.get(id=id)
        form=ReviewForm(request.POST)
        if form.is_valid():
            review=form.save(commit=False)#CREATING AN instance of the model but not save it to the database immediately
            print(review)
            review.user=request.user
            review.scrap=scrap_object
           
            review.save()
            
            return redirect("scrap-detail", pk=scrap_object.pk)
        return render(request,"scrap_detail.html",{"data":scrap_object,"form":form})
            

def add_to_wishlist(request,scrap_id):
    scrap_obj=Scraps.objects.get(id=scrap_id)
    wishlist,created=WishList.objects.get_or_create(user=request.user)
    wishlist.scrap.add(scrap_obj)
    return redirect('wishview')

def remove_wishlist(request,scrap_id):
    scrap_obj=Scraps.objects.get(id=scrap_id)
    wishlist,created=WishList.objects.get_or_create(user=request.user)
    wishlist.scrap.remove(scrap_obj)
    return redirect("wishview")

def wishlistView(request):
     wishlist,created=WishList.objects.get_or_create(user=request.user)
     wishlist_items=wishlist.scrap.all()
     count=wishlist_items.count()
     return render(request,"wishlist.html",{"wishlist":wishlist_items,"wishlistcount":count})
def buy_now(request,scrap_id):
    scrap=Scraps.objects.get(pk=scrap_id)
    existing=OrderItem.objects.filter(order__user=request.user,scrap=scrap).first()
    if existing:
        existing.quantity+=1
        existing.save()
    order,created=Order.objects.get_or_create(user=request.user,total_price=0)
    order_item,created=OrderItem.objects.get_or_create(order=order,scrap=scrap,defaults={'price':scrap.price})
    if not created:
        order_item.quantity+=1
        order_item.save()


    order.total_price+=scrap.price
    order.save()
    return redirect('checkout')

def remove_buynow(request, scrap_id):
    scrap_obj=Scraps.objects.get(pk=scrap_id)
    order,created=Order.objects.get_or_create(user=request.user,total_price=0)
    if not created:
        order_item=OrderItem.objects.filter(order=order,scrap=scrap_obj)
        print(order_item)
        if order_item:
            order_item.price=0
            order_item.delete()
            order.save()
        return redirect('checkout')

# def checkout(request):
#     orders = Order.objects.filter(user=request.user, total_price__gt=0)
    
#     for current_order in orders:
#         order_items = OrderItem.objects.filter(order=current_order)
#         existing = {item.scrap.id: item for item in order_items}
        
        
#         for order_item in order_items:
#             if order_item.scrap.id in existing:
#                 existing_item = existing[order_item.scrap.id]
                
#                 existing_item.quantity += 1
#                 order_items.remove(existing_item)
#                 existing_item.save()
#                 print(existing_item)
#             else:
#                 print("nothing")    

#     order_items = OrderItem.objects.filter(order__in=orders.values('id'))
#     return render(request, "checkout.html", {"orders": orders, "order_items": order_items})


def checkout(request):
    orders = Order.objects.filter(user=request.user, total_price__gt=0)

    for current_order in orders:
        order_items = OrderItem.objects.filter(order=current_order)
        existing_items = {}

        for order_item in order_items:
            scrap_id = order_item.scrap.id

            if scrap_id in existing_items:
                existing_items[scrap_id].quantity += 1
                order_item.delete()  # Remove the duplicate item
            else:
                existing_items[scrap_id] = order_item

        # Update the existing items
        for existing_item in existing_items.values():
            existing_item.save()
       
    order_items = OrderItem.objects.filter(order__in=orders.values('id'))
    
    total_price = 0

    for item in order_items:
        total_price += item.scrap.price * item.quantity

    return render(request, "checkout.html", {"orders": orders, "order_items": order_items, "total_price": total_price})


