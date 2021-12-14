/*
 * query.h
 *
 *  Created on: Apr 28, 2020
 *      Author: vlad
 */

#pragma once
#ifndef QUERY_H_
#define QUERY_H_

#include <vector>
#include <string>
#include <iostream>
#include <sstream>
using namespace std;

enum class QueryType {
	NewBus,
	BusesForStop,
	StopsForBus,
	AllBuses
};

struct Query {
	QueryType type;
	string bus;
	string stop;
	vector<string> stops;
};

istream& operator >> (istream& is, Query& q);

#endif /* QUERY_H_ */
