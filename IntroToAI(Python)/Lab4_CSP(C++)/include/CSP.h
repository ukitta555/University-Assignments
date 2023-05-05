#pragma once

#include <utility>
#include <vector>
#include <map>
#include <set>
#include <deque>

#include "Classes.h"

using namespace std;

class Schedule;

struct Variable {
    size_t id;
    Time time;
    Group group;

    Variable(size_t id_, Time time_, Group group_)
            : id(id_), time(move(time_)), group(group_) {}

    bool operator<(const Variable& other) const {
        return id < other.id;
    }
};

struct Domain {
    Subject subject;
    Teacher teacher;
    Room room;

    Domain(Subject subject_, Teacher teacher_, Room room_) :
            subject(subject_), teacher(teacher_), room(room_) {}
};

class CSPSolver {
public:
    CSPSolver() = default;

    void SetVariables(const vector<Group>& groups, const vector<Day>& days, int LESSONS_PER_DAY);

    void SetDomains(const vector<Room>& rooms);

    Schedule Solve();

private:

    bool Backtracking(map<const Variable *, Domain *>& cur, map<const Variable *, Domain *>& ans);


    bool check_constraints(map<const Variable *, Domain *>& cur);

    bool check_constraints(map<const Variable *, Domain *>& cur, const Variable *variable1, Domain *domain1);

    // Heuristics:

    const Variable *SelectUnassignedVariable(map<const Variable *, Domain *>& cur);

    vector<Domain *>& OrderDomainValues(vector<Domain *>& domains);

    vector<Domain *>& LeastConstrainingValue_Heuristic(const Variable *variable, vector<Domain *>& domains);

    const Variable *MRV_Heuristic(map<const Variable *, Domain *>& cur);

    const Variable *Degree_Heuristic(map<const Variable *, Domain *>& cur);

    void ForwardChecking(const Variable *variable, Domain *domain, map<const Variable *, Domain *>& cur);

    void RemoveInconsistentDomains(const Variable *variable, Domain *domain, map<const Variable *, Domain *>& cur);

    void UnRemoveInconsistentDomains(const Variable *variable);

    deque<Variable> variables_storage;
    set<const Variable *> free_variables;
    deque<Domain> domains_storage;
    map<const Variable *, vector<Domain *>> domains;
    map<const Variable *, vector<Domain *>> tmp;
    map<const Variable *, vector<Variable *>> variable_neighbours;
    size_t kLESSONS_PER_DAY;
};