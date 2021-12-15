# Features

In progress

# Demo

In progress

# Requirements

```bash
Ubuntu Server 20.04 LTS
Python        3.8.10
Pip           20.0.2

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

# Installation 

VIRTUAL ENV
**********
```bash

cd $HOME

git clone https://github.com/escomputers/allwisp.git

#token expiring 13th March 2022
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

cd allwisp

sudo python3 -m venv env_allwisp

source env_allwisp/bin/activate

cd allwisp

python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py createsuperuser

python3 manage.py runserver 0.0.0.0:8000

1) Create user groups 
2) Assign users to groups
3) Create task list with same name used in allwisp/allwisp/allwisp/settings.py
```

PRODUCTION
**********
```bash

In progress

```
