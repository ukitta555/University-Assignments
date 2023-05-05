#include <iostream>
#include <vector>
#include <random>
#include <algorithm>

#include "Classes.h"
#include "CSP.h"
#include "Schedule.h"
#include "profile.h"

using namespace std;

const int TEACHERS_PER_SUBJECT = 4;
const int SUBJECTS_PER_GROUP = 7;
const int LESSONS_PER_DAY = 3;

template<typename T>
static vector<T> GetRandomSubset(vector<T> vec, size_t len) {
    shuffle(vec.begin(), vec.end(), mt19937(random_device()()));
    return {vec.begin(), vec.begin() + len};
}

static vector<Teacher> GetRandomSubsetOfTeachers(const vector<Teacher>& teachers) {
    return GetRandomSubset(teachers, TEACHERS_PER_SUBJECT);
}

static vector<Subject> GetRandomSubsetOfSubjects(const vector<Subject>& subjects) {
    return GetRandomSubset(subjects, SUBJECTS_PER_GROUP);
}

int main() {
    vector<Day> days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday"}; // 5
    vector<Teacher> teachers = {
            Teacher("Merk"),
            Teacher("Margo"),
            Teacher("Fish"),
            Teacher("Roma"),
            Teacher("Pokemon"),
            Teacher("Bob"),
            Teacher("Nika"),
            Teacher("Vlad"),
    }; // 8
    vector<Room> rooms = {
            Room(215, 30),
            Room(505, 35),
            Room(1, 27),
            Room(39, 100),
            Room(303, 25),
            Room(27, 35),
    }; // 6
    vector<Subject> subjects = {
            Subject("Algebra", GetRandomSubsetOfTeachers(teachers)),
            Subject("Geometry", GetRandomSubsetOfTeachers(teachers)),
            Subject("Programming", GetRandomSubsetOfTeachers(teachers)),
            Subject("Discrete Math", GetRandomSubsetOfTeachers(teachers)),
            Subject("DataStorage science", GetRandomSubsetOfTeachers(teachers)),
            Subject("DataStorage structures", GetRandomSubsetOfTeachers(teachers)),
            Subject("Math Anal.", GetRandomSubsetOfTeachers(teachers)),
            Subject("Prob. Th.", GetRandomSubsetOfTeachers(teachers)),
            Subject("Algorithms", GetRandomSubsetOfTeachers(teachers)),
    }; // 9
    vector<Group> groups = {
            Group("TTP-42", GetRandomSubsetOfSubjects(subjects), 20),
            Group("TTP-41", GetRandomSubsetOfSubjects(subjects), 30),
            Group("MI-4", GetRandomSubsetOfSubjects(subjects), 26),
//            Group("TK-4", GetRandomSubsetOfSubjects(subjects), 20),
//            Group("OM-4", GetRandomSubsetOfSubjects(subjects), 20),
    };

    {
        LOG_DURATION("test");
        int cnt = 0;
        for (int i = 0; i < 100; ++i) {
            CSPSolver cspSolver;
            cspSolver.SetVariables(groups, days, LESSONS_PER_DAY);
            cspSolver.SetDomains(rooms);
            auto schedule = cspSolver.Solve().schedule;
            bool found = !schedule.empty();
            cnt += !found;
        }
        cout << "Not found: " << cnt << "\n";
    }
//    return 0;

    CSPSolver cspSolver;
    cspSolver.SetVariables(groups, days, LESSONS_PER_DAY);
    cspSolver.SetDomains(rooms);
    auto schedule = cspSolver.Solve().schedule;

    cout << "=================================\n";

    for (const Day& mainDay : days) {
        cout << "[Day: " << mainDay << "]\n";

        for (auto&[group, schedulePerGroup] : schedule) {
            auto& listOfClasses = schedulePerGroup[mainDay];
            cout << "  Group: " << group.name << "\n";
            for (Class& class_ : listOfClasses) {
                cout << "  " << class_.time.number << ")\n";
                cout << "  room = " << class_.room.number << "\n";
                cout << "  lesson = " << class_.subject.name << "\n";
                cout << "  teacher = " << class_.teacher.name << "\n";
            }
            cout << "  --------------------\n";
        }
        cout << "=================================\n";
    }

    return 0;
}
