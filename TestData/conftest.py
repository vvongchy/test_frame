import pytest


@pytest.fixture(scope="function",autouse=False,params=["p1","p2"])
def my_fix(request):
    print("执行前置"+request.param)