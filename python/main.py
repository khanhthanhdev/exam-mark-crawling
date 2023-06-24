import requests
from bs4 import BeautifulSoup

def get_token(id, type="01"):
    url = "https://tsdaucap.hanoi.gov.vn/tra-cuu-diem-thi-10"

    headers = {
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "requestverificationtoken": "CfDJ8GaVrXyqbnxOu3wE-OMJ5pjzIffrAdNleB_FuVzhXbu7XWquMZ_flWEGEnWahe6haWBwWXE_aKeG8rFv6gFgr8PzVGV5CdKtlMTbukctHTfpxIUZR3Eq8y8EMwF9xzszwMaJBywVKBrsOncjXYx1dy4",
        "cookie": "BIGipServerPool_TSDC_HN=1932005548.34304.0000; .AspNetCore.Antiforgery.68HoDSos0ic=CfDJ8GaVrXyqbnxOu3wE-OMJ5piXLNbeT7pu3R4hkfmQcY221KFa73heDYv0hypBflxGvqRCGb85CnB9G6r_FyLRvlnHPzLL1ZNMTx6nsJffRWctPPH2V4XKcvrqBrGnljrguHcH_ttF1L2pRT6-S7lV-qs",
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