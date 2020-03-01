# from poium import Page,PageElement

class LocateElement():
    def __init__(self,driver,timeout=4,log=False):
        self.driver=driver
        self.timeout=timeout
        self.log=log

    def by_id(self,id):
        return self.driver.find_element_by_id(id)

    def by_name(self,name):
        return self.driver.find_element_by_name(name)

    def by_class_name(self,classname):
        return self.driver.find_element_by_class_name(classname)

    def by_tag_name(self,tag_name):
        return self.driver.find_element_by_tag_name(tag_name)

    def by_link_text(self,link_text):
        return self.driver.find_element_by_link_text(link_text)

    def by_partial_link_text(self,partial_link_text):
        return self.driver.find_element_by_partial_link_text(partial_link_text)

    def by_css(self,css):
        return self.driver.find_element_by_css_selector(css)

    def by_xpath(self,xpath):
        return self.driver.find_element_by_xpath(xpath)


    #poium locate
    # def by_id(self,id,timeout=None,log=None):
    #     if timeout:
    #         time=timeout
    #     else:
    #         time=self.timeout
    #     return PageElement(id_=id,timeout=time,log=log)
    #
    # def by_name(self,name,timeout=None,log=None):
    #     if timeout:
    #         time=timeout
    #     else:
    #         time=self.timeout
    #     return PageElement(name=name,timeout=time,log=log)
    #
    # def by_class_name(self,classname,timeout=None,log=None):
    #     if timeout:
    #         time=timeout
    #     else:
    #         time=self.timeout
    #     return PageElement(class_name=classname,timeout=time,log=log)
    #
    # def by_tag_name(self,tag_name,timeout=None,log=None):
    #     if timeout:
    #         time=timeout
    #     else:
    #         time=self.timeout
    #     return PageElement(tag=tag_name,timeout=time,log=log)
    #
    # def by_link_text(self,link_text,timeout=None,log=None):
    #     if timeout:
    #         time=timeout
    #     else:
    #         time=self.timeout
    #     return PageElement(link_text=link_text,timeout=time,log=log)
    #
    # def by_partial_link_text(self,partial_link_text,timeout=None,log=None):
    #     if timeout:
    #         time=timeout
    #     else:
    #         time=self.timeout
    #     return PageElement(partial_link_text=partial_link_text,timeout=time,log=log)
    #
    # def by_css(self,css,timeout=None,log=None):
    #     if timeout:
    #         time=timeout
    #     else:
    #         time=self.timeout
    #     return PageElement(css=css,timeout=time,log=log)
    #
    # def by_xpath(self,xpath,timeout=None,log=None):
    #     if timeout:
    #         time=timeout
    #     else:
    #         time=self.timeout
    #     return PageElement(xpath=xpath,timeout=time,log=log)

