from django.apps import AppConfig  # type: ignore[reportMissingModuleSource]



class BlogappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blogapp'