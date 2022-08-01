# Django Rest Framework

``` py

python -m venv venv
./venv/bin/activate (linux)
venv\Scripts\activate (win)
django-admin startproject project .
python manage.py startapp api
python manage.py createsuperuser
python manage.py runserver 8000

python manage.py makemigrations
python manage.py migrate
# Caso falha:
python manage.py migrate --run-syncdb

#add app:
'rest_framework.urls'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls')),
]
```
