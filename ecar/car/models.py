from django.db import models
from datetime import datetime
from multiselectfield import MultiSelectField
# Create your models here.

class CarType(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table='CarType'

    def __str__(self): 
         return f"{self.name}"
    
class CarVarient(models.Model):
    name = models.CharField(max_length=100)

    class Meta: 
        db_table='CarVarient'

    def __str__(self):
        return self.name
    
class Brand(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='brand/')

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        db_table='Brand'
    
class CarEngineAndTransmission(models.Model):

    Engine_Type = models.CharField(max_length=100)
    Engine_Displacement = models.IntegerField()
    No_Of_Cylinder = models.IntegerField()
    Max_Power = models.CharField()
    Torque = models.CharField()
    Transmission_Type = models.CharField(max_length=100)
    Drive_Type = models.CharField(max_length=100)

    class Meta:
        db_table='CarEngine And Transmission'

    def __str__(self):  
        # return f"EngineType = {self.EngineType}, EngineDisplacement = {self.EngineDisplacement}, NoOfCylinder = {self.NoOfCylinder}, MaxPower = {self.MaxPower}, Torque = {self.Torque}, TransmissionType = {self.TransmissionType}, DriveType = {self.DriveType}, ClutchType = {self.ClutchType}"
         return f"EngineType = {self.Engine_Type}"
        
class Fuel(models.Model): 

    FuelType = models.CharField(max_length=100)
    TankCapacity = models.FloatField()
    TopSpeed = models.IntegerField()
    Mileage = models.FloatField()

    class Meta:
        db_table='Fuel'

    def __str__(self):
        return f"FuelType={self.FuelType},Tank={self.TankCapacity}"

class Exterior (models.Model):

    Rims = models.CharField(max_length=100)
    Color = models.CharField(max_length=100)
    # image = models.ImageField(upload_to='wheel/')

    def __str__(self):
        return f"{self.Rims}"

    class Meta:
        db_table='Exterior'

# class Comfort(models.Model):

#     VanityMirror = models.BooleanField(default=True)
#     Rearseatheadrest = models.BooleanField(default=True)
#     Adjustableheadrest = models.BooleanField(default=True)
#     Rearseatcentrearmrest = models.BooleanField(default=True)
#     Heightadjustablefrontseatbelts = models.BooleanField(default=True)
#     RearACVents = models.BooleanField(default=True)
#     SeatLumberSupport = models.BooleanField(default=True)
#     MultifunctionSteeringWheel = models.BooleanField(default=True)
#     CruiseControl = models.BooleanField(default = True)

#     class Meta:
#         db_table='Comfort'

#     def __str__(self):
#         return f"{self.VanityMirror}"
    
class Car(models.Model):

    comfort_choices  = (
        ('Vanity Mirror', 'Vanity Mirror'),
        ('Fog Lights - Front', 'Fog Lights - Front'),
        ('Adjustable seats', 'Adjustable seats'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Seat Heating', 'Seat Heating'),
        ('Alarm System', 'Alarm System'),
        ('Park Assist', 'Park Assist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Blind Spot Monitor', 'Blind Spot Monitor'),
        ('Bluetooth Handset', 'Bluetooth Handset'),
        )

    seating_capacity = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )

    year_choice = []
    for r in range(2000, (datetime.now().year+4)):
        year_choice.append((r,r))



    name = models.CharField(max_length=50)
    price = models.FloatField()
    cartype = models.ForeignKey(CarType,on_delete=models.CASCADE)
    carvarient = models.ForeignKey(CarVarient,on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    Engine = models.ForeignKey(CarEngineAndTransmission,on_delete=models.CASCADE)
    fuel = models.ForeignKey(Fuel,on_delete=models.CASCADE)
    exterior = models.ForeignKey(Exterior,on_delete=models.CASCADE)

    comfort = MultiSelectField(choices=comfort_choices,max_choices=13,max_length = 2000)
    capacity = models.CharField(choices=seating_capacity,max_length=10)
    year = models.IntegerField(('year'), choices=year_choice)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now)

    # comfort = models.ForeignKey(Comfort,on_delete=models.CASCADE)

    image1 = models.ImageField(upload_to='car/')
    image2 = models.ImageField(upload_to='car/')
    image3 = models.ImageField(upload_to='car/')

    # EngineType = models.CharField(max_length=50,null=True)
    # EngineDisplacement = models.IntegerField(null=True)
    # NoOfCylinder = models.IntegerField(null=True)
    # MaxPower = models.IntegerField(null=True)
    # Torque = models.IntegerField(null=True)
    # TransmissionType = models.CharField(max_length=50,null=True)
    # DriveType = models.CharField(max_length=50,null=True)
    # ClutchType = models.CharField(max_length=50,null=True)

    # FuelType = models.CharField(max_length=50,null=True)
    # TankCapacity = models.IntegerField(null=True)
    # TopSpeed = models.IntegerField(null=True)
    # Mileage = models.IntegerField(null=True)

    def __str__(self): 
        return self.name

    class Meta:
        db_table='car'
    
    # def __str__(self):
    #      return f"{self.name} {self.Price}{self.fuel} {self.brand}{self.carvarient} {self.cartype}"
        #  return f"clutch type={self.Engine.ClutchType} ,displacement= {self.Engine.EngineDisplacement}  {self.Engine.EngineType} {self.Engine.NoOfCylinder}  {self.Engine.Torque} "
    
    

    



