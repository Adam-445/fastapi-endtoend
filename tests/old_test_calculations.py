import pytest

from app.calculations import add, BankAccount

@pytest.fixture
def zero_bank_account():
    return BankAccount()

@pytest.fixture
def bank_account():
    return BankAccount(50)

@pytest.mark.parametrize(
    "num1, num2, result", [(1, 1, 2), (2, 2, 4), (0, 0, 0), (-1, 1, 0)]
)
def test_add(num1, num2, result):
    assert add(num1, num2) == result


def test_bank_set_initial_amount(zero_bank_account):
    assert zero_bank_account.balance == 0

def test_bank_default_amount(bank_account):
    assert bank_account.balance == 50
