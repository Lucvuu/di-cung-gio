/**
 * DI CUNG GIO - Main Interactive Controller
 * Inspiring modern trekking experience (inspired by gianglangthang.vn)
 * Zero-build vanilla ES6+ architecture
 */

// ==========================================
// 1. TOUR DATA REPOSITORY (ALL 20 TOURS)
// ==========================================
const TOURS_DATA = [
  {
    "id": 1,
    "code": "YT01",
    "title": "Trekking Yên Tử – Chùa Đồng",
    "category": "spiritual",
    "subCategory": "trekking",
    "badge": "Tâm linh & Non thiêng",
    "altitudeBadge": "⛰️ 1.068m",
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
    "isFeatured": true,
    "reviews": 128,
    "shortSummary": "Hành hương về non thiêng đất Phật, băng rừng Tùng cổ thụ 700 năm chạm đỉnh Chùa Đồng (1.068m).",
    "routeMap": "Xuất phát từ Hà Nội theo cao tốc Hải Phòng đi Uông Bí (Quảng Ninh). Tuyến trekking bắt đầu từ Suối Giải Oan, qua Đường Tùng cổ thụ 700 năm tuổi, Vườn Tháp Tổ Huệ Quang, Chùa Hoa Yên, Chùa Một Mái, tượng đá An Kỳ Sinh, vượt dốc Đá Chồng và chạm đỉnh Chùa Đồng 1.068m giữa mây ngàn Đông Bắc.",
    "routeSteps": [
      "Hà Nội",
      "Suối Giải Oan",
      "Đường Tùng 700 năm",
      "Chùa Hoa Yên",
      "Tượng An Kỳ Sinh",
      "Đỉnh Chùa Đồng (1.068m)"
    ],
    "historyStory": "Núi Yên Tử (còn gọi là Bạch Vân Sơn – núi mây trắng) là cái nôi của Thiền phái Trúc Lâm Đại Việt do Phật hoàng Trần Nhân Tông sáng lập năm 1299 sau hai lần đánh thắng quân Nguyên Mông. Chùa Đồng trên đỉnh núi được đúc hoàn toàn bằng đồng nguyên khối trên đỉnh núi lớn nhất châu Á, tọa lạc tại độ cao 1.068m giữa biển mây hùng vĩ.",
    "description": "Hành trình leo núi thiêng Yên Tử, chiêm bái Chùa Đồng trên đỉnh Phù Vân, rèn luyện thể lực và tìm lại an yên trong tâm hồn giữa mây ngàn đại ngàn.",
    "departureDates": [
      "26/10/2026",
      "02/11/2026",
      "09/11/2026",
      "16/11/2026"
    ],
    "gallery": [
      {
        "url": "assets/images/tour-yen-tu.jpg",
        "caption": "Chóp Chùa Đồng giữa mây ngàn Yên Tử"
      },
      {
        "url": "assets/images/yen-tu-1.jpg",
        "caption": "Mái chùa đồng cổ kính linh thiêng trên đỉnh núi đá"
      },
      {
        "url": "assets/images/yen-tu-2.jpg",
        "caption": "Toàn cảnh non thiêng Yên Tử từ độ cao 1.068m"
      },
      {
        "url": "assets/images/yen-tu-3.jpg",
        "caption": "Hành hương qua Đường Tùng cổ thụ 700 năm tuổi"
      }
    ],
    "highlights": [
      "Chạm tay vào Chùa Đồng đúc bằng đồng nguyên khối lớn nhất Châu Á trên đỉnh Phù Vân.",
      "Dạo bước giữa rừng trúc bạt ngàn ngàn năm tuổi và đường Tùng cổ thụ 700 năm.",
      "Đón bình minh hoặc hoàng hôn dát vàng trên non thiêng Yên Tử thanh tịnh và an lạc."
    ],
    "itinerary": [
      {
        "day": "05:30",
        "title": "Hà Nội – Uông Bí",
        "desc": "Xe đón đoàn tại 55 Nguyễn Quốc Trị và 489 Hoàng Quốc Việt, khởi hành đi Uông Bí (Quảng Ninh). Dừng chân ăn sáng đặc sản bánh cuốn chả mực."
      },
      {
        "day": "08:30",
        "title": "Bắt đầu trekking Yên Tử",
        "desc": "Khởi động tại chân núi, trekking qua suối Giải Oan, Tháp Tổ Huệ Quang, chùa Hoa Yên, chùa Một Mái giữa rừng thông xanh ngát."
      },
      {
        "day": "12:00",
        "title": "Chạm đỉnh Chùa Đồng 1.068m",
        "desc": "Chiêm bái Chùa Đồng linh thiêng trong sương mây, thưởng ngoạn panorama toàn cảnh Đông Bắc, dùng bữa trưa picnic."
      },
      {
        "day": "16:00",
        "title": "Xuống núi & Về Hà Nội",
        "desc": "Xuống núi, thư giãn ngâm chân thảo dược suối Giải Oan. Lên xe về lại thủ đô Hà Nội lúc 19:30."
      }
    ],
    "included": [
      "Xe ô tô du lịch đời mới khứ hồi Hà Nội – Yên Tử",
      "Hướng dẫn viên / Leader kinh nghiệm theo sát (tỉ lệ 8-10 khách/leader)",
      "Nước suối tinh khiết 500ml/khách",
      "Huy chương leo núi bằng gỗ độc quyền của Đi Cùng Gió",
      "Gậy leo núi trekking & đồ y tế sơ cứu cơ bản",
      "Bảo hiểm du lịch trọn gói 20.000.000đ/vụ"
    ],
    "preparation": [
      "Giày trekking hoặc thể thao bám tốt",
      "CCCD/Hộ chiếu bản gốc",
      "Áo khoác gió nhẹ, mũ nón chống nắng",
      "Thuốc cá nhân và sạc dự phòng"
    ]
  },
  {
    "id": 2,
    "code": "PSP01",
    "title": "Tà Xùa – Săn mây",
    "category": "trekking",
    "subCategory": "trekking",
    "badge": "Đại dương mây",
    "altitudeBadge": "☁️ 2.865m",
    "image": "assets/images/tour-ta-xua.jpg",
    "price": "1.600.000đ/người",
    "priceNum": 1600000,
    "agencyPrice": "1.450.000đ",
    "minPax": "Từ 5 khách",
    "departureFrequency": "Thứ 7 - Chủ Nhật hàng tuần",
    "pickupPoint": "55 Nguyễn Quốc Trị & 489 Hoàng Quốc Việt, Hà Nội",
    "duration": "2 ngày 1 đêm",
    "location": "Bắc Yên, Sơn La",
    "altitude": "2.865m",
    "trekDistance": "Khoảng 12 km",
    "difficultyLevel": 3,
    "difficultyText": "Trung bình",
    "isFeatured": true,
    "reviews": 186,
    "shortSummary": "Chinh phục 'Sống lưng khủng long' Háng Đồng, đón biển mây bồng bềnh cuộn trào và đón bình minh rực rỡ Tây Bắc.",
    "routeMap": "Khởi hành từ Hà Nội theo QL32 lên huyện Bắc Yên (Sơn La). Tuyến trekking đưa bạn dọc 'Sống lưng khủng long' tại bản Háng Đồng, check-in Mỏm Cá Heo, Cây Cô Đơn, Đỉnh Gió, thảo nguyên Tà Xùa và rừng nguyên sinh rêu phong huyền ảo.",
    "routeSteps": [
      "Hà Nội",
      "Bắc Yên (Sơn La)",
      "Xã Tà Xùa",
      "Sống lưng Háng Đồng",
      "Mỏm Cá Heo & Cây Cô Đơn",
      "Đỉnh Phu Sa Phìn (2.868m)"
    ],
    "historyStory": "Dãy Tà Xùa hợp thành từ ba đỉnh núi cao kỳ vĩ thuộc phần đuôi kéo dài về phía Nam của dãy Hoàng Liên Sơn hùng vĩ. Nơi đây sở hữu thung lũng lòng chảo giữ mây dày đặc và lâu tan bậc nhất Việt Nam, là quê hương của những cây chè Shan Tuyết cổ thụ hàng trăm năm tuổi của người Mông.",
    "description": "Chinh phục 'sống lưng khủng long' huyền thoại Bản Công, đắm chìm trong biển mây bồng bềnh lúc bình minh và tận hưởng bầu không khí Tây Bắc se lạnh.",
    "departureDates": [
      "01/11/2026",
      "08/11/2026",
      "15/11/2026",
      "22/11/2026"
    ],
    "gallery": [
      {
        "url": "assets/images/tour-ta-xua.jpg",
        "caption": "Biển mây bồng bềnh cuộn trào thung lũng Tà Xùa"
      },
      {
        "url": "assets/images/ta-xua-1.jpg",
        "caption": "Bình minh rực rỡ trên sống lưng khủng long Háng Đồng"
      },
      {
        "url": "assets/images/ta-xua-2.jpg",
        "caption": "Trekker check-in mỏm đá ngắm đại ngàn Tây Bắc"
      },
      {
        "url": "assets/images/hero-bg.jpg",
        "caption": "Toàn cảnh biển mây Tây Bắc lúc rạng đông"
      }
    ],
    "highlights": [
      "Đi bộ trên Sống Lưng Khủng Long kỳ vĩ với biển mây cuộn trào hai bên sườn núi.",
      "Check-in Mỏm Cá Heo, Cây Táo Mèo cô đơn ngắm hoàng hôn rực rỡ thung lũng Bản Công.",
      "Thưởng thức lẩu gà đen đồi H’Mông nóng hổi bên bếp than hồng và giao lưu đốt lửa trại."
    ],
    "itinerary": [
      {
        "day": "Ngày 0",
        "title": "Hà Nội – Tà Xùa",
        "desc": "19:00 đón đoàn tại 55 Nguyễn Quốc Trị và 489 Hoàng Quốc Việt đi Bắc Yên. Đến Tà Xùa lúc nửa đêm, nhận phòng homestay view mây nghỉ ngơi."
      },
      {
        "day": "Ngày 1",
        "title": "Khám phá Tà Xùa & Rừng rêu",
        "desc": "Đón bình minh Đỉnh Gió, check-in Cây Cô Đơn, Mỏm Cá Heo. Trekking nhẹ xuyên rừng rêu ma mị. Tối ăn lẩu gà đen."
      },
      {
        "day": "Ngày 2",
        "title": "Sống lưng khủng long – Hà Nội",
        "desc": "05:30 trekking Sống Lưng Khủng Long Háng Đồng săn biển mây cuồn cuộn. 13:30 lên xe về Hà Nội lúc 19:30."
      }
    ],
    "included": [
      "Xe ô tô giường nằm / Limousine khứ hồi Hà Nội – Tà Xùa",
      "Homestay view mây Bản Công tiêu chuẩn",
      "Các bữa ăn tiêu chuẩn vùng cao (lẩu gà đen, thịt nướng)",
      "Leader & Porter bản địa chu đáo (tỉ lệ 8-10 khách/leader)",
      "Huy chương leo núi bằng gỗ độc quyền Đi Cùng Gió",
      "Bảo hiểm du lịch trọn gói 100.000.000đ/người"
    ],
    "preparation": [
      "Áo khoác ấm (nhiệt độ đêm 10-14°C)",
      "Giày trekking chống trơn trượt",
      "CCCD/Hộ chiếu bản gốc",
      "Sạc dự phòng & máy ảnh"
    ]
  },
  {
    "id": 3,
    "code": "SM01",
    "title": "Phu Sa Phin – Chinh phục đỉnh cao",
    "category": "trekking",
    "subCategory": "trekking",
    "badge": "Rừng rêu ma mị",
    "altitudeBadge": "🏔️ 2.868m",
    "image": "assets/images/tour-samu.jpg",
    "price": "2.800.000đ/người",
    "priceNum": 2800000,
    "agencyPrice": "2.500.000đ",
    "minPax": "Từ 5 khách",
    "departureFrequency": "Thứ 7 - Chủ Nhật hàng tuần",
    "pickupPoint": "55 Nguyễn Quốc Trị & 489 Hoàng Quốc Việt, Hà Nội",
    "duration": "2 ngày 1 đêm",
    "location": "Bắc Yên, Sơn La",
    "altitude": "2.868m",
    "trekDistance": "Khoảng 14 km",
    "difficultyLevel": 3,
    "difficultyText": "Trung bình",
    "isFeatured": true,
    "reviews": 94,
    "shortSummary": "Khám phá khu rừng rêu ma mị cổ thụ, vượt sống lưng uốn lượn và chạm đỉnh cao nguyên sinh Phu Sa Phìn (2.868m).",
    "routeMap": "Hành trình từ Hà Nội qua Bắc Yên đến điểm trek Xím Vàng. Tuyến leo xuyên qua thảm thực vật rừng nguyên sinh nguyên sơ với các tầng rêu phủ kín thân cây cổ thụ hàng trăm năm, vượt dốc đá lên lán nghỉ và chạm đỉnh Sa Mu 2.756m.",
    "routeSteps": [
      "Hà Nội",
      "Bắc Yên",
      "Điểm trek Xím Vàng",
      "Cây Thần Kỳ",
      "Lán ngủ trên núi",
      "Đỉnh Sa Mu (2.756m)"
    ],
    "historyStory": "Đỉnh Sa Mu (U Bò) cao 2.756m là ranh giới tự nhiên giữa Sơn La và Yên Bái. Cung trek nổi tiếng với cánh rừng rêu ma mị đẹp bậc nhất vùng Tây Bắc, nơi lưu giữ hệ sinh thái rừng á nhiệt đới nguyên sinh gần như nguyên vẹn chưa bị tác động của con người.",
    "description": "Hành trình lạc bước vào khu rừng cổ tích rêu phong, săn mây đại ngàn và ngắm dải ngân hà lấp lánh khi ngủ đêm trong lán gỗ trên núi.",
    "departureDates": [
      "01/11/2026",
      "08/11/2026",
      "15/11/2026",
      "22/11/2026"
    ],
    "highlights": [
      "Chiêm ngưỡng khu rừng rêu ma mị với cây cổ thụ phủ kín rêu phong như truyện cổ tích tích.",
      "Check-in Cây Thần Kỳ khổng lồ đứng sừng sững giữa rừng già Tây Bắc.",
      "Ngắm biển mây lúc bình minh từ chóp Sa Mu 2.756m và thưởng thức thịt nướng thơm lừng bên lán gỗ."
    ],
    "itinerary": [
      {
        "day": "Ngày 0",
        "title": "Hà Nội – Bắc Yên",
        "desc": "19:00 xe đón tại 55 Nguyễn Quốc Trị & 489 Hoàng Quốc Việt đi Bắc Yên. Nghỉ đêm homestay chuẩn bị thể lực."
      },
      {
        "day": "Ngày 1",
        "title": "Trek Xím Vàng – Lán rừng rêu",
        "desc": "Ăn sáng, xe đưa vào điểm trek. Leo dốc qua rừng rêu nguyên sinh ma mị, check-in Cây Thần Kỳ. Chiều đến lán ngủ, ngắm hoàng hôn ăn tối lẩu nóng."
      },
      {
        "day": "Ngày 2",
        "title": "Chạm đỉnh Sa Mu 2.756m – Hà Nội",
        "desc": "05:00 trekking lên chóp Sa Mu đón bình minh biển mây. Xuống núi ăn trưa, lên xe về lại Hà Nội lúc 20:00."
      }
    ],
    "included": [
      "Xe ô tô giường nằm đưa đón khứ hồi từ Hà Nội",
      "Lán gỗ ngủ trên núi có túi ngủ & chăn ấm",
      "Porter bản địa gùi đồ & nấu các bữa ăn nóng sốt",
      "Huy chương gỗ Sa Mu kỷ niệm độc quyền",
      "Gậy trekking & đồ y tế, bảo hiểm du lịch trọn gói 100tr"
    ],
    "preparation": [
      "Giày leo núi có gai bám chống trơn",
      "Áo ấm giữ nhiệt",
      "Đèn pin đeo đầu",
      "Găng tay trekking"
    ]
  },
  {
    "id": 4,
    "code": "KQS01",
    "title": "Kỳ Quan San – Đỉnh núi hùng vĩ",
    "category": "trekking",
    "subCategory": "trekking",
    "badge": "Top 4 Nóc nhà VN",
    "altitudeBadge": "🏔️ 3.046m",
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
    "isFeatured": true,
    "reviews": 115,
    "shortSummary": "Hành trình chinh phục đỉnh Kỳ Quan San (3.046m - Top 4 VN), đón bình minh tráng lệ trên sống lưng khủng long Đồi Muối.",
    "routeMap": "Từ Hà Nội đi Bát Xát (Lào Cai). Tuyến trekking xuất phát từ bản Dền Sung, vượt suối, leo rừng thảo quả, chinh phục Đồi Muối (2.100m) và men theo sống núi hiểm trở để chạm chóp inox 3.046m.",
    "routeSteps": [
      "Hà Nội",
      "Bát Xát (Lào Cai)",
      "Bản Dền Sung",
      "Lán Đồi Muối (2.100m)",
      "Sống lưng khủng long",
      "Đỉnh Kỳ Quan San (3.046m)"
    ],
    "historyStory": "Kỳ Quan San (thường gọi là Bạch Mộc Lương Tử) là đỉnh núi cao thứ 4 tại Việt Nam (3.046m). Tên gọi Kỳ Quan San theo tiếng địa phương nghĩa là 'ngọn núi kỳ vĩ'. Cung đường này được giới mê leo núi mệnh danh là cung đường săn bình minh và biển mây tráng lệ nhất Việt Nam.",
    "description": "Cung trekking huyền thoại thử thách thể lực và ý chí, đón bình minh rực đỏ trên sống lưng Đồi Muối và chạm tay vào đỉnh cao 3.046m.",
    "departureDates": [
      "15/11/2026",
      "22/11/2026",
      "29/11/2026",
      "06/12/2026"
    ],
    "highlights": [
      "Chiêm ngưỡng bình minh Đồi Muối – một trong những khung cảnh bình minh kỳ vĩ bậc nhất Đông Nam Á.",
      "Đi bộ trên Sống Lưng Khủng Long cheo leo giữa hai bên vực sâu ngút ngàn mây trắng.",
      "Chạm tay vào chóp inox đỉnh cao 3.046m và nhận huy chương gỗ độc quyền của Đi Cùng Gió."
    ],
    "itinerary": [
      {
        "day": "Ngày 0",
        "title": "Hà Nội – Sapa – Bát Xát",
        "desc": "21:00 đón đoàn tại 55 Nguyễn Quốc Trị & 489 Hoàng Quốc Việt, xe giường nằm chạy đêm lên Lào Cai."
      },
      {
        "day": "Ngày 1",
        "title": "Bản Dền Sung – Lán Đồi Muối 2.100m",
        "desc": "Ăn sáng, xe đưa đến chân núi. Trekking qua suối đá, rừng trúc, rừng thảo quả. Đến lán Đồi Muối, ngắm biển mây hoàng hôn đỏ rực."
      },
      {
        "day": "Ngày 2",
        "title": "Chạm đỉnh Kỳ Quan San 3.046m",
        "desc": "04:30 trekking vượt Sống lưng khủng long đón bình minh, chạm đỉnh 3.046m lúc 09:30. Chiều quay về lại lán Đồi Muối nghỉ ngơi ăn mừng."
      },
      {
        "day": "Ngày 3",
        "title": "Xuống núi – Tắm lá thuốc Dao đỏ – Hà Nội",
        "desc": "Xuống chân núi, tắm lá thuốc Dao Đỏ xua tan mệt mỏi tại Sapa. Lên xe về lại Hà Nội lúc 21:00."
      }
    ],
    "included": [
      "Xe giường nằm khứ hồi Hà Nội – Sapa – Bát Xát",
      "Lán ngủ Đồi Muối có đầy đủ chăn đệm ấm áp",
      "Đội ngũ Porter bản địa nhiệt tình gùi hành lý và nấu ăn",
      "Tắm lá thuốc người Dao đỏ thư giãn hồi phục cơ thể",
      "Huy chương gỗ Kỳ Quan San khắc tên kỷ niệm",
      "Bảo hiểm du lịch mức 100.000.000đ/người"
    ],
    "preparation": [
      "Giày trekking chuyên dụng bám đá",
      "Áo ấm lông vũ, áo gió chống nước",
      "Bó gối, tất dài, găng tay bám",
      "CCCD/Hộ chiếu bản gốc"
    ]
  },
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
    "isFeatured": false,
    "reviews": 142,
    "shortSummary": "Chinh phục đỉnh Tà Chì Nhù 2.979m – ngọn núi của gió, mây và đồi hoa tím Chi Pâu bạt ngàn.",
    "routeMap": "Từ Hà Nội đi thị xã Nghĩa Lộ rồi vào Mỏ Chì (huyện Trạm Tấu, Yên Bái). Tuyến trek dốc liên tục nhưng thoáng đãng, mở ra tầm nhìn đại dương mây cuồn cuộn và đồi hoa Chi Pâu tím biếc.",
    "routeSteps": [
      "Hà Nội",
      "Nghĩa Lộ",
      "Mỏ Chì Trạm Tấu",
      "Lán 2.400m",
      "Đỉnh Tà Chì Nhù (2.979m)"
    ],
    "historyStory": "Tà Chì Nhù (còn gọi là Phu Song Sung) cao 2.979m, là đỉnh núi cao thứ 7 tại Việt Nam. Nơi đây được ví như 'vương quốc mây và hoa' nhờ không gian lộng gió và những triền đồi hoa Chi Pâu tím ngắt nở rộ vào mùa thu đông.",
    "description": "Chiêm ngưỡng đồi hoa tím Chi Pâu nở bạt ngàn khắp các sườn núi và đón hoàng hôn biển mây ngoạn mục bậc nhất miền Bắc.",
    "departureDates": [
      "22/11/2026",
      "29/11/2026",
      "06/12/2026",
      "13/12/2026"
    ],
    "highlights": [
      "Đắm chìm giữa thảo nguyên hoa tím Chi Pâu nở rực khắp các triền đồi.",
      "Ngắm hoàng hôn và bình minh biển mây 360 độ từ đỉnh chóp inox 2.979m.",
      "Trải nghiệm tắm khoáng nóng tự nhiên Trạm Tấu sau khi xuống núi."
    ],
    "itinerary": [
      {
        "day": "Ngày 0",
        "title": "Hà Nội – Trạm Tấu",
        "desc": "19:00 xe đón tại Hà Nội đi Nghĩa Lộ. Nghỉ đêm tại Trạm Tấu."
      },
      {
        "day": "Ngày 1",
        "title": "Mỏ Chì – Lán 2.400m",
        "desc": "Trekking men theo sườn núi dốc ngắm mây và hoa Chi Pâu. 16:30 đến lán nghỉ ngắm hoàng hôn, ăn lẩu nóng."
      },
      {
        "day": "Ngày 2",
        "title": "Chạm đỉnh 2.979m – Tắm khoáng nóng",
        "desc": "05:00 chạm đỉnh Tà Chì Nhù đón bình minh. Xuống núi tắm suối khoáng nóng Trạm Tấu thư giãn, về lại Hà Nội."
      }
    ],
    "included": [
      "Xe ô tô giường nằm khứ hồi Hà Nội – Trạm Tấu",
      "Vé tắm khoáng nóng tự nhiên Trạm Tấu",
      "Lán nghỉ trên núi, túi ngủ và chăn ấm",
      "Porter bản địa & Leader nhiều kinh nghiệm",
      "Huy chương gỗ Tà Chì Nhù độc quyền",
      "Bảo hiểm du lịch trọn gói 100.000.000đ"
    ],
    "preparation": [
      "Giày trekking bám tốt",
      "Áo gió chống gió mạnh",
      "Mũ tai bèo, kính râm",
      "CCCD bản gốc"
    ]
  },
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
    "isFeatured": false,
    "reviews": 110,
    "shortSummary": "Cung leo núi 'quốc dân' cực chill, ngắm bình minh trên biển mây bồng bềnh và check-in mỏm đá câu cá Y Tý.",
    "routeMap": "Từ Hà Nội đi thị trấn Sapa rồi di chuyển lên xã vùng cao Y Tý (Bát Xát). Tuyến leo thoai thoải qua đồi cây cháy, lán người Mông và sống núi thoai thoải lên chóp inox 2.860m.",
    "routeSteps": [
      "Hà Nội",
      "Sapa",
      "Y Tý",
      "Lán nghỉ A Hờ",
      "Mỏm đá Câu Cá",
      "Đỉnh Lảo Thần (2.860m)"
    ],
    "historyStory": "Lảo Thần cao 2.860m được xem là 'nóc nhà của vùng đất sương mù Y Tý'. Địa hình cung này thoai thoải, đường mòn rõ ràng nên là lựa chọn số 1 cho người mới bắt đầu bước chân vào bộ môn trekking leo núi.",
    "description": "Cung trekking nhẹ nhàng, lãng mạn với biển mây tràn thung lũng, hoàng hôn rực rỡ và sao trời ngút ngàn đêm trên núi.",
    "departureDates": [
      "01/11/2026",
      "08/11/2026",
      "15/11/2026",
      "22/11/2026"
    ],
    "highlights": [
      "Check-in Mỏm đá Câu cá và Cây cầu gỗ vươn ra biển mây huyền ảo.",
      "Ngắm biển mây lúc hoàng hôn và bình minh đẹp nhất vùng rẻo cao Y Tý.",
      "Thưởng thức gà nướng xôi ngũ sắc bên bếp lửa bập bùng cùng đồng bào Mông."
    ],
    "itinerary": [
      {
        "day": "Ngày 0",
        "title": "Hà Nội – Sapa – Y Tý",
        "desc": "21:30 đón tại Hà Nội đi Lào Cai trên xe giường nằm êm ái."
      },
      {
        "day": "Ngày 1",
        "title": "Y Tý – Lán A Hờ (Trek 8km)",
        "desc": "Ăn sáng tại Y Tý, bắt đầu trek qua rừng thảo quả lên lán. Chiều săn mây hoàng hôn đỏ rực."
      },
      {
        "day": "Ngày 2",
        "title": "Chạm đỉnh Lảo Thần 2.860m – Hà Nội",
        "desc": "05:00 đón bình minh trên đỉnh chóp inox. Xuống núi tắm lá thuốc Dao đỏ Sapa, lên xe về Hà Nội."
      }
    ],
    "included": [
      "Xe giường nằm khứ hồi Hà Nội – Sapa – Y Tý",
      "Lán gỗ ngủ trên núi đầy đủ chăn ấm",
      "Leader Đi Cùng Gió & Porter bản địa tận tâm",
      "Huy chương gỗ lưu niệm độc quyền",
      "Bảo hiểm du lịch 100.000.000đ/người"
    ],
    "preparation": [
      "Giày thể thao êm chân",
      "Áo ấm, khăn quàng",
      "CCCD bản gốc"
    ]
  },
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
    "isFeatured": false,
    "reviews": 88,
    "shortSummary": "Chinh phục ngọn núi bí ẩn của người Thái bản Tu San, đón gió trên bãi cỏ bạt ngàn tại đỉnh Lùng Cúng 2.913m.",
    "routeMap": "Từ Hà Nội đi thị trấn Tú Lệ, rẽ vào bản Tu San (Mù Cang Chải). Tuyến trek xuyên qua những cánh rừng hạt dẻ cổ thụ, rừng trúc xanh ngút ngàn và triền đồi hoa đỗ quyên rực rỡ.",
    "routeSteps": [
      "Hà Nội",
      "Tú Lệ",
      "Bản Tu San",
      "Rừng trúc cổ",
      "Lán nghỉ",
      "Đỉnh Lùng Cúng (2.913m)"
    ],
    "historyStory": "Lùng Cúng được đặt tên theo bản làng hẻo lánh dưới chân núi. Đỉnh núi cao 2.913m với thảo nguyên cỏ bằng phẳng trên đỉnh, mang lại tầm nhìn bao quát toàn bộ thung lũng Mù Cang Chải và ruộng bậc thang kỳ vĩ.",
    "description": "Hành trình hoang sơ chạm vào trái tim đại ngàn Mù Cang Chải, thưởng thức xôi nếp nương Tú Lệ thơm dẻo.",
    "departureDates": [
      "01/11/2026",
      "08/11/2026",
      "15/11/2026",
      "22/11/2026"
    ],
    "highlights": [
      "Đứng trên thảo nguyên cỏ bao la lộng gió tại đỉnh chóp 2.913m.",
      "Băng qua khu rừng trúc thẳng tắp huyền ảo như phim kiếm hiệp.",
      "Thưởng thức đặc sản nếp nương Tú Lệ và lợn bản nướng thơm phức."
    ],
    "itinerary": [
      {
        "day": "Đêm 0",
        "title": "Hà Nội – Tú Lệ",
        "desc": "19:00 xuất phát từ 55 Nguyễn Quốc Trị & 489 Hoàng Quốc Việt đi Tú Lệ. Nghỉ đêm homestay."
      },
      {
        "day": "Ngày 1",
        "title": "Bản Tu San – Lán nghỉ 2.400m",
        "desc": "Trek qua rừng trúc, rừng thảo quả và suối trong. Chiều đến lán nghỉ ngắm hoàng hôn mây bồng bềnh."
      },
      {
        "day": "Ngày 2",
        "title": "Chạm đỉnh Lùng Cúng 2.913m – Hà Nội",
        "desc": "Sáng sớm chạm đỉnh ngắm bình minh 360 độ. Xuống núi về Tú Lệ, ăn trưa và lên xe về Hà Nội."
      }
    ],
    "included": [
      "Xe ô tô giường nằm khứ hồi Hà Nội – Tú Lệ",
      "Lán nghỉ trên núi, túi ngủ ấm",
      "Porter bản địa & Leader theo sát chăm sóc",
      "Huy chương gỗ Lùng Cúng độc quyền",
      "Bảo hiểm du lịch 100.000.000đ/người"
    ],
    "preparation": [
      "Giày leo núi có gai",
      "Áo gió giữ ấm",
      "CCCD bản gốc"
    ]
  },
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
    "isFeatured": false,
    "reviews": 76,
    "shortSummary": "Chinh phục đỉnh núi Sừng Trâu hoang dã, chiêm ngưỡng Thác Ong Chúa tuyệt mỹ và rừng thảo quả ngát hương.",
    "routeMap": "Từ Hà Nội qua Sapa đến bản Nhìu Cồ San (Bát Xát). Cung đường đưa bạn qua Thác Ong Chúa kỳ vĩ tung bọt trắng xóa, xuyên rừng đỗ quyên và rừng trúc lên chóp inox 2.965m.",
    "routeSteps": [
      "Hà Nội",
      "Sapa",
      "Bản Nhìu Cồ San",
      "Thác Ong Chúa",
      "Lán nghỉ",
      "Đỉnh Nhìu Cồ San (2.965m)"
    ],
    "historyStory": "Nhìu Cồ San theo tiếng người H’Mông có nghĩa là 'núi ba sừng trâu'. Với độ cao 2.965m (top 9 ngọn núi cao nhất Việt Nam), nơi đây còn lưu giữ con đường đá cổ Pavi thời Pháp thuộc chạy xuyên qua đại ngàn.",
    "description": "Cung leo núi giàu trải nghiệm thiên nhiên với thác nước tuyệt đẹp, khu rừng nguyên sinh rêu phong và đỉnh cao lộng gió.",
    "departureDates": [
      "01/11/2026",
      "08/11/2026",
      "15/11/2026",
      "22/11/2026"
    ],
    "highlights": [
      "Chiêm ngưỡng Thác Ong Chúa hùng vĩ tuôn dòng nước mát lạnh giữa vách đá dựng đứng.",
      "Check-in chóp inox 2.965m ngắm trọn vẹn dải Hoàng Liên Sơn mờ ảo trong mây.",
      "Tắm lá thuốc người Dao đỏ tại Sapa hồi phục sức khỏe sau chuyến đi."
    ],
    "itinerary": [
      {
        "day": "Đêm 0",
        "title": "Hà Nội – Sapa – Bát Xát",
        "desc": "21:30 xe giường nằm đón tại 55 Nguyễn Quốc Trị & 489 Hoàng Quốc Việt đi Lào Cai."
      },
      {
        "day": "Ngày 1",
        "title": "Bản Nhìu Cồ San – Thác Ong Chúa – Lán",
        "desc": "Check-in Thác Ong Chúa tráng lệ, vượt rừng rêu và đỗ quyên lên lán nghỉ ngơi."
      },
      {
        "day": "Ngày 2",
        "title": "Chạm đỉnh 2.965m – Tắm lá thuốc – Hà Nội",
        "desc": "Đón bình minh trên đỉnh núi, xuống chân núi tắm lá thuốc Dao đỏ Sapa, lên xe về Hà Nội lúc 21:00."
      }
    ],
    "included": [
      "Xe giường nằm khứ hồi Hà Nội – Lào Cai",
      "Lán ngủ trên núi có túi ngủ ấm",
      "Porter bản địa & Leader chu đáo",
      "Tắm lá thuốc người Dao đỏ",
      "Huy chương gỗ Nhìu Cồ San kỷ niệm",
      "Bảo hiểm du lịch 100.000.000đ/người"
    ],
    "preparation": [
      "Giày trekking chống trơn",
      "Áo ấm, tất dài",
      "CCCD bản gốc"
    ]
  },
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
    "isFeatured": false,
    "reviews": 160,
    "shortSummary": "Hành trình tự thân leo bộ chinh phục đỉnh Fansipan 3.143m kiêu hãnh – cột mốc lịch sử của mọi trekker Việt Nam.",
    "routeMap": "Từ Hà Nội lên thị xã Sapa. Xuất phát từ Trạm Tôn (1.900m), men theo rừng trúc và khe suối lên lán 2.800m nghỉ đêm, sáng sớm vượt dốc đá dựng đứng chạm chóp inox 3.143m.",
    "routeSteps": [
      "Hà Nội",
      "Sapa",
      "Trạm Tôn (1.900m)",
      "Lán 2.800m",
      "Đỉnh Fansipan (3.143m)"
    ],
    "historyStory": "Fansipan cao 3.143m là ngọn núi cao nhất ba nước Việt Nam – Lào – Campuchia, được xưng tụng là 'Nóc nhà Đông Dương'. Chinh phục Fansipan bằng chính đôi chân mình trên cung đường Trạm Tôn là niềm tự hào của hàng ngàn bạn trẻ đam mê phiêu lưu.",
    "description": "Cung trekking kinh điển vượt qua giới hạn bản thân, chiêm ngưỡng quần thể tâm linh kỳ vĩ trên đỉnh mây ngàn.",
    "departureDates": [
      "01/11/2026",
      "08/11/2026",
      "15/11/2026",
      "22/11/2026"
    ],
    "highlights": [
      "Tự hào chạm tay vào chóp inox 3.143m – Nóc nhà Đông Dương bằng chính sức lực của mình.",
      "Chiêm ngưỡng biển mây bao la và Đại tượng Phật A Di Đà sừng sững giữa trời xanh.",
      "Nhận giấy chứng nhận và huy chương chinh phục Fansipan độc quyền từ Đi Cùng Gió."
    ],
    "itinerary": [
      {
        "day": "Ngày 0",
        "title": "Hà Nội – Sapa",
        "desc": "21:30 xe giường nằm chất lượng cao đón tại Hà Nội đi Sapa."
      },
      {
        "day": "Ngày 1",
        "title": "Trạm Tôn – Lán 2.800m",
        "desc": "Khởi hành từ Trạm Tôn, băng qua rừng trúc và suối đá. Đến lán 2.800m nghỉ đêm, ngắm bầu trời sao rực rỡ."
      },
      {
        "day": "Ngày 2",
        "title": "Chạm đỉnh Fansipan 3.143m – Hà Nội",
        "desc": "06:00 đón bình minh trên Nóc nhà Đông Dương. Xuống núi Trạm Tôn, tắm lá thuốc Dao đỏ và về Hà Nội."
      }
    ],
    "included": [
      "Xe giường nằm khứ hồi Hà Nội – Sapa",
      "Giấy phép leo núi Fansipan của Vườn Quốc Gia Hoàng Liên",
      "Lán ngủ 2.800m có chăn ấm, túi ngủ",
      "Leader & Porter bản địa dày dạn kinh nghiệm",
      "Huy chương gỗ độc quyền Đi Cùng Gió",
      "Bảo hiểm du lịch 100.000.000đ/người"
    ],
    "preparation": [
      "Giày trekking chuyên dụng bám dốc",
      "Áo gió chống mưa tuyết",
      "Găng tay, tất dài",
      "CCCD bản gốc"
    ]
  },
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
    "isFeatured": false,
    "reviews": 65,
    "shortSummary": "Hành hương về am thiêng Ngọa Vân – nơi Phật hoàng Trần Nhân Tông hóa Phật và nhập Niết bàn.",
    "routeMap": "Từ Hà Nội theo QL18 đi thị xã Đông Triều (Quảng Ninh). Tuyến trekking men theo rừng thông và suối xanh, qua chùa Trại Cấp, dốc Đô Kiệu và viếng Am Ngọa Vân thanh tịnh trên đỉnh mây.",
    "routeSteps": [
      "Hà Nội",
      "Đông Triều",
      "Chùa Trại Cấp",
      "Dốc Đô Kiệu",
      "Am Ngọa Vân"
    ],
    "historyStory": "Am Ngọa Vân nằm trên ngọn núi Bảo Đài thuộc dãy cánh cung Đông Triều. Đây là thánh địa tối thượng của Phật giáo Trúc Lâm, nơi Phật hoàng Trần Nhân Tông tu hành những năm tháng cuối đời và viên tịch hóa Phật vào ngày 1 tháng 11 năm Mậu Thân (1308).",
    "description": "Cung hành hương thanh tịnh giữa rừng thông ngát hương, lắng nghe tiếng chuông chùa thanh thản giữa non thiêng.",
    "departureDates": [
      "01/11/2026",
      "08/11/2026",
      "15/11/2026",
      "22/11/2026"
    ],
    "highlights": [
      "Chiêm bái Am tháp Ngọa Vân nơi Phật hoàng Trần Nhân Tông nhập Niết bàn.",
      "Dạo bước trên cung đường bậc đá rợp bóng rừng thông ngàn năm tuổi.",
      "Thưởng thức cơm chay thanh đạm và cảm nhận sự thanh thản trong tâm hồn."
    ],
    "itinerary": [
      {
        "day": "06:00",
        "title": "Hà Nội – Đông Triều",
        "desc": "Xe đón tại 55 Nguyễn Quốc Trị & 489 Hoàng Quốc Việt đi Đông Triều (Quảng Ninh)."
      },
      {
        "day": "08:30",
        "title": "Trekking Am Ngọa Vân",
        "desc": "Trekking qua dốc Đô Kiệu, rừng trúc và đồi thông xanh ngát."
      },
      {
        "day": "12:00",
        "title": "Chiêm bái & Ăn trưa",
        "desc": "Dâng hương tại Am Ngọa Vân trên đỉnh núi, dùng bữa trưa picnic thanh tịnh."
      },
      {
        "day": "15:30",
        "title": "Xuống núi về Hà Nội",
        "desc": "Xuống chân núi, lên xe trở về Hà Nội lúc 18:30."
      }
    ],
    "included": [
      "Xe ô tô đưa đón khứ hồi từ Hà Nội",
      "Hướng dẫn viên theo sát lịch trình",
      "Nước uống tinh khiết 500ml",
      "Huy chương gỗ độc quyền kỷ niệm",
      "Bảo hiểm du lịch trọn gói 20.000.000đ"
    ],
    "preparation": [
      "Trang phục lịch sự kín đáo",
      "Giày thể thao bám tốt",
      "CCCD bản gốc"
    ]
  },
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
    "isFeatured": false,
    "reviews": 52,
    "shortSummary": "Hành hương leo núi Thanh Đằng, chiêm bái đại bảo tháp chùa Ba Vàng và ngắm toàn cảnh sông núi Uông Bí.",
    "routeMap": "Từ Hà Nội đi Uông Bí, trekking theo sườn đồi thông núi Thanh Đằng thoai thoải, viếng thăm chùa Ba Vàng và dạo bước an lạc giữa thiên nhiên.",
    "routeSteps": [
      "Hà Nội",
      "Uông Bí",
      "Chân núi Thanh Đằng",
      "Chùa Ba Vàng",
      "Đỉnh đồi thông"
    ],
    "historyStory": "Núi Thanh Đằng tọa lạc tại vị trí phong thủy đắc địa 'tiền hữu ngoạn thủy, hậu hữu ỷ sơn'. Đây là vùng đất tâm linh thanh bình nằm kề bên quần thể di tích danh thắng Yên Tử.",
    "description": "Chuyến đi trong ngày nhẹ nhàng phù hợp mọi lứa tuổi, kết hợp rèn luyện sức khỏe và hành hương thanh tịnh.",
    "departureDates": [
      "01/11/2026",
      "08/11/2026",
      "15/11/2026",
      "22/11/2026"
    ],
    "highlights": [
      "Chiêm bái ngôi chùa có tòa Chính điện trên núi lớn nhất Việt Nam.",
      "Dạo bước giữa rừng thông thơ mộng ngắm thành phố Uông Bí từ trên cao.",
      "Thưởng thức các món chay thanh lọc cơ thể và tâm trí."
    ],
    "itinerary": [
      {
        "day": "06:30",
        "title": "Hà Nội – Uông Bí",
        "desc": "Đón khách tại 55 Nguyễn Quốc Trị & 489 Hoàng Quốc Việt khởi hành đi Uông Bí."
      },
      {
        "day": "09:00",
        "title": "Trekking núi Thanh Đằng",
        "desc": "Băng qua đồi thông xanh ngát, hít thở không khí thanh trong."
      },
      {
        "day": "12:00",
        "title": "Chiêm bái & Nghỉ trưa",
        "desc": "Dâng hương lễ Phật tại chùa Ba Vàng, dùng bữa cơm trưa thanh tịnh."
      },
      {
        "day": "15:00",
        "title": "Về lại Hà Nội",
        "desc": "Lên xe khởi hành về Hà Nội, kết thúc chuyến đi lúc 18:00."
      }
    ],
    "included": [
      "Xe đưa đón khứ hồi",
      "HDV theo sát",
      "Nước uống & Bữa trưa chay",
      "Bảo hiểm du lịch"
    ],
    "preparation": [
      "Trang phục trang nhã",
      "Giày êm",
      "CCCD bản gốc"
    ]
  },
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
    "isFeatured": false,
    "reviews": 48,
    "shortSummary": "Hành trình kết hợp chiêm bái tâm linh Thành Đẳng và check-in đồi cỏ cháy Phượng Hoàng đẹp như thảo nguyên Mông Cổ.",
    "routeMap": "Từ Hà Nội đi Uông Bí, hành hương chiêm bái Thành Đẳng buổi sáng, buổi chiều trekking chinh phục Đồi Phượng Hoàng với thảo nguyên cỏ vàng óng ánh.",
    "routeSteps": [
      "Hà Nội",
      "Uông Bí",
      "Thành Đẳng",
      "Đồi Phượng Hoàng",
      "Thảo nguyên cỏ cháy"
    ],
    "historyStory": "Đồi Phượng Hoàng được mệnh danh là 'thảo nguyên Đà Lạt thu nhỏ' của Quảng Ninh. Mùa thu đông, những triền cỏ chuyển sang màu vàng cháy thơ mộng tạo nên khung cảnh lãng mạn vô cùng cuốn hút.",
    "description": "Chuyến trekking check-in sống ảo cực đẹp kết hợp viếng cảnh chùa thanh tịnh trong một ngày cuối tuần.",
    "departureDates": [
      "01/11/2026",
      "08/11/2026",
      "15/11/2026",
      "22/11/2026"
    ],
    "highlights": [
      "Check-in đồi cỏ cháy Phượng Hoàng ngút ngàn đẹp ngỡ ngàng.",
      "Hành hương chiêm bái cầu bình an, may mắn cho gia đình.",
      "Chụp những bức ảnh kỷ niệm tuyệt đẹp giữa thảo nguyên mộng mơ."
    ],
    "itinerary": [
      {
        "day": "06:00",
        "title": "Hà Nội – Uông Bí",
        "desc": "Xuất phát từ Hà Nội đi Uông Bí."
      },
      {
        "day": "09:00",
        "title": "Chiêm bái Thành Đẳng",
        "desc": "Hành hương lễ Phật cầu bình an giữa không gian thanh tịnh."
      },
      {
        "day": "13:30",
        "title": "Trekking Đồi Phượng Hoàng",
        "desc": "Chinh phục đỉnh đồi, ngắm toàn cảnh thung lũng cỏ cháy vàng rực lúc hoàng hôn."
      },
      {
        "day": "16:30",
        "title": "Về Hà Nội",
        "desc": "Lên xe về lại thủ đô lúc 19:30."
      }
    ],
    "included": [
      "Xe đưa đón khứ hồi",
      "Leader Đi Cùng Gió",
      "Nước uống, đồ y tế",
      "Huy chương gỗ độc quyền",
      "Bảo hiểm du lịch"
    ],
    "preparation": [
      "Trang phục màu nổi bật chụp ảnh",
      "Giày thể thao",
      "CCCD bản gốc"
    ]
  },
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
    "isFeatured": false,
    "reviews": 79,
    "shortSummary": "Du ngoạn vịnh Ngòi Hoa trên hồ Hòa Bình xanh biếc, khám phá Hồ Mắt Ngọc bí ẩn và hang động thạch nhũ kỳ vĩ.",
    "routeMap": "Từ Hà Nội đi cảng Ngòi Hoa (Tân Lạc, Hòa Bình). Lên thuyền du ngoạn ngắm các đảo đá vôi xanh ngọc, trekking nhẹ vào bản người Mường và khám phá Hồ Mắt Ngọc tuyệt đẹp.",
    "routeSteps": [
      "Hà Nội",
      "TP Hòa Bình",
      "Cảng Ngòi Hoa",
      "Du thuyền lòng hồ",
      "Hồ Mắt Ngọc & Hang thạch nhũ"
    ],
    "historyStory": "Lòng hồ sông Đà được ví như 'Vịnh Hạ Long trên cạn của miền Tây Bắc'. Nơi đây nổi tiếng với phong cảnh sơn thủy hữu tình, dòng nước trong xanh như ngọc bích và bản sắc văn hóa Mường đặc sắc.",
    "description": "Một ngày trốn khói bụi thủ đô, hòa mình vào làn nước mát lành và thiên nhiên non xanh nước biếc của dòng sông Đà huyền thoại.",
    "departureDates": [
      "01/11/2026",
      "08/11/2026",
      "15/11/2026",
      "22/11/2026"
    ],
    "highlights": [
      "Du thuyền lướt trên mặt hồ xanh ngắt giữa trập trùng đảo đá vôi hoang sơ.",
      "Khám phá Hồ Mắt Ngọc nước trong nhìn thấu đáy và hang thạch nhũ kỳ ảo.",
      "Thưởng thức cá nướng sông Đà và gà đồi thơm lừng tại nhà bè nổi."
    ],
    "itinerary": [
      {
        "day": "05:00",
        "title": "Hà Nội – TP Hòa Bình – Cảng Ngòi Hoa",
        "desc": "Xe đón tại 55 Nguyễn Quốc Trị & 489 Hoàng Quốc Việt đi Hòa Bình. Ăn sáng tại TP Hòa Bình."
      },
      {
        "day": "08:30",
        "title": "Du thuyền vịnh Ngòi Hoa",
        "desc": "Lên thuyền ngắm vịnh Ngòi Hoa, chèo SUP trên mặt nước xanh ngọc."
      },
      {
        "day": "11:30",
        "title": "Ăn trưa cá sông Đà & Khám phá Hồ Mắt Ngọc",
        "desc": "Ăn trưa đặc sản vùng hồ. Buổi chiều trekking khám phá hang động thạch nhũ và Hồ Mắt Ngọc."
      },
      {
        "day": "16:00",
        "title": "Về lại Hà Nội",
        "desc": "Lên xe về lại thủ đô, kết thúc hành trình lúc 19:00."
      }
    ],
    "included": [
      "Xe ô tô du lịch đời mới khứ hồi",
      "Thuyền tham quan chuyên dụng trên hồ Hòa Bình",
      "Bữa ăn trưa đặc sản cá sông Đà tươi ngon",
      "Leader & Áo phao an toàn tuyệt đối",
      "Huy chương gỗ kỷ niệm độc quyền",
      "Bảo hiểm du lịch 20.000.000đ"
    ],
    "preparation": [
      "Quần áo dự phòng thay khi tắm hồ",
      "Kem chống nắng",
      "CCCD bản gốc"
    ]
  },
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
    "isFeatured": false,
    "reviews": 103,
    "shortSummary": "Lội suối băng rừng nguyên sinh Đại Từ, trượt máng đá tự nhiên và nhảy thác mát lạnh tại suối Cửa Tử.",
    "routeMap": "Từ Hà Nội theo cao tốc Hà Nội – Thái Nguyên đến chân suối Cửa Tử (xã Hoàng Nông, Đại Từ). Tuyến trekking lội dọc dòng suối đá trong vắt, vượt Cửa 1, Cửa 2 và Cửa 3 với những thác nước tuyệt mỹ.",
    "routeSteps": [
      "Hà Nội",
      "Đại Từ (Thái Nguyên)",
      "Cửa 1 (Máng trượt đá)",
      "Cửa 2 (Bể bơi tự nhiên)",
      "Cửa 3 (Thác nước đại ngàn)"
    ],
    "historyStory": "Suối Cửa Tử bắt nguồn từ sườn Đông dãy Tam Đảo chảy xuống thung lũng Hoàng Nông. Dòng nước mát lạnh quanh năm chảy len lỏi qua những khối đá cuội khổng lồ và rừng cây cổ thụ nhiệt đới xanh rì.",
    "description": "Trải nghiệm vượt suối tắm thác cực sảng khoái và xua tan mọi căng thẳng oi bức của mùa hè miền Bắc.",
    "departureDates": [
      "01/11/2026",
      "08/11/2026",
      "15/11/2026",
      "22/11/2026"
    ],
    "highlights": [
      "Trượt máng đá tự nhiên dài hàng chục mét trút thẳng xuống làn nước trong vắt.",
      "Bơi lội thỏa thích giữa các hồ nước tự nhiên xanh biếc như ngọc bích.",
      "Thưởng thức gà nướng lá móc mật và chè búp Tân Cương Thái Nguyên thơm lừng."
    ],
    "itinerary": [
      {
        "day": "05:30",
        "title": "Hà Nội – Đại Từ Thái Nguyên",
        "desc": "Đón đoàn tại 55 Nguyễn Quốc Trị & 489 Hoàng Quốc Việt đi Thái Nguyên."
      },
      {
        "day": "08:30",
        "title": "Bắt đầu trek lội suối Cửa Tử",
        "desc": "Trang bị áo phao, khởi động và bắt đầu lội dọc con suối đá hoang sơ."
      },
      {
        "day": "12:00",
        "title": "Ăn trưa picnic bên bờ suối",
        "desc": "Ăn trưa thịt nướng, xôi nếp nóng hổi bên bờ thác róc rách."
      },
      {
        "day": "14:00",
        "title": "Trượt máng đá Cửa 2 & Nhảy thác",
        "desc": "Trải nghiệm trượt máng đá tự nhiên cảm giác mạnh cực vui."
      },
      {
        "day": "16:30",
        "title": "Về lại Hà Nội",
        "desc": "Tắm tráng nước ngọt, lên xe về lại thủ đô lúc 19:00."
      }
    ],
    "included": [
      "Xe đưa đón khứ hồi Hà Nội – Cửa Tử",
      "Áo phao an toàn cá nhân & Túi chống nước",
      "Porter bản địa & Leader nhiều kinh nghiệm suối",
      "Bữa ăn trưa nóng sốt bên bờ thác",
      "Huy chương gỗ độc quyền của Đi Cùng Gió",
      "Bảo hiểm du lịch trọn gói 20.000.000đ"
    ],
    "preparation": [
      "Giày lội suối hoặc quai hậu bám đá",
      "2 bộ quần áo khô thay",
      "Túi chống nước điện thoại",
      "CCCD bản gốc"
    ]
  },
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
    "isFeatured": false,
    "reviews": 89,
    "shortSummary": "Lạc bước giữa hàng vạn cánh bướm rợp trời, chiêm bái Cây Chò ngàn năm tuổi giữa rừng già Cúc Phương.",
    "routeMap": "Từ Hà Nội theo QL1A đi Nho Quan (Ninh Bình). Tuyến trekking xuyên qua lối mòn rừng già rợp bóng cây cổ thụ, viếng Động Người Xưa và Cây Chò chỉ ngàn năm tuổi.",
    "routeSteps": [
      "Hà Nội",
      "Cổng Vườn Cúc Phương",
      "Động Người Xưa",
      "Rừng nguyên sinh mùa bướm",
      "Cây Chò ngàn năm"
    ],
    "historyStory": "Cúc Phương là vườn quốc gia đầu tiên tại Việt Nam, thành lập năm 1962. Nơi đây bảo tồn hệ động thực vật nhiệt đới vô cùng phong phú và nổi tiếng thế giới với mùa bướm hàng triệu con bay rợp trời vào mỗi độ đầu hạ.",
    "description": "Chuyến dã ngoại rừng già trong lành, khám phá thiên nhiên hoang dã kỳ thú phù hợp cả gia đình và trẻ nhỏ.",
    "departureDates": [
      "01/11/2026",
      "08/11/2026",
      "15/11/2026",
      "22/11/2026"
    ],
    "highlights": [
      "Ngắm nhìn hàng triệu cánh bướm trắng, vàng bay rợp các con đường mòn xuyên rừng.",
      "Ôm thân Cây Chò ngàn năm tuổi sừng sững giữa lõi rừng nguyên sinh.",
      "Tham quan Trung tâm Cứu hộ Linh trưởng Quý hiếm hàng đầu Đông Nam Á."
    ],
    "itinerary": [
      {
        "day": "06:00",
        "title": "Hà Nội – Ninh Bình",
        "desc": "Xe đón tại 55 Nguyễn Quốc Trị & 489 Hoàng Quốc Việt đi VQG Cúc Phương."
      },
      {
        "day": "08:30",
        "title": "Trekking xuyên rừng & Săn bướm",
        "desc": "Check-in ngắm hàng đàn bướm bay rực rỡ, viếng Động Người Xưa."
      },
      {
        "day": "12:00",
        "title": "Ăn trưa đặc sản Ninh Bình",
        "desc": "Ăn trưa cơm cháy, dê núi tại nhà hàng trong rừng."
      },
      {
        "day": "14:00",
        "title": "Chinh phục Cây Chò ngàn năm",
        "desc": "Trekking 3km đường mòn ngắm Cây Chò đại thụ."
      },
      {
        "day": "16:00",
        "title": "Về lại Hà Nội",
        "desc": "Lên xe về lại thủ đô lúc 18:30."
      }
    ],
    "included": [
      "Xe ô tô đưa đón khứ hồi Hà Nội – Cúc Phương",
      "Vé vào cổng Vườn Quốc Gia Cúc Phương",
      "Leader hướng dẫn khám phá sinh thái",
      "Bữa ăn trưa đặc sản Ninh Bình thơm ngon",
      "Bảo hiểm du lịch trọn gói 20.000.000đ"
    ],
    "preparation": [
      "Trang phục thoải mái, chống muỗi",
      "Giày thể thao",
      "CCCD bản gốc"
    ]
  },
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
    "isFeatured": false,
    "reviews": 112,
    "shortSummary": "Trekking xuyên rừng thông bạt ngàn, khám phá Nhà Thờ Đổ Pháp cổ kính và chạm đỉnh Vua 1.296m.",
    "routeMap": "Từ nội thành Hà Nội đi Vườn Quốc Gia Ba Vì (60km). Tuyến trek qua rừng thông cốt 400, viếng Nhà Thờ Đổ rêu phong ma mị và leo bậc đá lên Đền Thượng thờ Tản Viên Sơn Thánh.",
    "routeSteps": [
      "Hà Nội",
      "Cổng VQG Ba Vì",
      "Rừng thông Cốt 400",
      "Nhà Thờ Đổ cổ kính",
      "Đỉnh Vua (1.296m)"
    ],
    "historyStory": "Dãy núi Ba Vì gắn liền với truyền thuyết Sơn Tinh – Thủy Tinh bất hủ trong tâm thức người Việt. Nơi đây có khí hậu á nhiệt đới mát mẻ quanh năm cùng những công trình kiến trúc Pháp cổ kính phủ đầy rêu phong.",
    "description": "Cung trekking gần gũi nhất với Hà Nội, không khí trong lành như Đà Lạt, thích hợp nạp lại năng lượng sau tuần làm việc bận rộn.",
    "departureDates": [
      "01/11/2026",
      "08/11/2026",
      "15/11/2026",
      "22/11/2026"
    ],
    "highlights": [
      "Check-in Nhà Thờ Đổ Pháp cổ kính huyền bí giữa rừng già mây phủ.",
      "Chinh phục Đỉnh Vua cao 1.296m viếng Đền Thượng linh thiêng.",
      "Thưởng thức gà đồi nướng than hoa và sữa tươi Ba Vì béo ngậy."
    ],
    "itinerary": [
      {
        "day": "06:30",
        "title": "Hà Nội – Ba Vì",
        "desc": "Xe đón tại 55 Nguyễn Quốc Trị & 489 Hoàng Quốc Việt đi Ba Vì."
      },
      {
        "day": "08:30",
        "title": "Trekking Rừng thông cốt 400 & Nhà Thờ Đổ",
        "desc": "Băng qua những cánh rừng thông ngút ngàn, chụp ảnh sống ảo tại Nhà Thờ Đổ."
      },
      {
        "day": "11:30",
        "title": "Ăn trưa gà đồi nướng",
        "desc": "Dùng bữa trưa nóng sốt với đặc sản gà đồi Ba Vì."
      },
      {
        "day": "13:30",
        "title": "Leo Đền Thượng Đỉnh Vua",
        "desc": "Leo bậc đá lên đỉnh Vua 1.296m ngắm mây trôi lãng đãng."
      },
      {
        "day": "16:00",
        "title": "Về lại Hà Nội",
        "desc": "Lên xe về lại nội thành lúc 18:00."
      }
    ],
    "included": [
      "Xe đưa đón khứ hồi",
      "Vé cổng VQG Ba Vì",
      "Bữa trưa đặc sản gà đồi",
      "Leader theo sát",
      "Huy chương gỗ độc quyền",
      "Bảo hiểm du lịch"
    ],
    "preparation": [
      "Giày thể thao",
      "Áo khoác nhẹ",
      "CCCD bản gốc"
    ]
  },
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
    "isFeatured": false,
    "reviews": 98,
    "shortSummary": "Cung trekking rèn luyện thể lực cuối tuần cực vui, leo dốc rừng thông và cắm trại chill bên hồ Suối Bàu.",
    "routeMap": "Từ trung tâm Hà Nội đi Sóc Sơn (40km). Tuyến trek bắt đầu từ chân hồ Suối Bàu, men theo suối đá hoặc leo dốc rừng thông lên đỉnh Hàm Lợn (462m).",
    "routeSteps": [
      "Hà Nội",
      "Sóc Sơn",
      "Hồ Suối Bàu",
      "Cung suối đá / Rừng thông",
      "Đỉnh Hàm Lợn (462m)"
    ],
    "historyStory": "Núi Hàm Lợn thuộc dãy Độc Tôn (Sóc Sơn), là đỉnh núi cao nhất Hà Nội (462m). Nơi đây từ lâu là 'thao trường' quen thuộc của cộng đồng phượt thủ miền Bắc tập dượt thể lực trước khi chinh phục các cung lớn như Fansipan hay Kỳ Quan San.",
    "description": "Chuyến dã ngoại cuối tuần vui vẻ, tiết kiệm, phù hợp nhóm bạn trẻ, sinh viên và các gia đình muốn vận động nhẹ nhàng.",
    "departureDates": [
      "26/10/2026",
      "02/11/2026",
      "09/11/2026",
      "16/11/2026"
    ],
    "highlights": [
      "Chạm đỉnh 'Nóc nhà Thủ đô' Hàm Lợn và ngắm trọn hồ Suối Bàu từ trên cao.",
      "Check-in rừng thông bạt ngàn ngỡ như Đà Lạt thu nhỏ chỉ cách Hà Nội 1 tiếng đi xe.",
      "Cắm trại picnic, nướng BBQ và thưởng thức cà phê thư giãn bên hồ nước thơ mộng."
    ],
    "itinerary": [
      {
        "day": "07:00",
        "title": "Hà Nội – Sóc Sơn",
        "desc": "Xe đón tại 55 Nguyễn Quốc Trị & 489 Hoàng Quốc Việt đi Sóc Sơn."
      },
      {
        "day": "08:30",
        "title": "Bắt đầu leo đỉnh Hàm Lợn",
        "desc": "Khởi động và trekking qua rừng thông bạt ngàn lên đỉnh 462m."
      },
      {
        "day": "11:30",
        "title": "Chạm đỉnh & Xuống hồ Suối Bàu",
        "desc": "Chụp ảnh tại cột mốc nóc nhà Hà Nội, di chuyển xuống hồ Suối Bàu hạ trại ăn trưa BBQ."
      },
      {
        "day": "15:30",
        "title": "Về lại Hà Nội",
        "desc": "Thu dọn rác, lên xe về lại nội thành lúc 17:00."
      }
    ],
    "included": [
      "Xe ô tô đưa đón khứ hồi",
      "Leader hướng dẫn & Bữa trưa BBQ picnic bên hồ",
      "Nước uống tinh khiết & đồ sơ cứu cơ bản",
      "Huy chương gỗ Hàm Lợn độc quyền",
      "Bảo hiểm du lịch 20.000.000đ"
    ],
    "preparation": [
      "Giày thể thao êm chân",
      "Mũ nón chống nắng",
      "CCCD bản gốc"
    ]
  },
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
    "isFeatured": false,
    "reviews": 45,
    "shortSummary": "Gói tour dành cho khách tự di chuyển xe riêng đến Thái Nguyên, lội suối Cửa Tử và trượt máng đá an toàn cùng Leader bản địa.",
    "routeMap": "Đón khách trực tiếp tại chân suối Cửa Tử (Hoàng Nông, Đại Từ, Thái Nguyên). Leader trang bị áo phao và dẫn đoàn lội suối khám phá các máng trượt đá tự nhiên.",
    "routeSteps": [
      "Chân suối Cửa Tử",
      "Cửa 1",
      "Cửa 2",
      "Máng trượt tự nhiên"
    ],
    "historyStory": "Dành cho các nhóm bạn, gia đình tự lái xe ô tô hoặc xe máy lên Thái Nguyên, cần dịch vụ hướng dẫn an toàn, porter bản địa và trang thiết bị áo phao chuyên nghiệp.",
    "description": "Trải nghiệm lội suối vượt thác cực chill và an toàn với chi phí tiết kiệm nhất.",
    "departureDates": [
      "01/11/2026",
      "08/11/2026",
      "15/11/2026",
      "22/11/2026"
    ],
    "highlights": [
      "Leader địa phương dẫn đường an toàn tuyệt đối.",
      "Trang bị áo phao chuyên dụng và túi chống nước cho cả đoàn.",
      "Tự do khám phá trượt máng đá và bơi lội giữa hồ nước trong vắt."
    ],
    "itinerary": [
      {
        "day": "08:30",
        "title": "Đón tại chân suối",
        "desc": "Tập trung tại homestay chân suối Cửa Tử, phổ biến quy tắc an toàn."
      },
      {
        "day": "09:00",
        "title": "Lội suối vượt thác",
        "desc": "Trekking lội suối, trượt máng đá Cửa 1 và Cửa 2."
      },
      {
        "day": "12:00",
        "title": "Ăn trưa bên bờ suối",
        "desc": "Ăn trưa picnic thơm ngon giữa tiếng suối chảy róc rách."
      },
      {
        "day": "15:00",
        "title": "Kết thúc tour",
        "desc": "Trở về chân suối tắm tráng, chia tay đoàn."
      }
    ],
    "included": [
      "Leader & Porter bản địa",
      "Áo phao an toàn",
      "Bữa trưa picnic",
      "Bảo hiểm du lịch"
    ],
    "preparation": [
      "Giày lội suối bám đá",
      "Quần áo khô thay",
      "CCCD bản gốc"
    ]
  },
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
    "isFeatured": false,
    "reviews": 56,
    "shortSummary": "Hành trình mang áo ấm và quà tặng đến với các em nhỏ điểm trường vùng cao khó khăn tại Mù Cang Chải.",
    "routeMap": "Từ Hà Nội qua đèo Khau Phạ đến các điểm trường mầm non và tiểu học vùng sâu tại Mù Cang Chải (Yên Bái). Trao quà thiện nguyện, giao lưu văn nghệ và trekking nhẹ thăm bản làng người Mông.",
    "routeSteps": [
      "Hà Nội",
      "Đèo Khau Phạ",
      "Điểm trường vùng cao",
      "Treo áo ấm & Tặng quà",
      "Giao lưu bản Mông"
    ],
    "historyStory": "Chương trình thường niên của cộng đồng Đi Cùng Gió nhằm kết nối những trái tim nhân ái, trao gửi sự ấm áp đến trẻ em vùng cao trước mùa đông giá buốt.",
    "description": "Một chuyến đi đong đầy ý nghĩa nhân văn, nơi mỗi bước chân đều mang lại nụ cười và niềm hy vọng cho các em nhỏ vùng cao.",
    "departureDates": [
      "15/11/2026",
      "29/11/2026",
      "13/12/2026"
    ],
    "highlights": [
      "Trực tiếp trao tận tay những chiếc áo ấm, sách vở và bữa ăn dinh dưỡng cho các em nhỏ khó khăn.",
      "Giao lưu nhảy sạp, đốt lửa trại ấm áp cùng đồng bào vùng cao.",
      "Ngắm hoàng hôn đèo Khau Phạ – một trong 'Tứ đại đỉnh đèo' Tây Bắc."
    ],
    "itinerary": [
      {
        "day": "Ngày 1",
        "title": "Hà Nội – Khau Phạ – Điểm trường Mù Cang Chải",
        "desc": "Xe đón tại Hà Nội. Chiều đến điểm trường trao quà áo ấm, đồ dùng học tập cho các bé."
      },
      {
        "day": "Ngày 2",
        "title": "Giao lưu bản làng – Hà Nội",
        "desc": "Trekking thăm bản người Mông, thưởng thức đặc sản xôi nếp Tú Lệ. Chiều về lại Hà Nội."
      }
    ],
    "included": [
      "Xe du lịch khứ hồi",
      "Homestay bản địa",
      "Các bữa ăn vùng cao",
      "Điều phối viên thiện nguyện",
      "Bảo hiểm du lịch"
    ],
    "preparation": [
      "Quần áo ấm",
      "Tấm lòng nhiệt huyết",
      "CCCD bản gốc"
    ]
  },
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
    "isFeatured": false,
    "reviews": 42,
    "shortSummary": "Xây dựng tủ sách tri thức, trao học bổng khuyến học và hỗ trợ sửa chữa phòng học cho trẻ em vùng cao Nậm Có.",
    "routeMap": "Từ Hà Nội di chuyển vào xã đặc biệt khó khăn Nậm Có (huyện Mù Cang Chải, Yên Bái). Lắp đặt tủ sách, sơn sửa lớp học và tổ chức ngày hội đọc sách cùng các em nhỏ.",
    "routeSteps": [
      "Hà Nội",
      "Nghĩa Lộ",
      "Xã Nậm Có",
      "Điểm trường",
      "Ngày hội đọc sách"
    ],
    "historyStory": "Dự án phi lợi nhuận hướng tới mục tiêu mang sách truyện hay và nguồn cảm hứng học tập đến với trẻ em các thôn bản xa xôi hẻo lánh vùng Tây Bắc.",
    "description": "Cùng Đi Cùng Gió gieo mầm tri thức, mang lại tương lai tươi sáng hơn cho thế hệ măng non vùng cao.",
    "departureDates": [
      "22/11/2026",
      "06/12/2026",
      "20/12/2026"
    ],
    "highlights": [
      "Trực tiếp lắp đặt tủ sách với hơn 500 đầu sách truyện ý nghĩa cho trường học.",
      "Tổ chức các trò chơi tập thể, kể chuyện và đố vui có thưởng cùng các em.",
      "Thưởng thức không gian thanh bình và tình cảm nồng ấm của người dân bản địa."
    ],
    "itinerary": [
      {
        "day": "Ngày 1",
        "title": "Hà Nội – Xã Nậm Có",
        "desc": "Khởi hành sớm từ Hà Nội. Chiều lắp đặt tủ sách, sơn sửa bàn ghế lớp học."
      },
      {
        "day": "Ngày 2",
        "title": "Ngày hội sách & Về Hà Nội",
        "desc": "Tổ chức ngày hội đọc sách cùng các em học sinh. Chiều lên xe về lại thủ đô lúc 20:00."
      }
    ],
    "included": [
      "Xe đưa đón khứ hồi",
      "Homestay bản địa",
      "Bữa ăn địa phương",
      "Chi phí điều phối dự án",
      "Bảo hiểm du lịch"
    ],
    "preparation": [
      "Sách truyện mang theo ủng hộ",
      "Giày thể thao",
      "CCCD bản gốc"
    ]
  }
];

