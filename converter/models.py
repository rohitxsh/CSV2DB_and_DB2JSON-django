from django.db import models

# Create your models here.
class CSVdata(models.Model):
    Region = models.CharField(max_length=50)
    Country = models.CharField(max_length=50)
    Item_Type = models.CharField(max_length=50)
    Sales_Channel = models.CharField(max_length=50)
    Order_Priority = models.CharField(max_length=50)
    Order_Date = models.CharField(max_length=50)
    Order_ID = models.CharField(max_length=50)
    Ship_Date = models.CharField(max_length=50)
    Units_Sold = models.IntegerField()
    Unit_Price = models.FloatField()
    Unit_Cost = models.FloatField()
    Total_Revenue = models.FloatField()
    Total_Cost = models.FloatField()
    Total_Profit = models.FloatField()