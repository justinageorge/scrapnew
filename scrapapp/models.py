from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save





class Scraps(models.Model):
    name=models.CharField(max_length=200)
    user= user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="profile",null=True)
    category=models.CharField(max_length=200)
    price=models.PositiveIntegerField()
    location=models.CharField(max_length=200)
    image=models.ImageField(upload_to="images",null=True)
    
    def __str__(self):
       return self.name    
    

class UserProfile(models.Model):  
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="usprofile")  
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    profile_pic=models.ImageField(upload_to="profilepics",null=True,blank=True)
    bio=models.CharField(max_length=200)

class Category(models.Model):
    name=models.CharField(max_length=200)  
   

    def __str__(self):
        return self.name 

class ScrapsFeauture(models.Model):
    name=models.ForeignKey(Scraps,on_delete=models.CASCADE, related_name="user_scraps") 
    condition=models.CharField(max_length=200)   
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="scrap_user")
    price=models.PositiveIntegerField(null=True)
    picture=models.ImageField(upload_to="images",blank=True,null=True)
    place=models.CharField(max_length=200,null=True)
    created_date=models.DateTimeField(auto_now_add=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="category_feauture",null=True)


class WishList(models.Model):
    scrap=models.ManyToManyField(Scraps,related_name="wish")   
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="scrap_wish") 
    created_date=models.DateField()
    

class Bids(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_bids")    
    scrap=models.ForeignKey(Scraps,on_delete=models.CASCADE,related_name="scrap_bid")
    amount=models.PositiveIntegerField()
    status=[
       ('reject','Reject'),
       ('pending','Pending'),
       ('accept','Accept')
    ]
    status=models.CharField(max_length=100,choices=status,default="pending")

class Reviews(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_review") 
    scrap=models.ForeignKey(Scraps,on_delete=models.CASCADE,related_name="scrap_review")  
    comment=models.CharField(max_length=300)
    rating=[(1, '1star'),
            (2,'2 star'),
             (3,'3 star'),
              (4,'4 star'),
               (5,'5 star'),
            

    ]
    rating=models.PositiveIntegerField(choices=rating)

    def create_profile(sender,created,instance,**kwargs) :
        if created:
            UserProfile.objects.create(user=instance)
    post_save.connect(create_profile,sender=User)            

