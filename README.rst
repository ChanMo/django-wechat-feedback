基于django-wechat-member的留言系统
===================================


快速开始
---------

安装django-wechat-feedback:

.. code-block::

    pip install django-wechat-feedback

在settings.py文件中添加feedback:

.. code-block::

    INSTALLED_APPS = (
        ...
        'feedback',
    )

在urls.py文件中添加:

.. code-block::

    url(r'^feedback/', include('feedback.urls')),

更新数据库:

.. code-block::

    python manage.py migrate
