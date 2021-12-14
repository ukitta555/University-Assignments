/*
 * Students.hpp
 *
 *  Created on: Feb 18, 2020
 *      Author: vlad
 */

#ifndef STUDENTS_HPP_
#define STUDENTS_HPP_

#include <string>


struct Student
{
	std::string name;
	unsigned int ticketNumber;
	int disciplines [71];
	void fillArray()
	{
		for (int i = 0; i < 71; i++)
		{
			disciplines[i] = -1;
		}
	}
	bool checkGrade (int grade)
	{
		if (grade < 0 || grade > 100) return false;
		return true;
	}
};

typedef Student* PStudent;

class Group
{
private:
	std::string groupName;
	int N; // number of students
public:
	PStudent* ppStudent = new PStudent[36];
	Group();
	Group(std::string groupName);
	Group (const Group& groupOld);
	void setGrade (int studentNumber, int discipline, int grade);
	void addStudent (Student newStudent);
	void writeBadStudents (double percentage);
}



#endif /* STUDENTS_HPP_ */
