from lxml import etree
import json
from pprint import pprint

def get_html(json_data):
    entries = json_data['log']['entries']
    for i in range(0, len(entries)):
        if "text/html" in entries[i]['response']['content']['mimeType']:
            try:
                html =  entries[i]['response']['content']['text']
                print(i)
                # with open("test.html", 'w') as fp:
                #     fp.write()
                return html
            except:
                pass


def parser():

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

    parse_response = {}

    f = open("har-files/kijiji-2020-ford-f150-xlt.har")

    data = json.load(f)

    html = get_html(data)
    # html = clean_data(html)
    tree = etree.HTML(html)

    for entry in range(len(raw_json)):

        # print("entry: ",entry)

        # print(raw_json[entry].get("path"))

        val = tree.xpath(raw_json[entry]["path"])

        parse_response[raw_json[entry]["field"]] = val

    
    for response in parse_response.values():
        while(' ' in response):
            response.remove(' ')
        



    # print(xpaths)
    # for xpath in xpaths:
    #     # print(xpath)
    #     # txt = tree.xpath('//*[@id="question-header"]/h1/a/text()')
    #     txt = tree.xpath(xpath)
    #     text_list.append(txt)
        # txt=tree.xpath("//div[@itemprop='description']/text()")
    # print(text_list)
    pprint(parse_response)
    # return text_list, field


if __name__ == "__main__":
    parser()