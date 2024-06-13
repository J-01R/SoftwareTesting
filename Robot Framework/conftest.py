#Jonatan Rassekhnia
#2023.04.23
#DVB17
#Karlstad University
#Lab - 5 Testing Execution & Reporting

import pytest
import conftest
import math



#   Test case 1
def test_circumference():
    output = conftest.circumference_of_circle(2 / math.pi)

    assert output == 4


def test_area():
    output = conftest.area_of_circle(2 / math.sqrt(math.pi))

    assert output == 4


#   Test case 2
def test_circumference():
    output = conftest.circumference_of_circle(2 / math.sqrt(math.pi))

    assert output == 7


def test_area():
    output = conftest.area_of_circle(2 / math.pi)

    assert output == 1


#   Test case 3
def test_circumference():
    output = conftest.circumference_of_circle(1)

    assert output == 2 * math.pi


def test_area():
    output = conftest.area_of_circle(1)

    assert output == math.pi


#   Test case 4
def test_circumference():
    output = conftest.circumference_of_circle(2 / math.pi)

    assert round(output) == 4


def test_area():
    output = conftest.area_of_circle(2 / math.sqrt(math.pi))

    assert round(output) == 4
