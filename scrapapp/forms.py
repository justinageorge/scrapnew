from django import forms
from scrapapp.models import Scraps,Category,ScrapsFeauture,Reviews
from django.contrib.auth.models import User


class ScrapForm(forms.ModelForm):
    
    class Meta:
        model=Scraps
        fields="__all__"
        widgets={"name":forms.TextInput(attrs={"class":"form-control"}),
                 "category":forms.TextInput(attrs={"class":"form-control"}),
                 "price":forms.NumberInput(attrs={"class":"form-control"}),
                 "location":forms.TextInput(attrs={"class":"form-control"}),
                  
                 }
        
        def set_user(self, user):
        
            self.instance.user = user
            print(user)
        
class RegistraionForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username",'email',"password"]

class LoginForm(forms.Form):
    username=forms.CharField(widget=(forms.TextInput(attrs={"class":"form-control"})))
    password=forms.CharField(widget=(forms.PasswordInput(attrs={"class":"form-control"})))  


class ScrapFeautureForm(forms.ModelForm):
    
    class Meta:
        model= ScrapsFeauture
        exclude=["user","price","category","picture","place"]


        def set_user(self,user):
            self.instance.user=user



class ReviewForm(forms.ModelForm):
    class Meta:
        model=Reviews
        fields=["comment","rating"]
                

        