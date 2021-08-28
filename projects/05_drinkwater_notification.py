from plyer import notification
import time


if __name__=="__main__":
    while True:
        notification.notify(
            title = "**Please drink water Udit!!!",
            message = "It is very important to take water at a certain time",
            app_icon = "E:\\Python\\projects\\water_glass.ico",
            timeout = 10       #Means the notification is raised for only 10 second
              )
        time.sleep(60*60)      


        #To run this notification system in background run 'pythonw .\file name' in terminal