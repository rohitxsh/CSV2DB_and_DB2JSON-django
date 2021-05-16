Django  app to save CSV file data to MySQL DB and fetch it in JSON format from the DB.

![alt text](https://github.com/rohitxsh/CSV2DB_and_DB2JSON-django/blob/master/UI_snip.png)

Instructions to run the app:

Setup DB:
1. Run your MySQL server with user root and no password configuration or change the mysql connector code accordingly to add the password.
2. Run the following command in mysql shell > set global max_allowed_packet=67108864; (The sample file is of very large size and default allowed packet limit in mysql won't allow the program to insert the all the data which will result in an error)
3. Create a database named 'django1'

Run the app:
1. Install virtualenv: > pip install virtualenv
2. Create a virtual environment: > virtualenv <virtual_environment_name>
3. Activate the virtual environment: > .\\<virtual_environment_name>\Scripts\activate.bat
4. Install all the dependencies: > pip install -r requirements.txt
5. Run the migrate commands: > python manage.py migrate
6. Run the app: > python manage.py runserver
7. Access the app on: > localhost:8000 \
Try out the app :)
8. Once done you can deactivate the virtual environment: > .\\<virtual_environment_name>\Scripts\deactivate.bat
