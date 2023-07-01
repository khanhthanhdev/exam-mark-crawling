import requests
from bs4 import BeautifulSoup

def get_token(id, type="01"):
    url = "https://tsdaucap.hanoi.gov.vn/tra-cuu-diem-thi-10"

    headers = {
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "requestverificationtoken": "CfDJ8CjI4AkC0xlNiBlQXi0796pPe6spT-DfbWy4y6fzzNzKn6gTNWqRaiTYsB6cq9mcBCvG0RDSZF5_7eeno9ZwSU8bYYF4FaC2fPNPde5hishfnDuriO0mixSjHM1D3jKiFIKD0PCx9zTEJ_BkdfjdnGg",
        "cookie": "BIGipServerPool_TSDC_HN=1915228332.34048.0000; .AspNetCore.Antiforgery.68HoDSos0ic=CfDJ8CjI4AkC0xlNiBlQXi0796pPe6spT-DfbWy4y6fzzNzKn6gTNWqRaiTYsB6cq9mcBCvG0RDSZF5_7eeno9ZwSU8bYYF4FaC2fPNPde5hishfnDuriO0mixSjHM1D3jKiFIKD0PCx9zTEJ_BkdfjdnGg",
    }

    data = {
        "LOAI_TRA_CUU": type,
        "GIA_TRI": id,
        "CaptchaTime": "CfDJ8GaVrXyqbnxOu3wE-OMJ5pjGk_ehkKnj_M_GmN6fsxxJf7y7LQEg8XabVJ6jclU6LhH7r1xhVcwmMkxb395cMgGVKpnQLhN7LOsoEjeVCPPXWY9IUJ6Nd80ey-PnqgRK9A",
        "CaptchaInput": "UN61",
    }

    response = requests.post(url, headers=headers, data=data)
    response_data = response.json()
    return response_data["key"]


def get_mark_from_token(token):
    url = f"https://tsdaucap.hanoi.gov.vn/TraCuu/KetQuaTraCuuTuyenSinh10?key={token}"
    response = requests.get(url)
    source = response.text
    dom = BeautifulSoup(source, "html.parser")

    mark = dom.select(".box-thong-tin-diem .row")[3].find("b").text
    name = dom.select(".box-thong-tin-diem .row")[2].find("b").text

    return {"name": name, "mark": mark}


userid = input("Enter your student ID: ")
mark = get_mark_from_token(get_token(userid))

print(f"Your mark is: {mark['mark']}")
print(f"Your name is: {mark['name']}")