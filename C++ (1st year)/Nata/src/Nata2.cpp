
#include <iostream>
#include <algorithm>
#include <map>
#include <vector>

using namespace std;

class Person {
public:
/*
    Person (const string& FirstName, const string& LastName, int year){
        firstName[year] = FirstName;
        lastName[year] = LastName;
    }
    */
    void ChangeFirstName(int year, const string& first_name) {
        firstName[year] = first_name;
    }
    void ChangeLastName(int year, const string& last_name) {
        lastName[year] = last_name;
    }
    string GetFullName(int year) {
        string help1, help2, result;
        if ( firstName.count(year) != 0 ) help1 = firstName[year];
        else {
            help1 = check(year, firstName);
        }
        if ( lastName.count(year) != 0 ) help2 = lastName[year];
        else {
            help2 = check(year, lastName);
        }
        if (help1 == "-" && help2 == "-") result = "Incognito";
        if (help1 != "-" && help2 == "-") result = help1 + " with unknown last name";
        if (help1 == "-" && help2 != "-") result = help2 + " with unknown first name";
        if (help1 != "-" && help2 != "-") result = help1 + " " + help2;
        return result;
    }

    string GetFullNameWithHistory(int year)  {
        vector<string> help1 = check2(year, firstName);
        vector<string> help2 = check2(year, lastName);
        string result1, result2 = "";

        if (help1[0] == "e" && help2[0] == "e") result1 = "Incognito";
        if (help1[0] != "e" && help2[0] == "e") {
            result2 = " with unknown last name";
            Reverse(help1);
            if (help1.size() > 1) {
                result1 = help1[0] + " (";
                for (size_t i = 1; i < help1.size() - 1 ; ++i) {
                    result1 += help1[i] + ", ";
                }
                result1 += help1[help1.size() - 1] + ")" + result2;
            }
            else result1 = help1[0] + result2;
        }

        if (help1[0] == "e" && help2[0] != "e") {
            result2 = " with unknown first name";
            Reverse(help2);
            if (help2.size() > 1) {
                result1 = help2[0] + " (";
                for (size_t i = 1; i < help2.size() - 1; ++i) {
                    result1 += help2[i] + ", ";
                }
                result1 += help2[help2.size() - 1] + ")" + result2;
            }
            else result1 = help2[0]  + result2;

        }

        if (help1[0] != "e" && help2[0] != "e") {
            Reverse(help1);
            Reverse(help2);
            if (help1.size() > 1) {
                result1 = help1[0] + " (";
                for (size_t i = 1; i < help1.size() - 1 ; ++i) {
                    result1 += help1[i] + ", ";
                }
                result1 += help1[help1.size() - 1] + ")";
            }
            else result1 = help1[0];
            if (help2.size() > 1) {
                result2 = help2[0] + " (";
                for (size_t i = 1; i < help2.size() - 1; ++i) {
                    result2 += help2[i] + ", ";
                }
                result2 += help2[help2.size() - 1] + ")";
            }
            else result2 = help2[0];
            result1 += " " + result2;
        }
        return result1;
    }

private:
    map<int, string> firstName;
    map<int, string> lastName;
    string check (const int& year, const map<int, string>& m) {
        bool y = 1;
        string help;
        for (auto& item : m) {
            if (item.first < year) {
                help = item.second;
                y = 0;
            }
        }
        if (y) help = "-";
        return help;
    }
     bool f (string s, vector<string> v){
        if (v.size() == 0) return 1;
        if (v.back() != s) return 1;
        return 0;
    }


     vector<string> check2 (int year, const map<int, string>& m){
         vector<string> words;
         bool y = 1;
         bool x = 1;
         for (const auto& item : m){
             y = f(item.second, words);
             if (item.first <= year) {
                 if (y)  words.push_back(item.second);
                 x = 0;
             }
         }
         if (x == 1) {
             words.clear();
             words.push_back("e");
         }
         return words;
     }

     void Reverse(vector<string>& v) {
         int n = v.size();
         for (int i = 0; i < n / 2; ++i) {
             string tmp = v[i];
             v[i] = v[n - 1 - i];
             v[n - 1 - i] = tmp;
         }
     }
 };


/*
int main() {
  Person person;

  person.ChangeFirstName(1965, "Polina");
  person.ChangeFirstName(1965, "Appolinaria");

  person.ChangeLastName(1965, "Sergeeva");
  person.ChangeLastName(1965, "Volkova");
  person.ChangeLastName(1965, "Volkova-Sergeeva");

  for (int year : {1964, 1965, 1966}) {
    cout << person.GetFullNameWithHistory(year) << endl;
  }

  return 0;
}
*/
