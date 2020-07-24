import requests
import re


class BilibiliDanmuSpider(object):
    # 构造要爬取的url
    def __init__(self, BV):
        # 想要爬取弹幕视频的url
        self.video_url = "https://www.bilibili.com/video/" + BV
        # 请求头
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"}

    # 弹幕在返回的网页数据中，获取弹幕url
    def get_danmu_url(self):
        # 先请求网页
        response = requests.get(url = self.video_url, headers = self.headers)
        # 返回内容解码
        page = response.content.decode()
        # oid获取
        page = page.split('"backup_url"')[5]
        page = str(page)
        oid = page.split("/")[6]
        # 弹幕地址：https://api.bilibili.com/x/v1/dm/list.so?oid=203472310
        # 拼接弹幕url
        danmu_url = "https://api.bilibili.com/x/v1/dm/list.so?oid=" + oid
        return danmu_url
        # print(danmu_url)
        # print(len(page))
        # print(type(page))

    # 解析页面，Xpath不能解析指明编码格式的字符串，所以此处我们不解码，还是二进制文本
    def get_danmu_page(self, danmu_url):
        # 请求弹幕网页url
        response = requests.get(url = danmu_url, headers = self.headers)
        print(response.content.decode())


    # 运行
    # def run(self):
    #     根据BV号获取弹幕地址
        # start_url = self.get_danmu_url()
        # 根据弹幕地址解析页面
        # danmu_url = self.get_danmu_page(start_url)


if __name__ == '__main__':
    # BV号： BV1zg4y1q7RT
    BVName = input("请输入要爬取的视频的BV号：")
    spider = BilibiliDanmuSpider(BVName)
    spider.get_danmu_url()