// ==========================================
// 2. DEPARTURE SCHEDULE DATA (5 KEY TOURS WITH SCARCITY & URGENCY)
// ==========================================
const DEPARTURE_SCHEDULE = [
  {
    "id": "sch-1",
    "day": "26",
    "month": "Th10",
    "code": "PSP01",
    "title": "Tà Xùa – Săn mây",
    "duration": "2 ngày 1 đêm",
    "price": "1.600.000đ",
    "priceNum": 1600000,
    "dateFull": "26/10/2026",
    "status": "🔥 Còn 3 chỗ",
    "statusType": "urgent",
    "tourId": 2
  },
  {
    "id": "sch-2",
    "day": "01",
    "month": "Th11",
    "code": "YT01",
    "title": "Yên Tử – Chùa Đồng",
    "duration": "Trong ngày",
    "price": "550.000đ",
    "priceNum": 550000,
    "dateFull": "01/11/2026",
    "status": "Còn 8 chỗ",
    "statusType": "available",
    "tourId": 1
  },
  {
    "id": "sch-3",
    "day": "08",
    "month": "Th11",
    "code": "PSP02",
    "title": "Phu Sa Phìn – Chinh phục đỉnh cao",
    "duration": "2 ngày 1 đêm",
    "price": "2.800.000đ",
    "priceNum": 2800000,
    "dateFull": "08/11/2026",
    "status": "🔥 Còn 2 chỗ",
    "statusType": "urgent",
    "tourId": 3
  },
  {
    "id": "sch-4",
    "day": "15",
    "month": "Th11",
    "code": "TCN01",
    "title": "Tà Chì Nhù – Mùa Hoa Chi Pâu",
    "duration": "2 ngày 1 đêm",
    "price": "2.800.000đ",
    "priceNum": 2800000,
    "dateFull": "15/11/2026",
    "status": "Còn 6 chỗ",
    "statusType": "available",
    "tourId": 5
  },
  {
    "id": "sch-5",
    "day": "22",
    "month": "Th11",
    "code": "KQ01",
    "title": "Kỳ Quan San – Đỉnh núi hùng vĩ",
    "duration": "3 ngày 2 đêm",
    "price": "3.500.000đ",
    "priceNum": 3500000,
    "dateFull": "22/11/2026",
    "status": "Mở đăng ký",
    "statusType": "open",
    "tourId": 4
  }
];

