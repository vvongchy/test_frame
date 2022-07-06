import pytest


class TestFunc2:
    age =18
    # @pytest.mark.model1
    @pytest.mark.skip( reason= "test case")
    def test_01(self):
        print("test-model1_func2-1")
    @pytest.mark.skipif(age>=18,reason="age>18")
    def test_02(self):
        print("test-model1_func2-2")