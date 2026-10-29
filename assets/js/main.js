/**
 * Trekking Đi Cùng Gió - Interactive Prototype Engine (Version 3.1)
 * "Khám phá thiên nhiên, chinh phục mọi giới hạn"
 */

// ==========================================
// 1. TOUR DATA REPOSITORY (ALL 5 CATEGORIES)
// ==========================================
const TOURS_DATA = [
  // --- CATEGORY 1: TREKKING ---
  {
    id: 1,
    title: 'Trekking Yên Tử – Chùa Đồng',
    category: 'trekking',
    subCategory: 'near_hanoi',
    categoryName: 'Trekking',
    duration: '1 ngày',
    location: 'Hà Nội – Yên Tử',
    price: '1.200.000đ/người',
    priceNum: 1200000,
    rating: 5.0,
    reviews: 128,
    image: 'assets/images/tour-yen-tu.jpg',
    badge: 'Trekking',
    altitudeBadge: '⛰️ 1.068m',
    altitude: '1.068m',
    trekDistance: '10 km',
    difficultyLevel: 2,
    difficultyText: 'Nhẹ - Trung bình',
    description: 'Hành trình leo núi thiêng Yên Tử, chiêm bái Chùa Đồng trên đỉnh Phù Vân, rèn luyện thể lực và tìm lại an yên trong tâm hồn giữa mây ngàn đại ngàn.',
    departureDates: ['01/11/2026', '08/11/2026', '15/11/2026', '22/11/2026'],
    isFeatured: true,
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
  {
    id: 2,
    title: 'Tà Xùa – Săn mây',
    category: 'trekking',
    subCategory: 'experience',
    categoryName: 'Trekking',
    duration: '2 ngày 1 đêm',
    location: 'Hà Nội – Tà Xùa',
    price: '1.850.000đ/người',
    priceNum: 1850000,
    rating: 5.0,
    reviews: 96,
    image: 'assets/images/tour-ta-xua.jpg',
    badge: 'Trekking',
    altitudeBadge: '☁️ 2.865m',
    altitude: '2.865m',
    trekDistance: '14 km',
    difficultyLevel: 3,
    difficultyText: 'Trung bình',
    description: 'Chinh phục "sống lưng khủng long" huyền thoại Bản Công, đắm chìm trong biển mây bồng bềnh lúc bình minh và tận hưởng bầu không khí Tây Bắc se lạnh.',
    departureDates: ['26/10/2026', '02/11/2026', '09/11/2026', '16/11/2026'],
    isFeatured: true,
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
    altitudeBadge: '🏔️ 2.879m',
    altitude: '2.879m',
    trekDistance: '18 km',
    difficultyLevel: 4,
    difficultyText: 'Khá thách thức',
    description: 'Cung đường hoang sơ đầy thách thức với những vách đá hùng vĩ, thảm thực vật đỗ quyên nguyên sinh và tầm nhìn panorama ngoạn mục bậc nhất Tây Bắc.',
    departureDates: ['08/11/2026', '22/11/2026', '06/12/2026'],
    isFeatured: true,
    highlights: [
      'Băng qua rừng cổ thụ rêu phong kỳ bí như trong truyện cổ tích.',
      'Chạm mốc đỉnh Phu Sa Phin hùng vĩ giữa bốn bề mây ngàn Tây Bắc.',
      'Cắm trại ngủ lán gỗ giữa lưng chừng trời, ngắm dải Ngân Hà rực rỡ không ánh đèn đô thị.'
    ],
    itinerary: [
      { day: 'Đêm 0', title: 'Hà Nội – Điểm tập kết', desc: '21:30 đón tại Hà Nội đi xe giường nằm chất lượng cao tới chân núi.' },
      { day: 'Ngày 1', title: 'Bắt đầu leo dốc – Hạ trại lán rừng', desc: 'Ăn sáng, phân chia đồ dùng cùng Porter. Bắt đầu leo qua các dốc đá và rừng thảo quả. Chiều tới lán nghỉ 2.400m, nướng thịt ăn tối.' },
      { day: 'Ngày 2', title: 'Chạm đỉnh đón bình minh – Xuống núi', desc: '05:00 xuất phát lên đỉnh đón bình minh biển mây. Xuống núi, tắm lá thuốc người Dao đỏ và lên xe về Hà Nội.' }
    ],
    included: ['Xe đưa đón giường nằm cao cấp', 'Porter bản địa gùi đồ & nấu ăn', 'Ngủ lán gỗ ấm cúng có chăn dày', 'Các bữa ăn đậm đà bản sắc', 'Bảo hiểm du lịch 100.000.000đ', 'Giấy phép trekking ban quản lý'],
    preparation: ['Balo trợ lực 30-40L', 'Đèn pin đội đầu loại sáng tốt', 'Áo mưa bộ chống nước tuyệt đối', 'Găng tay leo núi có hạt cao su']
  },
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
    trekDistance: '28 km',
    difficultyLevel: 5,
    difficultyText: 'Thử thách cao',
    description: 'Chinh phục đỉnh núi cao thứ 4 Việt Nam (3.046m), ngắm đồi Muối lung linh dưới ánh sao đêm và biển mây ngút ngàn tầm mắt đón bình minh.',
    departureDates: ['22/11/2026', '06/12/2026', '20/12/2026'],
    isFeatured: true,
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

  // --- CATEGORY 2: TÂM LINH (SPIRITUAL) ---
  {
    id: 5,
    title: 'Hành hương Tam Chúc – Ba Sao An Nhiên',
    category: 'spiritual',
    subCategory: 'spiritual',
    categoryName: 'Tâm linh',
    duration: '1 ngày',
    location: 'Hà Nội – Hà Nam',
    price: '950.000đ/người',
    priceNum: 950000,
    rating: 4.9,
    reviews: 88,
    image: 'https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=800&q=80',
    badge: 'Tâm linh',
    altitudeBadge: '🪷 An yên',
    altitude: '250m',
    trekDistance: '6 km',
    difficultyLevel: 1,
    difficultyText: 'Nhẹ nhàng',
    description: 'Chuyến hành hương tìm về cõi Phật thanh tịnh giữa non nước Ninh Bình - Hà Nam, du thuyền trên hồ Lục Nhạc và viếng chùa Tam Chúc linh thiêng.',
    departureDates: ['01/11/2026', '15/11/2026', '29/11/2026'],
    isFeatured: false,
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
  {
    id: 6,
    title: 'Chiêm bái Chùa Hương – Suối Yến Mùa Thu',
    category: 'spiritual',
    subCategory: 'spiritual',
    categoryName: 'Tâm linh',
    duration: '1 ngày',
    location: 'Hà Nội – Mỹ Đức',
    price: '890.000đ/người',
    priceNum: 890000,
    rating: 4.8,
    reviews: 64,
    image: 'https://images.unsplash.com/photo-1528127269322-539801943592?auto=format&fit=crop&w=800&q=80',
    badge: 'Tâm linh',
    altitudeBadge: '🪷 Non thiêng',
    altitude: '380m',
    trekDistance: '7 km',
    difficultyLevel: 2,
    difficultyText: 'Nhẹ nhàng',
    description: 'Chèo thuyền xuôi dòng suối Yến ngắm hoa súng tím biếc, trekking chinh phục Động Hương Tích – Nam Thiên Đệ Nhất Động linh thiêng cầu bình an.',
    departureDates: ['08/11/2026', '22/11/2026'],
    isFeatured: false,
    highlights: ['Thuyền nan trôi nhẹ giữa dòng suối Yến hoa súng nở rộ.', 'Chiêm bái Động Hương Tích tĩnh mịch linh thiêng.', 'Trekking bậc đá rèn luyện đôi chân dẻo dai.'],
    itinerary: [
      { day: '07:30', title: 'Hà Nội – Bến Đục Chùa Hương', desc: 'Di chuyển bằng xe du lịch êm ái.' },
      { day: '09:00', title: 'Xuôi dòng Suối Yến', desc: 'Thưởng ngoạn cảnh sắc mộng mơ suối Yến mùa hoa súng.' },
      { day: '11:30', title: 'Chiêm bái Động Hương Tích', desc: 'Trekking lên động dâng hương cầu tài lộc sức khỏe cho người thân.' },
      { day: '16:00', title: 'Về lại Hà Nội', desc: 'Lên xe trở về thủ đô sau ngày an yên.' }
    ],
    included: ['Xe du lịch khứ hồi', 'Vé thuyền đò suối Yến', 'Ăn trưa đặc sản rau sắng', 'Hướng dẫn viên chu đáo', 'Bảo hiểm du lịch'],
    preparation: ['Giày thể thao êm chân', 'Trang phục trang nhã', 'Mũ che nắng']
  },
  {
    id: 7,
    title: 'Bái Đính – Tràng An: Non Nước Linh Thiêng',
    category: 'spiritual',
    subCategory: 'spiritual',
    categoryName: 'Tâm linh',
    duration: '1 ngày',
    location: 'Hà Nội – Ninh Bình',
    price: '1.050.000đ/người',
    priceNum: 1050000,
    rating: 4.9,
    reviews: 110,
    image: 'https://images.unsplash.com/photo-1570197788417-0e82375c9371?auto=format&fit=crop&w=800&q=80',
    badge: 'Tâm linh',
    altitudeBadge: '🪷 Di sản',
    altitude: '200m',
    trekDistance: '5 km',
    difficultyLevel: 1,
    difficultyText: 'Dễ dàng',
    description: 'Hành hương ngôi chùa nắm giữ nhiều kỷ lục nhất châu Á, kết hợp ngồi thuyền len lỏi qua các hang động kỳ vĩ của di sản thế giới Tràng An.',
    departureDates: ['07/11/2026', '21/11/2026'],
    isFeatured: false,
    highlights: ['Hành lang 500 vị La Hán đá nguyên khối Chùa Bái Đính.', 'Thuyền nan luồn qua 4 hang động kỳ ảo Tràng An.', 'Thưởng thức ẩm thực dê núi cơm cháy Ninh Bình.'],
    itinerary: [
      { day: '07:00', title: 'Hà Nội – Bái Đính', desc: 'Khởi hành theo đường cao tốc Hà Nội – Ninh Bình.' },
      { day: '09:30', title: 'Vãn cảnh Đại Bi Tự Bái Đính', desc: 'Viếng Bảo Tháp, Điện Tam Thế, giếng Ngọc.' },
      { day: '13:30', title: 'Khám phá Tràng An bằng thuyền', desc: 'Hòa mình vào thiên nhiên sơn thủy hữu tình.' },
      { day: '17:00', title: 'Khởi hành về Hà Nội', desc: 'Về tới Hà Nội lúc 19:00.' }
    ],
    included: ['Xe du lịch máy lạnh', 'Vé thắng cảnh & thuyền Tràng An', 'Bữa trưa ẩm thực Ninh Bình', 'Hướng dẫn viên nhiệt tình', 'Bảo hiểm du lịch'],
    preparation: ['Máy ảnh & nón lá', 'Kem chống nắng', 'Giày đi bộ thoải mái']
  },
  {
    id: 8,
    title: 'Trekking Yên Tử – Non Thiêng Mây Ngàn (Mở rộng)',
    category: 'spiritual',
    subCategory: 'near_hanoi',
    categoryName: 'Tâm linh',
    duration: '1 ngày',
    location: 'Hà Nội – Uông Bí',
    price: '1.200.000đ/người',
    priceNum: 1200000,
    rating: 5.0,
    reviews: 79,
    image: 'assets/images/tour-yen-tu.jpg',
    badge: 'Tâm linh',
    altitudeBadge: '⛰️ 1.068m',
    altitude: '1.068m',
    trekDistance: '10 km',
    difficultyLevel: 2,
    difficultyText: 'Trung bình',
    description: 'Hành trình leo bộ 100% không dùng cáp treo, trải nghiệm con đường hành hương cổ xưa của vua Trần Nhân Tông lên đỉnh Chùa Đồng linh thiêng.',
    departureDates: ['08/11/2026', '22/11/2026'],
    isFeatured: false,
    highlights: ['Chinh phục trọn vẹn từng bậc đá cổ truyền thống.', 'Nghe chuyện về Phật hoàng Trần Nhân Tông khai sáng Thiền phái Trúc Lâm.', 'Tìm lại sự tĩnh lặng tuyệt đối cho tâm hồn.'],
    itinerary: [
      { day: '06:00', title: 'Hà Nội – Chân núi Yên Tử', desc: 'Khởi hành sớm đón không khí trong lành.' },
      { day: '09:00', title: 'Trekking qua Suối Giải Oan – Chùa Hoa Yên', desc: 'Leo bộ qua từng cung bậc lịch sử.' },
      { day: '12:30', title: 'Chạm đỉnh Chùa Đồng', desc: 'Dâng hương chiêm bái, ngắm biển mây và dùng bữa trưa.' },
      { day: '18:00', title: 'Về đến Hà Nội', desc: 'Kết thúc chuyến hành hương trọn vẹn ý nghĩa.' }
    ],
    included: ['Xe du lịch khứ hồi', 'Bữa trưa picnic thịnh soạn', 'Hướng dẫn viên kinh nghiệm', 'Gậy trekking & bảo hiểm', 'Nước uống điện giải'],
    preparation: ['Giày bám đá tốt', 'Bình giữ nhiệt nhỏ', 'Trang phục vận động thoải mái']
  },

  // --- CATEGORY 3: TRẢI NGHIỆM (EXPERIENCE) ---
  {
    id: 9,
    title: 'Mai Châu – Mộc Châu: Mùa Hoa Cải Trắng',
    category: 'experience',
    subCategory: 'experience',
    categoryName: 'Trải nghiệm',
    duration: '2 ngày 1 đêm',
    location: 'Hòa Bình – Sơn La',
    price: '1.450.000đ/người',
    priceNum: 1450000,
    rating: 4.9,
    reviews: 65,
    image: 'https://images.unsplash.com/photo-1528127269322-539801943592?auto=format&fit=crop&w=800&q=80',
    badge: 'Trải nghiệm',
    altitudeBadge: '🌸 Mộc Châu',
    altitude: '1.050m',
    trekDistance: '8 km',
    difficultyLevel: 1,
    difficultyText: 'Nhẹ nhàng',
    description: 'Trải nghiệm nét đẹp văn hóa người Thái ở Bản Lác, ngắm mùa hoa cải trắng tinh khôi Mộc Châu và đốt lửa trại giữa thung lũng đại ngàn.',
    departureDates: ['07/11/2026', '21/11/2026', '05/12/2026'],
    isFeatured: false,
    highlights: ['Đạp xe dạo quanh Bản Lác người Thái yên bình.', 'Check-in cánh đồng hoa cải trắng bạt ngàn thung lũng Mộc Châu.', 'Giao lưu múa sạp, uống rượu cần bên bếp lửa ấm áp.'],
    itinerary: [
      { day: 'Ngày 1', title: 'Hà Nội – Đèo Thung Khe – Bản Lác Mai Châu', desc: 'Dừng chân ngắm tuyết trắng đèo Thung Khe. Chiều đạp xe khám phá bản làng, tối múa xòe Thái.' },
      { day: 'Ngày 2', title: 'Mai Châu – Cao nguyên Mộc Châu – Hà Nội', desc: 'Tham quan đồi chè trái tim, vườn hoa cải trắng Mu Náu. Chiều về lại Hà Nội.' }
    ],
    included: ['Xe du lịch suốt tuyến', 'Homestay nhà sàn sạch sẽ tiện nghi', 'Các bữa ăn đặc sản Tây Bắc', 'Xe đạp dạo bản & múa xòe rượu cần', 'Bảo hiểm du lịch trọn gói'],
    preparation: ['Trang phục chụp ảnh rực rỡ', 'Áo ấm nhẹ cho buổi tối', 'Máy ảnh & sạc dự phòng']
  },
  {
    id: 10,
    title: 'Mù Cang Chải: Mùa Vàng Ruộng Bậc Thang',
    category: 'experience',
    subCategory: 'experience',
    categoryName: 'Trải nghiệm',
    duration: '3 ngày 2 đêm',
    location: 'Hà Nội – Yên Bái',
    price: '2.250.000đ/người',
    priceNum: 2250000,
    rating: 5.0,
    reviews: 82,
    image: 'https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=800&q=80',
    badge: 'Trải nghiệm',
    altitudeBadge: '🌾 Mù Cang Chải',
    altitude: '1.200m',
    trekDistance: '12 km',
    difficultyLevel: 2,
    difficultyText: 'Dễ - Trung bình',
    description: 'Chiêm ngưỡng kiệt tác ruộng bậc thang Mâm Xôi, Vành Móng Ngựa vàng óng ả dưới nắng thu và bay dù lượn trên đỉnh đèo Khau Phạ.',
    departureDates: ['14/11/2026', '28/11/2026'],
    isFeatured: false,
    highlights: ['Bình minh trên đồi Mâm Xôi và hoàng hôn Vành Móng Ngựa.', 'Chinh phục một trong "Tứ đại đỉnh đèo" Khau Phạ.', 'Thưởng thức nếp mới Tú Lệ thơm nức lòng.'],
    itinerary: [
      { day: 'Ngày 1', title: 'Hà Nội – Nghĩa Lộ – Đèo Khau Phạ – Mù Cang Chải', desc: 'Check-in thung lũng Tú Lệ, vượt đèo Khau Phạ hùng vĩ.' },
      { day: 'Ngày 2', title: 'Đồi Mâm Xôi – Vành Móng Ngựa – La Pán Tẩn', desc: 'Trekking săn ảnh mùa lúa chín vàng rực thung lũng.' },
      { day: 'Ngày 3', title: 'Bản Lìm Mông – Hà Nội', desc: 'Giao lưu văn hóa trẻ em người H’Mông, lên xe về lại Hà Nội.' }
    ],
    included: ['Xe du lịch 29 chỗ đời mới', 'Homestay view ruộng bậc thang', 'Ăn uống trọn gói đặc sản xôi nếp Tú Lệ', 'Hướng dẫn viên bản địa', 'Bảo hiểm du lịch'],
    preparation: ['Giày thể thao êm chân', 'Trang phục màu sắc nổi bật chụp ảnh', 'Áo gió nhẹ']
  },
  {
    id: 11,
    title: 'Hà Giang: Mùa Hoa Tam Giác Mạch & Mã Pí Lèng',
    category: 'experience',
    subCategory: 'experience',
    categoryName: 'Trải nghiệm',
    duration: '3 ngày 2 đêm',
    location: 'Hà Nội – Hà Giang',
    price: '2.450.000đ/người',
    priceNum: 2450000,
    rating: 5.0,
    reviews: 94,
    image: 'https://images.unsplash.com/photo-1570197788417-0e82375c9371?auto=format&fit=crop&w=800&q=80',
    badge: 'Trải nghiệm',
    altitudeBadge: '🏔️ Cao nguyên đá',
    altitude: '1.500m',
    trekDistance: '10 km',
    difficultyLevel: 2,
    difficultyText: 'Trung bình',
    description: 'Chinh phục hẻm Tu Sản sâu nhất Đông Nam Á trên dòng sông Nho Quế xanh ngọc bích, ngắm hoa tam giác mạch hồng phớt phủ kín cao nguyên đá Đồng Văn.',
    departureDates: ['13/11/2026', '27/11/2026'],
    isFeatured: false,
    highlights: ['Đi thuyền kayak ngắm hẻm vực Tu Sản kỳ vĩ sông Nho Quế.', 'Chinh phục đèo Mã Pí Lèng huyền thoại.', 'Check-in Cột cờ Lũng Cú cực Bắc Tổ quốc.'],
    itinerary: [
      { day: 'Ngày 1', title: 'Hà Nội – Quản Bạ – Yên Minh – Đồng Văn', desc: 'Ngắm dốc Thẩm Mã, cổng trời Quản Bạ, phố cổ Đồng Văn về đêm.' },
      { day: 'Ngày 2', title: 'Mã Pí Lèng – Sông Nho Quế – Mèo Vạc', desc: 'Đi thuyền dưới hẻm Tu Sản, thưởng ngoạn cảnh sắc kỳ vĩ.' },
      { day: 'Ngày 3', title: 'Dinh thự Vua Mèo – Hà Nội', desc: 'Khám phá kiến trúc Dinh họ Vương, lên xe về lại thủ đô.' }
    ],
    included: ['Xe du lịch giường nằm / ghế ngả cao cấp', 'Vé đi thuyền hẻm Tu Sản', 'Khách sạn / Homestay tiện nghi', 'Các bữa ăn thịnh soạn', 'Bảo hiểm du lịch'],
    preparation: ['Áo khoác ấm (nhiệt độ đêm se lạnh)', 'Máy ảnh & thẻ nhớ lớn', 'Thuốc say xe']
  },
  {
    id: 12,
    title: 'Pù Luông: Mùa Lúa Chín Thung Lũng Xanh',
    category: 'experience',
    subCategory: 'experience',
    categoryName: 'Trải nghiệm',
    duration: '2 ngày 1 đêm',
    location: 'Hà Nội – Thanh Hóa',
    price: '1.650.000đ/người',
    priceNum: 1650000,
    rating: 4.9,
    reviews: 48,
    image: 'https://images.unsplash.com/photo-1448375240586-882707db888b?auto=format&fit=crop&w=800&q=80',
    badge: 'Trải nghiệm',
    altitudeBadge: '🌾 Thung lũng xanh',
    altitude: '800m',
    trekDistance: '10 km',
    difficultyLevel: 2,
    difficultyText: 'Nhẹ nhàng',
    description: 'Nghỉ dưỡng giữa thiên đường xanh Pù Luông, ngắm guồng nước khổng lồ bản Co Lương và đi bộ xuyên qua những bản làng người Thái mến khách.',
    departureDates: ['07/11/2026', '21/11/2026'],
    isFeatured: false,
    highlights: ['Bể bơi vô cực view trọn thung lũng lúa chín Pù Luông.', 'Trekking bản Đôn, bản Hiêu tắm thác nước trong veo.', 'Thưởng thức vịt Cổ Lũng nướng than hoa nức tiếng.'],
    itinerary: [
      { day: 'Ngày 1', title: 'Hà Nội – Pù Luông – Bản Đôn', desc: 'Trekking qua ruộng bậc thang bản Đôn, ngắm hoàng hôn bên bể bơi vô cực.' },
      { day: 'Ngày 2', title: 'Thác Hiêu – Guồng nước bản Co Lương – Hà Nội', desc: 'Khám phá guồng nước khổng lồ, dùng bữa trưa rồi về lại Hà Nội.' }
    ],
    included: ['Xe du lịch đưa đón khứ hồi', 'Resort / Homestay cao cấp view ruộng', 'Ăn uống đặc sản vịt Cổ Lũng', 'Hướng dẫn viên nhiệt tình', 'Bảo hiểm du lịch'],
    preparation: ['Đồ bơi check-in', 'Giày đi bộ thoải mái', 'Xịt chống muỗi']
  },

  // --- CATEGORY 4: THIỆN NGUYỆN (CHARITY) ---
  {
    id: 13,
    title: 'Áo Ấm Cho Em – Thiện Nguyện Mù Cang Chải',
    category: 'charity',
    subCategory: 'charity',
    categoryName: 'Thiện nguyện',
    duration: '2 ngày 1 đêm',
    location: 'Hà Nội – Yên Bái',
    price: '1.100.000đ/người',
    priceNum: 1100000,
    rating: 5.0,
    reviews: 42,
    image: 'https://images.unsplash.com/photo-1488521787991-ed7bbaae773c?auto=format&fit=crop&w=800&q=80',
    badge: 'Thiện nguyện',
    altitudeBadge: '❤️ Yêu thương',
    altitude: '1.200m',
    trekDistance: '6 km',
    difficultyLevel: 1,
    difficultyText: 'Cộng đồng',
    description: 'Hành trình ý nghĩa mang hơi ấm mùa đông đến cho các em nhỏ vùng cao La Pán Tẩn, kết hợp giao lưu văn nghệ và ngắm mùa vàng ruộng bậc thang.',
    departureDates: ['14/11/2026', '28/11/2026'],
    isFeatured: false,
    highlights: [
      'Trao tận tay 150 suất quà áo ấm, ủng đi mưa và sách vở cho học sinh điểm trường vùng cao.',
      'Tổ chức đêm hội Trung thu / giao lưu đốt lửa trại cùng thầy trò bản địa.',
      'Gắn kết những trái tim thiện nguyện cùng chí hướng lan tỏa yêu thương.'
    ],
    itinerary: [
      { day: 'Ngày 1', title: 'Hà Nội – Điểm trường Mù Cang Chải', desc: 'Vận chuyển quà tặng, tổ chức chương trình trao quà và giao lưu văn nghệ cùng các em nhỏ.' },
      { day: 'Ngày 2', title: 'Khám phá bản làng – Hà Nội', desc: 'Trekking nhẹ thăm đời sống bà con người H’Mông, lên xe về lại Hà Nội chiều muộn.' }
    ],
    included: ['Xe du lịch chuyên chở đoàn & hàng hóa thiện nguyện', 'Ăn ngủ homestay bản làng', 'Điều phối viên chương trình chu đáo', 'Bảo hiểm du lịch'],
    preparation: ['Trang phục ấm áp giản dị', 'Tấm lòng sẻ chia nhiệt huyết', 'Có thể mang thêm sách truyện cũ hoặc bánh kẹo']
  },
  {
    id: 14,
    title: 'Thư Viện Vùng Cao – Bắc Hà Nụ Cười Em Thơ',
    category: 'charity',
    subCategory: 'charity',
    categoryName: 'Thiện nguyện',
    duration: '2 ngày 1 đêm',
    location: 'Hà Nội – Lào Cai',
    price: '1.250.000đ/người',
    priceNum: 1250000,
    rating: 5.0,
    reviews: 38,
    image: 'https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=800&q=80',
    badge: 'Thiện nguyện',
    altitudeBadge: '❤️ Nụ cười',
    altitude: '1.000m',
    trekDistance: '5 km',
    difficultyLevel: 1,
    difficultyText: 'Cộng đồng',
    description: 'Xây dựng tủ sách học đường và trang bị đồ dùng học tập cho trường tiểu học Bản Phố (Bắc Hà), kết hợp trải nghiệm chợ phiên rực rỡ sắc màu.',
    departureDates: ['21/11/2026', '05/12/2026'],
    isFeatured: false,
    highlights: ['Trực tiếp lắp ráp tủ sách 1.000 đầu sách bổ ích cho trường nghèo.', 'Giao lưu trò chơi dân gian cùng học sinh vùng cao.', 'Khám phá chợ phiên Bắc Hà giàu bản sắc.'],
    itinerary: [
      { day: 'Ngày 1', title: 'Hà Nội – Bắc Hà – Lắp đặt thư viện', desc: 'Bàn giao sách, sơn sửa góc đọc sách cùng thầy cô và học sinh.' },
      { day: 'Ngày 2', title: 'Chợ phiên Bắc Hà – Hà Nội', desc: 'Dạo chợ phiên ngắm sắc màu trang phục thổ cẩm, về lại thủ đô.' }
    ],
    included: ['Xe đưa đón khứ hồi', 'Homestay bản làng', 'Các bữa ăn bản địa', 'Bảo hiểm du lịch trọn gói'],
    preparation: ['Sách truyện lứa tuổi mầm non/tiểu học', 'Găng tay lao động nhẹ', 'Quần áo ấm']
  },
  {
    id: 15,
    title: 'Đi Học Cùng Em – Sưởi Ấm Mùa Đông Y Tý',
    category: 'charity',
    subCategory: 'charity',
    categoryName: 'Thiện nguyện',
    duration: '3 ngày 2 đêm',
    location: 'Hà Nội – Bát Xát',
    price: '1.950.000đ/người',
    priceNum: 1950000,
    rating: 5.0,
    reviews: 55,
    image: 'assets/images/tour-ky-quan-san.jpg',
    badge: 'Thiện nguyện',
    altitudeBadge: '❤️ Y Tý mây ngàn',
    altitude: '2.000m',
    trekDistance: '8 km',
    difficultyLevel: 2,
    difficultyText: 'Cộng đồng',
    description: 'Chuyến xe thiện nguyện đưa áo ấm, chăn bông và bình nóng lạnh năng lượng mặt trời lên điểm trường mầm non vùng cao Y Tý mây ngàn buốt giá.',
    departureDates: ['27/11/2026', '11/12/2026'],
    isFeatured: false,
    highlights: ['Trao trang thiết bị nước ấm giúp các em nhỏ không còn sợ rét mùa đông.', 'Ngắm biển mây Y Tý bồng bềnh và những ngôi nhà nấm đất của người Hà Nhì.'],
    itinerary: [
      { day: 'Đêm 0', title: 'Hà Nội – Lào Cai', desc: 'Xe giường nằm khởi hành 22:00 lên ga Lào Cai.' },
      { day: 'Ngày 1', title: 'Lên Y Tý – Trao quà thiện nguyện', desc: 'Lắp đặt bình nước ấm, nấu bữa ăn có thịt cho các em nhỏ.' },
      { day: 'Ngày 2', title: 'Săn mây Ngải Thầu – Bản Choản Thèn – Về Hà Nội', desc: 'Check-in biển mây và nhà Trình Tường, chiều về lại thủ đô.' }
    ],
    included: ['Toàn bộ chi phí xe cộ di chuyển', 'Ăn uống ngủ nghỉ tại Y Tý', 'Điều phối viên giàu kinh nghiệm', 'Bảo hiểm du lịch'],
    preparation: ['Áo siêu ấm (Y Tý mùa đông dưới 5°C)', 'Mũ len & găng tay', 'Tấm lòng nhiệt thành']
  },

  // --- CATEGORY 5: TOUR GẦN HÀ NỘI (NEAR HANOI) ---
  {
    id: 16,
    title: 'Trekking Vườn Quốc Gia Ba Vì – Rừng Thông & Đền Thượng',
    category: 'near_hanoi',
    subCategory: 'near_hanoi',
    categoryName: 'Tour gần Hà Nội',
    duration: '1 ngày',
    location: 'Hà Nội – Ba Vì',
    price: '790.000đ/người',
    priceNum: 790000,
    rating: 4.9,
    reviews: 112,
    image: 'https://images.unsplash.com/photo-1448375240586-882707db888b?auto=format&fit=crop&w=800&q=80',
    badge: 'Tour gần Hà Nội',
    altitudeBadge: '🌿 1.296m',
    altitude: '1.296m',
    trekDistance: '8 km',
    difficultyLevel: 1,
    difficultyText: 'Nhẹ nhàng - Trong ngày',
    description: 'Trekking khám phá nhà thờ đổ Ba Vì rêu phong huyền bí, dạo bước giữa rừng thông ngút ngàn và leo lên đỉnh Đền Thượng chiêm bái Đức Thánh Tản Viên.',
    departureDates: ['25/10/2026', '01/11/2026', '08/11/2026', '15/11/2026'],
    isFeatured: false,
    highlights: [
      'Chạm mốc Đền Thượng trên đỉnh Ba Vì 1.296m quanh năm mây mù bao phủ.',
      'Check-in nhà thờ cổ đổ rêu phong và vườn xương rồng độc đáo.',
      'Thưởng thức gà đồi nướng mọi và cơm lam nóng giòn giữa rừng thông.'
    ],
    itinerary: [
      { day: '07:00', title: 'Hà Nội – Vườn Quốc Gia Ba Vì', desc: 'Xuất phát từ trung tâm Hà Nội chỉ mất 1h15 di chuyển.' },
      { day: '08:30', title: 'Trekking rừng thông & Nhà thờ đổ', desc: 'Đi bộ dưới tán thông xanh mướt, check-in di tích kiến trúc Pháp cổ.' },
      { day: '11:00', title: 'Chinh phục Đền Thượng 1.296m', desc: 'Leo hơn 500 bậc đá lên chiêm bái đền Thánh Tản Viên.' },
      { day: '12:30', title: 'Tiệc nướng BBQ giữa rừng', desc: 'Thưởng thức bữa trưa gà đồi Ba Vì nướng than hoa thơm lừng.' },
      { day: '17:00', title: 'Về lại Hà Nội', desc: 'Về đến Hà Nội khoảng 18:30, sẵn sàng cho tuần làm việc mới.' }
    ],
    included: ['Xe du lịch đời mới khứ hồi', 'Vé vào cổng Vườn Quốc Gia Ba Vì', 'Bữa trưa BBQ gà đồi thịnh soạn', 'Leader đồng hành hỗ trợ chụp ảnh', 'Bảo hiểm du lịch', 'Nước uống suốt chuyến đi'],
    preparation: ['Giày thể thao êm chân', 'Trang phục vận động thoải mái', 'Bình nước cá nhân & áo khoác gió mỏng']
  },
  {
    id: 17,
    title: 'Chinh phục Núi Hàm Lợn Sóc Sơn – Cắm Trại Hồ Suối Bàu',
    category: 'near_hanoi',
    subCategory: 'near_hanoi',
    categoryName: 'Tour gần Hà Nội',
    duration: '1 ngày',
    location: 'Hà Nội – Sóc Sơn',
    price: '650.000đ/người',
    priceNum: 650000,
    rating: 4.8,
    reviews: 86,
    image: 'https://images.unsplash.com/photo-1518548419970-58e3b4079ab2?auto=format&fit=crop&w=800&q=80',
    badge: 'Tour gần Hà Nội',
    altitudeBadge: '⛰️ 462m',
    altitude: '462m',
    trekDistance: '9 km',
    difficultyLevel: 2,
    difficultyText: 'Nhẹ - Thể lực',
    description: 'Chinh phục "nóc nhà thủ đô" đỉnh Hàm Lợn 462m, rèn luyện thể lực qua suối đá và cắm trại chill bên bờ hồ Suối Bàu thơ mộng.',
    departureDates: ['26/10/2026', '02/11/2026', '09/11/2026'],
    isFeatured: false,
    highlights: ['Vượt cung suối đá rèn luyện kỹ năng trekking cơ bản.', 'Chạm đỉnh Hàm Lợn ngắm toàn cảnh hồ nước rừng keo xanh biếc.', 'Tiệc nướng BBQ thịt xiên cơm lam bên hồ Suối Bàu.'],
    itinerary: [
      { day: '07:30', title: 'Hà Nội – Chân núi Hàm Lợn', desc: 'Đoàn tập trung, khởi động và nhận gậy trekking.' },
      { day: '08:30', title: 'Trekking cung suối đá mạo hiểm nhẹ', desc: 'Thử thách vượt ghềnh đá, rèn luyện sự dẻo dai và thăng bằng.' },
      { day: '11:30', title: 'Chạm đỉnh Hàm Lợn 462m', desc: 'Nghỉ ngơi, ngắm cảnh và chụp ảnh check-in đỉnh núi.' },
      { day: '13:00', title: 'Hạ trại BBQ bên bờ hồ Suối Bàu', desc: 'Thưởng thức đồ nướng, cà phê chill và ngắm hoàng hôn buông xuống mặt hồ.' },
      { day: '17:30', title: 'Về lại Hà Nội', desc: 'Về tới nội thành lúc 18:45.' }
    ],
    included: ['Xe đưa đón trọn gói từ trung tâm Hà Nội', 'Bữa trưa BBQ phong phú', 'Lều trại nghỉ trưa bên hồ', 'Leader dẫn đoàn kinh nghiệm', 'Bảo hiểm du lịch'],
    preparation: ['Giày có độ bám tốt (có đoạn qua suối)', 'Quần áo dễ vận động', 'Quần áo dự phòng thay nếu dính nước']
  },
  {
    id: 18,
    title: 'Khám phá Quần Thể Núi Trầm – Chùa Trầm An Nhiên',
    category: 'near_hanoi',
    subCategory: 'near_hanoi',
    categoryName: 'Tour gần Hà Nội',
    duration: '1 ngày',
    location: 'Hà Nội – Chương Mỹ',
    price: '590.000đ/người',
    priceNum: 590000,
    rating: 4.8,
    reviews: 58,
    image: 'https://images.unsplash.com/photo-1509316975850-ff9c5deb0cd9?auto=format&fit=crop&w=800&q=80',
    badge: 'Tour gần Hà Nội',
    altitudeBadge: '⛰️ Cao nguyên đá',
    altitude: '180m',
    trekDistance: '5 km',
    difficultyLevel: 1,
    difficultyText: 'Nhẹ nhàng',
    description: 'Chinh phục "cao nguyên đá thu nhỏ" giữa lòng Hà Nội với các mỏm đá vôi trắng kỳ vĩ, viếng Chùa Trầm cổ kính và dã ngoại picnic cuối tuần.',
    departureDates: ['01/11/2026', '15/11/2026'],
    isFeatured: false,
    highlights: ['Vách núi đá vôi trắng muốt tựa cao nguyên đá Hà Giang thu nhỏ.', 'Viếng Chùa Trầm và Động Long Tiên trầm mặc.', 'Không gian dã ngoại cuối tuần thư thái gần Hà Nội.'],
    itinerary: [
      { day: '08:00', title: 'Hà Nội – Núi Trầm Chương Mỹ', desc: 'Chỉ cách trung tâm Hà Nội 25km.' },
      { day: '09:00', title: 'Trekking các mỏm đá trắng Núi Trầm', desc: 'Chinh phục đỉnh núi đá ngắm toàn cảnh đồng quê bình yên.' },
      { day: '12:00', title: 'Bữa trưa picnic thảm cỏ', desc: 'Dùng cơm nắm muối vừng, gà quay và trái cây tươi.' },
      { day: '14:30', title: 'Thăm Chùa Trầm cổ kính – Về Hà Nội', desc: 'Tìm hiểu lịch sử ngôi chùa cổ, về Hà Nội lúc 17:00.' }
    ],
    included: ['Xe du lịch khứ hồi', 'Bữa trưa picnic dã ngoại', 'Hướng dẫn viên nhiệt tình', 'Bảo hiểm du lịch'],
    preparation: ['Giày thể thao có đế bám đá', 'Nón nón che nắng', 'Nước uống cá nhân']
  }
];

// ==========================================
// 2. DEPARTURE SCHEDULE WIDGET DATA
// ==========================================
const DEPARTURE_SCHEDULE = [
  {
    id: 'sch-1',
    day: '26',
    month: 'Th10',
    title: 'Tà Xùa – Săn mây',
    duration: '2 ngày 1 đêm',
    price: '1.850.000đ',
    priceNum: 1850000,
    dateFull: '26/10/2026',
    status: 'Còn chỗ',
    tourId: 2
  },
  {
    id: 'sch-2',
    day: '01',
    month: 'Th11',
    title: 'Yên Tử – Chùa Đồng',
    duration: '1 ngày',
    price: '1.200.000đ',
    priceNum: 1200000,
    dateFull: '01/11/2026',
    status: 'Còn chỗ',
    tourId: 1
  },
  {
    id: 'sch-3',
    day: '08',
    month: 'Th11',
    title: 'Phu Sa Phin',
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
    title: 'Tà Chì Nhù',
    duration: '2 ngày 1 đêm',
    price: '1.850.000đ',
    priceNum: 1850000,
    dateFull: '15/11/2026',
    status: 'Còn chỗ',
    tourId: 2
  },
  {
    id: 'sch-5',
    day: '22',
    month: 'Th11',
    title: 'Kỳ Quan San',
    duration: '3 ngày 2 đêm',
    price: '2.650.000đ',
    priceNum: 2650000,
    dateFull: '22/11/2026',
    status: 'Còn chỗ',
    tourId: 4
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
    comment: '“Cung đường đẹp, hướng dẫn viên nhiệt tình, đồ ăn ngon. Cảm ơn ĐI CÙNG GIÓ đã cho mình một hành trình thật đáng nhớ!”',
    rating: 5
  },
  {
    id: 2,
    name: 'Lê Minh Đức',
    role: 'Trekking Phu Sa Phin',
    avatar: 'assets/images/avatar-duc.jpg',
    comment: '“Lần đầu đi trekking mà được trải nghiệm nhiều điều tuyệt vời như vậy. Nhóm rất vui, đoàn kết. Sẽ quay lại cùng ĐI CÙNG GIÓ!”',
    rating: 5
  },
  {
    id: 3,
    name: 'Trần Thị Mai',
    role: 'Hành hương Yên Tử',
    avatar: 'assets/images/avatar-mai.jpg',
    comment: '“Hành trình ý nghĩa, vừa được khám phá thiên nhiên vừa học được nhiều điều về Phật pháp. Cảm ơn đội ngũ đã tổ chức chu đáo!”',
    rating: 5
  },
  {
    id: 4,
    name: 'Hoàng Quốc Bảo',
    role: 'Chinh phục Kỳ Quan San',
    avatar: 'assets/images/avatar-duc.jpg',
    comment: '“Đỉnh Bạch Mộc Lương Tử quá đẹp! Biển mây đồi Muối lúc bình minh khiến mình nổi da gà vì quá hùng vĩ. Porter gùi đồ rất khỏe và thân thiện.”',
    rating: 5
  },
  {
    id: 5,
    name: 'Đặng Thảo Linh',
    role: 'Thiện nguyện Mù Cang Chải',
    avatar: 'assets/images/avatar-ha.jpg',
    comment: '“Chuyến đi nhiều cảm xúc nhất từ trước tới nay của mình. Nụ cười của các em nhỏ khi nhận áo ấm làm tan chảy cái rét mùa đông vùng cao.”',
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
    // Show 4 tours matching the chosen category
    filtered = TOURS_DATA.filter(t => t.category === filterCategory || t.subCategory === filterCategory);
  }

  // Fallback to top 4 if empty
  if (filtered.length === 0) {
    filtered = TOURS_DATA.slice(0, 4);
  } else if (filtered.length > 4) {
    filtered = filtered.slice(0, 4);
  }

  container.innerHTML = filtered.map(tour => {
    const isLiked = wishlist.has(tour.id);
    return `
      <div class="tour-card bg-white rounded-2xl overflow-hidden border border-gray-100 shadow-sm flex flex-col justify-between group">
        
        <!-- Tour Image Container (Zoom on hover + Centered Action Pill) -->
        <div class="relative overflow-hidden aspect-[4/3] bg-gray-100 cursor-pointer" onclick="openTourDetailModal(${tour.id})">
          <img 
            src="${tour.image}" 
            alt="${tour.title}" 
            loading="lazy"
            onerror="this.src='assets/images/tour-ta-xua.jpg'"
            class="tour-card-image w-full h-full object-cover"
          />
          
          <!-- Category Badge (Top Left with Glassmorphism) -->
          <div class="absolute top-3 left-3 z-10">
            <span class="backdrop-blur-md bg-[#1E4D3B]/85 text-white text-[11px] font-bold px-2.5 py-1 rounded-full shadow-sm">
              ${tour.badge}
            </span>
          </div>

          <!-- Subtle Altitude Badge (Top Center/Right) -->
          <div class="absolute top-3 left-24 z-10">
            <span class="backdrop-blur-md bg-black/40 text-white text-[10px] font-semibold px-2 py-0.5 rounded-md shadow-sm">
              ${tour.altitudeBadge}
            </span>
          </div>

          <!-- Hover Overlay with Small "Xem chi tiết hành trình" button -->
          <div class="absolute inset-0 bg-black/35 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center p-4 pointer-events-none">
            <span class="px-3.5 py-1.5 rounded-full bg-white/95 text-forest text-xs font-bold shadow-lg backdrop-blur-sm transform translate-y-2 group-hover:translate-y-0 transition-transform duration-300 flex items-center gap-1.5">
              <i data-lucide="eye" class="w-3.5 h-3.5 text-forest"></i>
              <span>Xem chi tiết</span>
            </span>
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
            <!-- Compact Meta Details above title -->
            <div class="flex items-center justify-between text-[11px] text-gray-500 mb-1.5">
              <span class="flex items-center gap-1">
                <i data-lucide="map-pin" class="w-3 h-3 text-forest shrink-0"></i>
                <span class="truncate max-w-[130px]">${tour.location}</span>
              </span>
              <span class="flex items-center gap-1 font-medium">
                <i data-lucide="clock" class="w-3 h-3 text-gray-400 shrink-0"></i>
                <span>${tour.duration}</span>
              </span>
            </div>

            <!-- Title: 2 lines with consistent height, fully readable -->
            <h3 
              class="font-bold text-gray-900 text-[13.5px] xl:text-[14px] leading-snug line-clamp-2 min-h-[38px] tracking-tight group-hover:text-forest transition-colors cursor-pointer" 
              onclick="openTourDetailModal(${tour.id})" 
              title="${tour.title}"
            >
              ${tour.title}
            </h3>

            <!-- Price -->
            <div class="mt-2.5">
              <span class="text-[15px] font-extrabold text-forest whitespace-nowrap">${tour.price}</span>
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
              onclick="openSmartBookingModal(${tour.id})"
              class="btn-shine whitespace-nowrap px-3.5 py-1.5 rounded-lg bg-[#1E4D3B] text-white text-xs font-semibold shrink-0 hover:bg-forest/90 active:scale-95 transition-all shadow-sm"
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
      onclick="openSmartBookingModal(${item.tourId}, '${item.dateFull}')"
      class="schedule-row p-3 rounded-xl bg-gray-50/70 border border-gray-100/80 flex items-center justify-between gap-3 cursor-pointer group"
      title="Nhấn để xem chi tiết & đăng ký tour này"
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
// 10. RICH TOUR DETAIL MODAL CONTROLLER
// ==========================================
function openTourDetailModal(tourId) {
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
        <img src="${tour.image}" alt="${tour.title}" class="w-full h-full object-cover">
        <div class="absolute inset-0 bg-gradient-to-t from-black/85 via-black/40 to-transparent"></div>
        
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
          <p class="text-xs sm:text-sm text-gray-200 mt-1 flex items-center gap-2">
            <i data-lucide="map-pin" class="w-3.5 h-3.5 text-emerald-300"></i>
            <span>${tour.location}</span>
          </p>
        </div>
      </div>

      <!-- Trekking Key Specs Bar -->
      <div class="grid grid-cols-4 gap-2 px-5 py-3.5 bg-[#F6F7F2] border-b border-gray-100 text-center shrink-0">
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
          <span class="block text-[10px] font-bold uppercase tracking-wider text-gray-500">Xuất phát</span>
          <span class="block text-xs sm:text-sm font-extrabold text-gray-900 mt-0.5">Hà Nội</span>
        </div>
      </div>

      <!-- Tab Navigation -->
      <div class="px-5 pt-3 border-b border-gray-100 flex items-center gap-6 text-xs sm:text-sm shrink-0">
        <button type="button" onclick="switchDetailTab(1)" id="tab-btn-1" class="modal-tab-btn active cursor-pointer">
          1. Điểm nhấn hành trình
        </button>
        <button type="button" onclick="switchDetailTab(2)" id="tab-btn-2" class="modal-tab-btn cursor-pointer">
          2. Lịch trình chi tiết
        </button>
        <button type="button" onclick="switchDetailTab(3)" id="tab-btn-3" class="modal-tab-btn cursor-pointer">
          3. Chuẩn bị & Vật dụng
        </button>
      </div>

      <!-- Tab Content Panels (Scrollable) -->
      <div class="p-5 sm:p-6 overflow-y-auto flex-1 space-y-4 text-xs sm:text-sm text-gray-700 leading-relaxed">
        
        <!-- PANEL 1: Điểm nhấn hành trình -->
        <div id="tab-panel-1" class="space-y-4">
          <p class="text-gray-700 leading-relaxed">${tour.description}</p>
          
          <div class="space-y-2.5">
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

          <div class="p-3 bg-emerald-50/70 rounded-xl border border-emerald-100 flex items-center justify-between">
            <div>
              <span class="text-xs font-bold text-forest block">Lịch khởi hành sắp tới:</span>
              <span class="text-xs text-gray-600 font-medium">${dates}</span>
            </div>
            <span class="badge-seat text-xs">Còn chỗ</span>
          </div>
        </div>

        <!-- PANEL 2: Lịch trình chi tiết -->
        <div id="tab-panel-2" class="hidden space-y-4">
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

        <!-- PANEL 3: Chuẩn bị & Vật dụng -->
        <div id="tab-panel-3" class="hidden space-y-4">
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
            <span>Đăng ký hành trình này ngay</span>
            <i data-lucide="arrow-right" class="w-4 h-4"></i>
          </button>
        </div>
      </div>

    </div>
  `;

  modal.classList.remove('hidden');
  document.body.style.overflow = 'hidden';
  initLucideIcons();
}

function closeTourDetailModal() {
  const modal = document.getElementById('tour-detail-modal');
  if (modal) {
    modal.classList.add('hidden');
    document.body.style.overflow = '';
  }
}

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
};

// ==========================================
// 11. SMART BOOKING MODAL WITH LIVE CALCULATOR
// ==========================================
function openSmartBookingModal(tourId = 1, defaultDate = '') {
  currentBookingTour = TOURS_DATA.find(t => t.id === tourId) || TOURS_DATA[0];
  bookingGuests = 1;

  const modal = document.getElementById('booking-modal');
  if (!modal) return;

  // Populate tour select options
  const tourSelect = document.getElementById('booking-tour-select');
  if (tourSelect) {
    tourSelect.innerHTML = TOURS_DATA.map(t => `
      <option value="${t.id}" ${t.id === currentBookingTour.id ? 'selected' : ''}>
        ${t.title} (${t.duration}) – ${t.price}
      </option>
    `).join('');
  }

  // Populate date
  const dateInput = document.getElementById('booking-date-input');
  if (dateInput) {
    dateInput.value = defaultDate || (currentBookingTour.departureDates ? currentBookingTour.departureDates[0] : '26/10/2026');
  }

  // Reset form & confirmation view
  const formBox = document.getElementById('booking-form-box');
  const successBox = document.getElementById('booking-success-box');
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

// Real-time price calculation logic
function updateBookingCalculation() {
  if (!currentBookingTour) return;

  const countInput = document.getElementById('booking-guests-count');
  if (countInput) countInput.textContent = bookingGuests;

  const subtotal = currentBookingTour.priceNum * bookingGuests;
  const isGroupDiscount = bookingGuests >= 4;
  const discount = isGroupDiscount ? Math.round(subtotal * 0.05) : 0;
  const finalTotal = subtotal - discount;

  const summaryContainer = document.getElementById('booking-summary-box');
  if (summaryContainer) {
    summaryContainer.innerHTML = `
      <div class="p-3.5 rounded-2xl bg-[#F6F7F2] border border-gray-200/80 space-y-2 text-xs">
        <div class="flex items-center justify-between text-gray-600">
          <span>Đơn giá mỗi khách:</span>
          <span class="font-bold text-gray-800">${formatCurrency(currentBookingTour.priceNum)}</span>
        </div>
        <div class="flex items-center justify-between text-gray-600">
          <span>Tạm tính (${bookingGuests} người):</span>
          <span class="font-bold text-gray-800">${formatCurrency(subtotal)}</span>
        </div>
        
        ${isGroupDiscount ? `
          <div class="flex items-center justify-between text-emerald-700 bg-emerald-100/60 p-1.5 rounded-lg font-semibold">
            <span>🎉 Ưu đãi nhóm (≥4 người):</span>
            <span>-5% (-${formatCurrency(discount)})</span>
          </div>
        ` : ''}

        <div class="pt-2 border-t border-gray-200 flex items-center justify-between text-sm">
          <span class="font-bold text-gray-900">Tổng thanh toán dự kiến:</span>
          <span class="text-base font-black text-forest">${formatCurrency(finalTotal)}</span>
        </div>
      </div>
    `;
  }
}

function adjustBookingGuests(delta) {
  bookingGuests = Math.max(1, Math.min(20, bookingGuests + delta));
  updateBookingCalculation();
}

function setupBookingModalEvents() {
  const tourSelect = document.getElementById('booking-tour-select');
  tourSelect?.addEventListener('change', (e) => {
    const selectedId = parseInt(e.target.value);
    currentBookingTour = TOURS_DATA.find(t => t.id === selectedId) || TOURS_DATA[0];
    
    // Auto-update departure date
    const dateInput = document.getElementById('booking-date-input');
    if (dateInput && currentBookingTour.departureDates) {
      dateInput.value = currentBookingTour.departureDates[0];
    }
    updateBookingCalculation();
  });

  const form = document.getElementById('booking-form');
  form?.addEventListener('submit', (e) => {
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
      showToast('Đăng ký thành công!', `Mã booking ${randomCode} đã được khởi tạo.`, 'success');
    }
  });
}

// ==========================================
// 12. WISHLIST & CART DRAWER CONTROLLER
// ==========================================
function toggleWishlist(tourId, event) {
  if (event) {
    event.stopPropagation();
  }

  const tour = TOURS_DATA.find(t => t.id === tourId);
  const title = tour ? tour.title : 'Tour';

  if (wishlist.has(tourId)) {
    wishlist.delete(tourId);
    showToast('Đã xóa khỏi yêu thích', `Đã bỏ "${title}" khỏi danh sách quan tâm.`);
  } else {
    wishlist.add(tourId);
    showToast('Đã lưu tour yêu thích!', `Đã thêm "${title}" vào danh sách quan tâm của bạn.`, 'success');
  }

  try {
    localStorage.setItem('dicunggio_wishlist', JSON.stringify(Array.from(wishlist)));
  } catch (e) {
    // ignore
  }

  updateWishlistBadges();
  renderTours(currentCategory);
}

function updateWishlistBadges() {
  const count = wishlist.size;
  const badges = document.querySelectorAll('.wishlist-counter-badge');
  badges.forEach(badge => {
    badge.textContent = count;
  });
}

function openWishlistDrawer() {
  const drawer = document.getElementById('wishlist-drawer');
  const overlay = document.getElementById('drawer-overlay');
  const container = document.getElementById('wishlist-items-container');
  if (!drawer || !overlay) return;

  const savedTours = TOURS_DATA.filter(t => wishlist.has(t.id));

  if (savedTours.length === 0) {
    container.innerHTML = `
      <div class="text-center py-12 space-y-3">
        <div class="w-12 h-12 rounded-full bg-gray-100 flex items-center justify-center mx-auto text-gray-400">
          <i data-lucide="heart" class="w-6 h-6"></i>
        </div>
        <h4 class="text-sm font-bold text-gray-700">Chưa có tour nào được lưu</h4>
        <p class="text-xs text-gray-400 max-w-[200px] mx-auto">Nhấn biểu tượng trái tim trên các thẻ tour để lưu hành trình bạn yêu thích.</p>
      </div>
    `;
  } else {
    container.innerHTML = savedTours.map(tour => `
      <div class="p-3 bg-gray-50 rounded-2xl border border-gray-100 flex items-center gap-3 group">
        <img src="${tour.image}" alt="${tour.title}" class="w-16 h-16 rounded-xl object-cover shrink-0">
        <div class="flex-1 min-w-0">
          <h4 class="text-xs font-bold text-gray-900 truncate">${tour.title}</h4>
          <span class="text-xs font-extrabold text-forest block mt-0.5">${tour.price}</span>
          <div class="flex items-center gap-2 mt-2">
            <button 
              onclick="openSmartBookingModal(${tour.id}); closeWishlistDrawer();"
              class="text-[11px] bg-forest text-white px-3 py-1 rounded-full font-bold hover:bg-forest/90 cursor-pointer"
            >
              Đăng ký ngay
            </button>
            <button 
              onclick="toggleWishlist(${tour.id}); openWishlistDrawer();"
              class="text-[11px] text-red-500 hover:underline cursor-pointer"
            >
              Xóa
            </button>
          </div>
        </div>
      </div>
    `).join('');
  }

  drawer.classList.remove('translate-x-full');
  overlay.classList.remove('hidden');
  document.body.style.overflow = 'hidden';
  initLucideIcons();
}

function closeWishlistDrawer() {
  const drawer = document.getElementById('wishlist-drawer');
  const overlay = document.getElementById('drawer-overlay');
  if (drawer) drawer.classList.add('translate-x-full');
  if (overlay) overlay.classList.add('hidden');
  document.body.style.overflow = '';
}

// ==========================================
// 13. SEARCH OVERLAY MODAL
// ==========================================
function openSearchModal() {
  const modal = document.getElementById('search-modal');
  const input = document.getElementById('search-input');
  if (!modal) return;

  modal.classList.remove('hidden');
  document.body.style.overflow = 'hidden';
  setTimeout(() => input?.focus(), 100);
  handleSearchInput('');
}

function closeSearchModal() {
  const modal = document.getElementById('search-modal');
  if (modal) {
    modal.classList.add('hidden');
    document.body.style.overflow = '';
  }
}

function handleSearchInput(query) {
  const container = document.getElementById('search-results-container');
  if (!container) return;

  const q = query.toLowerCase().trim();
  const results = q ? TOURS_DATA.filter(t => 
    t.title.toLowerCase().includes(q) || 
    t.location.toLowerCase().includes(q) ||
    t.categoryName.toLowerCase().includes(q)
  ) : TOURS_DATA.slice(0, 5);

  if (results.length === 0) {
    container.innerHTML = `
      <div class="py-8 text-center text-xs text-gray-400">
        Không tìm thấy hành trình nào với từ khóa "${query}".
      </div>
    `;
    return;
  }

  container.innerHTML = results.map(tour => `
    <div 
      onclick="openTourDetailModal(${tour.id}); closeSearchModal();"
      class="p-3 hover:bg-emerald-50/60 rounded-xl cursor-pointer flex items-center justify-between gap-3 border border-transparent hover:border-emerald-100 transition-colors"
    >
      <div class="flex items-center gap-3 min-w-0">
        <img src="${tour.image}" alt="${tour.title}" class="w-12 h-12 rounded-lg object-cover shrink-0">
        <div class="min-w-0">
          <h4 class="text-xs font-bold text-gray-900 truncate">${tour.title}</h4>
          <span class="text-[11px] text-gray-500">${tour.location} • ${tour.duration}</span>
        </div>
      </div>
      <span class="text-xs font-bold text-forest whitespace-nowrap shrink-0">${tour.price}</span>
    </div>
  `).join('');
}

// ==========================================
// 14. VIDEO LIGHTBOX MODAL
// ==========================================
function openVideoModal() {
  const modal = document.getElementById('video-modal');
  const frame = document.getElementById('video-frame');
  if (!modal || !frame) return;

  // Majestic Vietnam Mountain Trekking Flycam Video
  frame.src = 'https://www.youtube-nocookie.com/embed/g6b4WfN3Kqw?autoplay=1&rel=0&modestbranding=1';
  modal.classList.remove('hidden');
  document.body.style.overflow = 'hidden';
}

function closeVideoModal() {
  const modal = document.getElementById('video-modal');
  const frame = document.getElementById('video-frame');
  if (frame) frame.src = '';
  if (modal) modal.classList.add('hidden');
  document.body.style.overflow = '';
}

// ==========================================
// 15. REVIEWS / TESTIMONIALS MODAL
// ==========================================
function openReviewsModal() {
  const modal = document.getElementById('reviews-modal');
  const listContainer = document.getElementById('reviews-list-container');
  if (!modal || !listContainer) return;

  listContainer.innerHTML = TESTIMONIALS_DATA.map(rev => `
    <div class="p-4 bg-gray-50 rounded-2xl border border-gray-100 space-y-2">
      <div class="flex items-center gap-3">
        <img src="${rev.avatar}" alt="${rev.name}" class="w-10 h-10 rounded-full object-cover border border-emerald-100">
        <div>
          <h4 class="text-xs font-bold text-gray-900 leading-tight">${rev.name}</h4>
          <span class="text-[10px] text-forest font-medium">${rev.role}</span>
        </div>
      </div>
      <p class="text-xs text-gray-700 italic leading-relaxed">${rev.comment}</p>
      <div class="flex text-amber-400">
        ${'<i data-lucide="star" class="w-3 h-3 fill-amber-400 text-amber-400"></i>'.repeat(rev.rating)}
      </div>
    </div>
  `).join('');

  modal.classList.remove('hidden');
  document.body.style.overflow = 'hidden';
  initLucideIcons();
}

function closeReviewsModal() {
  const modal = document.getElementById('reviews-modal');
  if (modal) {
    modal.classList.add('hidden');
    document.body.style.overflow = '';
  }
}

function submitNewReview(event) {
  event.preventDefault();
  const name = document.getElementById('review-input-name')?.value;
  const tour = document.getElementById('review-input-tour')?.value;
  const comment = document.getElementById('review-input-comment')?.value;

  if (!name || !comment) return;

  TESTIMONIALS_DATA.unshift({
    id: Date.now(),
    name: name,
    role: tour || 'Trekking Việt Nam',
    avatar: 'assets/images/avatar-duc.jpg',
    comment: `“${comment}”`,
    rating: 5
  });

  closeReviewsModal();
  showToast('Cảm ơn bạn!', 'Cảm nhận chuyến đi của bạn đã được ghi nhận thành công.', 'success');
}

// ==========================================
// 16. TOAST NOTIFICATIONS
// ==========================================
function showToast(title, message, type = 'info') {
  const container = document.getElementById('toast-container');
  if (!container) return;

  const id = 'toast-' + Date.now();
  const toast = document.createElement('div');
  toast.id = id;
  toast.className = 'toast-slide-in pointer-events-auto bg-white rounded-2xl p-4 shadow-xl border border-gray-100 flex items-start gap-3 max-w-sm w-full transition-all duration-300';

  let icon = '<i data-lucide="info" class="w-5 h-5 text-forest"></i>';
  if (type === 'success') {
    icon = '<i data-lucide="check-circle" class="w-5 h-5 text-emerald-600"></i>';
  } else if (type === 'error') {
    icon = '<i data-lucide="alert-circle" class="w-5 h-5 text-red-500"></i>';
  }

  toast.innerHTML = `
    <div class="shrink-0 mt-0.5">${icon}</div>
    <div class="flex-1 min-w-0">
      <h4 class="text-xs font-bold text-gray-900 leading-tight">${title}</h4>
      <p class="text-xs text-gray-500 mt-0.5 leading-snug">${message}</p>
    </div>
    <button onclick="document.getElementById('${id}')?.remove()" class="text-gray-400 hover:text-gray-600 p-1">
      <i data-lucide="x" class="w-4 h-4"></i>
    </button>
  `;

  container.appendChild(toast);
  initLucideIcons();

  setTimeout(() => {
    toast.style.opacity = '0';
    toast.style.transform = 'translateX(50px)';
    setTimeout(() => toast.remove(), 300);
  }, 4000);
}

// ==========================================
// 17. SCROLL OBSERVERS & MICRO-INTERACTIONS
// ==========================================
function setupScrollReveal() {
  const elements = document.querySelectorAll('.reveal-on-scroll');
  if (!elements.length) return;

  const observer = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('revealed');
        obs.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

  elements.forEach(el => observer.observe(el));
}

function setupScrollSpy() {
  const navLinks = document.querySelectorAll('.nav-link');
  const sections = ['home', 'tours-section', 'schedule-section', 'why-us-section', 'about-section', 'testimonials-section', 'contact-section'];

  window.addEventListener('scroll', () => {
    const scrollPos = window.scrollY + 130;

    sections.forEach(id => {
      const el = document.getElementById(id);
      if (!el) return;
      const top = el.offsetTop;
      const height = el.offsetHeight;

      if (scrollPos >= top && scrollPos < top + height) {
        navLinks.forEach(link => {
          if (link.getAttribute('href') === `#${id}`) {
            link.classList.add('active');
          } else {
            link.classList.remove('active');
          }
        });
      }
    });
  });
}

function setupNavbarGlass() {
  const header = document.querySelector('header');
  const backToTop = document.getElementById('back-to-top');

  window.addEventListener('scroll', () => {
    if (window.scrollY > 40) {
      header?.classList.add('header-glass');
    } else {
      header?.classList.remove('header-glass');
    }

    if (window.scrollY > 450) {
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
  form?.addEventListener('submit', (e) => {
    e.preventDefault();
    const input = document.getElementById('newsletter-email');
    if (input && input.value) {
      showToast('Đăng ký nhận tin', 'Đăng ký nhận lịch khởi hành sớm thành công! Chúng tôi sẽ gửi thông báo mới nhất tới email của bạn.', 'success');
      form.reset();
    }
  });
}
