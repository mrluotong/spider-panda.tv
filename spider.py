import re
from urllib import request

class Spider():
    url = 'https://www.panda.tv/cate/lol?pdt=1.24.s1.3.30llv0ncajs'
    root_pattern = '<div class="video-info">([\s\S]*?)</div>'
    name_pattern = '</i>([\s\S]*?)</span>'
    number_pattern = '<span class="video-number"><i class="ricon ricon-eye"></i>([\s\S]*?)</span>'
    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()
        htmls = str(htmls,encoding='utf-8')
        return htmls
    def __analysis(self,htmls):
        root_htmls = re.findall(Spider.root_pattern,htmls)
        anchors=[]
        for html in root_htmls:
            name = re.findall(Spider.name_pattern,html)
            number = re.findall(Spider.number_pattern,html)
            anchor = {"name":name,"number":number}
            anchors.append(anchor)
        return anchors
    def __refine(self,anchors):
        pass
    def go(self):
        htmls = self.__fetch_content()
        anchors = self.__analysis(htmls)
        self.__refine(anchors)
spider = Spider()
spider.go()

