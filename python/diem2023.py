import requests
import json
import time
import threading
reqUrl = "https://hanoimoi.vn/api/getdiemthi2023"

headersList = {
 "authority": "hanoimoi.vn",
 "accept": "*/*",
 "accept-language": "en-US,en;q=0.9",
 "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
 "cookie": "zone-430=0; zone-330=0; zone-230=0; zone-130=0",
 "origin": "https://hanoimoi.vn",
 "referer": "https://hanoimoi.vn/diem-thi-lop-10-2023",
 "sec-ch-ua-mobile": "?0",
 "sec-fetch-dest": "empty",
 "sec-fetch-mode": "cors",
 "sec-fetch-site": "same-origin",
 "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.58",
 "x-requested-with": "XMLHttpRequest" 
}

start = time.time()

def form1() :
    with open('data2.json', 'w', encoding='utf-8') as f:
        for i in range(200000, 205000):
            userid = str(i)
            payload = "t=2&q=" + userid
            response = requests.request("POST", reqUrl, data=payload,  headers=headersList)
            data = response.text
            json_object = json.loads(data)
            if json_object["SBD"] != "":
                json.dump(json_object, f, ensure_ascii=False, indent=4, separators=(", ", " : "))
                f.write(",\n")

def form2() :
    with open('data3.json', 'w', encoding='utf-8') as f:
        for i in range(205000, 210000):
            userid = str(i)
            payload = "t=2&q=" + userid
            response = requests.request("POST", reqUrl, data=payload,  headers=headersList)
            data = response.text
            json_object = json.loads(data)
            if json_object["SBD"] != "":
                json.dump(json_object, f, ensure_ascii=False, indent=4, separators=(", ", " : "))
                f.write(",\n")

def form3() :
    with open('data4.json', 'w', encoding='utf-8') as f:
        for i in range(210000, 215000):
            userid = str(i)
            payload = "t=2&q=" + userid
            response = requests.request("POST", reqUrl, data=payload,  headers=headersList)
            data = response.text
            json_object = json.loads(data)
            if json_object["SBD"] != "":
                json.dump(json_object, f, ensure_ascii=False, indent=4, separators=(", ", " : "))
                f.write(",\n")


# def form1():
#     with open('data2.json', 'w', encoding='utf-8') as f:
#         json_objects = [requests.get(reqUrl, params={"t": 2, "q": str(i)}).json() for i in range(100001, 105000)]
#         for json_object in json_objects:
#             if json_object["SBD"] != "":
#                 f.write(json_object["SBD"] + ",\n")

# def form2():
#     with open('data3.json', 'w', encoding='utf-8') as f:
#         json_objects = [requests.get(reqUrl, params={"t": 2, "q": str(i)}).json() for i in range(105000, 110000)]
#         for json_object in json_objects:
#             if json_object["SBD"] != "":
#                 f.write(json_object["SBD"] + ",\n")

# def form3():
#     with open('data4.json', 'w', encoding='utf-8') as f:
#         json_objects = [requests.get(reqUrl, params={"t": 2, "q": str(i)}).json() for i in range(110000, 115000)]
#         for json_object in json_objects:
#             if json_object["SBD"] != "":
#                 f.write(json_object["SBD"] + ",\n")

t1 = threading.Thread(target=form1)
t2 = threading.Thread(target=form2)
t3 = threading.Thread(target=form3)
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()

# with concurrent.futures.ThreadPoolExecutor(3) as tp:
#     tp.submit(form1)
#     tp.submit(form2)
#     tp.submit(form3)

end = time.time()
print(f"Runtime of the program is {end - start}")
print("Done")
