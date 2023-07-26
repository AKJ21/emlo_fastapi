import requests
import time

# Get 100 requests from gpt model
sum_gpt=0
print("Starting inference on GPT model. Generating 128 tokens per request...")
for i in range(100):
    start = time.time()

    # url = "http://3.110.139.232:8080/infer" # Ran on aws instance
    url = "http://127.0.0.1:8080/infer"
    payload = {'text':"I solemnly swear I am up to no good.", 'max_new_tokens':128}
    response = requests.get(url, params=payload)
    # print(response.text)
    
    end = time.time()
    resp_time = end-start
    print("Response time {}: {}".format(i+1, resp_time), "secs")
    sum_gpt+=resp_time

print("\n")

# Get 100 requests from vit model
sum_vit=0
print("Starting inference on VIT model...")
for i in range(100):
    start = time.time()

    # url = "http://3.110.139.232:8081/infer" # Ran on aws instance
    url = "http://127.0.0.1:8081/infer"
    img_url = "./sample/download.jpg"
    response = requests.post(url, files={"image": open(img_url, "rb")})
    # print(response.text)

    end = time.time()
    resp_time = end-start
    print("Response time {}: {}".format(i+1, resp_time), "secs")
    sum_vit+=resp_time

print("-"*80)
print("Average response time for GPT model: ", sum_gpt/100, "secs")
print("Average response time for VIT model: ", sum_vit/100, "secs")