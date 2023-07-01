import json
diem = '{"SBD":"001008","MS_HS":"0117768938","Diem":"Ngữ văn: 6.50; Ngoại ngữ: 5.75; Toán:  7.50; Tổng điểm XT: 33.75"}'
comma = ";"
data = json.loads(diem)

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4, separators=(", ", " : "))
    f.write(comma)