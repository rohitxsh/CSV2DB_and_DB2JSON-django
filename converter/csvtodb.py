import pandas as pd
import glob
import mysql.connector

path = r'files'
all_files = glob.glob(path + "/*.csv")
if not all_files:
    print("No CSV files")
li =[]
for filename in all_files:
        df = pd.read_csv(filename)
        li.append(df)
frame = pd.concat(li)

q= """Insert into converter_csvdata (Region, Country, Item_Type, Sales_Channel, Order_Priority, Order_ID, Order_Date,  Ship_Date, Units_Sold, Unit_Price, Unit_Cost, Total_Revenue, Total_Cost, Total_Profit) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"""
cnx = mysql.connector.connect(user='root', password='3497', database='django1',autocommit=True)
cursor = cnx.cursor()
cursor.execute('Delete from converter_csvdata')
cursor.executemany(q, frame.values.tolist())
cnx.commit()
print("Successfully parsed all CSV files and inserted the data into database!")
cursor.close()
cnx.close()