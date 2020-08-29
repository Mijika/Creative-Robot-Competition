import time

time = time.strftime("%Y %m %d %I:%M").split(" ")
time = time[0] + "년 " + time[1] + "월 " + time[2] + "일 " + time[3]
print(time)
