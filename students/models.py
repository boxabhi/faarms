from django.db import models

GENDER = (('Male' , 'Male') , ('Female' , 'Female'))


import datetime;
ts = datetime.datetime.now().timestamp()

class Students(models.Model):
    
    registration_number = models.CharField(max_length=100 , null=True , blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=8 , choices=GENDER)
    date_of_admission = models.DateField()
    created_at = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now = True)
    
    def __str__(self):
        return self.registration_number
    
    def save(self, *args, **kwargs):
        try:
            current_timestamp =  int(datetime.datetime.now().timestamp())
            self.registration_number = self.first_name[0] + self.last_name[0] + str(current_timestamp)
            super(Students, self).save(*args, **kwargs)
        except Exception as e:
            print(e)