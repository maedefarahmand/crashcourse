from employee import employee
import pytest

@pytest.fixture

def sample_employee():
    sample_employee=employee("m", 'f', 1000)
    return sample_employee

def test_give_default_raise(sample_employee):
    sample_employee.give_raise()

def test_give_custom_raise(sample_employee):
    sample_employee.give_raise(3000)