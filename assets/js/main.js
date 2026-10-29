/**
 * ĐI CÙNG GIÓ - Interactive Prototype Engine
 * "Hẹn nhau trên những đỉnh núi"
 */

// Tour data repository
const TOURS_DATA = [
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
    description: 'Hành trình leo núi thiêng Yên Tử, chiêm bái Chùa Đồng trên đỉnh Phù Vân, rèn luyện thể lực và tìm lại an yên trong tâm hồn giữa mây ngàn.',
    departureDates: ['01/11/2026', '08/11/2026', '15/11/2026'],
    difficulty: 'Trung bình',
    isFeatured: true
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
    description: 'Chinh phục "sống lưng khủng long" huyền thoại, đắm chìm trong biển mây bồng bềnh lúc bình minh và tận hưởng bầu không khí Tây Bắc se lạnh.',
    departureDates: ['26/10/2026', '02/11/2026', '09/11/2026'],
    difficulty: 'Dễ - Trung bình',
    isFeatured: true
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
    description: 'Cung đường hoang sơ đầy thách thức với những vách đá hùng vĩ, thảm thực vật đỗ quyên nguyên sinh và tầm nhìn panorama ngoạn mục.',
    departureDates: ['08/11/2026', '22/11/2026'],
    difficulty: 'Khá thách thức',
    isFeatured: true
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
    description: 'Chinh phục đỉnh núi cao thứ 4 Việt Nam (3.046m), ngắm đồi Muối lung linh dưới ánh sao đêm và biển mây ngút ngàn tầm mắt.',
    departureDates: ['22/11/2026', '06/12/2026'],
    difficulty: 'Thử thách cao',
    isFeatured: true
  },
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
    image: 'https://images.unsplash.com/photo-1518548419970-58e3b4079ab2?auto=format&fit=crop&w=800&q=80',
    badge: 'Tâm linh',
    description: 'Chuyến hành hương tìm về cõi Phật thanh tịnh giữa non nước Ninh Bình - Hà Nam, du thuyền trên hồ Lục Nhạc và viếng chùa Tam Chúc.',
    departureDates: ['01/11/2026', '15/11/2026'],
    difficulty: 'Nhẹ nhàng',
    isFeatured: false
  },
  {
    id: 6,
    title: 'Mai Châu – Mộc Châu: Mùa Hoa Cải Trắng',
    category: 'experience',
    subCategory: 'experience',
    categoryName: 'Trải nghiệm',
    duration: '2 ngày 1 đêm',
    location: 'Hà Nội – Hòa Bình – Sơn La',
    price: '1.450.000đ/người',
    priceNum: 1450000,
    rating: 4.9,
    reviews: 65,
    image: 'https://images.unsplash.com/photo-1528127269322-539801943592?auto=format&fit=crop&w=800&q=80',
    badge: 'Trải nghiệm',
    description: 'Trải nghiệm nét đẹp văn hóa người Thái ở Bản Lác, ngắm mùa hoa cải trắng tinh khôi Mộc Châu và đốt lửa trại giữa thung lũng đại ngàn.',
    departureDates: ['07/11/2026', '21/11/2026'],
    difficulty: 'Gia đình & Bạn bè',
    isFeatured: false
  },
  {
    id: 7,
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
    description: 'Hành trình ý nghĩa mang hơi ấm mùa đông đến cho các em nhỏ vùng cao La Pán Tẩn, kết hợp giao lưu văn nghệ và ngắm mùa vàng ruộng bậc thang.',
    departureDates: ['14/11/2026', '28/11/2026'],
    difficulty: 'Cộng đồng',
    isFeatured: false
  },
  {
    id: 8,
    title: 'Trekking Vườn Quốc Gia Ba Vì – Rừng Thông',
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
    description: 'Trekking khám phá nhà thờ đổ Ba Vì huyền bí, dạo bước giữa rừng thông ngút ngàn và ngắm hoa dã quỳ nở rộ khắp sườn đồi.',
    departureDates: ['25/10/2026', '01/11/2026', '08/11/2026'],
    difficulty: 'Nhẹ nhàng - Trong ngày',
    isFeatured: false
  }
];

// Departure schedule widget data
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
    status: 'Còn chỗ'
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
    status: 'Còn chỗ'
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
    status: 'Còn chỗ'
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
    status: 'Còn chỗ'
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
    status: 'Còn chỗ'
  }
];

// Destinations Data
const DESTINATIONS_DATA = [
  {
    id: 'dest-taxua',
    name: 'Tà Xùa',
    province: 'Sơn La',
    subtitle: 'Thiên đường săn mây',
    altitude: '2.865m',
    level: 'Dễ - Trung bình',
    image: 'assets/images/tour-ta-xua.jpg',
    badge: 'Tây Bắc',
    description: 'Chiêm ngưỡng "sống lưng khủng long" huyền thoại giữa biển mây trắng xoá cuồn cuộn dưới ánh bình minh.',
    categoryFilter: 'trekking'
  },
  {
    id: 'dest-yentu',
    name: 'Yên Tử',
    province: 'Quảng Ninh',
    subtitle: 'Non thiêng mây ngàn',
    altitude: '1.068m',
    level: 'Trung bình',
    image: 'assets/images/tour-yen-tu.jpg',
    badge: 'Đông Bắc',
    description: 'Chinh phục đỉnh Phù Vân, chiêm bái Chùa Đồng linh thiêng trong sương mây huyền ảo và rừng trúc cổ thụ.',
    categoryFilter: 'near_hanoi'
  },
  {
    id: 'dest-kyquansan',
    name: 'Kỳ Quan San',
    province: 'Lào Cai',
    subtitle: 'Bạch Mộc Lương Tử',
    altitude: '3.046m',
    level: 'Thử thách cao',
    image: 'assets/images/tour-ky-quan-san.jpg',
    badge: 'Tây Bắc',
    description: 'Đỉnh núi cao thứ 4 Việt Nam với cung đường sống trâu ngoạn mục, đồi Muối ngắm sao trời và biển mây ngút ngàn.',
    categoryFilter: 'trekking'
  },
  {
    id: 'dest-phusaphin',
    name: 'Phu Sa Phin',
    province: 'Tây Bắc',
    subtitle: 'Chinh phục vách đá',
    altitude: '2.879m',
    level: 'Khá thách thức',
    image: 'assets/images/tour-phu-sa-phin.jpg',
    badge: 'Tây Bắc',
    description: 'Cung đường rừng nguyên sinh hoang sơ với vách đá hùng vĩ, hoa đỗ quyên khoe sắc và phong cảnh ngoạn mục.',
    categoryFilter: 'trekking'
  }
];

