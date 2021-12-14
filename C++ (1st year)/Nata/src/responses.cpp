/*
 * responses.cpp
 *
 *  Created on: Apr 28, 2020
 *      Author: vlad
 */

#include "responses.h"

ostream& operator << (ostream& os, const BusesForStopResponse& r)
{
	// Реализуйте эту функцию
	if (r.buses.size() == 0) os << "No stop";
	else
	{
		for (size_t i = 0; i < r.buses.size(); i++) os << r.buses[i] << ' ';
	}
	return os;
}

ostream& operator << (ostream& os, const StopsForBusResponse& r)
{

	// Реализуйте эту функцию
	if (r.stopBusesVector.size() == 0) os << "No bus";
	else
	{
		for (size_t i = 0; i < r.stopBusesVector.size(); i++)
		{
			string key = r.stopBusesVector[i].first;
			vector<string> value = r.stopBusesVector[i].second;
			os << "Stop " << key << ": ";
			if (value.size() == 1) os << "no interchange";
			else
			{
				for (const string& bus : value)
				{
					if (r.bus != bus) os << bus << ' ';
				}
			}
			if (static_cast<int>(i) < static_cast<int>(r.stopBusesVector.size())-1)	os << endl;
		}
	}
	return os;
}
//

ostream& operator << (ostream& os, const AllBusesResponse& r) {
	// Реализуйте эту функцию
	if (r.busesToStops.empty()) os << "No buses";
	else
	{
		int counter = 0;
		for (const auto& [key, value] : r.busesToStops)
		{
			os << "Bus " << key << ": ";
			for (const string& stop : value)
			{
				os << stop << ' ';
			}
			if (counter < static_cast<int>(r.busesToStops.size()) - 1) os << endl;
			counter++;
		}
	}
	return os;
}

