from tasks import Task

import pytest
import tasks

# def test_assert01():
#     a = Task('t', 'm')
#     b = Task('s', 'w')
#
#     assert a == b

def test_assert02():
    with pytest.raises(TypeError):
        tasks.add(task="string")
