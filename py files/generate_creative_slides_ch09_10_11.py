import os

output_dir = r'd:\Code\Books\Transition for Iran\00- Iran in phase of Transition State\images\slides'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def create_federal_layers_slide(filename, chapter_title):
    svg = f'''<svg width="1080" height="1350" viewBox="0 0 1080 1350" xmlns="http://www.w3.org/2000/svg">
    <rect width="1080" height="1350" fill="#f0f4f8"/>
    <rect x="0" y="0" width="1080" height="100" fill="#1565C0"/>
    <foreignObject x="0" y="0" width="1080" height="100"><div xmlns="http://www.w3.org/1999/xhtml" style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; font-family:Vazirmatn; font-size:36px; font-weight:800; color:white; direction:rtl;">{chapter_title}</div></foreignObject>
    <text x="540" y="200" text-anchor="middle" font-family="'Vazirmatn'" font-size="52" font-weight="900" fill="#1565C0">ساختار چهارلایه حکومت</text>
    <g transform="translate(540, 300)">
        <rect x="-500" y="0" width="1000" height="140" rx="70" fill="#0D47A1"/><text y="60" text-anchor="middle" font-family="Vazirmatn" font-size="32" font-weight="900" fill="white">سطح ملی (فدرال)</text><text y="100" text-anchor="middle" font-family="Vazirmatn" font-size="18" fill="white">دفاع، سیاست خارجی، پول ملی</text>
        <path d="M0,140 L0,200" stroke="#1565C0" stroke-width="5" marker-end="url(#arrowhead)"/>
        <rect x="-400" y="200" width="800" height="140" rx="70" fill="#1976D2"/><text y="260" text-anchor="middle" font-family="Vazirmatn" font-size="32" font-weight="900" fill="white">سطح منطقه‌ای (ایالت‌ها)</text><text y="300" text-anchor="middle" font-family="Vazirmatn" font-size="18" fill="white">آموزش، توسعه محلی، پلیس منطقه‌ای</text>
        <path d="M0,340 L0,400" stroke="#1565C0" stroke-width="5" marker-end="url(#arrowhead)"/>
        <rect x="-300" y="400" width="600" height="140" rx="70" fill="#1E88E5"/><text y="460" text-anchor="middle" font-family="Vazirmatn" font-size="32" font-weight="900" fill="white">سطح استانی</text><text y="500" text-anchor="middle" font-family="Vazirmatn" font-size="18" fill="white">خدمات تخصصی، راه‌ها، بهداشت</text>
        <path d="M0,540 L0,600" stroke="#1565C0" stroke-width="5" marker-end="url(#arrowhead)"/>
        <rect x="-200" y="600" width="400" height="140" rx="70" fill="#42A5F5"/><text y="660" text-anchor="middle" font-family="Vazirmatn" font-size="32" font-weight="900" fill="white">سطح محلی</text><text y="700" text-anchor="middle" font-family="Vazirmatn" font-size="18" fill="white">شهرداری‌ها، خدمات شهری</text>
    </g>
    <defs><marker id="arrowhead" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto"><polygon points="0 0, 10 3.5, 0 7" fill="#1565C0" /></marker></defs>
    </svg>'''
    full_path = os.path.join(output_dir, filename)
    with open(full_path, 'wb') as f: f.write(svg.encode('utf-8'))
    print(f"Generated federal layers slide at: {full_path}")

