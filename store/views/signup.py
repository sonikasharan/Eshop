from django.shortcuts import render , redirect
from django.contrib.auth.hashers import make_password 
from store.models.customer import Customer
from django.views import View
class Signup(View):
   def get(self,request):
       return render(request,'signup.html')   
   def post(self , request):
      postData=request.POST
      first_name =postData.get('firstname')
      last_name =postData.get('lastname')
      phone =postData.get('contactnumber')
      email =postData.get('email')
      password =postData.get('password')
      # validation
      value={
         'first_name':first_name,
         'last_name': last_name,
         'phone': phone,
         'email':email
       }
      error_message =None
      customer = Customer(first_name=first_name,
          last_name=last_name,phone=phone,
          email=email,password=password)
      error_message = self.validateCustomer(customer)
     
      #saving
      if not error_message:
          print(first_name,last_name,phone,email,password)
          customer.password= make_password(customer.password)
          customer.register()
          return redirect('homepage')
      else:    
          data={
            'error':error_message,
            'values':value
          }
          return render(request ,'signup.html',data)
   def validateCustomer(self,customer):
      error_message= None
      if(not customer.first_name):
         error_message="First Name Required !!"
      elif len(customer.first_name)< 4:
         error_message ='Firstname must be 4 char long or more'   
      elif not customer.last_name:
         error_message="last Name Required !!"
      elif len(customer.last_name)< 3:
         error_message ='lastname must be 3 char long or more'   
      elif not customer.phone:
         error_message="contact number Required !!"
      elif len(customer.phone)< 10:
         error_message ='contact number must be of 10 digit'  
      elif len(customer.password)< 3:
         error_message ='password too small'  
      elif len(customer.email)< 7:
         error_message ='email should be alteast 7 character '
      elif customer.isExists():
         error_message = 'Email address already exist'   
      return error_message    
