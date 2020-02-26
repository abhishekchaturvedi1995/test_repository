from random import randint, random, uniform

incircle=0
outcircle=0
for i in range(100000):	
	x=uniform(1,10)
	y=uniform(1,10)
	print tuple((x,y))
	if(((x-5.5)**2+(y-5.5)**2)<=(4.5*4.5)):
		incircle += 1
	else:
		outcircle += 1
	totalpoints = incircle + outcircle
	pi = 4*float(float(incircle)/float(totalpoints))
	print "In circle points - "+str(incircle)
	print "outcircle points - "+str(outcircle)
	print "total points - "+str(totalpoints)
	print "PIE"
	print pi





