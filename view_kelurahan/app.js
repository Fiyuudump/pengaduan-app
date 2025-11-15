// app.js - Frontend JavaScript untuk konsumsi API Warga Kelurahan

// Variabel global untuk menyimpan state
let currentPage = 1;
let nextPageUrl = null;
let previousPageUrl = null;
let currentSearchQuery = '';

// Base API URL
const API_BASE_URL = 'http://127.0.0.1:8000/api/warga/';

/**
 * Event listener yang dijalankan setelah DOM selesai dimuat
 */
document.addEventListener('DOMContentLoaded', () => {
    console.log('📱 Aplikasi Frontend dimulai...');
    fetchWargaData(API_BASE_URL);
    
    // Add Enter key support for search
    document.getElementById('search-input').addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            searchWarga();
        }
    });
});

/**
 * Fungsi untuk membuat elemen HTML untuk setiap warga
 * @param {Object} warga - Data warga dari API
 * @returns {HTMLElement} - Element div yang berisi data warga
 */
function renderWarga(warga) {
    const wargaDiv = document.createElement('div');
    wargaDiv.className = 'warga-item';

    const nama = document.createElement('h3');
    nama.textContent = warga.nama_lengkap;

    const nik = document.createElement('p');
    nik.innerHTML = `<strong>NIK:</strong> ${warga.nik}`;

    const alamat = document.createElement('p');
    alamat.innerHTML = `<strong>Alamat:</strong> ${warga.alamat}`;

    const tanggalLahir = document.createElement('p');
    tanggalLahir.innerHTML = `<strong>Tanggal Lahir:</strong> ${warga.tanggal_lahir}`;

    wargaDiv.appendChild(nama);
    wargaDiv.appendChild(nik);
    wargaDiv.appendChild(alamat);
    wargaDiv.appendChild(tanggalLahir);

    // Tambahkan nomor telepon jika ada
    if (warga.no_telepon) {
        const telepon = document.createElement('p');
        telepon.innerHTML = `<strong>Telepon:</strong> ${warga.no_telepon}`;
        wargaDiv.appendChild(telepon);
    }

    // Tambahkan email jika ada
    if (warga.email) {
        const email = document.createElement('p');
        email.innerHTML = `<strong>Email:</strong> ${warga.email}`;
        wargaDiv.appendChild(email);
    }

    // Tambahkan tanggal registrasi
    const tanggalRegistrasi = document.createElement('p');
    tanggalRegistrasi.innerHTML = `<strong>Registrasi:</strong> ${new Date(warga.tanggal_registrasi).toLocaleDateString('id-ID')}`;
    wargaDiv.appendChild(tanggalRegistrasi);

    return wargaDiv;
}

/**
 * Fungsi utama untuk mengambil data dari API
 * @param {string} url - URL endpoint API
 */
function fetchWargaData(url) {
    const container = document.getElementById('warga-list-container');
    const statusElement = document.getElementById('connection-status');
    
    // Tampilkan loading
    container.innerHTML = '<p class="loading">⏳ Memuat data...</p>';
    statusElement.textContent = 'Loading...';
    statusElement.style.color = '#f39c12';

    console.log(`🌐 Fetching data from: ${url}`);

    fetch(url)
        .then(response => {
            console.log(`📡 Response status: ${response.status}`);
            
            // Cek apakah response berhasil
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            
            statusElement.textContent = '✅ Connected';
            statusElement.style.color = '#27ae60';
            
            return response.json();
        })
        .then(data => {
            console.log('📦 Data received:', data);
            
            // Clear container
            container.innerHTML = '';

            // Update total count
            document.getElementById('total-count').textContent = data.count || data.results.length;

            // Cek apakah ada data
            if (data.results && data.results.length > 0) {
                // Render setiap warga
                data.results.forEach(warga => {
                    const wargaElement = renderWarga(warga);
                    container.appendChild(wargaElement);
                });

                // Update pagination state
                nextPageUrl = data.next;
                previousPageUrl = data.previous;
                
                // Update pagination UI
                updatePagination(data);
                
                console.log(`✅ Successfully rendered ${data.results.length} warga`);
            } else {
                container.innerHTML = '<p class="loading">Tidak ada data warga ditemukan.</p>';
            }
        })
        .catch(error => {
            console.error('❌ Error fetching data:', error);
            
            statusElement.textContent = '❌ Connection Failed';
            statusElement.style.color = '#e74c3c';
            
            container.innerHTML = `
                <div class="error">
                    <h3>⚠️ Gagal Memuat Data</h3>
                    <p>Error: ${error.message}</p>
                    <p style="margin-top: 10px;">
                        <strong>Troubleshooting:</strong><br>
                        1. Pastikan server Django berjalan di http://127.0.0.1:8000<br>
                        2. Pastikan django-cors-headers sudah terinstall dan dikonfigurasi<br>
                        3. Cek console browser untuk detail error
                    </p>
                </div>
            `;
        });
}

/**
 * Update pagination UI dan state
 * @param {Object} data - Response data dari API
 */
function updatePagination(data) {
    const paginationDiv = document.getElementById('pagination');
    const prevBtn = document.getElementById('prev-btn');
    const nextBtn = document.getElementById('next-btn');
    const pageInfo = document.getElementById('page-info');

    // Show pagination only if there are results
    if (data.count > 0) {
        paginationDiv.style.display = 'flex';
        
        // Calculate current page
        const pageSize = 10;
        const totalPages = Math.ceil(data.count / pageSize);
        
        // Update page info
        pageInfo.textContent = `Page ${currentPage} of ${totalPages} (Total: ${data.count} warga)`;
        
        // Update button states
        prevBtn.disabled = !data.previous;
        nextBtn.disabled = !data.next;
    } else {
        paginationDiv.style.display = 'none';
    }
}

/**
 * Load halaman berikutnya
 */
function loadNextPage() {
    if (nextPageUrl) {
        currentPage++;
        fetchWargaData(nextPageUrl);
        window.scrollTo({ top: 0, behavior: 'smooth' });
    }
}

/**
 * Load halaman sebelumnya
 */
function loadPreviousPage() {
    if (previousPageUrl) {
        currentPage--;
        fetchWargaData(previousPageUrl);
        window.scrollTo({ top: 0, behavior: 'smooth' });
    }
}

/**
 * Fungsi untuk search warga
 */
function searchWarga() {
    const searchInput = document.getElementById('search-input');
    const searchQuery = searchInput.value.trim();
    
    if (searchQuery) {
        currentSearchQuery = searchQuery;
        currentPage = 1;
        const searchUrl = `${API_BASE_URL}?search=${encodeURIComponent(searchQuery)}`;
        console.log(`🔍 Searching for: ${searchQuery}`);
        fetchWargaData(searchUrl);
    } else {
        alert('Masukkan kata kunci pencarian!');
    }
}

/**
 * Fungsi untuk reset search dan kembali ke tampilan awal
 */
function resetSearch() {
    document.getElementById('search-input').value = '';
    currentSearchQuery = '';
    currentPage = 1;
    fetchWargaData(API_BASE_URL);
}

/**
 * Fungsi helper untuk format tanggal
 * @param {string} dateString - String tanggal dari API
 * @returns {string} - Tanggal yang sudah diformat
 */
function formatDate(dateString) {
    const options = { year: 'numeric', month: 'long', day: 'numeric' };
    return new Date(dateString).toLocaleDateString('id-ID', options);
}

// Log info ke console
console.log('🚀 Frontend Application Loaded');
console.log('📍 API Endpoint:', API_BASE_URL);
console.log('ℹ️  Pastikan Django server berjalan di http://127.0.0.1:8000');
