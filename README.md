# Features

All-in-one web based Enterprise Resource Planning software: 
- Customer management
- Employees management
- Simple and recurring billing system
- Content Management System
- Ticketing system
- Financial reporting
- Reminder
- Organizer 
- Notepad

# Demo

```
http://ec2-13-38-127-165.eu-west-3.compute.amazonaws.com:8000/todo
user: demo
password: demo
```

# Developer Installation 

```bash

git clone https://github.com/escomputers/allwisp.git

#token expiring 12th September 2022
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


cd allwisp && wget https://github.com/escomputers/PortableVirtualenv/raw/master/venv3.9_lin_amd64.tar.xz

tar -xf venv3.9_lin_amd64.tar.xz

source venv3.9/bin/activate

python -m pip install -r requirements.txt

rsync -a site-packages/ venv3.9/lib/python3.9/site-packages/

cd allwisp && python manage.py makemigrations

python manage.py migrate

python manage.py createcachetable django_orm_cache_table

#uncomment in settings.py
"""
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'django_orm_cache_table',
    }
}
"""

python manage.py createsuperuser

python manage.py runserver 0.0.0.0:8000

#for DjangoQ open new terminal with venv activated
python manage.py qcluster
```

1) Create user groups 
2) Assign users to groups
3) Create task list with same name used in allwisp/allwisp/allwisp/settings.py

# Production

System requirements
**********
```
Debian 10> or Ubuntu 20.04>
Python 3.8>
Pip

#Javascript libraries in compressed versions (min.js)
Adminlte                  		v3.2.0
jQuery                    		v3.6.0
jQuery UI                 		v1.13.1
jQuery OverlayScrollbars  		v1.13.0
jQuery TableDND           		v0.5.0
Bootstrap Bundle          		v.4.0.0
Bootstrap Tagsinput       		v0.8.0
Easymde                   		v2.15.0
Fullcalendar              		v5.10.1
Select2                   		v4.0.13
Moment                    		v3.0.0
Bootstrap Datetimepicker  		v4.17.49
Bootstrap Toggle          		v2.2.0
Bootstrap icheck          		v3.0.1
Bootstrap Duallistbox     		v4.0.2
Daterangepicker           		v.3.0.5
Datatables                		v1.11.5
Datatables buttons        		v2.2.2
Datatables colreorder     		v1.5.5
Datatables fixedcolumns   		v4.0.2
Datatables fixedheader    		v3.2.2
Datatables rowreorder     		v1.2.8
JSZip                     		v3.7.1
Pdfmake                         v0.2.4
Maplibre-gl                     v1.15.2
Maplibre-gl-js-amplify (umd)	v1.5.0
Aws-amplify-core              	v4.3.0 
Aws-amplify-auth                v4.3.8       
Aws-amplify-geo                 v1.3.2
Aws-sdk                         v2.1167.0
```
