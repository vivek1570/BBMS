from django.db import models

# Create your models here.
# class person(models.Model):
#    p_name=models.CharField(max_length=200)
#    p_phone=models.CharField(max_length=10)
#    p_b_group=models.CharField(max_length=3)
#    p_add=models.CharField(max_length=300)
#    p_gender=models.CharField(max_length=6)
#    p_age=models.PositiveIntegerField()
#    p_loc=models.CharField(max_length=100)
class person(models.Model):
    # Your existing fields
    id=models.IntegerField.primary_key
    p_name = models.CharField(max_length=100)
    p_phone = models.CharField(max_length=15)
    p_b_group = models.CharField(max_length=5)
    p_add = models.TextField()
    p_age = models.IntegerField()
    p_loc = models.CharField(max_length=100)

    # New gender field
    p_gender = models.CharField(max_length=1, choices=[
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ])

    def __str__(self):
        return self.p_name

   
class donor(models.Model):
   p_id = models.ForeignKey(person.id)
   d_name=models.CharField(max_length=200)
   d_phone=models.CharField(max_length=10)
   d_b_group=models.CharField(max_length=3)
   d_quantity=models.PositiveIntegerField()
   d_date=models.DateField()
   d_loc=models.CharField(max_length=100)
   p_id = models.IntegerField().primary_key
   

class stock(models.Model):
   b_group=models.ForeignKey(donor.p_id)
   b_group=models.CharField(max_length=3).primary_key
   b_quantity=models.PositiveIntegerField()
  

class receive(models.Model):
   id=models.ForeignKey(donor.p_id)
   r_name=models.CharField(max_length=200)
   r_phone=models.CharField(max_length=10)
   r_b_group=models.CharField(max_length=3)
   r_quantity=models.PositiveIntegerField()
   r_loc=models.CharField(max_length=100)
   id=models.IntegerField.primary_key
