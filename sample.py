import json


raw_json = [
        {
            "field": "description",
            "type": "xpath",
            "path": "//div[@itemprop='description']/text()",
            "endpoint": "abt.com"
        },
        {
            "field": "title",
            "type": "xpath",
            "path": "//h1[@class='title-2323565163']/text()",
            "endpoint": ""
        },
        {
            "field": "location",
            "type": "xpath",
            "path": "//span[@class='address-3617944557']/text()",
            "endpoint": ""
        },
        {
            "field": "price",
            "type": "xpath",
            "path": "//span[@itemprop='price'][1]/text()",
            "endpoint": ""
        }
    ]

string_json = str(raw_json)

# print(string_json)

# list1 = string_json.strip('][').strip(',').replace('{','').replace(' ','').split('},')

# final_list = []
    
# for ele in list1:
#     # print(ele)
#     # print('------------------')
#     dictionary = dict(subString.split(":") for subString in ele.split(","))
#     final_list.append(dictionary)

# print(final_list)

# f_final_list = []

# for dict1 in final_list:
#     # print(dict1)
#     dict2 = {}
#     for key in dict1:
#         new_key = key.replace("'","")
#         dict2[new_key] = dict1[key]
   
#     # print(dict2)
#     f_final_list.append(dict2)

# # print(f_final_list)

# for dict1 in f_final_list:
#     for key in dict1:
#         # print(dict1[key])
#         if key == 'path':
#             print(dict1[key].replace('"',''))

#         else:
#             print(dict1[key].replace("'",''))

    # print(ele["path"])


# list2="".join(string_json.splitlines())
# list1=list2.replace(" ","").replace('"','')
# print(list1)
# for ele in list1:
#     ele1 = ele.replace('{','').replace('}','')
#     dictionary = dict(subString.split(":") for subString in ele1.split(","))
#     print(dictionary)
#     final_list.append(dictionary)

d = json.loads(string_json)

print(y)