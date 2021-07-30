import GetSalesOrder
import unittest


class TestMatchSalesOrder(unittest.TestCase):

    def test_b(self):

        open_xml = open("./salesorderapi/SB S21 Sales XML2021062313 24 17.xml", "r")
        so = GetSalesOrder.TestGetSalesOrder.test_readdata(self)
        flag = 0
        index = 0

        for line in open_xml:
            index += 1

            if so in line:

                flag = 1
                break

        if flag == 0:
            print("Sales order not found")
        else:
            return so
        open_xml.close()


if __name__ == "__main__":
    unittest.main(verbosity=1)
