import requests
import json
import time
import urllib3
urllib3.disable_warnings()
def ios12_get_rank(keyword,appid):
    st = time.time()
    cookies = {
        'wosid-lite': 'udbGWDV4NWTsCS8xPuGVcg',
        'pldfltcid': '37d90499766645efaeffab0e31f26247055',
        'ndcd': 'wc1.1.w-855182.1.2.YYTq2gydU37Bp1LD-JCstg%%2C%%2C.4LmgZ5CbRibf6Xj5DaXo9kIAD9o-ZNyXTSkIyF-ltVHOWvAHIipI0NtN9dgxgLE7CBe_ixKwC1M2L0c6TT3Vjjl3uKiL0bmkij-b5CNKHZ4IPrBKs0JHsxigWuYzLlwQoHUarFtPqqWmoyP3IXQD-08EMPbyKziAbMVdCpjKSM0%%2C',
        'mz_at_ssl-16322342170': 'AwUAAAF4AAHVJgAAAABdCd/KNn5+rDEOUw2/ePGa9f9ywrHJQgU=',
        'mz_at0-16322342170': 'AwQAAAF4AAHVJgAAAABdCd/KJQiA/YPuJHq8TXY2f1CYWDYGkFM=',
        'itspod': '55',
        'xp_ci': '3zhkROTz6MHz4S5zCwOzXiPqEDD4',
        'xp_abc': 'tctfLBP2',
        'xt-b-ts-16322342170': '1560928202008',
        'X-Dsid': '16322342170',
        'vrep': 'CJrajOc8EgQIAhAAEgQIARAAEgQIBBAAEgQIAxAAEgQIBRAAEgQIBhAAEgQICRAAEgQIBxAAEgQICBAAEgQIChAA',
        'xt-src': 'b',
        'xp_ab': '1#NyCxKBD+471+qnaQUdu0#isj11bm+9100+tctfLBP2',
    }
 
    headers = {
        'Host': 'api-edge.apps.apple.com',
        'User-Agent': 'AppStore/3.0 iOS/12.1.2 model/iPhone8,1 hwp/s8000 build/16C101 (6; dt:120) AMS/1',
        'X-Apple-Store-Front': '143441-1,29 t:apps3',
        'X-Apple-iAd-Request-Data': 'AAAAHAAAAV0K1gIJAACAx7ZE10ESEmNvbS5hcHBsZS5BcHBTdG9yZRoJaVBob25lOCwxJQAAAEEoAjIBMTodVmVyc2lvbiAxMi4xLjIgKEJ1aWxkIDE2QzEwMSlCCzE0MzQ0MS0xLDI5SgV6aF9DTlIOemhfSGFucy1QaW55aW5SDnpoX0hhbnMtUGlueWluUgVlbW9qaVIFZW5fVVNYAWAAaAGoAQCyASRCODI1RkUyNi1GODNFLTQ1OTgtOTJBOS02NEE0M0I0QjE1QkO6ASQwRDExMzBCOC05N0E0LTQxNEYtQkE1RC04QTI5N0Q3RUYyRTHKASlEUElELTZBMTZBNTkxLTQ5RDktNDlGNS1BQ0UxLTczQTRFNTk5RURBRfABAPoBJDU3OUZFRjcxLUE3MTAtNDEyRS1CREZELTFEN0FFQTJGRDU5M5ICAjAxmgIDNDYwqAICsgICZW64AgEQABgA',
        'X-DSID': '16322342170',
        'X-Apple-Tz': '28800',
        'X-Apple-iAd-Env-Name': 'AAAAAAAAAEQKAlNTEjlodHRwczovL3RyLmlhZHNkay5hcHBsZS5jb20vYWRzZXJ2ZXIvMi42L3Nwb25zb3JlZC9zZWFyY2gaAzIuNg==',
        'X-Apple-Client-Application': 'com.apple.AppStore',
        'X-Apple-I-TimeZone': 'GMT+8',
        'Connection': 'keep-alive',
        'X-Apple-I-Client-Time': '2019-06-26T02:40:30Z',
        'X-Apple-App-Store-Client-Request-Id': '5B28EEB8-1C6B-485C-ACDE-CE607E0D61A8',
        'Authorization': 'Bearer eyJraWQiOiJGNDdEWk4xOEYwIiwiYWxnIjoiRVMyNTYifQ.eyJpc3MiOiJBUzI4UjdHMTdNIiwiaWF0IjoxNTYwNDkyODgyLCJleHAiOjE1NjMwODQ4ODJ9.vPl82SQDbs0o8TFBoEkvjSk3TzDdh5npaQlP2mQspVPv2qYOHscV-jun8o4PZmMSpwanmovCDCFf3bHHlBPZFQ',
        'Accept-Language': 'zh-Hans-CN',
        'X-Apple-I-MD-RINFO': '17106176',
        'X-Apple-ADSID': '000651-08-e8e477c4-1d62-41e0-9236-a84ae8fa2803',
        'Accept': '*/*',
        'Accept-Encoding': 'br, gzip, deflate',
        'X-Apple-I-MD-M': 'wpgb7FOqeEG2INWFLKKHRfSnUCAw15zJcIk8P8OLKR+Tp/1PV+VKMUDkOcTmcAo7dT835g/usrX+EztS',
        'X-Apple-I-Locale': 'zh_CN',
        'X-Apple-I-MD': 'AAAABQAAABBFuvbzMu+lvc0EVeOntirfAAAAAw==',
    }
    # proxies = {
    #     "https": "https://129.28.149.223:16819",
    # }
    # proxy = '129.28.149.223:16819'
    # list = []
    # proxies = {
    #     'http': 'http://' + proxy,
    #     'https': 'https://' + proxy,
    # }
    response = requests.get('https://api-edge.apps.apple.com/v1/catalog/cn/search?platform=iphone&extend=editorialBadgeInfo,messagesScreenshots,minimumOSVersion,requiredCapabilities,screenshotsByType,supportsFunCamera,videoPreviewsByType&include=apps,top-apps&bubble[search]=apps,developers,groupings,editorial-items,app-bundles,in-apps&term={}&l=zh-Hans-CN'.format(keyword), headers=headers, cookies=cookies, verify=False)
 
 
    print(response.status_code)
    print(response.text)
    print(type(json.loads(response.text)))
    print(json.loads(response.text)["results"]["search"]["data"])
    allapp = json.loads(response.text)["results"]["search"]["data"]
    app_id_list =[]
    for i in allapp:
        if i["type"]=="apps":
            app_id_list.append(i["id"])
    apprank = 0
    try:
        apprank = app_id_list.index(appid)+1
    except:
        apprank = 0
    et = time.time()
    print("间隔时间",et-st)
    return apprank
