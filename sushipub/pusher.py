from django.conf import settings
from pusher import Pusher

socket = Pusher(app_id=settings.PUSHER_APP_ID,
                key=settings.PUSHER_KEY,
                secret=settings.PUSHER_SECRET, cluster='eu', ssl=True)
