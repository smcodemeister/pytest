import pytest
import api_call_1

def test_count_pass():
    assert api_call_1.getCount() > 0
    
def test_count_fail():
    assert api_call_1.getCount() == 0    