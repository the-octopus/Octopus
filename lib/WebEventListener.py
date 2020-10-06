#!/usr/bin/env python3
import time
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
from lib.reporter import Reporter


class WebEventListener(AbstractEventListener):

    def before_click(self, element, driver):
        strElement = get_element_string(element)
        Reporter.info("Clicked   On Element  ***<<((   %s   ))>>***" % strElement)

    # def after_click(self, element, driver):
    #     strElement = get_element_string(element)
    #     Reporter.info("Clicked   On Element  ***<<((  %s  ))>>***" % strElement)

    def after_change_value_of(self, element, driver):
        strElement = get_element_string(element)
        Reporter.info("Sent Data To Element  ***<<((   %s   ))>>***" % strElement)






def get_element_string(element):
        elementid = element.get_attribute("id")
        elementName = element.get_attribute("name")
        elementClass = element.get_attribute("class")
        elementType = element.get_attribute("type")
        elementTag = element.tag_name
        if(elementid is not None and len(elementid) > 0):
            return "ID: "+elementid
        elif (elementName is not None and len(elementName) > 0):
            return "Name: "+elementName
        elif (elementClass is not None and len(elementClass) > 0):
            return "Class: "+elementClass
        elif (elementType is not None and len(elementType) > 0):
            return "Type: "+elementType
        elif (elementTag is not None and len(elementTag) > 0):
            return "Tag: "+elementTag
        else:
            return "-"