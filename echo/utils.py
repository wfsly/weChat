from xml.etree import ElementTree as ET

#parse message of weChat into dict{}
def parse_xml(data):
    result = {}

    if type(data) == unicode:
        data = data.encode('utf-8')
    elif type(data) == str:
        pass
    else:
        raise "parse error"
        
    xml = ET.fromstring(data)
    for child in xml:
        result[child.tag] = child.text

    return result

def generate_response(data):
    xml = ["<xml>"]
    for key in data:
        xml.append("<{0}>{1}</{0}>\n".format(key.encode("utf-8"), data[key].encode("utf-8")))

    xml.append("</xml>")
    return "".join(xml)

def exchange_src_des(data):
    data['FromUserName'], data['ToUserName'] = data['ToUserName'], data['FromUserName']
