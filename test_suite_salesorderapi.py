import unittest
from GetSalesOrder import TestGetSalesOrder
from getdatafromxml import TestMatchSalesOrder
import TestOpenWebsite

tc1 = unittest.TestLoader().loadTestsFromTestCase(TestGetSalesOrder)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestMatchSalesOrder)
tc3 = unittest.TestLoader().loadTestsFromTestCase(TestOpenWebsite)

regression_test = unittest.TestSuite([tc1, tc2, tc3])

unittest.TextTestRunner(verbosity=2).run(regression_test)
