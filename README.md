# DjangoAuth

Basic Django authenticating system for user login and registration

*Clone this and implement into your existing Django project by following the next steps*

__Step one__

Clone this git into your folder where the 'manage.py' file exists

__Step two__

Move the folders like so:
- Main Auth next to your 'manage.py' file
- If you have a Static folder, place the 'CSS' folder in it, else copy the full 'Static' folder.
- In your Templates folder, copy and place the 'Auth' folder.

__Step three__

In your 'settings.py' add 'Auth' to the list of installed apps

__Step four__

Make changes to the CSS in whatever way you like

__Step five__

Run these commands in your terminal to make sure your DataBase is up to date:
- python manage.py makemigrations
- python manage.py migrate

__Congrats! The Auth system should be working from now on!__

## Updates

| Update | Person | Date | Info |
| ----------- | ----------- | ----------- | ----------- |
| 1.1 | Sebastiaan | 06-12-2022 | Build of the project |