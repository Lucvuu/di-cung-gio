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
    image: 'https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=800&q=80',
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
    image: 'https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=800&q=80',
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
    image: 'https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=800&q=80',
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
    image: 'https://images.unsplash.com/photo-1486870591958-9b9d0d1dda99?auto=format&fit=crop&w=800&q=80',
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
  updateWishlistBadges();
  setupCategoryFilter();
  setupBookingForm();
  setupMobileNav();
  setupFloatingActions();
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
        <!-- Tour Image Container -->
        <div class="relative overflow-hidden aspect-[4/3] bg-gray-100">
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
            <h3 class="font-bold text-gray-900 text-base leading-snug line-clamp-1 group-hover:text-forest transition-colors" title="${tour.title}">
              ${tour.title}
            </h3>

            <!-- Meta details (Duration & Route) -->
            <div class="flex items-center gap-3 text-xs text-gray-500 mt-2.5">
              <span class="inline-flex items-center gap-1">
                <i data-lucide="clock" class="w-3.5 h-3.5 text-gray-400"></i>
                ${tour.duration}
              </span>
              <span class="inline-flex items-center gap-1">
                <i data-lucide="map-pin" class="w-3.5 h-3.5 text-gray-400"></i>
                ${tour.location}
              </span>
            </div>

            <!-- Price -->
            <div class="mt-3">
              <span class="text-base font-bold text-forest">${tour.price}</span>
            </div>
          </div>

          <!-- Bottom: Rating & Book Button -->
          <div class="mt-3 pt-3 border-t border-gray-100 flex items-center justify-between">
            <div class="flex items-center gap-1 text-xs">
              <div class="flex text-amber-400">
                <i data-lucide="star" class="w-3.5 h-3.5 fill-amber-400 text-amber-400"></i>
                <i data-lucide="star" class="w-3.5 h-3.5 fill-amber-400 text-amber-400"></i>
                <i data-lucide="star" class="w-3.5 h-3.5 fill-amber-400 text-amber-400"></i>
                <i data-lucide="star" class="w-3.5 h-3.5 fill-amber-400 text-amber-400"></i>
                <i data-lucide="star" class="w-3.5 h-3.5 fill-amber-400 text-amber-400"></i>
              </div>
              <span class="text-gray-400 font-medium">(${tour.reviews})</span>
            </div>

            <button 
              type="button" 
              onclick="openBookingModal('${tour.title.replace(/'/g, "\\'")}', '${tour.departureDates ? tour.departureDates[0] : ''}', '${tour.price}')"
              class="px-3 py-1.5 bg-forest text-white text-xs font-semibold rounded-full hover:bg-forest/90 active:scale-95 transition-all shadow-sm"
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
 * Render Schedule Widget (Right column 30%)
 */
function renderSchedule() {
  const container = document.getElementById('schedule-list-container');
  if (!container) return;

  container.innerHTML = DEPARTURE_SCHEDULE.map(item => `
    <div 
      onclick="openBookingModal('${item.title.replace(/'/g, "\\'")}', '${item.dateFull}', '${item.price}')"
      class="schedule-row p-3 rounded-xl border border-gray-100 flex items-center justify-between cursor-pointer hover:border-emerald-200 transition-all bg-white"
    >
      <!-- Date Box -->
      <div class="flex items-center gap-3">
        <div class="w-12 h-12 rounded-xl bg-gray-50 border border-gray-200 flex flex-col items-center justify-center text-center shrink-0">
          <span class="text-base font-extrabold text-gray-900 leading-none">${item.day}</span>
          <span class="text-[10px] font-semibold text-gray-500 uppercase mt-0.5">${item.month}</span>
        </div>

        <!-- Tour Info -->
        <div>
          <h4 class="text-sm font-bold text-gray-800 line-clamp-1">${item.title}</h4>
          <p class="text-xs text-gray-500 mt-0.5 flex items-center gap-2">
            <span>${item.duration}</span>
            <span>•</span>
            <span class="font-medium text-forest">${item.price}</span>
          </p>
        </div>
      </div>

      <!-- Status & Arrow -->
      <div class="flex items-center gap-2 shrink-0">
        <span class="badge-seat text-[11px]">${item.status}</span>
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
 * Smooth Scroll Navigation & Active link highlight
 */
function setupSmoothScroll() {
  const navLinks = document.querySelectorAll('.nav-link');
  window.addEventListener('scroll', () => {
    const scrollPos = window.scrollY + 120;
    const sections = ['home', 'tours-section', 'schedule-section', 'why-us-section', 'testimonials-section', 'about-section', 'contact-section'];
    
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