// ==========================================
// 3. REVIEWS & TESTIMONIALS DATA
// ==========================================
const TESTIMONIALS_DATA = [
  {
    id: 1,
    name: 'Nguyễn Thu Hà',
    role: 'Trekking Tà Xùa – Săn mây',
    verified: true,
    avatar: 'assets/images/avatar-ha.jpg',
    comment: 'Cung đường sống lưng khủng long Tà Xùa đẹp nín thở, hướng dẫn viên nhiệt tình, đồ ăn ngon. Cảm ơn Trekking Đi Cùng Gió đã cho mình một hành trình thật đáng nhớ!',
    rating: 5,
    date: '18/10/2026'
  },
  {
    id: 2,
    name: 'Lê Minh Đức',
    role: 'Trekking Yên Tử – Chùa Đồng',
    verified: true,
    avatar: 'assets/images/avatar-duc.jpg',
    comment: 'Lần đầu leo bộ Yên Tử mà được chạm tay vào Chùa Đồng lúc bình minh mây ngàn. Anh em leader chăm sóc chu đáo, huy chương gỗ độc quyền kỷ niệm rất đẹp.',
    rating: 5,
    date: '12/10/2026'
  },
  {
    id: 3,
    name: 'Trần Thị Mai',
    role: 'Kỳ Quan San – Đỉnh núi hùng vĩ',
    verified: true,
    avatar: 'assets/images/avatar-mai.jpg',
    comment: 'Đỉnh Kỳ Quan San quả thực xứng danh ngọn núi kỳ vĩ. Bình minh Đồi Muối biển mây bạt ngàn vượt xa mọi sự tưởng tượng. Đi Cùng Gió tổ chức cực kỳ chuyên nghiệp!',
    rating: 5,
    date: '05/10/2026'
  }
];

