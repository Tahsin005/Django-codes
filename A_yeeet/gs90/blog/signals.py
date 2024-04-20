from django.dispatch import Signal, receiver

# Creating signal

notification = Signal()

# Receiver fucntion
@receiver(notification)
def show_notification(sender, **kwargs):
    print(sender)
    print(f'Kwaregs : {kwargs}')
    print('Notification')