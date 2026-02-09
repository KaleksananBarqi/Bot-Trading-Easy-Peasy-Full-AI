# 🤖 Easy Peasy Trading Bot: AI Vision & Logic Sniper

<div align="center">


  <br />
  
  ![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
  ![Binance](https://img.shields.io/badge/Binance-Futures-yellow?style=for-the-badge&logo=binance)
  ![DeepSeek](https://img.shields.io/badge/Brain-DeepSeek%20V3.2-blueviolet?style=for-the-badge)
  ![Vision AI](https://img.shields.io/badge/Vision-Llama%20Vision-ff69b4?style=for-the-badge)
  ![Sentiment AI](https://img.shields.io/badge/Sentiment-Xiaomi%20Mimo-orange?style=for-the-badge)
  ![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)
  ![License](https://img.shields.io/badge/License-PolyForm%20Noncommercial-5D6D7E?style=for-the-badge)
</div>

---

## 📖 Tentang Easy Peasy Bot (Multi AI Edition)

**Easy Peasy Trading Bot** adalah sistem trading **Hybrid Multi-AI** tercanggih yang menggabungkan analisis logika, tekstual, dan kemampuan visual (computer vision) untuk menguasai market crypto.

Dibangun di atas arsitektur **Triple AI Core**, bot ini tidak hanya menghitung angka, tapi juga "membaca" narasi berita dan "melihat" struktur market secara visual layaknya trader pro.

### 🧠 The Triple AI Core
1.  **Strategic Brain (Logic AI)**: Ditenagai oleh **DeepSeek V3.2**. Bertugas sebagai eksekutor utama yang mengambil keputusan BUY/SELL/WAIT berdasarkan data teknikal, on-chain, dan sentimen secara holistik.
2.  **Visual Cortex (Vision AI)**: Ditenagai oleh **Llama-4-Maverick**. Modul Vision yang menganalisis chart candlestick real-time untuk mendeteksi pola murni (Flags, Pennants, Divergence) dan validasi struktur market.
3.  **Sentiment Analyst (Text AI)**: Ditenagai oleh **Xiaomi Mimo V2 Flash**. Spesialis narasi yang melakukan scanning berita global, news RSS, dan Fear & Greed index untuk menentukan "Market Vibe" saat ini.

---

## 🚀 Fitur Utama & Keunggulan

### 1. ⚖️ Objective Market Analysis (Multi-Scenario Thinking) - **NEW!**
Bot dirancang untuk menghilangkan bias emosional. Pada setiap analisa, AI diinstruksikan untuk:
*   **Neutral Evaluation**: Menilai struktur market secara objektif (Bullish vs Bearish) tanpa asumsi awal.
*   **Scenario Mapping**: Mengidentifikasi zona kunci untuk kedua kemungkinan (jika harga naik tembus R1 vs jika harga turun jebol S1).
*   **Best Path Selection**: AI memilih **SATU** skenario dengan probabilitas tertinggi (High Probability Setup) untuk dieksekusi, atau memilih **WAIT** jika kondisi ambigu.

### 2. 👁️ Vision AI Pattern Recognition
Integrasi Computer Vision yang canggih:
*   **Chart Rendering**: Otomatis mencetak chart teknikal lengkap dengan indikator.
*   **Validasi Pola**: AI Vision memvalidasi apakah ada pola reversal atau continuation.
*   **MACD Divergence Detection**: Deteksi visual divergensi harga vs momentum.

### 3. 🛡️ Multi-Strategy AI System

Bot tidak hanya mengandalkan satu strategi! AI akan **memilih strategi terbaik** berdasarkan kondisi market saat itu:

| Strategi | Kondisi Optimal | Cara Kerja |
|----------|-----------------|------------|
| **LIQUIDITY_REVERSAL_MASTER** | Sweep rejection di Pivot S1/R1 | Entry saat harga menyapu liquidity zone lalu berbalik |
| **PULLBACK_CONTINUATION** | Trend kuat dengan pullback ke EMA | Entry saat pullback di uptrend atau bounce di downtrend |
| **BREAKDOWN_FOLLOW** | Breakout dengan volume tinggi | Follow momentum breakout dari level S1/R1 |

#### 🏆 Strategi Unggulan: Liquidity Hunt Specialist (PROVEN!)

Bot menggunakan strategi **Liquidity Hunt Specialist** yang fokus mencari titik balik di area "Stop Run" dan "Liquidity Grab" — zona di mana market maker sering memburu stop loss retail trader sebelum membalikkan arah.

**📊 Hasil Backtest (Januari 2026)**
| Metrik | Hasil |
|--------|-------|
| **Total Profit** | +$845.42 (+84.54%) |
| **Modal Awal → Akhir** | $1,000 → $1,845.42 |
| **Win Rate** | 84.52% (71 TP, 13 SL) |
| **Total Trades** | 84 trades |
| **Profit Factor** | 7.94 |
| **Max Drawdown** | -1.82% ✅ (Sangat aman) |

**🏆 Performa per Koin**
| Koin | Profit | Total Trades |
|------|--------|--------------|
| SOL/USDT | +$566.16 | 40 trades |
| BTC/USDT | +$279.26 | 44 trades |

**💡 Konsep Strategi**
1. **Deteksi Liquidity Zone**: Identifikasi area di mana banyak stop loss berkumpul
2. **Tunggu "Sweep"**: Sabar menunggu harga menyapu zona likuiditas
3. **Entry saat Reversal**: Masuk posisi setelah konfirmasi pembalikan arah
4. **Risk Terkontrol**: SL ketat di bawah swing low/high terdekat

### 4. 🤖 Full AI-Driven Trading Setup (AI-Only Mode) - **NEW!**
Bot kini beroperasi dalam mode **Full AI-Driven**, di mana AI memiliki kendali penuh atas eksekusi trading:

*   **AI Entry Determination**: AI menentukan `Entry Price` terbaik berdasarkan analisis teknikal & sentimen.
*   **AI Take Profit (TP)**: AI menetapkan target profit yang realistis.
*   **AI Stop Loss (SL)**: AI menentukan batas kerugian untuk menjaga risk management.

**Validasi Setup AI (Safety First):**
Sebelum eksekusi, sistem melakukan validasi ketat terhadap output AI:
1.  **Logical Check**: Memastikan `TP > Entry > SL` (untuk Long) atau sebaliknya (untuk Short).
2.  **Risk:Reward Ratio**: Setup ditolak jika R:R < `MIN_RISK_REWARD_RATIO` (Default: 1:1.5).
3.  **SL Distance**: Warning jika SL terlalu jauh (> `MAX_SL_DISTANCE_PERCENT` dari entry).

> **Note**: Jika AI gagal memberikan setup yang valid atau R:R terlalu kecil, order otomatis **DIBATALKAN** demi keamanan.

### 5. 🪙 Smart Per-Coin Configuration - **NEW!**
Setiap koin dalam daftar pantau dapat dikustomisasi secara spesifik:
*   **Specific Keywords**: News filtering yang lebih akurat per aset.
*   **BTC Correlation Toggle**: Opsi untuk mengikuti atau mengabaikan tren Bitcoin.
*   **Custom Leverage & Margin**: Pengaturan risiko berbeda untuk setiap koin.

### 6. 📑 Dynamic Prompt Generation
Sistem prompt AI yang cerdas dan adaptif:
*   **Toggle-able Market Orders**: Jika `ENABLE_MARKET_ORDERS = False`, AI hanya akan diberikan opsi Limit Order (Liquidity Hunt) untuk meminimalkan slippage dan fee.
*   **Contextual Hiding**: Jika korelasi BTC rendah, data BTC akan disembunyikan agar AI fokus pada price action independen koin tersebut.

### 7. 📢 Pro-Grade Notifications with ROI - **NEW!**
Notifikasi Telegram yang mendetail dan transparan:
*   **Start-to-Finish Tracking**: Notifikasi saat Order Created (Limit), Filled (Entry), hingga TP/SL Hit.
*   **Profit/Loss Estimation**: Estimasi potensi keuntungan (Green) dan kerugian (Red) ditampilkan sejak awal entry.
*   **Realized ROI**: Kalkulasi ROI (%) akurat berdasarkan margin dan leverage saat posisi ditutup.

### 8. 📰 Smart News Filtering System - **NEW!**
Sistem filter berita cerdas yang memastikan AI hanya menerima informasi relevan:

**Mekanisme Filtering:**
*   **Kategori Makro (Prioritas 1)**: Berita tentang Fed, inflasi, regulasi - maksimal 3 berita
*   **Kategori Koin Spesifik (Prioritas 2)**: Berita langsung tentang koin yang dianalisis - minimal 4 berita
*   **Kategori BTC Correlation (Prioritas 3)**: Berita Bitcoin untuk non-BTC coins - maksimal 3 berita

**Keunggulan:**
*   ✅ Menghindari "noise" dari berita tidak relevan
*   ✅ Mencegah AI berhalusinasi karena informasi campur aduk
*   ✅ Keyword customizable per koin di `config.py`
*   ✅ Sumber berita dari 15+ RSS feeds internasional & Indonesia

### 9. 🔄 Intelligent Trailing Stop Loss
Sistem trailing stop otomatis yang mengunci profit saat market bergerak menguntungkan:

**Cara Kerja:**
1. Bot membuka posisi dengan SL & TP awal
2. Saat harga bergerak **80%** menuju TP → Trailing Stop aktif
3. SL otomatis naik/turun mengikuti harga dengan jarak 0.75%
4. Minimal profit 0.5% dikunci saat trailing aktif

**Ilustrasi (LONG Position):**
```
Entry: $100 | TP: $110 | SL Awal: $97
Harga naik ke $108 (80% ke TP) → Trailing Aktif!
- SL baru: $107.19 (0.75% di bawah harga tertinggi)
Harga naik ke $109 → SL naik ke $108.18
Harga turun ke $108.50 → SL tetap $108.18 (terkunci!)
Harga turun ke $108.18 → Posisi ditutup dengan profit ~8%
```

### 10. 📈 Multi-Timeframe Technical Analysis
Arsitektur analisis 3-layer untuk presisi maksimal:

| Layer | Timeframe | Fungsi | Indikator |
|-------|-----------|--------|------------|
| **TREND** | 1H | Arah tren besar | EMA 21, ADX |
| **SETUP** | 30M | Deteksi pola | MACD |
| **EXECUTION** | 15M | Entry timing | RSI, StochRSI, Bollinger Bands |

### 11. ❄️ Cooldown Anti-FOMO/Revenge Trading
Mekanisme pendinginan otomatis setelah trade selesai:
*   **Setelah PROFIT**: Jeda 1 jam sebelum re-entry di koin yang sama
*   **Setelah LOSS**: Jeda 2 jam untuk mencegah revenge trading

### 12. ⏰ Limit Order Expiry System
Pembersihan otomatis limit order yang tidak terisi:
*   Order yang pending > 2 jam akan **auto-cancel**
*   Mencegah order "zombie" yang menggantung
*   Sinkronisasi real-time dengan exchange

### 13. 🐋 On-Chain Whale Detection
Deteksi transaksi whale secara real-time via WebSocket:
*   Threshold: > $1,000,000 USDT
*   Pelacakan per-koin (bukan global)
*   Integrasi dengan Stablecoin Inflow dari DeFiLlama
*   De-duplication untuk mencegah spam notifikasi

### 14. 📚 Order Book Depth Analysis
Analisis kedalaman order book untuk deteksi buying/selling pressure:
*   Range analisis: 2% dari current price
*   Kalkulasi bid/ask volume dalam USDT
*   Imbalance percentage untuk konfirmasi momentum

---

## 🛠️ Instalasi & Konfigurasi

### Persyaratan Sistem & API
*   **Python 3.10+** (Wajib)
*   **pip** dan **venv** (tools Python bawaan)
*   **Git** untuk clone repository
*   **Akun Binance Futures**: API Key & Secret Key (Enable Futures Trading & Read)
*   **Telegram Bot**: Token & Chat ID (Untuk notifikasi real-time)
*   **AI Provider API**: Key dari [OpenRouter](https://openrouter.ai/) atau DeepSeek
*   **CoinMarketCap API**: Key untuk analisis data fundamental & berita
*   *(Opsional)* **Binance Testnet**: API Key khusus jika ingin menggunakan uang monopoli
*   *(Opsional)* **Telegram Channel Khusus**: Token & Chat ID terpisah untuk log analisis sentimen

---

### 💻 Instalasi di Windows

<details>
<summary>Klik untuk melihat langkah-langkah Windows</summary>

**1. Install Python 3.10+**
- Download dari [python.org/downloads](https://www.python.org/downloads/)
- ⚠️ **PENTING**: Centang "Add Python to PATH" saat instalasi!
- Verifikasi: Buka PowerShell/CMD, ketik: `python --version`

**2. Clone Repository**
```powershell
cd C:\Projects  # atau folder pilihan kamu
git clone https://github.com/KaleksananBarqi/Bot-Trading-Easy-Peasy.git
cd Bot-Trading-Easy-Peasy
```

**3. Buat Virtual Environment**
```powershell
python -m venv venv
.\venv\Scripts\Activate
```

**4. Install Dependencies**
```powershell
pip install -e .
```

**5. Setup Konfigurasi**
- Buat file `.env` di root folder (gunakan `copy .env.example .env`)
- Isi semua API Key yang diperlukan
- Ubah pengaturan di `src/config.py` sesuai kebutuhan

**6. Jalankan Bot**
```powershell
python src/main.py
```

</details>

---

### 🍎 Instalasi di macOS

<details>
<summary>Klik untuk melihat langkah-langkah macOS</summary>

**1. Install Python 3.10+ via Homebrew**
```bash
# Install Homebrew (jika belum ada)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python
brew install python@3.10

# Verifikasi
python3 --version
```

**2. Clone Repository**
```bash
cd ~/Projects  # atau folder pilihan kamu
git clone https://github.com/KaleksananBarqi/Bot-Trading-Easy-Peasy.git
cd Bot-Trading-Easy-Peasy
```

**3. Buat Virtual Environment**
```bash
python3 -m venv venv
source venv/bin/activate
```

**4. Install Dependencies**
```bash
pip install -e .
```

**5. Setup Konfigurasi**
- Buat file `.env` di root folder
- Isi semua API Key yang diperlukan
- Ubah pengaturan di `src/config.py` sesuai kebutuhan

**6. Jalankan Bot**
```bash
python src/main.py
```

</details>

---

### 🐧 Instalasi di Linux Server (Ubuntu/Debian)

<details>
<summary>Klik untuk melihat langkah-langkah Linux Server</summary>

**1. Update Sistem & Install Dependencies**
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3.10 python3.10-venv python3-pip git screen -y
```

**2. Clone Repository**
```bash
cd /opt  # atau /home/username
sudo git clone https://github.com/KaleksananBarqi/Bot-Trading-Easy-Peasy.git
sudo chown -R $USER:$USER Bot-Trading-Easy-Peasy
cd Bot-Trading-Easy-Peasy
```

**3. Buat Virtual Environment**
```bash
python3.10 -m venv venv
source venv/bin/activate
```

**4. Install Dependencies**
```bash
pip install --upgrade pip
pip install -e .
```

**5. Setup Konfigurasi**
```bash
# Buat file .env dari template
cp .env.example .env
nano .env
# Isi API Keys, lalu Simpan: Ctrl+X, Y, Enter
```

**6. Jalankan Bot (Background dengan Screen)**
```bash
# Jalankan dalam screen session
screen -S trading-bot
python src/main.py

# Lepas dari session: Ctrl+A, D
# Kembali ke session: screen -r trading-bot
# Lihat daftar session: screen -ls
```

**7. (Opsional) Systemd Service untuk Auto-Start**
```bash
sudo nano /etc/systemd/system/trading-bot.service
```

Isi file service (sesuaikan user & path):
```ini
[Unit]
Description=Easy Peasy Trading Bot
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/opt/Bot-Trading-Easy-Peasy
ExecStart=/opt/Bot-Trading-Easy-Peasy/venv/bin/python src/main.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Aktifkan service:
```bash
sudo systemctl daemon-reload
sudo systemctl enable trading-bot
sudo systemctl start trading-bot
sudo systemctl status trading-bot
```

</details>

---

### ⚙️ Konfigurasi Penting (`src/config.py`)
Pastikan Anda menyesuaikan parameter berikut sesuai risk profile Anda:

| Parameter | Deskripsi | Default |
|-----------|-----------|---------|
| `MIN_RISK_REWARD_RATIO` | Minimal rasio profit vs loss yang diterima AI | `1.5` |
| `MAX_SL_DISTANCE_PERCENT` | Batas maksimal jarak Stop Loss dari Entry | `0.10` (10%) |
| `AI_CONFIDENCE_THRESHOLD` | Minimal keyakinan AI untuk eksekusi | `70` (%) |
| `ENABLE_MARKET_ORDERS` | `True` = Hajar Kanan (Cepat), `False` = Limit Only (Hemat Fee) | `False` |

---

## 📊 Struktur Proyek

```text
📂 Bot-Trading-Easy-Peasy/
 ├── 📂 src/                     # 🚀 Source Code Utama
 │    ├── 📂 modules/            # Modul Logika Inti
 │    │    ├── 🧠 ai_brain.py           # Otak Utama AI
 │    │    ├── 👁️ pattern_recognizer.py # Vision AI Engine
 │    │    ├── ⚙️ executor.py           # Eksekusi Order & Sync Posisi
 │    │    ├── 📊 market_data.py        # Pengolah Data & Indikator
 │    │    ├── 🗞️ sentiment.py          # Analisis Berita & RSS
 │    │    └── 🐋 onchain.py            # Deteksi Whale & Stablecoin Inflow
 │    ├── 📂 utils/              # Fungsi Pembantu
 │    │    ├── 🧮 calc.py               # Validasi AI Setup & Estimasi PnL
 │    │    ├── 📝 prompt_builder.py     # Konstruktor Prompt AI Dinamis
 │    │    └── 🛠️ helper.py             # Logger & Tele Utils
 │    ├── ⚙️ config.py                 # PUSAT KONFIGURASI
 │    └── 🚀 main.py                   # Titik Masuk Bot
 ├── 📂 backtesting/             # ⏳ Sistem Pengujian Historis
 │    ├── 📊 backtest.py               # Engine Backtest Utama
 │    └── 📈 backtest_result.md        # Hasil & Laporan Backtest
 ├── 📂 tests/                   # 🧪 Automated Testing (25+ test files)
 └── 📦 pyproject.toml           # Manajemen Dependensi Modern
```

---

## 🧪 Automated Testing

Proyek ini dilengkapi dengan **25+ automated test files** untuk memastikan kualitas kode:

```bash
# Menjalankan semua tests
python -m pytest tests/

# Menjalankan test spesifik
python -m pytest tests/test_trailing_logic.py
```

**Test Coverage:**
*   ✅ Trailing Stop Logic
*   ✅ News Filtering System
*   ✅ Pattern Recognition Validation
*   ✅ Limit Order Expiry
*   ✅ Profit/Loss Calculation
*   ✅ Market Data Optimization
*   ✅ Benchmark Performance Tests

---

## 🤝 Kontribusi
Kami terbuka untuk perbaikan strategi, optimasi AI, atau dokumentasi. Silakan ajukan **Pull Request** atau buka **Issue** jika menemukan bug.

---

## ⚠️ Disclaimer
**Trading crypto futures melibatkan risiko finansial yang besar.** Bot ini adalah alat bantu berbasis AI, bukan jaminan keuntungan. **AI bisa berhalusinasi** atau salah sinyal. Gunakan modal yang siap hilang dan aktifkan fitur risk management di `config.py`.

---
**Developed with ☕ & 🤖 by [Kaleksanan Barqi Aji Massani](https://github.com/KaleksananBarqi)**