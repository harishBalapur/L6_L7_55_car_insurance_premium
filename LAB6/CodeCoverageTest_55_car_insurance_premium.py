
import pytest

from car_insurance_premium import (
    annual_premium,
    no_claim_bonus,
    claim_payout
)


# 1. ANNUAL PREMIUM TEST CASES

def test_invalid_car_type():
    with pytest.raises(ValueError):
        annual_premium("truck", 30, 0, False)


def test_driver_below_18():
    with pytest.raises(ValueError):
        annual_premium("sedan", 17, 0, False)


def test_young_driver():
    assert annual_premium("hatchback", 20, 1, True) == 11500


def test_senior_driver_with_many_claims():
    assert annual_premium("sedan", 60, 3, False) == 28000


def test_middle_aged_driver_with_claims():
    assert annual_premium("suv", 40, 1, False) == 15000


def test_anti_theft_discount():
    assert annual_premium("suv", 40, 1, True) == 14500


# 2. NO CLAIM BONUS TEST CASES

def test_invalid_claim_free_years():
    with pytest.raises(ValueError):
        no_claim_bonus(-1)


@pytest.mark.parametrize("years, expected", [
    (0, 0),
    (1, 20),
    (2, 20),
    (3, 35),
    (4, 35),
    (5, 50),
    (10, 50)
])
def test_no_claim_bonus_categories(years, expected):
    assert no_claim_bonus(years) == expected


# 3. CLAIM PAYOUT TEST CASES

def test_negative_damage_cost():
    with pytest.raises(ValueError):
        claim_payout(-100, 50000, 1000, False)


def test_negative_deductible():
    with pytest.raises(ValueError):
        claim_payout(5000, 50000, -100, False)


def test_total_loss():
    assert claim_payout(50000, 40000, 1000, True) == 40000


def test_damage_less_than_deductible():
    assert claim_payout(500, 50000, 1000, False) == 0


def test_damage_equal_to_deductible():
    assert claim_payout(1000, 50000, 1000, False) == 0


def test_payout_exceeds_insured_value():
    assert claim_payout(60000, 40000, 1000, False) == 40000


def test_normal_claim_payout():
    assert claim_payout(10000, 50000, 1000, False) == 9000