// Blog Guides Data
const BLOG_POSTS_DATA = [
  {
    id: 1,
    title: 'Kinh nghiệm săn biển mây Tà Xùa thành công 99% cho người mới',
    category: 'Cẩm nang săn mây',
    readTime: '5 phút đọc',
    date: '28/10/2026',
    author: 'Leader Tuấn Anh',
    image: 'assets/images/tour-ta-xua.jpg',
    excerpt: 'Thời điểm vàng từ tháng 10 đến tháng 4 hàng năm, cách xem dự báo độ ẩm và mẹo chọn góc chụp ảnh đẹp trên sống lưng khủng long.',
    content: `
      <p class="mb-4">Tà Xùa (Bắc Yên, Sơn La) từ lâu đã trở thành "thánh địa săn mây" của các trekker miền Bắc. Để có chuyến đi trọn vẹn với tỉ lệ thấy mây cao nhất, bạn cần nắm vững các kinh nghiệm cốt lõi:</p>
      <h4 class="text-base font-bold text-gray-900 mb-2">1. Thời điểm vàng để săn mây</h4>
      <p class="mb-4">Mùa mây đẹp nhất kéo dài từ tháng 10 đến tháng 4 năm sau. Đặc biệt là những ngày sau đợt không khí lạnh tràn về kèm mưa phùn nhẹ, ngày hôm sau trời hửng nắng ấm – 99% bạn sẽ bắt trọn biển mây bồng bềnh.</p>
      <h4 class="text-base font-bold text-gray-900 mb-2">2. Trang bị cần thiết</h4>
      <p class="mb-4">Nhiệt độ ban đêm và rạng sáng ở Tà Xùa có thể xuống dưới 10 độ C. Hãy mang theo áo gió giữ nhiệt chống nước, giày có gai bám đá tốt, mũ len và găng tay.</p>
      <h4 class="text-base font-bold text-gray-900 mb-2">3. Đi cùng người dẫn đường bản địa</h4>
      <p>Cung đường "sống lưng khủng long" hai bên là vực sâu gió lớn. Đi cùng đội ngũ Leader kinh nghiệm của ĐI CÙNG GIÓ sẽ giúp bạn an tâm tuyệt đối và có những bức ảnh check-in để đời.</p>
    `
  },
  {
    id: 2,
    title: 'Kế hoạch rèn luyện thể lực 4 tuần trước chuyến trekking đầu tiên',
    category: 'Rèn luyện thể lực',
    readTime: '6 phút đọc',
    date: '25/10/2026',
    author: 'HLV Minh Hoàng',
    image: 'assets/images/hero-bg.jpg',
    excerpt: 'Lộ trình chạy bộ cardio, leo cầu thang bộ với balo tạ và bài tập squat tăng sức bền cổ chân giúp bạn chinh phục mọi đỉnh cao mà không mỏi gối.',
    content: `
      <p class="mb-4">Leo núi trekking đòi hỏi sự dẻo dai của cơ đùi, bắp chân và sức bền tim mạch. Với lịch tập 4 tuần sau đây, bạn hoàn toàn có thể tự tin sải bước:</p>
      <h4 class="text-base font-bold text-gray-900 mb-2">Tuần 1-2: Xây dựng nền tảng tim mạch</h4>
      <p class="mb-4">Chạy bộ nhẹ nhàng hoặc đi bộ nhanh 3-5km mỗi buổi (3 buổi/tuần). Tập leo cầu thang bộ thay vì đi thang máy tại nơi làm việc.</p>
      <h4 class="text-base font-bold text-gray-900 mb-2">Tuần 3: Tăng cường sức mạnh cơ chân</h4>
      <p class="mb-4">Thực hiện bài tập Squat, Lunges và Calf Raises mỗi ngày 3 hiệp. Đi bộ dốc với balo nặng 3-5kg để làm quen với cảm giác tải trọng.</p>
      <h4 class="text-base font-bold text-gray-900 mb-2">Tuần 4: Duy trì và nghỉ ngơi phục hồi</h4>
      <p>Giảm tải cường độ, ngủ đủ giấc, nạp đủ protein và uống nhiều nước để cơ thể ở trạng thái sung sức nhất vào ngày xuất phát.</p>
    `
  },
  {
    id: 3,
    title: 'Checklist 12 vật dụng bất ly thân trong balo trekker chuyên nghiệp',
    category: 'Trang bị trekking',
    readTime: '4 phút đọc',
    date: '20/10/2026',
    author: 'Trekker Thu Trang',
    image: 'assets/images/tour-ky-quan-san.jpg',
    excerpt: 'Từ đôi giày trekking chống trượt, gậy leo núi carbon, bình nước giữ nhiệt đến bộ sơ cứu y tế cá nhân – những thứ cứu cánh trên từng cung đường.',
    content: `
      <p class="mb-4">Một chiếc balo được sắp xếp khoa học và đầy đủ vật dụng cần thiết sẽ là người bạn đồng hành tin cậy nhất của bạn:</p>
      <ul class="list-disc pl-5 space-y-2 mb-4">
        <li><strong>Giày trekking:</strong> Đế gai sâu, cổ lửng bảo vệ mắt cá chân, chống trơn trượt trên vách đá sương mù.</li>
        <li><strong>Gậy leo núi:</strong> Giảm 30% áp lực lên đầu gối khi xuống dốc, giữ thăng bằng hiệu quả.</li>
        <li><strong>Đèn pin đội đầu:</strong> Thiết yếu cho các buổi sáng dậy sớm đón bình minh từ 4h sáng.</li>
        <li><strong>Áo mưa & bọc balo:</strong> Thời tiết vùng cao thay đổi rất nhanh, luôn giữ đồ khô ráo.</li>
        <li><strong>Túi y tế:</strong> Băng keo cá nhân, thuốc giảm đau, thuốc cảm, oresol bù nước và xịt chống côn trùng.</li>
        <li><strong>Bình giữ nhiệt:</strong> Một ngụm trà gừng nóng trên đỉnh núi lạnh giá sẽ tiếp thêm 200% năng lượng!</li>
      </ul>
    `
  }
];

