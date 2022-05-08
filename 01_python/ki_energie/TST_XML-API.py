import requests
import xml.etree.ElementTree as xml


#Links hier:
# XML-API https://www.homematic-inside.de/software/xml-api
# XML-RPC https://homematic-forum.de/forum/viewtopic.php?f=44&t=4827&hilit=xml+rpc#p29572
#         https://homematic-forum.de/forum/viewtopic.php?f=44&t=11995#p89591     
#         https://homematic-forum.de/forum/viewtopic.php?f=44&t=4827&hilit=xml+rpc#p29572
#         https://www.eq-3.de/Downloads/eq3/download%20bereich/hm_web_ui_doku/HM_XmlRpc_API.pdf


# Beispiel für alle Geräte
#r = requests.get("http://pi001/addons/xmlapi/statelist.cgi?ise_id=12345&new_value=0.20")

# Beispiel für die Temperatur eines Gerätes
#setlocale(LC_NUMERIC, 'French_Canada.1252')
r = requests.get("http://pi001/addons/xmlapi/state.cgi?datapoint_id=4907")
rtn = r.status_code
hdr = r.headers
value = r.text
xmldoc = xml.fromstring(value)

#for child in xmldoc:
#    print (child.tag, child.attrib)
temp = xmldoc.find('./datapoint').attrib['value']
print(temp)
tempval = float(temp.replace(",", "."))
print(tempval)

#print(rtn)
#print(hdr)
#print(value)


r_rooms = requests.get("http://pi001/addons/xmlapi/roomlist.cgi")
rooms = r_rooms.text
#print(rooms)
#print('Ende!')