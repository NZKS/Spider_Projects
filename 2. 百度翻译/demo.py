import execjs
import requests


class baidu_fanyi:
    def __init__(self):
        # 判断语言链接
        self.detect_url = "https://fanyi.baidu.com/langdetect"

        # 翻译链接
        self.trans_url = "https://fanyi.baidu.com/v2transapi?from={}&to=en"

        # 头部
        self.headers = {
            "Referer": "https://fanyi.baidu.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
            "Cookie": "输入您的 Cookie (百度翻译网站)"
        }

    # 判断是哪种语言
    def detect_lang(self, query):
        data = {"query": query}

        response = requests.post(url=self.detect_url, data=data, headers=self.headers).json()
        if response["error"] == 0:
            return response["lan"]

        else:
            # 这边输出，到时候方便看问题情况
            print(response)
            return False

    # 进行翻译
    def transfer_lang(self, query, lang):
        with open("baidu.js") as javascript_file:
            ctx = execjs.compile(javascript_file.read())

        sign = ctx.call("sign", query)

        url = self.trans_url.format(lang)
        data = {
            "from": lang,
            "to": "en",
            "query": query,
            "transtype": "realtime",
            "simple_means_flag": "3",
            "sign": sign,
            "token": "b7ddd8ad9cbc810a5e8e19f4fe8d80f7",
            "domain": "common"
        }

        response = requests.post(url, data=data, headers=self.headers).json()
        trans_result = response["trans_result"]["data"][0]["dst"]

        return trans_result

    def main(self):
        query = input("请输入你要翻译的文字：")

        lang = self.detect_lang(query)
        if lang is False:
            print("检测语言时，出现错误！")

        else:
            result = self.transfer_lang(query, lang)

            print("翻译结果为:", result)


if __name__ == '__main__':
    spider = baidu_fanyi()
    spider.main()
