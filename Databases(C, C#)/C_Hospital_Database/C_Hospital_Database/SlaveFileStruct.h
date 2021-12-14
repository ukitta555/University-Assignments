#pragma once
#include "Date.h"
#include "Time.h"

typedef struct AppointmentInfo {
	Date appointmentDate;
	Time appointmentTime;
	int doctorId;
	int patientId;
} AppointmentInfo;

typedef struct SlaveFileStruct {
	AppointmentInfo info;
	int nextSlave;
	int appointmentId;
} SlaveFileStruct;