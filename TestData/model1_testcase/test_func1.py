import pytest




class TestFunc1:

    # def setup_class(self):
    #     print("\n初始化")
    #
    # def setup(self):
    #     print("\n执行前置条件")

    @pytest.mark.run(order=1)
    def test_01(self,my_fix):
        print("test-model1_func1-1")

    @pytest.mark.run(order=2)
    def test_02(self):
        print("test-model1_func1-2")
        # assert expect == result
    # def teardown(self):
    #     print("\n清除数据")