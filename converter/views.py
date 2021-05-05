from django.contrib import messages
from django.core.files.storage import default_storage
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

#rest_framework imports
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from . models import CSVdata
from . serializers import CSVdataSerializer

import logging
import pandas as pd
import glob
import mysql.connector

# Create your views here.
def index(request):
    if request.method == "GET":
        return render(request, "index.html", {})
    try:
        #reading all files from the "files" folder
        path = r'files'
        all_files = glob.glob(path + "/*.csv")
        if not all_files:
            messages.error(request,"No CSV files in the \"files\" foder")
            return HttpResponseRedirect(reverse("index"))

        li =[]

        #appending dataframe of all csv files into one
        for filename in all_files:
            df = pd.read_csv(filename)
            li.append(df)
        frame = pd.concat(li)

        #inserting the dataframe into sql database using executemany to achieve better performance
        q= """Insert into converter_csvdata (Region, Country, Item_Type, Sales_Channel, Order_Priority, Order_ID, Order_Date,  Ship_Date, Units_Sold, Unit_Price, Unit_Cost, Total_Revenue, Total_Cost, Total_Profit) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"""
        cnx = mysql.connector.connect(user='root', password='3497', database='django1',autocommit=True)
        cursor = cnx.cursor()
        #clearing up the data to insert new data
        #incase if you don't want to clear up the table just comment the line below
        cursor.execute('Truncate table converter_csvdata')
        cursor.executemany(q, frame.values.tolist())
        cnx.commit()
        messages.success(request, "Successfully parsed all CSV files and inserted the data into database!")
        cursor.close()
        cnx.close()

    except Exception as e:
        logging.getLogger("error_logger").error("Error: "+repr(e))
        messages.error(request,"Error: "+repr(e))

    return HttpResponseRedirect(reverse("index"))

def file_add(request):
    pass

def file_delete(request):
    pass

class JSONdata(APIView):
    def get(self, request):
        JSON_data = CSVdata.objects.filter(Country = 'India')
        serializer = CSVdataSerializer(JSON_data, many = True)
        if not serializer.data:
            messages.error(request,"No data to fetch!")
            return HttpResponseRedirect(reverse("index"))
        else:
            return Response(serializer.data)
    def post(self):
        pass