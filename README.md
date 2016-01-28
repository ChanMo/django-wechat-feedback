======================
Django-wechat-feedback
======================

feedback base django.
Detailed documentation is in the "docs" directory

Quick start
-----------

1. Add "wechat-page" to your INSTALLED_APPS setting like this::
   INSTALLED_APPS = (
       ...
       'wechat',
       'wechat_member',
       'feedback',
   )

2. Include the wechat URLconf in your project urls.py like this::
   url(r'^feedback', include('feedback.urls')),

5. Run 'python manage.py migrate' to create the wechat models.

