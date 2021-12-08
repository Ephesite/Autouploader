import lxml.etree
import secrets
import random
from xml.dom import minidom
from xml.etree import ElementTree as etree

file = 'Baseplate.rbxlx'

doc = lxml.etree.parse(file)
def uniqueId():
    for el in doc.xpath("//UniqueId[@name='UniqueId']"):
        el.text = f'{secrets.token_hex(17)}'
    doc.write (file)
def referentt():
    for el in doc.xpath("//Item[@referent]"):
        string = ''.join(random.choice('0123456789ABCDEF') for i in range(33))
        el.attrib['referent'] = f'RBX{string}'
    doc.write (file)