// ==========================================
// 4. APP STATE
// ==========================================
let currentCategory = 'all';
let currentDifficulty = 'all';
let currentDuration = 'all';
let currentSort = 'popular';
let searchKeyword = '';
let showAllTours = false;

let heroCurrentIndex = 0;
let heroSlideTimer = null;
let currentBookingTour = TOURS_DATA[0];
let bookingGuests = 1;
let modalBookingPax = 1;

// Load Wishlist from LocalStorage
let wishlist = new Set();
try {
  const savedWishlist = localStorage.getItem('dicunggio_wishlist');
  if (savedWishlist) {
    wishlist = new Set(JSON.parse(savedWishlist));
  }
} catch (e) {
  console.warn('LocalStorage error:', e);
}

// ==========================================
// 5. INITIALIZATION ON DOM READY
// ==========================================
function initApp() {
  initHeroSlider();
  renderTours();
  renderSchedule();
  setupCategoryFilter();
  setupScrollSpy();
  setupBookingModalEvents();
  setupReviewsModalEvents();
  setupScrollReveal();
  updateWishlistBadges();
  initLucideIcons();
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initApp);
} else {
  initApp();
}

function initLucideIcons() {
  if (typeof lucide !== 'undefined' && lucide.createIcons) {
    lucide.createIcons();
  }
}

