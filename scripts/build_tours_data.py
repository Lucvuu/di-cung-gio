import json, sys
sys.stdout.reconfigure(encoding='utf-8')

# Build the complete TOURS_DATA list
tours = [
  # TOUR 1: YÊN TỬ – CHÙA ĐỒNG (YT01)
  {
    "id": 1,
    "code": "YT01",
    "title": "Trekking Yên Tử – Chùa Đồng",
    "category": "spiritual",
    "subCategory": "trekking",
    "badge": "Tâm linh & Non thiêng",
    "altitudeBadge": "Đỉnh 1.068m",
    "image": "assets/images/tour-yen-tu.jpg",
    "price": "550.000đ/người",
    "priceNum": 550000,
    "agencyPrice": "500.000đ",
    "minPax": "Từ 5 khách",
    "departureFrequency": "Hàng ngày",
    "pickupPoint": "55 Nguyễn Quốc Trị & 489 Hoàng Quốc Việt, Hà Nội",
    "duration": "Trong ngày",
    "location": "Uông Bí, Quảng Ninh",
    "altitude": "1.068m",
    "trekDistance": "Khoảng 6 km (~6.000 bậc đá)",
    "difficultyLevel": 2,
    "difficultyText": "Nhẹ - Trung bình",
    "isFeatured": True,
    "reviews": 128,
    "shortSummary": "Hành hương về non thiêng đất Phật, băng rừng Tùng cổ thụ 700 năm chạm đỉnh Chùa Đồng (1.068m).",
    "routeMap": "Xuất phát từ Hà Nội theo cao tốc Hải Phòng đi Uông Bí (Quảng Ninh). Tuyến trekking bắt đầu từ Suối Giải Oan, qua Đường Tùng cổ thụ 700 năm tuổi, Vườn Tháp Tổ Huệ Quang, Chùa Hoa Yên, Chùa Một Mái, tượng đá An Kỳ Sinh, vượt dốc Đá Chồng và chạm đỉnh Chùa Đồng 1.068m giữa mây ngàn Đông Bắc.",
    "routeSteps": ["Hà Nội", "Suối Giải Oan", "Đường Tùng 700 năm", "Chùa Hoa Yên", "Tượng An Kỳ Sinh", "Đỉnh Chùa Đồng (1.068m)"],
    "historyStory": "Núi Yên Tử (còn gọi là Bạch Vân Sơn – núi mây trắng) là cái nôi của Thiền phái Trúc Lâm Đại Việt do Phật hoàng Trần Nhân Tông sáng lập năm 1299 sau hai lần đánh thắng quân Nguyên Mông. Chùa Đồng trên đỉnh núi được đúc hoàn toàn bằng đồng nguyên khối trên đỉnh núi lớn nhất châu Á, tọa lạc tại độ cao 1.068m giữa biển mây hùng vĩ.",
    "description": "Hành trình leo núi thiêng Yên Tử, chiêm bái Chùa Đồng trên đỉnh Phù Vân, rèn luyện thể lực và tìm lại an yên trong tâm hồn giữa mây ngàn đại ngàn.",
    "departureDates": ["26/10/2026", "02/11/2026", "09/11/2026", "16/11/2026"],
    "gallery": [
      { "url": "assets/images/tour-yen-tu.jpg", "caption": "Chóp Chùa Đồng giữa mây ngàn Yên Tử" },
      { "url": "assets/images/yen-tu-1.jpg", "caption": "Mái chùa đồng cổ kính linh thiêng trên đỉnh núi đá" },
      { "url": "assets/images/yen-tu-2.jpg", "caption": "Toàn cảnh non thiêng Yên Tử từ độ cao 1.068m" },
      { "url": "assets/images/yen-tu-3.jpg", "caption": "Hành hương qua Đường Tùng cổ thụ 700 năm tuổi" }
    ],
    "highlights": [
      "Chạm tay vào Chùa Đồng đúc bằng đồng nguyên khối lớn nhất Châu Á trên đỉnh Phù Vân.",
      "Dạo bước giữa rừng trúc bạt ngàn ngàn năm tuổi và đường Tùng cổ thụ 700 năm.",
      "Đón bình minh hoặc hoàng hôn dát vàng trên non thiêng Yên Tử thanh tịnh và an lạc."
    ],
    "itinerary": [
      { "day": "05:30", "title": "Hà Nội – Uông Bí", "desc": "Xe đón đoàn tại 55 Nguyễn Quốc Trị và 489 Hoàng Quốc Việt, khởi hành đi Uông Bí (Quảng Ninh). Dừng chân ăn sáng đặc sản bánh cuốn chả mực." },
      { "day": "08:30", "title": "Bắt đầu trekking Yên Tử", "desc": "Khởi động tại chân núi, trekking qua suối Giải Oan, Tháp Tổ Huệ Quang, chùa Hoa Yên, chùa Một Mái giữa rừng thông xanh ngát." },
      { "day": "12:00", "title": "Chạm đỉnh Chùa Đồng 1.068m", "desc": "Chiêm bái Chùa Đồng linh thiêng trong sương mây, thưởng ngoạn panorama toàn cảnh Đông Bắc, dùng bữa trưa picnic." },
      { "day": "16:00", "title": "Xuống núi & Về Hà Nội", "desc": "Xuống núi, thư giãn ngâm chân thảo dược suối Giải Oan. Lên xe về lại thủ đô Hà Nội lúc 19:30." }
    ],
    "included": [
      "Xe ô tô du lịch đời mới khứ hồi Hà Nội – Yên Tử",
      "Hướng dẫn viên / Leader kinh nghiệm theo sát (tỉ lệ 8-10 khách/leader)",
      "Nước suối tinh khiết 500ml/khách",
      "Huy chương leo núi bằng gỗ độc quyền của Đi Cùng Gió",
      "Gậy leo núi trekking & đồ y tế sơ cứu cơ bản",
      "Bảo hiểm du lịch trọn gói 20.000.000đ/vụ"
    ],
    "preparation": ["Giày trekking hoặc thể thao bám tốt", "CCCD/Hộ chiếu bản gốc", "Áo khoác gió nhẹ, mũ nón chống nắng", "Thuốc cá nhân và sạc dự phòng"]
  },

  # TOUR 2: TÀ XÙA – PHU SA PHÌN (PSP01)
  {
    "id": 2,
    "code": "PSP01",
    "title": "Tà Xùa – Phu Sa Phìn Săn Mây",
    "category": "trekking",
    "subCategory": "trekking",
    "badge": "Đại dương mây",
    "altitudeBadge": "Đỉnh 2.868m",
    "image": "assets/images/tour-ta-xua.jpg",
    "price": "1.600.000đ/người",
    "priceNum": 1600000,
    "agencyPrice": "1.450.000đ",
    "minPax": "Từ 5 khách",
    "departureFrequency": "Thứ 7 - Chủ Nhật hàng tuần",
    "pickupPoint": "55 Nguyễn Quốc Trị & 489 Hoàng Quốc Việt, Hà Nội",
    "duration": "2 ngày 1 đêm",
    "location": "Bắc Yên, Sơn La",
    "altitude": "2.868m",
    "trekDistance": "Khoảng 12 km",
    "difficultyLevel": 3,
    "difficultyText": "Trung bình",
    "isFeatured": True,
    "reviews": 186,
    "shortSummary": "Chinh phục 'Sống lưng khủng long' Háng Đồng, đón biển mây bồng bềnh cuộn trào và khám phá đỉnh Phu Sa Phìn.",
    "routeMap": "Khởi hành từ Hà Nội theo QL32 lên huyện Bắc Yên (Sơn La). Tuyến trekking đưa bạn dọc 'Sống lưng khủng long' tại bản Háng Đồng, check-in Mỏm Cá Heo, Cây Cô Đơn, Đỉnh Gió, thảo nguyên Tà Xùa và rừng nguyên sinh rêu phong huyền ảo.",
    "routeSteps": ["Hà Nội", "Bắc Yên (Sơn La)", "Xã Tà Xùa", "Sống lưng Háng Đồng", "Mỏm Cá Heo & Cây Cô Đơn", "Đỉnh Phu Sa Phìn (2.868m)"],
    "historyStory": "Dãy Tà Xùa hợp thành từ ba đỉnh núi cao kỳ vĩ thuộc phần đuôi kéo dài về phía Nam của dãy Hoàng Liên Sơn hùng vĩ. Nơi đây sở hữu thung lũng lòng chảo giữ mây dày đặc và lâu tan bậc nhất Việt Nam, là quê hương của những cây chè Shan Tuyết cổ thụ hàng trăm năm tuổi của người Mông.",
    "description": "Chinh phục 'sống lưng khủng long' huyền thoại Bản Công, đắm chìm trong biển mây bồng bềnh lúc bình minh và tận hưởng bầu không khí Tây Bắc se lạnh.",
    "departureDates": ["01/11/2026", "08/11/2026", "15/11/2026", "22/11/2026"],
    "gallery": [
      { "url": "assets/images/tour-ta-xua.jpg", "caption": "Biển mây bồng bềnh cuộn trào thung lũng Tà Xùa" },
      { "url": "assets/images/ta-xua-1.jpg", "caption": "Bình minh rực rỡ trên sống lưng khủng long Háng Đồng" },
      { "url": "assets/images/ta-xua-2.jpg", "caption": "Trekker check-in mỏm đá ngắm đại ngàn Tây Bắc" },
      { "url": "assets/images/hero-bg.jpg", "caption": "Toàn cảnh biển mây Tây Bắc lúc rạng đông" }
    ],
    "highlights": [
      "Đi bộ trên Sống Lưng Khủng Long kỳ vĩ với biển mây cuộn trào hai bên sườn núi.",
      "Check-in Mỏm Cá Heo, Cây Táo Mèo cô đơn ngắm hoàng hôn rực rỡ thung lũng Bản Công.",
      "Thưởng thức lẩu gà đen đồi H’Mông nóng hổi bên bếp than hồng và giao lưu đốt lửa trại."
    ],
    "itinerary": [
      { "day": "Ngày 0", "title": "Hà Nội – Tà Xùa", "desc": "19:00 đón đoàn tại 55 Nguyễn Quốc Trị và 489 Hoàng Quốc Việt đi Bắc Yên. Đến Tà Xùa lúc nửa đêm, nhận phòng homestay view mây nghỉ ngơi." },
      { "day": "Ngày 1", "title": "Khám phá Tà Xùa & Rừng rêu", "desc": "Đón bình minh Đỉnh Gió, check-in Cây Cô Đơn, Mỏm Cá Heo. Trekking nhẹ xuyên rừng rêu ma mị. Tối ăn lẩu gà đen." },
      { "day": "Ngày 2", "title": "Sống lưng khủng long – Hà Nội", "desc": "05:30 trekking Sống Lưng Khủng Long Háng Đồng săn biển mây cuồn cuộn. 13:30 lên xe về Hà Nội lúc 19:30." }
    ],
    "included": [
      "Xe ô tô giường nằm / Limousine khứ hồi Hà Nội – Tà Xùa",
      "Homestay view mây Bản Công tiêu chuẩn",
      "Các bữa ăn tiêu chuẩn vùng cao (lẩu gà đen, thịt nướng)",
      "Leader & Porter bản địa chu đáo (tỉ lệ 8-10 khách/leader)",
      "Huy chương leo núi bằng gỗ độc quyền Đi Cùng Gió",
      "Bảo hiểm du lịch trọn gói 100.000.000đ/người"
    ],
    "preparation": ["Áo khoác ấm (nhiệt độ đêm 10-14°C)", "Giày trekking chống trơn trượt", "CCCD/Hộ chiếu bản gốc", "Sạc dự phòng & máy ảnh"]
  },

  # TOUR 3: SA MU – U BÒ (SM01)
  {
    "id": 3,
    "code": "SM01",
    "title": "Sa Mu – U Bò (2.756m)",
    "category": "trekking",
    "subCategory": "trekking",
    "badge": "Rừng rêu ma mị",
    "altitudeBadge": "Đỉnh 2.756m",
    "image": "assets/images/tour-samu.jpg",
    "price": "2.800.000đ/người",
    "priceNum": 2800000,
    "agencyPrice": "2.500.000đ",
    "minPax": "Từ 5 khách",
    "departureFrequency": "Thứ 7 - Chủ Nhật hàng tuần",
    "pickupPoint": "55 Nguyễn Quốc Trị & 489 Hoàng Quốc Việt, Hà Nội",
    "duration": "2 ngày 1 đêm",
    "location": "Bắc Yên, Sơn La",
    "altitude": "2.756m",
    "trekDistance": "Khoảng 14 km",
    "difficultyLevel": 3,
    "difficultyText": "Trung bình",
    "isFeatured": True,
    "reviews": 94,
    "shortSummary": "Chinh phục đỉnh Sa Mu – U Bò (2.756m), ngắm khu rừng rêu cổ thụ ma mị và check-in Cây Thần Kỳ độc nhất vô nhị.",
    "routeMap": "Hành trình từ Hà Nội qua Bắc Yên đến điểm trek Xím Vàng. Tuyến leo xuyên qua thảm thực vật rừng nguyên sinh nguyên sơ với các tầng rêu phủ kín thân cây cổ thụ hàng trăm năm, vượt dốc đá lên lán nghỉ và chạm đỉnh Sa Mu 2.756m.",
    "routeSteps": ["Hà Nội", "Bắc Yên", "Điểm trek Xím Vàng", "Cây Thần Kỳ", "Lán ngủ trên núi", "Đỉnh Sa Mu (2.756m)"],
    "historyStory": "Đỉnh Sa Mu (U Bò) cao 2.756m là ranh giới tự nhiên giữa Sơn La và Yên Bái. Cung trek nổi tiếng với cánh rừng rêu ma mị đẹp bậc nhất vùng Tây Bắc, nơi lưu giữ hệ sinh thái rừng á nhiệt đới nguyên sinh gần như nguyên vẹn chưa bị tác động của con người.",
    "description": "Hành trình lạc bước vào khu rừng cổ tích rêu phong, săn mây đại ngàn và ngắm dải ngân hà lấp lánh khi ngủ đêm trong lán gỗ trên núi.",
    "departureDates": ["01/11/2026", "08/11/2026", "15/11/2026", "22/11/2026"],
    "highlights": [
      "Chiêm ngưỡng khu rừng rêu ma mị với cây cổ thụ phủ kín rêu phong như truyện cổ tích tích.",
      "Check-in Cây Thần Kỳ khổng lồ đứng sừng sững giữa rừng già Tây Bắc.",
      "Ngắm biển mây lúc bình minh từ chóp Sa Mu 2.756m và thưởng thức thịt nướng thơm lừng bên lán gỗ."
    ],
    "itinerary": [
      { "day": "Ngày 0", "title": "Hà Nội – Bắc Yên", "desc": "19:00 xe đón tại 55 Nguyễn Quốc Trị & 489 Hoàng Quốc Việt đi Bắc Yên. Nghỉ đêm homestay chuẩn bị thể lực." },
      { "day": "Ngày 1", "title": "Trek Xím Vàng – Lán rừng rêu", "desc": "Ăn sáng, xe đưa vào điểm trek. Leo dốc qua rừng rêu nguyên sinh ma mị, check-in Cây Thần Kỳ. Chiều đến lán ngủ, ngắm hoàng hôn ăn tối lẩu nóng." },
      { "day": "Ngày 2", "title": "Chạm đỉnh Sa Mu 2.756m – Hà Nội", "desc": "05:00 trekking lên chóp Sa Mu đón bình minh biển mây. Xuống núi ăn trưa, lên xe về lại Hà Nội lúc 20:00." }
    ],
    "included": [
      "Xe ô tô giường nằm đưa đón khứ hồi từ Hà Nội",
      "Lán gỗ ngủ trên núi có túi ngủ & chăn ấm",
      "Porter bản địa gùi đồ & nấu các bữa ăn nóng sốt",
      "Huy chương gỗ Sa Mu kỷ niệm độc quyền",
      "Gậy trekking & đồ y tế, bảo hiểm du lịch trọn gói 100tr"
    ],
    "preparation": ["Giày leo núi có gai bám chống trơn", "Áo ấm giữ nhiệt", "Đèn pin đeo đầu", "Găng tay trekking"]
  },

  # TOUR 4: KỲ QUAN SAN – BẠCH MỘC LƯƠNG TỬ (KQS01)
  {
    "id": 4,
    "code": "KQS01",
    "title": "Kỳ Quan San – Bạch Mộc Lương Tử",
    "category": "trekking",
    "subCategory": "trekking",
    "badge": "Top 4 Nóc nhà VN",
    "altitudeBadge": "Đỉnh 3.046m",
    "image": "assets/images/tour-ky-quan-san.jpg",
    "price": "3.500.000đ/người",
    "priceNum": 3500000,
    "agencyPrice": "3.000.000đ",
    "minPax": "Từ 5 khách",
    "departureFrequency": "Thứ 6 - Chủ Nhật hàng tuần",
    "pickupPoint": "55 Nguyễn Quốc Trị & 489 Hoàng Quốc Việt, Hà Nội",
    "duration": "3 ngày 2 đêm",
    "location": "Bát Xát, Lào Cai",
    "altitude": "3.046m",
    "trekDistance": "Khoảng 28 – 30 km",
    "difficultyLevel": 4,
    "difficultyText": "Thử thách cao",
    "isFeatured": True,
    "reviews": 115,
    "shortSummary": "Hành trình chinh phục đỉnh Kỳ Quan San (3.046m), đón bình minh tráng lệ trên sống lưng khủng long Đồi Muối.",
    "routeMap": "Từ Hà Nội đi Bát Xát (Lào Cai). Tuyến trekking xuất phát từ bản Dền Sung, vượt suối, leo rừng thảo quả, chinh phục Đồi Muối (2.100m) và men theo sống núi hiểm trở để chạm chóp inox 3.046m.",
    "routeSteps": ["Hà Nội", "Bát Xát (Lào Cai)", "Bản Dền Sung", "Lán Đồi Muối (2.100m)", "Sống lưng khủng long", "Đỉnh Kỳ Quan San (3.046m)"],
    "historyStory": "Kỳ Quan San (thường gọi là Bạch Mộc Lương Tử) là đỉnh núi cao thứ 4 tại Việt Nam (3.046m). Tên gọi Kỳ Quan San theo tiếng địa phương nghĩa là 'ngọn núi kỳ vĩ'. Cung đường này được giới mê leo núi mệnh danh là cung đường săn bình minh và biển mây tráng lệ nhất Việt Nam.",
    "description": "Cung trekking huyền thoại thử thách thể lực và ý chí, đón bình minh rực đỏ trên sống lưng Đồi Muối và chạm tay vào đỉnh cao 3.046m.",
    "departureDates": ["15/11/2026", "22/11/2026", "29/11/2026", "06/12/2026"],
    "highlights": [
      "Chiêm ngưỡng bình minh Đồi Muối – một trong những khung cảnh bình minh kỳ vĩ bậc nhất Đông Nam Á.",
      "Đi bộ trên Sống Lưng Khủng Long cheo leo giữa hai bên vực sâu ngút ngàn mây trắng.",
      "Chạm tay vào chóp inox đỉnh cao 3.046m và nhận huy chương gỗ độc quyền của Đi Cùng Gió."
    ],
    "itinerary": [
      { "day": "Ngày 0", "title": "Hà Nội – Sapa – Bát Xát", "desc": "21:00 đón đoàn tại 55 Nguyễn Quốc Trị & 489 Hoàng Quốc Việt, xe giường nằm chạy đêm lên Lào Cai." },
      { "day": "Ngày 1", "title": "Bản Dền Sung – Lán Đồi Muối 2.100m", "desc": "Ăn sáng, xe đưa đến chân núi. Trekking qua suối đá, rừng trúc, rừng thảo quả. Đến lán Đồi Muối, ngắm biển mây hoàng hôn đỏ rực." },
      { "day": "Ngày 2", "title": "Chạm đỉnh Kỳ Quan San 3.046m", "desc": "04:30 trekking vượt Sống lưng khủng long đón bình minh, chạm đỉnh 3.046m lúc 09:30. Chiều quay về lại lán Đồi Muối nghỉ ngơi ăn mừng." },
      { "day": "Ngày 3", "title": "Xuống núi – Tắm lá thuốc Dao đỏ – Hà Nội", "desc": "Xuống chân núi, tắm lá thuốc Dao Đỏ xua tan mệt mỏi tại Sapa. Lên xe về lại Hà Nội lúc 21:00." }
    ],
    "included": [
      "Xe giường nằm khứ hồi Hà Nội – Sapa – Bát Xát",
      "Lán ngủ Đồi Muối có đầy đủ chăn đệm ấm áp",
      "Đội ngũ Porter bản địa nhiệt tình gùi hành lý và nấu ăn",
      "Tắm lá thuốc người Dao đỏ thư giãn hồi phục cơ thể",
      "Huy chương gỗ Kỳ Quan San khắc tên kỷ niệm",
      "Bảo hiểm du lịch mức 100.000.000đ/người"
    ],
    "preparation": ["Giày trekking chuyên dụng bám đá", "Áo ấm lông vũ, áo gió chống nước", "Bó gối, tất dài, găng tay bám", "CCCD/Hộ chiếu bản gốc"]
  },

  # TOUR 5: TÀ CHÌ NHÙ (TCN01)
  {
    "id": 5,
    "code": "TCN01",
    "title": "Tà Chì Nhù – Mùa Hoa Chi Pâu (2.979m)",
    "category": "trekking",
    "subCategory": "trekking",
    "badge": "Mùa hoa Chi Pâu",
    "altitudeBadge": "Đỉnh 2.979m",
    "image": "assets/images/tour-ta-chi-nhu.jpg",
    "price": "2.800.000đ/người",
    "priceNum": 2800000,
    "agencyPrice": "2.500.000đ",
    "minPax": "Từ 5 khách",
    "departureFrequency": "Thứ 7 - Chủ Nhật hàng tuần",
    "pickupPoint": "55 Nguyễn Quốc Trị & 489 Hoàng Quốc Việt, Hà Nội",
    "duration": "2 ngày 1 đêm",
    "location": "Trạm Tấu, Yên Bái",
    "altitude": "2.979m",
    "trekDistance": "Khoảng 16 km",
    "difficultyLevel": 3,
    "difficultyText": "Trung bình - Thử thách",
    "isFeatured": False,
    "reviews": 142,
    "shortSummary": "Chinh phục đỉnh Tà Chì Nhù 2.979m – ngọn núi của gió, mây và đồi hoa tím Chi Pâu bạt ngàn.",
    "routeMap": "Từ Hà Nội đi thị xã Nghĩa Lộ rồi vào Mỏ Chì (huyện Trạm Tấu, Yên Bái). Tuyến trek dốc liên tục nhưng thoáng đãng, mở ra tầm nhìn đại dương mây cuồn cuộn và đồi hoa Chi Pâu tím biếc.",
    "routeSteps": ["Hà Nội", "Nghĩa Lộ", "Mỏ Chì Trạm Tấu", "Lán 2.400m", "Đỉnh Tà Chì Nhù (2.979m)"],
    "historyStory": "Tà Chì Nhù (còn gọi là Phu Song Sung) cao 2.979m, là đỉnh núi cao thứ 7 tại Việt Nam. Nơi đây được ví như 'vương quốc mây và hoa' nhờ không gian lộng gió và những triền đồi hoa Chi Pâu tím ngắt nở rộ vào mùa thu đông.",
    "description": "Chiêm ngưỡng đồi hoa tím Chi Pâu nở bạt ngàn khắp các sườn núi và đón hoàng hôn biển mây ngoạn mục bậc nhất miền Bắc.",
    "departureDates": ["22/11/2026", "29/11/2026", "06/12/2026", "13/12/2026"],
    "highlights": [
      "Đắm chìm giữa thảo nguyên hoa tím Chi Pâu nở rực khắp các triền đồi.",
      "Ngắm hoàng hôn và bình minh biển mây 360 độ từ đỉnh chóp inox 2.979m.",
      "Trải nghiệm tắm khoáng nóng tự nhiên Trạm Tấu sau khi xuống núi."
    ],
    "itinerary": [
      { "day": "Ngày 0", "title": "Hà Nội – Trạm Tấu", "desc": "19:00 xe đón tại Hà Nội đi Nghĩa Lộ. Nghỉ đêm tại Trạm Tấu." },
      { "day": "Ngày 1", "title": "Mỏ Chì – Lán 2.400m", "desc": "Trekking men theo sườn núi dốc ngắm mây và hoa Chi Pâu. 16:30 đến lán nghỉ ngắm hoàng hôn, ăn lẩu nóng." },
      { "day": "Ngày 2", "title": "Chạm đỉnh 2.979m – Tắm khoáng nóng", "desc": "05:00 chạm đỉnh Tà Chì Nhù đón bình minh. Xuống núi tắm suối khoáng nóng Trạm Tấu thư giãn, về lại Hà Nội." }
    ],
    "included": [
      "Xe ô tô giường nằm khứ hồi Hà Nội – Trạm Tấu",
      "Vé tắm khoáng nóng tự nhiên Trạm Tấu",
      "Lán nghỉ trên núi, túi ngủ và chăn ấm",
      "Porter bản địa & Leader nhiều kinh nghiệm",
      "Huy chương gỗ Tà Chì Nhù độc quyền",
      "Bảo hiểm du lịch trọn gói 100.000.000đ"
    ],
    "preparation": ["Giày trekking bám tốt", "Áo gió chống gió mạnh", "Mũ tai bèo, kính râm", "CCCD bản gốc"]
  },

  # TOUR 6: LẢO THẨN – NÓC NHÀ Y TÝ (LT01)
  {
    "id": 6,
    "code": "LT01",
    "title": "Lảo Thần – Nóc nhà Y Tý (2.860m)",
    "category": "trekking",
    "subCategory": "trekking",
    "badge": "Săn mây Y Tý",
    "altitudeBadge": "Đỉnh 2.860m",
    "image": "assets/images/tour-y-ty.jpg",
    "price": "3.000.000đ/người",
    "priceNum": 3000000,
    "agencyPrice": "2.700.000đ",
    "minPax": "Từ 5 khách",
    "departureFrequency": "Thứ 7 - Chủ Nhật hàng tuần",
    "pickupPoint": "55 Nguyễn Quốc Trị & 489 Hoàng Quốc Việt, Hà Nội",
    "duration": "2 ngày 1 đêm",
    "location": "Bát Xát, Lào Cai",
    "altitude": "2.860m",
    "trekDistance": "Khoảng 16 km",
    "difficultyLevel": 2,
    "difficultyText": "Nhẹ - Trung bình (Rất dễ đi)",
    "isFeatured": False,
    "reviews": 110,
    "shortSummary": "Cung leo núi 'quốc dân' cực chill, ngắm bình minh trên biển mây bồng bềnh và check-in mỏm đá câu cá Y Tý.",
    "routeMap": "Từ Hà Nội đi thị trấn Sapa rồi di chuyển lên xã vùng cao Y Tý (Bát Xát). Tuyến leo thoai thoải qua đồi cây cháy, lán người Mông và sống núi thoai thoải lên chóp inox 2.860m.",
    "routeSteps": ["Hà Nội", "Sapa", "Y Tý", "Lán nghỉ A Hờ", "Mỏm đá Câu Cá", "Đỉnh Lảo Thần (2.860m)"],
    "historyStory": "Lảo Thần cao 2.860m được xem là 'nóc nhà của vùng đất sương mù Y Tý'. Địa hình cung này thoai thoải, đường mòn rõ ràng nên là lựa chọn số 1 cho người mới bắt đầu bước chân vào bộ môn trekking leo núi.",
    "description": "Cung trekking nhẹ nhàng, lãng mạn với biển mây tràn thung lũng, hoàng hôn rực rỡ và sao trời ngút ngàn đêm trên núi.",
    "departureDates": ["01/11/2026", "08/11/2026", "15/11/2026", "22/11/2026"],
    "highlights": [
      "Check-in Mỏm đá Câu cá và Cây cầu gỗ vươn ra biển mây huyền ảo.",
      "Ngắm biển mây lúc hoàng hôn và bình minh đẹp nhất vùng rẻo cao Y Tý.",
      "Thưởng thức gà nướng xôi ngũ sắc bên bếp lửa bập bùng cùng đồng bào Mông."
    ],
    "itinerary": [
      { "day": "Ngày 0", "title": "Hà Nội – Sapa – Y Tý", "desc": "21:30 đón tại Hà Nội đi Lào Cai trên xe giường nằm êm ái." },
      { "day": "Ngày 1", "title": "Y Tý – Lán A Hờ (Trek 8km)", "desc": "Ăn sáng tại Y Tý, bắt đầu trek qua rừng thảo quả lên lán. Chiều săn mây hoàng hôn đỏ rực." },
      { "day": "Ngày 2", "title": "Chạm đỉnh Lảo Thần 2.860m – Hà Nội", "desc": "05:00 đón bình minh trên đỉnh chóp inox. Xuống núi tắm lá thuốc Dao đỏ Sapa, lên xe về Hà Nội." }
    ],
    "included": [
      "Xe giường nằm khứ hồi Hà Nội – Sapa – Y Tý",
      "Lán gỗ ngủ trên núi đầy đủ chăn ấm",
      "Leader Đi Cùng Gió & Porter bản địa tận tâm",
      "Huy chương gỗ lưu niệm độc quyền",
      "Bảo hiểm du lịch 100.000.000đ/người"
    ],
    "preparation": ["Giày thể thao êm chân", "Áo ấm, khăn quàng", "CCCD bản gốc"]
  },

  # TOUR 7: LÙNG CÚNG (LC01)
  {
    "id": 7,
    "code": "LC01",
    "title": "Lùng Cúng – Cung đường đỗ quyên Tú Lệ (2.913m)",
    "category": "trekking",
    "subCategory": "trekking",
    "badge": "Đỉnh 2.913m",
    "altitudeBadge": "Đỉnh 2.913m",
    "image": "assets/images/tour-lung-cung.jpg",
    "price": "2.800.000đ/người",
    "priceNum": 2800000,
    "agencyPrice": "2.500.000đ",
    "minPax": "Từ 5 khách",
    "departureFrequency": "Thứ 7 - Chủ Nhật hàng tuần",
    "pickupPoint": "55 Nguyễn Quốc Trị & 489 Hoàng Quốc Việt, Hà Nội",
    "duration": "2 ngày 2 đêm",
    "location": "Mù Cang Chải, Yên Bái",
    "altitude": "2.913m",
    "trekDistance": "Khoảng 18 km",
    "difficultyLevel": 3,
    "difficultyText": "Trung bình",
    "isFeatured": False,
    "reviews": 88,
    "shortSummary": "Chinh phục ngọn núi bí ẩn của người Thái bản Tu San, đón gió trên bãi cỏ bạt ngàn tại đỉnh Lùng Cúng 2.913m.",
    "routeMap": "Từ Hà Nội đi thị trấn Tú Lệ, rẽ vào bản Tu San (Mù Cang Chải). Tuyến trek xuyên qua những cánh rừng hạt dẻ cổ thụ, rừng trúc xanh ngút ngàn và triền đồi hoa đỗ quyên rực rỡ.",
    "routeSteps": ["Hà Nội", "Tú Lệ", "Bản Tu San", "Rừng trúc cổ", "Lán nghỉ", "Đỉnh Lùng Cúng (2.913m)"],
    "historyStory": "Lùng Cúng được đặt tên theo bản làng hẻo lánh dưới chân núi. Đỉnh núi cao 2.913m với thảo nguyên cỏ bằng phẳng trên đỉnh, mang lại tầm nhìn bao quát toàn bộ thung lũng Mù Cang Chải và ruộng bậc thang kỳ vĩ.",
    "description": "Hành trình hoang sơ chạm vào trái tim đại ngàn Mù Cang Chải, thưởng thức xôi nếp nương Tú Lệ thơm dẻo.",
    "departureDates": ["01/11/2026", "08/11/2026", "15/11/2026", "22/11/2026"],
    "highlights": [
      "Đứng trên thảo nguyên cỏ bao la lộng gió tại đỉnh chóp 2.913m.",
      "Băng qua khu rừng trúc thẳng tắp huyền ảo như phim kiếm hiệp.",
      "Thưởng thức đặc sản nếp nương Tú Lệ và lợn bản nướng thơm phức."
    ],
    "itinerary": [
      { "day": "Đêm 0", "title": "Hà Nội – Tú Lệ", "desc": "19:00 xuất phát từ 55 Nguyễn Quốc Trị & 489 Hoàng Quốc Việt đi Tú Lệ. Nghỉ đêm homestay." },
      { "day": "Ngày 1", "title": "Bản Tu San – Lán nghỉ 2.400m", "desc": "Trek qua rừng trúc, rừng thảo quả và suối trong. Chiều đến lán nghỉ ngắm hoàng hôn mây bồng bềnh." },
      { "day": "Ngày 2", "title": "Chạm đỉnh Lùng Cúng 2.913m – Hà Nội", "desc": "Sáng sớm chạm đỉnh ngắm bình minh 360 độ. Xuống núi về Tú Lệ, ăn trưa và lên xe về Hà Nội." }
    ],
    "included": [
      "Xe ô tô giường nằm khứ hồi Hà Nội – Tú Lệ",
      "Lán nghỉ trên núi, túi ngủ ấm",
      "Porter bản địa & Leader theo sát chăm sóc",
      "Huy chương gỗ Lùng Cúng độc quyền",
      "Bảo hiểm du lịch 100.000.000đ/người"
    ],
    "preparation": ["Giày leo núi có gai", "Áo gió giữ ấm", "CCCD bản gốc"]
  },

  # TOUR 8: NHÌU CỒ SAN (NCS01)
  {
    "id": 8,
    "code": "NCS01",
    "title": "Nhìu Cồ San – Thác Ong Chúa (2.965m)",
    "category": "trekking",
    "subCategory": "trekking",
    "badge": "Đỉnh 2.965m",
    "altitudeBadge": "Đỉnh 2.965m",
    "image": "assets/images/tour-nhiu-co-san.jpg",
    "price": "2.800.000đ/người",
    "priceNum": 2800000,
    "agencyPrice": "2.700.000đ",
    "minPax": "Từ 5 khách",
    "departureFrequency": "Thứ 7 - Chủ Nhật hàng tuần",
    "pickupPoint": "55 Nguyễn Quốc Trị & 489 Hoàng Quốc Việt, Hà Nội",
    "duration": "2 ngày 2 đêm",
    "location": "Bát Xát, Lào Cai",
    "altitude": "2.965m",
    "trekDistance": "Khoảng 16 km",
    "difficultyLevel": 3,
    "difficultyText": "Trung bình",
    "isFeatured": False,
    "reviews": 76,
    "shortSummary": "Chinh phục đỉnh núi Sừng Trâu hoang dã, chiêm ngưỡng Thác Ong Chúa tuyệt mỹ và rừng thảo quả ngát hương.",
    "routeMap": "Từ Hà Nội qua Sapa đến bản Nhìu Cồ San (Bát Xát). Cung đường đưa bạn qua Thác Ong Chúa kỳ vĩ tung bọt trắng xóa, xuyên rừng đỗ quyên và rừng trúc lên chóp inox 2.965m.",
    "routeSteps": ["Hà Nội", "Sapa", "Bản Nhìu Cồ San", "Thác Ong Chúa", "Lán nghỉ", "Đỉnh Nhìu Cồ San (2.965m)"],
    "historyStory": "Nhìu Cồ San theo tiếng người H’Mông có nghĩa là 'núi ba sừng trâu'. Với độ cao 2.965m (top 9 ngọn núi cao nhất Việt Nam), nơi đây còn lưu giữ con đường đá cổ Pavi thời Pháp thuộc chạy xuyên qua đại ngàn.",
    "description": "Cung leo núi giàu trải nghiệm thiên nhiên với thác nước tuyệt đẹp, khu rừng nguyên sinh rêu phong và đỉnh cao lộng gió.",
    "departureDates": ["01/11/2026", "08/11/2026", "15/11/2026", "22/11/2026"],
    "highlights": [
      "Chiêm ngưỡng Thác Ong Chúa hùng vĩ tuôn dòng nước mát lạnh giữa vách đá dựng đứng.",
      "Check-in chóp inox 2.965m ngắm trọn vẹn dải Hoàng Liên Sơn mờ ảo trong mây.",
      "Tắm lá thuốc người Dao đỏ tại Sapa hồi phục sức khỏe sau chuyến đi."
    ],
    "itinerary": [
      { "day": "Đêm 0", "title": "Hà Nội – Sapa – Bát Xát", "desc": "21:30 xe giường nằm đón tại 55 Nguyễn Quốc Trị & 489 Hoàng Quốc Việt đi Lào Cai." },
      { "day": "Ngày 1", "title": "Bản Nhìu Cồ San – Thác Ong Chúa – Lán", "desc": "Check-in Thác Ong Chúa tráng lệ, vượt rừng rêu và đỗ quyên lên lán nghỉ ngơi." },
      { "day": "Ngày 2", "title": "Chạm đỉnh 2.965m – Tắm lá thuốc – Hà Nội", "desc": "Đón bình minh trên đỉnh núi, xuống chân núi tắm lá thuốc Dao đỏ Sapa, lên xe về Hà Nội lúc 21:00." }
    ],
    "included": [
      "Xe giường nằm khứ hồi Hà Nội – Lào Cai",
      "Lán ngủ trên núi có túi ngủ ấm",
      "Porter bản địa & Leader chu đáo",
      "Tắm lá thuốc người Dao đỏ",
      "Huy chương gỗ Nhìu Cồ San kỷ niệm",
      "Bảo hiểm du lịch 100.000.000đ/người"
    ],
    "preparation": ["Giày trekking chống trơn", "Áo ấm, tất dài", "CCCD bản gốc"]
  },

  # TOUR 9: FANSIPAN (FSP)
  {
    "id": 9,
    "code": "FSP",
    "title": "Fansipan – Chinh phục Nóc nhà Đông Dương (3.143m)",
    "category": "trekking",
    "subCategory": "trekking",
    "badge": "Nóc nhà Đông Dương",
    "altitudeBadge": "Đỉnh 3.143m",
    "image": "assets/images/tour-fansipan.jpg",
    "price": "3.000.000đ/người",
    "priceNum": 3000000,
    "agencyPrice": "2.700.000đ",
    "minPax": "Từ 5 khách",
    "departureFrequency": "Thứ 7 - Chủ Nhật hàng tuần",
    "pickupPoint": "55 Nguyễn Quốc Trị & 489 Hoàng Quốc Việt, Hà Nội",
    "duration": "2 ngày 1 đêm",
    "location": "Sapa, Lào Cai",
    "altitude": "3.143m",
    "trekDistance": "Khoảng 24 km",
    "difficultyLevel": 4,
    "difficultyText": "Thử thách thể lực",
    "isFeatured": False,
    "reviews": 160,
    "shortSummary": "Hành trình tự thân leo bộ chinh phục đỉnh Fansipan 3.143m kiêu hãnh – cột mốc lịch sử của mọi trekker Việt Nam.",
    "routeMap": "Từ Hà Nội lên thị xã Sapa. Xuất phát từ Trạm Tôn (1.900m), men theo rừng trúc và khe suối lên lán 2.800m nghỉ đêm, sáng sớm vượt dốc đá dựng đứng chạm chóp inox 3.143m.",
    "routeSteps": ["Hà Nội", "Sapa", "Trạm Tôn (1.900m)", "Lán 2.800m", "Đỉnh Fansipan (3.143m)"],
    "historyStory": "Fansipan cao 3.143m là ngọn núi cao nhất ba nước Việt Nam – Lào – Campuchia, được xưng tụng là 'Nóc nhà Đông Dương'. Chinh phục Fansipan bằng chính đôi chân mình trên cung đường Trạm Tôn là niềm tự hào của hàng ngàn bạn trẻ đam mê phiêu lưu.",
    "description": "Cung trekking kinh điển vượt qua giới hạn bản thân, chiêm ngưỡng quần thể tâm linh kỳ vĩ trên đỉnh mây ngàn.",
    "departureDates": ["01/11/2026", "08/11/2026", "15/11/2026", "22/11/2026"],
    "highlights": [
      "Tự hào chạm tay vào chóp inox 3.143m – Nóc nhà Đông Dương bằng chính sức lực của mình.",
      "Chiêm ngưỡng biển mây bao la và Đại tượng Phật A Di Đà sừng sững giữa trời xanh.",
      "Nhận giấy chứng nhận và huy chương chinh phục Fansipan độc quyền từ Đi Cùng Gió."
    ],
    "itinerary": [
      { "day": "Ngày 0", "title": "Hà Nội – Sapa", "desc": "21:30 xe giường nằm chất lượng cao đón tại Hà Nội đi Sapa." },
      { "day": "Ngày 1", "title": "Trạm Tôn – Lán 2.800m", "desc": "Khởi hành từ Trạm Tôn, băng qua rừng trúc và suối đá. Đến lán 2.800m nghỉ đêm, ngắm bầu trời sao rực rỡ." },
      { "day": "Ngày 2", "title": "Chạm đỉnh Fansipan 3.143m – Hà Nội", "desc": "06:00 đón bình minh trên Nóc nhà Đông Dương. Xuống núi Trạm Tôn, tắm lá thuốc Dao đỏ và về Hà Nội." }
    ],
    "included": [
      "Xe giường nằm khứ hồi Hà Nội – Sapa",
      "Giấy phép leo núi Fansipan của Vườn Quốc Gia Hoàng Liên",
      "Lán ngủ 2.800m có chăn ấm, túi ngủ",
      "Leader & Porter bản địa dày dạn kinh nghiệm",
      "Huy chương gỗ độc quyền Đi Cùng Gió",
      "Bảo hiểm du lịch 100.000.000đ/người"
    ],
    "preparation": ["Giày trekking chuyên dụng bám dốc", "Áo gió chống mưa tuyết", "Găng tay, tất dài", "CCCD bản gốc"]
  },

  # TOUR 10: NGỌA VÂN – YÊN TỬ (NV01)
  {
    "id": 10,
    "code": "NV01",
    "title": "Ngọa Vân – Thánh địa Trúc Lâm Yên Tử",
    "category": "spiritual",
    "subCategory": "trekking",
    "badge": "Tâm linh Trúc Lâm",
    "altitudeBadge": "Độ cao 800m",
    "image": "assets/images/tour-ngoa-van.jpg",
    "price": "650.000đ/người",
    "priceNum": 650000,
    "agencyPrice": "600.000đ",
    "minPax": "Từ 5 khách",
    "departureFrequency": "Thứ 7 - Chủ Nhật hàng tuần",
    "pickupPoint": "55 Nguyễn Quốc Trị & 489 Hoàng Quốc Việt, Hà Nội",
    "duration": "Trong ngày",
    "location": "Đông Triều, Quảng Ninh",
    "altitude": "800m",
    "trekDistance": "Khoảng 8 km",
    "difficultyLevel": 2,
    "difficultyText": "Nhẹ nhàng",
    "isFeatured": False,
    "reviews": 65,
    "shortSummary": "Hành hương về am thiêng Ngọa Vân – nơi Phật hoàng Trần Nhân Tông hóa Phật và nhập Niết bàn.",
    "routeMap": "Từ Hà Nội theo QL18 đi thị xã Đông Triều (Quảng Ninh). Tuyến trekking men theo rừng thông và suối xanh, qua chùa Trại Cấp, dốc Đô Kiệu và viếng Am Ngọa Vân thanh tịnh trên đỉnh mây.",
    "routeSteps": ["Hà Nội", "Đông Triều", "Chùa Trại Cấp", "Dốc Đô Kiệu", "Am Ngọa Vân"],
    "historyStory": "Am Ngọa Vân nằm trên ngọn núi Bảo Đài thuộc dãy cánh cung Đông Triều. Đây là thánh địa tối thượng của Phật giáo Trúc Lâm, nơi Phật hoàng Trần Nhân Tông tu hành những năm tháng cuối đời và viên tịch hóa Phật vào ngày 1 tháng 11 năm Mậu Thân (1308).",
    "description": "Cung hành hương thanh tịnh giữa rừng thông ngát hương, lắng nghe tiếng chuông chùa thanh thản giữa non thiêng.",
    "departureDates": ["01/11/2026", "08/11/2026", "15/11/2026", "22/11/2026"],
    "highlights": [
      "Chiêm bái Am tháp Ngọa Vân nơi Phật hoàng Trần Nhân Tông nhập Niết bàn.",
      "Dạo bước trên cung đường bậc đá rợp bóng rừng thông ngàn năm tuổi.",
      "Thưởng thức cơm chay thanh đạm và cảm nhận sự thanh thản trong tâm hồn."
    ],
    "itinerary": [
      { "day": "06:00", "title": "Hà Nội – Đông Triều", "desc": "Xe đón tại 55 Nguyễn Quốc Trị & 489 Hoàng Quốc Việt đi Đông Triều (Quảng Ninh)." },
      { "day": "08:30", "title": "Trekking Am Ngọa Vân", "desc": "Trekking qua dốc Đô Kiệu, rừng trúc và đồi thông xanh ngát." },
      { "day": "12:00", "title": "Chiêm bái & Ăn trưa", "desc": "Dâng hương tại Am Ngọa Vân trên đỉnh núi, dùng bữa trưa picnic thanh tịnh." },
      { "day": "15:30", "title": "Xuống núi về Hà Nội", "desc": "Xuống chân núi, lên xe trở về Hà Nội lúc 18:30." }
    ],
    "included": [
      "Xe ô tô đưa đón khứ hồi từ Hà Nội",
      "Hướng dẫn viên theo sát lịch trình",
      "Nước uống tinh khiết 500ml",
      "Huy chương gỗ độc quyền kỷ niệm",
      "Bảo hiểm du lịch trọn gói 20.000.000đ"
    ],
    "preparation": ["Trang phục lịch sự kín đáo", "Giày thể thao bám tốt", "CCCD bản gốc"]
  },

  # TOUR 11: NÚI THANH ĐẰNG – BA VÀNG (TĐ01)
  {
    "id": 11,
    "code": "TĐ01",
    "title": "Núi Thanh Đằng – Ba Vàng An Nhiên",
    "category": "spiritual",
    "subCategory": "near_hanoi",
    "badge": "Hành hương an lạc",
    "altitudeBadge": "Độ cao 450m",
    "image": "assets/images/tour-tam-chuc.jpg",
    "price": "500.000đ/người",
    "priceNum": 500000,
    "agencyPrice": "450.000đ",
    "minPax": "Từ 5 khách",
    "departureFrequency": "Thứ 7 - Chủ Nhật hàng tuần",
    "pickupPoint": "55 Nguyễn Quốc Trị & 489 Hoàng Quốc Việt, Hà Nội",
    "duration": "Trong ngày",
    "location": "Uông Bí, Quảng Ninh",
    "altitude": "450m",
    "trekDistance": "Khoảng 6 km",
    "difficultyLevel": 1,
    "difficultyText": "Rất nhẹ nhàng",
    "isFeatured": False,
    "reviews": 52,
    "shortSummary": "Hành hương leo núi Thanh Đằng, chiêm bái đại bảo tháp chùa Ba Vàng và ngắm toàn cảnh sông núi Uông Bí.",
    "routeMap": "Từ Hà Nội đi Uông Bí, trekking theo sườn đồi thông núi Thanh Đằng thoai thoải, viếng thăm chùa Ba Vàng và dạo bước an lạc giữa thiên nhiên.",
    "routeSteps": ["Hà Nội", "Uông Bí", "Chân núi Thanh Đằng", "Chùa Ba Vàng", "Đỉnh đồi thông"],
    "historyStory": "Núi Thanh Đằng tọa lạc tại vị trí phong thủy đắc địa 'tiền hữu ngoạn thủy, hậu hữu ỷ sơn'. Đây là vùng đất tâm linh thanh bình nằm kề bên quần thể di tích danh thắng Yên Tử.",
    "description": "Chuyến đi trong ngày nhẹ nhàng phù hợp mọi lứa tuổi, kết hợp rèn luyện sức khỏe và hành hương thanh tịnh.",
    "departureDates": ["01/11/2026", "08/11/2026", "15/11/2026", "22/11/2026"],
    "highlights": [
      "Chiêm bái ngôi chùa có tòa Chính điện trên núi lớn nhất Việt Nam.",
      "Dạo bước giữa rừng thông thơ mộng ngắm thành phố Uông Bí từ trên cao.",
      "Thưởng thức các món chay thanh lọc cơ thể và tâm trí."
    ],
    "itinerary": [
      { "day": "06:30", "title": "Hà Nội – Uông Bí", "desc": "Đón khách tại 55 Nguyễn Quốc Trị & 489 Hoàng Quốc Việt khởi hành đi Uông Bí." },
      { "day": "09:00", "title": "Trekking núi Thanh Đằng", "desc": "Băng qua đồi thông xanh ngát, hít thở không khí thanh trong." },
      { "day": "12:00", "title": "Chiêm bái & Nghỉ trưa", "desc": "Dâng hương lễ Phật tại chùa Ba Vàng, dùng bữa cơm trưa thanh tịnh." },
      { "day": "15:00", "title": "Về lại Hà Nội", "desc": "Lên xe khởi hành về Hà Nội, kết thúc chuyến đi lúc 18:00." }
    ],
    "included": ["Xe đưa đón khứ hồi", "HDV theo sát", "Nước uống & Bữa trưa chay", "Bảo hiểm du lịch"],
    "preparation": ["Trang phục trang nhã", "Giày êm", "CCCD bản gốc"]
  },

  # TOUR 12: THÀNH ĐẲNG + PHƯỢNG HOÀNG (TĐPH)
  {
    "id": 12,
    "code": "TĐPH",
    "title": "Thành Đẳng + Đồi Cỏ Cháy Phượng Hoàng",
    "category": "spiritual",
    "subCategory": "experience",
    "badge": "Tâm linh & Cỏ cháy",
    "altitudeBadge": "Độ cao 500m",
    "image": "assets/images/tour-chua-huong.jpg",
    "price": "750.000đ/người",
    "priceNum": 750000,
    "agencyPrice": "700.000đ",
    "minPax": "Từ 5 khách",
    "departureFrequency": "Thứ 7 - Chủ Nhật hàng tuần",
    "pickupPoint": "55 Nguyễn Quốc Trị & 489 Hoàng Quốc Việt, Hà Nội",
    "duration": "Trong ngày",
    "location": "Uông Bí, Quảng Ninh",
    "altitude": "500m",
    "trekDistance": "Khoảng 8 km",
    "difficultyLevel": 2,
    "difficultyText": "Nhẹ nhàng",
    "isFeatured": False,
    "reviews": 48,
    "shortSummary": "Hành trình kết hợp chiêm bái tâm linh Thành Đẳng và check-in đồi cỏ cháy Phượng Hoàng đẹp như thảo nguyên Mông Cổ.",
    "routeMap": "Từ Hà Nội đi Uông Bí, hành hương chiêm bái Thành Đẳng buổi sáng, buổi chiều trekking chinh phục Đồi Phượng Hoàng với thảo nguyên cỏ vàng óng ánh.",
    "routeSteps": ["Hà Nội", "Uông Bí", "Thành Đẳng", "Đồi Phượng Hoàng", "Thảo nguyên cỏ cháy"],
    "historyStory": "Đồi Phượng Hoàng được mệnh danh là 'thảo nguyên Đà Lạt thu nhỏ' của Quảng Ninh. Mùa thu đông, những triền cỏ chuyển sang màu vàng cháy thơ mộng tạo nên khung cảnh lãng mạn vô cùng cuốn hút.",
    "description": "Chuyến trekking check-in sống ảo cực đẹp kết hợp viếng cảnh chùa thanh tịnh trong một ngày cuối tuần.",
    "departureDates": ["01/11/2026", "08/11/2026", "15/11/2026", "22/11/2026"],
    "highlights": [
      "Check-in đồi cỏ cháy Phượng Hoàng ngút ngàn đẹp ngỡ ngàng.",
      "Hành hương chiêm bái cầu bình an, may mắn cho gia đình.",
      "Chụp những bức ảnh kỷ niệm tuyệt đẹp giữa thảo nguyên mộng mơ."
    ],
    "itinerary": [
      { "day": "06:00", "title": "Hà Nội – Uông Bí", "desc": "Xuất phát từ Hà Nội đi Uông Bí." },
      { "day": "09:00", "title": "Chiêm bái Thành Đẳng", "desc": "Hành hương lễ Phật cầu bình an giữa không gian thanh tịnh." },
      { "day": "13:30", "title": "Trekking Đồi Phượng Hoàng", "desc": "Chinh phục đỉnh đồi, ngắm toàn cảnh thung lũng cỏ cháy vàng rực lúc hoàng hôn." },
      { "day": "16:30", "title": "Về Hà Nội", "desc": "Lên xe về lại thủ đô lúc 19:30." }
    ],
    "included": ["Xe đưa đón khứ hồi", "Leader Đi Cùng Gió", "Nước uống, đồ y tế", "Huy chương gỗ độc quyền", "Bảo hiểm du lịch"],
    "preparation": ["Trang phục màu nổi bật chụp ảnh", "Giày thể thao", "CCCD bản gốc"]
  },

  # TOUR 13: ĐÀ GIANG – HÒA BÌNH (DG01)
  {
    "id": 13,
    "code": "DG01",
    "title": "Đà Giang Hòa Bình – Vịnh Ngòi Hoa & Hồ Mắt Ngọc",
    "category": "experience",
    "subCategory": "experience",
    "badge": "Hồ Mắt Ngọc",
    "altitudeBadge": "Lòng hồ Đà Giang",
    "image": "assets/images/tour-da-giang.jpg",
    "price": "790.000đ/người",
    "priceNum": 790000,
    "agencyPrice": "700.000đ",
    "minPax": "Từ 5 khách",
    "departureFrequency": "Thứ 7 - Chủ Nhật hàng tuần",
    "pickupPoint": "55 Nguyễn Quốc Trị & 489 Hoàng Quốc Việt, Hà Nội",
    "duration": "Trong ngày",
    "location": "Tân Lạc, Hòa Bình",
    "altitude": "Mặt hồ sông Đà",
    "trekDistance": "Khoảng 6 km trek + Chèo thuyền",
    "difficultyLevel": 1,
    "difficultyText": "Nhẹ nhàng - Trải nghiệm nước",
    "isFeatured": False,
    "reviews": 79,
    "shortSummary": "Du ngoạn vịnh Ngòi Hoa trên hồ Hòa Bình xanh biếc, khám phá Hồ Mắt Ngọc bí ẩn và hang động thạch nhũ kỳ vĩ.",
    "routeMap": "Từ Hà Nội đi cảng Ngòi Hoa (Tân Lạc, Hòa Bình). Lên thuyền du ngoạn ngắm các đảo đá vôi xanh ngọc, trekking nhẹ vào bản người Mường và khám phá Hồ Mắt Ngọc tuyệt đẹp.",
    "routeSteps": ["Hà Nội", "TP Hòa Bình", "Cảng Ngòi Hoa", "Du thuyền lòng hồ", "Hồ Mắt Ngọc & Hang thạch nhũ"],
    "historyStory": "Lòng hồ sông Đà được ví như 'Vịnh Hạ Long trên cạn của miền Tây Bắc'. Nơi đây nổi tiếng với phong cảnh sơn thủy hữu tình, dòng nước trong xanh như ngọc bích và bản sắc văn hóa Mường đặc sắc.",
    "description": "Một ngày trốn khói bụi thủ đô, hòa mình vào làn nước mát lành và thiên nhiên non xanh nước biếc của dòng sông Đà huyền thoại.",
    "departureDates": ["01/11/2026", "08/11/2026", "15/11/2026", "22/11/2026"],
    "highlights": [
      "Du thuyền lướt trên mặt hồ xanh ngắt giữa trập trùng đảo đá vôi hoang sơ.",
      "Khám phá Hồ Mắt Ngọc nước trong nhìn thấu đáy và hang thạch nhũ kỳ ảo.",
      "Thưởng thức cá nướng sông Đà và gà đồi thơm lừng tại nhà bè nổi."
    ],
    "itinerary": [
      { "day": "05:00", "title": "Hà Nội – TP Hòa Bình – Cảng Ngòi Hoa", "desc": "Xe đón tại 55 Nguyễn Quốc Trị & 489 Hoàng Quốc Việt đi Hòa Bình. Ăn sáng tại TP Hòa Bình." },
      { "day": "08:30", "title": "Du thuyền vịnh Ngòi Hoa", "desc": "Lên thuyền ngắm vịnh Ngòi Hoa, chèo SUP trên mặt nước xanh ngọc." },
      { "day": "11:30", "title": "Ăn trưa cá sông Đà & Khám phá Hồ Mắt Ngọc", "desc": "Ăn trưa đặc sản vùng hồ. Buổi chiều trekking khám phá hang động thạch nhũ và Hồ Mắt Ngọc." },
      { "day": "16:00", "title": "Về lại Hà Nội", "desc": "Lên xe về lại thủ đô, kết thúc hành trình lúc 19:00." }
    ],
    "included": [
      "Xe ô tô du lịch đời mới khứ hồi",
      "Thuyền tham quan chuyên dụng trên hồ Hòa Bình",
      "Bữa ăn trưa đặc sản cá sông Đà tươi ngon",
      "Leader & Áo phao an toàn tuyệt đối",
      "Huy chương gỗ kỷ niệm độc quyền",
      "Bảo hiểm du lịch 20.000.000đ"
    ],
    "preparation": ["Quần áo dự phòng thay khi tắm hồ", "Kem chống nắng", "CCCD bản gốc"]
  },

  # TOUR 14: SUỐI CỬA TỬ – THÁI NGUYÊN (CT01)
  {
    "id": 14,
    "code": "CT01",
    "title": "Trekking Suối Cửa Tử – Thái Nguyên (Khứ Hồi Hà Nội)",
    "category": "experience",
    "subCategory": "near_hanoi",
    "badge": "Vượt thác suối",
    "altitudeBadge": "Khu bảo tồn Đại Từ",
    "image": "assets/images/tour-cua-tu.jpg",
    "price": "850.000đ/người",
    "priceNum": 850000,
    "agencyPrice": "800.000đ",
    "minPax": "Từ 5 khách",
    "departureFrequency": "Thứ 7 - Chủ Nhật hàng tuần",
    "pickupPoint": "55 Nguyễn Quốc Trị & 489 Hoàng Quốc Việt, Hà Nội",
    "duration": "Trong ngày",
    "location": "Đại Từ, Thái Nguyên",
    "altitude": "Chân núi Tam Đảo",
    "trekDistance": "Khoảng 8 – 10 km lội suối",
    "difficultyLevel": 2,
    "difficultyText": "Trung bình - Lội nước thú vị",
    "isFeatured": False,
    "reviews": 103,
    "shortSummary": "Lội suối băng rừng nguyên sinh Đại Từ, trượt máng đá tự nhiên và nhảy thác mát lạnh tại suối Cửa Tử.",
    "routeMap": "Từ Hà Nội theo cao tốc Hà Nội – Thái Nguyên đến chân suối Cửa Tử (xã Hoàng Nông, Đại Từ). Tuyến trekking lội dọc dòng suối đá trong vắt, vượt Cửa 1, Cửa 2 và Cửa 3 với những thác nước tuyệt mỹ.",
    "routeSteps": ["Hà Nội", "Đại Từ (Thái Nguyên)", "Cửa 1 (Máng trượt đá)", "Cửa 2 (Bể bơi tự nhiên)", "Cửa 3 (Thác nước đại ngàn)"],
    "historyStory": "Suối Cửa Tử bắt nguồn từ sườn Đông dãy Tam Đảo chảy xuống thung lũng Hoàng Nông. Dòng nước mát lạnh quanh năm chảy len lỏi qua những khối đá cuội khổng lồ và rừng cây cổ thụ nhiệt đới xanh rì.",
    "description": "Trải nghiệm vượt suối tắm thác cực sảng khoái và xua tan mọi căng thẳng oi bức của mùa hè miền Bắc.",
    "departureDates": ["01/11/2026", "08/11/2026", "15/11/2026", "22/11/2026"],
    "highlights": [
      "Trượt máng đá tự nhiên dài hàng chục mét trút thẳng xuống làn nước trong vắt.",
      "Bơi lội thỏa thích giữa các hồ nước tự nhiên xanh biếc như ngọc bích.",
      "Thưởng thức gà nướng lá móc mật và chè búp Tân Cương Thái Nguyên thơm lừng."
    ],
    "itinerary": [
      { "day": "05:30", "title": "Hà Nội – Đại Từ Thái Nguyên", "desc": "Đón đoàn tại 55 Nguyễn Quốc Trị & 489 Hoàng Quốc Việt đi Thái Nguyên." },
      { "day": "08:30", "title": "Bắt đầu trek lội suối Cửa Tử", "desc": "Trang bị áo phao, khởi động và bắt đầu lội dọc con suối đá hoang sơ." },
      { "day": "12:00", "title": "Ăn trưa picnic bên bờ suối", "desc": "Ăn trưa thịt nướng, xôi nếp nóng hổi bên bờ thác róc rách." },
      { "day": "14:00", "title": "Trượt máng đá Cửa 2 & Nhảy thác", "desc": "Trải nghiệm trượt máng đá tự nhiên cảm giác mạnh cực vui." },
      { "day": "16:30", "title": "Về lại Hà Nội", "desc": "Tắm tráng nước ngọt, lên xe về lại thủ đô lúc 19:00." }
    ],
    "included": [
      "Xe đưa đón khứ hồi Hà Nội – Cửa Tử",
      "Áo phao an toàn cá nhân & Túi chống nước",
      "Porter bản địa & Leader nhiều kinh nghiệm suối",
      "Bữa ăn trưa nóng sốt bên bờ thác",
      "Huy chương gỗ độc quyền của Đi Cùng Gió",
      "Bảo hiểm du lịch trọn gói 20.000.000đ"
    ],
    "preparation": ["Giày lội suối hoặc quai hậu bám đá", "2 bộ quần áo khô thay", "Túi chống nước điện thoại", "CCCD bản gốc"]
  },

  # TOUR 15: CÚC PHƯƠNG MÙA BƯỚM (CP01)
  {
    "id": 15,
    "code": "CP01",
    "title": "Vườn Quốc Gia Cúc Phương – Mùa Bướm Rực Rỡ",
    "category": "experience",
    "subCategory": "near_hanoi",
    "badge": "Mùa bướm rừng già",
    "altitudeBadge": "Rừng quốc gia Cúc Phương",
    "image": "assets/images/tour-cuc-phuong.jpg",
    "price": "550.000đ/người",
    "priceNum": 550000,
    "agencyPrice": "500.000đ",
    "minPax": "Từ 5 khách",
    "departureFrequency": "Thứ 7 - Chủ Nhật hàng tuần",
    "pickupPoint": "55 Nguyễn Quốc Trị & 489 Hoàng Quốc Việt, Hà Nội",
    "duration": "Trong ngày",
    "location": "Nho Quan, Ninh Bình",
    "altitude": "Rừng nhiệt đới",
    "trekDistance": "Khoảng 7 km",
    "difficultyLevel": 1,
    "difficultyText": "Rất nhẹ nhàng",
    "isFeatured": False,
    "reviews": 89,
    "shortSummary": "Lạc bước giữa hàng vạn cánh bướm rợp trời, chiêm bái Cây Chò ngàn năm tuổi giữa rừng già Cúc Phương.",
    "routeMap": "Từ Hà Nội theo QL1A đi Nho Quan (Ninh Bình). Tuyến trekking xuyên qua lối mòn rừng già rợp bóng cây cổ thụ, viếng Động Người Xưa và Cây Chò chỉ ngàn năm tuổi.",
    "routeSteps": ["Hà Nội", "Cổng Vườn Cúc Phương", "Động Người Xưa", "Rừng nguyên sinh mùa bướm", "Cây Chò ngàn năm"],
    "historyStory": "Cúc Phương là vườn quốc gia đầu tiên tại Việt Nam, thành lập năm 1962. Nơi đây bảo tồn hệ động thực vật nhiệt đới vô cùng phong phú và nổi tiếng thế giới với mùa bướm hàng triệu con bay rợp trời vào mỗi độ đầu hạ.",
    "description": "Chuyến dã ngoại rừng già trong lành, khám phá thiên nhiên hoang dã kỳ thú phù hợp cả gia đình và trẻ nhỏ.",
    "departureDates": ["01/11/2026", "08/11/2026", "15/11/2026", "22/11/2026"],
    "highlights": [
      "Ngắm nhìn hàng triệu cánh bướm trắng, vàng bay rợp các con đường mòn xuyên rừng.",
      "Ôm thân Cây Chò ngàn năm tuổi sừng sững giữa lõi rừng nguyên sinh.",
      "Tham quan Trung tâm Cứu hộ Linh trưởng Quý hiếm hàng đầu Đông Nam Á."
    ],
    "itinerary": [
      { "day": "06:00", "title": "Hà Nội – Ninh Bình", "desc": "Xe đón tại 55 Nguyễn Quốc Trị & 489 Hoàng Quốc Việt đi VQG Cúc Phương." },
      { "day": "08:30", "title": "Trekking xuyên rừng & Săn bướm", "desc": "Check-in ngắm hàng đàn bướm bay rực rỡ, viếng Động Người Xưa." },
      { "day": "12:00", "title": "Ăn trưa đặc sản Ninh Bình", "desc": "Ăn trưa cơm cháy, dê núi tại nhà hàng trong rừng." },
      { "day": "14:00", "title": "Chinh phục Cây Chò ngàn năm", "desc": "Trekking 3km đường mòn ngắm Cây Chò đại thụ." },
      { "day": "16:00", "title": "Về lại Hà Nội", "desc": "Lên xe về lại thủ đô lúc 18:30." }
    ],
    "included": [
      "Xe ô tô đưa đón khứ hồi Hà Nội – Cúc Phương",
      "Vé vào cổng Vườn Quốc Gia Cúc Phương",
      "Leader hướng dẫn khám phá sinh thái",
      "Bữa ăn trưa đặc sản Ninh Bình thơm ngon",
      "Bảo hiểm du lịch trọn gói 20.000.000đ"
    ],
    "preparation": ["Trang phục thoải mái, chống muỗi", "Giày thể thao", "CCCD bản gốc"]
  },

  # TOUR 16: BA VÌ (BV01)
  {
    "id": 16,
    "code": "BV01",
    "title": "Trekking Vườn Quốc Gia Ba Vì – Rừng Thông & Đền Thượng",
    "category": "near_hanoi",
    "subCategory": "near_hanoi",
    "badge": "Trốn phố về rừng",
    "altitudeBadge": "Độ cao 1.296m",
    "image": "assets/images/tour-ba-vi.jpg",
    "price": "750.000đ/người",
    "priceNum": 750000,
    "agencyPrice": "700.000đ",
    "minPax": "Từ 5 khách",
    "departureFrequency": "Thứ 7 - Chủ Nhật hàng tuần",
    "pickupPoint": "55 Nguyễn Quốc Trị & 489 Hoàng Quốc Việt, Hà Nội",
    "duration": "Trong ngày",
    "location": "Ba Vì, Hà Nội",
    "altitude": "1.296m",
    "trekDistance": "Khoảng 8 km",
    "difficultyLevel": 2,
    "difficultyText": "Nhẹ nhàng",
    "isFeatured": False,
    "reviews": 112,
    "shortSummary": "Trekking xuyên rừng thông bạt ngàn, khám phá Nhà Thờ Đổ Pháp cổ kính và chạm đỉnh Vua 1.296m.",
    "routeMap": "Từ nội thành Hà Nội đi Vườn Quốc Gia Ba Vì (60km). Tuyến trek qua rừng thông cốt 400, viếng Nhà Thờ Đổ rêu phong ma mị và leo bậc đá lên Đền Thượng thờ Tản Viên Sơn Thánh.",
    "routeSteps": ["Hà Nội", "Cổng VQG Ba Vì", "Rừng thông Cốt 400", "Nhà Thờ Đổ cổ kính", "Đỉnh Vua (1.296m)"],
    "historyStory": "Dãy núi Ba Vì gắn liền với truyền thuyết Sơn Tinh – Thủy Tinh bất hủ trong tâm thức người Việt. Nơi đây có khí hậu á nhiệt đới mát mẻ quanh năm cùng những công trình kiến trúc Pháp cổ kính phủ đầy rêu phong.",
    "description": "Cung trekking gần gũi nhất với Hà Nội, không khí trong lành như Đà Lạt, thích hợp nạp lại năng lượng sau tuần làm việc bận rộn.",
    "departureDates": ["01/11/2026", "08/11/2026", "15/11/2026", "22/11/2026"],
    "highlights": [
      "Check-in Nhà Thờ Đổ Pháp cổ kính huyền bí giữa rừng già mây phủ.",
      "Chinh phục Đỉnh Vua cao 1.296m viếng Đền Thượng linh thiêng.",
      "Thưởng thức gà đồi nướng than hoa và sữa tươi Ba Vì béo ngậy."
    ],
    "itinerary": [
      { "day": "06:30", "title": "Hà Nội – Ba Vì", "desc": "Xe đón tại 55 Nguyễn Quốc Trị & 489 Hoàng Quốc Việt đi Ba Vì." },
      { "day": "08:30", "title": "Trekking Rừng thông cốt 400 & Nhà Thờ Đổ", "desc": "Băng qua những cánh rừng thông ngút ngàn, chụp ảnh sống ảo tại Nhà Thờ Đổ." },
      { "day": "11:30", "title": "Ăn trưa gà đồi nướng", "desc": "Dùng bữa trưa nóng sốt với đặc sản gà đồi Ba Vì." },
      { "day": "13:30", "title": "Leo Đền Thượng Đỉnh Vua", "desc": "Leo bậc đá lên đỉnh Vua 1.296m ngắm mây trôi lãng đãng." },
      { "day": "16:00", "title": "Về lại Hà Nội", "desc": "Lên xe về lại nội thành lúc 18:00." }
    ],
    "included": ["Xe đưa đón khứ hồi", "Vé cổng VQG Ba Vì", "Bữa trưa đặc sản gà đồi", "Leader theo sát", "Huy chương gỗ độc quyền", "Bảo hiểm du lịch"],
    "preparation": ["Giày thể thao", "Áo khoác nhẹ", "CCCD bản gốc"]
  },

  # TOUR 17: HÀM LỢN – SÓC SƠN (HL01)
  {
    "id": 17,
    "code": "HL01",
    "title": "Chinh phục Đỉnh Hàm Lợn – Nóc nhà Thủ Đô (462m)",
    "category": "near_hanoi",
    "subCategory": "near_hanoi",
    "badge": "Nóc nhà Thủ Đô",
    "altitudeBadge": "Đỉnh 462m",
    "image": "assets/images/tour-ham-lon.jpg",
    "price": "300.000đ/người",
    "priceNum": 300000,
    "agencyPrice": "250.000đ",
    "minPax": "Từ 5 khách",
    "departureFrequency": "Thứ 7 - Chủ Nhật hàng tuần",
    "pickupPoint": "55 Nguyễn Quốc Trị & 489 Hoàng Quốc Việt, Hà Nội",
    "duration": "Trong ngày",
    "location": "Sóc Sơn, Hà Nội",
    "altitude": "462m",
    "trekDistance": "Khoảng 6 km",
    "difficultyLevel": 1,
    "difficultyText": "Nhẹ nhàng - Tập dượt thể lực",
    "isFeatured": False,
    "reviews": 98,
    "shortSummary": "Cung trekking rèn luyện thể lực cuối tuần cực vui, leo dốc rừng thông và cắm trại chill bên hồ Suối Bàu.",
    "routeMap": "Từ trung tâm Hà Nội đi Sóc Sơn (40km). Tuyến trek bắt đầu từ chân hồ Suối Bàu, men theo suối đá hoặc leo dốc rừng thông lên đỉnh Hàm Lợn (462m).",
    "routeSteps": ["Hà Nội", "Sóc Sơn", "Hồ Suối Bàu", "Cung suối đá / Rừng thông", "Đỉnh Hàm Lợn (462m)"],
    "historyStory": "Núi Hàm Lợn thuộc dãy Độc Tôn (Sóc Sơn), là đỉnh núi cao nhất Hà Nội (462m). Nơi đây từ lâu là 'thao trường' quen thuộc của cộng đồng phượt thủ miền Bắc tập dượt thể lực trước khi chinh phục các cung lớn như Fansipan hay Kỳ Quan San.",
    "description": "Chuyến dã ngoại cuối tuần vui vẻ, tiết kiệm, phù hợp nhóm bạn trẻ, sinh viên và các gia đình muốn vận động nhẹ nhàng.",
    "departureDates": ["26/10/2026", "02/11/2026", "09/11/2026", "16/11/2026"],
    "highlights": [
      "Chạm đỉnh 'Nóc nhà Thủ đô' Hàm Lợn và ngắm trọn hồ Suối Bàu từ trên cao.",
      "Check-in rừng thông bạt ngàn ngỡ như Đà Lạt thu nhỏ chỉ cách Hà Nội 1 tiếng đi xe.",
      "Cắm trại picnic, nướng BBQ và thưởng thức cà phê thư giãn bên hồ nước thơ mộng."
    ],
    "itinerary": [
      { "day": "07:00", "title": "Hà Nội – Sóc Sơn", "desc": "Xe đón tại 55 Nguyễn Quốc Trị & 489 Hoàng Quốc Việt đi Sóc Sơn." },
      { "day": "08:30", "title": "Bắt đầu leo đỉnh Hàm Lợn", "desc": "Khởi động và trekking qua rừng thông bạt ngàn lên đỉnh 462m." },
      { "day": "11:30", "title": "Chạm đỉnh & Xuống hồ Suối Bàu", "desc": "Chụp ảnh tại cột mốc nóc nhà Hà Nội, di chuyển xuống hồ Suối Bàu hạ trại ăn trưa BBQ." },
      { "day": "15:30", "title": "Về lại Hà Nội", "desc": "Thu dọn rác, lên xe về lại nội thành lúc 17:00." }
    ],
    "included": [
      "Xe ô tô đưa đón khứ hồi",
      "Leader hướng dẫn & Bữa trưa BBQ picnic bên hồ",
      "Nước uống tinh khiết & đồ sơ cứu cơ bản",
      "Huy chương gỗ Hàm Lợn độc quyền",
      "Bảo hiểm du lịch 20.000.000đ"
    ],
    "preparation": ["Giày thể thao êm chân", "Mũ nón chống nắng", "CCCD bản gốc"]
  },

  # TOUR 18: ĐÓN TẠI CỬA TỬ (CT02)
  {
    "id": 18,
    "code": "CT02",
    "title": "Trải Nghiệm Suối Cửa Tử (Đón Tại Cửa Tử Thái Nguyên)",
    "category": "near_hanoi",
    "subCategory": "experience",
    "badge": "Lội suối vượt thác",
    "altitudeBadge": "Chân suối Cửa Tử",
    "image": "assets/images/tour-cua-tu.jpg",
    "price": "399.000đ/người",
    "priceNum": 399000,
    "agencyPrice": "350.000đ",
    "minPax": "Từ 5 khách",
    "departureFrequency": "Thứ 7 - Chủ Nhật hàng tuần",
    "pickupPoint": "Chân suối Cửa Tử, Đại Từ, Thái Nguyên",
    "duration": "Trong ngày",
    "location": "Đại Từ, Thái Nguyên",
    "altitude": "Chân thác Cửa Tử",
    "trekDistance": "Khoảng 6 km",
    "difficultyLevel": 2,
    "difficultyText": "Nhẹ - Vui nhộn",
    "isFeatured": False,
    "reviews": 45,
    "shortSummary": "Gói tour dành cho khách tự di chuyển xe riêng đến Thái Nguyên, lội suối Cửa Tử và trượt máng đá an toàn cùng Leader bản địa.",
    "routeMap": "Đón khách trực tiếp tại chân suối Cửa Tử (Hoàng Nông, Đại Từ, Thái Nguyên). Leader trang bị áo phao và dẫn đoàn lội suối khám phá các máng trượt đá tự nhiên.",
    "routeSteps": ["Chân suối Cửa Tử", "Cửa 1", "Cửa 2", "Máng trượt tự nhiên"],
    "historyStory": "Dành cho các nhóm bạn, gia đình tự lái xe ô tô hoặc xe máy lên Thái Nguyên, cần dịch vụ hướng dẫn an toàn, porter bản địa và trang thiết bị áo phao chuyên nghiệp.",
    "description": "Trải nghiệm lội suối vượt thác cực chill và an toàn với chi phí tiết kiệm nhất.",
    "departureDates": ["01/11/2026", "08/11/2026", "15/11/2026", "22/11/2026"],
    "highlights": [
      "Leader địa phương dẫn đường an toàn tuyệt đối.",
      "Trang bị áo phao chuyên dụng và túi chống nước cho cả đoàn.",
      "Tự do khám phá trượt máng đá và bơi lội giữa hồ nước trong vắt."
    ],
    "itinerary": [
      { "day": "08:30", "title": "Đón tại chân suối", "desc": "Tập trung tại homestay chân suối Cửa Tử, phổ biến quy tắc an toàn." },
      { "day": "09:00", "title": "Lội suối vượt thác", "desc": "Trekking lội suối, trượt máng đá Cửa 1 và Cửa 2." },
      { "day": "12:00", "title": "Ăn trưa bên bờ suối", "desc": "Ăn trưa picnic thơm ngon giữa tiếng suối chảy róc rách." },
      { "day": "15:00", "title": "Kết thúc tour", "desc": "Trở về chân suối tắm tráng, chia tay đoàn." }
    ],
    "included": ["Leader & Porter bản địa", "Áo phao an toàn", "Bữa trưa picnic", "Bảo hiểm du lịch"],
    "preparation": ["Giày lội suối bám đá", "Quần áo khô thay", "CCCD bản gốc"]
  },

  # TOUR 19: THIỆN NGUYỆN ÁO ẤM CHO EM (CHARITY-01)
  {
    "id": 19,
    "code": "CHARITY-01",
    "title": "Áo Ấm Cho Em – Thiện Nguyện Mù Cang Chải",
    "category": "charity",
    "subCategory": "charity",
    "badge": "Lan tỏa yêu thương",
    "altitudeBadge": "Vùng cao Tây Bắc",
    "image": "assets/images/tour-thien-nguyen.jpg",
    "price": "1.250.000đ/người",
    "priceNum": 1250000,
    "agencyPrice": "1.100.000đ",
    "minPax": "Từ 5 khách",
    "departureFrequency": "Tháng 11 & 12",
    "pickupPoint": "55 Nguyễn Quốc Trị & 489 Hoàng Quốc Việt, Hà Nội",
    "duration": "2 ngày 1 đêm",
    "location": "Mù Cang Chải, Yên Bái",
    "altitude": "1.500m",
    "trekDistance": "Khoảng 6 km",
    "difficultyLevel": 1,
    "difficultyText": "Nhẹ nhàng",
    "isFeatured": False,
    "reviews": 56,
    "shortSummary": "Hành trình mang áo ấm và quà tặng đến với các em nhỏ điểm trường vùng cao khó khăn tại Mù Cang Chải.",
    "routeMap": "Từ Hà Nội qua đèo Khau Phạ đến các điểm trường mầm non và tiểu học vùng sâu tại Mù Cang Chải (Yên Bái). Trao quà thiện nguyện, giao lưu văn nghệ và trekking nhẹ thăm bản làng người Mông.",
    "routeSteps": ["Hà Nội", "Đèo Khau Phạ", "Điểm trường vùng cao", "Treo áo ấm & Tặng quà", "Giao lưu bản Mông"],
    "historyStory": "Chương trình thường niên của cộng đồng Đi Cùng Gió nhằm kết nối những trái tim nhân ái, trao gửi sự ấm áp đến trẻ em vùng cao trước mùa đông giá buốt.",
    "description": "Một chuyến đi đong đầy ý nghĩa nhân văn, nơi mỗi bước chân đều mang lại nụ cười và niềm hy vọng cho các em nhỏ vùng cao.",
    "departureDates": ["15/11/2026", "29/11/2026", "13/12/2026"],
    "highlights": [
      "Trực tiếp trao tận tay những chiếc áo ấm, sách vở và bữa ăn dinh dưỡng cho các em nhỏ khó khăn.",
      "Giao lưu nhảy sạp, đốt lửa trại ấm áp cùng đồng bào vùng cao.",
      "Ngắm hoàng hôn đèo Khau Phạ – một trong 'Tứ đại đỉnh đèo' Tây Bắc."
    ],
    "itinerary": [
      { "day": "Ngày 1", "title": "Hà Nội – Khau Phạ – Điểm trường Mù Cang Chải", "desc": "Xe đón tại Hà Nội. Chiều đến điểm trường trao quà áo ấm, đồ dùng học tập cho các bé." },
      { "day": "Ngày 2", "title": "Giao lưu bản làng – Hà Nội", "desc": "Trekking thăm bản người Mông, thưởng thức đặc sản xôi nếp Tú Lệ. Chiều về lại Hà Nội." }
    ],
    "included": ["Xe du lịch khứ hồi", "Homestay bản địa", "Các bữa ăn vùng cao", "Điều phối viên thiện nguyện", "Bảo hiểm du lịch"],
    "preparation": ["Quần áo ấm", "Tấm lòng nhiệt huyết", "CCCD bản gốc"]
  },

  # TOUR 20: TỦ SÁCH VÙNG CAO (CHARITY-02)
  {
    "id": 20,
    "code": "CHARITY-02",
    "title": "Tủ Sách Vùng Cao – Tiếp Bước Nậm Có Yên Bái",
    "category": "charity",
    "subCategory": "charity",
    "badge": "Gieo mầm tri thức",
    "altitudeBadge": "Xã Nậm Có",
    "image": "assets/images/tour-mu-cang-chai.jpg",
    "price": "1.200.000đ/người",
    "priceNum": 1200000,
    "agencyPrice": "1.050.000đ",
    "minPax": "Từ 5 khách",
    "departureFrequency": "Tháng 11 & 12",
    "pickupPoint": "55 Nguyễn Quốc Trị & 489 Hoàng Quốc Việt, Hà Nội",
    "duration": "2 ngày 1 đêm",
    "location": "Mù Cang Chải, Yên Bái",
    "altitude": "1.400m",
    "trekDistance": "Khoảng 6 km",
    "difficultyLevel": 1,
    "difficultyText": "Nhẹ nhàng",
    "isFeatured": False,
    "reviews": 42,
    "shortSummary": "Xây dựng tủ sách tri thức, trao học bổng khuyến học và hỗ trợ sửa chữa phòng học cho trẻ em vùng cao Nậm Có.",
    "routeMap": "Từ Hà Nội di chuyển vào xã đặc biệt khó khăn Nậm Có (huyện Mù Cang Chải, Yên Bái). Lắp đặt tủ sách, sơn sửa lớp học và tổ chức ngày hội đọc sách cùng các em nhỏ.",
    "routeSteps": ["Hà Nội", "Nghĩa Lộ", "Xã Nậm Có", "Điểm trường", "Ngày hội đọc sách"],
    "historyStory": "Dự án phi lợi nhuận hướng tới mục tiêu mang sách truyện hay và nguồn cảm hứng học tập đến với trẻ em các thôn bản xa xôi hẻo lánh vùng Tây Bắc.",
    "description": "Cùng Đi Cùng Gió gieo mầm tri thức, mang lại tương lai tươi sáng hơn cho thế hệ măng non vùng cao.",
    "departureDates": ["22/11/2026", "06/12/2026", "20/12/2026"],
    "highlights": [
      "Trực tiếp lắp đặt tủ sách với hơn 500 đầu sách truyện ý nghĩa cho trường học.",
      "Tổ chức các trò chơi tập thể, kể chuyện và đố vui có thưởng cùng các em.",
      "Thưởng thức không gian thanh bình và tình cảm nồng ấm của người dân bản địa."
    ],
    "itinerary": [
      { "day": "Ngày 1", "title": "Hà Nội – Xã Nậm Có", "desc": "Khởi hành sớm từ Hà Nội. Chiều lắp đặt tủ sách, sơn sửa bàn ghế lớp học." },
      { "day": "Ngày 2", "title": "Ngày hội sách & Về Hà Nội", "desc": "Tổ chức ngày hội đọc sách cùng các em học sinh. Chiều lên xe về lại thủ đô lúc 20:00." }
    ],
    "included": ["Xe đưa đón khứ hồi", "Homestay bản địa", "Bữa ăn địa phương", "Chi phí điều phối dự án", "Bảo hiểm du lịch"],
    "preparation": ["Sách truyện mang theo ủng hộ", "Giày thể thao", "CCCD bản gốc"]
  }
]

with open('scripts/parsed_tours.json', 'w', encoding='utf-8') as f:
    json.dump(tours, f, ensure_ascii=False, indent=2)

print(f"Generated parsed_tours.json with {len(tours)} comprehensive tours!")

