#pragma once

#include <vector>
#include <map>

#include "Classes.h"

using namespace std;

struct Schedule {
    using Schedule_Per_Group = map<Day, vector<Class>>;
    map<Group, Schedule_Per_Group> schedule;
};