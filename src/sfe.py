import requests
import json

# url = "http://www.baidu.com/"
url = 'http://ad.wkanx.com/data/plan/list'
# url = "http://144.34.194.39:8080"
# url = "http://e.qq.com/"

headers = {
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": "remember_82e5d2c56bdd0811318f0cf078b78bfc=eyJpdiI6IlpwR2RtNERRUFNYcDV2TU1hUEhtVFE9PSIsInZhbHVlIjoiNnBFUHZXOGlYRG5RS3IzYzlpYzBYTmg3eldPXC9Va0pQVWdSbEptaWk1b1N3alZiSVFNRk0xbCtaK3JGN1QzeHl4Vno4dzExT2dKdGozM2dhWDU4R0d5RHUxXC9GVHM4ejd4dCtaWjlPb2swaz0iLCJtYWMiOiJjY2ViNzdkYmQyYjhkYjU5ZDRiNTM1ZmMxZDk0ZDk2NzY0OTZiMWVmOWRjNTA4NzNjZTFhOGIwMGFlZWI4Nzg2In0%3D; laravel_session=eyJpdiI6IjVFREc5YU5aUGNCeXJlSnlITXYzNFE9PSIsInZhbHVlIjoidlIxRFNTTUZCdzBXcjNDc0Q1dWg2dmo3WFJXRHRpNVlZN1pmZDREK0RIVng2THdWdU5XcGlHZkhXOFZ3TUg5SThmQVo4bk51UXdMZWNmcW44TFNkU2c9PSIsIm1hYyI6ImY2ODM2NzU0Y2U0NDgzMzZjMzc1YTA4MzcyODcxYmY2YmMwNGNmOTM2Yzc5ODJjMjY3ZDc0NDdkNmM2YzRhMDMifQ%3D%3D",
    "Host": "ad.wkanx.com",
    "Referer": "http://ad.wkanx.com/",
    "X-Forwarded-For": "161.177.151.224",
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36'
}
data = {'pageSize': 50, 'lref': 'http%3A%2F%2Fad.wkanx.com%2F%23%2Fuser%2Flogin'}
ip_port = '183.146.213.198:80'
proxies = {
    'http': 'http://' + ip_port,
    'https': 'https://' + ip_port
}

# response = requests.request("GET", url, proxies=proxies, headers=headers)
# response = requests.request("GET", url, proxies=proxies)
response = requests.request("POST", url, data=json.dumps(data), proxies=proxies, headers=headers)
# response = requests.request("POST", url, data=json.dumps(data), headers=headers)
# response = requests.request("GET", url, headers=headers)
# response = requests.request("GET", url)

print(response.text)
print(response.status_code)
