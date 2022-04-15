from cgitb import reset
from unittest import expectedFailure, result
from Module import Person, Wizard, HealthPotion
import numpy as np

def test_Person_getHp():
    person1 = Person("getHp")
    expected_result = 100
    result = person1.get_life_points()
    assert result == expected_result

def test_Person_isDead_alive():
    person1 = Person("Alive")
    expected_result = False
    result = person1.is_dead()
    assert result == expected_result

def test_Person_hit():
    person1 = Person("Hit")
    person2 = Person("Receive")
    person1.hit(person2)
    expected_result = 90
    result = person1.get_life_points()
    assert result == expected_result

def test_Person_isDead_dead():
    person1 = Person("Dead")
    person2 = Person("Hit")
    for i in range(10):
        person2.hit(person1)

def test_Person_gained_life_points():
    person1 = Person("Gained")
    person1.gained_life_points(10)
    expected_result = 110
    result = person1.get_life_points()
    assert result == expected_result