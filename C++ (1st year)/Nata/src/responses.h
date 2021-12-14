/*
 * responses.h
 *
 *  Created on: Apr 28, 2020
 *      Author: vlad
 */

#pragma once
#ifndef RESPONSES_H_
#define RESPONSES_H_

#include <string>
#include <vector>
#include <map>
#include <iostream>
using namespace std;

struct BusesForStopResponse
{
	// Наполните полями эту структуру
	string stop;
	vector<string> buses;
};

struct StopsForBusResponse
{
	// Наполните полями эту структуру
	vector<pair<string, vector<string>>> stopBusesVector;
	string bus;

};

struct AllBusesResponse {
	// Наполните полями эту структуру
	map<string, vector<string>> busesToStops;
};

ostream& operator << (ostream& os, const BusesForStopResponse& r);
ostream& operator << (ostream& os, const StopsForBusResponse& r);
ostream& operator << (ostream& os, const AllBusesResponse& r);




#endif /* RESPONSES_H_ */
