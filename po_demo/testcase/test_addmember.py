from time import sleep

import pytest
from po_demo.page.mainpage import MainPage


class TestMember:
    def setup_class(self):
        self.main = MainPage()

    def teardown_class(self):
        self.main.exit()

    @pytest.mark.parametrize("username,acctid,phone", [("han13", "1212013", "13212120013")])
    def test_addmember_success(self, username, acctid, phone):

        main =self.main.login().title_book()
        # 添加前数据
        old_eles = main.get_member_list()
        new_eles = main.add_member_button().add_member(username, acctid, phone).get_member_list()

        assert len(old_eles) + 1 == len(new_eles)



if __name__ == '__main__':
    pytest.main()