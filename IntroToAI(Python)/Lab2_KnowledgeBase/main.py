from typing import Callable

from person import Person


john = Person(name="John")
kate = Person(name="Kate")
lia = Person(name="Lia")
jake = Person(name="Jake")
chris = Person(name="Chris")

people = [john, kate, lia, jake, chris]
"""
Base predicates:

teacher_angry_at(person)
lives_near_university(person)
is_smart(person)
goes_to_parties(person)
attends_lectures(person)
studies_a_lot(person)

Producing new rules (R):
1. X lives near university -> X visits lectures
2. X is smart AND teacher is not mad at X -> X passes the exam
3. X is visits lectures AND X studies a lot -> X passes the exam
4. X does not go to parties -> X studies a lot
5. (X is not smart OR Teacher mad at X) AND (X doesn't attend lectures OR X doesn't study a lot) -> X fails exam
"""

# Procedures (P)
# Use command pattern: try to find existing fact in DB;
# if can't find one, pass the responsibility down the tree
def teacher_angry(p: Person):
    teacher_angry_fact = fact_dictionary.get(teacher_angry).get(p)
    if teacher_angry_fact is True:
        return True
    elif teacher_angry_fact is False:
        return False
    else:
        return None

def lives_near_university(p: Person):
    lives_near_university_fact = fact_dictionary.get(lives_near_university).get(p)
    if lives_near_university_fact is True:
        return True
    elif lives_near_university_fact is False:
        return False
    else:
        return None

def is_smart(p: Person):
    is_smart_fact = fact_dictionary.get(is_smart).get(p)
    if is_smart_fact is True:
        return True
    elif is_smart_fact is False:
        return False
    else:
        return None

def goes_to_parties(p: Person):
    goes_to_parties_fact = fact_dictionary.get(goes_to_parties).get(p)
    if goes_to_parties_fact is True:
        return True
    elif goes_to_parties_fact is False:
        return False
    else:
        return None

def attends_lectures(p: Person):
    visits_lectures_fact = fact_dictionary.get(attends_lectures).get(p)
    if visits_lectures_fact is True:
        return True
    elif visits_lectures_fact is False:
        return False
    else:
        lives_near_university_fact = fact_dictionary.get(lives_near_university).get(p)
        if lives_near_university_fact is True:
            return True
        elif lives_near_university_fact is False:
            return False
        elif lives_near_university_fact is None:
            result = lives_near_university(p)
            if result:
                return True
        return None

def studies_a_lot(p: Person):
    studies_a_lot_fact = fact_dictionary.get(studies_a_lot).get(p)
    if studies_a_lot_fact is True:
        return True
    elif studies_a_lot_fact is False:
        return False
    else:
        does_party_fact = fact_dictionary.get(goes_to_parties).get(p)
        if does_party_fact is False:
            return True
        else:
            return None


def will_pass_exam(p: Person):
    is_person_smart = is_smart(p)
    is_teacher_angry_at_person = teacher_angry(p)
    person_visits_lectures = attends_lectures(p)
    does_person_study_a_lot = studies_a_lot(p)
    if (is_person_smart is True and is_teacher_angry_at_person is False)\
            or (person_visits_lectures is True and does_person_study_a_lot is True):
        return True
    elif (is_person_smart is False or is_teacher_angry_at_person is True)\
            and (person_visits_lectures is False or does_person_study_a_lot is False):
        return False
    else:
        return None

"""
FACTS (F):

John - smart
Kate - does not go to parties; visits lectures
Lia - visits lectures
Jake - studies a lot; smart; does not go to lectures
Chris - lives near university; studies a lot
"""

fact_dictionary: dict[Callable, dict[Person, bool]] = {
    is_smart: {
        john: True,
        jake: True
    },
    goes_to_parties: {
        kate: False
    },
    attends_lectures: {
        kate: True,
        lia: True,
        jake: False
    },
    studies_a_lot: {
        chris: True,
        jake: True
    },
    lives_near_university: {
        chris: True
    },
    teacher_angry: {}
}

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for person in people:
        print(f'Is teacher angry at {person.name} right now?')
        x = input()
        if x == "yes":
            fact_dictionary[teacher_angry][person] = True
        elif x == "no":
            fact_dictionary[teacher_angry][person] = False

        will_pass = will_pass_exam(person)
        if will_pass is True:
            print(f"Will {person.name} pass the exam: yes!")
        elif will_pass is False:
            print(f"Will {person.name} pass the exam: no!")
        else:
            print(f"Will {person.name} pass the exam: not enough information...")