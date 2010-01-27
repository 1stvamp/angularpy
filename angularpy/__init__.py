# coding: utf-8

"""angularpy is a python data structure for parsing and working with XML,
based on PHP5's SimpleXML.
"""
__author__ = 'Wesley Mason<wes [at] 1stvamp [dot] org'
__docformat__ = 'restructuredtext en'
__version__ = '1.0b1'

import sys
from lxml import etree

if not hasattr(sys, "hexversion") or sys.hexversion < 0x020700f0:
    from ordereddict import OrderedDict
else:
    from collections import OrderedDict

# TODO: override __iter__(), __reversed__(), keys(), values(), get() and has_key()

class SimpleXML(OrderedDict):
    doc = None
    attrs = []
    selector = []
    __data_dict = {}

    def _get_data_dict(self):
        return self.__data_dict
    def _set_data_dict(self, data_dict):
        self.__data_dict = data_dict
    data_dict = property(_get_data_dict, _set_data_dict)

    def __init__(self, doc=None, attrs=None, data_dict=None, selector=None):
        if doc:
            self.doc = doc
            if attrs:
                self.attrs = attrs
            # Grab data_dict here
        if not self.data_dict and data_dict:
            self.data_dict = data_dict
        if selector:
            self.selector = selector

    @classmethod
    def parse(cls, location):
        return super(SimpleXML, cls).__init__(doc=etree.parse(location))

    @classmethod
    def from_string(cls, string):
        return super(SimpleXML, cls).__init__(doc=etree.fromstring(string))

    @classmethod
    def from_simple(cls, simple_xml_instance):
        return super(SimpleXML, cls).__init__(
                    doc=simple_xml_instance.doc,
                    attrs=simple_xml_instance.attrs,
                    data_dict=simple_xml_instance.data_dict
                )

    @classmethod
    def from_dict(cls, data_dict):
        return super(SimpleXML, cls).__init__(
                    data_dict=data_dict
                )

    @property
    def value(self):
        return


