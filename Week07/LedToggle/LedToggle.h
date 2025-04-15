#ifndef LedToggle_h
#define LedToggle_h

#include "Arduino.h"

	class LedToggle{
	public:
		LedToggle(int pin);
		LedToggle(int pin, unsigned long delayTime);	
		vold toggle();		
		
	private:
		int _pin;			
		bool _state;			
		unsigned long _delayTime;
};							

#endif
