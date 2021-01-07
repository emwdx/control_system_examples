

//On/Off Control
/*
var setpoint = 100;

async function startProgram() {
	while(true){
		if(getLocation().y < setpoint){
			await rawMotor(128,128,0.2);
		}
		else{
			if(getLocation().y > setpoint){
				
				await rawMotor(-128,-128,0.2);
			}
			else{
				await setSpeed(0);
			}
			
		}
		await delay(0.025);
	}
}
*/

//On/Off control with Tolerance

/*

var tolerance = 20;
var speed = 40

async function startProgram() {
	while(true){
		if(getLocation().y < setpoint - tolerance){
			await rawMotor(speed,speed,0.2);
			
		}
		else{
			if(getLocation().y > setpoint+tolerance){
				
				await roll(-speed,-speed,0.2);
			}
			else{
				await setSpeed(0);
			}
			
			
		}
		await delay(0.025);
	}
}

*/

//Proportional control


/*
let setpoint =100;
let k = 4;

async function startProgram() {
	while(true){
		var location = getLocation().y;
		var error = setpoint - location;
		
		var output = k*error;
		
		if(output >255){
			
			output = 255;		
		
		}
		if(output < -255){
			
			output = -255;
		}
		await rawMotor(output,output,0.2);
		
		await delay(0.025);
	}
}

*/

//Proportional-Integral control

/*

let setpoint = 100;
let k = 3.0;
let kI = 0.5;
var accumulatedError = 0;

async function startProgram() {
	while(true){
		var location = getLocation().y;
		var error = setpoint - location;
		accumulatedError = accumulatedError + error
		
		var output = k*error + kI*accumulatedError;
		
		if(output >255){
			
			output = 255;		
		
		}
		if(output < -255){
			
			output = -255;
		}
		await rawMotor(output,output,0.2);
		
		await delay(0.025);
	}
}

*/

//Proportional-Derivative control

/*

let setpoint = 100;
let k = 3.0;
let kD = 1.5;
var oldError = 0;


async function startProgram() {
	while(true){
		var location = getLocation().y;
		
		var error = setpoint - location;
		var changeError = error - oldError;
		
		
		var output = k*error - kD*changeError;
		oldError = error
		
		if(output >255){
			
			output = 255;		
		
		}
		if(output < -255){
			
			output = -255;
		}
		await rawMotor(output,output,0.2);
		
		await delay(0.025);
	}
}


*/


//Proportional-Integral-Derivative Control

/*
let setpoint = 100;
let k = 3.0;
let kD = 0.5;
let kI = 0.1;
var accumulatedError = 0;
var oldError = 0;


async function startProgram() {
	while(true){
		var location = getLocation().y;
		
		var error = setpoint - location;
		var changeError = error - oldError;
		accumulatedError = error + accumulatedError
		
		
		var output = k*error - kD*changeError + kI*accumulatedError;
		oldError = error
		
		if(output >255){
			
			output = 255;		
		
		}
		if(output < -255){
			
			output = -255;
		}
		await rawMotor(output,output,0.2);
		
		await delay(0.025);
	}
}



*/
