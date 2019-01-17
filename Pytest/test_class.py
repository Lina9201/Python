import pytest

class TestClass:
    x = "hello"

    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        tc = TestClass()
        assert hasattr(tc, 'x')

    def test_three(self):
        a = "hello"
        b = "hello world"
        assert a in b


if __name__ == '__main__':
    pytest.main(['–collect-only', 'test_class.py'])
