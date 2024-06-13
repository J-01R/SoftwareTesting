#Jonatan Rassekhnia
#2023.04.23
#Lab 5
#Test Execution and Reporting
#Karlstad University

import conftest

import math

#   TestCase 1

def test_circumference():
    output = conftest.circumference_of_circle(2 / math.pi)

    assert output == 4

def test_area():
    output = conftest.area_of_circle(2 / math.sqrt(math.pi))

    assert output == 4

#   TestCase 2

def test_circumference():
    output = conftest.circumference_of_circle(2 / math.sqrt(math.pi))

    assert output == 7

def test_area():
    output = conftest.area_of_circle(2 / math.pi)

    assert output == 1

#   TestCase 3

def test_circumference():
    output = conftest.circumference_of_circle(1)

    assert output == 2 * math.pi

def test_area():
    output = conftest.area_of_circle(1)

    assert output == math.pi

#   TestCase 4

def test_circumference():
    output = conftest.circumference_of_circle(2 / math.pi)

    assert round(output) == 4

def test_area():
    output = conftest.area_of_circle(2 / math.sqrt(math.pi))

    assert round(output) == 4
