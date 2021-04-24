import os
import json

with open('input1.json') as file:
    data = json.load(file)


order_details = data['OrderDetails']

number_invoice = order_details['Order_Number__c']
date_invoice = order_details['LastModifiedDate']
date_invoice = date_invoice.split('T')[0]

date_order = order_details['ActivatedDate']
name_order = order_details['Name']
total_amount = order_details['TotalAmount']

l1_bill = order_details['Account']['Name']
l2_bill = order_details['BillingStreet']
l3_bill = order_details['BillingCity']+ ', '+ order_details['BillingState']+ ' '
l3_bill += order_details['BillingPostalCode']

order_items_list = data['OrderItems']

test_list = []
for item in order_items_list:
    test_list.append(item.get('Search_Name__c')) 

print(test_list)
test_string = test_list[1]
print(test_string)


# print(date_invoice.split('T')[0])
# print(date_order.split('T')[0])

# for item in order_items_list:
#     print('*'*50)
#     print('Name:  ', item['PricebookEntry']['Name'])
#     print('Description:  ', item['Description'])
#     print('Unit Price:  ', item['UnitPrice'])
#     print('Quantity:  ', item['Quantity'])
#     print('Total Price:  ', item['TotalPrice'])
#     print('*'*50)

# #print(l3_bill)
# for i in os.listdir(os.getcwd()):
#     if i.split('.')[1] == 'json':
#         print(i)