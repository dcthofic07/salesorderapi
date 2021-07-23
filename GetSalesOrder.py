import requests
import json


def read_data():
    headers = {
        'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIzN2JhMzFkOC03MDJlLTM4MDAtOWUxYi1lNTE2OTg3MTIxZTMiLCJjb250ZXh0Ijp7ImJhc2VVcmwiOiJodHRwczpcL1wvc2Jncm91cGl0LmF0bGFzc2lhbi5uZXQiLCJ1c2VyIjp7ImFjY291bnRJZCI6IjVlOGYwNjQwMmNjZmJmMGI5MDM2NWQxZiJ9fSwiaXNzIjoiY29tLmthbm9haC50ZXN0LW1hbmFnZXIiLCJleHAiOjE2NTgzMzA1NTAsImlhdCI6MTYyNjc5NDU1MH0.o_Sy-DhzGsKQhnWdLqQ9x1aQ9fNEmerJuv8fNMV4mns',
        'Content-Type': 'application/json'
    }
    response = requests.get("https://api.zephyrscale.smartbear.com/v2/testcases/SP-T37/teststeps", headers=headers)
    data = json.loads(response.text)
    return data['values'][0]['inline']['testData']


read_data()