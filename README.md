Cloud Maya test

Documentation 
- mkdir workspace
- cd workspace
- git clone https://github.com/Soumya44/Soumya_Ecommerce
- python3 -m venv ecomm-env [python 3.7] 
- source ecomm-env/bin/activate
- pip install -r requirements.txt
- psycopg2 commented as its not required. (PostgreSQL related connector)
- pillow issues, resolved by going to https://pillow.readthedocs.io/en/latest/installation.html and installing the dependencies externally: brew install libtiff libjpeg webp little-cms2
- pip install mysqlclient (As we will be using mysql db engine) [ NOTE: brew install mysql ; brew services start mysql has to be executed before installing this]
- Added local.py file in settings folder, and added mysql credentials
- Python manage.py check    [Issues w.r.t to syntax in python 3.7 for this project]
- Install python 3.6.2 and re-activated virtualenv. 
- python mange migrate
           Faced issues w.r.t max_length: django.db.utils.OperationalError: (1426, "Too-big precision 100 specified for 'shipping_total'. Maximum is 65.")
	Fix: reduced the max_length to 65 as allowed by mysql [If PostgreSQL was used this error would ve not popped up]
- python manage.py createsuperuser
- python manage.py runserver [Ecommerce web app successfully set up in local system]
- python manage.py startapp mentoring 
- Add mentoring in INSTALLED_APPS of ecommerce/settings/local.py
- Created Mentor and Student classes in models.py
- python manage.py makemigrations  mentoring
- python mange migrate
- Added crud related functions/business logic for Mentor and Student in views.py
- Defined appropriate urls for the app in urls.py
- Created two model forms to display in html pages in forms.py
- Created templates folder inside monitoring folder, inside that created base.html and other appropriate html files for the CRUD operations which extends from base.html
- In order to access the mentoring platform hit this URL: http://localhost:8000/mentoring/
- You can either CRUD operations on mentor and students from the above link or http://localhost:8000/admin/mentoring/
- Search mentors logic: I am passing the student’s skill as query for Mentor objects filter as shown below:
student = get_object_or_404(Student, pk=pk)
mentors = Mentor.objects.filter(expertise=student.skill_to_learn)
