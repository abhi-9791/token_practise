from django.apps import AppConfig


class TokenPractiseAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'token_practise_app'
    def ready(self):
       
        import token_practise_app.signals 