// Utility: format number to Vietnamese currency VND
function formatCurrency(amount) {
  return new Intl.NumberFormat('vi-VN').format(amount) + 'đ';
}

// ==========================================
// 6. HERO MULTI-SLIDE CONTROLLER (KEN BURNS)
// ==========================================
function initHeroSlider() {
  const slides = document.querySelectorAll('.hero-slide');
  const dots = document.querySelectorAll('.hero-dot');
  if (!slides.length) return;

  function showSlide(index) {
    slides.forEach((slide, i) => {
      if (i === index) {
        slide.classList.add('active');
      } else {
        slide.classList.remove('active');
      }
    });

    dots.forEach((dot, i) => {
      if (i === index) {
        dot.classList.add('active');
        dot.classList.remove('opacity-60');
      } else {
        dot.classList.remove('active');
        dot.classList.add('opacity-60');
      }
    });

    heroCurrentIndex = index;
  }

  window.prevHeroSlide = function() {
    let newIndex = heroCurrentIndex - 1;
    if (newIndex < 0) newIndex = slides.length - 1;
    showSlide(newIndex);
    resetHeroTimer();
  };

  window.nextHeroSlide = function() {
    let newIndex = (heroCurrentIndex + 1) % slides.length;
    showSlide(newIndex);
    resetHeroTimer();
  };

  window.goToHeroSlide = function(index) {
    showSlide(index);
    resetHeroTimer();
  };

  function resetHeroTimer() {
    if (heroSlideTimer) clearInterval(heroSlideTimer);
    heroSlideTimer = setInterval(() => {
      window.nextHeroSlide();
    }, 6500);
  }

  resetHeroTimer();
}

// ==========================================
// 7. RENDER TOURS (SMART TREKKING FILTER & CARDS)
// ==========================================
function renderTours(category = currentCategory) {
  const container = document.getElementById('tour-grid-container');
  if (!container) return;

  currentCategory = category;
  let filtered = [...TOURS_DATA];

  // 1. Category filter
  if (currentCategory !== 'all') {
    filtered = filtered.filter(t => t.category === currentCategory || t.subCategory === currentCategory);
  }

  // 2. Difficulty filter
  if (currentDifficulty === 'easy') {
    filtered = filtered.filter(t => (t.difficultyLevel || 2) <= 2);
  } else if (currentDifficulty === 'medium') {
    filtered = filtered.filter(t => t.difficultyLevel === 3);
  } else if (currentDifficulty === 'hard') {
    filtered = filtered.filter(t => (t.difficultyLevel || 3) >= 4);
  }

  // 3. Duration filter
  if (currentDuration === 'day') {
    filtered = filtered.filter(t => (t.duration || '').toLowerCase().includes('trong ngày'));
  } else if (currentDuration === '2d1n') {
    filtered = filtered.filter(t => (t.duration || '').toLowerCase().includes('2 ngày'));
  } else if (currentDuration === '3d2n') {
    filtered = filtered.filter(t => (t.duration || '').toLowerCase().includes('3 ngày'));
  }

  // 4. Keyword search
  if (searchKeyword) {
    filtered = filtered.filter(t => {
      const haystack = (t.title + ' ' + t.location + ' ' + (t.shortSummary || '') + ' ' + (t.code || '') + ' ' + (t.altitude || '')).toLowerCase();
      return haystack.includes(searchKeyword);
    });
  }

  // 5. Sorting
  if (currentSort === 'price-asc') {
    filtered.sort((a, b) => (a.priceNum || 0) - (b.priceNum || 0));
  } else if (currentSort === 'price-desc') {
    filtered.sort((a, b) => (b.priceNum || 0) - (a.priceNum || 0));
  } else if (currentSort === 'altitude-desc') {
    const parseAlt = (s) => parseInt((s || '').replace(/\D/g, '') || '0', 10);
    filtered.sort((a, b) => parseAlt(b.altitude) - parseAlt(a.altitude));
  } else {
    // popular: featured first, then reviews desc
    filtered.sort((a, b) => {
      if (a.isFeatured && !b.isFeatured) return -1;
      if (!a.isFeatured && b.isFeatured) return 1;
      return (b.reviews || 0) - (a.reviews || 0);
    });
  }

  // UI Count & Reset Button
  const countEl = document.getElementById('filter-result-count');
  const resetBtn = document.getElementById('filter-reset-btn');
  const hasActiveFilters = currentCategory !== 'all' || currentDifficulty !== 'all' || currentDuration !== 'all' || currentSort !== 'popular' || searchKeyword !== '';

  if (resetBtn) {
    if (hasActiveFilters || showAllTours) {
      resetBtn.classList.remove('hidden');
      resetBtn.classList.add('inline-flex');
    } else {
      resetBtn.classList.add('hidden');
      resetBtn.classList.remove('inline-flex');
    }
  }

  // Display limited or full
  let displayTours = filtered;
  if (!hasActiveFilters && !showAllTours) {
    displayTours = filtered.slice(0, 4);
    if (countEl) countEl.textContent = `Hiển thị 4 tour tiêu biểu (${filtered.length} tour có sẵn)`;
  } else {
    if (countEl) countEl.textContent = `Tìm thấy ${filtered.length} hành trình phù hợp`;
  }

  // Empty state if 0 tours found
  if (displayTours.length === 0) {
    container.innerHTML = `
      <div class="col-span-full py-12 px-6 text-center bg-white rounded-2xl border border-gray-100 space-y-4">
        <div class="w-16 h-16 mx-auto rounded-full bg-emerald-50 text-forest flex items-center justify-center">
          <i data-lucide="compass" class="w-8 h-8 text-forest"></i>
        </div>
        <h4 class="text-base font-bold text-gray-900">Không tìm thấy cung đường phù hợp</h4>
        <p class="text-xs text-gray-500 max-w-md mx-auto">
          Hãy thử nới lỏng bộ lọc hoặc tìm kiếm với từ khóa khác (ví dụ: Tà Xùa, Yên Tử, Fansipan, Kỳ Quan San...).
        </p>
        <button 
          type="button" 
          onclick="resetTourFilters()" 
          class="inline-flex items-center gap-1.5 px-4 py-2 rounded-xl bg-forest text-white text-xs font-bold hover:bg-forest/90 transition-all cursor-pointer"
        >
          <i data-lucide="rotate-ccw" class="w-3.5 h-3.5"></i>
          <span>Đặt lại toàn bộ lọc</span>
        </button>
      </div>
    `;
    initLucideIcons();
    return;
  }

  container.innerHTML = displayTours.map(tour => {
    const isLiked = wishlist.has(tour.id);
    const displayPrice = tour.priceNum ? formatCurrency(tour.priceNum) : tour.price.replace('/người', '');
    
    // Clean distance string
    let shortDist = (tour.trekDistance || '12km').replace(/Khoảng\s*/gi, '').split('(')[0].trim();
    if (shortDist.length > 13) shortDist = shortDist.substring(0, 11) + '...';

    return `
      <div class="tour-card bg-white rounded-2xl overflow-hidden border border-gray-100 shadow-sm hover:shadow-md transition-all duration-300 flex flex-col h-full justify-between group">
        
        <!-- Tour Image Container -->
        <div class="relative overflow-hidden aspect-[4/3] bg-gray-100 cursor-pointer shrink-0" onclick="openTourDetailModal(${tour.id})">
          <img 
            src="${tour.image}" 
            alt="${tour.title}" 
            loading="lazy" 
            onerror="this.onerror=null; this.src='assets/images/tour-yen-tu.jpg';"
            class="tour-card-image w-full h-full object-cover transition-transform duration-500 group-hover:scale-108"
          />
          
          <!-- Category & Altitude Badges (Top Left Corner) -->
          <div class="absolute top-2.5 left-2.5 z-10 flex items-center gap-1.5 max-w-[calc(100%-46px)] flex-wrap">
            <span class="backdrop-blur-md bg-[#1E4D3B]/90 text-white text-[10.5px] font-bold px-2 py-0.5 rounded-full shadow-sm truncate">
              ${tour.badge}
            </span>
            <span class="backdrop-blur-md bg-black/65 text-emerald-200 text-[10px] font-bold px-2 py-0.5 rounded-md shadow-sm shrink-0">
              ${tour.altitudeBadge || '⛰️ ' + tour.altitude}
            </span>
          </div>

          <!-- Wishlist Heart Button (Top Right Corner) -->
          <button 
            type="button" 
            onclick="toggleWishlist(${tour.id}, event)" 
            title="${isLiked ? 'Bỏ yêu thích' : 'Lưu tour yêu thích'}"
            class="heart-btn absolute top-2.5 right-2.5 z-20 w-7 h-7 rounded-full bg-white/85 backdrop-blur-md flex items-center justify-center text-gray-700 hover:text-red-500 hover:bg-white transition-all shadow-sm ${isLiked ? 'active' : ''}"
          >
            <i data-lucide="heart" class="w-3.5 h-3.5 transition-colors ${isLiked ? 'fill-red-500 text-red-500' : ''}"></i>
          </button>

          <!-- Fast Spec Bar: Difficulty & Distance (Bottom Left Corner) -->
          <div class="absolute bottom-2.5 left-2.5 z-10">
            <span class="backdrop-blur-md bg-black/65 text-white text-[10.5px] font-semibold px-2.5 py-1 rounded-md shadow-sm flex items-center gap-1.5">
              <span class="text-amber-300 font-bold">⚡ Độ khó: ${tour.difficultyLevel || 3}/5</span>
              <span class="text-white/40">•</span>
              <span class="text-emerald-300 font-bold">🥾 ${shortDist}</span>
            </span>
          </div>

          <!-- Real Photo indicator (Bottom Right Corner) -->
          ${tour.gallery && tour.gallery.length > 0 ? `
            <div class="absolute bottom-2.5 right-2.5 z-10">
              <span class="backdrop-blur-md bg-black/65 text-white text-[10px] font-medium px-2 py-0.5 rounded-md shadow-sm flex items-center gap-1">
                <i data-lucide="camera" class="w-3 h-3 text-emerald-300"></i>
                <span>${tour.gallery.length} ảnh</span>
              </span>
            </div>
          ` : ''}

          <!-- Hover Overlay -->
          <div class="absolute inset-0 backdrop-blur-[2px] bg-black/45 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex flex-col items-center justify-center p-3 text-center pointer-events-none">
            <span class="px-3.5 py-1.5 rounded-full bg-white text-forest text-xs font-bold shadow-lg transform translate-y-2 group-hover:translate-y-0 transition-transform duration-300 flex items-center gap-1.5">
              <i data-lucide="compass" class="w-3.5 h-3.5 text-forest"></i>
              <span>Xem chi tiết tour</span>
            </span>
            <p class="text-[11px] text-white/95 font-medium mt-2 drop-shadow-sm px-2 leading-snug">
              📍 Lộ trình • Lịch sử • Chính sách hoàn hủy
            </p>
          </div>
        </div>

        <!-- Tour Body Content -->
        <div class="p-3.5 flex flex-col flex-1 justify-between">
          <div>
            <!-- Meta Details: Location & History Story Button -->
            <div class="flex items-center justify-between text-[11px] text-gray-500 mb-2 gap-2 h-5">
              <span class="flex items-center gap-1 min-w-0 flex-1 truncate">
                <i data-lucide="map-pin" class="w-3 h-3 text-forest shrink-0"></i>
                <span class="truncate font-medium text-gray-600">${tour.location}</span>
              </span>
              <button 
                type="button" 
                onclick="openTourDetailModal(${tour.id}, 2); event.stopPropagation();" 
                class="inline-flex items-center gap-1 text-[10.5px] font-bold text-forest hover:text-forest-dark bg-emerald-50/90 hover:bg-emerald-100 px-1.5 py-0.5 rounded transition-colors shrink-0 whitespace-nowrap cursor-pointer"
                title="Xem lịch sử & câu chuyện địa danh"
              >
                <i data-lucide="book-open" class="w-3 h-3 text-forest shrink-0"></i>
                <span>Câu chuyện</span>
              </button>
            </div>

            <!-- Title: Locked to h-[40px] for consistent 2-line alignment -->
            <h3 
              class="font-bold text-gray-900 text-[13.5px] leading-snug line-clamp-2 h-[40px] tracking-tight group-hover:text-forest transition-colors cursor-pointer" 
              onclick="openTourDetailModal(${tour.id})" 
              title="${tour.title}"
            >
              ${tour.title}
            </h3>

            <!-- 1-line / 2-line Short Summary Description: Locked to h-[36px] -->
            <p class="text-xs text-gray-600 line-clamp-2 mt-1 mb-2 leading-relaxed h-[36px]" title="${tour.shortSummary || tour.description}">
              ${tour.shortSummary || tour.description}
            </p>

            <!-- Commitment Tag & Schedule: Locked to h-6 -->
            <div class="flex items-center gap-1.5 mb-2.5 h-6">
              <span class="px-2 py-0.5 rounded-md bg-emerald-50 text-forest text-[10px] font-bold border border-emerald-100/80 flex items-center gap-1 shrink-0">
                <i data-lucide="check" class="w-3 h-3 text-forest"></i>
                <span>${tour.minPax}</span>
              </span>
              <span class="text-[10px] text-gray-500 font-medium truncate flex-1" title="${tour.departureFrequency}">
                ${tour.departureFrequency}
              </span>
            </div>

            <!-- Price & Duration: Clearly separated to prevent text collision -->
            <div class="flex items-center justify-between gap-2 pt-2 border-t border-gray-100/90">
              <div class="flex flex-col min-w-0">
                <span class="text-[9.5px] text-gray-400 font-semibold uppercase tracking-wider">Trọn gói từ</span>
                <div class="flex items-baseline gap-0.5">
                  <span class="text-[15px] xl:text-[16px] font-black text-[#1E4D3B] tracking-tight leading-none">
                    ${displayPrice}
                  </span>
                  <span class="text-[10px] text-gray-500 font-normal">/khách</span>
                </div>
              </div>
              <div class="shrink-0 text-right">
                <span class="inline-block text-[10.5px] text-gray-600 font-medium bg-gray-100/80 px-2 py-0.5 rounded-md border border-gray-200/50 whitespace-nowrap">
                  ${tour.duration}
                </span>
              </div>
            </div>
          </div>

          <!-- Bottom: Rating & Direct Book Button: Laser-aligned horizontally -->
          <div class="mt-3 pt-3 border-t border-gray-100 flex items-center justify-between gap-1">
            <div class="flex items-center gap-1 shrink-0">
              <div class="flex text-amber-400">
                <i data-lucide="star" class="w-3 h-3 fill-amber-400 text-amber-400"></i>
                <i data-lucide="star" class="w-3 h-3 fill-amber-400 text-amber-400"></i>
                <i data-lucide="star" class="w-3 h-3 fill-amber-400 text-amber-400"></i>
                <i data-lucide="star" class="w-3 h-3 fill-amber-400 text-amber-400"></i>
                <i data-lucide="star" class="w-3 h-3 fill-amber-400 text-amber-400"></i>
              </div>
              <span class="text-[10.5px] text-gray-400 font-semibold">(${tour.reviews || 120})</span>
            </div>

            <button 
              type="button" 
              onclick="openSmartBookingModal(${tour.id}); event.stopPropagation();"
              class="btn-shine whitespace-nowrap px-3 py-1.5 rounded-lg bg-[#1E4D3B] text-white text-[11px] font-bold shrink-0 hover:bg-forest/90 hover:scale-102 active:scale-95 transition-all shadow-sm cursor-pointer flex items-center gap-1"
            >
              <span>Đăng ký ngay</span>
              <i data-lucide="arrow-right" class="w-3 h-3"></i>
            </button>
          </div>

        </div>

      </div>
    `;
  }).join('');

  initLucideIcons();
}

// ==========================================
// 8. RENDER DEPARTURE SCHEDULE (RIGHT 28%)
// ==========================================
function renderSchedule() {
  const container = document.getElementById('schedule-list-container');
  if (!container) return;

  container.innerHTML = DEPARTURE_SCHEDULE.map(item => {
    let badgeClass = 'badge-seat';
    if (item.statusType === 'urgent') {
      badgeClass += ' badge-urgent';
    } else if (item.statusType === 'available') {
      badgeClass += ' badge-available';
    } else if (item.statusType === 'open') {
      badgeClass += ' badge-open';
    }

    return `
      <div 
        onclick="openTourDetailModal(${item.tourId})"
        class="schedule-row p-2.5 rounded-xl bg-gray-50/70 border border-gray-100/80 flex items-center justify-between gap-2.5 cursor-pointer group hover:bg-emerald-50/60 hover:border-emerald-200/80 hover:shadow-xs transition-all relative"
        title="Bấm để giữ chỗ hoặc xem lịch trình chi tiết"
      >
        <!-- Date Block -->
        <div class="flex items-center gap-2.5 min-w-0 flex-1">
          <div class="w-10 h-10 rounded-xl bg-[#1E4D3B] text-white flex flex-col items-center justify-center shadow-xs group-hover:scale-105 transition-transform shrink-0">
            <span class="text-sm font-black leading-none">${item.day}</span>
            <span class="text-[9px] font-bold uppercase tracking-wider text-emerald-200 mt-0.5">${item.month}</span>
          </div>

          <div class="min-w-0 flex-1">
            <div class="flex items-center gap-1.5">
              <span class="text-[9px] font-extrabold px-1.5 py-0.2 rounded bg-emerald-100 text-forest shrink-0">${item.code}</span>
              <h4 class="text-xs font-bold text-gray-900 group-hover:text-forest transition-colors truncate" title="${item.title}">
                ${item.title}
              </h4>
            </div>
            <span class="text-[10.5px] text-gray-500 font-medium truncate block mt-0.5">${item.duration} • Hà Nội</span>
          </div>
        </div>

        <!-- Price & Status Badge -->
        <div class="text-right shrink-0 pl-1.5 min-w-[75px]">
          <span class="block text-xs font-black text-[#1E4D3B] whitespace-nowrap">${item.price}</span>
          <span class="${badgeClass} text-[9.5px] inline-block mt-0.5 whitespace-nowrap">${item.status}</span>
        </div>
      </div>
    `;
  }).join('');

  initLucideIcons();
}

