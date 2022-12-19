from datetime import *
from win10toast import ToastNotifier

a =int(input('Please Enter timer : '))
b = int(input( "Please Enter minutes : "))
c= input(('Please Enter PM OR AM : '))

if c =='pm'  :
    a+=12

    

while True:
    if a==datetime.now().hour and b==datetime.now().minute :
           print("done")
           
           toaster = ToastNotifier()
           toaster.show_toast("موعد الصلاة",
         "حان الان موعد الصلاة",
         icon_path='tt.ico',
         duration=3,
         threaded=True)
           break
        
    







# from win10toast import ToastNotifier

# def job():
#     print("I'm working...")

# schedule.every(10).minutes.do(job)


# while True:
#     schedule.run_pending()
#     time.sleep(1)