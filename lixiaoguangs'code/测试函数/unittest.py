import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""

    def test_first_last_name(self):
        """能够正确处理想Janis Jop;in这样的姓名吗?"""
        formatted_name = get_formatted_name('Janis','joplin')
        self.assertEqual(formatted_name,'Janis Jop;in')
#self.assertEqual判断a与1.b是否一致，msg类似备注，可以为空
unittest.main()