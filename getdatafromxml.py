import opensite.GetSalesOrder


class Match_sales_order():

    def b_test(self):

        open_xml = open("C:\\Users\\dcthofic07\\Documents\\D365Test\\SB S21 Sales XML2021062313 24 17.xml", "r")
        so = opensite.GetSalesOrder.read_data()
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


test2 = Match_sales_order()
test2.b_test()