// ==========================================
// 9. CATEGORY BAR & SMART FILTER CONTROLLERS
// ==========================================
function setupCategoryFilter() {
  const items = document.querySelectorAll('.category-item');
  items.forEach(item => {
    item.addEventListener('click', (e) => {
      e.preventDefault();
      const cat = item.getAttribute('data-category');
      filterByCategory(cat);
    });
  });
}

function filterByCategory(cat) {
  currentCategory = cat;
  if (cat === 'all') {
    showAllTours = true;
  }

  // Update Category Bar active classes
  const items = document.querySelectorAll('.category-item');
  items.forEach(item => {
    const itemCat = item.getAttribute('data-category');
    if (itemCat === cat) {
      item.classList.add('active');
    } else {
      item.classList.remove('active');
    }
  });

  // Smooth fade-in re-render of tours
  const grid = document.getElementById('tour-grid-container');
  if (grid) {
    grid.style.opacity = '0';
    grid.style.transform = 'translateY(8px)';
    grid.style.transition = 'all 0.3s cubic-bezier(0.16, 1, 0.3, 1)';
    setTimeout(() => {
      renderTours(cat);
      grid.style.opacity = '1';
      grid.style.transform = 'translateY(0)';
    }, 180);
  }

  // Update Title text
  const titleEl = document.getElementById('section-tour-title');
  if (titleEl) {
    const titles = {
      all: 'Tất Cả Tour Chinh Phục',
      trekking: 'Tour Trekking Chinh Phục',
      spiritual: 'Tour Hành Hương Tâm Linh',
      experience: 'Tour Trải Nghiệm & Thiên Nhiên',
      charity: 'Tour Thiện Nguyện Ý Nghĩa',
      near_hanoi: 'Tour Gần Hà Nội Trong Ngày'
    };
    titleEl.textContent = titles[cat] || 'Danh Sách Tour';
  }
}
window.filterByCategory = filterByCategory;

function handleTourFilterChange() {
  const searchInput = document.getElementById('tour-search-input');
  const clearBtn = document.getElementById('tour-search-clear');
  const diffSelect = document.getElementById('filter-difficulty');
  const durSelect = document.getElementById('filter-duration');
  const sortSelect = document.getElementById('filter-sort');

  searchKeyword = searchInput ? searchInput.value.trim().toLowerCase() : '';
  currentDifficulty = diffSelect ? diffSelect.value : 'all';
  currentDuration = durSelect ? durSelect.value : 'all';
  currentSort = sortSelect ? sortSelect.value : 'popular';

  if (clearBtn) {
    if (searchKeyword) {
      clearBtn.classList.remove('hidden');
    } else {
      clearBtn.classList.add('hidden');
    }
  }

  renderTours();
}
window.handleTourFilterChange = handleTourFilterChange;

function clearTourSearch() {
  const searchInput = document.getElementById('tour-search-input');
  if (searchInput) {
    searchInput.value = '';
  }
  handleTourFilterChange();
}
window.clearTourSearch = clearTourSearch;

function resetTourFilters() {
  const searchInput = document.getElementById('tour-search-input');
  const diffSelect = document.getElementById('filter-difficulty');
  const durSelect = document.getElementById('filter-duration');
  const sortSelect = document.getElementById('filter-sort');

  if (searchInput) searchInput.value = '';
  if (diffSelect) diffSelect.value = 'all';
  if (durSelect) durSelect.value = 'all';
  if (sortSelect) sortSelect.value = 'popular';

  searchKeyword = '';
  currentDifficulty = 'all';
  currentDuration = 'all';
  currentSort = 'popular';
  showAllTours = false;

  const titleEl = document.getElementById('section-tour-title');
  if (titleEl) titleEl.textContent = 'Tour Nổi Bật';

  filterByCategory('all');
}
window.resetTourFilters = resetTourFilters;

