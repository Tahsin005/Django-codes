from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User 
from django.dispatch import receiver


@receiver(user_logged_in, sender=User)
def login_success(sender, request, **kwargs):
    # print('--------------------------------')
    # print('Logged in signal......')
    ip = request.META.get('REMOTE_ADDR')
    # print(f'IP : {ip}')
    request.session['ip'] = ip