// FAQs Data
const FAQS_DATA = [
  {
    q: 'Người chưa từng đi trekking bao giờ có tham gia được không?',
    a: 'Hoàn toàn được! ĐI CÙNG GIÓ thiết kế các cung đường phân cấp rõ ràng từ Dễ (Yên Tử, Ba Vì) đến Trung bình (Tà Xùa). Mỗi đoàn luôn có Leader đi đầu mở đường, Leader chốt đoàn bọc lót phía sau và Porter bản địa hỗ trợ mang vác hành lý chung, đảm bảo bạn luôn an toàn và được hướng dẫn từng bước chân.'
  },
  {
    q: 'Đồ ăn và điều kiện sinh hoạt, ngủ nghỉ trên núi như thế nào?',
    a: 'Chúng tôi luôn chú trọng dinh dưỡng và giấc ngủ cho các thành viên. Bữa tối trên núi luôn là các món ăn nóng hổi thịnh soạn: lẩu gà đồi, thịt nướng than hoa bản địa, rau rừng tươi xanh. Chỗ ngủ là lán gỗ có chăn bông dày hoặc lều cắm trại cách nhiệt chất lượng cao.'
  },
  {
    q: 'Tôi đi một mình có ghép đoàn được không?',
    a: 'Có tới hơn 60% thành viên tham gia tour của ĐI CÙNG GIÓ là đi một mình! Bạn sẽ nhanh chóng làm quen, kết nối với những người bạn cùng chung niềm đam mê xê dịch qua các hoạt động giao lưu, đốt lửa trại ấm áp.'
  },
  {
    q: 'Chính sách bảo lưu và hoàn hủy tour khi có việc đột xuất?',
    a: 'ĐI CÙNG GIÓ có chính sách linh hoạt hàng đầu: bạn được chuyển ngày hoặc bảo lưu 100% kinh phí sang chuyến đi tiếp theo nếu báo trước 7 ngày khởi hành. Trường hợp thời tiết bất khả kháng, ban tổ chức sẽ hoàn tiền 100% hoặc đổi cung đường tương đương theo thỏa thuận.'
  }
];

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

// Current state
let currentCategory = 'all';
let isShowingAllTours = false;

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
  renderTours();
  renderSchedule();
  renderDestinations();
  renderBlogPosts();
  renderFAQs();
  updateWishlistBadges();
  setupCategoryFilter();
  setupBookingForm();
  setupMobileNav();
  setupFloatingActions();
  setupNavbarScroll();
  setupHeroSearch();
  setupSmoothScroll();
  initLucideIcons();
});

// Helper to safely re-init Lucide icons
function initLucideIcons() {
  if (window.lucide && typeof window.lucide.createIcons === 'function') {
    window.lucide.createIcons();
  }
}

/**
 * Render Tour Cards (Left column 70%)
 */
