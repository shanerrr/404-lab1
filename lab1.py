import requests
# print(requests.__version__)
request = requests.get('https://raw.githubusercontent.com/shanerrr/404-lab1/main/lab1.py')
print(request.text)