def create_two_turnover_test_slide(filename, chapter_title):
    svg = f'''<svg width="1080" height="1350" viewBox="0 0 1080 1350" xmlns="http://www.w3.org/2000/svg">
    <rect width="1080" height="1350" fill="#fdfdfd"/>
    <rect x="0" y="0" width="1080" height="100" fill="#5D4037"/>
    <foreignObject x="0" y="0" width="1080" height="100"><div xmlns="http://www.w3.org/1999/xhtml" style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; font-family:Vazirmatn; font-size:36px; font-weight:800; color:white; direction:rtl;">{chapter_title}</div></foreignObject>
    <text x="540" y="240" text-anchor="middle" font-family="'Vazirmatn'" font-size="52" font-weight="900" fill="#5D4037">آزمونِ دو انتقال (Two-Turnover Test)</text>
    <g transform="translate(140, 450)">
        <rect width="300" height="400" rx="20" fill="#E8F5E9" stroke="#2E7D32" stroke-width="4"/><text x="150" y="100" text-anchor="middle" font-family="Vazirmatn" font-size="32" fill="#1B5E20">انتقال اول</text><text x="150" y="250" text-anchor="middle" font-family="Vazirmatn" font-size="20" fill="#388E3C">حاکمانِ گذار<br/>شکست در انتخابات را<br/>می‌پذیرند و می‌روند.</text>
        <path d="M300,200 L500,200" stroke="#5D4037" stroke-width="5" stroke-dasharray="10 5"/>
        <rect x="500" width="300" height="400" rx="20" fill="#E1F5FE" stroke="#0288D1" stroke-width="4"/><text x="650" y="100" text-anchor="middle" font-family="Vazirmatn" font-size="32" fill="#01579B">انتقال دوم</text><text x="650" y="250" text-anchor="middle" font-family="Vazirmatn" font-size="20" fill="#0288D1">جانشینان نیز<br/>در انتخابات بعد<br/>قدرت را واگذار می‌کنند.</text>
    </g>
    <foreignObject x="100" y="950" width="880" height="200"><div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn; font-size:24px; color:#5D4037; text-align:center; line-height:1.8;">دموکراسی زمانی <strong style="color:#C62828;">تحکیم</strong> می‌شود که نخبگان سیاسی بپذیرند <strong style="color:#2E7D32;">باختن در انتخابات</strong> پایان زندگی سیاسی نیست، بلکه بخشی از قواعد بازی است.</div></foreignObject>
    </svg>'''
    full_path = os.path.join(output_dir, filename)
    with open(full_path, 'wb') as f: f.write(svg.encode('utf-8'))
    print(f"Generated turnover test slide at: {full_path}")

def create_excellence_stairs_slide(filename, chapter_title):
    svg = f'''<svg width="1080" height="1350" viewBox="0 0 1080 1350" xmlns="http://www.w3.org/2000/svg">
    <rect width="1080" height="1350" fill="#121212"/>
    <rect x="0" y="0" width="1080" height="100" fill="#FFD700"/>
    <foreignObject x="0" y="0" width="1080" height="100"><div xmlns="http://www.w3.org/1999/xhtml" style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; font-family:Vazirmatn; font-size:36px; font-weight:800; color:#121212; direction:rtl;">{chapter_title}</div></foreignObject>
    <text x="540" y="220" text-anchor="middle" font-family="'Vazirmatn'" font-size="52" font-weight="900" fill="white">پله‌های تعالی: ایران در افق ۱۴۳۰</text>
    <g transform="translate(100, 350)">
        <path d="M0,800 L300,800 L300,600 L600,600 L600,400 L900,400 L900,200" fill="none" stroke="#FFD700" stroke-width="10"/>
        <g transform="translate(50, 680)"><text font-family="Vazirmatn" font-size="28" fill="#FFD700">سال ۵: نهادسازی</text></g>
        <g transform="translate(350, 480)"><text font-family="Vazirmatn" font-size="28" fill="#FFD700">سال ۱۰: تحکیم</text></g>
        <g transform="translate(650, 280)"><text font-family="Vazirmatn" font-size="28" fill="#FFD700">سال ۲۵: تعالی</text></g>
        <circle cx="900" cy="200" r="30" fill="#FFD700"/>
        <text x="900" y="150" text-anchor="middle" font-family="Vazirmatn" font-size="40" font-weight="900" fill="white">الگوی جهانی</text>
    </g>
    </svg>'''
    full_path = os.path.join(output_dir, filename)
    with open(full_path, 'wb') as f: f.write(svg.encode('utf-8'))
    print(f"Generated excellence stairs slide at: {full_path}")

create_federal_layers_slide('ch09_creative_2.svg', 'فصل ۹: فاز ۲ — نهادسازی (سال ۳-۵)')
create_two_turnover_test_slide('ch10_creative_2.svg', 'فصل ۱۰: فاز ۳ — تحکیم (سال ۶-۱۰)')
create_excellence_stairs_slide('ch11_creative_1.svg', 'فصل ۱۱: فاز ۴ و ۵ — بلوغ و تعالی')
