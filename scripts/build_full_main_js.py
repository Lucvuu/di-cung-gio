import json, sys
sys.stdout.reconfigure(encoding='utf-8')

# Load the comprehensive 20 tours
with open('scripts/parsed_tours.json', 'r', encoding='utf-8') as f:
    tours_data = json.load(f)

tours_json_str = json.dumps(tours_data, ensure_ascii=False, indent=2)

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
schedule_json_str = json.dumps(departure_schedule, ensure_ascii=False, indent=2)

js_content = f"""/**
 * TREKKING ĐI CÙNG GIÓ - OFFICIAL APPLICATION SCRIPT
 * Cập nhật bảng giá & chính sách hoàn hủy chính thức theo tài liệu Google Sheets 2026
 * Pure Vanilla JavaScript ES6+ (Zero Build Pipeline)
 */

// ==========================================
// 1. TOUR DATA REPOSITORY (ALL 20 TOURS)
// ==========================================
const TOURS_DATA = {tours_json_str};

// ==========================================
// 2. DEPARTURE SCHEDULE DATA (5 KEY TOURS)
// ==========================================
const DEPARTURE_SCHEDULE = {schedule_json_str};

// ==========================================
// 3. REVIEWS & TESTIMONIALS DATA
// ==========================================
const TESTIMONIALS_DATA = [
  {{
    id: 1,
    name: 'Nguyễn Thu Hà',
    role: 'Trekking Tà Xùa – Săn mây',
    avatar: 'assets/images/avatar-ha.jpg',
    comment: 'Cung đường sống lưng khủng long Tà Xùa đẹp nín thở, hướng dẫn viên nhiệt tình, đồ ăn ngon. Cảm ơn Trekking Đi Cùng Gió đã cho mình một hành trình thật đáng nhớ!',
    rating: 5,
    date: '18/10/2026'
  }},
  {{
    id: 2,
    name: 'Lê Minh Đức',
    role: 'Trekking Yên Tử – Chùa Đồng',
    avatar: 'assets/images/avatar-duc.jpg',
    comment: 'Lần đầu leo bộ Yên Tử mà được chạm tay vào Chùa Đồng lúc bình minh mây ngàn. Anh em leader chăm sóc chu đáo, huy chương gỗ độc quyền kỷ niệm rất đẹp.',
    rating: 5,
    date: '12/10/2026'
  }},
  {{
    id: 3,
    name: 'Trần Thị Mai',
    role: 'Kỳ Quan San – Bạch Mộc Lương Tử',
    avatar: 'assets/images/avatar-mai.jpg',
    comment: 'Đỉnh Kỳ Quan San quả thực xứng danh ngọn núi kỳ vĩ. Bình minh Đồi Muối biển mây bạt ngàn vượt xa mọi sự tưởng tượng. Đi Cùng Gió tổ chức cực kỳ chuyên nghiệp!',
    rating: 5,
    date: '05/10/2026'
  }}
];

// ==========================================
// 4. APP STATE
// ==========================================
let currentCategory = 'all';
let heroCurrentIndex = 0;
let heroSlideTimer = null;
let currentBookingTour = TOURS_DATA[0];
let bookingGuests = 1;

// Load Wishlist from LocalStorage
let wishlist = new Set();
try {{
  const savedWishlist = localStorage.getItem('dicunggio_wishlist');
  if (savedWishlist) {{
    wishlist = new Set(JSON.parse(savedWishlist));
  }}
}} catch (e) {{
  console.warn('LocalStorage error:', e);
}}

// ==========================================
// 5. INITIALIZATION ON DOM READY
// ==========================================
document.addEventListener('DOMContentLoaded', () => {{
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
}});

function initLucideIcons() {{
  if (typeof lucide !== 'undefined' && lucide.createIcons) {{
    lucide.createIcons();
  }}
}}

// Utility: format number to Vietnamese currency VND
function formatCurrency(amount) {{
  return new Intl.NumberFormat('vi-VN').format(amount) + 'đ';
}}

// ==========================================
// 6. HERO MULTI-SLIDE CONTROLLER (KEN BURNS)
// ==========================================
function initHeroSlider() {{
  const slides = document.querySelectorAll('.hero-slide');
  const dots = document.querySelectorAll('.hero-dot');
  if (!slides.length) return;

  function showSlide(index) {{
    slides.forEach((slide, i) => {{
      if (i === index) {{
        slide.classList.add('active');
      }} else {{
        slide.classList.remove('active');
      }}
    }});

    dots.forEach((dot, i) => {{
      if (i === index) {{
        dot.classList.add('active');
        dot.classList.remove('opacity-60');
      }} else {{
        dot.classList.remove('active');
        dot.classList.add('opacity-60');
      }}
    }});

    heroCurrentIndex = index;
  }}

  window.prevHeroSlide = function() {{
    let newIndex = heroCurrentIndex - 1;
    if (newIndex < 0) newIndex = slides.length - 1;
    showSlide(newIndex);
    resetHeroTimer();
  }};

  window.nextHeroSlide = function() {{
    let newIndex = (heroCurrentIndex + 1) % slides.length;
    showSlide(newIndex);
    resetHeroTimer();
  }};

  window.goToHeroSlide = function(index) {{
    showSlide(index);
    resetHeroTimer();
  }};

  function resetHeroTimer() {{
    if (heroSlideTimer) clearInterval(heroSlideTimer);
    heroSlideTimer = setInterval(() => {{
      window.nextHeroSlide();
    }}, 6500);
  }}

  resetHeroTimer();
}}

// ==========================================
// 7. RENDER TOURS (LEFT COLUMN 72%)
// ==========================================
function renderTours(filterCategory = currentCategory) {{
  const container = document.getElementById('tour-grid-container');
  if (!container) return;

  currentCategory = filterCategory;
  let filtered = [];

  if (filterCategory === 'all') {{
    filtered = TOURS_DATA.filter(t => t.isFeatured);
  }} else {{
    filtered = TOURS_DATA.filter(t => t.category === filterCategory || t.subCategory === filterCategory);
  }}

  if (filtered.length === 0) {{
    filtered = TOURS_DATA.slice(0, 4);
  }} else if (filtered.length > 4) {{
    filtered = filtered.slice(0, 4);
  }}

  container.innerHTML = filtered.map(tour => {{
    const isLiked = wishlist.has(tour.id);
    return `
      <div class="tour-card bg-white rounded-2xl overflow-hidden border border-gray-100 shadow-sm hover:shadow-md transition-all duration-300 flex flex-col justify-between group">
        
        <!-- Tour Image Container -->
        <div class="relative overflow-hidden aspect-[4/3] bg-gray-100 cursor-pointer" onclick="openTourDetailModal(${{tour.id}})">
          <img 
            src="${{tour.image}}" 
            alt="${{tour.title}}" 
            loading="lazy" 
            onerror="this.onerror=null; this.src='assets/images/tour-yen-tu.jpg';"
            class="tour-card-image w-full h-full object-cover transition-transform duration-500 group-hover:scale-108"
          />
          
          <!-- Category Badge (Top Left) -->
          <div class="absolute top-3 left-3 z-10 flex items-center gap-1.5">
            <span class="backdrop-blur-md bg-[#1E4D3B]/90 text-white text-[11px] font-bold px-2.5 py-1 rounded-full shadow-sm">
              ${{tour.badge}}
            </span>
            <span class="backdrop-blur-md bg-black/50 text-emerald-200 text-[10px] font-extrabold px-2 py-0.5 rounded-md shadow-sm">
              ${{tour.code}}
            </span>
          </div>

          <!-- Altitude Badge (Top Center/Left) -->
          <div class="absolute top-3 left-28 z-10">
            <span class="backdrop-blur-md bg-black/45 text-white text-[10px] font-semibold px-2 py-0.5 rounded-md shadow-sm">
              ${{tour.altitudeBadge}}
            </span>
          </div>

          <!-- Real Photo indicator if available -->
          ${{tour.gallery && tour.gallery.length > 0 ? `
            <div class="absolute bottom-2.5 left-2.5 z-10">
              <span class="backdrop-blur-md bg-black/60 text-emerald-300 text-[10px] font-bold px-2 py-0.5 rounded-full shadow-sm flex items-center gap-1">
                <i data-lucide="camera" class="w-3 h-3 text-emerald-300"></i>
                <span>${{tour.gallery.length}} ảnh thực tế</span>
              </span>
            </div>
          ` : ''}}

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

          <!-- Wishlist Heart Button -->
          <button 
            type="button" 
            onclick="toggleWishlist(${{tour.id}}, event)" 
            title="${{isLiked ? 'Bỏ yêu thích' : 'Lưu tour yêu thích'}}"
            class="heart-btn absolute top-3 right-3 z-20 w-8 h-8 rounded-full bg-white/80 backdrop-blur-md flex items-center justify-center text-gray-700 hover:text-red-500 hover:bg-white transition-all shadow-sm ${{isLiked ? 'active' : ''}}"
          >
            <i data-lucide="heart" class="w-4 h-4 transition-colors ${{isLiked ? 'fill-red-500 text-red-500' : ''}}"></i>
          </button>
        </div>

        <!-- Tour Body Content -->
        <div class="p-4 flex flex-col flex-1 justify-between">
          <div>
            <!-- Meta Details: Location & History Story -->
            <div class="flex items-center justify-between text-[11px] text-gray-500 mb-1.5">
              <span class="flex items-center gap-1">
                <i data-lucide="map-pin" class="w-3 h-3 text-forest shrink-0"></i>
                <span class="truncate max-w-[125px]">${{tour.location}}</span>
              </span>
              <button 
                type="button" 
                onclick="openTourDetailModal(${{tour.id}}, 2); event.stopPropagation();" 
                class="inline-flex items-center gap-1 text-[11px] font-semibold text-forest hover:text-forest-dark hover:underline cursor-pointer"
                title="Xem lịch sử & câu chuyện địa danh"
              >
                <i data-lucide="book-open" class="w-3 h-3 text-forest"></i>
                <span>Câu chuyện</span>
              </button>
            </div>

            <!-- Title -->
            <h3 
              class="font-bold text-gray-900 text-[13.5px] xl:text-[14px] leading-snug line-clamp-2 min-h-[38px] tracking-tight group-hover:text-forest transition-colors cursor-pointer" 
              onclick="openTourDetailModal(${{tour.id}})" 
              title="${{tour.title}}"
            >
              ${{tour.title}}
            </h3>

            <!-- 1-line Short Summary Description -->
            <p class="text-xs text-gray-600 line-clamp-2 mt-1 mb-2 leading-relaxed">
              ${{tour.shortSummary || tour.description}}
            </p>

            <!-- Commitment Tag (Từ 5 khách, Lịch chạy) -->
            <div class="flex items-center gap-1.5 mb-2">
              <span class="px-2 py-0.5 rounded-md bg-emerald-50 text-forest text-[10px] font-bold border border-emerald-100 flex items-center gap-1">
                <i data-lucide="check" class="w-3 h-3 text-forest"></i>
                <span>${{tour.minPax}}</span>
              </span>
              <span class="text-[10px] text-gray-500 font-medium">
                ${{tour.departureFrequency}}
              </span>
            </div>

            <!-- Price & Duration -->
            <div class="flex items-baseline justify-between mt-1">
              <span class="text-[15px] font-black text-forest whitespace-nowrap">${{tour.price}}</span>
              <span class="text-[11px] text-gray-500 font-medium">${{tour.duration}}</span>
            </div>
          </div>

          <!-- Bottom: Rating & Direct Book Button -->
          <div class="mt-3 pt-3 border-t border-gray-100 flex items-center justify-between gap-1">
            <div class="flex items-center gap-1 shrink-0">
              <div class="flex text-amber-400">
                <i data-lucide="star" class="w-3 h-3 fill-amber-400 text-amber-400"></i>
                <i data-lucide="star" class="w-3 h-3 fill-amber-400 text-amber-400"></i>
                <i data-lucide="star" class="w-3 h-3 fill-amber-400 text-amber-400"></i>
                <i data-lucide="star" class="w-3 h-3 fill-amber-400 text-amber-400"></i>
                <i data-lucide="star" class="w-3 h-3 fill-amber-400 text-amber-400"></i>
              </div>
              <span class="text-[11px] text-gray-400 font-medium">(${{tour.reviews}})</span>
            </div>

            <button 
              type="button" 
              onclick="openSmartBookingModal(${{tour.id}}); event.stopPropagation();"
              class="btn-shine whitespace-nowrap px-3.5 py-1.5 rounded-lg bg-[#1E4D3B] text-white text-xs font-semibold shrink-0 hover:bg-forest/90 active:scale-95 transition-all shadow-sm cursor-pointer"
            >
              Đăng ký tour
            </button>
          </div>

        </div>

      </div>
    `;
  }}).join('');

  initLucideIcons();
}}

// ==========================================
// 8. RENDER DEPARTURE SCHEDULE (RIGHT 28%)
// ==========================================
function renderSchedule() {{
  const container = document.getElementById('schedule-list-container');
  if (!container) return;

  container.innerHTML = DEPARTURE_SCHEDULE.map(item => `
    <div 
      onclick="openTourDetailModal(${{item.tourId}})"
      class="schedule-row p-3 rounded-xl bg-gray-50/70 border border-gray-100/80 flex items-center justify-between gap-3 cursor-pointer group"
      title="Nhấn để xem lộ trình & đăng ký tour này"
    >
      <!-- Date Block -->
      <div class="flex items-center gap-2.5 shrink-0">
        <div class="w-11 h-11 rounded-xl bg-[#1E4D3B] text-white flex flex-col items-center justify-center shadow-xs group-hover:scale-105 transition-transform">
          <span class="text-sm font-black leading-none">${{item.day}}</span>
          <span class="text-[9px] font-bold uppercase tracking-wider text-emerald-200 mt-0.5">${{item.month}}</span>
        </div>

        <div class="min-w-0">
          <div class="flex items-center gap-1.5">
            <span class="text-[9px] font-extrabold px-1.5 py-0.2 rounded bg-emerald-100 text-forest">${{item.code}}</span>
            <h4 class="text-xs font-bold text-gray-900 group-hover:text-forest transition-colors truncate">
              ${{item.title}}
            </h4>
          </div>
          <span class="text-[11px] text-gray-500 font-medium">${{item.duration}} • Hà Nội</span>
        </div>
      </div>

      <!-- Price & Status Badge -->
      <div class="text-right shrink-0">
        <span class="block text-xs font-extrabold text-forest">${{item.price}}</span>
        <span class="badge-seat text-[10px] inline-block mt-0.5">${{item.status}}</span>
      </div>
    </div>
  `).join('');

  initLucideIcons();
}}

// ==========================================
// 9. CATEGORY BAR FILTERING CONTROLLER
// ==========================================
function setupCategoryFilter() {{
  const items = document.querySelectorAll('.category-item');
  items.forEach(item => {{
    item.addEventListener('click', (e) => {{
      e.preventDefault();
      const cat = item.getAttribute('data-category');
      filterByCategory(cat);
    }});
  }});
}}

function filterByCategory(cat) {{
  currentCategory = cat;

  // Update Category Bar active classes
  const items = document.querySelectorAll('.category-item');
  items.forEach(item => {{
    const itemCat = item.getAttribute('data-category');
    if (itemCat === cat) {{
      item.classList.add('active');
    }} else {{
      item.classList.remove('active');
    }}
  }});

  // Smooth fade-in re-render of tours
  const grid = document.getElementById('tour-grid-container');
  if (grid) {{
    grid.style.opacity = '0';
    grid.style.transform = 'translateY(8px)';
    grid.style.transition = 'all 0.3s cubic-bezier(0.16, 1, 0.3, 1)';
    setTimeout(() => {{
      renderTours(cat);
      grid.style.opacity = '1';
      grid.style.transform = 'translateY(0)';
    }}, 180);
  }}

  // Update Title text
  const titleEl = document.getElementById('section-tour-title');
  if (titleEl) {{
    const titles = {{
      all: 'Tour Nổi Bật',
      trekking: 'Tour Trekking Chinh Phục',
      spiritual: 'Tour Hành Hương Tâm Linh',
      experience: 'Tour Trải Nghiệm & Thiên Nhiên',
      charity: 'Tour Thiện Nguyện Ý Nghĩa',
      near_hanoi: 'Tour Gần Hà Nội Trong Ngày'
    }};
    titleEl.textContent = titles[cat] || 'Danh Sách Tour';
  }}
}}
window.filterByCategory = filterByCategory;

// ==========================================
// 10. PROFESSIONAL STORYTELLING MODAL CONTROLLER (4 TABS)
// ==========================================
function openTourDetailModal(tourId, initialTab = 1) {{
  const tour = TOURS_DATA.find(t => t.id === tourId) || TOURS_DATA[0];
  if (!tour) return;

  const modal = document.getElementById('tour-detail-modal');
  const content = document.getElementById('tour-detail-content');
  if (!modal || !content) return;

  const isLiked = wishlist.has(tour.id);
  const dates = tour.departureDates ? tour.departureDates.join(', ') : 'Thứ 6 & Thứ 7 hàng tuần';

  // Render 1-5 difficulty dots
  let diffDots = '';
  for (let i = 1; i <= 5; i++) {{
    diffDots += `<span class="difficulty-dot ${{i <= tour.difficultyLevel ? 'active' : ''}}"></span>`;
  }}

  content.innerHTML = `
    <div class="relative bg-white rounded-3xl overflow-hidden shadow-2xl max-w-3xl w-full border border-gray-100 modal-enter max-h-[92vh] flex flex-col">
      
      <!-- Top Image Banner & Close Button -->
      <div class="relative h-60 sm:h-72 w-full shrink-0">
        <img 
          id="modal-main-image"
          src="${{tour.image}}" 
          alt="${{tour.title}}" 
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
            <span class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-[#1E4D3B] text-white">${{tour.badge}}</span>
            <span class="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-white/20 backdrop-blur-sm text-white">${{tour.altitudeBadge}}</span>
            <span class="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-white/20 backdrop-blur-sm text-white">${{tour.duration}}</span>
            <span class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-amber-400 text-stone-900">${{tour.code}}</span>
          </div>
          <h2 class="text-xl sm:text-2xl font-black leading-tight drop-shadow-sm">${{tour.title}}</h2>
          <p class="text-xs sm:text-sm text-emerald-200 mt-1 flex items-center gap-2">
            <i data-lucide="map-pin" class="w-3.5 h-3.5 text-emerald-300"></i>
            <span>${{tour.location}} • Điểm đón: ${{tour.pickupPoint || '55 Nguyễn Quốc Trị & 489 Hoàng Quốc Việt'}}</span>
          </p>
        </div>
      </div>

      <!-- Key Specs Bar -->
      <div class="grid grid-cols-4 gap-2 px-5 py-3 bg-[#F6F7F2] border-b border-gray-100 text-center shrink-0">
        <div>
          <span class="block text-[10px] font-bold uppercase tracking-wider text-gray-500">Độ cao</span>
          <span class="block text-xs sm:text-sm font-extrabold text-forest mt-0.5">${{tour.altitude}}</span>
        </div>
        <div class="border-l border-gray-200">
          <span class="block text-[10px] font-bold uppercase tracking-wider text-gray-500">Quãng đường</span>
          <span class="block text-xs sm:text-sm font-extrabold text-gray-900 mt-0.5">${{tour.trekDistance}}</span>
        </div>
        <div class="border-l border-gray-200">
          <span class="block text-[10px] font-bold uppercase tracking-wider text-gray-500">Độ khó (${{tour.difficultyLevel}}/5)</span>
          <div class="difficulty-meter mt-1 justify-center">
            ${{diffDots}}
          </div>
        </div>
        <div class="border-l border-gray-200">
          <span class="block text-[10px] font-bold uppercase tracking-wider text-gray-500">Khởi hành</span>
          <span class="block text-xs sm:text-sm font-extrabold text-gray-900 mt-0.5">${{tour.minPax}}</span>
        </div>
      </div>

      <!-- Storytelling Tabs Navigation (4 TABS) -->
      <div class="flex items-center gap-4 sm:gap-6 px-5 sm:px-6 pt-3 border-b border-gray-100 bg-white text-xs sm:text-sm shrink-0 overflow-x-auto no-scrollbar whitespace-nowrap">
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
        <button 
          id="tab-btn-4" 
          onclick="switchDetailTab(4)"
          class="modal-tab-btn cursor-pointer flex items-center gap-1.5 text-forest"
        >
          <i data-lucide="shield-check" class="w-3.5 h-3.5 text-forest"></i>
          <span>4. Chính sách hoàn hủy & Dịch vụ</span>
        </button>
      </div>

      <!-- Tab Content Panels -->
      <div class="p-5 sm:p-6 overflow-y-auto flex-1 space-y-4 text-xs sm:text-sm text-gray-700 leading-relaxed">
        
        <!-- PANEL 1: Hành trình & Lộ trình địa lý -->
        <div id="tab-panel-1" class="space-y-4">
          <!-- Visual Route Steps -->
          <div class="space-y-2">
            <h4 class="text-xs font-bold uppercase tracking-wider text-forest flex items-center gap-1.5">
              <i data-lucide="map-pin" class="w-4 h-4 text-forest"></i>
              <span>Sơ đồ các chặng hành trình</span>
            </h4>
            <div class="flex flex-wrap items-center gap-1.5 sm:gap-2 p-3 bg-emerald-50/70 rounded-2xl border border-emerald-100">
              ${{(tour.routeSteps || []).map((step, idx, arr) => `
                <span class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-white border border-emerald-200 text-forest font-bold text-xs shadow-2xs">
                  <span class="w-4 h-4 rounded-full bg-forest text-white text-[10px] flex items-center justify-center font-extrabold shrink-0">${{idx + 1}}</span>
                  <span>${{step}}</span>
                </span>
                ${{idx < arr.length - 1 ? '<i data-lucide="chevron-right" class="w-3.5 h-3.5 text-emerald-600 shrink-0"></i>' : ''}}
              `).join('')}}
            </div>
          </div>

          <!-- Geographic Itinerary Description -->
          <div class="space-y-1.5">
            <h4 class="text-xs font-bold uppercase tracking-wider text-gray-800 flex items-center gap-1.5">
              <i data-lucide="map" class="w-4 h-4 text-forest"></i>
              <span>Lộ trình chi tiết</span>
            </h4>
            <p class="text-xs sm:text-sm text-gray-700 leading-relaxed bg-gray-50 p-3.5 rounded-xl border border-gray-100 font-normal">
              ${{tour.routeMap || tour.description}}
            </p>
          </div>
          
          <!-- Highlights -->
          <div class="space-y-2.5 pt-1">
            <h4 class="text-xs font-bold uppercase tracking-wider text-forest">Trải nghiệm độc bản không thể bỏ lỡ</h4>
            <ul class="space-y-2">
              ${{(tour.highlights || []).map(hl => `
                <li class="flex items-start gap-2.5">
                  <i data-lucide="check-circle-2" class="w-4 h-4 text-forest shrink-0 mt-0.5"></i>
                  <span>${{hl}}</span>
                </li>
              `).join('')}}
            </ul>
          </div>

          <!-- Real Photos Gallery from Expedition -->
          ${{tour.gallery && tour.gallery.length > 0 ? `
            <div class="space-y-2.5 pt-2">
              <div class="flex items-center justify-between">
                <h4 class="text-xs font-bold uppercase tracking-wider text-forest flex items-center gap-1.5">
                  <i data-lucide="camera" class="w-4 h-4 text-forest"></i>
                  <span>Khoảnh khắc thực tế từ các chuyến đi của Đi Cùng Gió</span>
                </h4>
                <span class="text-[10px] text-gray-500 font-medium">Bấm vào ảnh để xem lớn</span>
              </div>
              <div class="grid grid-cols-2 sm:grid-cols-4 gap-2.5">
                ${{tour.gallery.map(g => `
                  <div 
                    onclick="switchModalImage('${{g.url}}')"
                    class="group/img relative rounded-xl overflow-hidden aspect-[4/3] bg-gray-100 shadow-2xs border border-gray-200 cursor-pointer hover:border-emerald-500 hover:ring-2 hover:ring-emerald-400/40 transition-all"
                    title="${{g.caption}} - Bấm để phóng to lên banner"
                  >
                    <img 
                      src="${{g.url}}" 
                      alt="${{g.caption}}" 
                      loading="lazy"
                      onerror="this.onerror=null; this.src='assets/images/tour-yen-tu.jpg';"
                      class="w-full h-full object-cover group-hover/img:scale-108 transition-transform duration-500"
                    />
                    <div class="absolute inset-0 bg-gradient-to-t from-black/85 via-black/25 to-transparent opacity-0 group-hover/img:opacity-100 transition-opacity duration-200 p-2 flex items-end">
                      <span class="text-[10px] text-white font-medium leading-tight">${{g.caption}}</span>
                    </div>
                  </div>
                `).join('')}}
              </div>
            </div>
          ` : ''}}

          <div class="p-3 bg-emerald-50/70 rounded-xl border border-emerald-100 flex items-center justify-between">
            <div>
              <span class="text-xs font-bold text-forest block">Lịch khởi hành sắp tới:</span>
              <span class="text-xs text-gray-600 font-medium">${{dates}} (${{tour.departureFrequency}})</span>
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
                Lịch sử & Huyền thoại ngọn núi ${{tour.title}}
              </h4>
            </div>
            
            <p class="text-xs sm:text-sm text-gray-700 leading-relaxed font-normal">
              ${{tour.historyStory || tour.description}}
            </p>

            <div class="pt-3 text-[11px] text-gray-500 italic border-t border-stone-200/70 flex items-center gap-2">
              <i data-lucide="sparkles" class="w-4 h-4 text-amber-500 shrink-0"></i>
              <span>Mỗi hành trình của Trekking Đi Cùng Gió không chỉ là thể lực, mà là một trải nghiệm chạm vào chiều sâu văn hóa và lịch sử đất nước.</span>
            </div>
          </div>
        </div>

        <!-- PANEL 3: Lịch trình & Chuẩn bị -->
        <div id="tab-panel-3" class="hidden space-y-4">
          <!-- Day-by-Day Timeline -->
          <div class="space-y-3">
            <h4 class="text-xs font-bold uppercase tracking-wider text-forest flex items-center gap-1.5">
              <i data-lucide="calendar" class="w-4 h-4 text-forest"></i>
              <span>Lịch trình chi tiết các chặng</span>
            </h4>
            <div class="relative pl-6 space-y-4 before:content-[''] before:absolute before:left-2.5 before:top-2 before:bottom-2 before:w-0.5 before:bg-emerald-200">
              ${{(tour.itinerary || []).map(step => `
                <div class="relative group">
                  <div class="absolute -left-[27px] top-1 w-4 h-4 rounded-full border-2 border-white bg-forest shadow-xs"></div>
                  <h5 class="font-bold text-gray-900 text-xs sm:text-sm flex items-center gap-2">
                    <span class="px-2 py-0.5 rounded-md bg-emerald-100 text-forest text-[11px] font-extrabold">${{step.day}}</span>
                    <span>${{step.title}}</span>
                  </h5>
                  <p class="text-xs text-gray-600 mt-1 leading-relaxed">${{step.desc}}</p>
                </div>
              `).join('')}}
            </div>
          </div>

          <!-- Included & Preparation Checklist -->
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 pt-2">
            <!-- Included -->
            <div class="bg-gray-50 p-4 rounded-2xl border border-gray-100 space-y-2">
              <h5 class="font-bold text-xs text-forest uppercase tracking-wider flex items-center gap-1.5">
                <i data-lucide="check" class="w-4 h-4 text-forest"></i>
                <span>Dịch vụ bao gồm</span>
              </h5>
              <ul class="text-xs text-gray-600 space-y-1.5">
                ${{(tour.included || []).map(inc => `
                  <li class="flex items-start gap-2">
                    <span class="text-forest font-bold">•</span>
                    <span>${{inc}}</span>
                  </li>
                `).join('')}}
              </ul>
            </div>

            <!-- Preparation -->
            <div class="bg-emerald-50/50 p-4 rounded-2xl border border-emerald-100/70 space-y-2">
              <h5 class="font-bold text-xs text-forest uppercase tracking-wider flex items-center gap-1.5">
                <i data-lucide="backpack" class="w-4 h-4 text-forest"></i>
                <span>Đồ cần chuẩn bị</span>
              </h5>
              <ul class="text-xs text-gray-700 space-y-1.5">
                ${{(tour.preparation || []).map(prep => `
                  <li class="flex items-start gap-2">
                    <span class="text-amber-600 font-bold">✔</span>
                    <span>${{prep}}</span>
                  </li>
                `).join('')}}
              </ul>
            </div>
          </div>
        </div>

        <!-- PANEL 4: CHÍNH SÁCH HOÀN HỦY & DỊCH VỤ -->
        <div id="tab-panel-4" class="hidden space-y-4">
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
              * Tour đặc thù mùa vụ (Cúc Phương mùa bướm): Trước 15 ngày hoàn 100%, 5–10 ngày bảo lưu 45 ngày, dưới 5 ngày không hoàn/hủy.
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

          <!-- Services Included & Excluded -->
          <div class="space-y-2 pt-1">
            <h4 class="text-xs font-bold uppercase tracking-wider text-forest flex items-center gap-1.5">
              <i data-lucide="sparkles" class="w-4 h-4 text-forest"></i>
              <span>Dịch vụ tiêu chuẩn độc quyền của Đi Cùng Gió</span>
            </h4>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs text-gray-700">
              <div class="flex items-start gap-2 bg-white p-2.5 rounded-xl border border-gray-100 shadow-2xs">
                <i data-lucide="award" class="w-4 h-4 text-amber-600 shrink-0 mt-0.5"></i>
                <span><strong>Huy chương gỗ độc quyền:</strong> Khắc kỷ niệm riêng, thân thiện môi trường</span>
              </div>
              <div class="flex items-start gap-2 bg-white p-2.5 rounded-xl border border-gray-100 shadow-2xs">
                <i data-lucide="users" class="w-4 h-4 text-forest shrink-0 mt-0.5"></i>
                <span><strong>Đội ngũ chuyên nghiệp:</strong> 1 Leader + Porter chu đáo trên mỗi 8-10 khách</span>
              </div>
              <div class="flex items-start gap-2 bg-white p-2.5 rounded-xl border border-gray-100 shadow-2xs">
                <i data-lucide="shield-check" class="w-4 h-4 text-forest shrink-0 mt-0.5"></i>
                <span><strong>Bảo hiểm du lịch:</strong> Trọn gói bồi thường từ 20.000.000đ – 100.000.000đ/vụ</span>
              </div>
              <div class="flex items-start gap-2 bg-white p-2.5 rounded-xl border border-gray-100 shadow-2xs">
                <i data-lucide="compass" class="w-4 h-4 text-forest shrink-0 mt-0.5"></i>
                <span><strong>Gậy & Đồ bảo hộ:</strong> Gậy trekking, đèn pin đeo đầu & túi y tế sơ cứu</span>
              </div>
            </div>
          </div>

          <!-- Health and Responsibility Note -->
          <div class="p-3 bg-amber-50/80 border-l-4 border-amber-500 rounded-r-xl text-[11px] text-amber-950 leading-relaxed">
            <strong>Lưu ý trách nhiệm & Sức khỏe:</strong> Quý khách bắt buộc mang CCCD/Hộ chiếu bản gốc. Tự bảo đảm thể lực và khai báo y tế trung thực. Tuân thủ nghiêm ngặt nguyên tắc bảo vệ thiên nhiên (Không xả rác, mang toàn bộ rác xuống núi).
          </div>
        </div>

      </div>

      <!-- Modal Footer -->
      <div class="p-4 sm:p-5 border-t border-gray-100 bg-gray-50 flex items-center justify-between gap-4 shrink-0">
        <div>
          <span class="block text-[11px] text-gray-500">Giá tour trọn gói</span>
          <span class="block text-base sm:text-lg font-black text-forest leading-tight">${{tour.price}}</span>
        </div>

        <div class="flex items-center gap-3">
          <button 
            type="button" 
            onclick="toggleWishlist(${{tour.id}}); openTourDetailModal(${{tour.id}});" 
            class="p-2.5 rounded-full border border-gray-200 bg-white text-gray-600 hover:text-red-500 hover:border-red-200 transition-colors shrink-0 shadow-sm cursor-pointer"
            title="Lưu yêu thích"
          >
            <i data-lucide="heart" class="w-5 h-5 ${{isLiked ? 'fill-red-500 text-red-500' : ''}}"></i>
          </button>

          <button 
            type="button" 
            onclick="closeTourDetailModal(); openSmartBookingModal(${{tour.id}});" 
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
}}

function closeTourDetailModal() {{
  const modal = document.getElementById('tour-detail-modal');
  if (modal) {{
    modal.classList.add('hidden');
    document.body.style.overflow = '';
  }}
}}

// Switch modal top preview image on thumbnail click
window.switchModalImage = function(imgUrl) {{
  const img = document.getElementById('modal-main-image');
  if (img) {{
    img.style.opacity = '0.35';
    setTimeout(() => {{
      img.src = imgUrl;
      img.style.opacity = '1';
    }}, 150);
  }}
}};

// Switch tabs inside detail modal (1 to 4)
window.switchDetailTab = function(tabIndex) {{
  for (let i = 1; i <= 4; i++) {{
    const btn = document.getElementById(`tab-btn-${{i}}`);
    const panel = document.getElementById(`tab-panel-${{i}}`);
    if (btn && panel) {{
      if (i === tabIndex) {{
        btn.classList.add('active');
        panel.classList.remove('hidden');
      }} else {{
        btn.classList.remove('active');
        panel.classList.add('hidden');
      }}
    }}
  }}
  initLucideIcons();
}};

window.openTourDetailModal = openTourDetailModal;
window.closeTourDetailModal = closeTourDetailModal;

// ==========================================
// 10B. GLOBAL POLICY MODAL CONTROLLER
// ==========================================
window.openPolicyModal = function() {{
  const modal = document.getElementById('policy-modal');
  if (modal) {{
    modal.classList.remove('hidden');
    document.body.style.overflow = 'hidden';
    initLucideIcons();
  }}
}};

window.closePolicyModal = function() {{
  const modal = document.getElementById('policy-modal');
  if (modal) {{
    modal.classList.add('hidden');
    document.body.style.overflow = '';
  }}
}};

// ==========================================
// 11. SMART BOOKING MODAL WITH LIVE CALCULATOR
// ==========================================
function openSmartBookingModal(tourId = 1, defaultDate = '') {{
  currentBookingTour = TOURS_DATA.find(t => t.id === tourId) || TOURS_DATA[0];
  bookingGuests = 1;

  const modal = document.getElementById('booking-modal');
  const select = document.getElementById('booking-tour-select');
  const dateInput = document.getElementById('booking-date-input');
  const formBox = document.getElementById('booking-form-box');
  const successBox = document.getElementById('booking-success-box');

  if (!modal) return;

  // Populate Select options if empty
  if (select) {{
    select.innerHTML = TOURS_DATA.map(t => `
      <option value="${{t.id}}" ${{t.id === currentBookingTour.id ? 'selected' : ''}}>
        ${{t.code ? `[${{t.code}}] ` : ''}}${{t.title}} – ${{t.price}} (${{t.duration}})
      </option>
    `).join('');
    
    select.onchange = (e) => {{
      const selectedId = parseInt(e.target.value, 10);
      currentBookingTour = TOURS_DATA.find(t => t.id === selectedId) || TOURS_DATA[0];
      updateBookingCalculation();
    }};
  }}

  // Pre-fill date
  if (dateInput) {{
    if (defaultDate) {{
      dateInput.value = defaultDate;
    }} else if (currentBookingTour.departureDates && currentBookingTour.departureDates.length > 0) {{
      dateInput.value = currentBookingTour.departureDates[0];
    }} else {{
      dateInput.value = 'Thứ 6 tuần tới';
    }}
  }}

  // Reset form and show
  if (formBox) formBox.classList.remove('hidden');
  if (successBox) successBox.classList.add('hidden');

  updateBookingCalculation();
  modal.classList.remove('hidden');
  document.body.style.overflow = 'hidden';
  initLucideIcons();
}}

function closeBookingModal() {{
  const modal = document.getElementById('booking-modal');
  if (modal) {{
    modal.classList.add('hidden');
    document.body.style.overflow = '';
  }}
}}

// Adjust guests with plus / minus buttons
window.adjustBookingGuests = function(delta) {{
  const newCount = bookingGuests + delta;
  if (newCount >= 1 && newCount <= 20) {{
    bookingGuests = newCount;
    updateBookingCalculation();
  }}
}};

// Calculate and render live price breakdown
function updateBookingCalculation() {{
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
        <span>Đơn giá (${{bookingGuests}} khách):</span>
        <span class="font-bold text-gray-900">${{formatCurrency(priceEach)}} × ${{bookingGuests}} = ${{formatCurrency(subtotal)}}</span>
      </div>
      ${{isGroupDiscount ? `
        <div class="flex justify-between items-center text-emerald-700 font-bold">
          <span>Ưu đãi nhóm (≥4 khách giảm 5%):</span>
          <span>- ${{formatCurrency(discountAmount)}}</span>
        </div>
      ` : `
        <div class="text-[11px] text-gray-500 italic">
          💡 Đặt từ 4 người trở lên được giảm thêm 5% tổng hoá đơn.
        </div>
      `}}
      <div class="pt-2 border-t border-emerald-200/80 flex justify-between items-center">
        <span class="font-bold text-gray-800 text-xs sm:text-sm">Tổng thanh toán dự kiến:</span>
        <span class="font-black text-forest text-base sm:text-lg">${{formatCurrency(finalTotal)}}</span>
      </div>
      <!-- Cancellation reassurance link -->
      <div class="flex items-center justify-between text-[11px] text-forest pt-1 border-t border-emerald-100/60">
        <span class="flex items-center gap-1 font-semibold">
          <i data-lucide="shield-check" class="w-3.5 h-3.5"></i>
          Cam kết hoàn 100% trước 10 ngày
        </span>
        <button type="button" onclick="openPolicyModal()" class="text-emerald-700 underline hover:text-emerald-900 cursor-pointer">
          Xem chính sách hoàn hủy
        </button>
      </div>
    </div>
  `;
  initLucideIcons();
}}

// Booking Form Submit Event
function setupBookingModalEvents() {{
  const form = document.getElementById('booking-form');
  if (!form) return;

  form.addEventListener('submit', (e) => {{
    e.preventDefault();
    const name = document.getElementById('booking-name')?.value.trim();
    const phone = document.getElementById('booking-phone')?.value.trim();
    const date = document.getElementById('booking-date-input')?.value.trim();

    if (!name || name.length < 2) {{
      showToast('Thông tin chưa hợp lệ', 'Vui lòng nhập họ và tên đầy đủ của bạn.', 'error');
      return;
    }}

    const phoneRegex = /^(0[3|5|7|8|9])[0-9]{{8}}$/;
    if (!phoneRegex.test(phone)) {{
      showToast('Số điện thoại không hợp lệ', 'Vui lòng nhập số điện thoại Việt Nam gồm 10 chữ số (VD: 0965983302).', 'error');
      return;
    }}

    const randomCode = '#DCG-' + Math.floor(100000 + Math.random() * 900000);
    const subtotal = currentBookingTour.priceNum * bookingGuests;
    const isGroupDiscount = bookingGuests >= 4;
    const finalTotal = isGroupDiscount ? subtotal * 0.95 : subtotal;

    const formBox = document.getElementById('booking-form-box');
    const successBox = document.getElementById('booking-success-box');
    
    if (formBox && successBox) {{
      formBox.classList.add('hidden');
      successBox.classList.remove('hidden');

      successBox.innerHTML = `
        <div class="text-center py-6 space-y-4">
          <div class="w-16 h-16 rounded-full bg-emerald-100 text-forest mx-auto flex items-center justify-center animate-bounce">
            <i data-lucide="check-circle" class="w-10 h-10"></i>
          </div>
          
          <div>
            <span class="text-xs font-bold uppercase tracking-wider text-emerald-600 block">Đăng ký thành công!</span>
            <h3 class="text-xl font-black text-gray-900 mt-1">Hẹn gặp bạn trên những đỉnh núi!</h3>
            <p class="text-xs text-gray-600 mt-1">Mã giữ chỗ tạm thời của bạn: <strong class="text-forest text-sm">${{randomCode}}</strong></p>
          </div>

          <div class="p-4 bg-emerald-50 rounded-2xl text-left text-xs text-gray-700 space-y-1.5 border border-emerald-100">
            <div class="flex justify-between">
              <span class="text-gray-500">Hành trình:</span>
              <span class="font-bold text-gray-900 text-right">${{currentBookingTour.title}}</span>
            </div>
            <div class="flex justify-between">
              <span class="text-gray-500">Khách hàng:</span>
              <span class="font-bold text-gray-900">${{name}}</span>
            </div>
            <div class="flex justify-between">
              <span class="text-gray-500">Số điện thoại:</span>
              <span class="font-bold text-gray-900">${{phone}}</span>
            </div>
            <div class="flex justify-between">
              <span class="text-gray-500">Số lượng khách:</span>
              <span class="font-bold text-gray-900">${{bookingGuests}} người</span>
            </div>
            <div class="flex justify-between">
              <span class="text-gray-500">Dự kiến khởi hành:</span>
              <span class="font-bold text-gray-900">${{date}}</span>
            </div>
            <div class="flex justify-between">
              <span class="text-gray-500">Điểm đón Hà Nội:</span>
              <span class="font-bold text-forest">55 Nguyễn Quốc Trị / 489 HQV</span>
            </div>
            <div class="pt-2 border-t border-emerald-200 flex justify-between items-center">
              <span class="font-bold text-gray-900">Tổng chi phí:</span>
              <span class="font-black text-forest text-base">${{formatCurrency(finalTotal)}}</span>
            </div>
          </div>

          <p class="text-[11px] text-gray-500 italic">
            Tư vấn viên Đi Cùng Gió sẽ liên hệ qua Zalo/Điện thoại trong vòng 15 phút để xác nhận và gửi checklist chuẩn bị!
          </p>

          <button 
            type="button" 
            onclick="closeBookingModal()" 
            class="w-full py-3 rounded-full bg-forest text-white font-bold text-xs sm:text-sm hover:bg-forest/90 transition-all cursor-pointer shadow-sm"
          >
            Hoàn tất & Quay lại trang chủ
          </button>
        </div>
      `;

      initLucideIcons();
      showToast('Đăng ký thành công!', `Mã tour ${{randomCode}} đã được ghi nhận. Chúng tôi sẽ liên hệ bạn ngay!`, 'success');
    }}
  }});
}}

window.openSmartBookingModal = openSmartBookingModal;
window.closeBookingModal = closeBookingModal;

// ==========================================
// 12. WISHLIST & DRAWER SYSTEM
// ==========================================
window.toggleWishlist = function(tourId, e) {{
  if (e) e.stopPropagation();
  const tour = TOURS_DATA.find(t => t.id === tourId);
  if (!tour) return;

  if (wishlist.has(tourId)) {{
    wishlist.delete(tourId);
    showToast('Đã xóa khỏi yêu thích', `Đã bỏ lưu "${{tour.title}}".`, 'info');
  }} else {{
    wishlist.add(tourId);
    showToast('Đã lưu vào yêu thích', `"${{tour.title}}" đã được thêm vào danh sách quan tâm!`, 'success');
  }}

  try {{
    localStorage.setItem('dicunggio_wishlist', JSON.stringify(Array.from(wishlist)));
  }} catch (err) {{}}

  updateWishlistBadges();
  renderTours();
  renderWishlistDrawer();
}};

function updateWishlistBadges() {{
  const count = wishlist.size;
  const badges = document.querySelectorAll('#header-cart-badge, #mobile-wishlist-badge');
  badges.forEach(b => {{
    b.textContent = count;
    if (count > 0) {{
      b.classList.remove('hidden');
    }} else {{
      b.classList.add('hidden');
    }}
  }});
}}

window.openWishlistDrawer = function() {{
  const drawer = document.getElementById('wishlist-drawer');
  const backdrop = document.getElementById('wishlist-drawer-backdrop');
  renderWishlistDrawer();
  if (drawer && backdrop) {{
    backdrop.classList.remove('hidden');
    drawer.classList.remove('translate-x-full');
    document.body.style.overflow = 'hidden';
  }}
}};

window.closeWishlistDrawer = function() {{
  const drawer = document.getElementById('wishlist-drawer');
  const backdrop = document.getElementById('wishlist-drawer-backdrop');
  if (drawer && backdrop) {{
    drawer.classList.add('translate-x-full');
    setTimeout(() => {{
      backdrop.classList.add('hidden');
      document.body.style.overflow = '';
    }}, 300);
  }}
}};

function renderWishlistDrawer() {{
  const container = document.getElementById('wishlist-items-container');
  if (!container) return;

  const savedTours = TOURS_DATA.filter(t => wishlist.has(t.id));

  if (savedTours.length === 0) {{
    container.innerHTML = `
      <div class="text-center py-12 space-y-3">
        <div class="w-12 h-12 rounded-full bg-gray-100 text-gray-400 mx-auto flex items-center justify-center">
          <i data-lucide="heart-off" class="w-6 h-6"></i>
        </div>
        <p class="text-xs text-gray-500 font-medium">Bạn chưa lưu tour nào vào danh sách yêu thích.</p>
        <button 
          onclick="closeWishlistDrawer()"
          class="px-4 py-2 rounded-full bg-forest text-white text-xs font-bold hover:bg-forest/90 transition-colors cursor-pointer"
        >
          Khám phá tour ngay
        </button>
      </div>
    `;
    initLucideIcons();
    return;
  }}

  container.innerHTML = savedTours.map(tour => `
    <div class="flex items-center gap-3 p-3 bg-gray-50 rounded-2xl border border-gray-100">
      <img 
        src="${{tour.image}}" 
        alt="${{tour.title}}" 
        onerror="this.onerror=null; this.src='assets/images/tour-yen-tu.jpg';"
        class="w-16 h-16 rounded-xl object-cover shrink-0 cursor-pointer"
        onclick="openTourDetailModal(${{tour.id}}); closeWishlistDrawer();"
      />
      <div class="flex-1 min-w-0">
        <h4 
          class="font-bold text-xs text-gray-900 truncate hover:text-forest transition-colors cursor-pointer"
          onclick="openTourDetailModal(${{tour.id}}); closeWishlistDrawer();"
        >
          ${{tour.title}}
        </h4>
        <p class="text-xs font-black text-forest mt-0.5">${{tour.price}}</p>
        <div class="flex items-center gap-2 mt-1">
          <button 
            type="button" 
            onclick="closeWishlistDrawer(); openSmartBookingModal(${{tour.id}});"
            class="text-[11px] font-bold text-white bg-forest px-2.5 py-0.5 rounded-full hover:bg-forest/90 transition-colors"
          >
            Đăng ký
          </button>
          <button 
            type="button" 
            onclick="toggleWishlist(${{tour.id}})"
            class="text-[11px] text-gray-400 hover:text-red-500 transition-colors"
          >
            Xóa
          </button>
        </div>
      </div>
    </div>
  `).join('');

  initLucideIcons();
}}

// ==========================================
// 13. SEARCH OVERLAY & REAL-TIME FILTER
// ==========================================
window.openSearchModal = function() {{
  const modal = document.getElementById('search-modal');
  const input = document.getElementById('search-input');
  if (modal) {{
    modal.classList.remove('hidden');
    document.body.style.overflow = 'hidden';
    if (input) {{
      input.value = '';
      input.focus();
      handleSearchInput('');
    }}
    initLucideIcons();
  }}
}};

window.closeSearchModal = function() {{
  const modal = document.getElementById('search-modal');
  if (modal) {{
    modal.classList.add('hidden');
    document.body.style.overflow = '';
  }}
}};

window.handleSearchInput = function(query) {{
  const container = document.getElementById('search-results-container');
  if (!container) return;

  const q = query.trim().toLowerCase();
  let results = TOURS_DATA;

  if (q.length > 0) {{
    results = TOURS_DATA.filter(t => 
      t.title.toLowerCase().includes(q) ||
      (t.code && t.code.toLowerCase().includes(q)) ||
      t.location.toLowerCase().includes(q) ||
      t.description.toLowerCase().includes(q)
    );
  }}

  if (results.length === 0) {{
    container.innerHTML = `
      <div class="text-center py-8 text-xs text-gray-400">
        Không tìm thấy hành trình phù hợp với từ khóa "${{query}}".
      </div>
    `;
    return;
  }}

  container.innerHTML = results.slice(0, 6).map(tour => `
    <div 
      onclick="closeSearchModal(); openTourDetailModal(${{tour.id}});"
      class="p-2.5 rounded-xl hover:bg-gray-50 flex items-center gap-3 cursor-pointer transition-colors border border-transparent hover:border-gray-100"
    >
      <img 
        src="${{tour.image}}" 
        alt="${{tour.title}}" 
        onerror="this.onerror=null; this.src='assets/images/tour-yen-tu.jpg';"
        class="w-12 h-12 rounded-lg object-cover shrink-0"
      />
      <div class="flex-1 min-w-0">
        <h5 class="text-xs font-bold text-gray-900 truncate">${{tour.title}}</h5>
        <p class="text-[11px] text-gray-500">${{tour.location}} • ${{tour.duration}}</p>
      </div>
      <span class="text-xs font-black text-forest shrink-0">${{tour.price}}</span>
    </div>
  `).join('');
}};

// ==========================================
// 14. VIDEO MODAL LIGHTBOX
// ==========================================
window.openVideoModal = function() {{
  const modal = document.getElementById('video-modal');
  const frame = document.getElementById('video-frame');
  if (modal && frame) {{
    frame.src = 'https://www.youtube.com/embed/dQw4w9WgXcQ?autoplay=1';
    modal.classList.remove('hidden');
    document.body.style.overflow = 'hidden';
    initLucideIcons();
  }}
}};

window.closeVideoModal = function() {{
  const modal = document.getElementById('video-modal');
  const frame = document.getElementById('video-frame');
  if (modal && frame) {{
    frame.src = '';
    modal.classList.add('hidden');
    document.body.style.overflow = '';
  }}
}};

// ==========================================
// 15. REVIEWS & TESTIMONIALS MODAL
// ==========================================
window.openReviewsModal = function() {{
  const modal = document.getElementById('reviews-modal');
  const container = document.getElementById('reviews-list-container');
  if (!modal || !container) return;

  container.innerHTML = TESTIMONIALS_DATA.map(rev => `
    <div class="p-4 bg-gray-50/80 rounded-2xl border border-gray-100 space-y-2">
      <div class="flex items-center justify-between">
        <div class="flex items-center gap-2.5">
          <img src="${{rev.avatar}}" alt="${{rev.name}}" class="w-9 h-9 rounded-full object-cover border border-emerald-100 shadow-2xs" />
          <div>
            <h5 class="font-bold text-xs text-gray-900 leading-tight">${{rev.name}}</h5>
            <span class="text-[10px] text-forest font-medium">${{rev.role}}</span>
          </div>
        </div>
        <div class="flex text-amber-400">
          ${{Array(rev.rating).fill('<i data-lucide=\"star\" class=\"w-3 h-3 fill-amber-400 text-amber-400\"></i>').join('')}}
        </div>
      </div>
      <p class="text-xs text-gray-700 italic leading-relaxed">${{rev.comment}}</p>
      <span class="text-[10px] text-gray-400 block text-right">${{rev.date}}</span>
    </div>
  `).join('');

  modal.classList.remove('hidden');
  document.body.style.overflow = 'hidden';
  initLucideIcons();
}};

window.closeReviewsModal = function() {{
  const modal = document.getElementById('reviews-modal');
  if (modal) {{
    modal.classList.add('hidden');
    document.body.style.overflow = '';
  }}
}};

function setupReviewsModalEvents() {{
  const form = document.getElementById('add-review-form');
  if (!form) return;

  form.addEventListener('submit', (e) => {{
    e.preventDefault();
    const name = document.getElementById('review-author-input')?.value.trim();
    const tour = document.getElementById('review-tour-input')?.value.trim();
    const text = document.getElementById('review-content-input')?.value.trim();

    if (!name || !text) {{
      showToast('Thiếu thông tin', 'Vui lòng nhập tên và nội dung đánh giá.', 'error');
      return;
    }}

    TESTIMONIALS_DATA.unshift({{
      id: Date.now(),
      name: name,
      role: tour || 'Trekker Đi Cùng Gió',
      avatar: 'assets/images/avatar-ha.jpg',
      comment: text,
      rating: 5,
      date: 'Vừa xong'
    }});

    form.reset();
    showToast('Cảm ơn bạn!', 'Đánh giá của bạn đã được gửi thành công!', 'success');
    openReviewsModal();
  }});
}}

// ==========================================
// 16. TOAST NOTIFICATION UTILITY
// ==========================================
function showToast(title, message, type = 'info') {{
  const toast = document.createElement('div');
  toast.className = `fixed bottom-5 right-5 z-50 max-w-sm w-full p-4 rounded-2xl bg-white shadow-2xl border border-gray-100 flex items-start gap-3 transform translate-y-10 opacity-0 transition-all duration-300 pointer-events-auto`;

  let iconHtml = '<i data-lucide=\"info\" class=\"w-5 h-5 text-forest shrink-0 mt-0.5\"></i>';
  if (type === 'success') {{
    iconHtml = '<i data-lucide=\"check-circle-2\" class=\"w-5 h-5 text-emerald-600 shrink-0 mt-0.5\"></i>';
  }} else if (type === 'error') {{
    iconHtml = '<i data-lucide=\"alert-circle\" class=\"w-5 h-5 text-red-500 shrink-0 mt-0.5\"></i>';
  }}

  toast.innerHTML = `
    ${{iconHtml}}
    <div class="flex-1 min-w-0">
      <h5 class="text-xs font-bold text-gray-900">${{title}}</h5>
      <p class="text-[11px] text-gray-500 mt-0.5 leading-snug">${{message}}</p>
    </div>
    <button onclick="this.parentElement.remove()" class="text-gray-400 hover:text-gray-600 p-1">
      <i data-lucide=\"x\" class=\"w-3.5 h-3.5\"></i>
    </button>
  `;

  document.body.appendChild(toast);
  initLucideIcons();

  requestAnimationFrame(() => {{
    toast.classList.remove('translate-y-10', 'opacity-0');
  }});

  setTimeout(() => {{
    toast.classList.add('translate-y-10', 'opacity-0');
    setTimeout(() => toast.remove(), 300);
  }}, 3500);
}}
window.showToast = showToast;

// ==========================================
// 17. SCROLL OBSERVERS & INTERACTIONS
// ==========================================
function setupScrollReveal() {{
  const elements = document.querySelectorAll('.reveal-on-scroll');
  if (!elements.length) return;

  const observer = new IntersectionObserver((entries) => {{
    entries.forEach(entry => {{
      if (entry.isIntersecting) {{
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }}
    }});
  }}, {{ threshold: 0.1 }});

  elements.forEach(el => observer.observe(el));
}}

function setupScrollSpy() {{
  const sections = document.querySelectorAll('section[id], main[id]');
  const navLinks = document.querySelectorAll('.nav-link');

  window.addEventListener('scroll', () => {{
    let current = '';
    const scrollPos = window.scrollY + 200;

    sections.forEach(section => {{
      const sectionTop = section.offsetTop;
      const sectionHeight = section.offsetHeight;
      if (scrollPos >= sectionTop && scrollPos < sectionTop + sectionHeight) {{
        current = section.getAttribute('id');
      }}
    }});

    navLinks.forEach(link => {{
      const href = link.getAttribute('href');
      if (href && href.startsWith('#')) {{
        const targetId = href.substring(1);
        if (targetId === current) {{
          link.classList.add('active');
        }} else {{
          link.classList.remove('active');
        }}
      }}
    }});
  }});
}}
"""

with open('assets/js/main.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print("assets/js/main.js generated successfully!")
