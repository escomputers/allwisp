# Features

In progress

# Demo

In progress

# Developer Installation 

```bash

sudo su

git clone -b development https://github.com/escomputers/allwisp.git

#token expiring 13th March 2022
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


cd allwisp && wget https://github.com/escomputers/PortableVirtualenv/raw/master/venv3.9_lin_amd64.tar.xz

tar -xf venv3.9_lin_amd64.tar.xz

source venv3.9/bin/activate

python -m pip install -r requirements.txt

unzip site-packages.zip

rsync -a site-packages/ venv3.9/lib/python3.9/site-packages/

cd allwisp && python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver 0.0.0.0:8000
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
jQuery                    v3.6.0
jQuery UI                 v1.12.1
jQuery OverlayScrollbars  v1.13.0
jQuery TableDND           v0.5.0
Bootstrap Bundle          v.4.6.0
Bootstrap Tagsinput       v0.8.0
AdminLTE                  v3.1.0
Easymde                   v2.15.0
Fullcalendar              v2.2.5
```