// ==========================================
// 10. ALL-IN-ONE TREKKING GUIDE MODAL CONTROLLER (Inspired by Giang Lang Thang)
// ==========================================
function openTourDetailModal(tourId, initialTab = 1) {
  const tour = TOURS_DATA.find(t => t.id === tourId) || TOURS_DATA[0];
  if (!tour) return;

  modalBookingPax = 1;
  const modal = document.getElementById('tour-detail-modal');
  const content = document.getElementById('tour-detail-content');
  if (!modal || !content) return;

  const isLiked = wishlist.has(tour.id);
  const dates = tour.departureDates && tour.departureDates.length > 0 
    ? tour.departureDates 
    : ['26/10/2026', '01/11/2026', '08/11/2026', '15/11/2026', '22/11/2026'];

  let cleanDist = (tour.trekDistance || '12km').replace(/Khoảng\s*/gi, '').split('(')[0].trim();

  // Altitude badge text
  let altSubtitle = 'Đỉnh cao hùng vĩ';
  if (tour.id === 1) altSubtitle = 'Chùa Đồng linh thiêng';
  else if (tour.id === 2) altSubtitle = 'Thiên đường săn mây';
  else if (tour.id === 3) altSubtitle = 'Rừng rêu nguyên sinh';
  else if (tour.id === 4) altSubtitle = 'Top 4 Nóc nhà VN';
  else if (tour.id === 9) altSubtitle = 'Nóc nhà Đông Dương';

  content.innerHTML = `
    <div class="relative bg-white rounded-3xl overflow-hidden shadow-2xl max-w-4xl w-full border border-gray-100 modal-enter max-h-[92vh] flex flex-col">
      
      <!-- Top Image Banner & Close Button -->
      <div class="relative h-60 sm:h-72 w-full shrink-0">
        <img 
          id="modal-main-image"
          src="${tour.image}" 
          alt="${tour.title}" 
          onerror="this.onerror=null; this.src='assets/images/tour-yen-tu.jpg';"
          class="w-full h-full object-cover transition-opacity duration-300"
        />
        <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-black/45 to-transparent"></div>
        
        <button 
          type="button" 
          onclick="closeTourDetailModal()" 
          class="absolute top-4 right-4 z-20 w-9 h-9 rounded-full bg-black/50 text-white hover:bg-black/80 flex items-center justify-center transition-colors backdrop-blur-sm cursor-pointer shadow-md"
          title="Đóng"
        >
          <i data-lucide="x" class="w-5 h-5"></i>
        </button>

        <!-- Banner Text & Badges -->
        <div class="absolute bottom-4 left-5 right-5 text-white">
          <div class="flex flex-wrap items-center gap-2 mb-2">
            <span class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-[#1E4D3B] text-white shadow-xs">${tour.badge}</span>
            <span class="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-white/20 backdrop-blur-sm text-white">${tour.altitudeBadge || '⛰️ ' + tour.altitude}</span>
            <span class="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-white/20 backdrop-blur-sm text-white">${tour.duration}</span>
            <span class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-amber-400 text-stone-900 shadow-xs">${tour.code}</span>
          </div>
          <h2 class="text-xl sm:text-2xl lg:text-3xl font-black leading-tight drop-shadow-sm">${tour.title}</h2>
          <p class="text-xs sm:text-sm text-emerald-200 mt-1 flex items-center gap-2">
            <i data-lucide="map-pin" class="w-3.5 h-3.5 text-emerald-300 shrink-0"></i>
            <span>${tour.location} • Điểm đón: ${tour.pickupPoint || '55 Nguyễn Quốc Trị & 489 Hoàng Quốc Việt'}</span>
          </p>
        </div>
      </div>

      <!-- 1. TREKKING DASHBOARD (4 METRIC TILES) -->
      <div class="grid grid-cols-2 sm:grid-cols-4 gap-2.5 px-5 py-3.5 bg-[#F6F7F2] border-b border-gray-100 shrink-0">
        <!-- Tile 1: Altitude -->
        <div class="bg-white p-2.5 rounded-xl border border-gray-100 shadow-2xs flex items-center gap-2.5">
          <div class="w-9 h-9 rounded-lg bg-emerald-50 text-forest flex items-center justify-center shrink-0">
            <i data-lucide="mountain" class="w-5 h-5"></i>
          </div>
          <div class="min-w-0">
            <span class="block text-[10px] font-bold uppercase tracking-wider text-gray-500">Độ cao đỉnh</span>
            <span class="block text-xs sm:text-sm font-black text-forest truncate">${tour.altitude}</span>
            <span class="block text-[9.5px] text-gray-400 truncate">${altSubtitle}</span>
          </div>
        </div>

        <!-- Tile 2: Difficulty -->
        <div class="bg-white p-2.5 rounded-xl border border-gray-100 shadow-2xs flex items-center gap-2.5">
          <div class="w-9 h-9 rounded-lg bg-amber-50 text-amber-600 flex items-center justify-center shrink-0">
            <i data-lucide="zap" class="w-5 h-5"></i>
          </div>
          <div class="min-w-0">
            <span class="block text-[10px] font-bold uppercase tracking-wider text-gray-500">Độ khó thể lực</span>
            <span class="block text-xs sm:text-sm font-black text-amber-600">Level ${tour.difficultyLevel || 3}/5</span>
            <span class="block text-[9.5px] text-gray-500 truncate">${tour.difficultyText || 'Trung bình'}</span>
          </div>
        </div>

        <!-- Tile 3: Total Distance -->
        <div class="bg-white p-2.5 rounded-xl border border-gray-100 shadow-2xs flex items-center gap-2.5">
          <div class="w-9 h-9 rounded-lg bg-emerald-50 text-emerald-600 flex items-center justify-center shrink-0">
            <i data-lucide="footprints" class="w-5 h-5"></i>
          </div>
          <div class="min-w-0">
            <span class="block text-[10px] font-bold uppercase tracking-wider text-gray-500">Tổng quãng đường</span>
            <span class="block text-xs sm:text-sm font-black text-gray-900 truncate">${cleanDist}</span>
            <span class="block text-[9.5px] text-gray-400 truncate">Rừng & sống núi</span>
          </div>
        </div>

        <!-- Tile 4: Ratio Leader / Porter -->
        <div class="bg-white p-2.5 rounded-xl border border-gray-100 shadow-2xs flex items-center gap-2.5">
          <div class="w-9 h-9 rounded-lg bg-forest/10 text-forest flex items-center justify-center shrink-0">
            <i data-lucide="shield-check" class="w-5 h-5"></i>
          </div>
          <div class="min-w-0">
            <span class="block text-[10px] font-bold uppercase tracking-wider text-gray-500">Tỷ lệ Leader/Porter</span>
            <span class="block text-xs sm:text-sm font-black text-forest">1 kèm 3</span>
            <span class="block text-[9.5px] text-emerald-600 font-semibold truncate">An toàn tuyệt đối</span>
          </div>
        </div>
      </div>

      <!-- STORYTELLING TABS NAVIGATION (5 TABS) -->
      <div class="flex items-center gap-3 sm:gap-5 px-5 sm:px-6 pt-3 border-b border-gray-100 bg-white text-xs sm:text-sm shrink-0 overflow-x-auto no-scrollbar whitespace-nowrap">
        <button 
          id="tab-btn-1" 
          onclick="switchDetailTab(1)"
          class="modal-tab-btn active cursor-pointer flex items-center gap-1.5"
        >
          <i data-lucide="navigation" class="w-3.5 h-3.5"></i>
          <span>1. Hành trình & Đi đâu</span>
        </button>
        <button 
          id="tab-btn-2" 
          onclick="switchDetailTab(2)"
          class="modal-tab-btn cursor-pointer flex items-center gap-1.5"
        >
          <i data-lucide="landmark" class="w-3.5 h-3.5"></i>
          <span>2. Lịch sử & Câu chuyện</span>
        </button>
        <button 
          id="tab-btn-3" 
          onclick="switchDetailTab(3)"
          class="modal-tab-btn cursor-pointer flex items-center gap-1.5"
        >
          <i data-lucide="calendar" class="w-3.5 h-3.5"></i>
          <span>3. Lịch trình chi tiết</span>
        </button>
        <button 
          id="tab-btn-4" 
          onclick="switchDetailTab(4)"
          class="modal-tab-btn cursor-pointer flex items-center gap-1.5"
        >
          <i data-lucide="backpack" class="w-3.5 h-3.5"></i>
          <span>4. Dịch vụ & Đồ chuẩn bị</span>
        </button>
        <button 
          id="tab-btn-5" 
          onclick="switchDetailTab(5)"
          class="modal-tab-btn cursor-pointer flex items-center gap-1.5 text-forest"
        >
          <i data-lucide="shield-check" class="w-3.5 h-3.5 text-forest"></i>
          <span>5. Chính sách hoàn hủy</span>
        </button>
      </div>

      <!-- TAB CONTENT PANELS -->
      <div class="p-5 sm:p-6 overflow-y-auto flex-1 space-y-4 text-xs sm:text-sm text-gray-700 leading-relaxed">
        
        <!-- PANEL 1: Hành trình & Đi đâu -->
        <div id="tab-panel-1" class="space-y-4">
          <!-- Visual Route Steps -->
          <div class="space-y-2">
            <h4 class="text-xs font-bold uppercase tracking-wider text-forest flex items-center gap-1.5">
              <i data-lucide="map-pin" class="w-4 h-4 text-forest"></i>
              <span>Sơ đồ lộ trình các chặng từ Hà Nội</span>
            </h4>
            <div class="flex flex-wrap items-center gap-1.5 sm:gap-2 p-3 bg-emerald-50/70 rounded-2xl border border-emerald-100">
              ${(tour.routeSteps || ['Hà Nội', 'Chân núi', 'Lán nghỉ', 'Đỉnh núi', 'Hạ sơn']).map((step, idx, arr) => `
                <span class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-white border border-emerald-200 text-forest font-bold text-xs shadow-2xs">
                  <span class="w-4 h-4 rounded-full bg-forest text-white text-[10px] flex items-center justify-center font-extrabold shrink-0">${idx + 1}</span>
                  <span>${step}</span>
                </span>
                ${idx < arr.length - 1 ? '<i data-lucide="chevron-right" class="w-3.5 h-3.5 text-emerald-600 shrink-0"></i>' : ''}
              `).join('')}
            </div>
          </div>

          <!-- Geographic Route Description -->
          <div class="space-y-1.5">
            <h4 class="text-xs font-bold uppercase tracking-wider text-gray-800 flex items-center gap-1.5">
              <i data-lucide="map" class="w-4 h-4 text-forest"></i>
              <span>Hành trình đi đâu & Lộ trình địa lý</span>
            </h4>
            <p class="text-xs sm:text-sm text-gray-700 leading-relaxed bg-gray-50 p-3.5 rounded-xl border border-gray-100 font-normal">
              ${tour.routeMap || tour.description}
            </p>
          </div>
          
          <!-- Highlights -->
          <div class="space-y-2.5 pt-1">
            <h4 class="text-xs font-bold uppercase tracking-wider text-forest">Trải nghiệm độc bản không thể bỏ lỡ</h4>
            <ul class="space-y-2">
              ${(tour.highlights || [
                'Chinh phục đỉnh cao ngoạn mục vùng cao Tây Bắc',
                'Đón bình minh và biển mây cuồn cuộn tráng lệ',
                'Thưởng thức ẩm thực bản địa tươi ngon bên bếp lửa lán rừng'
              ]).map(hl => `
                <li class="flex items-start gap-2.5">
                  <i data-lucide="check-circle-2" class="w-4 h-4 text-forest shrink-0 mt-0.5"></i>
                  <span>${hl}</span>
                </li>
              `).join('')}
            </ul>
          </div>

          <!-- Real Photos Gallery from Expedition -->
          ${tour.gallery && tour.gallery.length > 0 ? `
            <div class="space-y-2.5 pt-2">
              <div class="flex items-center justify-between">
                <h4 class="text-xs font-bold uppercase tracking-wider text-forest flex items-center gap-1.5">
                  <i data-lucide="camera" class="w-4 h-4 text-forest"></i>
                  <span>Khoảnh khắc thực tế từ các chuyến đi của Đi Cùng Gió</span>
                </h4>
                <span class="text-[10px] text-gray-500 font-medium">Bấm vào ảnh để xem lớn</span>
              </div>
              <div class="grid grid-cols-2 sm:grid-cols-4 gap-2.5">
                ${tour.gallery.map(g => `
                  <div 
                    onclick="switchModalImage('${g.url}')"
                    class="group/img relative rounded-xl overflow-hidden aspect-[4/3] bg-gray-100 shadow-2xs border border-gray-200 cursor-pointer hover:border-emerald-500 hover:ring-2 hover:ring-emerald-400/40 transition-all"
                    title="${g.caption} - Bấm để phóng to lên banner"
                  >
                    <img 
                      src="${g.url}" 
                      alt="${g.caption}" 
                      loading="lazy"
                      onerror="this.onerror=null; this.src='assets/images/tour-yen-tu.jpg';"
                      class="w-full h-full object-cover group-hover/img:scale-108 transition-transform duration-500"
                    />
                    <div class="absolute inset-0 bg-gradient-to-t from-black/85 via-black/25 to-transparent opacity-0 group-hover/img:opacity-100 transition-opacity duration-200 p-2 flex items-end">
                      <span class="text-[10px] text-white font-medium leading-tight">${g.caption}</span>
                    </div>
                  </div>
                `).join('')}
              </div>
            </div>
          ` : ''}
        </div>

        <!-- PANEL 2: Lịch sử & Câu chuyện vùng đất -->
        <div id="tab-panel-2" class="hidden space-y-4">
          <div class="bg-[#F6F7F2] border-l-4 border-[#1E4D3B] p-5 rounded-r-2xl shadow-xs space-y-3.5">
            <div class="flex items-center gap-2 text-forest">
              <i data-lucide="landmark" class="w-5 h-5 text-forest"></i>
              <h4 class="font-extrabold text-sm sm:text-base text-gray-900">
                Lịch sử, Huyền thoại & Câu chuyện văn hóa: ${tour.title}
              </h4>
            </div>
            
            <p class="text-xs sm:text-sm text-gray-700 leading-relaxed font-normal">
              ${tour.historyStory || tour.description}
            </p>

            <div class="pt-3 text-[11px] text-gray-500 italic border-t border-stone-200/70 flex items-center gap-2">
              <i data-lucide="sparkles" class="w-4 h-4 text-amber-500 shrink-0"></i>
              <span>Mỗi hành trình của Trekking Đi Cùng Gió không chỉ là thử thách thể lực, mà là một trải nghiệm chạm vào chiều sâu văn hóa và lịch sử đất nước.</span>
            </div>
          </div>
        </div>

        <!-- PANEL 3: Lịch trình chi tiết theo ngày -->
        <div id="tab-panel-3" class="hidden space-y-4">
          <div class="space-y-3">
            <h4 class="text-xs font-bold uppercase tracking-wider text-forest flex items-center gap-1.5">
              <i data-lucide="calendar" class="w-4 h-4 text-forest"></i>
              <span>Lịch trình chi tiết các chặng</span>
            </h4>
            <div class="relative pl-6 space-y-4 before:content-[''] before:absolute before:left-2.5 before:top-2 before:bottom-2 before:w-0.5 before:bg-emerald-200">
              ${(tour.itinerary || [
                { day: "Đêm 0", title: "Khởi hành từ Hà Nội", desc: "Xe đón tại 55 Nguyễn Quốc Trị và 489 Hoàng Quốc Việt, di chuyển xuyên đêm lên điểm leo." },
                { day: "Ngày 1", title: "Bắt đầu trekking & Nghỉ lán", desc: "Ăn sáng, gặp gỡ Porter, bắt đầu hành trình trekking qua rừng, ăn trưa dã ngoại và nghỉ đêm tại lán gỗ." },
                { day: "Ngày 2", title: "Chạm đỉnh & Hạ sơn", desc: "Thức dậy sớm đón bình minh săn mây, chạm đỉnh nhận huy chương danh dự và di chuyển về Hà Nội." }
              ]).map(step => `
                <div class="relative group">
                  <div class="absolute -left-[27px] top-1 w-4 h-4 rounded-full border-2 border-white bg-forest shadow-xs"></div>
                  <h5 class="font-bold text-gray-900 text-xs sm:text-sm flex items-center gap-2">
                    <span class="px-2 py-0.5 rounded-md bg-emerald-100 text-forest text-[11px] font-extrabold">${step.day}</span>
                    <span>${step.title}</span>
                  </h5>
                  <p class="text-xs text-gray-600 mt-1 leading-relaxed">${step.desc}</p>
                </div>
              `).join('')}
            </div>
          </div>
        </div>

        <!-- PANEL 4: DỊCH VỤ BAO GỒM & ĐỒ CHUẨN BỊ (Included & Packing List) -->
        <div id="tab-panel-4" class="hidden space-y-4">
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <!-- Cột trái: ĐI CÙNG GIÓ CHUẨN BỊ -->
            <div class="bg-gray-50 p-4 rounded-2xl border border-gray-100 space-y-2.5">
              <h5 class="font-bold text-xs text-forest uppercase tracking-wider flex items-center gap-1.5">
                <i data-lucide="check-circle-2" class="w-4 h-4 text-forest"></i>
                <span>ĐI CÙNG GIÓ Chuẩn Bị</span>
              </h5>
              <ul class="text-xs text-gray-600 space-y-2">
                ${(tour.included || [
                  "Xe giường nằm / Limousine đời mới khứ hồi Hà Nội",
                  "Đội ngũ Leader giàu kinh nghiệm + Porter bản địa gùi đồ",
                  "Chỗ ngủ lán gỗ / lều cách nhiệt ấm cúng và đầy đủ chăn đệm",
                  "Tất cả các bữa ăn chính tiêu chuẩn vùng cao ấm cúng",
                  "Bảo hiểm du lịch trọn gói mức bồi thường tới 100.000.000đ",
                  "Gậy trekking trợ lực, áo mưa, túi y tế chuyên dụng",
                  "Huy chương gỗ độc quyền khắc kỷ niệm chinh phục đỉnh núi"
                ]).map(inc => `
                  <li class="flex items-start gap-2">
                    <span class="text-forest font-bold">•</span>
                    <span>${inc}</span>
                  </li>
                `).join('')}
              </ul>
            </div>

            <!-- Cột phải: BẠN CẦN CHUẨN BỊ -->
            <div class="bg-emerald-50/50 p-4 rounded-2xl border border-emerald-100/70 space-y-2.5">
              <h5 class="font-bold text-xs text-forest uppercase tracking-wider flex items-center gap-1.5">
                <i data-lucide="backpack" class="w-4 h-4 text-forest"></i>
                <span>Bạn Cần Chuẩn Bị</span>
              </h5>
              <ul class="text-xs text-gray-700 space-y-2">
                ${(tour.preparation || [
                  "Giày trekking chuyên dụng có độ bám gai cao, chống trơn trượt",
                  "Áo khoác gió giữ nhiệt / áo phao ấm cho ban đêm trên lán",
                  "Balo cá nhân gọn nhẹ 20 – 30L đựng đồ dùng cần thiết",
                  "Đèn pin đội đầu có pin dự phòng (dùng khi săn mây sớm)",
                  "Bình nước cá nhân 1 – 1.5L, đồ ăn vặt bổ sung năng lượng",
                  "Giấy tờ tùy thân (CCCD / Hộ chiếu bản gốc bắt buộc)"
                ]).map(prep => `
                  <li class="flex items-start gap-2">
                    <span class="text-amber-600 font-bold">✔</span>
                    <span>${prep}</span>
                  </li>
                `).join('')}
              </ul>
            </div>
          </div>
        </div>

        <!-- PANEL 5: CHÍNH SÁCH HOÀN HỦY & QUY ĐỊNH -->
        <div id="tab-panel-5" class="hidden space-y-4">
          <!-- Timeline visual cards -->
          <div class="space-y-2">
            <h4 class="text-xs font-bold uppercase tracking-wider text-forest flex items-center gap-1.5">
              <i data-lucide="clock" class="w-4 h-4 text-forest"></i>
              <span>Quy định hoàn hủy & Bảo lưu tour</span>
            </h4>
            <div class="grid grid-cols-1 sm:grid-cols-3 gap-2.5">
              <div class="p-3.5 rounded-2xl bg-emerald-50/80 border border-emerald-200 space-y-1">
                <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-[10px] font-extrabold bg-emerald-600 text-white">Trước 10 ngày</span>
                <p class="text-xs sm:text-sm font-black text-emerald-950">Hoàn 100% chi phí</p>
                <p class="text-[11px] text-emerald-800 leading-tight">Hoàn trả 100% toàn bộ số tiền quý khách đã thanh toán/đặt cọc.</p>
              </div>

              <div class="p-3.5 rounded-2xl bg-amber-50/80 border border-amber-200 space-y-1">
                <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-[10px] font-extrabold bg-amber-600 text-white">Từ 5 – 10 ngày</span>
                <p class="text-xs sm:text-sm font-black text-amber-950">Bảo lưu trong 45 ngày</p>
                <p class="text-[11px] text-amber-800 leading-tight">Hỗ trợ bảo lưu suất đi sang ngày khởi hành khác trong vòng 45 ngày.</p>
              </div>

              <div class="p-3.5 rounded-2xl bg-rose-50/80 border border-rose-200 space-y-1">
                <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-[10px] font-extrabold bg-rose-600 text-white">Dưới 5 ngày (1 – 5 ngày)</span>
                <p class="text-xs sm:text-sm font-black text-rose-950">Không hoàn – Không bảo lưu</p>
                <p class="text-[11px] text-rose-800 leading-tight">Do toàn bộ chi phí xe, porter, lán nghỉ và thực phẩm đã được thanh toán.</p>
              </div>
            </div>
            <p class="text-[11px] text-gray-500 italic">
              * Tour đặc thù mùa vụ: Trước 15 ngày hoàn 100%, 5–10 ngày bảo lưu 45 ngày, dưới 5 ngày không hoàn/hủy.
            </p>
          </div>

          <!-- Pickup & Commitments Box -->
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 pt-1">
            <div class="p-3.5 bg-stone-50 rounded-2xl border border-stone-200/80 space-y-2">
              <h5 class="text-xs font-bold text-gray-900 flex items-center gap-1.5 uppercase tracking-wide">
                <i data-lucide="map-pin" class="w-3.5 h-3.5 text-forest"></i>
                <span>2 Điểm đón cố định tại Hà Nội</span>
              </h5>
              <ul class="text-xs text-gray-700 space-y-1.5">
                <li class="flex items-start gap-2">
                  <span class="w-4 h-4 rounded-full bg-forest/10 text-forest font-bold text-[10px] flex items-center justify-center shrink-0 mt-0.5">1</span>
                  <span><strong>55 Nguyễn Quốc Trị</strong> (Cầu Giấy, Hà Nội)</span>
                </li>
                <li class="flex items-start gap-2">
                  <span class="w-4 h-4 rounded-full bg-forest/10 text-forest font-bold text-[10px] flex items-center justify-center shrink-0 mt-0.5">2</span>
                  <span><strong>489 Hoàng Quốc Việt</strong> (Cầu Giấy, Hà Nội)</span>
                </li>
              </ul>
              <p class="text-[11px] text-gray-500 italic pt-1">
                💬 Nhóm Zalo đoàn được lập trước 2–4 ngày cập nhật số xe, hướng dẫn viên & thời tiết.
              </p>
            </div>

            <div class="p-3.5 bg-emerald-50/60 rounded-2xl border border-emerald-100 space-y-2">
              <h5 class="text-xs font-bold text-forest flex items-center gap-1.5 uppercase tracking-wide">
                <i data-lucide="badge-check" class="w-3.5 h-3.5 text-forest"></i>
                <span>Chính sách giá & Trẻ em</span>
              </h5>
              <ul class="text-xs text-gray-700 space-y-1.5">
                <li>• <strong>Cam kết chạy:</strong> Chắc chắn khởi hành chỉ từ <strong>05 khách</strong>.</li>
                <li>• <strong>Trẻ em 5 – 9 tuổi:</strong> Tính <strong>75%</strong> giá tour người lớn.</li>
                <li>• <strong>Khách nước ngoài:</strong> Phụ thu <strong>200.000đ/khách</strong> (thủ tục biên phòng/tạm trú).</li>
              </ul>
            </div>
          </div>
        </div>

      </div>

      <!-- 5. STICKY BOTTOM BAR (QUICK BOOKING & LIVE PRICING) -->
      <div class="p-3.5 sm:p-4 border-t border-gray-100 bg-gray-50/95 flex flex-wrap sm:flex-nowrap items-center justify-between gap-3 shrink-0">
        <!-- Date Selector -->
        <div class="flex items-center gap-2">
          <label for="modal-booking-date" class="sr-only">Ngày khởi hành</label>
          <div class="relative">
            <select 
              id="modal-booking-date" 
              onchange="updateModalBookingTotal(${tour.id})"
              class="appearance-none pl-3 pr-7 py-2 rounded-xl bg-white border border-gray-200 text-xs font-bold text-gray-800 focus:outline-none focus:border-forest shadow-2xs cursor-pointer"
            >
              ${dates.map(d => `<option value="${d}">📅 ${d}</option>`).join('')}
            </select>
            <i data-lucide="chevron-down" class="w-3.5 h-3.5 text-gray-400 absolute right-2 top-1/2 -translate-y-1/2 pointer-events-none"></i>
          </div>

          <!-- Pax Stepper -->
          <div class="flex items-center border border-gray-200 rounded-xl bg-white shadow-2xs overflow-hidden">
            <button 
              type="button" 
              onclick="adjustModalPax(-1, ${tour.id})" 
              class="px-2.5 py-1.5 text-gray-600 hover:bg-gray-100 text-xs font-black cursor-pointer"
              title="Giảm 1 khách"
            >-</button>
            <span id="modal-booking-pax" class="px-2.5 py-1.5 text-xs font-extrabold text-gray-900 min-w-[28px] text-center">1</span>
            <button 
              type="button" 
              onclick="adjustModalPax(1, ${tour.id})" 
              class="px-2.5 py-1.5 text-gray-600 hover:bg-gray-100 text-xs font-black cursor-pointer"
              title="Thêm 1 khách"
            >+</button>
          </div>
        </div>

        <!-- Price Total & Submit CTA -->
        <div class="flex items-center gap-3 sm:gap-4 ml-auto">
          <div class="text-right">
            <span class="block text-[10px] text-gray-400 uppercase font-bold tracking-wider">Tổng chi phí</span>
            <span id="modal-booking-total" class="block text-base sm:text-lg font-black text-forest leading-none">
              ${formatCurrency(tour.priceNum || 550000)}
            </span>
          </div>

          <button 
            type="button" 
            onclick="proceedModalBooking(${tour.id})" 
            class="btn-shine px-5 py-2.5 rounded-full bg-forest text-white text-xs sm:text-sm font-bold hover:bg-forest/90 active:scale-95 transition-all shadow-md flex items-center gap-1.5 shrink-0 cursor-pointer"
          >
            <span>Đăng ký giữ chỗ ngay</span>
            <i data-lucide="arrow-right" class="w-4 h-4"></i>
          </button>
        </div>
      </div>

    </div>
  `;

  modal.classList.remove('hidden');
  document.body.style.overflow = 'hidden';
  switchDetailTab(initialTab);
  initLucideIcons();
}

function closeTourDetailModal() {
  const modal = document.getElementById('tour-detail-modal');
  if (modal) {
    modal.classList.add('hidden');
    document.body.style.overflow = '';
  }
}

// Switch modal top preview image on thumbnail click
window.switchModalImage = function(imgUrl) {
  const img = document.getElementById('modal-main-image');
  if (img) {
    img.style.opacity = '0.35';
    setTimeout(() => {
      img.src = imgUrl;
      img.style.opacity = '1';
    }, 150);
  }
};

// Switch tab in detail modal (1 to 5)
function switchDetailTab(tabIndex) {
  for (let i = 1; i <= 5; i++) {
    const btn = document.getElementById(`tab-btn-${i}`);
    const panel = document.getElementById(`tab-panel-${i}`);
    if (btn && panel) {
      if (i === tabIndex) {
        btn.classList.add('active');
        panel.classList.remove('hidden');
      } else {
        btn.classList.remove('active');
        panel.classList.add('hidden');
      }
    }
  }
  initLucideIcons();
}
window.switchDetailTab = switchDetailTab;

window.adjustModalPax = function(delta, tourId) {
  const newPax = modalBookingPax + delta;
  if (newPax >= 1 && newPax <= 20) {
    modalBookingPax = newPax;
    updateModalBookingTotal(tourId);
  }
};

window.updateModalBookingTotal = function(tourId) {
  const tour = TOURS_DATA.find(t => t.id === tourId);
  if (!tour) return;
  const paxEl = document.getElementById('modal-booking-pax');
  const totalEl = document.getElementById('modal-booking-total');
  if (paxEl) paxEl.textContent = modalBookingPax;
  if (totalEl) {
    const total = (tour.priceNum || 550000) * modalBookingPax;
    totalEl.textContent = formatCurrency(total);
  }
};

window.proceedModalBooking = function(tourId) {
  const dateSelect = document.getElementById('modal-booking-date');
  const selectedDate = dateSelect ? dateSelect.value : '';
  const pax = modalBookingPax || 1;
  closeTourDetailModal();
  openSmartBookingModal(tourId, selectedDate, pax);
};

// ==========================================
// 11. SMART BOOKING MODAL WITH LIVE CALCULATOR
// ==========================================
function openSmartBookingModal(tourId = 1, defaultDate = '', defaultGuests = 1) {
  currentBookingTour = TOURS_DATA.find(t => t.id === tourId) || TOURS_DATA[0];
  bookingGuests = defaultGuests || 1;

  const modal = document.getElementById('booking-modal');
  const select = document.getElementById('booking-tour-select');
  const dateInput = document.getElementById('booking-date-input');
  const formBox = document.getElementById('booking-form-box');
  const successBox = document.getElementById('booking-success-box');

  if (!modal) return;

  // Populate Select options if empty
  if (select) {
    select.innerHTML = TOURS_DATA.map(t => `
      <option value="${t.id}" ${t.id === currentBookingTour.id ? 'selected' : ''}>
        ${t.code ? `[${t.code}] ` : ''}${t.title} - ${t.price} (${t.duration})
      </option>
    `).join('');
    
    select.onchange = (e) => {
      const chosenId = parseInt(e.target.value, 10);
      currentBookingTour = TOURS_DATA.find(t => t.id === chosenId) || TOURS_DATA[0];
      updateBookingCalculation();
    };
  }

  // Set default date if passed
  if (dateInput) {
    if (defaultDate) {
      dateInput.value = defaultDate;
    } else if (currentBookingTour.departureDates && currentBookingTour.departureDates.length > 0) {
      dateInput.value = currentBookingTour.departureDates[0];
    } else {
      dateInput.value = '26/10/2026';
    }
  }

  // Reset display boxes
  if (formBox) formBox.classList.remove('hidden');
  if (successBox) successBox.classList.add('hidden');

  updateBookingCalculation();

  modal.classList.remove('hidden');
  document.body.style.overflow = 'hidden';
  initLucideIcons();
}

function closeBookingModal() {
  const modal = document.getElementById('booking-modal');
  if (modal) {
    modal.classList.add('hidden');
    document.body.style.overflow = '';
  }
}

// Adjust guests with plus / minus buttons
window.adjustBookingGuests = function(delta) {
  const newCount = bookingGuests + delta;
  if (newCount >= 1 && newCount <= 20) {
    bookingGuests = newCount;
    updateBookingCalculation();
  }
};

