import sys

import pytest


def setup_module():
    print("这是setup_model")


class TestDemo1:
    def setup_class(self):
        print("这是TestDemo1,class_setup")

    def teardown_class(self):
        print("这是TestDemo1,class_teardown")

    def setup(self):
        print("这是fun_setup")

    def teardown(self):
        print("这是fun_teardown")

    @pytest.mark.parametrize("username,password",[('zhang',"1234qwer"),('li',"5677qwer")],ids=["正确用户名和密码","错误的用户名和密码"])
    def test_demo1(self,username,password):
        print("test_demo1")
        print(username,password)

    @pytest.mark.parametrize("a",[1,2,3])
    @pytest.mark.parametrize("b",["q","w","e","r"])
    def test_demo2(self,a,b):
        print("test_demo2")
        print(f"{a}{b}")


class TestDemo2:
    def setup_class(self):
        print("这是TestDemo2,class_setup")

    def teardown_class(self):
        print("这是TestDemo2,class_teardown")

    def setup(self):
        print("这是fun_setup")

    def teardown(self):
        print("这是fun_teardown")

    def test_demo1(self):
        print("test_demo1")

    def test_demo2(self):
        print("test_demo2")


if __name__ == '__main__':
    pytest.main(['test_231113001.py','-vs'])