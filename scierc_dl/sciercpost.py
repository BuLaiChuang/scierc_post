import requests
import json

# python的requests库发送form-data参数    da   d

url = "http://10.10.12.91:32318/spert"

# form-data参数要写成如下格式，注意有None
data = {
    "modelType": (None, "military_field_en"),
    "text": (None, "This paper presents a new approach to  statistical sentence generation  in which alternative  phrases  are represented as packed sets of  trees , or  forests , and then ranked statistically to choose the best one. This representation offers advantages in compactness and in the ability to represent  syntactic information . It also facilitates more efficient  statistical ranking  than a previous approach to  statistical generation . An efficient  ranking algorithm  is described, together with experimental results showing significant improvements over simple enumeration or a  lattice-based approach .")
}

# 此种方式发送form-data类型参数时，请求时不要headers，且用files参数
response = requests.request("POST", url, files=data)

result_str = response.text

result_json = json.loads(result_str)

print(result_json)

entities_list = result_json['data']['entities']

# 定义一个list
entity_list = []

for entity in entities_list:

    # entities_list.append(entity[0])
    print(entity)
    entity_list.append(entity)

print(entity_list)