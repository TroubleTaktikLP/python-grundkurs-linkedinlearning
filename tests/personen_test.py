from aufgaben_package.personen import Person

def test_str():
    peter = Person("peter", 48)
    assert str(peter) == "peter (48)"