function renderTours(filterCategory = currentCategory) {
  const container = document.getElementById('tour-grid-container');
  if (!container) return;

  let filtered = TOURS_DATA;

  if (filterCategory !== 'all') {
    filtered = TOURS_DATA.filter(t => t.category === filterCategory || t.subCategory === filterCategory);
  } else if (!isShowingAllTours) {
    // If user is on 'all' and hasn't clicked expand all, default to showing the 4 primary featured tours first
    filtered = TOURS_DATA.filter(t => t.isFeatured);
  }

  // Update toggle button text if available
  const toggleBtn = document.getElementById('toggle-all-tours-btn');
  if (toggleBtn) {
    if (isShowingAllTours && filterCategory === 'all') {
      toggleBtn.innerHTML = `<span>Thu gọn</span><i data-lucide="chevron-up" class="w-4 h-4"></i>`;
    } else {
      toggleBtn.innerHTML = `<span>Xem tất cả tour</span><i data-lucide="arrow-right" class="w-4 h-4"></i>`;
    }
  }

  if (filtered.length === 0) {
    container.innerHTML = `
      <div class="col-span-full py-12 text-center bg-white rounded-2xl border border-gray-100 p-8 shadow-sm">
        <i data-lucide="compass" class="w-12 h-12 mx-auto text-gray-400 mb-3 animate-spin"></i>
        <h4 class="text-lg font-bold text-gray-700">Chưa có tour trong danh mục này</h4>
        <p class="text-sm text-gray-500 mt-1">Vui lòng chọn danh mục khác hoặc liên hệ để thiết kế tour riêng.</p>
        <button onclick="filterByCategory('all')" class="mt-4 px-5 py-2 bg-forest text-white rounded-full text-sm font-semibold hover:bg-forest/90 transition-all">
          Xem tất cả tour
        </button>
      </div>
    `;
    initLucideIcons();
    return;
  }

  container.innerHTML = filtered.map(tour => {
    const isLiked = wishlist.has(tour.id);
    return `
      <div class="tour-card bg-white rounded-2xl overflow-hidden border border-gray-100 shadow-sm flex flex-col justify-between group">
        <!-- Tour Image Container (Clickable for Quick View) -->
        <div class="relative overflow-hidden aspect-[4/3] bg-gray-100 cursor-pointer" onclick="openTourDetailModal(${tour.id})">
          <img 
            src="${tour.image}" 
            alt="${tour.title}" 
            loading="lazy"
            onerror="this.src='https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=800&q=80'"
            class="tour-card-image w-full h-full object-cover"
          />
          <!-- Category Badge (Top Left) -->
          <div class="absolute top-3 left-3 z-10">
            <span class="bg-[#1E4D3B]/90 backdrop-blur-sm text-white text-xs font-semibold px-3 py-1 rounded-full shadow-sm">
              ${tour.badge}
            </span>
          </div>

          <!-- Quick view hint overlay on hover -->
          <div class="absolute inset-0 bg-black/25 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center pointer-events-none">
            <span class="px-3 py-1.5 rounded-full bg-white/95 text-forest text-xs font-bold shadow-md backdrop-blur-sm flex items-center gap-1.5 transform translate-y-2 group-hover:translate-y-0 transition-transform">
              <i data-lucide="eye" class="w-3.5 h-3.5 text-forest"></i>
              <span>Xem chi tiết</span>
            </span>
          </div>

          <!-- Wishlist Heart Button (Top Right) -->
          <button 
            type="button" 
            onclick="toggleWishlist(${tour.id}, event)" 
            title="${isLiked ? 'Bỏ yêu thích' : 'Lưu tour yêu thích'}"
            class="heart-btn absolute top-3 right-3 z-10 w-8 h-8 rounded-full bg-black/35 backdrop-blur-md flex items-center justify-center text-white hover:bg-black/55 transition-all shadow-sm ${isLiked ? 'active' : ''}"
          >
            <i data-lucide="heart" class="w-4 h-4 transition-colors ${isLiked ? 'fill-red-500 text-red-500' : 'text-white'}"></i>
          </button>
        </div>

        <!-- Tour Body Content -->
        <div class="p-4 flex flex-col flex-1 justify-between">
          <div>
            <h3 class="font-bold text-gray-900 text-[13.5px] xl:text-[14px] leading-snug line-clamp-2 min-h-[38px] tracking-tight group-hover:text-forest transition-colors cursor-pointer" onclick="openTourDetailModal(${tour.id})" title="${tour.title}">
              ${tour.title}
            </h3>

            <!-- Meta details (Duration & Route) on 2 clean lines -->
            <div class="mt-2 space-y-1 text-xs text-gray-500">
              <div class="flex items-center gap-1.5 whitespace-nowrap">
                <i data-lucide="clock" class="w-3.5 h-3.5 text-gray-400 shrink-0"></i>
                <span>${tour.duration}</span>
              </div>
              <div class="flex items-center gap-1.5 whitespace-nowrap">
                <i data-lucide="map-pin" class="w-3.5 h-3.5 text-gray-400 shrink-0"></i>
                <span class="truncate">${tour.location}</span>
              </div>
            </div>

            <!-- Price -->
            <div class="mt-2.5">
              <span class="text-[15px] font-bold text-forest whitespace-nowrap">${tour.price}</span>
            </div>
          </div>

          <!-- Bottom: Rating & Book Button (strictly on 1 horizontal line) -->
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
              onclick="openBookingModal('${tour.title.replace(/'/g, "\\'")}', '${tour.departureDates ? tour.departureDates[0] : ''}', '${tour.price}')"
              class="whitespace-nowrap px-3.5 py-1.5 rounded-md bg-[#1E4D3B] text-white text-xs font-medium shrink-0 hover:bg-forest/90 active:scale-95 transition-all shadow-sm"
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

/**
 * Toggle between showing 4 featured tours and all tours
 */
function toggleViewAllTours() {
  if (currentCategory !== 'all') {
    filterByCategory('all');
    isShowingAllTours = true;
  } else {
    isShowingAllTours = !isShowingAllTours;
  }
  renderTours('all');
}

/**
 * Render Schedule Widget (Right column 28%)
 */
function renderSchedule() {
  const container = document.getElementById('schedule-list-container');
  if (!container) return;

  container.innerHTML = DEPARTURE_SCHEDULE.map(item => `
    <div 
      onclick="openBookingModal('${item.title.replace(/'/g, "\\'")}', '${item.dateFull}', '${item.price}')"
      class="schedule-row flex items-center justify-between gap-3 p-3 rounded-xl border border-gray-100 cursor-pointer hover:border-emerald-200 transition-all bg-white"
    >
      <!-- Bên trái: Khối ngày tháng -->
      <div class="w-12 text-center shrink-0">
        <div class="w-11 h-11 mx-auto rounded-xl bg-gray-50 border border-gray-200 flex flex-col items-center justify-center text-center">
          <span class="text-sm font-extrabold text-gray-900 leading-none">${item.day}</span>
          <span class="text-[10px] font-semibold text-gray-500 uppercase mt-0.5">${item.month}</span>
        </div>
      </div>

      <!-- Ở giữa (flex-1 min-w-0): Dòng 1 Tên tour, Dòng 2 Thời lượng & Giá tiền chung 1 dòng ngang duy nhất -->
      <div class="flex-1 min-w-0">
        <h4 class="text-sm font-bold text-gray-800 truncate" title="${item.title}">${item.title}</h4>
        <p class="text-xs text-gray-500 whitespace-nowrap mt-0.5 flex items-center gap-1.5">
          <span>${item.duration}</span>
          <span class="text-gray-300">|</span>
          <span class="font-bold text-[#1E4D3B]">${item.price}</span>
        </p>
      </div>

      <!-- Bên phải (shrink-0 flex items-center gap-1.5): Badge Còn chỗ + icon > -->
      <div class="shrink-0 flex items-center gap-1.5">
        <span class="bg-[#E6F4EA] text-[#1E4D3B] text-[11px] font-medium px-2 py-0.5 rounded whitespace-nowrap">
          ${item.status}
        </span>
        <i data-lucide="chevron-right" class="w-4 h-4 text-gray-400"></i>
      </div>
    </div>
  `).join('');

  initLucideIcons();
}

/**
 * Category bar interaction
 */
function setupCategoryFilter() {
  const items = document.querySelectorAll('.category-item');
  items.forEach(el => {
    el.addEventListener('click', (e) => {
      e.preventDefault();
      const cat = el.getAttribute('data-category');
      filterByCategory(cat);
    });
  });
}

function filterByCategory(cat) {
  currentCategory = cat;
  isShowingAllTours = (cat === 'all' ? isShowingAllTours : true);

  const items = document.querySelectorAll('.category-item');
  items.forEach(el => {
    if (el.getAttribute('data-category') === cat) {
      el.classList.add('active');
    } else {
      el.classList.remove('active');
    }
  });

  renderTours(cat);

  // Smoothly scroll down to tours section if needed
  const tourSection = document.getElementById('tours-section');
  if (tourSection) {
    const rect = tourSection.getBoundingClientRect();
    if (rect.top < 0 || rect.bottom < 100) {
      tourSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  }
}

/**
 * Toggle Wishlist & Cart Counter
 */
function toggleWishlist(tourId, event) {
  if (event) {
    event.stopPropagation();
  }

  const tour = TOURS_DATA.find(t => t.id === tourId);
  const title = tour ? tour.title : 'Tour';

  if (wishlist.has(tourId)) {
    wishlist.delete(tourId);
    showToast('Đã xóa khỏi yêu thích', `Đã bỏ "${title}" khỏi danh sách lưu trữ.`);
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
    if (count > 0) {
      badge.classList.remove('hidden');
    } else {
      badge.classList.add('hidden');
    }
  });
}

/**
 * Wishlist Drawer
 */
function openWishlistDrawer() {
  const drawer = document.getElementById('wishlist-drawer');
  const overlay = document.getElementById('drawer-overlay');
  const container = document.getElementById('wishlist-items-container');
  if (!drawer || !overlay) return;

  const savedTours = TOURS_DATA.filter(t => wishlist.has(t.id));

  if (savedTours.length === 0) {
    container.innerHTML = `
      <div class="py-16 text-center text-gray-500">
        <i data-lucide="heart" class="w-12 h-12 mx-auto text-gray-300 mb-3"></i>
        <p class="font-medium text-gray-700">Danh sách yêu thích trống</p>
        <p class="text-xs text-gray-400 mt-1">Hãy bấm vào biểu tượng trái tim ở các thẻ tour để lưu hành trình bạn quan tâm nhé!</p>
      </div>
    `;
  } else {
    container.innerHTML = savedTours.map(tour => `
      <div class="flex items-center gap-3 p-3 bg-gray-50 rounded-xl border border-gray-100 hover:border-emerald-200 transition-all">
        <img src="${tour.image}" alt="${tour.title}" class="w-16 h-16 rounded-lg object-cover shrink-0">
        <div class="flex-1 min-w-0">
          <h4 class="text-sm font-bold text-gray-800 truncate">${tour.title}</h4>
          <p class="text-xs text-forest font-semibold mt-0.5">${tour.price}</p>
          <div class="flex items-center gap-2 mt-2">
            <button 
              onclick="openBookingModal('${tour.title.replace(/'/g, "\\'")}', '', '${tour.price}'); closeWishlistDrawer();"
              class="text-xs bg-forest text-white px-3 py-1 rounded-full font-semibold hover:bg-forest/90"
            >
              Đặt tour
            </button>
            <button 
              onclick="toggleWishlist(${tour.id}); openWishlistDrawer();"
              class="text-xs text-red-500 hover:underline"
            >
              Xóa
            </button>
          </div>
        </div>
      </div>
    `).join('');
  }

  initLucideIcons();
  drawer.classList.remove('translate-x-full');
  overlay.classList.remove('hidden');
  document.body.style.overflow = 'hidden';
}

function closeWishlistDrawer() {
  const drawer = document.getElementById('wishlist-drawer');
  const overlay = document.getElementById('drawer-overlay');
  if (drawer) drawer.classList.add('translate-x-full');
  if (overlay) overlay.classList.add('hidden');
  document.body.style.overflow = '';
}

/**
 * Booking Modal
 */
function openBookingModal(tourName = '', tourDate = '', tourPrice = '') {
  const modal = document.getElementById('booking-modal');
  if (!modal) return;

  const tourSelect = document.getElementById('booking-tour-select');
  const dateInput = document.getElementById('booking-date-input');
  const summaryBox = document.getElementById('booking-summary-box');

  if (tourSelect) {
    if (tourName) {
      let found = false;
      for (let i = 0; i < tourSelect.options.length; i++) {
        if (tourSelect.options[i].text.includes(tourName) || tourSelect.options[i].value.includes(tourName)) {
          tourSelect.selectedIndex = i;
          found = true;
          break;
        }
      }
      if (!found) {
        const newOpt = new Option(tourName, tourName, true, true);
        tourSelect.add(newOpt);
      }
    }
  }

  if (dateInput && tourDate) {
    dateInput.value = tourDate;
  }

  if (summaryBox && tourPrice) {
    summaryBox.innerHTML = `
      <div class="p-3 bg-mint-soft/60 rounded-xl border border-secondary-mint-border text-xs text-forest flex items-center justify-between">
        <span class="font-medium">Giá niêm yết:</span>
        <span class="font-bold text-sm">${tourPrice}</span>
      </div>
    `;
  }

  modal.classList.remove('hidden');
  document.body.style.overflow = 'hidden';
}

function closeBookingModal() {
  const modal = document.getElementById('booking-modal');
  if (modal) {
    modal.classList.add('hidden');
    document.body.style.overflow = '';
  }
}

function setupBookingForm() {
  const form = document.getElementById('booking-form');
  if (!form) return;

  form.addEventListener('submit', (e) => {
    e.preventDefault();

    const name = document.getElementById('booking-name')?.value || 'Quý khách';
    const phone = document.getElementById('booking-phone')?.value || '';
    const tourSelect = document.getElementById('booking-tour-select');
    const tour = tourSelect ? tourSelect.options[tourSelect.selectedIndex].text : 'Tour trekking';
    const people = document.getElementById('booking-people')?.value || '1';

    closeBookingModal();
    form.reset();

    showToast(
      '🎉 Đặt tour thành công!',
      `Cảm ơn ${name} đã gửi thông tin đặt tour "${tour}" cho ${people} người. Đội ngũ ĐI CÙNG GIÓ sẽ gọi tới ${phone} trong 15 phút!`,
      'success',
      8000
    );
  });
}

/**
 * Video Modal
 */
function openVideoModal() {
  const modal = document.getElementById('video-modal');
  const player = document.getElementById('video-frame');
  if (!modal) return;

  // Scenic trekking & mountains in Vietnam video embed
  if (player) {
    player.src = 'https://www.youtube.com/embed/8Z1e9MRKSQU?autoplay=1&rel=0&modestbranding=1';
  }

  modal.classList.remove('hidden');
  document.body.style.overflow = 'hidden';
}

function closeVideoModal() {
  const modal = document.getElementById('video-modal');
  const player = document.getElementById('video-frame');
  if (modal) {
    modal.classList.add('hidden');
    document.body.style.overflow = '';
  }
  if (player) {
    player.src = '';
  }
}

/**
 * Search Modal
 */
function openSearchModal() {
  const modal = document.getElementById('search-modal');
  const input = document.getElementById('search-input');
  if (!modal) return;

  modal.classList.remove('hidden');
  document.body.style.overflow = 'hidden';
  if (input) {
    input.value = '';
    setTimeout(() => input.focus(), 100);
    handleSearchInput('');
  }
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

  const term = query.trim().toLowerCase();
  const results = TOURS_DATA.filter(t => 
    t.title.toLowerCase().includes(term) ||
    t.location.toLowerCase().includes(term) ||
    t.categoryName.toLowerCase().includes(term) ||
    t.description.toLowerCase().includes(term)
  );

  if (results.length === 0) {
    container.innerHTML = `
      <div class="py-8 text-center text-gray-400">
        <i data-lucide="search-x" class="w-10 h-10 mx-auto mb-2 text-gray-300"></i>
        <p class="text-sm">Không tìm thấy tour phù hợp với từ khóa "${query}".</p>
      </div>
    `;
  } else {
    container.innerHTML = results.map(tour => `
      <div 
        onclick="openBookingModal('${tour.title.replace(/'/g, "\\'")}', '', '${tour.price}'); closeSearchModal();"
        class="flex items-center gap-3 p-3 rounded-xl hover:bg-gray-50 border border-gray-100 transition-all cursor-pointer"
      >
        <img src="${tour.image}" alt="${tour.title}" class="w-14 h-14 rounded-lg object-cover shrink-0">
        <div class="flex-1 min-w-0">
          <div class="flex items-center justify-between">
            <h4 class="text-sm font-bold text-gray-900 truncate">${tour.title}</h4>
            <span class="text-xs font-bold text-forest">${tour.price}</span>
          </div>
          <p class="text-xs text-gray-500 mt-0.5 line-clamp-1">${tour.location} • ${tour.duration}</p>
        </div>
      </div>
    `).join('');
  }

  initLucideIcons();
}

/**
 * Toast Notification System
 */
function showToast(title, message, type = 'info', duration = 5000) {
  const container = document.getElementById('toast-container');
  if (!container) return;

  const toast = document.createElement('div');
  toast.className = `toast-slide-in max-w-sm w-full bg-white rounded-2xl shadow-xl border border-gray-100 p-4 flex items-start gap-3 pointer-events-auto transition-all`;

  let iconHtml = `<i data-lucide="info" class="w-5 h-5 text-blue-500 shrink-0 mt-0.5"></i>`;
  if (type === 'success') {
    iconHtml = `<i data-lucide="check-circle" class="w-5 h-5 text-emerald-500 shrink-0 mt-0.5"></i>`;
  } else if (type === 'warning') {
    iconHtml = `<i data-lucide="alert-triangle" class="w-5 h-5 text-amber-500 shrink-0 mt-0.5"></i>`;
  }

  toast.innerHTML = `
    ${iconHtml}
    <div class="flex-1 min-w-0">
      <h5 class="text-sm font-bold text-gray-900">${title}</h5>
      <p class="text-xs text-gray-600 mt-1 leading-relaxed">${message}</p>
    </div>
    <button onclick="this.parentElement.remove()" class="text-gray-400 hover:text-gray-600 p-1">
      <i data-lucide="x" class="w-4 h-4"></i>
    </button>
  `;

  container.appendChild(toast);
  initLucideIcons();

  setTimeout(() => {
    toast.style.opacity = '0';
    toast.style.transform = 'translateX(50px)';
    setTimeout(() => toast.remove(), 400);
  }, duration);
}

/**
 * Mobile Navigation Drawer
 */
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

  // Close nav on link click
  navDrawer.querySelectorAll('a').forEach(a => {
    a.addEventListener('click', closeNav);
  });
}

/**
 * Floating Action Bar Setup
 */
function setupFloatingActions() {
  const zaloBtn = document.getElementById('float-zalo');
  const phoneBtn = document.getElementById('float-phone');
  const messengerBtn = document.getElementById('float-messenger');

  zaloBtn?.addEventListener('click', () => {
    window.open('https://zalo.me/0988668899', '_blank');
  });

  phoneBtn?.addEventListener('click', () => {
    window.location.href = 'tel:0988668899';
  });

  messengerBtn?.addEventListener('click', () => {
    window.open('https://m.me/dicunggiotrekking', '_blank');
  });
}

/**
 * Render Destinations Section
 */
function renderDestinations() {
  const container = document.getElementById('destinations-grid-container');
  if (!container) return;

  container.innerHTML = DESTINATIONS_DATA.map(dest => `
    <div class="destination-card bg-white rounded-2xl overflow-hidden border border-gray-100 shadow-sm group flex flex-col justify-between">
      <div class="relative aspect-[4/3] overflow-hidden bg-gray-100">
        <img 
          src="${dest.image}" 
          alt="${dest.name}" 
          loading="lazy"
          class="w-full h-full object-cover"
        />
        <div class="absolute inset-0 bg-gradient-to-t from-black/75 via-black/25 to-transparent"></div>
        
        <!-- Region & Altitude Badges -->
        <div class="absolute top-3 left-3 right-3 flex items-center justify-between">
          <span class="px-2.5 py-1 rounded-full text-[11px] font-bold bg-[#1E4D3B]/90 text-white backdrop-blur-sm shadow-sm">
            ${dest.badge}
          </span>
          <span class="px-2.5 py-1 rounded-full text-[11px] font-bold bg-black/45 text-white backdrop-blur-sm flex items-center gap-1 shadow-sm">
            <i data-lucide="mountain" class="w-3 h-3 text-emerald-300"></i>
            ${dest.altitude}
          </span>
        </div>

        <!-- Destination Title Overlay -->
        <div class="absolute bottom-3 left-3 right-3 text-white">
          <h3 class="text-lg font-bold leading-tight drop-shadow">${dest.name}</h3>
          <p class="text-xs text-emerald-200 font-medium">${dest.subtitle}</p>
        </div>
      </div>

      <div class="p-4 flex flex-col flex-1 justify-between space-y-3">
        <p class="text-xs text-gray-600 leading-relaxed">${dest.description}</p>
        
        <div class="pt-2 border-t border-gray-100 flex items-center justify-between">
          <span class="text-[11px] font-semibold text-gray-500 flex items-center gap-1">
            <i data-lucide="activity" class="w-3.5 h-3.5 text-forest"></i>
            ${dest.level}
          </span>
          <button 
            type="button" 
            onclick="filterByCategory('${dest.categoryFilter}'); document.getElementById('tours-section').scrollIntoView({behavior: 'smooth'});"
            class="inline-flex items-center gap-1 text-xs font-bold text-forest hover:text-forest-dark hover:underline"
          >
            <span>Xem tour</span>
            <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
          </button>
        </div>
      </div>
    </div>
  `).join('');

  initLucideIcons();
}

/**
 * Render Blog & Guides Section
 */
function renderBlogPosts() {
  const container = document.getElementById('blog-grid-container');
  if (!container) return;

  container.innerHTML = BLOG_POSTS_DATA.map(post => `
    <article class="blog-card bg-white rounded-2xl overflow-hidden border border-gray-100 shadow-sm flex flex-col justify-between group">
      <div class="relative aspect-[16/10] overflow-hidden bg-gray-100 cursor-pointer" onclick="openBlogModal(${post.id})">
        <img 
          src="${post.image}" 
          alt="${post.title}" 
          loading="lazy"
          class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105"
        />
        <div class="absolute top-3 left-3">
          <span class="px-2.5 py-1 rounded-full text-[11px] font-bold bg-[#1E4D3B]/90 text-white backdrop-blur-sm">
            ${post.category}
          </span>
        </div>
      </div>

      <div class="p-5 flex flex-col flex-1 justify-between space-y-3">
        <div>
          <div class="flex items-center gap-2 text-[11px] text-gray-400 mb-2">
            <span>${post.date}</span>
            <span>•</span>
            <span class="flex items-center gap-1"><i data-lucide="clock" class="w-3 h-3"></i> ${post.readTime}</span>
          </div>
          <h3 
            class="blog-title font-bold text-gray-900 text-sm sm:text-base leading-snug line-clamp-2 cursor-pointer transition-colors"
            onclick="openBlogModal(${post.id})"
          >
            ${post.title}
          </h3>
          <p class="text-xs text-gray-500 leading-relaxed mt-2 line-clamp-2">
            ${post.excerpt}
          </p>
        </div>

        <div class="pt-3 border-t border-gray-100 flex items-center justify-between">
          <span class="text-xs font-medium text-gray-600 flex items-center gap-1.5">
            <i data-lucide="user" class="w-3.5 h-3.5 text-forest"></i>
            ${post.author}
          </span>
          <button 
            type="button" 
            onclick="openBlogModal(${post.id})"
            class="text-xs font-bold text-forest hover:text-forest-dark flex items-center gap-1 group-hover:translate-x-0.5 transition-transform"
          >
            <span>Đọc tiếp</span>
            <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
          </button>
        </div>
      </div>
    </article>
  `).join('');

  initLucideIcons();
}

/**
 * Render FAQs Section
 */
function renderFAQs() {
  const container = document.getElementById('faq-accordion-container');
  if (!container) return;

  container.innerHTML = FAQS_DATA.map((faq, index) => `
    <div class="faq-item bg-white rounded-2xl border border-gray-200/80 overflow-hidden ${index === 0 ? 'active' : ''}">
      <button 
        type="button" 
        onclick="toggleFaq(${index})" 
        class="w-full px-5 py-4 text-left flex items-center justify-between gap-4 font-bold text-gray-900 text-sm sm:text-base hover:text-forest transition-colors focus:outline-none"
      >
        <span>${faq.q}</span>
        <i data-lucide="chevron-down" class="faq-chevron w-5 h-5 text-gray-400 shrink-0 transition-transform duration-300"></i>
      </button>
      <div class="faq-answer px-5 pb-4 text-xs sm:text-sm text-gray-600 leading-relaxed">
        <p>${faq.a}</p>
      </div>
    </div>
  `).join('');

  initLucideIcons();
}

/**
 * Toggle FAQ Accordion item
 */
function toggleFaq(index) {
  const items = document.querySelectorAll('.faq-item');
  items.forEach((item, i) => {
    if (i === index) {
      item.classList.toggle('active');
    } else {
      item.classList.remove('active');
    }
  });
}

/**
 * Open Tour Detail Quick View Modal
 */
function openTourDetailModal(tourId) {
  const tour = TOURS_DATA.find(t => t.id === tourId);
  if (!tour) return;

  const modal = document.getElementById('tour-detail-modal');
  const content = document.getElementById('tour-detail-content');
  if (!modal || !content) return;

  const isLiked = wishlist.has(tour.id);
  const dates = tour.departureDates ? tour.departureDates.join(', ') : 'Thứ 6 hàng tuần';

  content.innerHTML = `
    <div class="relative bg-white rounded-3xl overflow-hidden shadow-2xl max-w-2xl w-full border border-gray-100 modal-enter max-h-[90vh] flex flex-col">
      <!-- Header Image & Close Button -->
      <div class="relative h-60 sm:h-72 w-full shrink-0">
        <img src="${tour.image}" alt="${tour.title}" class="w-full h-full object-cover">
        <div class="absolute inset-0 bg-gradient-to-t from-black/85 via-black/35 to-transparent"></div>
        
        <button 
          type="button"
          onclick="closeTourDetailModal()" 
          class="absolute top-4 right-4 z-10 w-9 h-9 rounded-full bg-black/50 text-white hover:bg-black/80 flex items-center justify-center transition-colors backdrop-blur-sm"
          title="Đóng"
        >
          <i data-lucide="x" class="w-5 h-5"></i>
        </button>

        <div class="absolute bottom-4 left-5 right-5 text-white">
          <div class="flex items-center gap-2 mb-1.5">
            <span class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-[#1E4D3B] text-white">${tour.badge}</span>
            <span class="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-white/20 backdrop-blur-sm text-white">${tour.difficulty || 'Trung bình'}</span>
          </div>
          <h2 class="text-xl sm:text-2xl font-extrabold leading-tight drop-shadow-sm">${tour.title}</h2>
          <p class="text-xs sm:text-sm text-gray-200 mt-1 flex items-center gap-2">
            <i data-lucide="map-pin" class="w-3.5 h-3.5 text-emerald-300"></i>
            <span>${tour.location}</span>
            <span>•</span>
            <i data-lucide="clock" class="w-3.5 h-3.5 text-emerald-300"></i>
            <span>${tour.duration}</span>
          </p>
        </div>
      </div>

      <!-- Modal Body (Scrollable) -->
      <div class="p-5 sm:p-6 overflow-y-auto space-y-5 text-gray-700 text-sm flex-1">
        <!-- Key Stats Pills -->
        <div class="grid grid-cols-3 gap-3 p-3.5 rounded-2xl bg-[#F6F7F2] border border-gray-100 text-center">
          <div>
            <span class="block text-xs text-gray-500 font-medium">Giá trọn gói</span>
            <span class="block text-base font-bold text-forest mt-0.5">${tour.price}</span>
          </div>
          <div class="border-x border-gray-200">
            <span class="block text-xs text-gray-500 font-medium">Thời gian</span>
            <span class="block text-base font-bold text-gray-900 mt-0.5">${tour.duration}</span>
          </div>
          <div>
            <span class="block text-xs text-gray-500 font-medium">Đánh giá</span>
            <span class="block text-base font-bold text-amber-500 mt-0.5 flex items-center justify-center gap-1">
              <i data-lucide="star" class="w-4 h-4 fill-amber-400"></i>
              ${tour.rating} (${tour.reviews})
            </span>
          </div>
        </div>

        <!-- Description -->
        <div>
          <h4 class="text-xs font-bold uppercase tracking-wider text-gray-500 mb-1.5">Giới thiệu hành trình</h4>
          <p class="text-gray-700 leading-relaxed text-xs sm:text-sm">${tour.description}</p>
        </div>

        <!-- Highlights Checklist -->
        <div>
          <h4 class="text-xs font-bold uppercase tracking-wider text-gray-500 mb-2">Điểm nổi bật của cung đường</h4>
          <ul class="space-y-2 text-xs sm:text-sm">
            <li class="flex items-start gap-2">
              <i data-lucide="check-circle-2" class="w-4 h-4 text-emerald-600 shrink-0 mt-0.5"></i>
              <span>Chinh phục đỉnh cao ngoạn mục, check-in sống ảo biển mây bồng bềnh lúc bình minh.</span>
            </li>
            <li class="flex items-start gap-2">
              <i data-lucide="check-circle-2" class="w-4 h-4 text-emerald-600 shrink-0 mt-0.5"></i>
              <span>Giao lưu đốt lửa trại, thưởng thức ẩm thực nóng hổi đặc sản bản địa Tây Bắc.</span>
            </li>
            <li class="flex items-start gap-2">
              <i data-lucide="check-circle-2" class="w-4 h-4 text-emerald-600 shrink-0 mt-0.5"></i>
              <span>Đội ngũ Leader & Porter bản địa chu đáo, nhiệt tình hỗ trợ 100% suốt hành trình.</span>
            </li>
          </ul>
        </div>

        <!-- Inclusions -->
        <div>
          <h4 class="text-xs font-bold uppercase tracking-wider text-gray-500 mb-2">Dịch vụ bao gồm trọn gói</h4>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs text-gray-600">
            <span class="flex items-center gap-1.5"><i data-lucide="check" class="w-3.5 h-3.5 text-forest"></i> Xe đưa đón khứ hồi từ Hà Nội</span>
            <span class="flex items-center gap-1.5"><i data-lucide="check" class="w-3.5 h-3.5 text-forest"></i> Leader dẫn đoàn & Porter hỗ trợ</span>
            <span class="flex items-center gap-1.5"><i data-lucide="check" class="w-3.5 h-3.5 text-forest"></i> Các bữa ăn tiêu chuẩn theo lịch trình</span>
            <span class="flex items-center gap-1.5"><i data-lucide="check" class="w-3.5 h-3.5 text-forest"></i> Bảo hiểm du lịch tối đa 100.000.000đ</span>
            <span class="flex items-center gap-1.5"><i data-lucide="check" class="w-3.5 h-3.5 text-forest"></i> Mượn gậy trekking & áo mưa miễn phí</span>
            <span class="flex items-center gap-1.5"><i data-lucide="check" class="w-3.5 h-3.5 text-forest"></i> Lều trại / Lán nghỉ ấm áp</span>
          </div>
        </div>

        <!-- Next Departures -->
        <div class="p-3 bg-emerald-50/70 rounded-xl border border-emerald-100 flex items-center justify-between">
          <div>
            <span class="text-xs font-semibold text-forest block">Lịch khởi hành sắp tới:</span>
            <span class="text-xs text-gray-600 font-medium">${dates}</span>
          </div>
          <span class="badge-seat text-xs">Còn chỗ</span>
        </div>
      </div>

      <!-- Modal Footer CTAs -->
      <div class="p-4 sm:p-5 border-t border-gray-100 bg-gray-50/70 flex items-center justify-between gap-3 shrink-0">
        <button 
          type="button"
          onclick="toggleWishlist(${tour.id}); openTourDetailModal(${tour.id});" 
          class="p-2.5 rounded-full border border-gray-200 bg-white text-gray-600 hover:text-red-500 hover:border-red-200 transition-colors shrink-0 shadow-sm"
          title="Lưu yêu thích"
        >
          <i data-lucide="heart" class="w-5 h-5 ${isLiked ? 'fill-red-500 text-red-500' : ''}"></i>
        </button>

        <button 
          type="button"
          onclick="closeTourDetailModal(); openBookingModal('${tour.title.replace(/'/g, "\\'")}', '${tour.departureDates ? tour.departureDates[0] : ''}', '${tour.price}');" 
          class="flex-1 py-3 px-6 rounded-full bg-forest text-white font-bold text-sm hover:bg-forest/90 active:scale-95 transition-all shadow-md flex items-center justify-center gap-2"
        >
          <i data-lucide="calendar-check" class="w-4 h-4"></i>
          <span>Đăng ký tham gia tour này</span>
        </button>
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

