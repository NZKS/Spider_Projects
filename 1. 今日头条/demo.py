import execjs
import requests

with open("toutiao.js") as javascript_file:
    ctx = execjs.compile(javascript_file.read())

    first_url = "https://www.toutiao.com/api/pc/list/feed?channel_id=3189398996&min_behot_time=0&refresh_count=1&category=pc_profile_channel&aid=24&app_name=toutiao_web"
    _signature = ctx.call("_signature", first_url)

    signature_url = first_url + "&_signature=" + _signature

    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"}

    response = requests.get(url=signature_url, headers=headers)

    data_list = response.json()["data"]
    for data in data_list:
        print(data)
