import json, sys
sys.stdout.reconfigure(encoding='utf-8')

# Load the comprehensive 20 tours from scripts/parsed_tours.json
with open('scripts/parsed_tours.json', 'r', encoding='utf-8') as f:
    tours_data = json.load(f)

tours_json_str = json.dumps(tours_data, ensure_ascii=False, indent=2)

departure_schedule = [
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
]

schedule_json_str = json.dumps(departure_schedule, ensure_ascii=False, indent=2)

js_content = f"""/**
 * DI CUNG GIO - Main Interactive Controller
 * Inspiring modern trekking experience (inspired by gianglangthang.vn)
 * Zero-build vanilla ES6+ architecture
 */

// ==========================================
// 1. TOUR DATA REPOSITORY (ALL 20 TOURS)
// ==========================================
const TOURS_DATA = {tours_json_str};

// ==========================================
// 2. DEPARTURE SCHEDULE DATA (5 KEY TOURS WITH SCARCITY & URGENCY)
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
    verified: true,
    avatar: 'assets/images/avatar-ha.jpg',
    comment: 'Cung đường sống lưng khủng long Tà Xùa đẹp nín thở, hướng dẫn viên nhiệt tình, đồ ăn ngon. Cảm ơn Trekking Đi Cùng Gió đã cho mình một hành trình thật đáng nhớ!',
    rating: 5,
    date: '18/10/2026'
  }},
  {{
    id: 2,
    name: 'Lê Minh Đức',
    role: 'Trekking Yên Tử – Chùa Đồng',
    verified: true,
    avatar: 'assets/images/avatar-duc.jpg',
    comment: 'Lần đầu leo bộ Yên Tử mà được chạm tay vào Chùa Đồng lúc bình minh mây ngàn. Anh em leader chăm sóc chu đáo, huy chương gỗ độc quyền kỷ niệm rất đẹp.',
    rating: 5,
    date: '12/10/2026'
  }},
  {{
    id: 3,
    name: 'Trần Thị Mai',
    role: 'Kỳ Quan San – Đỉnh núi hùng vĩ',
    verified: true,
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
function initApp() {{
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
}}

if (document.readyState === 'loading') {{
  document.addEventListener('DOMContentLoaded', initApp);
}} else {{
  initApp();
}}

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
// 7. RENDER TOURS (SMART TREKKING FILTER & CARDS)
// ==========================================
function renderTours(category = currentCategory) {{
  const container = document.getElementById('tour-grid-container');
  if (!container) return;

  currentCategory = category;
  let filtered = [...TOURS_DATA];

  // 1. Category filter
  if (currentCategory !== 'all') {{
    filtered = filtered.filter(t => t.category === currentCategory || t.subCategory === currentCategory);
  }}

  // 2. Difficulty filter
  if (currentDifficulty === 'easy') {{
    filtered = filtered.filter(t => (t.difficultyLevel || 2) <= 2);
  }} else if (currentDifficulty === 'medium') {{
    filtered = filtered.filter(t => t.difficultyLevel === 3);
  }} else if (currentDifficulty === 'hard') {{
    filtered = filtered.filter(t => (t.difficultyLevel || 3) >= 4);
  }}

  // 3. Duration filter
  if (currentDuration === 'day') {{
    filtered = filtered.filter(t => (t.duration || '').toLowerCase().includes('trong ngày'));
  }} else if (currentDuration === '2d1n') {{
    filtered = filtered.filter(t => (t.duration || '').toLowerCase().includes('2 ngày'));
  }} else if (currentDuration === '3d2n') {{
    filtered = filtered.filter(t => (t.duration || '').toLowerCase().includes('3 ngày'));
  }}

  // 4. Keyword search
  if (searchKeyword) {{
    filtered = filtered.filter(t => {{
      const haystack = (t.title + ' ' + t.location + ' ' + (t.shortSummary || '') + ' ' + (t.code || '') + ' ' + (t.altitude || '')).toLowerCase();
      return haystack.includes(searchKeyword);
    }});
  }}

  // 5. Sorting
  if (currentSort === 'price-asc') {{
    filtered.sort((a, b) => (a.priceNum || 0) - (b.priceNum || 0));
  }} else if (currentSort === 'price-desc') {{
    filtered.sort((a, b) => (b.priceNum || 0) - (a.priceNum || 0));
  }} else if (currentSort === 'altitude-desc') {{
    const parseAlt = (s) => parseInt((s || '').replace(/\\D/g, '') || '0', 10);
    filtered.sort((a, b) => parseAlt(b.altitude) - parseAlt(a.altitude));
  }} else {{
    // popular: featured first, then reviews desc
    filtered.sort((a, b) => {{
      if (a.isFeatured && !b.isFeatured) return -1;
      if (!a.isFeatured && b.isFeatured) return 1;
      return (b.reviews || 0) - (a.reviews || 0);
    }});
  }}

  // UI Count & Reset Button
  const countEl = document.getElementById('filter-result-count');
  const resetBtn = document.getElementById('filter-reset-btn');
  const hasActiveFilters = currentCategory !== 'all' || currentDifficulty !== 'all' || currentDuration !== 'all' || currentSort !== 'popular' || searchKeyword !== '';

  if (resetBtn) {{
    if (hasActiveFilters || showAllTours) {{
      resetBtn.classList.remove('hidden');
      resetBtn.classList.add('inline-flex');
    }} else {{
      resetBtn.classList.add('hidden');
      resetBtn.classList.remove('inline-flex');
    }}
  }}

  // Display limited or full
  let displayTours = filtered;
  if (!hasActiveFilters && !showAllTours) {{
    displayTours = filtered.slice(0, 4);
    if (countEl) countEl.textContent = `Hiển thị 4 tour tiêu biểu (${{filtered.length}} tour có sẵn)`;
  }} else {{
    if (countEl) countEl.textContent = `Tìm thấy ${{filtered.length}} hành trình phù hợp`;
  }}

  // Empty state if 0 tours found
  if (displayTours.length === 0) {{
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
  }}

  container.innerHTML = displayTours.map(tour => {{
    const isLiked = wishlist.has(tour.id);
    const displayPrice = tour.priceNum ? formatCurrency(tour.priceNum) : tour.price.replace('/người', '');
    
    // Clean distance string
    let shortDist = (tour.trekDistance || '12km').replace(/Khoảng\\s*/gi, '').split('(')[0].trim();
    if (shortDist.length > 13) shortDist = shortDist.substring(0, 11) + '...';

    return `
      <div class="tour-card bg-white rounded-2xl overflow-hidden border border-gray-100 shadow-sm hover:shadow-md transition-all duration-300 flex flex-col h-full justify-between group">
        
        <!-- Tour Image Container -->
        <div class="relative overflow-hidden aspect-[4/3] bg-gray-100 cursor-pointer shrink-0" onclick="openTourDetailModal(${{tour.id}})">
          <img 
            src="${{tour.image}}" 
            alt="${{tour.title}}" 
            loading="lazy" 
            onerror="this.onerror=null; this.src='assets/images/tour-yen-tu.jpg';"
            class="tour-card-image w-full h-full object-cover transition-transform duration-500 group-hover:scale-108"
          />
          
          <!-- Category & Altitude Badges (Top Left Corner) -->
          <div class="absolute top-2.5 left-2.5 z-10 flex items-center gap-1.5 max-w-[calc(100%-46px)] flex-wrap">
            <span class="backdrop-blur-md bg-[#1E4D3B]/90 text-white text-[10.5px] font-bold px-2 py-0.5 rounded-full shadow-sm truncate">
              ${{tour.badge}}
            </span>
            <span class="backdrop-blur-md bg-black/65 text-emerald-200 text-[10px] font-bold px-2 py-0.5 rounded-md shadow-sm shrink-0">
              ${{tour.altitudeBadge || '⛰️ ' + tour.altitude}}
            </span>
          </div>

          <!-- Wishlist Heart Button (Top Right Corner) -->
          <button 
            type="button" 
            onclick="toggleWishlist(${{tour.id}}, event)" 
            title="${{isLiked ? 'Bỏ yêu thích' : 'Lưu tour yêu thích'}}"
            class="heart-btn absolute top-2.5 right-2.5 z-20 w-7 h-7 rounded-full bg-white/85 backdrop-blur-md flex items-center justify-center text-gray-700 hover:text-red-500 hover:bg-white transition-all shadow-sm ${{isLiked ? 'active' : ''}}"
          >
            <i data-lucide="heart" class="w-3.5 h-3.5 transition-colors ${{isLiked ? 'fill-red-500 text-red-500' : ''}}"></i>
          </button>

          <!-- Fast Spec Bar: Difficulty & Distance (Bottom Left Corner) -->
          <div class="absolute bottom-2.5 left-2.5 z-10">
            <span class="backdrop-blur-md bg-black/65 text-white text-[10.5px] font-semibold px-2.5 py-1 rounded-md shadow-sm flex items-center gap-1.5">
              <span class="text-amber-300 font-bold">⚡ Độ khó: ${{tour.difficultyLevel || 3}}/5</span>
              <span class="text-white/40">•</span>
              <span class="text-emerald-300 font-bold">🥾 ${{shortDist}}</span>
            </span>
          </div>

          <!-- Real Photo indicator (Bottom Right Corner) -->
          ${{tour.gallery && tour.gallery.length > 0 ? `
            <div class="absolute bottom-2.5 right-2.5 z-10">
              <span class="backdrop-blur-md bg-black/65 text-white text-[10px] font-medium px-2 py-0.5 rounded-md shadow-sm flex items-center gap-1">
                <i data-lucide="camera" class="w-3 h-3 text-emerald-300"></i>
                <span>${{tour.gallery.length}} ảnh</span>
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
        </div>

        <!-- Tour Body Content -->
        <div class="p-3.5 flex flex-col flex-1 justify-between">
          <div>
            <!-- Meta Details: Location & History Story Button -->
            <div class="flex items-center justify-between text-[11px] text-gray-500 mb-2 gap-2 h-5">
              <span class="flex items-center gap-1 min-w-0 flex-1 truncate">
                <i data-lucide="map-pin" class="w-3 h-3 text-forest shrink-0"></i>
                <span class="truncate font-medium text-gray-600">${{tour.location}}</span>
              </span>
              <button 
                type="button" 
                onclick="openTourDetailModal(${{tour.id}}, 2); event.stopPropagation();" 
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
              onclick="openTourDetailModal(${{tour.id}})" 
              title="${{tour.title}}"
            >
              ${{tour.title}}
            </h3>

            <!-- 1-line / 2-line Short Summary Description: Locked to h-[36px] -->
            <p class="text-xs text-gray-600 line-clamp-2 mt-1 mb-2 leading-relaxed h-[36px]" title="${{tour.shortSummary || tour.description}}">
              ${{tour.shortSummary || tour.description}}
            </p>

            <!-- Commitment Tag & Schedule: Locked to h-6 -->
            <div class="flex items-center gap-1.5 mb-2.5 h-6">
              <span class="px-2 py-0.5 rounded-md bg-emerald-50 text-forest text-[10px] font-bold border border-emerald-100/80 flex items-center gap-1 shrink-0">
                <i data-lucide="check" class="w-3 h-3 text-forest"></i>
                <span>${{tour.minPax}}</span>
              </span>
              <span class="text-[10px] text-gray-500 font-medium truncate flex-1" title="${{tour.departureFrequency}}">
                ${{tour.departureFrequency}}
              </span>
            </div>

            <!-- Price & Duration: Clearly separated to prevent text collision -->
            <div class="flex items-center justify-between gap-2 pt-2 border-t border-gray-100/90">
              <div class="flex flex-col min-w-0">
                <span class="text-[9.5px] text-gray-400 font-semibold uppercase tracking-wider">Trọn gói từ</span>
                <div class="flex items-baseline gap-0.5">
                  <span class="text-[15px] xl:text-[16px] font-black text-[#1E4D3B] tracking-tight leading-none">
                    ${{displayPrice}}
                  </span>
                  <span class="text-[10px] text-gray-500 font-normal">/khách</span>
                </div>
              </div>
              <div class="shrink-0 text-right">
                <span class="inline-block text-[10.5px] text-gray-600 font-medium bg-gray-100/80 px-2 py-0.5 rounded-md border border-gray-200/50 whitespace-nowrap">
                  ${{tour.duration}}
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
              <span class="text-[10.5px] text-gray-400 font-semibold">(${{tour.reviews || 120}})</span>
            </div>

            <button 
              type="button" 
              onclick="openSmartBookingModal(${{tour.id}}); event.stopPropagation();"
              class="btn-shine whitespace-nowrap px-3 py-1.5 rounded-lg bg-[#1E4D3B] text-white text-[11px] font-bold shrink-0 hover:bg-forest/90 hover:scale-102 active:scale-95 transition-all shadow-sm cursor-pointer flex items-center gap-1"
            >
              <span>Đăng ký ngay</span>
              <i data-lucide="arrow-right" class="w-3 h-3"></i>
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

  container.innerHTML = DEPARTURE_SCHEDULE.map(item => {{
    let badgeClass = 'badge-seat';
    if (item.statusType === 'urgent') {{
      badgeClass += ' badge-urgent';
    }} else if (item.statusType === 'available') {{
      badgeClass += ' badge-available';
    }} else if (item.statusType === 'open') {{
      badgeClass += ' badge-open';
    }}

    return `
      <div 
        onclick="openTourDetailModal(${{item.tourId}})"
        class="schedule-row p-2.5 rounded-xl bg-gray-50/70 border border-gray-100/80 flex items-center justify-between gap-2.5 cursor-pointer group hover:bg-emerald-50/60 hover:border-emerald-200/80 hover:shadow-xs transition-all relative"
        title="Bấm để giữ chỗ hoặc xem lịch trình chi tiết"
      >
        <!-- Date Block -->
        <div class="flex items-center gap-2.5 min-w-0 flex-1">
          <div class="w-10 h-10 rounded-xl bg-[#1E4D3B] text-white flex flex-col items-center justify-center shadow-xs group-hover:scale-105 transition-transform shrink-0">
            <span class="text-sm font-black leading-none">${{item.day}}</span>
            <span class="text-[9px] font-bold uppercase tracking-wider text-emerald-200 mt-0.5">${{item.month}}</span>
          </div>

          <div class="min-w-0 flex-1">
            <div class="flex items-center gap-1.5">
              <span class="text-[9px] font-extrabold px-1.5 py-0.2 rounded bg-emerald-100 text-forest shrink-0">${{item.code}}</span>
              <h4 class="text-xs font-bold text-gray-900 group-hover:text-forest transition-colors truncate" title="${{item.title}}">
                ${{item.title}}
              </h4>
            </div>
            <span class="text-[10.5px] text-gray-500 font-medium truncate block mt-0.5">${{item.duration}} • Hà Nội</span>
          </div>
        </div>

        <!-- Price & Status Badge -->
        <div class="text-right shrink-0 pl-1.5 min-w-[75px]">
          <span class="block text-xs font-black text-[#1E4D3B] whitespace-nowrap">${{item.price}}</span>
          <span class="${{badgeClass}} text-[9.5px] inline-block mt-0.5 whitespace-nowrap">${{item.status}}</span>
        </div>
      </div>
    `;
  }}).join('');

  initLucideIcons();
}}

// ==========================================
// 9. CATEGORY BAR & SMART FILTER CONTROLLERS
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
  if (cat === 'all') {{
    showAllTours = true;
  }}

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
      all: 'Tất Cả Tour Chinh Phục',
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

function handleTourFilterChange() {{
  const searchInput = document.getElementById('tour-search-input');
  const clearBtn = document.getElementById('tour-search-clear');
  const diffSelect = document.getElementById('filter-difficulty');
  const durSelect = document.getElementById('filter-duration');
  const sortSelect = document.getElementById('filter-sort');

  searchKeyword = searchInput ? searchInput.value.trim().toLowerCase() : '';
  currentDifficulty = diffSelect ? diffSelect.value : 'all';
  currentDuration = durSelect ? durSelect.value : 'all';
  currentSort = sortSelect ? sortSelect.value : 'popular';

  if (clearBtn) {{
    if (searchKeyword) {{
      clearBtn.classList.remove('hidden');
    }} else {{
      clearBtn.classList.add('hidden');
    }}
  }}

  renderTours();
}}
window.handleTourFilterChange = handleTourFilterChange;

function clearTourSearch() {{
  const searchInput = document.getElementById('tour-search-input');
  if (searchInput) {{
    searchInput.value = '';
  }}
  handleTourFilterChange();
}}
window.clearTourSearch = clearTourSearch;

function resetTourFilters() {{
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
}}
window.resetTourFilters = resetTourFilters;

// ==========================================
// 10. ALL-IN-ONE TREKKING GUIDE MODAL CONTROLLER (Inspired by Giang Lang Thang)
// ==========================================
function openTourDetailModal(tourId, initialTab = 1) {{
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

  let cleanDist = (tour.trekDistance || '12km').replace(/Khoảng\\s*/gi, '').split('(')[0].trim();

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
          src="${{tour.image}}" 
          alt="${{tour.title}}" 
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
            <span class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-[#1E4D3B] text-white shadow-xs">${{tour.badge}}</span>
            <span class="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-white/20 backdrop-blur-sm text-white">${{tour.altitudeBadge || '⛰️ ' + tour.altitude}}</span>
            <span class="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-white/20 backdrop-blur-sm text-white">${{tour.duration}}</span>
            <span class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-amber-400 text-stone-900 shadow-xs">${{tour.code}}</span>
          </div>
          <h2 class="text-xl sm:text-2xl lg:text-3xl font-black leading-tight drop-shadow-sm">${{tour.title}}</h2>
          <p class="text-xs sm:text-sm text-emerald-200 mt-1 flex items-center gap-2">
            <i data-lucide="map-pin" class="w-3.5 h-3.5 text-emerald-300 shrink-0"></i>
            <span>${{tour.location}} • Điểm đón: ${{tour.pickupPoint || '55 Nguyễn Quốc Trị & 489 Hoàng Quốc Việt'}}</span>
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
            <span class="block text-xs sm:text-sm font-black text-forest truncate">${{tour.altitude}}</span>
            <span class="block text-[9.5px] text-gray-400 truncate">${{altSubtitle}}</span>
          </div>
        </div>

        <!-- Tile 2: Difficulty -->
        <div class="bg-white p-2.5 rounded-xl border border-gray-100 shadow-2xs flex items-center gap-2.5">
          <div class="w-9 h-9 rounded-lg bg-amber-50 text-amber-600 flex items-center justify-center shrink-0">
            <i data-lucide="zap" class="w-5 h-5"></i>
          </div>
          <div class="min-w-0">
            <span class="block text-[10px] font-bold uppercase tracking-wider text-gray-500">Độ khó thể lực</span>
            <span class="block text-xs sm:text-sm font-black text-amber-600">Level ${{tour.difficultyLevel || 3}}/5</span>
            <span class="block text-[9.5px] text-gray-500 truncate">${{tour.difficultyText || 'Trung bình'}}</span>
          </div>
        </div>

        <!-- Tile 3: Total Distance -->
        <div class="bg-white p-2.5 rounded-xl border border-gray-100 shadow-2xs flex items-center gap-2.5">
          <div class="w-9 h-9 rounded-lg bg-emerald-50 text-emerald-600 flex items-center justify-center shrink-0">
            <i data-lucide="footprints" class="w-5 h-5"></i>
          </div>
          <div class="min-w-0">
            <span class="block text-[10px] font-bold uppercase tracking-wider text-gray-500">Tổng quãng đường</span>
            <span class="block text-xs sm:text-sm font-black text-gray-900 truncate">${{cleanDist}}</span>
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
              ${{(tour.routeSteps || ['Hà Nội', 'Chân núi', 'Lán nghỉ', 'Đỉnh núi', 'Hạ sơn']).map((step, idx, arr) => `
                <span class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-white border border-emerald-200 text-forest font-bold text-xs shadow-2xs">
                  <span class="w-4 h-4 rounded-full bg-forest text-white text-[10px] flex items-center justify-center font-extrabold shrink-0">${{idx + 1}}</span>
                  <span>${{step}}</span>
                </span>
                ${{idx < arr.length - 1 ? '<i data-lucide="chevron-right" class="w-3.5 h-3.5 text-emerald-600 shrink-0"></i>' : ''}}
              `).join('')}}
            </div>
          </div>

          <!-- Geographic Route Description -->
          <div class="space-y-1.5">
            <h4 class="text-xs font-bold uppercase tracking-wider text-gray-800 flex items-center gap-1.5">
              <i data-lucide="map" class="w-4 h-4 text-forest"></i>
              <span>Hành trình đi đâu & Lộ trình địa lý</span>
            </h4>
            <p class="text-xs sm:text-sm text-gray-700 leading-relaxed bg-gray-50 p-3.5 rounded-xl border border-gray-100 font-normal">
              ${{tour.routeMap || tour.description}}
            </p>
          </div>
          
          <!-- Highlights -->
          <div class="space-y-2.5 pt-1">
            <h4 class="text-xs font-bold uppercase tracking-wider text-forest">Trải nghiệm độc bản không thể bỏ lỡ</h4>
            <ul class="space-y-2">
              ${{(tour.highlights || [
                'Chinh phục đỉnh cao ngoạn mục vùng cao Tây Bắc',
                'Đón bình minh và biển mây cuồn cuộn tráng lệ',
                'Thưởng thức ẩm thực bản địa tươi ngon bên bếp lửa lán rừng'
              ]).map(hl => `
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
        </div>

        <!-- PANEL 2: Lịch sử & Câu chuyện vùng đất -->
        <div id="tab-panel-2" class="hidden space-y-4">
          <div class="bg-[#F6F7F2] border-l-4 border-[#1E4D3B] p-5 rounded-r-2xl shadow-xs space-y-3.5">
            <div class="flex items-center gap-2 text-forest">
              <i data-lucide="landmark" class="w-5 h-5 text-forest"></i>
              <h4 class="font-extrabold text-sm sm:text-base text-gray-900">
                Lịch sử, Huyền thoại & Câu chuyện văn hóa: ${{tour.title}}
              </h4>
            </div>
            
            <p class="text-xs sm:text-sm text-gray-700 leading-relaxed font-normal">
              ${{tour.historyStory || tour.description}}
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
              ${{(tour.itinerary || [
                {{ day: "Đêm 0", title: "Khởi hành từ Hà Nội", desc: "Xe đón tại 55 Nguyễn Quốc Trị và 489 Hoàng Quốc Việt, di chuyển xuyên đêm lên điểm leo." }},
                {{ day: "Ngày 1", title: "Bắt đầu trekking & Nghỉ lán", desc: "Ăn sáng, gặp gỡ Porter, bắt đầu hành trình trekking qua rừng, ăn trưa dã ngoại và nghỉ đêm tại lán gỗ." }},
                {{ day: "Ngày 2", title: "Chạm đỉnh & Hạ sơn", desc: "Thức dậy sớm đón bình minh săn mây, chạm đỉnh nhận huy chương danh dự và di chuyển về Hà Nội." }}
              ]).map(step => `
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
                ${{(tour.included || [
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
                    <span>${{inc}}</span>
                  </li>
                `).join('')}}
              </ul>
            </div>

            <!-- Cột phải: BẠN CẦN CHUẨN BỊ -->
            <div class="bg-emerald-50/50 p-4 rounded-2xl border border-emerald-100/70 space-y-2.5">
              <h5 class="font-bold text-xs text-forest uppercase tracking-wider flex items-center gap-1.5">
                <i data-lucide="backpack" class="w-4 h-4 text-forest"></i>
                <span>Bạn Cần Chuẩn Bị</span>
              </h5>
              <ul class="text-xs text-gray-700 space-y-2">
                ${{(tour.preparation || [
                  "Giày trekking chuyên dụng có độ bám gai cao, chống trơn trượt",
                  "Áo khoác gió giữ nhiệt / áo phao ấm cho ban đêm trên lán",
                  "Balo cá nhân gọn nhẹ 20 – 30L đựng đồ dùng cần thiết",
                  "Đèn pin đội đầu có pin dự phòng (dùng khi săn mây sớm)",
                  "Bình nước cá nhân 1 – 1.5L, đồ ăn vặt bổ sung năng lượng",
                  "Giấy tờ tùy thân (CCCD / Hộ chiếu bản gốc bắt buộc)"
                ]).map(prep => `
                  <li class="flex items-start gap-2">
                    <span class="text-amber-600 font-bold">✔</span>
                    <span>${{prep}}</span>
                  </li>
                `).join('')}}
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
              onchange="updateModalBookingTotal(${{tour.id}})"
              class="appearance-none pl-3 pr-7 py-2 rounded-xl bg-white border border-gray-200 text-xs font-bold text-gray-800 focus:outline-none focus:border-forest shadow-2xs cursor-pointer"
            >
              ${{dates.map(d => `<option value="${{d}}">📅 ${{d}}</option>`).join('')}}
            </select>
            <i data-lucide="chevron-down" class="w-3.5 h-3.5 text-gray-400 absolute right-2 top-1/2 -translate-y-1/2 pointer-events-none"></i>
          </div>

          <!-- Pax Stepper -->
          <div class="flex items-center border border-gray-200 rounded-xl bg-white shadow-2xs overflow-hidden">
            <button 
              type="button" 
              onclick="adjustModalPax(-1, ${{tour.id}})" 
              class="px-2.5 py-1.5 text-gray-600 hover:bg-gray-100 text-xs font-black cursor-pointer"
              title="Giảm 1 khách"
            >-</button>
            <span id="modal-booking-pax" class="px-2.5 py-1.5 text-xs font-extrabold text-gray-900 min-w-[28px] text-center">1</span>
            <button 
              type="button" 
              onclick="adjustModalPax(1, ${{tour.id}})" 
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
              ${{formatCurrency(tour.priceNum || 550000)}}
            </span>
          </div>

          <button 
            type="button" 
            onclick="proceedModalBooking(${{tour.id}})" 
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

// Switch tab in detail modal (1 to 5)
function switchDetailTab(tabIndex) {{
  for (let i = 1; i <= 5; i++) {{
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
}}
window.switchDetailTab = switchDetailTab;

window.adjustModalPax = function(delta, tourId) {{
  const newPax = modalBookingPax + delta;
  if (newPax >= 1 && newPax <= 20) {{
    modalBookingPax = newPax;
    updateModalBookingTotal(tourId);
  }}
}};

window.updateModalBookingTotal = function(tourId) {{
  const tour = TOURS_DATA.find(t => t.id === tourId);
  if (!tour) return;
  const paxEl = document.getElementById('modal-booking-pax');
  const totalEl = document.getElementById('modal-booking-total');
  if (paxEl) paxEl.textContent = modalBookingPax;
  if (totalEl) {{
    const total = (tour.priceNum || 550000) * modalBookingPax;
    totalEl.textContent = formatCurrency(total);
  }}
}};

window.proceedModalBooking = function(tourId) {{
  const dateSelect = document.getElementById('modal-booking-date');
  const selectedDate = dateSelect ? dateSelect.value : '';
  const pax = modalBookingPax || 1;
  closeTourDetailModal();
  openSmartBookingModal(tourId, selectedDate, pax);
}};

// ==========================================
// 11. SMART BOOKING MODAL WITH LIVE CALCULATOR
// ==========================================
function openSmartBookingModal(tourId = 1, defaultDate = '', defaultGuests = 1) {{
  currentBookingTour = TOURS_DATA.find(t => t.id === tourId) || TOURS_DATA[0];
  bookingGuests = defaultGuests || 1;

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
        ${{t.code ? `[${{t.code}}] ` : ''}}${{t.title}} - ${{t.price}} (${{t.duration}})
      </option>
    `).join('');
    
    select.onchange = (e) => {{
      const chosenId = parseInt(e.target.value, 10);
      currentBookingTour = TOURS_DATA.find(t => t.id === chosenId) || TOURS_DATA[0];
      updateBookingCalculation();
    }};
  }}

  // Set default date if passed
  if (dateInput) {{
    if (defaultDate) {{
      dateInput.value = defaultDate;
    }} else if (currentBookingTour.departureDates && currentBookingTour.departureDates.length > 0) {{
      dateInput.value = currentBookingTour.departureDates[0];
    }} else {{
      dateInput.value = '26/10/2026';
    }}
  }}

  // Reset display boxes
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
        <span class="font-bold text-gray-900">${{formatCurrency(priceEach)}} x ${{bookingGuests}} = ${{formatCurrency(subtotal)}}</span>
      </div>
      ${{isGroupDiscount ? `
        <div class="flex justify-between items-center text-emerald-700 font-bold">
          <span>Ưu đãi nhóm (≥4 khách giảm 5%):</span>
          <span>- ${{formatCurrency(discountAmount)}}</span>
        </div>
      ` : `
        <div class="text-[11px] text-gray-500 italic">
          💡 Đặt từ 4 người trở lên được giảm thêm 5% tổng hóa đơn.
        </div>
      `}}
      <div class="pt-2 border-t border-emerald-200 flex justify-between items-center text-sm font-extrabold text-forest">
        <span>Tổng tạm tính:</span>
        <span class="text-base text-[#1E4D3B]">${{formatCurrency(finalTotal)}}</span>
      </div>
    </div>
  `;
}}

function setupBookingModalEvents() {{
  const form = document.getElementById('smart-booking-form');
  if (!form) return;

  form.addEventListener('submit', (e) => {{
    e.preventDefault();

    const name = document.getElementById('booking-name')?.value;
    const phone = document.getElementById('booking-phone')?.value;
    const email = document.getElementById('booking-email')?.value || 'Không có';
    const date = document.getElementById('booking-date-input')?.value;
    const note = document.getElementById('booking-note')?.value || 'Không có';

    if (!name || !phone) {{
      showToast('Lỗi thông tin', 'Vui lòng điền Họ tên và Số điện thoại nhận Zalo.', 'error');
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
        <div class="text-center space-y-4 py-4">
          <div class="w-16 h-16 bg-emerald-100 text-forest rounded-full flex items-center justify-center mx-auto shadow-inner">
            <i data-lucide="check" class="w-8 h-8"></i>
          </div>
          
          <h4 class="text-xl font-bold text-gray-900">Giữ Chỗ Thành Công!</h4>
          <p class="text-xs text-gray-600 max-w-sm mx-auto leading-relaxed">
            Cảm ơn <strong>${{name}}</strong> đã đăng ký hành trình cùng <strong>Trekking Đi Cùng Gió</strong>. 
            Mã đặt chỗ của bạn là <span class="px-2 py-0.5 rounded bg-emerald-100 font-mono font-bold text-forest">${{randomCode}}</span>.
          </p>

          <div class="bg-gray-50 rounded-2xl p-4 text-xs text-left space-y-2 border border-gray-100 font-medium">
            <div class="flex justify-between">
              <span class="text-gray-500">Hành trình:</span>
              <span class="font-bold text-gray-900">${{currentBookingTour.title}}</span>
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
              <span class="text-gray-600 font-bold">Tổng chi phí dự tính:</span>
              <span class="font-black text-sm text-forest">${{formatCurrency(finalTotal)}}</span>
            </div>
          </div>

          <p class="text-[11px] text-gray-500 italic">
            💬 Tư vấn viên / Leader đoàn sẽ gọi điện xác nhận và gửi lịch trình chi tiết qua Zalo <strong>${{phone}}</strong> trong vòng 15 phút.
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
    }}

    showToast('Đăng ký thành công!', 'Chúng tôi đã nhận thông tin giữ chỗ của bạn.', 'success');
  }});
}}

// ==========================================
// 12. WISHLIST & DRAWER SYSTEM
// ==========================================
function toggleWishlist(tourId, event) {{
  if (event) event.stopPropagation();

  if (wishlist.has(tourId)) {{
    wishlist.delete(tourId);
    showToast('Đã xóa khỏi danh sách', 'Đã bỏ lưu hành trình này.', 'info');
  }} else {{
    wishlist.add(tourId);
    showToast('Đã lưu yêu thích ❤️', 'Hành trình đã được thêm vào danh sách lưu!', 'success');
  }}

  try {{
    localStorage.setItem('dicunggio_wishlist', JSON.stringify([...wishlist]));
  }} catch (e) {{}}

  updateWishlistBadges();
  renderTours();
}}

function updateWishlistBadges() {{
  const badgeCountEls = document.querySelectorAll('.wishlist-count-badge');
  const count = wishlist.size;

  badgeCountEls.forEach(el => {{
    el.textContent = count;
    if (count > 0) {{
      el.classList.remove('hidden');
    }} else {{
      el.classList.add('hidden');
    }}
  }});
}}

window.openWishlistDrawer = function() {{
  const drawer = document.getElementById('wishlist-drawer');
  const list = document.getElementById('wishlist-items-list');
  if (!drawer || !list) return;

  const likedTours = TOURS_DATA.filter(t => wishlist.has(t.id));

  if (likedTours.length === 0) {{
    list.innerHTML = `
      <div class="py-12 text-center text-gray-400 space-y-3">
        <i data-lucide="heart-off" class="w-12 h-12 mx-auto stroke-1"></i>
        <p class="text-xs">Bạn chưa lưu tour nào vào danh sách yêu thích.</p>
        <button onclick="closeWishlistDrawer()" class="px-4 py-2 rounded-full bg-forest text-white text-xs font-bold hover:bg-forest/90">
          Khám phá tour ngay
        </button>
      </div>
    `;
  }} else {{
    list.innerHTML = likedTours.map(t => `
      <div class="flex items-center gap-3 p-3 bg-gray-50 rounded-2xl border border-gray-100 relative group">
        <img src="${{t.image}}" alt="${{t.title}}" class="w-16 h-16 rounded-xl object-cover shrink-0" />
        <div class="flex-1 min-w-0">
          <h5 class="font-bold text-xs text-gray-900 truncate">${{t.title}}</h5>
          <span class="text-[10px] text-gray-500 block">${{t.location}} • ${{t.duration}}</span>
          <span class="text-xs font-black text-forest mt-0.5 block">${{t.price}}</span>
        </div>
        <div class="flex flex-col gap-1 shrink-0">
          <button 
            type="button" 
            onclick="openTourDetailModal(${{t.id}}); closeWishlistDrawer();" 
            class="p-1.5 rounded-lg bg-white border border-gray-200 text-forest hover:bg-forest hover:text-white transition-colors"
            title="Xem chi tiết"
          >
            <i data-lucide="eye" class="w-3.5 h-3.5"></i>
          </button>
          <button 
            type="button" 
            onclick="toggleWishlist(${{t.id}})" 
            class="p-1.5 rounded-lg bg-white border border-gray-200 text-red-500 hover:bg-red-50 transition-colors"
            title="Bỏ thích"
          >
            <i data-lucide="trash-2" class="w-3.5 h-3.5"></i>
          </button>
        </div>
      </div>
    `).join('');
  }}

  drawer.classList.remove('hidden');
  initLucideIcons();
}};

window.closeWishlistDrawer = function() {{
  const drawer = document.getElementById('wishlist-drawer');
  if (drawer) drawer.classList.add('hidden');
}};

// ==========================================
// 13. SEARCH OVERLAY & REAL-TIME FILTER
// ==========================================
window.openSearchModal = function() {{
  const modal = document.getElementById('search-modal');
  const input = document.getElementById('search-modal-input');
  if (modal) {{
    modal.classList.remove('hidden');
    if (input) {{
      input.focus();
      input.value = '';
      renderSearchResults('');
    }}
  }}
}};

window.closeSearchModal = function() {{
  const modal = document.getElementById('search-modal');
  if (modal) modal.classList.add('hidden');
}};

window.handleLiveSearch = function(query) {{
  renderSearchResults(query.trim().toLowerCase());
}};

function renderSearchResults(q) {{
  const container = document.getElementById('search-results-container');
  if (!container) return;

  if (!q) {{
    container.innerHTML = `
      <div class="py-6 text-center text-xs text-gray-400">
        Nhập tên ngọn núi hoặc địa danh (vd: Yên Tử, Tà Xùa, Kỳ Quan San, Cúc Phương...)
      </div>
    `;
    return;
  }}

  const results = TOURS_DATA.filter(t => 
    t.title.toLowerCase().includes(q) || 
    t.location.toLowerCase().includes(q) ||
    t.description.toLowerCase().includes(q) ||
    t.code.toLowerCase().includes(q)
  );

  if (results.length === 0) {{
    container.innerHTML = `
      <div class="py-8 text-center text-xs text-gray-500">
        Không tìm thấy hành trình nào với từ khóa "<strong>${{q}}</strong>".
      </div>
    `;
  }} else {{
    container.innerHTML = results.map(t => `
      <div 
        onclick="openTourDetailModal(${{t.id}}); closeSearchModal();" 
        class="flex items-center gap-3 p-2.5 rounded-xl hover:bg-emerald-50/70 transition-colors cursor-pointer border-b border-gray-100 last:border-0"
      >
        <img src="${{t.image}}" alt="${{t.title}}" class="w-12 h-12 rounded-lg object-cover shrink-0" />
        <div class="flex-1 min-w-0">
          <div class="flex items-center gap-1.5">
            <span class="text-[9px] font-extrabold px-1.5 py-0.2 rounded bg-emerald-100 text-forest">${{t.code}}</span>
            <h5 class="font-bold text-xs text-gray-900 truncate">${{t.title}}</h5>
          </div>
          <span class="text-[11px] text-gray-500 truncate block mt-0.5">${{t.location}} • ${{t.duration}}</span>
        </div>
        <span class="text-xs font-black text-forest shrink-0">${{t.price}}</span>
      </div>
    `).join('');
  }}
}}

// ==========================================
// 14. VIDEO MODAL LIGHTBOX
// ==========================================
window.openVideoModal = function() {{
  const modal = document.getElementById('video-modal');
  if (modal) {{
    modal.classList.remove('hidden');
    document.body.style.overflow = 'hidden';
  }}
}};

window.closeVideoModal = function() {{
  const modal = document.getElementById('video-modal');
  if (modal) {{
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
            <span class="text-[10px] text-forest font-medium flex items-center gap-1.5 flex-wrap">
              <span>${{rev.role}}</span>
              <span class="inline-flex items-center gap-0.5 text-[9.5px] font-bold text-emerald-700 bg-emerald-50 px-1.5 py-0.2 rounded-full border border-emerald-200">
                <i data-lucide="badge-check" class="w-3 h-3 text-emerald-600"></i>
                <span>✓ Đã hoàn thành chặng</span>
              </span>
            </span>
          </div>
        </div>
        <div class="flex text-amber-400">
          ${{Array(rev.rating).fill('<i data-lucide="star" class="w-3 h-3 fill-amber-400 text-amber-400"></i>').join('')}}
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
  const form = document.getElementById('new-review-form');
  if (!form) return;

  form.addEventListener('submit', (e) => {{
    e.preventDefault();
    const name = document.getElementById('review-author')?.value;
    const tour = document.getElementById('review-tour')?.value;
    const text = document.getElementById('review-comment')?.value;

    if (!name || !text) return;

    TESTIMONIALS_DATA.unshift({{
      id: Date.now(),
      name: name,
      role: tour || 'Trekker Đi Cùng Gió',
      verified: true,
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

  let iconHtml = '<i data-lucide="info" class="w-5 h-5 text-forest shrink-0 mt-0.5"></i>';
  if (type === 'success') {{
    iconHtml = '<i data-lucide="check-circle-2" class="w-5 h-5 text-emerald-600 shrink-0 mt-0.5"></i>';
  }} else if (type === 'error') {{
    iconHtml = '<i data-lucide="alert-circle" class="w-5 h-5 text-red-500 shrink-0 mt-0.5"></i>';
  }}

  toast.innerHTML = `
    ${{iconHtml}}
    <div class="flex-1 min-w-0">
      <h6 class="font-bold text-xs text-gray-900">${{title}}</h6>
      <p class="text-xs text-gray-500 mt-0.5">${{message}}</p>
    </div>
    <button onclick="this.parentElement.remove()" class="text-gray-400 hover:text-gray-600 p-1">
      <i data-lucide="x" class="w-4 h-4"></i>
    </button>
  `;

  document.body.appendChild(toast);
  initLucideIcons();

  setTimeout(() => {{
    toast.classList.remove('translate-y-10', 'opacity-0');
  }}, 50);

  setTimeout(() => {{
    toast.classList.add('translate-y-10', 'opacity-0');
    setTimeout(() => toast.remove(), 300);
  }}, 3500);
}}

// ==========================================
// 17. SCROLL OBSERVERS & INTERACTIONS
// ==========================================
function setupScrollReveal() {{
  const elements = document.querySelectorAll('.reveal-on-scroll');
  if (!elements.length) return;

  const reveal = (el) => {{
    if (!el) return;
    el.classList.add('revealed');
    el.classList.add('visible');
  }};

  if (!('IntersectionObserver' in window)) {{
    elements.forEach(reveal);
    return;
  }}

  const observer = new IntersectionObserver((entries) => {{
    entries.forEach(entry => {{
      if (entry.isIntersecting) {{
        reveal(entry.target);
        observer.unobserve(entry.target);
      }}
    }});
  }}, {{ threshold: 0.05, rootMargin: '0px 0px 100px 0px' }});

  elements.forEach(el => {{
    const rect = el.getBoundingClientRect();
    const hash = window.location.hash ? window.location.hash.substring(1) : '';
    if (rect.top < window.innerHeight + 150 || (hash && el.id === hash)) {{
      reveal(el);
    }} else {{
      observer.observe(el);
    }}
  }});

  // Guarantee reveal after 500ms
  setTimeout(() => {{
    elements.forEach(reveal);
  }}, 500);

  // Hash navigation listener
  window.addEventListener('hashchange', () => {{
    const activeHash = window.location.hash ? window.location.hash.substring(1) : '';
    if (activeHash) {{
      const target = document.getElementById(activeHash);
      if (target) reveal(target);
    }}
  }});
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

// ==========================================
// 18. POLICY MODAL CONTROLLER
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
"""

with open('assets/js/main.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print("assets/js/main.js generated successfully!")
