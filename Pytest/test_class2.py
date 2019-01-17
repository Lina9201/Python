import pytest

class TestClass2:
    x = "hello"

    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        tc = TestClass2()
        assert hasattr(tc, 'x')

    def test_three(self):
        a = "hello"
        b = "hello world"
        assert a in b


if __name__ == '__main__':
    pytest.main(['-q', 'test_class2.py'])
