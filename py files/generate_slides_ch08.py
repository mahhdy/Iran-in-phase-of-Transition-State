import os

output_dir = r'd:\Code\Books\Transition for Iran\00- Iran in phase of Transition State\images\slides'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def create_svg(filename, chapter_title, slide_title, content_blocks):
    svg_start = f'''<svg width="1080" height="1350" viewBox="0 0 1080 1350" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="headerGrad" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" style="stop-color:#0D47A1;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#1976D2;stop-opacity:1" />
        </linearGradient>
    </defs>
    <rect width="1080" height="1350" fill="#E3F2FD" opacity="0.3" />
    <rect width="1080" height="1350" fill="white" />
    
    <rect width="1080" height="120" fill="#1565C0" />
    <foreignObject x="40" y="35" width="1000" height="60">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn', sans-serif; color: white; font-size: 34px; font-weight: bold;">
            {chapter_title}
        </div>
    </foreignObject>
    
    <foreignObject x="60" y="160" width="960" height="140">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn', sans-serif; color: #0D47A1; font-size: 50px; font-weight: 900; line-height: 1.3;">
            {slide_title}
        </div>
    </foreignObject>
    
    <g transform="translate(60, 310)">
    '''
    
    y_offset = 0
    cards_svg = ""
    
    for block in content_blocks:
        label = block.get('label', '')
        text = block.get('text', '')
        color = block.get('color', '#1565C0')
        is_hero = block.get('hero', False)
        
        text_len = len(text)
        height = 190
        if is_hero: height = 280
        if text_len > 120: height += 60
        if text_len > 220: height += 80
        
        card = f'''
        <rect y="{y_offset}" width="960" height="{height}" rx="28" fill="white" style="filter: drop-shadow(0 12px 24px rgba(21,101,192,0.12));" />
        <rect x="0" y="{y_offset + 30}" width="12" height="{height - 60}" rx="6" fill="{color}" />
        
        <foreignObject x="50" y="{y_offset + 35}" width="860" height="{height - 70}">
            <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn', sans-serif;">
                <div style="color: {color}; font-size: 26px; font-weight: 800; margin-bottom: 20px; text-decoration: underline;">{label}</div>
                <div style="color: #263238; font-size: { '44px' if is_hero else '32px' }; font-weight: { '900' if is_hero else '500' }; line-height: 1.6;">
                    {text}
                </div>
            </div>
        </foreignObject>
        '''
        cards_svg += card
        y_offset += height + 40
        
    svg_end = f'''
    </g>
    
    <text x="540" y="1310" text-anchor="middle" font-family="'Vazirmatn', sans-serif" font-size="22" font-weight="bold" fill="#1565C0" opacity="0.4">نقشه راه ۲۴ ماهه گذار • ۲۰۲۶</text>
    </svg>
    '''
    
    full_svg = svg_start + cards_svg + svg_end
    
    full_path = os.path.join(output_dir, filename)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(full_svg)
    print(f"Generated: {full_path}")

# Chapter 8 Slides Data
slides_data_ch08 = [
    {
        'filename': 'ch08_slide1.svg',
        'chapter': 'فاز ۱: گذار اولیه (سال ۱-۲)',
        'title': 'نقشه راه ۲۴ ماه نخست گذار',
        'blocks': [
            {'label': 'تبیین وضعیت', 'text': 'فاز اول حیاتی‌ترین دوره است. در این ۲۴ ماه باید هم‌زمان نظم عمومی حفظ شود و اصلاحات ساختاری آغاز گردد.', 'color': '#1565C0'},
            {'label': 'هدف نهایی', 'text': 'تشکیل شورای انتقالی، دولت موقت و برگزاری انتخابات مجلس مؤسسان برای تدوین قانون اساسی جدید.', 'color': '#2E7D32', 'hero': True}
        ]
    },
    {
        'filename': 'ch08_slide2.svg',
        'chapter': 'فاز ۱: گذار اولیه (سال ۱-۲)',
        'title': 'لحظه صفر: مدیریت ۷۲ ساعت اول',
        'blocks': [
            {'label': 'اولویت‌های فوری', 'text': 'کنترل امنیتی زیرساخت‌ها، درخواست آرامش و تداوم خدمات پایه (آب و برق) برای جلوگیری از هرج‌ومرج.', 'color': '#1565C0'},
            {'label': 'هشدار راهبردی', 'text': 'خلأ قدرت فاجعه‌بار است؛ نیروهای دموکراتیک باید برای استقرار سریع نهادهای موقت آمادگی کامل داشته باشند.', 'color': '#F9A825', 'hero': True}
        ]
    },
    {
        'filename': 'ch08_slide3.svg',
        'chapter': 'فاز ۱: گذار اولیه (سال ۱-۲)',
        'title': 'شورای انتقالی و دولت موقت',
        'blocks': [
            {'label': 'ترکیب شمول‌گرا', 'text': 'شورای ۲۱ نفره شامل رهبران اعتراضی، اقوام، زنان و متخصصان؛ ضامن مشروعیت و ائتلاف بزرگ ملی.', 'color': '#1565C0'},
            {'label': 'وظایف اجرایی', 'text': 'دولت موقت تکنوکرات مأمور مهار تورم، آزادی زندانیان و بسترسازی برای انتخابات آزاد است.', 'color': '#1A237E', 'hero': True}
        ]
    },
    {
        'filename': 'ch08_slide4.svg',
        'chapter': 'فاز ۱: گذار اولیه (سال ۱-۲)',
        'title': 'اقتصاد اضطراری و رفع تحریم‌ها',
        'blocks': [
            {'label': 'گشایش اقتصادی', 'text': '«معامله بزرگ» با جهان برای رفع کامل تحریم‌ها و آزادسازی ۱۰۰+ میلیارد دلار دارایی‌های ایران.', 'color': '#1565C0'},
            {'label': 'آبادانی ملموس', 'text': 'تثبیت قیمت‌ها و بهبود معیشت در ۱۰۰ روز اول، قوی‌ترین ابزار برای تحکیم دموکراسی نوپا است.', 'color': '#2E7D32', 'hero': True}
        ]
    },
    {
        'filename': 'ch08_slide5.svg',
        'chapter': 'فاز ۱: گذار اولیه (سال ۱-۲)',
        'title': 'مؤسسان و میثاق ملی نوین',
        'blocks': [
            {'label': 'قانون اساسی جدید', 'text': 'تدوین قانون اساسی بر پایه حقوق بشر و کثرت‌گرایی توسط برگزیدگان ملت در مجلس مؤسسان.', 'color': '#1565C0'},
            {'label': 'همه‌پرسی نهایی', 'text': 'تصویب میثاق نوین ایرانیان با رأی مستقیم مردم؛ آغاز دوران حاکمیت قانون و بالندگی ملی.', 'color': '#F9A825', 'hero': True}
        ]
    }
]

for slide in slides_data_ch08:
    create_svg(slide['filename'], slide['chapter'], slide['title'], slide['blocks'])
