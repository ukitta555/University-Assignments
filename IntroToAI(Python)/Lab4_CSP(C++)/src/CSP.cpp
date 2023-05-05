#include "CSP.h"

#include <random>
#include <algorithm>

#include "Schedule.h"

void CSPSolver::SetVariables(const vector<Group>& groups, const vector<Day>& days, int LESSONS_PER_DAY) {
    kLESSONS_PER_DAY = LESSONS_PER_DAY;
    size_t num = 0;
    for (const Day& day : days) {
        for (size_t lesson = 1; lesson <= LESSONS_PER_DAY; ++lesson) { // for all lessons in each day
            int start = num;
            for (const Group& group : groups) { // for each group
                variables_storage.push_back(Variable{num, Time{day, lesson}, group}); // deque
                free_variables.insert(&variables_storage.back()); // set
                ++num;
            }
            int finish = num - 1; // last assigned id
            for (int i = start; i <= finish; ++i) {
                for (int j = start; j <= finish; ++j) {
                    if (i != j) {
                        variable_neighbours[&variables_storage[i]].push_back(&variables_storage[j]);
                    }
                }
            }
        }
    }
}

void CSPSolver::SetDomains(const vector<Room>& rooms) {
    for (const Variable& variable : variables_storage) { // for each slot in the schedule...
        for (const Subject& subject : variable.group.subjects) { // for each subject... ( int the group)
            for (const Teacher& teacher : subject.teachers) { // for each teacher that is eligible to teach this course...
                for (const Room& room : rooms) { // for each room....
                    domains_storage.emplace_back(subject, teacher, room); // append to the end
                    domains[&variable].push_back(&domains_storage.back());
                }
            }
        }
        shuffle(domains[&variable].begin(), domains[&variable].end(), mt19937(random_device()()));
    }
}

Schedule ConvertToSchedule(map<const Variable *, Domain *>& cur) {
    Schedule schedule;

    for (const auto&[variable, domain] : cur) {
        size_t num = variable->time.number;
        size_t sz = schedule.schedule[variable->group][variable->time.day].size();
        schedule.schedule[variable->group][variable->time.day].resize(max(sz, num));
        schedule.schedule[variable->group][variable->time.day][num - 1] = Class(variable->group,
                                                                                domain->subject,
                                                                                domain->room,
                                                                                domain->teacher,
                                                                                variable->time);
    }

    return schedule;
}

Schedule CSPSolver::Solve() {
    map<const Variable *, Domain *> cur, ans;
    Backtracking(cur, ans);

    return ConvertToSchedule(ans);
}

const Variable *CSPSolver::MRV_Heuristic(map<const Variable *, Domain *>& cur) {
    const int INF = 1e9;
    int mn = INF;
    const Variable *res = nullptr;
    for (const Variable *variable : free_variables) {
        int cnt = domains[variable].size(); // TODO: possible optimization with set ordering by sizes
        if (cnt < mn) {
            res = variable;
            mn = cnt;
        }
    }
    return res;
}

const Variable *CSPSolver::Degree_Heuristic(map<const Variable *, Domain *>& cur) {
    const int INF = 1e9;
    int mx = -INF;
    const Variable *res = nullptr;
    for (const Variable *variable : free_variables) {
        int cnt = 0;
        // don't even try if degree of some prev variable is greater than the current maximum
        if (mx >= (int) variable_neighbours[variable].size()) {
            continue;
        }
        int k = 0;
        for (const Variable *variable1 : variable_neighbours[variable]) {
            ++k;
            if (!cur.count(variable1)) { // current does not have this variable assigned
                ++cnt;
            }
            // early break if it does not make sense to continue iterating
            if (cnt + ((int) variable_neighbours[variable].size() - k) <= mx) {
                break;
            }
        }
        if (cnt > mx) {
            res = variable;
            mx = cnt;
        }
    }
    return res;
}