/**
 * Open Blog Guide Modal
 */
function openBlogModal(postId) {
  const post = BLOG_POSTS_DATA.find(p => p.id === postId);
  if (!post) return;

  const modal = document.getElementById('blog-modal');
  const content = document.getElementById('blog-modal-content');
  if (!modal || !content) return;

  content.innerHTML = `
    <div class="relative bg-white rounded-3xl overflow-hidden shadow-2xl max-w-2xl w-full border border-gray-100 modal-enter max-h-[90vh] flex flex-col">
      <div class="relative h-56 sm:h-64 w-full shrink-0">
        <img src="${post.image}" alt="${post.title}" class="w-full h-full object-cover">
        <div class="absolute inset-0 bg-gradient-to-t from-black/85 via-black/40 to-transparent"></div>
        <button 
          type="button"
          onclick="closeBlogModal()" 
          class="absolute top-4 right-4 z-10 w-9 h-9 rounded-full bg-black/50 text-white hover:bg-black/80 flex items-center justify-center transition-colors"
          title="Đóng"
        >
          <i data-lucide="x" class="w-5 h-5"></i>
        </button>
        <div class="absolute bottom-4 left-5 right-5 text-white">
          <span class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-[#1E4D3B] text-white mb-2 inline-block">${post.category}</span>
          <h2 class="text-lg sm:text-xl font-bold leading-tight drop-shadow-sm">${post.title}</h2>
          <div class="flex items-center gap-3 text-xs text-gray-300 mt-2">
            <span>${post.author}</span>
            <span>•</span>
            <span>${post.date}</span>
            <span>•</span>
            <span>${post.readTime}</span>
          </div>
        </div>
      </div>
      <div class="p-6 overflow-y-auto space-y-4 text-gray-700 text-sm leading-relaxed flex-1">
        ${post.content}
        <div class="p-4 bg-emerald-50 rounded-2xl border border-emerald-100 mt-6">
          <h5 class="font-bold text-forest text-sm mb-1 flex items-center gap-1.5">
            <i data-lucide="compass" class="w-4 h-4"></i>
            Bạn đã sẵn sàng chinh phục đỉnh núi tiếp theo?
          </h5>
          <p class="text-xs text-gray-600 mb-3">ĐI CÙNG GIÓ luôn có lịch khởi hành đều đặn mỗi cuối tuần với đầy đủ dịch vụ hỗ trợ.</p>
          <button 
            type="button"
            onclick="closeBlogModal(); openBookingModal();" 
            class="px-4 py-2 rounded-full bg-forest text-white text-xs font-bold hover:bg-forest/90 transition-all shadow-sm"
          >
            Đăng ký tour ngay
          </button>
        </div>
      </div>
    </div>
  `;

  modal.classList.remove('hidden');
  document.body.style.overflow = 'hidden';
  initLucideIcons();
}

