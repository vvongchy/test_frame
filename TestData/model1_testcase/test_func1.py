import pytest


class TestFunc1:
    @pytest.mark.run(order=2)
    def test_01(self):
        print("test-model1_func1-1")

    @pytest.mark.run(order=1)
    def test_02(self):
        print("test-model1_func1-2")