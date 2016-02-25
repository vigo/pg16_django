# Django ile Blog

Django ile hızlıca basit bir blog uygulaması yapalım.

## Gerekenler

* GIT
* Python (2.7+)
* PIP

## Kurulum

```bash
git clone https://github.com/vigo/pg16_django

(sudo) easy_install pip # eğer pip yoksa...
(sudo) pip install django

cd pg16_django/
python manage.py migrate
python migrate.py createsuperuser  # admin panel için kullanıcı oluşturun
python manage.py runserver         # geliştirme yapmak için sunucuyu çalıştırın
```

Şimdi [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
adresinden **admin panel**’e giriş yapabilirsiniz.