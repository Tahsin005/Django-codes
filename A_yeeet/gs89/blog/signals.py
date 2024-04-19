from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_init, pre_save, pre_delete, post_init, post_save, post_delete


@receiver(user_logged_in, sender=User)
def login_success(sender, request, user, **kwargs):
    print('--------------------------------')
    print('Logged in signal......')
    print('Sender : ', sender)
    print('Request : ', request)
    print('User : ', user)
    print('User Password : ', user.password)
    print(f'kwargs : {kwargs}')
    
# user_logged_in.connect(login_success, sender=User)



@receiver(user_logged_out, sender=User)
def logout_success(sender, request, user, **kwargs):
    print('--------------------------------')
    print('Logged out signal......')
    print('Bye bye bye bye bye bye bye bye bye bye bye bye bye bye bye bye bye bye')
    print('Sender : ', sender)
    print('Request : ', request)
    print('User : ', user)
    print('User Password : ', user.password)
    print(f'kwargs : {kwargs}')
    
# user_logged_out.connect(logout_success, sender=User)

@receiver(user_login_failed)
def login_failed(sender, credentials, request, **kwargs):
    print('--------------------------------')
    print('Login failed signal......')
    print('Sender : ', sender)
    print('Request : ', request)
    print('Credentials : ', credentials)
    print(f'kwargs : {kwargs}')
    
# user_login_failed.connect(login_failed)



@receiver(pre_save, sender=User)
def at_beginning_save(sender, instance, **kwargs):
    print('--------------------------------')
    print('Pre save signal......')
    print('Sender : ', sender)
    print('Instance : ', instance)
    print(f'Kwargs : {kwargs}')
# pre_save.connect(at_beginning_save, sender=User)

@receiver(pre_save, sender=User)
def at_beginning_save(sender, instance, **kwargs):
    print('--------------------------------')
    print('Pre save signal......')
    print('Sender : ', sender)
    print('Instance : ', instance)
    print(f'Kwargs : {kwargs}')
# pre_save.connect(at_beginning_save, sender=User)
    
# 54:00