// Calculate and render live price breakdown
function updateBookingCalculation() {
  const countEl = document.getElementById('booking-guests-count');
  const summaryBox = document.getElementById('booking-summary-box');
  if (countEl) countEl.textContent = bookingGuests;

  if (!summaryBox || !currentBookingTour) return;

  const priceEach = currentBookingTour.priceNum;
  const subtotal = priceEach * bookingGuests;
  const isGroupDiscount = bookingGuests >= 4;
  const discountAmount = isGroupDiscount ? Math.round(subtotal * 0.05) : 0;
  const finalTotal = subtotal - discountAmount;

  summaryBox.innerHTML = `
    <div class="p-3.5 bg-emerald-50/70 rounded-2xl border border-emerald-100 space-y-2 text-xs">
      <div class="flex justify-between items-center text-gray-600">
        <span>Đơn giá (${bookingGuests} khách):</span>
        <span class="font-bold text-gray-900">${formatCurrency(priceEach)} x ${bookingGuests} = ${formatCurrency(subtotal)}</span>
      </div>
      ${isGroupDiscount ? `
        <div class="flex justify-between items-center text-emerald-700 font-bold">
          <span>Ưu đãi nhóm (≥4 khách giảm 5%):</span>
          <span>- ${formatCurrency(discountAmount)}</span>
        </div>
      ` : `
        <div class="text-[11px] text-gray-500 italic">
          💡 Đặt từ 4 người trở lên được giảm thêm 5% tổng hóa đơn.
        </div>
      `}
      <div class="pt-2 border-t border-emerald-200 flex justify-between items-center text-sm font-extrabold text-forest">
        <span>Tổng tạm tính:</span>
        <span class="text-base text-[#1E4D3B]">${formatCurrency(finalTotal)}</span>
      </div>
    </div>
  `;
}

function setupBookingModalEvents() {
  const form = document.getElementById('smart-booking-form');
  if (!form) return;

  form.addEventListener('submit', (e) => {
    e.preventDefault();

    const name = document.getElementById('booking-name')?.value;
    const phone = document.getElementById('booking-phone')?.value;
    const email = document.getElementById('booking-email')?.value || 'Không có';
    const date = document.getElementById('booking-date-input')?.value;
    const note = document.getElementById('booking-note')?.value || 'Không có';

    if (!name || !phone) {
      showToast('Lỗi thông tin', 'Vui lòng điền Họ tên và Số điện thoại nhận Zalo.', 'error');
      return;
    }

    const randomCode = '#DCG-' + Math.floor(100000 + Math.random() * 900000);
    const subtotal = currentBookingTour.priceNum * bookingGuests;
    const isGroupDiscount = bookingGuests >= 4;
    const finalTotal = isGroupDiscount ? subtotal * 0.95 : subtotal;

    const formBox = document.getElementById('booking-form-box');
    const successBox = document.getElementById('booking-success-box');
    
    if (formBox && successBox) {
      formBox.classList.add('hidden');
      successBox.classList.remove('hidden');

      successBox.innerHTML = `
        <div class="text-center space-y-4 py-4">
          <div class="w-16 h-16 bg-emerald-100 text-forest rounded-full flex items-center justify-center mx-auto shadow-inner">
            <i data-lucide="check" class="w-8 h-8"></i>
          </div>
          
          <h4 class="text-xl font-bold text-gray-900">Giữ Chỗ Thành Công!</h4>
          <p class="text-xs text-gray-600 max-w-sm mx-auto leading-relaxed">
            Cảm ơn <strong>${name}</strong> đã đăng ký hành trình cùng <strong>Trekking Đi Cùng Gió</strong>. 
            Mã đặt chỗ của bạn là <span class="px-2 py-0.5 rounded bg-emerald-100 font-mono font-bold text-forest">${randomCode}</span>.
          </p>

          <div class="bg-gray-50 rounded-2xl p-4 text-xs text-left space-y-2 border border-gray-100 font-medium">
            <div class="flex justify-between">
              <span class="text-gray-500">Hành trình:</span>
              <span class="font-bold text-gray-900">${currentBookingTour.title}</span>
            </div>
            <div class="flex justify-between">
              <span class="text-gray-500">Số lượng khách:</span>
              <span class="font-bold text-gray-900">${bookingGuests} người</span>
            </div>
            <div class="flex justify-between">
              <span class="text-gray-500">Dự kiến khởi hành:</span>
              <span class="font-bold text-gray-900">${date}</span>
            </div>
            <div class="flex justify-between">
              <span class="text-gray-500">Điểm đón Hà Nội:</span>
              <span class="font-bold text-forest">55 Nguyễn Quốc Trị / 489 HQV</span>
            </div>
            <div class="pt-2 border-t border-emerald-200 flex justify-between items-center">
              <span class="text-gray-600 font-bold">Tổng chi phí dự tính:</span>
              <span class="font-black text-sm text-forest">${formatCurrency(finalTotal)}</span>
            </div>
          </div>

          <p class="text-[11px] text-gray-500 italic">
            💬 Tư vấn viên / Leader đoàn sẽ gọi điện xác nhận và gửi lịch trình chi tiết qua Zalo <strong>${phone}</strong> trong vòng 15 phút.
          </p>

          <button 
            type="button" 
            onclick="closeBookingModal()" 
            class="w-full py-3 rounded-full bg-forest text-white font-bold text-xs hover:bg-forest/90 transition-colors shadow-sm cursor-pointer"
          >
            Hoàn tất & Tiếp tục khám phá
          </button>
        </div>
      `;
      initLucideIcons();
    }

    showToast('Đăng ký thành công!', 'Chúng tôi đã nhận thông tin giữ chỗ của bạn.', 'success');
  });
}

// ==========================================
// 12. WISHLIST & DRAWER SYSTEM
// ==========================================
function toggleWishlist(tourId, event) {
  if (event) event.stopPropagation();

  if (wishlist.has(tourId)) {
    wishlist.delete(tourId);
    showToast('Đã xóa khỏi danh sách', 'Đã bỏ lưu hành trình này.', 'info');
  } else {
    wishlist.add(tourId);
    showToast('Đã lưu yêu thích ❤️', 'Hành trình đã được thêm vào danh sách lưu!', 'success');
  }

  try {
    localStorage.setItem('dicunggio_wishlist', JSON.stringify([...wishlist]));
  } catch (e) {}

  updateWishlistBadges();
  renderTours();
}

function updateWishlistBadges() {
  const badgeCountEls = document.querySelectorAll('.wishlist-count-badge');
  const count = wishlist.size;

  badgeCountEls.forEach(el => {
    el.textContent = count;
    if (count > 0) {
      el.classList.remove('hidden');
    } else {
      el.classList.add('hidden');
    }
  });
}

window.openWishlistDrawer = function() {
  const drawer = document.getElementById('wishlist-drawer');
  const list = document.getElementById('wishlist-items-list');
  if (!drawer || !list) return;

  const likedTours = TOURS_DATA.filter(t => wishlist.has(t.id));

  if (likedTours.length === 0) {
    list.innerHTML = `
      <div class="py-12 text-center text-gray-400 space-y-3">
        <i data-lucide="heart-off" class="w-12 h-12 mx-auto stroke-1"></i>
        <p class="text-xs">Bạn chưa lưu tour nào vào danh sách yêu thích.</p>
        <button onclick="closeWishlistDrawer()" class="px-4 py-2 rounded-full bg-forest text-white text-xs font-bold hover:bg-forest/90">
          Khám phá tour ngay
        </button>
      </div>
    `;
  } else {
    list.innerHTML = likedTours.map(t => `
      <div class="flex items-center gap-3 p-3 bg-gray-50 rounded-2xl border border-gray-100 relative group">
        <img src="${t.image}" alt="${t.title}" class="w-16 h-16 rounded-xl object-cover shrink-0" />
        <div class="flex-1 min-w-0">
          <h5 class="font-bold text-xs text-gray-900 truncate">${t.title}</h5>
          <span class="text-[10px] text-gray-500 block">${t.location} • ${t.duration}</span>
          <span class="text-xs font-black text-forest mt-0.5 block">${t.price}</span>
        </div>
        <div class="flex flex-col gap-1 shrink-0">
          <button 
            type="button" 
            onclick="openTourDetailModal(${t.id}); closeWishlistDrawer();" 
            class="p-1.5 rounded-lg bg-white border border-gray-200 text-forest hover:bg-forest hover:text-white transition-colors"
            title="Xem chi tiết"
          >
            <i data-lucide="eye" class="w-3.5 h-3.5"></i>
          </button>
          <button 
            type="button" 
            onclick="toggleWishlist(${t.id})" 
            class="p-1.5 rounded-lg bg-white border border-gray-200 text-red-500 hover:bg-red-50 transition-colors"
            title="Bỏ thích"
          >
            <i data-lucide="trash-2" class="w-3.5 h-3.5"></i>
          </button>
        </div>
      </div>
    `).join('');
  }

  drawer.classList.remove('hidden');
  initLucideIcons();
};

window.closeWishlistDrawer = function() {
  const drawer = document.getElementById('wishlist-drawer');
  if (drawer) drawer.classList.add('hidden');
};

// ==========================================
// 13. SEARCH OVERLAY & REAL-TIME FILTER
// ==========================================
window.openSearchModal = function() {
  const modal = document.getElementById('search-modal');
  const input = document.getElementById('search-modal-input');
  if (modal) {
    modal.classList.remove('hidden');
    if (input) {
      input.focus();
      input.value = '';
      renderSearchResults('');
    }
  }
};

window.closeSearchModal = function() {
  const modal = document.getElementById('search-modal');
  if (modal) modal.classList.add('hidden');
};

window.handleLiveSearch = function(query) {
  renderSearchResults(query.trim().toLowerCase());
};

function renderSearchResults(q) {
  const container = document.getElementById('search-results-container');
  if (!container) return;

  if (!q) {
    container.innerHTML = `
      <div class="py-6 text-center text-xs text-gray-400">
        Nhập tên ngọn núi hoặc địa danh (vd: Yên Tử, Tà Xùa, Kỳ Quan San, Cúc Phương...)
      </div>
    `;
    return;
  }

  const results = TOURS_DATA.filter(t => 
    t.title.toLowerCase().includes(q) || 
    t.location.toLowerCase().includes(q) ||
    t.description.toLowerCase().includes(q) ||
    t.code.toLowerCase().includes(q)
  );

  if (results.length === 0) {
    container.innerHTML = `
      <div class="py-8 text-center text-xs text-gray-500">
        Không tìm thấy hành trình nào với từ khóa "<strong>${q}</strong>".
      </div>
    `;
  } else {
    container.innerHTML = results.map(t => `
      <div 
        onclick="openTourDetailModal(${t.id}); closeSearchModal();" 
        class="flex items-center gap-3 p-2.5 rounded-xl hover:bg-emerald-50/70 transition-colors cursor-pointer border-b border-gray-100 last:border-0"
      >
        <img src="${t.image}" alt="${t.title}" class="w-12 h-12 rounded-lg object-cover shrink-0" />
        <div class="flex-1 min-w-0">
          <div class="flex items-center gap-1.5">
            <span class="text-[9px] font-extrabold px-1.5 py-0.2 rounded bg-emerald-100 text-forest">${t.code}</span>
            <h5 class="font-bold text-xs text-gray-900 truncate">${t.title}</h5>
          </div>
          <span class="text-[11px] text-gray-500 truncate block mt-0.5">${t.location} • ${t.duration}</span>
        </div>
        <span class="text-xs font-black text-forest shrink-0">${t.price}</span>
      </div>
    `).join('');
  }
}

// ==========================================
// 14. VIDEO MODAL LIGHTBOX
// ==========================================
window.openVideoModal = function() {
  const modal = document.getElementById('video-modal');
  if (modal) {
    modal.classList.remove('hidden');
    document.body.style.overflow = 'hidden';
  }
};

window.closeVideoModal = function() {
  const modal = document.getElementById('video-modal');
  if (modal) {
    modal.classList.add('hidden');
    document.body.style.overflow = '';
  }
};

// ==========================================
// 15. REVIEWS & TESTIMONIALS MODAL
// ==========================================
window.openReviewsModal = function() {
  const modal = document.getElementById('reviews-modal');
  const container = document.getElementById('reviews-list-container');
  if (!modal || !container) return;

  container.innerHTML = TESTIMONIALS_DATA.map(rev => `
    <div class="p-4 bg-gray-50/80 rounded-2xl border border-gray-100 space-y-2">
      <div class="flex items-center justify-between">
        <div class="flex items-center gap-2.5">
          <img src="${rev.avatar}" alt="${rev.name}" class="w-9 h-9 rounded-full object-cover border border-emerald-100 shadow-2xs" />
          <div>
            <h5 class="font-bold text-xs text-gray-900 leading-tight">${rev.name}</h5>
            <span class="text-[10px] text-forest font-medium flex items-center gap-1.5 flex-wrap">
              <span>${rev.role}</span>
              <span class="inline-flex items-center gap-0.5 text-[9.5px] font-bold text-emerald-700 bg-emerald-50 px-1.5 py-0.2 rounded-full border border-emerald-200">
                <i data-lucide="badge-check" class="w-3 h-3 text-emerald-600"></i>
                <span>✓ Đã hoàn thành chặng</span>
              </span>
            </span>
          </div>
        </div>
        <div class="flex text-amber-400">
          ${Array(rev.rating).fill('<i data-lucide="star" class="w-3 h-3 fill-amber-400 text-amber-400"></i>').join('')}
        </div>
      </div>
      <p class="text-xs text-gray-700 italic leading-relaxed">${rev.comment}</p>
      <span class="text-[10px] text-gray-400 block text-right">${rev.date}</span>
    </div>
  `).join('');

  modal.classList.remove('hidden');
  document.body.style.overflow = 'hidden';
  initLucideIcons();
};

window.closeReviewsModal = function() {
  const modal = document.getElementById('reviews-modal');
  if (modal) {
    modal.classList.add('hidden');
    document.body.style.overflow = '';
  }
};

function setupReviewsModalEvents() {
  const form = document.getElementById('new-review-form');
  if (!form) return;

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const name = document.getElementById('review-author')?.value;
    const tour = document.getElementById('review-tour')?.value;
    const text = document.getElementById('review-comment')?.value;

    if (!name || !text) return;

    TESTIMONIALS_DATA.unshift({
      id: Date.now(),
      name: name,
      role: tour || 'Trekker Đi Cùng Gió',
      verified: true,
      avatar: 'assets/images/avatar-ha.jpg',
      comment: text,
      rating: 5,
      date: 'Vừa xong'
    });

    form.reset();
    showToast('Cảm ơn bạn!', 'Đánh giá của bạn đã được gửi thành công!', 'success');
    openReviewsModal();
  });
}

// ==========================================
// 16. TOAST NOTIFICATION UTILITY
// ==========================================
function showToast(title, message, type = 'info') {
  const toast = document.createElement('div');
  toast.className = `fixed bottom-5 right-5 z-50 max-w-sm w-full p-4 rounded-2xl bg-white shadow-2xl border border-gray-100 flex items-start gap-3 transform translate-y-10 opacity-0 transition-all duration-300 pointer-events-auto`;

  let iconHtml = '<i data-lucide="info" class="w-5 h-5 text-forest shrink-0 mt-0.5"></i>';
  if (type === 'success') {
    iconHtml = '<i data-lucide="check-circle-2" class="w-5 h-5 text-emerald-600 shrink-0 mt-0.5"></i>';
  } else if (type === 'error') {
    iconHtml = '<i data-lucide="alert-circle" class="w-5 h-5 text-red-500 shrink-0 mt-0.5"></i>';
  }

  toast.innerHTML = `
    ${iconHtml}
    <div class="flex-1 min-w-0">
      <h6 class="font-bold text-xs text-gray-900">${title}</h6>
      <p class="text-xs text-gray-500 mt-0.5">${message}</p>
    </div>
    <button onclick="this.parentElement.remove()" class="text-gray-400 hover:text-gray-600 p-1">
      <i data-lucide="x" class="w-4 h-4"></i>
    </button>
  `;

  document.body.appendChild(toast);
  initLucideIcons();

  setTimeout(() => {
    toast.classList.remove('translate-y-10', 'opacity-0');
  }, 50);

  setTimeout(() => {
    toast.classList.add('translate-y-10', 'opacity-0');
    setTimeout(() => toast.remove(), 300);
  }, 3500);
}

// ==========================================
// 17. SCROLL OBSERVERS & INTERACTIONS
// ==========================================
function setupScrollReveal() {
  const elements = document.querySelectorAll('.reveal-on-scroll');
  if (!elements.length) return;

  const reveal = (el) => {
    if (!el) return;
    el.classList.add('revealed');
    el.classList.add('visible');
  };

  if (!('IntersectionObserver' in window)) {
    elements.forEach(reveal);
    return;
  }

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        reveal(entry.target);
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.05, rootMargin: '0px 0px 100px 0px' });

  elements.forEach(el => {
    const rect = el.getBoundingClientRect();
    const hash = window.location.hash ? window.location.hash.substring(1) : '';
    if (rect.top < window.innerHeight + 150 || (hash && el.id === hash)) {
      reveal(el);
    } else {
      observer.observe(el);
    }
  });

  // Guarantee reveal after 500ms
  setTimeout(() => {
    elements.forEach(reveal);
  }, 500);

  // Hash navigation listener
  window.addEventListener('hashchange', () => {
    const activeHash = window.location.hash ? window.location.hash.substring(1) : '';
    if (activeHash) {
      const target = document.getElementById(activeHash);
      if (target) reveal(target);
    }
  });
}

function setupScrollSpy() {
  const sections = document.querySelectorAll('section[id], main[id]');
  const navLinks = document.querySelectorAll('.nav-link');

  window.addEventListener('scroll', () => {
    let current = '';
    const scrollPos = window.scrollY + 200;

    sections.forEach(section => {
      const sectionTop = section.offsetTop;
      const sectionHeight = section.offsetHeight;
      if (scrollPos >= sectionTop && scrollPos < sectionTop + sectionHeight) {
        current = section.getAttribute('id');
      }
    });

    navLinks.forEach(link => {
      const href = link.getAttribute('href');
      if (href && href.startsWith('#')) {
        const targetId = href.substring(1);
        if (targetId === current) {
          link.classList.add('active');
        } else {
          link.classList.remove('active');
        }
      }
    });
  });
}

// ==========================================
// 18. POLICY MODAL CONTROLLER
// ==========================================
window.openPolicyModal = function() {
  const modal = document.getElementById('policy-modal');
  if (modal) {
    modal.classList.remove('hidden');
    document.body.style.overflow = 'hidden';
    initLucideIcons();
  }
};

window.closePolicyModal = function() {
  const modal = document.getElementById('policy-modal');
  if (modal) {
    modal.classList.add('hidden');
    document.body.style.overflow = '';
  }
};
