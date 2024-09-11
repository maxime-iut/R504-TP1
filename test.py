import pytest
import fonctions as f


def test_1():
    assert f.puissance(2, 3) == 8
    assert f.puissance(2, 2) == 4


def test_2():
    assert f.puissance(-1, -5) == -1
    assert f.puissance(23, -3) == 8.218952905399852e-05


def test_3():
    with pytest.raises(TypeError):
        f.puissance("a", 1)
    with pytest.raises(TypeError):
        f.puissance("a", "b")
