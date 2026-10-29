# -*- coding: utf-8 -*-
"""
Script to generate assets/js/main.js with complete datasets, route steps,
historical storytelling, and refined UI/UX interactions.
"""

import sys

content = r'''/**
 * Trekking Đi Cùng Gió - Interactive Prototype Engine (Version 3.2)
 * "Khám phá thiên nhiên, chinh phục mọi giới hạn"
 */

// ==========================================
// 1. TOUR DATA REPOSITORY (ALL 5 CATEGORIES)
// ==========================================
const TOURS_DATA = [
  // --- TOUR 1: YÊN TỬ – CHÙA ĐỒNG ---
  {
    id: 1,
    title: 'Trekking Yên Tử – Chùa Đồng',
    category: 'trekking',
    subCategory: 'spiritual',
    categoryName: 'Trekking',
    duration: '1 ngày',
    location: 'Hà Nội – Yên Tử (Quảng Ninh)',
    price: '1.200.000đ/người',
    priceNum: 1200000,
    rating: 5.0,
    reviews: 128,
    image: 'assets/images/tour-yen-tu.jpg',
    badge: 'Trekking',
    altitudeBadge: '⛰️ 1.068m',
    altitude: '1.068m',
    trekDistance: '14 km',
    difficultyLevel: 2,
    difficultyText: 'Nhẹ - Trung bình',
    isFeatured: true,
    shortSummary: 'Hành hương về non thiêng đất Phật, băng rừng Tùng cổ thụ chạm đỉnh Chùa Đồng (1.068m).',
    routeMap: 'Xuất phát từ Hà Nội đi thành phố Uông Bí (tỉnh Quảng Ninh). Cung trekking bắt đầu từ suối Giải Oan, băng qua Đường Tùng cổ thụ 700 năm tuổi, vườn tháp Tổ Huệ Quang, chùa Hoa Yên, chùa Một Mái, chùa Bảo Sái, vượt dốc Đá Chồng và chinh phục đỉnh cao nhất tại Chùa Đồng (1.068m) giữa mây ngàn Đông Bắc.',
    routeSteps: ['Hà Nội', 'Suối Giải Oan', 'Đường Tùng 700 năm', 'Vườn Tháp Huệ Quang', 'Chùa Hoa Yên', 'Dốc Đá Chồng', 'Đỉnh Chùa Đồng (1.068m)'],
    historyStory: 'Núi Yên Tử (còn gọi là Bạch Vân Sơn – núi mây trắng) là cái nôi của Thiền phái Trúc Lâm Việt Nam. Năm 1299, sau khi lãnh đạo quân dân Đại Việt hai lần đánh bại đế quốc Nguyên – Mông, vua Trần Nhân Tông đã nhường ngôi, từ bỏ hoàng cung để lên núi Yên Tử tu hành, lấy hiệu là Hương Vân Đại Đầu Đà (Phật hoàng Trần Nhân Tông) và hợp nhất các dòng thiền thành Thiền phái Trúc Lâm mang đậm tinh thần nhập thế và bản sắc dân tộc Việt. Chùa Đồng trên đỉnh núi được khởi dựng từ thời Hậu Lê và hiện là ngôi chùa bằng đồng nguyên khối trên đỉnh núi lớn nhất châu Á.',
    description: 'Hành trình leo núi thiêng Yên Tử, chiêm bái Chùa Đồng trên đỉnh Phù Vân, rèn luyện thể lực và tìm lại an yên trong tâm hồn giữa mây ngàn đại ngàn.',
    departureDates: ['26/10/2026', '02/11/2026', '09/11/2026', '16/11/2026'],
    gallery: [
      { url: 'assets/images/tour-yen-tu.jpg', caption: 'Chóp Chùa Đồng giữa mây ngàn Yên Tử' },
      { url: 'assets/images/yen-tu-1.jpg', caption: 'Mái chùa đồng cổ kính linh thiêng trên đỉnh núi đá' },
      { url: 'assets/images/yen-tu-2.jpg', caption: 'Toàn cảnh non thiêng Yên Tử từ độ cao 1.068m' },
      { url: 'assets/images/yen-tu-3.jpg', caption: 'Hành hương qua Đường Tùng cổ thụ 700 năm tuổi' }
    ],
    highlights: [
      'Chạm tay vào Chùa Đồng đúc bằng đồng nguyên khối lớn nhất Châu Á trên đỉnh Phù Vân.',
      'Dạo bước giữa rừng trúc bạt ngàn ngàn năm tuổi và đường Tùng cổ thụ 700 năm.',
      'Đón ánh hoàng hôn dát vàng trên non thiêng Yên Tử thanh tịnh và an lạc.'
    ],
    itinerary: [
      { day: '05:30', title: 'Hà Nội – Uông Bí', desc: 'Xe đón đoàn tại Nhà Hát Lớn Hà Nội, khởi hành đi Uông Bí (Quảng Ninh). Dừng chân ăn sáng đặc sản bánh cuốn chả mực.' },
      { day: '08:30', title: 'Bắt đầu trekking Yên Tử', desc: 'Đoàn khởi động tại chân núi, trekking qua Tháp Tổ, chùa Hoa Yên, chùa Một Mái giữa tiếng suối reo và rừng thông rì rào.' },
      { day: '12:00', title: 'Chạm đỉnh Chùa Đồng 1.068m', desc: 'Chiêm bái Chùa Đồng linh thiêng trong sương mây, thưởng ngoạn panorama toàn cảnh Đông Bắc, dùng bữa trưa picnic nóng hổi.' },
      { day: '17:30', title: 'Trở về Hà Nội', desc: 'Xuống núi, thư giãn ngâm chân thảo dược lá thuốc người Dao, lên xe về lại thủ đô lúc 20:00.' }
    ],
    included: ['Xe du lịch 16-29 chỗ khứ hồi', 'Leader dẫn đường & Hướng dẫn viên', 'Bữa trưa nóng hổi trên núi', 'Bảo hiểm du lịch 100.000.000đ', 'Gậy trekking & áo mưa tiêu chuẩn', 'Nước uống điện giải suốt tuyến'],
    preparation: ['Giày leo núi có gai bám đá tốt', 'Quần áo co giãn thấm hút mồ hôi', 'Áo gió nhẹ giữ ấm khi lên đỉnh gió to', 'Bình nước cá nhân & mũ nón']
  },

  // --- TOUR 2: TÀ XÙA – SĂN MÂY ---
  {
    id: 2,
    title: 'Tà Xùa – Săn mây',
    category: 'trekking',
    subCategory: 'experience',
    categoryName: 'Trekking',
    duration: '2 ngày 1 đêm',
    location: 'Hà Nội – Tà Xùa (Sơn La)',
    price: '1.850.000đ/người',
    priceNum: 1850000,
    rating: 5.0,
    reviews: 96,
    image: 'assets/images/tour-ta-xua.jpg',
    badge: 'Trekking',
    altitudeBadge: '☁️ 2.865m',
    altitude: '2.865m',
    trekDistance: '16 km',
    difficultyLevel: 3,
    difficultyText: 'Trung bình',
    isFeatured: true,
    shortSummary: 'Chinh phục "Sống lưng khủng long" Háng Đồng và đón biển mây kỳ vĩ bậc nhất Tây Bắc.',
    routeMap: 'Khởi hành từ Hà Nội theo hướng Quốc lộ 32 lên xã vùng cao Tà Xùa (huyện Bắc Yên, tỉnh Sơn La). Hành trình đưa bạn đi dọc "Sống lưng khủng long" tại bản Háng Đồng, check-in Mỏm Cá Heo, Cây Cô Đơn, Đỉnh Gió, thảo nguyên Tà Xùa và khám phá bản làng của người Mông ẩn mình giữa đại ngàn.',
    routeSteps: ['Hà Nội', 'Bắc Yên (Sơn La)', 'Xã Tà Xùa', 'Sống lưng khủng long Háng Đồng', 'Mỏm Cá Heo & Cây Cô Đơn', 'Đỉnh Gió (2.865m)'],
    historyStory: 'Tà Xùa là dãy núi hợp thành từ ba đỉnh núi hùng vĩ thuộc phần kéo dài về phía Nam của dãy Hoàng Liên Sơn, tạo nên ranh giới tự nhiên giữa hai tỉnh Sơn La và Yên Bái. Nhờ địa hình thung lũng lòng chảo được bao bọc bởi các dãy núi cao chắn gió, Tà Xùa giữ được những biển mây dày đặc, lâu tan bậc nhất Việt Nam. Đây cũng là vùng đất sinh sống lâu đời của đồng bào dân tộc Mông với những rừng chè Shan Tuyết cổ thụ hàng trăm năm tuổi mọc tự nhiên trong sương mù.',
    description: 'Chinh phục "sống lưng khủng long" huyền thoại Bản Công, đắm chìm trong biển mây bồng bềnh lúc bình minh và tận hưởng bầu không khí Tây Bắc se lạnh.',
    departureDates: ['01/11/2026', '08/11/2026', '15/11/2026', '22/11/2026'],
    gallery: [
      { url: 'assets/images/tour-ta-xua.jpg', caption: 'Biển mây bồng bềnh cuộn trào thung lũng Tà Xùa' },
      { url: 'assets/images/ta-xua-1.jpg', caption: 'Bình minh rực rỡ trên sống lưng khủng long Háng Đồng' },
      { url: 'assets/images/ta-xua-2.jpg', caption: 'Trekker check-in mỏm đá ngắm đại ngàn Tây Bắc' },
      { url: 'assets/images/hero-bg.jpg', caption: 'Toàn cảnh biển mây Tây Bắc lúc rạng đông' }
    ],
    highlights: [
      'Đi bộ trên Sống Lưng Khủng Long kỳ vĩ với biển mây cuồn cuộn hai bên vực sâu.',
      'Check-in Mỏm Cá Heo, Cây Táo Mèo cô đơn ngắm hoàng hôn đỏ rực thung lũng Bản Công.',
      'Thưởng thức lẩu gà đen đồi H’Mông nóng hổi bên bếp than hồng và đốt lửa trại giao lưu.'
    ],
    itinerary: [
      { day: 'Ngày 1', title: 'Hà Nội – Bắc Yên – Đỉnh Gió Tà Xùa', desc: '06:00 xuất phát từ Hà Nội qua đèo Kê, đèo Chẹn. Chiều trekking Mỏm Cá Heo, đón hoàng hôn trên Đỉnh Gió. Tối thưởng thức lẩu gà đen.' },
      { day: 'Ngày 2', title: 'Sống lưng khủng long – Biển mây – Hà Nội', desc: '05:30 dậy sớm đón bình minh biển mây ngút ngàn tại Háng Đồng. Chinh phục Sống Lưng Khủng Long. Chiều về lại Hà Nội khoảng 19:30.' }
    ],
    included: ['Xe giường nằm / Limousine khứ hồi', 'Homestay view mây Bản Công', 'Các bữa ăn tiêu chuẩn vùng cao', 'Leader & Porter bản địa chu đáo', 'Bảo hiểm du lịch trọn gói 100tr', 'Gậy trekking & đồ y tế sơ cứu'],
    preparation: ['Áo khoác ấm (nhiệt độ đêm ~10°C)', 'Giày trekking chống trơn trượt', 'Sạc dự phòng & máy ảnh', 'Thuốc chống cảm & dầu gió']
  },

  // --- TOUR 3: PHU SA PHIN – CHINH PHỤC ĐỈNH CAO ---
  {
    id: 3,
    title: 'Phu Sa Phin – Chinh phục đỉnh cao',
    category: 'trekking',
    subCategory: 'experience',
    categoryName: 'Trekking',
    duration: '2 ngày 1 đêm',
    location: 'Hà Nội – Phu Sa Phin',
    price: '1.890.000đ/người',
    priceNum: 1890000,
    rating: 5.0,
    reviews: 74,
    image: 'assets/images/tour-phu-sa-phin.jpg',
    badge: 'Trekking',
    altitudeBadge: '🏔️ 2.868m',
    altitude: '2.868m',
    trekDistance: '22 km',
    difficultyLevel: 4,
    difficultyText: 'Thách thức',
    isFeatured: true,
    shortSummary: 'Băng rừng rêu cổ tích nguyên sinh, chinh phục chóp đỉnh Phu Sa Phin (2.868m) hùng vĩ.',
    routeMap: 'Di chuyển từ Hà Nội đến vùng núi giáp ranh giữa huyện Trạm Tấu (Yên Bái) và huyện Bắc Yên (Sơn La). Cung đường trekking dài khoảng 22km đưa người leo vượt qua Mỏm Đầu Rùa, sống lưng khủng long cheo leo dài gần 3km và xuyên qua khu rừng nguyên sinh phủ đầy rêu xanh ma mị trước khi chạm tay vào chóp inox trên đỉnh Phu Sa Phin (2.868m).',
    routeSteps: ['Hà Nội', 'Bản Trạm Tấu / Bắc Yên', 'Mỏm Đầu Rùa', 'Sống lưng khủng long 3km', 'Rừng rêu nguyên sinh', 'Chóp đỉnh Phu Sa Phin (2.868m)'],
    historyStory: 'Phu Sa Phin là tên gọi nguyên bản theo tiếng của người Mông bản địa dành cho đỉnh núi cao nhất trên dãy Tà Xùa (nằm trong Top 10 đỉnh núi cao nhất Việt Nam). Trong nhiều năm trước đây, giới leo núi thường gọi chung đỉnh này là "Đỉnh Tà Xùa". Đến cuối năm 2022, tên gọi lịch sử "Phu Sa Phin" cùng độ cao chuẩn 2.868m chính thức được khắc lên chóp đỉnh mới, tôn vinh văn hóa bản địa và đánh dấu một trong những cung đường trekking có địa hình sống núi đẹp và thử thách nhất Tây Bắc.',
    description: 'Cung đường hoang sơ đầy thách thức với những vách đá hùng vĩ, thảm thực vật đỗ quyên nguyên sinh và tầm nhìn panorama ngoạn mục bậc nhất Tây Bắc.',
    departureDates: ['08/11/2026', '22/11/2026', '06/12/2026'],
    highlights: [
      'Băng qua khu rừng rêu ma mị đẹp tựa thế giới Avatar giữa lòng Tây Bắc.',
      'Vượt sống lưng khủng long dốc cheo leo dài gần 3km đầy phấn khích.',
      'Chạm mốc đỉnh Phu Sa Phin 2.868m – Top 10 đỉnh núi cao nhất Việt Nam.'
    ],
    itinerary: [
      { day: 'Đêm 0', title: 'Hà Nội – Điểm tập kết', desc: '21:30 đón tại Hà Nội đi xe giường nằm chất lượng cao tới chân núi.' },
      { day: 'Ngày 1', title: 'Bắt đầu leo dốc – Hạ trại lán rừng', desc: 'Ăn sáng, phân chia đồ dùng cùng Porter. Bắt đầu leo qua các dốc đá và rừng thảo quả. Chiều tới lán nghỉ 2.400m, nướng thịt ăn tối.' },
      { day: 'Ngày 2', title: 'Chạm đỉnh đón bình minh – Xuống núi', desc: '05:00 xuất phát lên đỉnh đón bình minh biển mây. Xuống núi, tắm lá thuốc người Dao đỏ và lên xe về Hà Nội.' }
    ],
    included: ['Xe đưa đón giường nằm cao cấp', 'Porter bản địa gùi đồ & nấu ăn', 'Ngủ lán gỗ ấm cúng có chăn dày', 'Các bữa ăn đậm đà bản sắc', 'Bảo hiểm du lịch 100.000.000đ', 'Giấy phép trekking ban quản lý'],
    preparation: ['Balo trợ lực 30-40L', 'Đèn pin đội đầu loại sáng tốt', 'Áo mưa bộ chống nước tuyệt đối', 'Găng tay leo núi có hạt cao su']
  },

  // --- TOUR 4: KỲ QUAN SAN – ĐỈNH NÚI HÙNG VĨ ---
  {
    id: 4,
    title: 'Kỳ Quan San – Đỉnh núi hùng vĩ',
    category: 'trekking',
    subCategory: 'experience',
    categoryName: 'Trekking',
    duration: '3 ngày 2 đêm',
    location: 'Hà Nội – Lào Cai',
    price: '2.650.000đ/người',
    priceNum: 2650000,
    rating: 5.0,
    reviews: 52,
    image: 'assets/images/tour-ky-quan-san.jpg',
    badge: 'Trekking',
    altitudeBadge: '🏔️ 3.046m',
    altitude: '3.046m',
    trekDistance: '32 km',
    difficultyLevel: 5,
    difficultyText: 'Thử thách cao',
    isFeatured: true,
    shortSummary: 'Chinh phục ngọn núi cao thứ 4 Việt Nam (3.046m) và ngắm bình minh huyền thoại tại Đỉnh Núi Muối.',
    routeMap: 'Xuất phát từ Hà Nội lên bản Kỳ Quan San (xã Sàng Ma Sáo, huyện Bát Xát, tỉnh Lào Cai). Đoàn trekking băng qua rừng thảo quả, rừng trúc lùn, rừng đỗ quyên cổ thụ, nghỉ đêm tại lán gỗ ở độ cao 2.100m để đón bình minh rực lửa trên Đỉnh Núi Muối, sau đó vượt các vách đá dựng đứng chinh phục đỉnh Kỳ Quan San ở độ cao 3.046m.',
    routeSteps: ['Hà Nội', 'Bản Sàng Ma Sáo (Bát Xát)', 'Rừng Thảo Quả & Trúc Lùn', 'Lán Gỗ 2.100m', 'Đón bình minh Núi Muối', 'Chóp đỉnh Kỳ Quan San (3.046m)'],
    historyStory: 'Nằm trên ranh giới tự nhiên giữa hai huyện Bát Xát (Lào Cai) và Phong Thổ (Lai Châu), ngọn núi cao thứ 4 Việt Nam này từng được những nhóm phượt thủ đầu tiên mở đường vào năm 2012 đặt tên là "Bạch Mộc Lương Tử" (dãy núi cây gỗ trắng). Sau này, chính quyền và cộng đồng địa phương đã khôi phục lại tên gọi lịch sử chính xác trên bản đồ địa chính là "Kỳ Quan San" – gắn liền với ngôi bản cổ của đồng bào người Mông và người Dao dưới chân núi vùng biên viễn Tây Bắc.',
    description: 'Chinh phục đỉnh núi cao thứ 4 Việt Nam (3.046m), ngắm đồi Muối lung linh dưới ánh sao đêm và biển mây ngút ngàn tầm mắt đón bình minh.',
    departureDates: ['15/11/2026', '29/11/2026', '13/12/2026'],
    highlights: [
      'Chinh phục đỉnh núi Bạch Mộc Lương Tử (Kỳ Quan San) cao 3.046m huyền thoại.',
      'Đón hoàng hôn và bình minh ngoạn mục tại Đồi Muối 2.100m đẹp bậc nhất Việt Nam.',
      'Vượt qua sống trâu đá hiểm trở với sự bọc lót an toàn tuyệt đối từ đội ngũ Leader.'
    ],
    itinerary: [
      { day: 'Đêm 0', title: 'Hà Nội – Sàng Ma Sáo', desc: 'Xe giường nằm khởi hành 22:00 từ Hà Nội lên Bát Xát (Lào Cai).' },
      { day: 'Ngày 1', title: 'Sàng Ma Sáo – Đồi Muối 2.100m', desc: 'Trekking xuyên rừng trúc, suối đá. 16:30 đến Đồi Muối, cắm trại ngắm hoàng hôn dát vàng biển mây.' },
      { day: 'Ngày 2', title: 'Chinh phục đỉnh 3.046m – Về lán', desc: 'Vượt qua sống trâu hiểm trở, chạm đỉnh Kỳ Quan San lúc 10:30 trưa. Quay về Đồi Muối nghỉ đêm thứ hai.' },
      { day: 'Ngày 3', title: 'Xuống núi – Tắm lá Dao – Hà Nội', desc: 'Xuống núi về bản Mông, tắm lá thuốc thư giãn, liên hoan lẩu cá tầm Sa Pa trước khi lên xe về Hà Nội.' }
    ],
    included: ['Toàn bộ xe di chuyển khứ hồi', 'Đội ngũ Porter & Leader 1:3', 'Chỗ ngủ lán gỗ đầy đủ chăn đệm', 'Thực đơn 6 bữa chính thịnh soạn', 'Bảo hiểm du lịch mạo hiểm cao cấp', 'Huy chương & Chứng nhận chinh phục'],
    preparation: ['Thể lực rèn luyện trước tối thiểu 2 tuần', 'Giày leo núi chuyên dụng chống trơn', 'Quần áo ấm nhiều lớp (nhiệt độ đỉnh 0-5°C)', 'Miếng dán giữ nhiệt & gậy trekking']
  },

  // --- TOUR 5: TÀ CHÌ NHÙ – MÙA HOA CHI PÂU ---
  {
    id: 5,
    title: 'Tà Chì Nhù – Mùa Hoa Chi Pâu',
    category: 'trekking',
    subCategory: 'experience',
    categoryName: 'Trekking',
    duration: '2 ngày 1 đêm',
    location: 'Hà Nội – Yên Bái',
    price: '1.850.000đ/người',
    priceNum: 1850000,
    rating: 5.0,
    reviews: 86,
    image: 'assets/images/tour-ta-chi-nhu.jpg',
    badge: 'Trekking',
    altitudeBadge: '🌸 2.979m',
    altitude: '2.979m',
    trekDistance: '24 km',
    difficultyLevel: 4,
    difficultyText: 'Khá thách thức',
    isFeatured: false,
    shortSummary: 'Lạc bước giữa đại ngàn hoa Chi Pâu tím biếc và thảo nguyên ngựa hoang trên mây ở độ cao 2.979m.',
    routeMap: 'Từ Hà Nội di chuyển tới khu vực Mỏ Chì (xã Xà Hồ, huyện Trạm Tấu, tỉnh Yên Bái). Cung trekking vượt qua những con dốc đất dài bất tận để lên tới vùng thảo nguyên núi cao trên 2.400m – nơi những triền đồi phủ kín sắc tím hoa Chi Pâu mỗi độ thu về, trước khi chinh phục đỉnh Tà Chì Nhù (2.979m).',
    routeSteps: ['Hà Nội', 'Trạm Tấu (Yên Bái)', 'Khu Mỏ Chì (Xã Xà Hồ)', 'Dốc Ba Tầng', 'Lán nghỉ 2.400m (Thảo nguyên Chi Pâu)', 'Chóp đỉnh Tà Chì Nhù (2.979m)'],
    historyStory: 'Thuộc khối núi Pú Luông của dãy Hoàng Liên Sơn, đỉnh núi cao thứ 7 Việt Nam này được người Thái gọi là "Pú Luông", còn người Mông bản địa gọi là "Tà Chì Nhù". Khu vực chân núi xã Xà Hồ từng là nơi người Pháp mở mỏ khai thác chì – kẽm từ đầu thế kỷ 20, trong khi các sườn cỏ mênh mông phía trên đỉnh núi từ bao đời nay là bãi chăn thả ngựa và dê tự nhiên của đồng bào người Mông, tạo nên khung cảnh du mục độc nhất vô nhị tại Việt Nam.',
    description: 'Chinh phục nóc nhà Yên Bái 2.979m, đắm chìm trong sắc tím hoa Chi Pâu bung nở khắp thảo nguyên và ngắm những đàn ngựa thong dong gặm cỏ trên biển mây.',
    departureDates: ['22/11/2026', '06/12/2026', '20/12/2026'],
    highlights: [
      'Ngắm trọn vẹn thảo nguyên hoa Chi Pâu tím biếc phủ kín các sườn núi cao trên 2.400m.',
      'Chạm tay vào chóp kim loại đỉnh Tà Chì Nhù 2.979m – nóc nhà tỉnh Yên Bái.',
      'Thưởng thức khoai nướng, thịt nướng thơm lừng bên lán gỗ ấm áp giữa biển sương.'
    ],
    itinerary: [
      { day: 'Ngày 1', title: 'Hà Nội – Trạm Tấu – Lán nghỉ 2.400m', desc: 'Khởi hành từ Hà Nội lúc 05:30. 11:30 đến Mỏ Chì (Xà Hồ), bắt đầu vượt dốc Ba Tầng. 16:30 đến lán nghỉ ngắm hoàng hôn tím ngắt.' },
      { day: 'Ngày 2', title: 'Đón bình minh đỉnh 2.979m – Về Hà Nội', desc: '05:00 trekking lên chóp đỉnh đón mặt trời ló rạng trên biển mây. Trưa xuống núi tắm suối khoáng nóng Trạm Tấu trước khi về Hà Nội.' }
    ],
    included: ['Xe Limousine / Giường nằm chất lượng cao', 'Vé tắm khoáng nóng thư giãn Trạm Tấu', 'Porter bản địa gùi hành lý và nấu ăn', 'Toàn bộ bữa ăn chính và đồ ăn nhẹ', 'Bảo hiểm du lịch mạo hiểm 100.000.000đ'],
    preparation: ['Giày trekking bám đất tốt chống trơn trượt dốc', 'Áo khoác gió & áo ấm giữ nhiệt', 'Mũ rộng vành & kem chống nắng']
  },

  // --- TOUR 6: HÀNH HƯƠNG TAM CHÚC ---
  {
    id: 6,
    title: 'Hành hương Tam Chúc – Ba Sao An Nhiên',
    category: 'spiritual',
    subCategory: 'near_hanoi',
    categoryName: 'Tâm linh',
    duration: '1 ngày',
    location: 'Hà Nội – Hà Nam',
    price: '950.000đ/người',
    priceNum: 950000,
    rating: 4.9,
    reviews: 88,
    image: 'assets/images/tour-tam-chuc.jpg',
    badge: 'Tâm linh',
    altitudeBadge: '🪷 An yên',
    altitude: '250m',
    trekDistance: '6 km',
    difficultyLevel: 1,
    difficultyText: 'Nhẹ nhàng',
    isFeatured: false,
    shortSummary: 'Du thuyền hồ Lục Nhạc, chiêm bái ngôi chùa lớn nhất thế giới giữa cảnh sắc sơn thủy hữu tình.',
    routeMap: 'Khởi hành từ trung tâm Hà Nội theo cao tốc Pháp Vân – Cầu Giẽ đến thị trấn Ba Sao (huyện Kim Bảng, tỉnh Hà Nam). Đoàn lên thuyền du ngoạn lòng hồ Lục Nhạc, ghé thăm đình Tam Chúc cổ kính, vãng cảnh Điện Tam Thế, Điện Pháp Chủ, Điện Quan Âm và leo bộ lên Chùa Ngọc trên đỉnh núi Thất Tinh.',
    routeSteps: ['Hà Nội', 'Thị trấn Ba Sao (Hà Nam)', 'Du thuyền Hồ Lục Nhạc', 'Đình Tam Chúc', 'Điện Tam Thế & Điện Pháp Chủ', 'Chùa Ngọc (Núi Thất Tinh)'],
    historyStory: 'Khu danh thắng Tam Chúc gắn liền với huyền tích "Tiền Lục Nhạc – Hậu Thất Tinh", kể về 6 quả núi nổi lên giữa lòng hồ tượng trưng cho 6 chiếc chuông nhà trời và 7 ngọn núi phía sau tỏa sáng tựa 7 ngôi sao. Chùa Tam Chúc cổ được xây dựng từ thời nhà Đinh cách đây hơn 1.000 năm. Quần thể chùa mới hiện nay lưu giữ bức tường đá phù điêu khổng lồ bằng đá dung nham núi lửa do các nghệ nhân Hồi giáo Indonesia tạc thủ công và cây Bồ Đề quý được chiết từ Cây Bồ Đề Vĩ Đại 2.250 tuổi tại Sri Lanka.',
    description: 'Chuyến hành hương tìm về cõi Phật thanh tịnh giữa non nước Ninh Bình - Hà Nam, du thuyền trên hồ Lục Nhạc và viếng chùa Tam Chúc linh thiêng.',
    departureDates: ['01/11/2026', '15/11/2026', '29/11/2026'],
    highlights: [
      'Đi thuyền du ngoạn ngắm cảnh non nước hữu tình trên hồ Lục Nhạc.',
      'Chiêm bái Điện Tam Thế, Điện Pháp Chủ và Điện Quan Âm nguy nga thanh tịnh.',
      'Thưởng thức bữa cơm chay thanh lọc thân tâm trong không gian an lạc.'
    ],
    itinerary: [
      { day: '07:00', title: 'Khởi hành Hà Nội – Hà Nam', desc: 'Xe đón tại điểm hẹn, phổ biến ý nghĩa tâm linh của chuyến đi.' },
      { day: '09:00', title: 'Du thuyền hồ Lục Nhạc & Chùa Tam Chúc', desc: 'Đi thuyền vãng cảnh, dâng hương chiêm bái các pho tượng đồng khổng lồ.' },
      { day: '12:30', title: 'Thực dưỡng cơm chay thanh tịnh', desc: 'Dùng bữa cơm chay bổ dưỡng, tĩnh tâm nghe chuông chùa ngân vang.' },
      { day: '16:30', title: 'Khởi hành về Hà Nội', desc: 'Ghé thăm làng nghề truyền thống mua quà cho gia đình, về đến Hà Nội lúc 18:30.' }
    ],
    included: ['Xe đưa đón chất lượng cao', 'Vé du thuyền hồ Tam Chúc', 'Bữa trưa thực dưỡng chay thịnh soạn', 'Hướng dẫn viên am hiểu Phật pháp', 'Bảo hiểm du lịch', 'Nước uống & khăn lạnh'],
    preparation: ['Trang phục lịch sự kín đáo', 'Giày bệt hoặc giày thể thao êm chân', 'Tâm thái an yên nhẹ nhàng']
  },

  // --- TOUR 7: CHÙA HƯƠNG ---
  {
    id: 7,
    title: 'Chiêm bái Chùa Hương – Suối Yến Mùa Hoa Súng',
    category: 'spiritual',
    subCategory: 'near_hanoi',
    categoryName: 'Tâm linh',
    duration: '1 ngày',
    location: 'Hà Nội – Mỹ Đức',
    price: '890.000đ/người',
    priceNum: 890000,
    rating: 4.8,
    reviews: 64,
    image: 'assets/images/tour-chua-huong.jpg',
    badge: 'Tâm linh',
    altitudeBadge: '🌸 Thanh tịnh',
    altitude: '390m',
    trekDistance: '8 km',
    difficultyLevel: 2,
    difficultyText: 'Nhẹ - Vừa',
    isFeatured: false,
    shortSummary: 'Xuôi dòng Suối Yến ngắm hoa súng nở rộ, leo núi vãng cảnh Động Hương Tích – Nam Thiên Đệ Nhất Động.',
    routeMap: 'Từ trung tâm Hà Nội di chuyển 60km về bến Đục (huyện Mỹ Đức). Đoàn ngồi thuyền nan truyền thống xuôi dòng suối Yến thơ mộng rợp sắc hoa súng, cập bến đền Trình, chiêm bái chùa Thiên Trù và leo bộ qua các bậc đá rêu phong chinh phục Động Hương Tích.',
    routeSteps: ['Hà Nội', 'Bến Đục (Mỹ Đức)', 'Thuyền nan Suối Yến', 'Đền Trình & Chùa Thiên Trù', 'Bậc đá núi Hương Sơn', 'Động Hương Tích'],
    historyStory: 'Chùa Hương (Hương Sơn) là trung tâm Phật giáo linh thiêng bậc nhất xứ Đàng Ngoài từ thế kỷ 15. Tương truyền, đây là nơi Bồ Tát Quán Thế Âm đã ứng hiện tu hành đắc đạo cứu độ chúng sinh. Năm 1770, chúa Tĩnh Đô Vương Trịnh Sâm khi tuần du vãng cảnh đã tự tay đề 5 chữ vàng "Nam Thiên Đệ Nhất Động" (Động đẹp nhất trời Nam) lên cửa động Hương Tích hình hàm rồng uy nghiêm.',
    description: 'Xuôi dòng suối Yến thơ mộng ngắm hoa súng rực rỡ, leo các bậc đá cổ kính lên Động Hương Tích linh thiêng cầu bình an cho gia đạo.',
    departureDates: ['08/11/2026', '22/11/2026', '06/12/2026'],
    highlights: [
      'Ngồi thuyền nan trôi nhẹ giữa dòng Suối Yến ngắm hoa súng nở hồng rực rỡ.',
      'Chiêm bái chùa Thiên Trù cổ kính và động Hương Tích linh thiêng.',
      'Leo bộ rèn luyện sức khỏe qua các bậc đá núi Hương Sơn phủ bóng mát.'
    ],
    itinerary: [
      { day: '06:30', title: 'Hà Nội – Bến Đục', desc: 'Khởi hành từ Hà Nội, đến bến Đục lên thuyền nan xuôi dòng suối Yến.' },
      { day: '09:00', title: 'Xuôi dòng Suối Yến', desc: 'Thưởng ngoạn cảnh sắc mộng mơ suối Yến mùa hoa súng nở rộ.' },
      { day: '11:00', title: 'Chùa Thiên Trù – Động Hương Tích', desc: 'Dâng hương lễ Phật, chiêm ngưỡng bầu nhũ đá kỳ ảo trong động.' },
      { day: '16:30', title: 'Về lại Hà Nội', desc: 'Thuyền đưa đoàn về bến Đục, lên xe trở về trung tâm Hà Nội lúc 18:30.' }
    ],
    included: ['Xe du lịch đời mới máy lạnh', 'Thuyền nan khứ hồi suối Yến', 'Vé thắng cảnh danh lam Chùa Hương', 'Bữa trưa đặc sản rau sắng chùa Hương', 'Hướng dẫn viên suốt tuyến'],
    preparation: ['Trang phục kín đáo khi vào chùa', 'Giày đi bộ êm chân', 'Mũ nón che nắng']
  },

  // --- TOUR 8: BÁI ĐÍNH – TRÀNG AN ---
  {
    id: 8,
    title: 'Hành hương Bái Đính – Non nước Tràng An',
    category: 'spiritual',
    subCategory: 'near_hanoi',
    categoryName: 'Tâm linh',
    duration: '1 ngày',
    location: 'Hà Nội – Ninh Bình',
    price: '990.000đ/người',
    priceNum: 990000,
    rating: 4.9,
    reviews: 110,
    image: 'assets/images/tour-bai-dinh.jpg',
    badge: 'Tâm linh',
    altitudeBadge: '🏯 Di sản',
    altitude: '200m',
    trekDistance: '7 km',
    difficultyLevel: 1,
    difficultyText: 'Nhẹ nhàng',
    isFeatured: false,
    shortSummary: 'Chiêm bái đại tự Bái Đính giữ nhiều kỷ lục châu Á, ngồi thuyền khám phá Di sản Thế giới Tràng An.',
    routeMap: 'Khởi hành từ Hà Nội theo Quốc lộ 1A về cố đô Hoa Lư (Ninh Bình). Buổi sáng tham quan quần thể chùa Bái Đính, đi dọc hành lang La Hán dài nhất châu Á, viếng Bảo Tháp và Điện Tam Thế. Buổi chiều xuôi thuyền chèo tay qua hệ thống hang động karst ngập nước kỳ ảo tại Tràng An.',
    routeSteps: ['Hà Nội', 'Ninh Bình (Cố đô Hoa Lư)', 'Chùa Bái Đính', 'Hành lang 500 vị La Hán', 'Bảo Tháp & Điện Tam Thế', 'Quần thể hang động Tràng An'],
    historyStory: 'Chùa Bái Đính cổ nằm trên sườn núi Đính có lịch sử nghìn năm từ thời Lý, là nơi thiền sư Nguyễn Minh Không lập am bốc thuốc cứu dân. Quần thể Bái Đính mới hiện nay là trung tâm Phật giáo nắm giữ hàng loạt kỷ lục châu Á: tượng Phật bằng đồng dát vàng lớn nhất, hành lang La Hán dài nhất và đại hồng chung nặng 36 tấn. Kết hợp cùng Quần thể danh thắng Tràng An – Di sản Văn hóa và Thiên nhiên Thế giới kép duy nhất tại Đông Nam Á.',
    description: 'Hành trình kết hợp tâm linh và khám phá Di sản Thiên nhiên Thế giới Tràng An với hàng trăm hang động đá vôi kỳ vĩ.',
    departureDates: ['26/10/2026', '09/11/2026', '23/11/2026'],
    highlights: [
      'Chiêm ngưỡng hành lang La Hán dài nhất châu Á với 500 pho tượng đá nguyên khối.',
      'Du thuyền xuyên qua các hang động karst tự nhiên kỳ ảo tại Tràng An.',
      'Thưởng thức đặc sản cơm cháy, dê núi Ninh Bình nức tiếng.'
    ],
    itinerary: [
      { day: '07:30', title: 'Hà Nội – Ninh Bình', desc: 'Xe đón đoàn khởi hành theo cao tốc Hà Nội – Ninh Bình.' },
      { day: '09:30', title: 'Vãn cảnh Đại Bi Tự Bái Đính', desc: 'Viếng Bảo Tháp, Điện Tam Thế, giếng Ngọc nghìn năm.' },
      { day: '12:30', title: 'Ăn trưa đặc sản dê núi', desc: 'Dùng bữa tại nhà hàng địa phương với các món ẩm thực Ninh Bình.' },
      { day: '14:00', title: 'Du ngoạn Tràng An', desc: 'Ngồi thuyền nan len lỏi qua hang Sáng, hang Tối, hang Ba Giọt.' },
      { day: '17:30', title: 'Về lại Hà Nội', desc: 'Khởi hành về đến thủ đô khoảng 19:30.' }
    ],
    included: ['Xe du lịch cao cấp', 'Vé thuyền Tràng An', 'Xe điện Bái Đính khứ hồi', 'Bữa trưa đặc sản địa phương', 'Hướng dẫn viên nhiệt tình'],
    preparation: ['Giày thể thao', 'Ô/dù che nắng mưa', 'Trang phục trang nhã']
  },

  // --- TOUR 9: SĂN MÂY Y TÝ ---
  {
    id: 9,
    title: 'Săn mây Y Tý – Thảo nguyên Choản Thèn',
    category: 'experience',
    subCategory: 'experience',
    categoryName: 'Trải nghiệm',
    duration: '2 ngày 1 đêm',
    location: 'Hà Nội – Bát Xát (Lào Cai)',
    price: '1.950.000đ/người',
    priceNum: 1950000,
    rating: 5.0,
    reviews: 43,
    image: 'assets/images/tour-y-ty.jpg',
    badge: 'Trải nghiệm',
    altitudeBadge: '☁️ 2.000m',
    altitude: '2.000m',
    trekDistance: '12 km',
    difficultyLevel: 3,
    difficultyText: 'Trung bình',
    isFeatured: false,
    shortSummary: 'Khám phá vùng đất mây mù biên viễn, check-in công viên Choản Thèn và ngắm nhà Trình Tường người Hà Nhì.',
    routeMap: 'Di chuyển từ Hà Nội lên thành phố Lào Cai, tiếp tục men theo cung đường đèo hiểm trở qua thung lũng Mường Hum lên xã vùng cao Y Tý (huyện Bát Xát). Khám phá bản cổ Choản Thèn, ngắm hoàng hôn Ngải Thầu Thượng và trekking săn biển mây dâng ngập thung lũng.',
    routeSteps: ['Hà Nội', 'Thành phố Lào Cai', 'Thung lũng Mường Hum', 'Xã Y Tý', 'Bản cổ Choản Thèn & Nhà Trình Tường', 'Đỉnh Ngải Thầu Thượng (2.100m)'],
    historyStory: 'Y Tý nằm ở độ cao trên 2.000m sát đường biên giới Việt – Trung, quanh năm chìm trong biển mây sương. Đây là địa bàn sinh sống của người Hà Nhì đen với kiến trúc nhà Trình Tường đất nện dày 40-50cm hình nấm độc đáo, ấm vào mùa đông và mát vào mùa hè. Bản cổ Choản Thèn có lịch sử hơn 300 năm vẫn giữ trọn phong tục lễ hội "Khô Già Già" tôn vinh mẹ thiên nhiên và thần rừng.',
    description: 'Hành trình đưa bạn đến vùng đất cổ tích Y Tý ngắm những ngôi nhà Trình Tường hình nấm độc đáo của người Hà Nhì giữa biển mây bồng bềnh.',
    departureDates: ['08/11/2026', '22/11/2026', '06/12/2026'],
    highlights: [
      'Đón biển mây tràn qua các thung lũng tại Ngải Thầu Thượng – điểm cao nhất Bát Xát.',
      'Check-in hai cây phong cô đơn tại công viên Choản Thèn lúc hoàng hôn buông xuống.',
      'Thưởng thức thịt lợn cắp nách nướng than và rượu Sim San thơm nồng.'
    ],
    itinerary: [
      { day: 'Ngày 1', title: 'Hà Nội – Lào Cai – Y Tý', desc: '06:00 khởi hành qua cao tốc Nội Bài – Lào Cai, vượt đèo Mường Hum lên Y Tý. Chiều khám phá bản Choản Thèn, ngắm hoàng hôn Ngải Thầu.' },
      { day: 'Ngày 2', title: 'Săn mây thung lũng Thề Pả – Hà Nội', desc: '05:30 đón bình minh biển mây thung lũng Thề Pả. Thăm chợ phiên vùng cao trước khi quay về Hà Nội lúc 20:00.' }
    ],
    included: ['Xe giường nằm hoặc limousine', 'Homestay nhà trình tường view mây', 'Các bữa ăn vùng cao', 'Hướng dẫn viên am hiểu phong tục bản địa', 'Bảo hiểm du lịch'],
    preparation: ['Áo khoác ấm nhiều lớp', 'Giày đi bộ', 'Thuốc men cá nhân']
  },

  // --- TOUR 10: MÙ CANG CHẢI ---
  {
    id: 10,
    title: 'Mù Cang Chải – Mùa Vàng Ruộng Bậc Thang',
    category: 'experience',
    subCategory: 'experience',
    categoryName: 'Trải nghiệm',
    duration: '3 ngày 2 đêm',
    location: 'Hà Nội – Yên Bái',
    price: '2.150.000đ/người',
    priceNum: 2150000,
    rating: 5.0,
    reviews: 78,
    image: 'assets/images/tour-mu-cang-chai.jpg',
    badge: 'Trải nghiệm',
    altitudeBadge: '🌾 Mùa vàng',
    altitude: '1.200m',
    trekDistance: '15 km',
    difficultyLevel: 2,
    difficultyText: 'Nhẹ - Vừa',
    isFeatured: false,
    shortSummary: 'Chiêm ngưỡng kiệt tác ruộng bậc thang Mâm Xôi, Móng Ngựa và vượt đèo Khau Phạ hùng vĩ bậc nhất Tây Bắc.',
    routeMap: 'Khởi hành từ Hà Nội qua thị xã Nghĩa Lộ, vượt đèo Khau Phạ (tứ đại đỉnh đèo Tây Bắc) vào huyện Mù Cang Chải. Trekking qua đồi Mâm Xôi La Pán Tẩn, Mâm Xôi Lớn, Móng Ngựa Sáng Nhù và bản làng người Mông Lìm Mông dưới chân đèo.',
    routeSteps: ['Hà Nội', 'Nghĩa Lộ', 'Đèo Khau Phạ (Tứ đại đỉnh đèo)', 'Đồi Mâm Xôi La Pán Tẩn', 'Vành Móng Ngựa Sáng Nhù', 'Bản Lìm Mông – Lìm Thái'],
    historyStory: 'Ruộng bậc thang Mù Cang Chải là Di tích Quốc gia Đặc biệt, được vinh danh là một trong những kiệt tác cảnh quan nhân tạo đẹp nhất hành tinh. Qua hàng trăm năm khai phá, đồng bào dân tộc Mông nơi đây đã biến những triền đồi dốc đứng thành các bậc thang uốn lượn kỳ vĩ để giữ nước gieo cấy lúa, thể hiện trí tuệ và sự hòa hợp tuyệt đối giữa con người với thiên nhiên đại ngàn.',
    description: 'Hành trình ngắm mùa lúa chín vàng óng ánh trên những nấc thang lên thiên đường tại La Pán Tẩn, Chế Cu Nha và đèo Khau Phạ.',
    departureDates: ['26/10/2026', '09/11/2026', '23/11/2026'],
    highlights: [
      'Ngắm trọn vẹn kiệt tác đồi Mâm Xôi và đồi Móng Ngựa rực vàng mùa lúa chín.',
      'Chinh phục đèo Khau Phạ – một trong tứ đại đỉnh đèo hùng vĩ của Việt Nam.',
      'Giao lưu văn hóa múa khèn và thưởng thức xôi nếp Tú Lệ dẻo thơm.'
    ],
    itinerary: [
      { day: 'Ngày 1', title: 'Hà Nội – Nghĩa Lộ – Khau Phạ', desc: 'Khởi hành qua đồi chè Thanh Sơn, thị xã Nghĩa Lộ. Vượt đèo Khau Phạ ngắm thung lũng Lìm Mông.' },
      { day: 'Ngày 2', title: 'Đồi Mâm Xôi – Vành Móng Ngựa', desc: 'Trekking qua những cung ruộng bậc thang vàng óng La Pán Tẩn, đón hoàng hôn Móng Ngựa.' },
      { day: 'Ngày 3', title: 'Tú Lệ – Suối Giàng – Hà Nội', desc: 'Mua nếp cốm Tú Lệ, thưởng thức trà San Tuyết cổ thụ Suối Giàng trước khi về thủ đô.' }
    ],
    included: ['Xe du lịch tiện nghi', 'Homestay người Thái sạch sẽ', 'Ăn uống đặc sản Tây Bắc', 'Bảo hiểm du lịch', 'Áo cờ đỏ sao vàng'],
    preparation: ['Trang phục chụp ảnh rực rỡ', 'Giày đi bộ thoải mái', 'Pin dự phòng máy ảnh']
  },

  // --- TOUR 11: CAO NGUYÊN ĐÁ HÀ GIANG ---
  {
    id: 11,
    title: 'Cao nguyên đá Đồng Văn – Hẻm Tu Sản',
    category: 'experience',
    subCategory: 'experience',
    categoryName: 'Trải nghiệm',
    duration: '3 ngày 2 đêm',
    location: 'Hà Nội – Hà Giang',
    price: '2.450.000đ/người',
    priceNum: 2450000,
    rating: 5.0,
    reviews: 115,
    image: 'assets/images/tour-ha-giang.jpg',
    badge: 'Trải nghiệm',
    altitudeBadge: '⛰️ Công viên đá',
    altitude: '1.600m',
    trekDistance: '18 km',
    difficultyLevel: 3,
    difficultyText: 'Trung bình',
    isFeatured: false,
    shortSummary: 'Chinh phục Mã Pí Lèng, đi thuyền ngắm vực Tu Sản sâu nhất Đông Nam Á trên dòng Nho Quế xanh ngọc.',
    routeMap: 'Khởi hành từ Hà Nội lên thành phố Hà Giang, qua Cổng trời Quản Bạ, dốc Thẩm Mã, dinh thự họ Vương tại Sà Phìn, cột cờ Quốc gia Lũng Cú, vượt đèo Mã Pí Lèng và chèo thuyền sông Nho Quế.',
    routeSteps: ['Hà Nội', 'Cổng trời Quản Bạ', 'Dinh Thự Vua Mèo', 'Cột cờ Lũng Cú (Cực Bắc)', 'Đèo Mã Pí Lèng', 'Hẻm vực Tu Sản (Sông Nho Quế)'],
    historyStory: 'Công viên Địa chất Toàn cầu UNESCO Cao nguyên đá Đồng Văn mang niên đại địa chất hàng trăm triệu năm với những dãy núi đá vôi xám tai mèo trùng điệp. Nơi đây là mảnh đất thiêng liêng địa đầu Tổ quốc gắn với con đường Hạnh Phúc huyền thoại được hàng vạn thanh niên xung phong đục đá mở đường trong những năm 1959-1965 để mang ánh sáng về cho đồng bào vùng biên.',
    description: 'Hành trình chạm đến địa đầu cực Bắc Tổ quốc, đứng trên đỉnh đèo Mã Pí Lèng ngắm dòng sông Nho Quế màu ngọc bích huyền thoại.',
    departureDates: ['01/11/2026', '15/11/2026', '29/11/2026'],
    highlights: [
      'Chạm tay vào lá cờ đỏ sao vàng 54m² tung bay kiêu hãnh trên đỉnh Lũng Cú.',
      'Đi thuyền ngắm hẻm vực Tu Sản sâu nhất Đông Nam Á trên sông Nho Quế.',
      'Khám phá kiến trúc dinh thự Vua Mèo Vương Chính Đức trăm năm tuổi.'
    ],
    itinerary: [
      { day: 'Ngày 1', title: 'Hà Nội – Quản Bạ – Yên Minh', desc: 'Vượt dốc Bắc Sum, check-in Cổng trời Quản Bạ, ngắm Núi Đôi cô tiên.' },
      { day: 'Ngày 2', title: 'Dinh Vua Mèo – Lũng Cú – Đồng Văn', desc: 'Viếng Dinh họ Vương, chạm mốc cực Bắc Lũng Cú, tối dạo phố cổ Đồng Văn.' },
      { day: 'Ngày 3', title: 'Mã Pí Lèng – Sông Nho Quế – Hà Nội', desc: 'Chinh phục Mã Pí Lèng, đi thuyền hẻm Tu Sản trước khi lên xe về Hà Nội.' }
    ],
    included: ['Xe giường nằm hoặc limousine', 'Khách sạn/homestay trung tâm', 'Vé thuyền sông Nho Quế', 'Các bữa ăn bản địa', 'Bảo hiểm du lịch'],
    preparation: ['Áo ấm', 'Giấy tờ tùy thân bắt buộc', 'Máy ảnh & thẻ nhớ']
  },

  // --- TOUR 12: THIỆN NGUYỆN VÙNG CAO ---
  {
    id: 12,
    title: 'Áo ấm cho em – Thiện nguyện Mù Cang Chải',
    category: 'charity',
    subCategory: 'charity',
    categoryName: 'Thiện nguyện',
    duration: '2 ngày 1 đêm',
    location: 'Hà Nội – Yên Bái',
    price: '1.250.000đ/người',
    priceNum: 1250000,
    rating: 5.0,
    reviews: 47,
    image: 'assets/images/tour-thien-nguyen.jpg',
    badge: 'Thiện nguyện',
    altitudeBadge: '❤️ Yêu thương',
    altitude: '1.400m',
    trekDistance: '10 km',
    difficultyLevel: 2,
    difficultyText: 'Nhẹ nhàng',
    isFeatured: false,
    shortSummary: 'Trao áo ấm, học bổng và nấu bữa cơm dinh dưỡng cho các em nhỏ điểm trường vùng cao xa xôi.',
    routeMap: 'Đoàn xuất phát từ Hà Nội lên điểm trường mầm non và tiểu học vùng khó khăn tại xã Chế Tạo hoặc Lao Chải (Mù Cang Chải). Trekking nhẹ mang quà vào bản, tổ chức chương trình giao lưu, nấu ăn và trao tặng đồ dùng học tập.',
    routeSteps: ['Hà Nội', 'Nghĩa Lộ', 'Thị trấn Mù Cang Chải', 'Trekking vào bản Chế Tạo', 'Điểm trường tiểu học vùng cao', 'Trao quà & Nấu cơm có thịt'],
    historyStory: 'Chương trình "Áo ấm cho em" do Trekking Đi Cùng Gió khởi xướng từ năm 2021 với mong muốn mỗi bước chân lữ hành đều gắn liền với trách nhiệm xã hội. Mùa đông trên non cao Tây Bắc nhiệt độ thường xuyên xuống dưới 5°C, những chiếc áo ấm và cuốn sách nhỏ trao tận tay các em là ngọn lửa sưởi ấm ước mơ đến trường của thế hệ mầm non vùng biên cương.',
    description: 'Hành trình kết nối yêu thương, mang chăn ấm, áo khoác mùa đông và tổ chức bữa cơm có thịt cho học sinh mầm non và tiểu học vùng cao.',
    departureDates: ['15/11/2026', '06/12/2026', '20/12/2026'],
    highlights: [
      'Trao tận tay 150 bộ áo ấm mùa đông và đồ dùng học tập cho học trò bản nghèo.',
      'Cùng các thành viên tự tay nấu bữa cơm dinh dưỡng "Có thịt" ấm áp cho các em nhỏ.',
      'Trekking nhẹ ngắm cảnh bản làng nguyên sơ và đồi thông xanh ngắt.'
    ],
    itinerary: [
      { day: 'Ngày 1', title: 'Hà Nội – Điểm trường Mù Cang Chải', desc: 'Di chuyển sớm lên điểm trường, cùng thầy cô dọn dẹp, chuẩn bị nguyên liệu nấu ăn tối cho học sinh nội trú.' },
      { day: 'Ngày 2', title: 'Trao quà thiện nguyện – Trở về Hà Nội', desc: '08:00 tổ chức ngày hội thiếu nhi, trao quà áo ấm, giao lưu trò chơi dân gian. Chiều đoàn khởi hành về lại Hà Nội lúc 21:00.' }
    ],
    included: ['Xe đưa đón tình nguyện viên', 'Chi phí ăn ở cùng bà con bản làng', 'Áo đồng phục tình nguyện viên', 'Bảo hiểm du lịch trọn gói'],
    preparation: ['Trái tim nhiệt huyết sẻ chia', 'Quần áo ấm cá nhân', 'Đồ dùng ủng hộ sạch đẹp']
  },

  // --- TOUR 13: XÂY TỦ SÁCH VÙNG CAO ---
  {
    id: 13,
    title: 'Xây tủ sách vùng cao – Nậm Có Yên Bái',
    category: 'charity',
    subCategory: 'charity',
    categoryName: 'Thiện nguyện',
    duration: '2 ngày 1 đêm',
    location: 'Hà Nội – Nậm Có',
    price: '1.200.000đ/người',
    priceNum: 1200000,
    rating: 4.9,
    reviews: 35,
    image: 'assets/images/tour-thien-nguyen.jpg',
    badge: 'Thiện nguyện',
    altitudeBadge: '📚 Tri thức',
    altitude: '1.100m',
    trekDistance: '8 km',
    difficultyLevel: 2,
    difficultyText: 'Nhẹ nhàng',
    isFeatured: false,
    shortSummary: 'Xây dựng thư viện xanh, tặng sách truyện và tổ chức lớp học kỹ năng sống cho trẻ em H’Mông.',
    routeMap: 'Từ Hà Nội lên huyện Mù Cang Chải, rẽ vào cung đường đồi đất hiểm trở xã Nậm Có. Đoàn cùng người dân sơn sửa phòng học, đóng kệ sách gỗ và sắp xếp 1.000 đầu sách cho các em nhỏ.',
    routeSteps: ['Hà Nội', 'Đèo Khau Phạ', 'Xã Nậm Có', 'Điểm trường bản Làng Nhì', 'Khánh thành Tủ sách xanh', 'Giao lưu cộng đồng bản H’Mông'],
    historyStory: 'Xã Nậm Có là một trong những xã vùng sâu vùng xa nhất của huyện Mù Cang Chải với 98% là đồng bào H’Mông. Dự án "Tủ sách vùng cao" ra đời nhằm đưa tri thức, sách truyện song ngữ và kỹ năng đọc đến với các em học sinh nghèo, mở ra cánh cửa nhìn ra thế giới rộng lớn.',
    description: 'Chung tay xây dựng không gian thư viện mở, trang bị hàng ngàn đầu sách truyện bổ ích cho các em nhỏ bản nghèo Nậm Có.',
    departureDates: ['22/11/2026', '13/12/2026'],
    highlights: [
      'Xây dựng thành công 02 tủ sách xanh với hơn 1.000 cuốn sách bổ ích.',
      'Tổ chức lớp vẽ tranh và kể chuyện tiếng Việt tương tác cùng học sinh.',
      'Trải nghiệm lối sống sinh hoạt mộc mạc bên gia đình người Mông.'
    ],
    itinerary: [
      { day: 'Ngày 1', title: 'Hà Nội – Nậm Có', desc: 'Vận chuyển sách vở lên điểm trường, lắp ráp tủ sách, trang trí thư viện cùng thầy cô.' },
      { day: 'Ngày 2', title: 'Khánh thành thư viện – Hà Nội', desc: 'Bàn giao tủ sách, hướng dẫn kỹ năng đọc sách, khởi hành về lại Hà Nội.' }
    ],
    included: ['Xe di chuyển khứ hồi', 'Ăn uống theo đoàn thiện nguyện', 'Bảo hiểm du lịch', 'Huy hiệu tình nguyện viên'],
    preparation: ['Sách truyện cũ còn dùng tốt', 'Bút màu & đồ dùng học tập quyên góp']
  },

  // --- TOUR 14: BA VÌ ---
  {
    id: 14,
    title: 'Trekking Rừng Quốc Gia Ba Vì',
    category: 'near_hanoi',
    subCategory: 'trekking',
    categoryName: 'Gần Hà Nội',
    duration: '1 ngày',
    location: 'Hà Nội – Ba Vì',
    price: '650.000đ/người',
    priceNum: 650000,
    rating: 4.8,
    reviews: 92,
    image: 'assets/images/tour-ba-vi.jpg',
    badge: 'Gần Hà Nội',
    altitudeBadge: '🌲 1.296m',
    altitude: '1.296m',
    trekDistance: '12 km',
    difficultyLevel: 2,
    difficultyText: 'Nhẹ - Trung bình',
    isFeatured: false,
    shortSummary: 'Trốn khói bụi thành phố, trekking rừng nguyên sinh sương mờ và chạm đỉnh Vua – Đền Thượng Ba Vì.',
    routeMap: 'Từ trung tâm Hà Nội di chuyển 50km về phía Tây đến Vườn Quốc Gia Ba Vì. Trekking xuyên rừng thông, rừng bách xanh cổ thụ, check-in nhà thờ đổ cổ kính thời Pháp và leo 1.300 bậc đá lên Đền Thượng trên đỉnh Vua.',
    routeSteps: ['Hà Nội', 'Cổng VQG Ba Vì', 'Rừng Thông Cốt 400', 'Nhà Thờ Đổ Cổ Kính', 'Rừng Bách Xanh Cổ Thụ', 'Đền Thượng Đỉnh Vua (1.296m)'],
    historyStory: 'Dãy núi Ba Vì (còn gọi là Tản Viên Sơn) là ngọn núi thiêng bậc nhất trong tâm thức người Việt, gắn liền với huyền tích Sơn Tinh – Thủy Tinh thời vua Hùng dựng nước. Vua Thánh Tản Viên là vị đệ nhất trong Tứ Bất Tử Việt Nam. Nơi đây từng là khu nghỉ dưỡng cao cấp thời Pháp thuộc với các tàn tích dinh thự và nhà thờ cổ phủ đầy rêu phong ẩn hiện giữa sương mù.',
    description: 'Tour leo núi trong ngày lý tưởng gần Hà Nội, hít thở không khí rừng thông trong lành, khám phá nhà thờ đổ cổ kính và viếng đền thờ Bác Hồ trên đỉnh Vua.',
    departureDates: ['26/10/2026', '01/11/2026', '08/11/2026', '15/11/2026'],
    highlights: [
      'Trekking rèn luyện thể lực qua những tán rừng bách xanh nghìn năm tuổi.',
      'Check-in nhà thờ đá cổ rêu phong ma mị huyền ảo trong màn sương mù.',
      'Viếng Đền Thượng thờ Đức Thánh Tản Viên và Đền thờ Bác Hồ trên đỉnh núi.'
    ],
    itinerary: [
      { day: '06:30', title: 'Hà Nội – Ba Vì', desc: 'Xe đón đoàn tại trung tâm thủ đô, khởi hành đi Vườn Quốc Gia Ba Vì.' },
      { day: '08:00', title: 'Trekking rừng thông & Nhà thờ cổ', desc: 'Bắt đầu cung đường leo núi xuyên rừng, chụp ảnh tại phế tích nhà thờ Pháp.' },
      { day: '11:30', title: 'Chinh phục Đỉnh Vua 1.296m', desc: 'Vượt dốc đá lên Đền Thượng, ăn trưa picnic giữa thiên nhiên mây ngàn.' },
      { day: '16:00', title: 'Trở về Hà Nội', desc: 'Xuống chân núi, ghé mua sữa tươi Ba Vì đặc sản, về tới Hà Nội lúc 18:00.' }
    ],
    included: ['Xe đưa đón đời mới', 'Vé tham quan VQG Ba Vì', 'Bữa trưa picnic chất lượng', 'Gậy trekking & nước uống', 'Leader hướng dẫn nhiệt tình'],
    preparation: ['Giày thể thao bám tốt', 'Áo khoác nhẹ', 'Bình nước cá nhân']
  },

  // --- TOUR 15: HÀM LỢN ---
  {
    id: 15,
    title: 'Chinh phục Đỉnh Hàm Lợn – Rừng Thông & Hồ Suối Bàu',
    category: 'near_hanoi',
    subCategory: 'trekking',
    categoryName: 'Gần Hà Nội',
    duration: '1 ngày',
    location: 'Hà Nội – Sóc Sơn',
    price: '490.000đ/người',
    priceNum: 490000,
    rating: 4.8,
    reviews: 84,
    image: 'assets/images/tour-ham-lon.jpg',
    badge: 'Gần Hà Nội',
    altitudeBadge: '🏕️ 462m',
    altitude: '462m',
    trekDistance: '10 km',
    difficultyLevel: 2,
    difficultyText: 'Nhẹ nhàng',
    isFeatured: false,
    shortSummary: 'Leo "nóc nhà Thủ đô", vượt suối đá và cắm trại chill bên hồ nước thơ mộng cách trung tâm 40km.',
    routeMap: 'Từ nội thành Hà Nội vượt cầu Nhật Tân đi Sóc Sơn (40km). Trekking men theo suối đá Núi Bàu hoặc leo dốc rừng thông lên đỉnh Hàm Lợn (462m). Buổi trưa hạ trại ăn thịt nướng bên bờ hồ Suối Bàu.',
    routeSteps: ['Hà Nội', 'Sóc Sơn', 'Hồ Suối Bàu', 'Cung đường suối đá Núi Bàu', 'Đỉnh Hàm Lợn (462m)', 'Cắm trại BBQ bờ hồ'],
    historyStory: 'Đỉnh Hàm Lợn (cao 462m) thuộc dãy núi Độc Tôn (Sóc Sơn), được giới leo núi mệnh danh là "Nóc nhà của Thủ đô Hà Nội". Nơi đây từ lâu là điểm rèn luyện thể lực và test thể lực chuẩn bị cho các cung trekking lớn Tây Bắc như Fansipan hay Kỳ Quan San của cộng đồng phượt thủ miền Bắc.',
    description: 'Cung leo núi dã ngoại cuối tuần cực vui vẻ, băng qua suối đá, rừng thông bạt ngàn và cắm trại thư giãn bên hồ Suối Bàu thơ mộng.',
    departureDates: ['26/10/2026', '02/11/2026', '09/11/2026', '16/11/2026'],
    highlights: [
      'Chinh phục nóc nhà thủ đô Hàm Lợn qua cung suối đá thử thách kỹ năng.',
      'Cắm trại picnic, nướng BBQ và thưởng thức cà phê chill bên bờ hồ Suối Bàu.',
      'Check-in rừng thông bạt ngàn ngỡ như Đà Lạt thu nhỏ giữa lòng Hà Nội.'
    ],
    itinerary: [
      { day: '07:00', title: 'Hà Nội – Sóc Sơn', desc: 'Tập trung tại điểm hẹn, di chuyển xe máy hoặc ô tô lên chân núi Hàm Lợn.' },
      { day: '08:30', title: 'Trekking cung suối đá', desc: 'Bắt đầu leo dốc suối đá gồ ghề, hỗ trợ nhau vượt qua các chướng ngại vật.' },
      { day: '11:00', title: 'Chạm đỉnh Hàm Lợn – Hồ Suối Bàu', desc: 'Check-in chóp đỉnh 462m, xuống hồ cắm trại ăn tiệc nướng BBQ.' },
      { day: '16:00', title: 'Dọn trại – Về Hà Nội', desc: 'Thu gom rác bảo vệ môi trường, khởi hành về lại trung tâm Hà Nội lúc 17:30.' }
    ],
    included: ['Lều trại dã ngoại xịn xò', 'Bữa tiệc BBQ thịt nướng thơm lừng', 'Đồ uống & than nướng', 'Leader hướng dẫn kỹ năng trekking an toàn'],
    preparation: ['Quần áo thể thao nhanh khô', 'Giày trekking lội suối bám đá', 'Kem chống muỗi']
  },

  // --- TOUR 16: NÚI TRẦM ---
  {
    id: 16,
    title: 'Trekking Núi Trầm – Cao Nguyên Đá Trắng Hà Nội',
    category: 'near_hanoi',
    subCategory: 'trekking',
    categoryName: 'Gần Hà Nội',
    duration: '1 ngày',
    location: 'Hà Nội – Chương Mỹ',
    price: '450.000đ/người',
    priceNum: 450000,
    rating: 4.7,
    reviews: 58,
    image: 'assets/images/tour-nui-tram.jpg',
    badge: 'Gần Hà Nội',
    altitudeBadge: '🪨 Đá trắng',
    altitude: '200m',
    trekDistance: '6 km',
    difficultyLevel: 1,
    difficultyText: 'Nhẹ nhàng',
    isFeatured: false,
    shortSummary: 'Khám phá mỏm đá trắng tựa Hà Giang thu nhỏ, dâng hương Chùa Trầm cổ kính nghìn năm tuổi.',
    routeMap: 'Từ Hà Nội theo hướng Hà Đông đi Chương Mỹ (25km). Trekking qua các mỏm núi đá vôi trắng Tử Trầm Sơn, thăm chùa Trầm, chùa Hang và ngắm trọn đồng quê ngoại thành thanh bình.',
    routeSteps: ['Hà Nội', 'Chương Mỹ', 'Chùa Trầm Cổ Tự', 'Chùa Hang (Động Long Tiên)', 'Mỏm Đá Trắng Tử Trầm Sơn', 'Check-in hoàng hôn đồng bằng'],
    historyStory: 'Tử Trầm Sơn (Núi Trầm) là một trong bốn ngọn núi danh thắng của xứ Đoài. Năm 1516, vua Lê Chiêu Tông đã cho xây hành cung tại đây. Nơi đây còn có Chùa Hang trong lòng động Long Tiên – nơi Đài Tiếng nói Việt Nam từng đặt trạm phát sóng lời kêu gọi Toàn quốc kháng chiến của Chủ tịch Hồ Chí Minh vào đêm 19/12/1946 lịch sử.',
    description: 'Chuyến trekking nhẹ nhàng khám phá "cao nguyên đá Hà Giang thu nhỏ" với những mỏm đá vôi trắng xóa nhô lên giữa cánh đồng xanh ngát.',
    departureDates: ['01/11/2026', '08/11/2026', '15/11/2026'],
    highlights: [
      'Leo lên các mỏm đá trắng tuyệt đẹp ngắm hoàng hôn đỏ rực buông xuống đồng lúa.',
      'Viếng Chùa Trầm cổ kính và chùa Hang linh thiêng mát rượi trong lòng núi.',
      'Thưởng thức bữa trưa dã ngoại nhẹ nhàng giữa thung lũng đá tĩnh mịch.'
    ],
    itinerary: [
      { day: '07:30', title: 'Hà Nội – Chương Mỹ', desc: 'Di chuyển 25km về phía Tây Nam thủ đô đến chân núi Trầm.' },
      { day: '09:00', title: 'Trekking các mỏm đá trắng Núi Trầm', desc: 'Chinh phục đỉnh núi đá ngắm toàn cảnh đồng quê bình yên.' },
      { day: '12:00', title: 'Picnic dã ngoại & Chùa Hang', desc: 'Ăn trưa nhẹ, vãn cảnh Chùa Hang với các bài thơ cổ khắc trên vách đá.' },
      { day: '15:30', title: 'Trở về Hà Nội', desc: 'Kết thúc chuyến đi nửa ngày nhiều niềm vui, về đến Hà Nội lúc 17:00.' }
    ],
    included: ['Xe đưa đón', 'Vé tham quan', 'Bữa trưa dã ngoại', 'Nước uống', 'Hướng dẫn viên nhiệt tình'],
    preparation: ['Giày có độ ma sát tốt', 'Mũ chống nắng', 'Trang phục thoải mái']
  }
];

// ==========================================
// 2. DEPARTURE SCHEDULE DATA (5 KEY TOURS)
// ==========================================
const DEPARTURE_SCHEDULE = [
  {
    id: 'sch-1',
    day: '26',
    month: 'Th10',
    title: 'Trekking Yên Tử – Chùa Đồng',
    duration: '1 ngày',
    price: '1.200.000đ',
    priceNum: 1200000,
    dateFull: '26/10/2026',
    status: 'Còn chỗ',
    tourId: 1
  },
  {
    id: 'sch-2',
    day: '01',
    month: 'Th11',
    title: 'Tà Xùa – Săn mây',
    duration: '2 ngày 1 đêm',
    price: '1.850.000đ',
    priceNum: 1850000,
    dateFull: '01/11/2026',
    status: 'Còn chỗ',
    tourId: 2
  },
  {
    id: 'sch-3',
    day: '08',
    month: 'Th11',
    title: 'Phu Sa Phin – Chinh phục đỉnh cao',
    duration: '2 ngày 1 đêm',
    price: '1.890.000đ',
    priceNum: 1890000,
    dateFull: '08/11/2026',
    status: 'Còn chỗ',
    tourId: 3
  },
  {
    id: 'sch-4',
    day: '15',
    month: 'Th11',
    title: 'Kỳ Quan San – Đỉnh núi hùng vĩ',
    duration: '3 ngày 2 đêm',
    price: '2.650.000đ',
    priceNum: 2650000,
    dateFull: '15/11/2026',
    status: 'Còn chỗ',
    tourId: 4
  },
  {
    id: 'sch-5',
    day: '22',
    month: 'Th11',
    title: 'Tà Chì Nhù – Mùa Hoa Chi Pâu',
    duration: '2 ngày 1 đêm',
    price: '1.850.000đ',
    priceNum: 1850000,
    dateFull: '22/11/2026',
    status: 'Còn chỗ',
    tourId: 5
  }
];

// ==========================================
// 3. REVIEWS & TESTIMONIALS DATA
// ==========================================
const TESTIMONIALS_DATA = [
  {
    id: 1,
    name: 'Nguyễn Thu Hà',
    role: 'Trekking Tà Xùa',
    avatar: 'assets/images/avatar-ha.jpg',
    comment: '“Cung đường sống lưng khủng long Tà Xùa đẹp nín thở, hướng dẫn viên nhiệt tình, đồ ăn bản địa ngon miệng. Cảm ơn Trekking Đi Cùng Gió đã cho mình một hành trình thật đáng nhớ!”',
    rating: 5
  },
  {
    id: 2,
    name: 'Lê Minh Đức',
    role: 'Trekking Phu Sa Phin',
    avatar: 'assets/images/avatar-duc.jpg',
    comment: '“Lần đầu đi trekking rừng rêu nguyên sinh Phu Sa Phin mà được trải nghiệm nhiều điều tuyệt vời như vậy. Porter gùi đồ khỏe, nhóm gắn kết. Chắc chắn sẽ quay lại cùng Đi Cùng Gió!”',
    rating: 5
  },
  {
    id: 3,
    name: 'Trần Thị Mai',
    role: 'Hành hương Yên Tử – Chùa Đồng',
    avatar: 'assets/images/avatar-mai.jpg',
    comment: '“Hành trình Yên Tử leo bộ 100% chạm đỉnh Chùa Đồng rất linh thiêng và ý nghĩa. Vừa rèn luyện thể lực vừa được lắng nghe những câu chuyện lịch sử sâu sắc về vua Trần Nhân Tông.”',
    rating: 5
  },
  {
    id: 4,
    name: 'Hoàng Quốc Bảo',
    role: 'Chinh phục Kỳ Quan San',
    avatar: 'assets/images/avatar-duc.jpg',
    comment: '“Đỉnh Kỳ Quan San 3.046m quá hùng vĩ! Biển mây đồi Muối lúc bình minh khiến mình nổi da gà vì quá đẹp. Đội ngũ Leader bọc lót các vách đá hiểm trở vô cùng an toàn và chuyên nghiệp.”',
    rating: 5
  },
  {
    id: 5,
    name: 'Đặng Thảo Linh',
    role: 'Tà Chì Nhù Mùa Hoa Chi Pâu',
    avatar: 'assets/images/avatar-ha.jpg',
    comment: '“Được đắm mình trong sắc tím bạt ngàn của hoa Chi Pâu trên thảo nguyên 2.400m Tà Chì Nhù là một trong những trải nghiệm kỳ diệu nhất tuổi thanh xuân của mình!”',
    rating: 5
  }
];

// ==========================================
// 4. APP STATE
// ==========================================
let currentCategory = 'all';
let currentHeroSlide = 0;
let heroSlideTimer = null;
let currentBookingTour = null;
let bookingGuests = 1;

// Wishlist storage
let wishlist = new Set();
try {
  const saved = localStorage.getItem('dicunggio_wishlist');
  if (saved) {
    wishlist = new Set(JSON.parse(saved));
  }
} catch (e) {
  console.warn('LocalStorage not available', e);
}

// ==========================================
// 5. INITIALIZATION ON DOM READY
// ==========================================
document.addEventListener('DOMContentLoaded', () => {
  initHeroSlider();
  renderTours();
  renderSchedule();
  setupCategoryFilter();
  updateWishlistBadges();
  setupBookingModalEvents();
  setupMobileNav();
  setupFloatingActions();
  setupScrollReveal();
  setupScrollSpy();
  setupNavbarGlass();
  setupNewsletterForm();
  initLucideIcons();
});

// Helper to safely re-init Lucide icons
function initLucideIcons() {
  if (window.lucide && typeof window.lucide.createIcons === 'function') {
    window.lucide.createIcons();
  }
}

// Format number to VND
function formatCurrency(num) {
  return new Intl.NumberFormat('vi-VN').format(num) + 'đ';
}

// ==========================================
// 6. HERO MULTI-SLIDE CONTROLLER (KEN BURNS)
// ==========================================
function initHeroSlider() {
  const slides = document.querySelectorAll('.hero-slide');
  const dots = document.querySelectorAll('.hero-dot');
  if (!slides.length) return;

  window.setHeroSlide = function(index) {
    currentHeroSlide = (index + slides.length) % slides.length;
    
    slides.forEach((slide, i) => {
      if (i === currentHeroSlide) {
        slide.classList.add('active');
      } else {
        slide.classList.remove('active');
      }
    });

    dots.forEach((dot, i) => {
      if (i === currentHeroSlide) {
        dot.classList.add('w-8', 'bg-white');
        dot.classList.remove('w-2.5', 'bg-white/50');
      } else {
        dot.classList.remove('w-8', 'bg-white');
        dot.classList.add('w-2.5', 'bg-white/50');
      }
    });
  };

  window.nextHeroSlide = function() {
    setHeroSlide(currentHeroSlide + 1);
  };

  window.prevHeroSlide = function() {
    setHeroSlide(currentHeroSlide - 1);
  };

  // Autoplay every 6 seconds
  const startAutoplay = () => {
    clearInterval(heroSlideTimer);
    heroSlideTimer = setInterval(() => {
      nextHeroSlide();
    }, 6000);
  };

  startAutoplay();

  const heroSec = document.getElementById('home');
  heroSec?.addEventListener('mouseenter', () => clearInterval(heroSlideTimer));
  heroSec?.addEventListener('mouseleave', () => startAutoplay());
}

// ==========================================
// 7. RENDER TOURS (LEFT COLUMN 72%)
// ==========================================
function renderTours(filterCategory = currentCategory) {
  const container = document.getElementById('tour-grid-container');
  if (!container) return;

  currentCategory = filterCategory;
  let filtered = [];

  if (filterCategory === 'all') {
    // Show 4 primary featured tours by default
    filtered = TOURS_DATA.filter(t => t.isFeatured);
  } else {
    // Show tours matching the chosen category
    filtered = TOURS_DATA.filter(t => t.category === filterCategory || t.subCategory === filterCategory);
  }

  // Fallback if empty
  if (filtered.length === 0) {
    filtered = TOURS_DATA.slice(0, 4);
  } else if (filtered.length > 4) {
    filtered = filtered.slice(0, 4);
  }

  container.innerHTML = filtered.map(tour => {
    const isLiked = wishlist.has(tour.id);
    return `
      <div class="tour-card bg-white rounded-2xl overflow-hidden border border-gray-100 shadow-sm hover:shadow-md transition-all duration-300 flex flex-col justify-between group">
        
        <!-- Tour Image Container (Zoom on hover + Storytelling overlay) -->
        <div class="relative overflow-hidden aspect-[4/3] bg-gray-100 cursor-pointer" onclick="openTourDetailModal(${tour.id})">
          <img 
            src="${tour.image}" 
            alt="${tour.title}" 
            loading="lazy"
            onerror="this.onerror=null; this.src='assets/images/tour-yen-tu.jpg';"
            class="tour-card-image w-full h-full object-cover transition-transform duration-500 group-hover:scale-108"
          />
          
          <!-- Category Badge (Top Left with Glassmorphism) -->
          <div class="absolute top-3 left-3 z-10">
            <span class="backdrop-blur-md bg-[#1E4D3B]/90 text-white text-[11px] font-bold px-2.5 py-1 rounded-full shadow-sm">
              ${tour.badge}
            </span>
          </div>

          <!-- Subtle Altitude Badge (Top Center/Left) -->
          <div class="absolute top-3 left-24 z-10">
            <span class="backdrop-blur-md bg-black/45 text-white text-[10px] font-semibold px-2 py-0.5 rounded-md shadow-sm">
              ${tour.altitudeBadge}
            </span>
          </div>

          <!-- Real Photo indicator if available -->
          ${tour.gallery && tour.gallery.length > 0 ? `
            <div class="absolute bottom-2.5 left-2.5 z-10">
              <span class="backdrop-blur-md bg-black/60 text-emerald-300 text-[10px] font-bold px-2 py-0.5 rounded-full shadow-sm flex items-center gap-1">
                <i data-lucide="camera" class="w-3 h-3 text-emerald-300"></i>
                <span>${tour.gallery.length} ảnh thực tế</span>
              </span>
            </div>
          ` : ''}

          <!-- Hover Overlay with Frosted Glass Storytelling Hint -->
          <div class="absolute inset-0 backdrop-blur-[2px] bg-black/45 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex flex-col items-center justify-center p-3 text-center pointer-events-none">
            <span class="px-3.5 py-1.5 rounded-full bg-white text-forest text-xs font-bold shadow-lg transform translate-y-2 group-hover:translate-y-0 transition-transform duration-300 flex items-center gap-1.5">
              <i data-lucide="compass" class="w-3.5 h-3.5 text-forest"></i>
              <span>Xem chi tiết</span>
            </span>
            <p class="text-[11px] text-white/95 font-medium mt-2 drop-shadow-sm px-2 leading-snug">
              📍 Lộ trình & Lịch sử vùng đất → Bấm để khám phá
            </p>
          </div>

          <!-- Wishlist Heart Button (Top Right with Glassmorphism) -->
          <button 
            type="button" 
            onclick="toggleWishlist(${tour.id}, event)" 
            title="${isLiked ? 'Bỏ yêu thích' : 'Lưu tour yêu thích'}"
            class="heart-btn absolute top-3 right-3 z-20 w-8 h-8 rounded-full bg-white/80 backdrop-blur-md flex items-center justify-center text-gray-700 hover:text-red-500 hover:bg-white transition-all shadow-sm ${isLiked ? 'active' : ''}"
          >
            <i data-lucide="heart" class="w-4 h-4 transition-colors ${isLiked ? 'fill-red-500 text-red-500' : ''}"></i>
          </button>
        </div>

        <!-- Tour Body Content -->
        <div class="p-4 flex flex-col flex-1 justify-between">
          <div>
            <!-- Compact Meta Details above title with Book Story Link -->
            <div class="flex items-center justify-between text-[11px] text-gray-500 mb-1.5">
              <span class="flex items-center gap-1">
                <i data-lucide="map-pin" class="w-3 h-3 text-forest shrink-0"></i>
                <span class="truncate max-w-[125px]">${tour.location}</span>
              </span>
              <button 
                type="button" 
                onclick="openTourDetailModal(${tour.id}, 2); event.stopPropagation();" 
                class="inline-flex items-center gap-1 text-[11px] font-semibold text-forest hover:text-forest-dark hover:underline cursor-pointer"
                title="Xem lịch sử & câu chuyện địa danh"
              >
                <i data-lucide="book-open" class="w-3 h-3 text-forest"></i>
                <span>Câu chuyện</span>
              </button>
            </div>

            <!-- Title: 2 lines with consistent height, fully readable -->
            <h3 
              class="font-bold text-gray-900 text-[13.5px] xl:text-[14px] leading-snug line-clamp-2 min-h-[38px] tracking-tight group-hover:text-forest transition-colors cursor-pointer" 
              onclick="openTourDetailModal(${tour.id})" 
              title="${tour.title}"
            >
              ${tour.title}
            </h3>

            <!-- 1-line Short Summary Description -->
            <p class="text-xs text-gray-600 line-clamp-2 mt-1 mb-2 leading-relaxed">
              ${tour.shortSummary || tour.description}
            </p>

            <!-- Price & Duration -->
            <div class="flex items-baseline justify-between mt-1">
              <span class="text-[15px] font-black text-forest whitespace-nowrap">${tour.price}</span>
              <span class="text-[11px] text-gray-500 font-medium">${tour.duration}</span>
            </div>
          </div>

          <!-- Bottom: Rating & Direct Book Button (1 row) -->
          <div class="mt-3 pt-3 border-t border-gray-100 flex items-center justify-between gap-1">
            <div class="flex items-center gap-1 shrink-0">
              <div class="flex text-amber-400">
                <i data-lucide="star" class="w-3 h-3 fill-amber-400 text-amber-400"></i>
                <i data-lucide="star" class="w-3 h-3 fill-amber-400 text-amber-400"></i>
                <i data-lucide="star" class="w-3 h-3 fill-amber-400 text-amber-400"></i>
                <i data-lucide="star" class="w-3 h-3 fill-amber-400 text-amber-400"></i>
                <i data-lucide="star" class="w-3 h-3 fill-amber-400 text-amber-400"></i>
              </div>
              <span class="text-[11px] text-gray-400 font-medium">(${tour.reviews})</span>
            </div>

            <button 
              type="button" 
              onclick="openSmartBookingModal(${tour.id}); event.stopPropagation();"
              class="btn-shine whitespace-nowrap px-3.5 py-1.5 rounded-lg bg-[#1E4D3B] text-white text-xs font-semibold shrink-0 hover:bg-forest/90 active:scale-95 transition-all shadow-sm cursor-pointer"
            >
              Đăng ký ngay
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

  container.innerHTML = DEPARTURE_SCHEDULE.map(item => `
    <div 
      onclick="openTourDetailModal(${item.tourId})"
      class="schedule-row p-3 rounded-xl bg-gray-50/70 border border-gray-100/80 flex items-center justify-between gap-3 cursor-pointer group"
      title="Nhấn để xem lộ trình & đăng ký tour này"
    >
      <!-- Date Block -->
      <div class="flex items-center gap-2.5 shrink-0">
        <div class="w-11 h-11 rounded-xl bg-[#1E4D3B] text-white flex flex-col items-center justify-center shadow-xs group-hover:scale-105 transition-transform">
          <span class="text-sm font-black leading-none">${item.day}</span>
          <span class="text-[9px] font-bold uppercase tracking-wider text-emerald-200 mt-0.5">${item.month}</span>
        </div>

        <div class="min-w-0">
          <h4 class="text-xs font-bold text-gray-900 group-hover:text-forest transition-colors truncate">
            ${item.title}
          </h4>
          <span class="text-[11px] text-gray-500 font-medium">${item.duration}</span>
        </div>
      </div>

      <!-- Price & Status Badge -->
      <div class="text-right shrink-0">
        <span class="block text-xs font-extrabold text-forest">${item.price}</span>
        <span class="badge-seat text-[10px] inline-block mt-0.5">${item.status}</span>
      </div>
    </div>
  `).join('');

  initLucideIcons();
}

// ==========================================
// 9. CATEGORY BAR FILTERING CONTROLLER
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
    }, 150);
  }
}

// ==========================================
// 10. PROFESSIONAL STORYTELLING MODAL CONTROLLER
// ==========================================
function openTourDetailModal(tourId, initialTab = 1) {
  const tour = TOURS_DATA.find(t => t.id === tourId) || TOURS_DATA[0];
  if (!tour) return;

  const modal = document.getElementById('tour-detail-modal');
  const content = document.getElementById('tour-detail-content');
  if (!modal || !content) return;

  const isLiked = wishlist.has(tour.id);
  const dates = tour.departureDates ? tour.departureDates.join(', ') : 'Thứ 6 hàng tuần';

  // Render 1-5 difficulty dots
  let diffDots = '';
  for (let i = 1; i <= 5; i++) {
    diffDots += `<span class="difficulty-dot ${i <= tour.difficultyLevel ? 'active' : ''}"></span>`;
  }

  content.innerHTML = `
    <div class="relative bg-white rounded-3xl overflow-hidden shadow-2xl max-w-3xl w-full border border-gray-100 modal-enter max-h-[92vh] flex flex-col">
      
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
          class="absolute top-4 right-4 z-20 w-9 h-9 rounded-full bg-black/50 text-white hover:bg-black/80 flex items-center justify-center transition-colors backdrop-blur-sm cursor-pointer"
          title="Đóng"
        >
          <i data-lucide="x" class="w-5 h-5"></i>
        </button>

        <!-- Banner Text & Badges -->
        <div class="absolute bottom-4 left-5 right-5 text-white">
          <div class="flex flex-wrap items-center gap-2 mb-2">
            <span class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-[#1E4D3B] text-white">${tour.badge}</span>
            <span class="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-white/20 backdrop-blur-sm text-white">${tour.altitudeBadge}</span>
            <span class="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-white/20 backdrop-blur-sm text-white">${tour.duration}</span>
          </div>
          <h2 class="text-xl sm:text-2xl font-black leading-tight drop-shadow-sm">${tour.title}</h2>
          <p class="text-xs sm:text-sm text-emerald-200 mt-1 flex items-center gap-2">
            <i data-lucide="map-pin" class="w-3.5 h-3.5 text-emerald-300"></i>
            <span>${tour.location}</span>
          </p>
        </div>
      </div>

      <!-- Trekking Key Specs Bar -->
      <div class="grid grid-cols-4 gap-2 px-5 py-3 bg-[#F6F7F2] border-b border-gray-100 text-center shrink-0">
        <div>
          <span class="block text-[10px] font-bold uppercase tracking-wider text-gray-500">Độ cao đỉnh</span>
          <span class="block text-xs sm:text-sm font-extrabold text-forest mt-0.5">${tour.altitude}</span>
        </div>
        <div class="border-l border-gray-200">
          <span class="block text-[10px] font-bold uppercase tracking-wider text-gray-500">Quãng đường</span>
          <span class="block text-xs sm:text-sm font-extrabold text-gray-900 mt-0.5">${tour.trekDistance}</span>
        </div>
        <div class="border-l border-gray-200">
          <span class="block text-[10px] font-bold uppercase tracking-wider text-gray-500">Độ khó (${tour.difficultyLevel}/5)</span>
          <div class="difficulty-meter mt-1 justify-center">
            ${diffDots}
          </div>
        </div>
        <div class="border-l border-gray-200">
          <span class="block text-[10px] font-bold uppercase tracking-wider text-gray-500">Khởi hành</span>
          <span class="block text-xs sm:text-sm font-extrabold text-gray-900 mt-0.5">Hà Nội</span>
        </div>
      </div>

      <!-- Storytelling Tabs Navigation -->
      <div class="flex items-center gap-6 px-5 sm:px-6 pt-3 border-b border-gray-100 bg-white text-xs sm:text-sm shrink-0">
        <button 
          id="tab-btn-1" 
          onclick="switchDetailTab(1)"
          class="modal-tab-btn active cursor-pointer flex items-center gap-1.5"
        >
          <i data-lucide="navigation" class="w-3.5 h-3.5"></i>
          <span>1. Hành trình & Lộ trình</span>
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
          <i data-lucide="backpack" class="w-3.5 h-3.5"></i>
          <span>3. Lịch trình & Chuẩn bị</span>
        </button>
      </div>

      <!-- Tab Content Panels (Scrollable) -->
      <div class="p-5 sm:p-6 overflow-y-auto flex-1 space-y-4 text-xs sm:text-sm text-gray-700 leading-relaxed">
        
        <!-- PANEL 1: Hành trình đi đâu & Lộ trình địa lý -->
        <div id="tab-panel-1" class="space-y-4">
          <!-- Visual Route Steps -->
          <div class="space-y-2">
            <h4 class="text-xs font-bold uppercase tracking-wider text-forest flex items-center gap-1.5">
              <i data-lucide="map-pin" class="w-4 h-4 text-forest"></i>
              <span>Sơ đồ các chặng hành trình (Visual Route Steps)</span>
            </h4>
            <div class="flex flex-wrap items-center gap-1.5 sm:gap-2 p-3 bg-emerald-50/70 rounded-2xl border border-emerald-100">
              ${(tour.routeSteps || []).map((step, idx, arr) => `
                <span class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-white border border-emerald-200 text-forest font-bold text-xs shadow-2xs">
                  <span class="w-4 h-4 rounded-full bg-forest text-white text-[10px] flex items-center justify-center font-extrabold shrink-0">${idx + 1}</span>
                  <span>${step}</span>
                </span>
                ${idx < arr.length - 1 ? '<i data-lucide="chevron-right" class="w-3.5 h-3.5 text-emerald-600 shrink-0"></i>' : ''}
              `).join('')}
            </div>
          </div>

          <!-- Geographic Itinerary Description -->
          <div class="space-y-1.5">
            <h4 class="text-xs font-bold uppercase tracking-wider text-gray-800 flex items-center gap-1.5">
              <i data-lucide="map" class="w-4 h-4 text-forest"></i>
              <span>Hành trình đi đâu (Lộ trình địa lý)</span>
            </h4>
            <p class="text-xs sm:text-sm text-gray-700 leading-relaxed bg-gray-50 p-3.5 rounded-xl border border-gray-100 font-normal">
              ${tour.routeMap || tour.description}
            </p>
          </div>
          
          <!-- Highlights -->
          <div class="space-y-2.5 pt-1">
            <h4 class="text-xs font-bold uppercase tracking-wider text-forest">Trải nghiệm độc bản không thể bỏ lỡ</h4>
            <ul class="space-y-2">
              ${(tour.highlights || []).map(hl => `
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

          <div class="p-3 bg-emerald-50/70 rounded-xl border border-emerald-100 flex items-center justify-between">
            <div>
              <span class="text-xs font-bold text-forest block">Lịch khởi hành sắp tới:</span>
              <span class="text-xs text-gray-600 font-medium">${dates}</span>
            </div>
            <span class="badge-seat text-xs font-bold">Còn chỗ</span>
          </div>
        </div>

        <!-- PANEL 2: Lịch sử & Câu chuyện vùng đất -->
        <div id="tab-panel-2" class="hidden space-y-4">
          <div class="bg-[#F6F7F2] border-l-4 border-[#1E4D3B] p-5 rounded-r-2xl shadow-xs space-y-3.5">
            <div class="flex items-center gap-2 text-forest">
              <i data-lucide="landmark" class="w-5 h-5 text-forest"></i>
              <h4 class="font-extrabold text-sm sm:text-base text-gray-900">
                Lịch sử & Huyền thoại ngọn núi ${tour.title}
              </h4>
            </div>
            
            <p class="text-xs sm:text-sm text-gray-700 leading-relaxed font-normal">
              ${tour.historyStory || tour.description}
            </p>

            <div class="pt-3 text-[11px] text-gray-500 italic border-t border-stone-200/70 flex items-center gap-2">
              <i data-lucide="sparkles" class="w-4 h-4 text-amber-500 shrink-0"></i>
              <span>Mỗi hành trình của Trekking Đi Cùng Gió không chỉ là thể lực, mà là một trải nghiệm chạm vào chiều sâu văn hóa và lịch sử đất nước.</span>
            </div>
          </div>

          <div class="p-4 bg-emerald-50/50 rounded-2xl border border-emerald-100 space-y-2 text-xs">
            <h5 class="font-bold text-forest flex items-center gap-1.5">
              <i data-lucide="info" class="w-4 h-4"></i>
              <span>Góc nhìn văn hóa bản địa</span>
            </h5>
            <p class="text-gray-600 leading-relaxed">
              Các Porter và Hướng dẫn viên của Trekking Đi Cùng Gió đều là người dân bản địa (H’Mông, Dao, Tày...), am hiểu từng gốc cây ngọn cỏ, dòng suối và những phong tục truyền thống của đại ngàn.
            </p>
          </div>
        </div>

        <!-- PANEL 3: Lịch trình chi tiết & Chuẩn bị -->
        <div id="tab-panel-3" class="hidden space-y-5">
          <div>
            <h4 class="text-xs font-bold uppercase tracking-wider text-forest mb-3">Lịch trình chi tiết từng ngày</h4>
            <div class="relative border-l-2 border-emerald-600/30 ml-3 pl-5 space-y-5">
              ${(tour.itinerary || []).map((step, idx) => `
                <div class="relative">
                  <span class="absolute -left-[27px] top-0 w-3.5 h-3.5 rounded-full bg-forest ring-4 ring-emerald-100"></span>
                  <span class="inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-[#1E4D3B]/10 text-forest mb-1">${step.day}</span>
                  <h5 class="text-xs sm:text-sm font-bold text-gray-900">${step.title}</h5>
                  <p class="text-xs text-gray-600 mt-1 leading-relaxed">${step.desc}</p>
                </div>
              `).join('')}
            </div>
          </div>

          <div class="pt-2 border-t border-gray-100 space-y-3">
            <div>
              <h4 class="text-xs font-bold uppercase tracking-wider text-forest mb-2">Trekking Đi Cùng Gió đã chuẩn bị chu đáo cho bạn</h4>
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs text-gray-600">
                ${(tour.included || []).map(inc => `
                  <span class="flex items-center gap-1.5"><i data-lucide="check" class="w-3.5 h-3.5 text-forest"></i> ${inc}</span>
                `).join('')}
              </div>
            </div>

            <div class="pt-3 border-t border-gray-100">
              <h4 class="text-xs font-bold uppercase tracking-wider text-amber-700 mb-2">Đồ dùng cá nhân bạn cần mang theo</h4>
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs text-gray-600">
                ${(tour.preparation || []).map(prep => `
                  <span class="flex items-center gap-1.5"><i data-lucide="arrow-right" class="w-3.5 h-3.5 text-amber-600"></i> ${prep}</span>
                `).join('')}
              </div>
            </div>
          </div>
        </div>

      </div>

      <!-- Footer Action Bar -->
      <div class="p-4 sm:p-5 border-t border-gray-100 bg-gray-50/80 flex items-center justify-between gap-4 shrink-0">
        <div>
          <span class="block text-[11px] text-gray-500">Giá tour trọn gói</span>
          <span class="block text-base sm:text-lg font-black text-forest leading-tight">${tour.price}</span>
        </div>

        <div class="flex items-center gap-3">
          <button 
            type="button"
            onclick="toggleWishlist(${tour.id}); openTourDetailModal(${tour.id});" 
            class="p-2.5 rounded-full border border-gray-200 bg-white text-gray-600 hover:text-red-500 hover:border-red-200 transition-colors shrink-0 shadow-sm cursor-pointer"
            title="Lưu yêu thích"
          >
            <i data-lucide="heart" class="w-5 h-5 ${isLiked ? 'fill-red-500 text-red-500' : ''}"></i>
          </button>

          <button 
            type="button"
            onclick="closeTourDetailModal(); openSmartBookingModal(${tour.id});" 
            class="btn-shine py-2.5 px-6 rounded-full bg-forest text-white font-bold text-xs sm:text-sm hover:bg-forest/90 active:scale-95 transition-all shadow-md flex items-center gap-2 cursor-pointer"
          >
            <span>Đăng ký chinh phục ngay</span>
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

// Switch tabs inside detail modal
window.switchDetailTab = function(tabIndex) {
  for (let i = 1; i <= 3; i++) {
    const btn = document.getElementById(`tab-btn-${i}`);
    const panel = document.getElementById(`tab-panel-${i}`);
    if (i === tabIndex) {
      btn?.classList.add('active');
      panel?.classList.remove('hidden');
    } else {
      btn?.classList.remove('active');
      panel?.classList.add('hidden');
    }
  }
  initLucideIcons();
};

// ==========================================
// 11. SMART BOOKING MODAL WITH LIVE CALCULATOR
// ==========================================
function openSmartBookingModal(tourId = 1, defaultDate = '') {
  currentBookingTour = TOURS_DATA.find(t => t.id === tourId) || TOURS_DATA[0];
  bookingGuests = 1;

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
        ${t.title} – ${t.price} (${t.duration})
      </option>
    `).join('');
    
    select.onchange = (e) => {
      const selectedId = parseInt(e.target.value, 10);
      currentBookingTour = TOURS_DATA.find(t => t.id === selectedId) || TOURS_DATA[0];
      updateBookingCalculation();
    };
  }

  // Pre-fill date
  if (dateInput) {
    if (defaultDate) {
      dateInput.value = defaultDate;
    } else if (currentBookingTour.departureDates && currentBookingTour.departureDates.length > 0) {
      dateInput.value = currentBookingTour.departureDates[0];
    } else {
      dateInput.value = 'Thứ 6 tuần tới';
    }
  }

  // Reset form and show
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
        <span>Đơn giá (${bookingGuests} người):</span>
        <span class="font-bold text-gray-900">${formatCurrency(priceEach)} × ${bookingGuests} = ${formatCurrency(subtotal)}</span>
      </div>
      ${isGroupDiscount ? `
        <div class="flex justify-between items-center text-emerald-700 font-bold">
          <span>Ưu đãi nhóm (≥4 khách giảm 5%):</span>
          <span>- ${formatCurrency(discountAmount)}</span>
        </div>
      ` : `
        <div class="text-[11px] text-gray-500 italic">
          💡 Đặt từ 4 người trở lên được giảm thêm 5% tổng hoá đơn.
        </div>
      `}
      <div class="pt-2 border-t border-emerald-200/80 flex justify-between items-center">
        <span class="font-bold text-gray-800 text-xs sm:text-sm">Tổng thanh toán dự kiến:</span>
        <span class="font-black text-forest text-base sm:text-lg">${formatCurrency(finalTotal)}</span>
      </div>
    </div>
  `;
}

// Booking Form Submit Event
function setupBookingModalEvents() {
  const form = document.getElementById('booking-form');
  if (!form) return;

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const name = document.getElementById('booking-name')?.value.trim();
    const phone = document.getElementById('booking-phone')?.value.trim();
    const date = document.getElementById('booking-date-input')?.value.trim();

    // Validation
    if (!name || name.length < 2) {
      showToast('Thông tin chưa hợp lệ', 'Vui lòng nhập họ và tên đầy đủ của bạn.', 'error');
      return;
    }

    // Phone validation regex for Vietnam (10 digits starting with 03, 05, 07, 08, 09)
    const phoneRegex = /^(0[3|5|7|8|9])[0-9]{8}$/;
    if (!phoneRegex.test(phone)) {
      showToast('Số điện thoại không hợp lệ', 'Vui lòng nhập số điện thoại Việt Nam gồm 10 chữ số (VD: 0965983302).', 'error');
      return;
    }

    // Generate random booking code e.g. #DCG-202689
    const randomCode = '#DCG-' + Math.floor(100000 + Math.random() * 900000);
    const subtotal = currentBookingTour.priceNum * bookingGuests;
    const isGroupDiscount = bookingGuests >= 4;
    const finalTotal = isGroupDiscount ? subtotal * 0.95 : subtotal;

    // Show Confirmation screen
    const formBox = document.getElementById('booking-form-box');
    const successBox = document.getElementById('booking-success-box');
    
    if (formBox && successBox) {
      formBox.classList.add('hidden');
      successBox.classList.remove('hidden');

      successBox.innerHTML = `
        <div class="text-center py-4 space-y-4">
          <div class="w-16 h-16 rounded-full bg-emerald-100 text-forest flex items-center justify-center mx-auto ring-8 ring-emerald-50">
            <i data-lucide="check" class="w-8 h-8 stroke-[3]"></i>
          </div>

          <div>
            <span class="inline-block px-3 py-1 rounded-full text-xs font-black bg-[#1E4D3B] text-white tracking-wider">
              ${randomCode}
            </span>
            <h3 class="text-xl font-black text-gray-900 mt-2">Đăng ký tour thành công!</h3>
            <p class="text-xs text-gray-600 mt-1">Cảm ơn bạn đã lựa chọn đồng hành cùng Trekking Đi Cùng Gió.</p>
          </div>

          <!-- Receipt card -->
          <div class="p-4 bg-gray-50 rounded-2xl border border-gray-200 text-left space-y-2 text-xs">
            <div class="flex justify-between py-1 border-b border-gray-200/60">
              <span class="text-gray-500">Khách hàng:</span>
              <span class="font-bold text-gray-900">${name} (${phone})</span>
            </div>
            <div class="flex justify-between py-1 border-b border-gray-200/60">
              <span class="text-gray-500">Hành trình:</span>
              <span class="font-bold text-forest">${currentBookingTour.title}</span>
            </div>
            <div class="flex justify-between py-1 border-b border-gray-200/60">
              <span class="text-gray-500">Ngày khởi hành:</span>
              <span class="font-bold text-gray-900">${date}</span>
            </div>
            <div class="flex justify-between py-1 border-b border-gray-200/60">
              <span class="text-gray-500">Số lượng khách:</span>
              <span class="font-bold text-gray-900">${bookingGuests} người ${isGroupDiscount ? '(Đã giảm 5%)' : ''}</span>
            </div>
            <div class="flex justify-between pt-1">
              <span class="text-gray-700 font-bold">Tổng thanh toán dự kiến:</span>
              <span class="font-black text-sm text-forest">${formatCurrency(finalTotal)}</span>
            </div>
          </div>

          <p class="text-[11px] text-gray-500 leading-relaxed">
            📞 Tư vấn viên sẽ liên hệ qua hotline <strong>0965 983 302</strong> / Zalo trong vòng <strong>15 phút</strong> để gửi lịch trình chi tiết và hướng dẫn chuẩn bị hành lý.
          </p>

          <div class="pt-2 flex gap-3">
            <button 
              type="button" 
              onclick="navigator.clipboard.writeText('${randomCode}'); showToast('Đã sao chép', 'Mã booking đã được lưu vào bộ nhớ tạm.', 'success');"
              class="flex-1 py-3 rounded-full border border-gray-300 text-gray-700 text-xs font-bold hover:bg-gray-100 transition-colors"
            >
              Sao chép mã booking
            </button>
            <button 
              type="button" 
              onclick="closeBookingModal()"
              class="flex-1 py-3 rounded-full bg-forest text-white text-xs font-bold hover:bg-forest/90 transition-colors"
            >
              Hoàn tất
            </button>
          </div>
        </div>
      `;

      initLucideIcons();
      showToast('Đăng ký thành công', `Mã booking ${randomCode} đã được tạo thành công!`, 'success');
    }
  });
}

// ==========================================
// 12. WISHLIST & DRAWER SYSTEM
// ==========================================
window.toggleWishlist = function(tourId, e) {
  if (e) e.stopPropagation();
  const tour = TOURS_DATA.find(t => t.id === tourId);
  if (!tour) return;

  if (wishlist.has(tourId)) {
    wishlist.delete(tourId);
    showToast('Đã xóa khỏi yêu thích', `Đã bỏ lưu "${tour.title}".`, 'info');
  } else {
    wishlist.add(tourId);
    showToast('Đã lưu vào yêu thích', `"${tour.title}" đã được thêm vào danh sách quan tâm!`, 'success');
  }

  try {
    localStorage.setItem('dicunggio_wishlist', JSON.stringify(Array.from(wishlist)));
  } catch (err) {}

  updateWishlistBadges();
  renderTours();
  renderWishlistDrawer();
};

function updateWishlistBadges() {
  const count = wishlist.size;
  const badges = document.querySelectorAll('#header-cart-badge, #mobile-wishlist-badge');
  badges.forEach(b => {
    b.textContent = count;
    if (count > 0) {
      b.classList.remove('hidden');
    } else {
      b.classList.add('hidden');
    }
  });
}

window.openWishlistDrawer = function() {
  const drawer = document.getElementById('wishlist-drawer');
  const backdrop = document.getElementById('wishlist-drawer-backdrop');
  renderWishlistDrawer();
  if (drawer && backdrop) {
    backdrop.classList.remove('hidden');
    drawer.classList.remove('translate-x-full');
    document.body.style.overflow = 'hidden';
  }
};

window.closeWishlistDrawer = function() {
  const drawer = document.getElementById('wishlist-drawer');
  const backdrop = document.getElementById('wishlist-drawer-backdrop');
  if (drawer && backdrop) {
    drawer.classList.add('translate-x-full');
    backdrop.classList.add('hidden');
    document.body.style.overflow = '';
  }
};

function renderWishlistDrawer() {
  const list = document.getElementById('wishlist-drawer-items');
  if (!list) return;

  const likedTours = TOURS_DATA.filter(t => wishlist.has(t.id));

  if (likedTours.length === 0) {
    list.innerHTML = `
      <div class="text-center py-12 space-y-3">
        <div class="w-14 h-14 rounded-full bg-gray-100 flex items-center justify-center mx-auto text-gray-400">
          <i data-lucide="heart" class="w-6 h-6"></i>
        </div>
        <p class="text-xs text-gray-500">Chưa có tour nào trong danh sách quan tâm.</p>
        <button 
          type="button" 
          onclick="closeWishlistDrawer();" 
          class="text-xs font-bold text-forest hover:underline"
        >
          Khám phá danh sách tour ngay
        </button>
      </div>
    `;
  } else {
    list.innerHTML = likedTours.map(t => `
      <div class="flex items-center gap-3 p-3 rounded-2xl bg-gray-50 border border-gray-100 hover:border-gray-200 transition-colors">
        <img 
          src="${t.image}" 
          alt="${t.title}" 
          onerror="this.onerror=null; this.src='assets/images/tour-yen-tu.jpg';"
          class="w-16 h-16 rounded-xl object-cover shrink-0"
        />
        <div class="flex-1 min-w-0">
          <h4 class="text-xs font-bold text-gray-900 truncate">${t.title}</h4>
          <span class="text-xs font-extrabold text-forest block mt-0.5">${t.price}</span>
          <span class="text-[10px] text-gray-500">${t.duration}</span>
        </div>
        <div class="flex flex-col gap-1.5 shrink-0">
          <button 
            type="button" 
            onclick="closeWishlistDrawer(); openSmartBookingModal(${t.id});" 
            class="px-2.5 py-1 rounded-lg bg-forest text-white text-[11px] font-bold hover:bg-forest/90 cursor-pointer"
          >
            Đặt
          </button>
          <button 
            type="button" 
            onclick="toggleWishlist(${t.id});" 
            class="p-1 text-gray-400 hover:text-red-500 cursor-pointer text-center"
            title="Xóa"
          >
            <i data-lucide="trash-2" class="w-4 h-4 mx-auto"></i>
          </button>
        </div>
      </div>
    `).join('');
  }

  initLucideIcons();
}

// ==========================================
// 13. SEARCH OVERLAY & REAL-TIME FILTER
// ==========================================
window.openSearchModal = function() {
  const modal = document.getElementById('search-modal');
  const input = document.getElementById('search-input');
  if (modal) {
    modal.classList.remove('hidden');
    document.body.style.overflow = 'hidden';
    setTimeout(() => input?.focus(), 50);
    handleSearchInput('');
  }
};

window.closeSearchModal = function() {
  const modal = document.getElementById('search-modal');
  if (modal) {
    modal.classList.add('hidden');
    document.body.style.overflow = '';
  }
};

window.handleSearchInput = function(query) {
  const q = (query || '').toLowerCase().trim();
  const resultsBox = document.getElementById('search-results');
  if (!resultsBox) return;

  const matches = TOURS_DATA.filter(t => 
    t.title.toLowerCase().includes(q) || 
    t.location.toLowerCase().includes(q) || 
    t.categoryName.toLowerCase().includes(q) ||
    (t.shortSummary && t.shortSummary.toLowerCase().includes(q))
  );

  if (matches.length === 0) {
    resultsBox.innerHTML = `
      <div class="text-center py-8 text-gray-500 text-xs">
        Không tìm thấy tour phù hợp với từ khóa "<strong>${query}</strong>".
      </div>
    `;
  } else {
    resultsBox.innerHTML = matches.map(t => `
      <div 
        onclick="closeSearchModal(); openTourDetailModal(${t.id});"
        class="flex items-center gap-3 p-3 rounded-2xl hover:bg-gray-50 border border-transparent hover:border-gray-200 transition-all cursor-pointer group"
      >
        <img 
          src="${t.image}" 
          alt="${t.title}" 
          onerror="this.onerror=null; this.src='assets/images/tour-yen-tu.jpg';"
          class="w-14 h-14 rounded-xl object-cover shrink-0"
        />
        <div class="flex-1 min-w-0">
          <div class="flex items-center gap-2">
            <span class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-forest/10 text-forest">${t.badge}</span>
            <span class="text-[10px] text-gray-400">${t.duration}</span>
          </div>
          <h4 class="text-xs sm:text-sm font-bold text-gray-900 group-hover:text-forest transition-colors truncate mt-1">
            ${t.title}
          </h4>
          <span class="text-xs text-gray-500 truncate block">${t.location}</span>
        </div>
        <span class="text-xs font-black text-forest shrink-0">${t.price}</span>
      </div>
    `).join('');
  }

  initLucideIcons();
};

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
  const iframe = document.getElementById('video-iframe');
  if (modal) {
    modal.classList.add('hidden');
    document.body.style.overflow = '';
    // Pause iframe
    if (iframe) {
      const src = iframe.src;
      iframe.src = src;
    }
  }
};

// ==========================================
// 15. REVIEWS & TESTIMONIALS MODAL
// ==========================================
window.openReviewsModal = function() {
  const modal = document.getElementById('reviews-modal');
  const list = document.getElementById('reviews-modal-list');
  if (!modal || !list) return;

  list.innerHTML = TESTIMONIALS_DATA.map(r => `
    <div class="p-4 rounded-2xl bg-gray-50 border border-gray-100 space-y-2">
      <div class="flex items-center justify-between">
        <div class="flex items-center gap-3">
          <img src="${r.avatar}" alt="${r.name}" class="w-10 h-10 rounded-full object-cover border border-emerald-100" />
          <div>
            <h4 class="text-xs sm:text-sm font-bold text-gray-900 leading-tight">${r.name}</h4>
            <span class="text-[11px] text-forest font-semibold">${r.role}</span>
          </div>
        </div>
        <div class="flex text-amber-400 text-xs">
          ${'★'.repeat(r.rating)}
        </div>
      </div>
      <p class="text-xs text-gray-700 italic leading-relaxed">${r.comment}</p>
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

window.submitNewReview = function(e) {
  e.preventDefault();
  const name = document.getElementById('review-form-name')?.value.trim();
  const comment = document.getElementById('review-form-comment')?.value.trim();
  const tourName = document.getElementById('review-form-tour')?.value || 'Trekking Việt Nam';

  if (!name || !comment) {
    showToast('Vui lòng điền đủ', 'Hãy nhập họ tên và cảm nhận của bạn.', 'error');
    return;
  }

  TESTIMONIALS_DATA.unshift({
    id: Date.now(),
    name: name,
    role: tourName,
    avatar: 'assets/images/avatar-ha.jpg',
    comment: `“${comment}”`,
    rating: 5
  });

  showToast('Cảm ơn bạn!', 'Đánh giá của bạn đã được ghi nhận và hiển thị.', 'success');
  openReviewsModal();
};

// ==========================================
// 16. TOAST NOTIFICATION UTILITY
// ==========================================
function showToast(title, message, type = 'info') {
  const container = document.getElementById('toast-container');
  if (!container) return;

  const id = 'toast-' + Date.now();
  const toast = document.createElement('div');
  toast.id = id;
  toast.className = 'toast-slide-in pointer-events-auto flex items-start gap-3 p-4 rounded-2xl bg-white shadow-xl border border-gray-100 max-w-sm w-full transition-all';

  let iconName = 'info';
  let iconColor = 'text-blue-500 bg-blue-50';
  if (type === 'success') {
    iconName = 'check-circle-2';
    iconColor = 'text-forest bg-emerald-50';
  } else if (type === 'error') {
    iconName = 'alert-triangle';
    iconColor = 'text-red-500 bg-red-50';
  }

  toast.innerHTML = `
    <div class="w-8 h-8 rounded-xl ${iconColor} flex items-center justify-center shrink-0">
      <i data-lucide="${iconName}" class="w-4 h-4"></i>
    </div>
    <div class="flex-1 min-w-0">
      <h5 class="text-xs font-bold text-gray-900">${title}</h5>
      <p class="text-[11px] text-gray-600 mt-0.5 leading-relaxed">${message}</p>
    </div>
    <button 
      type="button" 
      onclick="document.getElementById('${id}')?.remove()" 
      class="text-gray-400 hover:text-gray-600 p-1"
    >
      <i data-lucide="x" class="w-3.5 h-3.5"></i>
    </button>
  `;

  container.appendChild(toast);
  initLucideIcons();

  setTimeout(() => {
    toast.style.opacity = '0';
    toast.style.transform = 'translateX(60px)';
    setTimeout(() => toast.remove(), 300);
  }, 4500);
}

// ==========================================
// 17. SCROLL OBSERVERS & INTERACTIONS
// ==========================================
function setupScrollReveal() {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('revealed');
      }
    });
  }, { threshold: 0.1 });

  document.querySelectorAll('.reveal-on-scroll').forEach(el => observer.observe(el));
}

function setupScrollSpy() {
  const sections = document.querySelectorAll('section[id], footer[id]');
  const navLinks = document.querySelectorAll('.nav-link');

  window.addEventListener('scroll', () => {
    let current = '';
    const scrollPos = window.scrollY + 200;

    sections.forEach(sec => {
      const top = sec.offsetTop;
      const height = sec.offsetHeight;
      if (scrollPos >= top && scrollPos < top + height) {
        current = sec.getAttribute('id');
      }
    });

    navLinks.forEach(link => {
      link.classList.remove('active');
      if (link.getAttribute('href') === `#${current}`) {
        link.classList.add('active');
      }
    });
  });
}

function setupNavbarGlass() {
  const backToTop = document.getElementById('back-to-top');

  window.addEventListener('scroll', () => {
    if (window.scrollY > 400) {
      backToTop?.classList.add('visible');
    } else {
      backToTop?.classList.remove('visible');
    }
  });

  backToTop?.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
}

function setupFloatingActions() {
  const zaloBtn = document.getElementById('float-zalo');
  const phoneBtn = document.getElementById('float-phone');
  const messengerBtn = document.getElementById('float-messenger');

  zaloBtn?.addEventListener('click', () => {
    window.open('https://zalo.me/0965983302', '_blank');
  });

  phoneBtn?.addEventListener('click', () => {
    window.location.href = 'tel:0965983302';
  });

  messengerBtn?.addEventListener('click', () => {
    window.open('https://m.me/dicunggiotrekking', '_blank');
  });
}

function setupMobileNav() {
  const toggleBtn = document.getElementById('mobile-menu-btn');
  const closeBtn = document.getElementById('mobile-menu-close');
  const navDrawer = document.getElementById('mobile-nav-drawer');
  const backdrop = document.getElementById('mobile-nav-backdrop');

  if (!toggleBtn || !navDrawer) return;

  const openNav = () => {
    navDrawer.classList.remove('-translate-x-full');
    backdrop?.classList.remove('hidden');
    document.body.style.overflow = 'hidden';
  };

  const closeNav = () => {
    navDrawer.classList.add('-translate-x-full');
    backdrop?.classList.add('hidden');
    document.body.style.overflow = '';
  };

  toggleBtn.addEventListener('click', openNav);
  closeBtn?.addEventListener('click', closeNav);
  backdrop?.addEventListener('click', closeNav);

  navDrawer.querySelectorAll('a').forEach(a => {
    a.addEventListener('click', closeNav);
  });
}

function setupNewsletterForm() {
  const form = document.getElementById('newsletter-form');
  if (!form) return;

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const emailInput = document.getElementById('newsletter-email');
    if (emailInput && emailInput.value) {
      showToast('Đăng ký nhận tin thành công', 'Cảm ơn bạn! Trekking Đi Cùng Gió sẽ gửi ưu đãi và lịch khởi hành mới nhất tới email của bạn.', 'success');
      emailInput.value = '';
    }
  });
}
'''

with open('assets/js/main.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("assets/js/main.js successfully generated!")

