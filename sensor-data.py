import android, time

droid = android.Android(('192.168.1.133' , 45001))
# name = droid.batteryGetLevel()
# print name  # name is a namedtuple

dt = 50
curTime =0
endTime =10000	 # in milliseconds
droid.startSensingTimed(2, dt) #first arg picks accelerometer , dt is time between

while curTime < endTime :
	print droid.sensorsReadAccelerometer().result
	print droid.time()
	time.sleep(dt/1000.0)
	curTime +=dt
droid.stopSensing()