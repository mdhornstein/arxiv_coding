import requests 

def hello_world_requests():
    r = requests.get("https://api.github.com/events")
    print("*" * 50)
    print(f"url: {r.url}")
    json_output = r.json()
    print("*" * 50)
    print(f"type of json output: {type(json_output)}")
    print(f"length of json output: {len(json_output)}")
    print("*" * 50)
    print(json_output[0])

if __name__ == "__main__":
    hello_world_requests()
