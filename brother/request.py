'''
请求题目
'''
import requests
import base64
trackId='031802342'
url = "http://47.102.118.1:8089/api/challenge/start/42ff0dbd-8ac7-47dd-847e-0bd2b5669435"
body = {
    "teamid":44,
    "token":"b305a640-b3a9-4f25-a4fb-befb6b7db9d9"
}
headers = {'content-type':"application/json"}
response = requests.request("post",url,headers=headers,json=body)
use_dic=response.json()
data=use_dic['data']
img=data['img']
stepre=data['step']
uuid=use_dic['uuid']
swap=data['swap']
image_data = base64.b64decode(img)  # 解码图片
print(swap)
print(stepre)
print(uuid)
