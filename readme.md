# Setup

- Install the pyenv and other required depedencies from the url [url](https://github.com/hitul007/shortcuts/blob/master/python-server-setup.sh).
- Create `local_settings.py` file inside `main` package and add below code.

```python
DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "NAME": "db-name",
        "USER": "username",
        "PASSWORD": "password",
        "HOST": "localhost",
        "PORT": "",
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue'
        }
    },
    'formatters': {
        'main_formatter': {
            'format': '%(levelname)s:%(name)s: %(message)s '
                      '(%(asctime)s; %(filename)s:%(lineno)d)',
            'datefmt': "%Y-%m-%d %H:%M:%S",
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'main_formatter',
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django': {
            'handlers': ['console', ],
        },
        'py.warnings': {
            'handlers': ['console', ],
        },
        '': {
            'handlers': ['console'],
            'level': "DEBUG",
        },
    }
}

```

- Run `pip install -r requirements.txt`.
- Run `pre-commit install`.

---

# Usage

- All the new models must inherite `main.BaseModel`.
- Always use `models.<Your model name>.onjects.dfilter()` instead of using `filter`. For more info read the documentation of `main.BaseModel`.