function closeBlogModal() {
  const modal = document.getElementById('blog-modal');
  if (modal) {
    modal.classList.add('hidden');
    document.body.style.overflow = '';
  }
}

/**
 * Navbar & Back to top scroll listener
 */
function setupNavbarScroll() {
  const header = document.querySelector('header');
  const backToTop = document.getElementById('back-to-top');

  window.addEventListener('scroll', () => {
    if (window.scrollY > 40) {
      header?.classList.add('header-scrolled');
    } else {
      header?.classList.remove('header-scrolled');
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

/**
 * Hero Search Bar Handler
 */
function setupHeroSearch() {
  const searchBtn = document.getElementById('hero-search-btn');
  const destSelect = document.getElementById('hero-dest-select');

  if (!searchBtn || !destSelect) return;

  searchBtn.addEventListener('click', () => {
    const selectedVal = destSelect.value;
    if (selectedVal && selectedVal !== 'all') {
      filterByCategory(selectedVal);
      showToast('Đã lọc theo điểm đến', `Hiển thị danh sách tour phù hợp với lựa chọn của bạn.`, 'success');
    } else {
      filterByCategory('all');
    }

    const toursSec = document.getElementById('tours-section');
    if (toursSec) {
      toursSec.scrollIntoView({ behavior: 'smooth' });
    }
  });
}

/**
 * Smooth Scroll Navigation & Active link highlight
 */
function setupSmoothScroll() {
  const navLinks = document.querySelectorAll('.nav-link');
  window.addEventListener('scroll', () => {
    const scrollPos = window.scrollY + 130;
    const sections = ['home', 'tours-section', 'schedule-section', 'destinations-section', 'why-us-section', 'about-section', 'testimonials-section', 'blog-section', 'faq-section', 'contact-section'];
    
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

