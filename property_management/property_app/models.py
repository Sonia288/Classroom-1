from django.db import models
import uuid
# Create your models here.

# propert model

class Property(models.Model):
    Property_types =[
      ('appartment','Appartment'),
      ('house','House'),
      ('commercial','Commercial')
    ]
    uu_id = models.UUIDField(default=uuid.uuid4)
    name = models.CharField(max_length=255)
    address = models.TextField()
    property_type= models.CharField(max_length=20,choices=Property_types)
    description = models.TextField(null=True,blank=True)
    number_of_unit = models.PositiveIntegerField()
    def __str__(self):
        return self.name
    
    #unit model 

class Unit(models.Model):
    property = models.ForeignKey(Property,related_name='units',on_delete = models.CASCADE)
    unit_number = models.PositiveIntegerField()
    bedroom = models.PositiveIntegerField()
    bathromm = models.PositiveIntegerField()
    rent = models.DecimalField(max_digits=8,decimal_places=2)
    is_Available = models.BooleanField(default=True)

    def __str__(self):
         return f'{self.property.name} - Unit {self.unit_number}'

