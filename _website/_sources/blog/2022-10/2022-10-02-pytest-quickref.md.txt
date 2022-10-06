---
blogpost: true
date: Oct 2, 2022
tags: pytest
category: Python
author: TIAN Zeyu
---

# pytest quick reference

simple code reference for pytest unittesting

```shell
poetry add pytest --group dev 
poetry add pytest-mock --group dev 
```
## Mocking and Typing for mocking
```python
import pytest  
from pytest_mock import MockFixture # this provides typehints to mocker objects

@pytest.fixture 
def obj() -> "some object":
    # do something 
    return 

def test_something(mocker:MockFixture, obj):
    # mock patch object
    method_name = "some_method"
    method_content = lambda x: print("some function")
    mock_obj = mocker.patch.object(obj,method_name,new=method_content)

    # mock open
    mocked_result = mocker.mock_open(read_data="{}")
    mocker.patch("src.quantcerebro.utils.open", new=mocked_result)

    # mock patch 
    import sys 
    mocker.patch("src.quantcerebro.utils.import_module", return_value=sys.modules[__name__])
```

## test on exception
```python
with pytest.raises(NotImplementedError, match="some keyword string from Error using regex"):
    some_func()
```

## using a fixture within a class

```python

@pytest.fixture
def fixtureA():
    return "A"

class TestSomething:
    @pytest.fixture(autouse=True)
    def setup(self, fixtureA):
        self.fixtureA = fixtureA
        
    def testA(self):
        assert self.fixtureA == "A", "something wrong"
```