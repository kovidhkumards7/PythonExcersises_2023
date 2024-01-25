import requests
import json

fd = requests.get("https://date.nager.at/api/v2/publicholidays/2020/US")
print(fd.json())
print(fd)


