import pytest

from app_core.deque import Deque, DequeEmptyError


def test_deque_add_remove_front_rear_order() -> None:
    d = Deque()
    assert d.is_empty() is True
    assert d.size() == 0
    d.add_rear(1)
    d.add_rear(2)
    d.add_front(0)
    assert list(d) == [0, 1, 2]
    assert d.remove_front() == 0
    assert d.remove_rear() == 2
    assert d.remove_front() == 1
    assert d.is_empty() is True


def test_deque_remove_front_empty_raises() -> None:
    d = Deque()
    with pytest.raises(DequeEmptyError):
        d.remove_front()


def test_deque_remove_rear_empty_raises() -> None:
    d = Deque()
    with pytest.raises(DequeEmptyError):
        d.remove_rear()


def test_deque_clear() -> None:
    d = Deque()
    d.add_rear("a")
    d.clear()
    assert d.is_empty() is True
    assert d.size() == 0