const Variable *CSPSolver::SelectUnassignedVariable(map<const Variable *, Domain *>& cur) {
    for (const Variable *variable : free_variables) {
        return variable;
    }
    return nullptr;
}

vector<Domain *>& CSPSolver::OrderDomainValues(vector<Domain *>& domains) {
//    shuffle(domains.begin(), domains.end(), mt19937(random_device()()));
    return domains;
}

//bool CSPSolver::check_constraints(map<const Variable *, Domain *>& cur) {
//    for (const auto&[variable1, domain1] : cur) {
//        for (Variable *variable2 : variable_neighbours[variable1]) {
//            if (cur.count(variable2)) {
//                Domain *domain2 = cur[variable2];
//                if (domain1->teacher == domain2->teacher) {
//                    return false;
//                }
//                if (domain1->room == domain2->room) {
//                    return false;
//                }
//            }
//        }
//    }
//    return true;
//}

bool CSPSolver::check_constraints(map<const Variable *, Domain *>& cur, const Variable *variable1, Domain *domain1) {
    for (Variable *variable2 : variable_neighbours[variable1]) {
        if (cur.count(variable2)) {
            Domain *domain2 = cur[variable2];
            if (domain1->teacher == domain2->teacher) {
                return false;
            }
            if (domain1->room == domain2->room) {
                return false;
            }
        }
    }
    return true;
}

bool CSPSolver::Backtracking(map<const Variable *, Domain *>& cur, map<const Variable *, Domain *>& ans) {
    if (cur.size() == variables_storage.size()) {
        ans = cur;
        return true;
    }

    // You can choose the method of selecting new variable base on different heuristics.
    //
//    const Variable *variable = SelectUnassignedVariable(cur);
    const Variable *variable = MRV_Heuristic(cur);
//    const Variable *variable = Degree_Heuristic(cur);

    free_variables.erase(variable);

    for (Domain *domain : OrderDomainValues(domains[variable])) { // TODO: OrderDomainValues
        if (check_constraints(cur, variable, domain)) {
            cur[variable] = domain;
            ForwardChecking(variable, domain, cur);
            bool result = Backtracking(cur, ans);
            if (result) {
                return true;
            }
            cur.erase(variable);
            UnRemoveInconsistentDomains(variable);
        }
    }

    free_variables.insert(variable);
    return false;
}

void
CSPSolver::RemoveInconsistentDomains(const Variable *variable, Domain *domain, map<const Variable *, Domain *>& cur) {
    for (Variable *variable2 : variable_neighbours[variable]) {
        if (!cur.count(variable2)) {
            for (int i = 0; i < domains[variable2].size();) {
                Domain *domain2 = domains[variable2][i];
                if (domain->teacher == domain2->teacher || domain->room == domain2->room) {
                    swap(domains[variable2][i], domains[variable2].back());
                    tmp[variable2].push_back(domains[variable2].back());
                    domains[variable2].pop_back();
                } else {
                    ++i;
                }
            }
        }
    }
}

void CSPSolver::UnRemoveInconsistentDomains(const Variable *variable) {
    for (Variable *variable2 : variable_neighbours[variable]) {
        for (int i = 0; i < tmp[variable2].size(); ++i) {
            domains[variable2].push_back(tmp[variable2][i]);
        }
    }
}

void CSPSolver::ForwardChecking(const Variable *variable, Domain *domain, map<const Variable *, Domain *>& cur) {
    RemoveInconsistentDomains(variable, domain, cur);
}

int CalcScore(const Variable *variable, const Domain *domain) {
    return domain->subject.teachers.size();
}

vector<Domain *>& CSPSolver::LeastConstrainingValue_Heuristic(const Variable *variable, vector<Domain *>& cur_domains) {
    sort(cur_domains.begin(), cur_domains.end(), [variable](const Domain *first, const Domain *second) {
        return CalcScore(variable, first) < CalcScore(variable, second);
    });
    //    shuffle(domains.begin(), domains.end(), mt19937(random_device()()));
    return cur_domains;
}
