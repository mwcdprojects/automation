import unittest
from apitest.apihelper import Apihelper
import logging

x = Apihelper()
class Testing(unittest.TestCase):
    log = logging.getLogger()  # root logger
    log.setLevel(logging.INFO)
    format_str = '%(asctime)s - %(levelname)-8s - %(message)s'

    def test_list_nonempty(self):
        ct = x.get_results()
        assert len(ct)!=0 , "The returned list is empty"
        if len(ct)== 0:
            print "The returned list is empty"
        else:
            logging.info("The returned list is not empty and its contents are: {}".format(ct))

if __name__ == '__main__':
    unittest.main()
