class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()

    instances = [Person(person["name"],
                 person["age"]) for person in people]

    for person in people:
        instances = Person.people[person["name"]]

        wife_name = person.get("wife")
        if wife_name:
            instances.wife = Person.people[wife_name]

        husband_name = person.get("husband")
        if husband_name:
            instances.husband = Person.people[husband_name]

    return [Person.people[person_dict["name"]] for person_dict in people]
