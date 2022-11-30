import time
import threading

from .models import UserAccount

def hello():
    accounts = UserAccount.objects.all()
    # accounts.update(key_used=2)
    # threading.Timer(86400.0, hello).start()

hello()

