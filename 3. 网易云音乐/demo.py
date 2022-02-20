import execjs
import requests


class WangYiYun_Spider:
    def __init__(self):
        # csrf_token 可以留空
        self.ajax_url = "https://music.163.com/weapi/music-vip-membership/front/vip/info"

        self.headers = {
            "origin": "https://music.163.com",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36",
        }

    def parse(self, user_id):
        # 指定的用户链接(对头部非常重要)
        user_url = f"https://music.163.com/user/songs/rank?id={user_id}"

        # ajax_url 的参数, 用于加密
        json_content = {"userId": "1681889734", "csrf_token": ""}
        a_key = "010001"
        b_key = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
        c_key = "0CoJUm6Qyw8W8jud"

        with open("网易云.js", "r", encoding="utf-8-sig") as javascript_file:
            ctx = execjs.compile(javascript_file.read())

        # 把参数放入 js, 然后进行加密
        result = ctx.call("d", str(json_content), a_key, b_key, c_key)

        # 更换 referer, 这样可以爬取指定的用户
        self.headers["referer"] = user_url

        data = {"params": result["encText"], "encSecKey": result["encSecKey"]}

        response = requests.post(self.ajax_url, data=data, headers=self.headers).text
        print(response)


if __name__ == '__main__':
    spider = WangYiYun_Spider()
    spider.parse("1681889734")
