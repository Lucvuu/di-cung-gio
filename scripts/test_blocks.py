import json, sys, re
sys.stdout.reconfigure(encoding='utf-8')

# 1. Load parsed tours
with open('scripts/parsed_tours.json', 'r', encoding='utf-8') as f:
    tours_data = json.load(f)

# Convert to JS code
tours_js = json.dumps(tours_data, ensure_ascii=False, indent=2)

departure_schedule = [
  {
    "id": "sch-1",
    "day": "26",
    "month": "Th10",
    "code": "YT01",
    "title": "Trekking Yên Tử – Chùa Đồng",
    "duration": "Trong ngày",
    "price": "550.000đ",
    "priceNum": 550000,
    "dateFull": "26/10/2026",
    "status": "Còn chỗ",
    "tourId": 1
  },
  {
    "id": "sch-2",
    "day": "01",
    "month": "Th11",
    "code": "PSP01",
    "title": "Tà Xùa – Phu Sa Phìn Săn Mây",
    "duration": "2 ngày 1 đêm",
    "price": "1.600.000đ",
    "priceNum": 1600000,
    "dateFull": "01/11/2026",
    "status": "Còn chỗ",
    "tourId": 2
  },
  {
    "id": "sch-3",
    "day": "08",
    "month": "Th11",
    "code": "SM01",
    "title": "Sa Mu – U Bò (Rừng Rêu)",
    "duration": "2 ngày 1 đêm",
    "price": "2.800.000đ",
    "priceNum": 2800000,
    "dateFull": "08/11/2026",
    "status": "Còn chỗ",
    "tourId": 3
  },
  {
    "id": "sch-4",
    "day": "15",
    "month": "Th11",
    "code": "KQS01",
    "title": "Kỳ Quan San – Đồi Muối",
    "duration": "3 ngày 2 đêm",
    "price": "3.500.000đ",
    "priceNum": 3500000,
    "dateFull": "15/11/2026",
    "status": "Còn chỗ",
    "tourId": 4
  },
  {
    "id": "sch-5",
    "day": "22",
    "month": "Th11",
    "code": "TCN01",
    "title": "Tà Chì Nhù – Hoa Chi Pâu",
    "duration": "2 ngày 1 đêm",
    "price": "2.800.000đ",
    "priceNum": 2800000,
    "dateFull": "22/11/2026",
    "status": "Còn chỗ",
    "tourId": 5
  }
]
schedule_js = json.dumps(departure_schedule, ensure_ascii=False, indent=2)

print("Generated JSON data blocks successfully!")

