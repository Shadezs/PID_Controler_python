tError1 = 0;
tError2 = 0;
error = 0;
forwardKp = 4;
tDerivative2 = 0;
tTotalError2 = 0;
tPrevError2 = 0;

def forward(distance, kP, velocity)
{
	resetMotorEncoder(lDrive);
	resetMotorEncoder(rDrive);
	while(abs(getMotorEncoder(lDrive))<distance)
	{
		tError1 = (getMotorEncoder(lDrive)-getMotorEncoder(rDrive))*kP;
		error = (distance-getMotorEncoder(lDrive))*forwardKp;
		setMotorSpeed(lDrive,error-tError1);
		setMotorSpeed(rDrive,error+tError1);
	}
	setMotorSpeed(lDrive,0);
	setMotorSpeed(rDrive,0);
}
def turn(heading,kP,kI,kD)
{
	tError2 = heading - SensorValue(gyro);
	while(abs(tDerivative2)>0||abs(tError2)>1.5)
	{
		tError2 = heading - SensorValue(gyro);
		tDerivative2 = tError2 - tPrevError2;
		tTotalError2 = tTotalError2 + tError2;
		setMotorSpeed(lDrive,-(tError2*kP)+(tTotalError2*kI)+(tDerivative2*kD));
		setMotorSpeed(rDrive,(tError2*kP)+(tTotalError2*kI)+(tDerivative2*kD));
		tPrevError2 = tError2;
	}
}
//turn(heading,velocity,kP,kI,kD)
task main()
{
	drawLine(5, 5, 10, 10);   //To test how far the code goes and when.
	forward(500,2,100);
	drawLine(15, 10, 20, 15);   //To test how far the code goes and when.
	turn(-90,1,0,2);
	drawLine(25, 15, 30, 20);   //To test how far the code goes and when.
	sleep(5000);
}
