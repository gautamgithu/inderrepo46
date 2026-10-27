import datetime, time

alarm = input("Alarm time (HH:MM:SS): ")
while datetime.datetime.now().strftime("%H:%M:%S") < alarm:
  time.sleep(1)
print("\a" * 5)
print("⏰ ALARM! Uth jao!")
