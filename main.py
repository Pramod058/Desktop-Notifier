#module import
from plyer import notification
from time import sleep

while True:
    notification.notify(
        title = "Break",
        message= "Hi Time to take break🥱🥱!!",
        timeout = 10,
        app_icon = None

        )
    sleep(3000)
