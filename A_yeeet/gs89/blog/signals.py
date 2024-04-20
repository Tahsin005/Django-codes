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
@receiver(post_save, sender=User)
def at_end_save(sender, instance, created, **kwargs):
    if created:
        print('--------------------------------')
        print('Post save signal......')
        print('New Record')
        print('Sender : ', sender)
        print('Instance : ', instance)
        print('Created : ', created)
        print(f'Kwargs : {kwargs}')
    else:
        print('--------------------------------')
        print('Post save signal......')
        print('Old Record, update')
        print('Sender : ', sender)
        print('Instance : ', instance)
        print('Created : ', created)
        print(f'Kwargs : {kwargs}')
        
# post_save.connect(at_end_save, sender=User)
@receiver(pre_delete, sender=User)
def at_beginning_delete(sender, instance, **kwargs):
    print('--------------------------------')
    print('Pre delete signal......')
    print('Sender : ', sender)
    print('Instance : ', instance)
    print(f'Kwargs : {kwargs}')
# pre_delete.connect(at_beginning_delete, sender=User)


@receiver(post_delete, sender=User)
def at_ending_delete(sender, instance, **kwargs):
    print('--------------------------------')
    print('Post delete signal......')
    print('Sender : ', sender)
    print('Instance : ', instance)
    print(f'Kwargs : {kwargs}')
# post_delete.connect(at_ending_delete, sender=User)
@receiver(pre_init, sender=User)
def at_beginning_init(sender, *args, **kwargs):
    print('--------------------------------')
    print('Pre init signal......')
    print('Sender : ', sender)
    print(f'args : {args}')
    print(f'Kwargs : {kwargs}')
# pre_init.connect(at_beginning_init, sender=User)


@receiver(post_init, sender=User)
def at_ending_init(sender, *args, **kwargs):
    print('--------------------------------')
    print('Post init signal......')
    print('Sender : ', sender)
    print(f'args : {args}')
    print(f'Kwargs : {kwargs}')
# post_init.connect(at_ending_init, sender=User)