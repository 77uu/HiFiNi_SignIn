import requests
import re

SIGN_IN_URL = "https://www.hifini.com/sg_sign.htm"

def main():
    post_data = {"x-requested-with": "XMLHttpRequest"}
    cookies = {"enwiki_session":r"bbs_sid=3duptpusvrahu1f5pvak6rlm8b; bbs_token=5P8NWgKQ3xftXY8mj9GEs5eDrb5wyl_2FSSOY3tz6o3N_2FLEGiKfhCuQj2WB_2FmpqpiBEHKXdjsvFD4MymFqcDcERNE5_2FgU_3D; Hm_lvt_4ab5ca5f7f036f4a4747f1836fffe6f2=1631490409,1631522127,1631664465,1631935253; Hm_lpvt_4ab5ca5f7f036f4a4747f1836fffe6f2=1632188930"}
    r1 = requests.post(url=SIGN_IN_URL, data=post_data, cookies=cookies)
    html_text = r1.text
    is_sign = False
    for line in html_text.splitlines():
        if line.find('今天已经签过啦') != -1:
            print("今天已经签过啦")
            is_sign = True
    if not is_sign: print("签到成功!")
    return 0

if __name__ == '__main__':
    if main() != 0:
        print("Script execution error, abnormal exit !")
    pass

