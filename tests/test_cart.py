from cart import total


def test_total_sums_the_items():
    assert total([1, 2, 3]) == 6


def test_total_of_empty_cart_is_zero():
    assert total([]) == 0
