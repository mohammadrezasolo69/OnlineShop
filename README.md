# OnlineShop

This project is a store website.
In Backend, the Django framework , Database Postgres and the template is made with Bootstrap, JavaScript, and so on.

- [ ] It is possible to register (by sending an activation Email) and login user.
- [ ] It is possible to login with Google account and Github account
- [ ] It is possible to buy, like and save products, comment and search products, and ...
- [ ] AbstractUser is used to implement the user model.

===========================================================
# Installation guide:

You must have [Python](http://python.org/) installed.

create virtualenv and activate

Then run `pip install -r requirements.txt` to install dependencies.

cp `.env-sample` to `.env`

```bash
py manage.py makemigrations
py manage.py migrate
```

create superuser

python manage.py runserver

