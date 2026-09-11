"""Cart totalling — the public entry point."""

from .pricing import apply_surcharge


def total(items):
    """Return the total price of the items in the cart."""
    running = 0
    for item in items:
        running += item
    return apply_surcharge(running)
