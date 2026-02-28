import os

output_dir = r'd:\Code\Books\Transition for Iran\00- Iran in phase of Transition State\images\slides'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def create_svg(filename, chapter_title, slide_title, content_blocks):
    svg_start = f'''<svg width="1080" height="1350" viewBox="0 0 1080 1350" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="headerGrad" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" style="stop-color:#37474F;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#263238;stop-opacity:1" />
        </linearGradient>
    </defs>
    <rect width="1080" height="1350" fill="#ECEFF1" opacity="0.4" />
    <rect width="1080" height="1350" fill="white" />
    
    <rect width="1080" height="120" fill="#263238" />
    <foreignObject x="40" y="35" width="1000" height="60">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn', sans-serif; color: white; font-size: 34px; font-weight: bold;">
            {chapter_title}
        </div>
    </foreignObject>
    
    <foreignObject x="60" y="160" width="960" height="140">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn', sans-serif; color: #263238; font-size: 50px; font-weight: 900; line-height: 1.3;">
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
        color = block.get('color', '#263238')
        is_hero = block.get('hero', False)
        
        text_len = len(text)
        height = 190
        if is_hero: height = 280
        if text_len > 120: height += 60
        if text_len > 220: height += 80
        
        card = f'''
        <rect y="{y_offset}" width="960" height="{height}" rx="28" fill="white" style="filter: drop-shadow(0 12px 24px rgba(38,50,56,0.12));" />
        <rect x="0" y="{y_offset}" width="16" height="{height}" rx="8" fill="{color}" />
        
        <foreignObject x="50" y="{y_offset + 35}" width="860" height="{height - 70}">
            <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn', sans-serif;">
                <div style="color: {color}; font-size: 26px; font-weight: 800; margin-bottom: 20px; font-variant-numeric: tabular-nums;">{label}</div>
                <div style="color: #2D3436; font-size: { '44px' if is_hero else '32px' }; font-weight: { '900' if is_hero else '500' }; line-height: 1.6;">
                    {text}
                </div>
            </div>
        </foreignObject>
        '''
        cards_svg += card
        y_offset += height + 40
        
    svg_end = f'''
    </g>
    
    <text x="540" y="1310" text-anchor="middle" font-family="'Vazirmatn', sans-serif" font-size="22" font-weight="bold" fill="#263238" opacity="0.6">پیمان پایدار شهروندی • ۲۰۲۶</text>
    </svg>
    '''
    
    full_svg = svg_start + cards_svg + svg_end
    
    full_path = os.path.join(output_dir, filename)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(full_svg)
    print(f"Generated: {full_path}")

# Chapter 15 Slides Data
slides_data_ch15 = [
    {
        'filename': 'ch15_slide1.svg',
        'chapter': 'فصل ۱۵: پایش، ارزیابی و مدیریت ریسک',
        'title': 'پایش: قطب‌نمای مسیر گذار',
        'blocks': [
            {'label': 'تبیین ضرورت', 'text': 'آنچه اندازه‌گیری نشود، مدیریت نمی‌شود. پایش مستمر و علمی، تنها ابزار برای جلوگیری از انحراف گذار و تضمین تحقق وعده‌هاست.', 'color': '#263238'},
            {'label': 'داشبورد ملی', 'text': 'استقرار سیستم رهگیری لحظه‌ای با ۵۰ شاخص کلیدی (KPI) در حوزه‌های سیاسی، اقتصادی، اجتماعی و محیط‌زیستی.', 'color': '#1A237E', 'hero': True}
        ]
    },
    {
        'filename': 'ch15_slide2.svg',
        'chapter': 'فصل ۱۵: پایش، ارزیابی و مدیریت ریسک',
        'title': 'شفافیت: زره پولادین دموکراسی',
        'blocks': [
            {'label': 'اصل نظارت', 'text': 'آنچه شفاف نباشد، مستعد فساد است. گزارش‌دهی مستقیم و سه‌ماهه به مردم، بازگرداندن نظارت به صاحبان اصلی قدرت است.', 'color': '#263238', 'hero': True},
            {'label': 'داده‌های باز', 'text': 'دسترسی آزاد تمام شهروندان به داده‌های دولتی (Open Data) برای نظارت همگانی و مشارکت فعال مدنی.', 'color': '#2E7D32'}
        ]
    },
    {
        'filename': 'ch15_slide3.svg',
        'chapter': 'فصل ۱۵: پایش، ارزیابی و مدیریت ریسک',
        'title': 'اهداف سنجش‌پذیر بالندگی ملی',
        'blocks': [
            {'label': 'نقشه راه عددی', 'text': 'ارتقای شاخص دموکراسی (EIU) از ۲.۲ به بالای ۸ و کاهش تورم به زیر ۵٪ در افق ربع قرن گذار ملی.', 'color': '#263238'},
            {'label': 'توسعه انسانی', 'text': 'هدف‌گذاری برای رسیدن به کیفیت زندگی در سطح استانداردهای جهانی و ایجاد فرصت‌های برابر برای تمام ایرانیان.', 'color': '#1B5E20', 'hero': True}
        ]
    },
    {
        'filename': 'ch15_slide4.svg',
        'chapter': 'فصل ۱۵: پایش، ارزیابی و مدیریت ریسک',
        'title': 'مدیریت ریسک و تاب‌آوری ملی',
        'blocks': [
            {'label': 'پیش‌بینی انحراف', 'text': 'شناسایی زودهنگام ریسک‌های گذار نظیر بازگشت پوپولیسم یا فشارهای اقتصادی و طراحی مکانیزم‌های اصلاح مسیر.', 'color': '#263238'},
            {'label': 'هشدار زودهنگام', 'text': 'دموکراسی پایدار نیازمند چشمان بیدار شهروندان و نهادهای نظارتی مستقل برای شناسایی کوچک‌ترین تهدیدات است.', 'color': '#BF360C', 'hero': True}
        ]
    },
    {
        'filename': 'ch15_slide5.svg',
        'chapter': 'فصل ۱۵: پایش، ارزیابی و مدیریت ریسک',
        'title': 'فرجام گذار: تعهد به آینده',
        'blocks': [
            {'label': 'پیام نهایی', 'text': 'پایش و ارزیابی، پایان مسیر نیست، بلکه آغاز فرهنگ مسئولیت‌پذیری در ایران نوین است. ما به ساختن ایرانی پایدار متعهدیم.', 'color': '#263238'},
            {'label': 'ایران فردا', 'text': 'دموکراسی زمانی بیمه می‌شود که نظارت شهروندی به یک عادت ملی تبدیل شود. ایرانی آزاد، برای همیشه.', 'color': '#F9A825', 'hero': True}
        ]
    }
]

for slide in slides_data_ch15:
    create_svg(slide['filename'], slide['chapter'], slide['title'], slide['blocks'])