if __name__ == '__main__':
    rank = ios12_get_rank("卡牌游戏","1356040265")
    print(rank)


'''
import time
import requests
import urllib3
urllib3.disable_warnings()

def get(keyword):
    headers = {'x-apple-store-front': '143465-19,29 t:apps3','authorization': 'Bearer eyJraWQiOiJGNDdEWk4xOEYwIiwiYWxnIjoiRVMyNTYifQ.eyJpc3MiOiJBUzI4UjdHMTdNIiwiaWF0IjoxNTY3NTc4Mzc2LCJleHAiOjE1NzAxNzAzNzZ9.a9TkggDjSFDJ9YH7gzKsxA0Q2N2GMH8RK-2ZG1uVtOw9j1asG1ujMvH-uKXDynTBP3roNR6zM6i685BC38kITA'}
    params = (('platform', 'iphone'),('extend', 'editorialBadgeInfo,messagesScreenshots,minimumOSVersion,requiredCapabilities,screenshotsByType,supportsFunCamera,videoPreviewsByType'),('include', 'apps,top-apps'),('bubble[search]', 'apps,developers,groupings,editorial-items,app-bundles,in-apps'),('term', '{}'.format(keyword)),('l', 'zh-Hans-CN'))
    response = requests.get('https://api-edge.apps.apple.com/v1/catalog/cn/search', headers=headers, params=params,verify=False)
    print(response.text)


get("快手")
'''
