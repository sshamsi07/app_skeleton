from django.db import models


# Create your models here.
class account(models.Model):
    # Given name, Last name,
    # email address
    # username, password
    # account creation date, last login date time
    given_name = models.CharField(max_length=255, help_text='First Name')
    last_name = models.CharField(max_length=255, help_text='Last Name')
    # TODO:username = models.OneToOneField(unique=True, on_delete= True, to= )
    # TODO: password = models.Password(unique=True)
    # TODO: Add creation_date and last login fields
    # TODO: Add account type Tutor/Student
