/*
 * bus_manager.cpp
 *
 *  Created on: Apr 28, 2020
 *      Author: vlad
 */

#include "bus_manager.h"

void BusManager::AddBus(const string& bus, const vector<string>& stops)
	{
		// Реализуйте этот метод
		buses_to_stops[bus] = stops;
		for (const string& stop : stops)
		{
			stops_to_buses[stop].push_back(bus);
		}
	}

BusesForStopResponse BusManager::GetBusesForStop(const string& stop) const
	{
		// Реализуйте этот метод
		vector<string> responseVector;
		if (stops_to_buses.count(stop) > 0)
		{
			responseVector = stops_to_buses.at(stop);
		}
		return {stop, responseVector};
	}

	StopsForBusResponse BusManager::GetStopsForBus(const string& bus) const {
		// Реализуйте этот метод
		vector<pair<string, vector<string>>> stopsBusesVector;
		if (buses_to_stops.count(bus) > 0)
		{
			for (const string& stop : buses_to_stops.at(bus))
			{
				stopsBusesVector.push_back(make_pair(stop, stops_to_buses.at(stop)));
			}
		}
		return {stopsBusesVector, bus};
	}

	AllBusesResponse BusManager::GetAllBuses() const {
		// Реализуйте этот метод
		return {buses_to_stops};
	}

