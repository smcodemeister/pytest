import requests
import json

url = "https://api.publicapis.org/entries"
payload={}
headers = {}  
response = requests.request("GET", url, headers=headers, data=payload)

def getCount():
    response_text = json.loads(response.text)
    response_count = response_text["count"]
    #print(response_text)
    return response_count

def main():
    getCount()

if __name__ == "__main__":
    main()