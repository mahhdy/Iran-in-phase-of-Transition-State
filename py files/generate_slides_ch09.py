import os

output_dir = r'd:\Code\Books\Transition for Iran\00- Iran in phase of Transition State\images\slides'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def create_svg(filename, chapter_title, slide_title, content_blocks):
    svg_start = f'''<svg width="1080" height="1350" viewBox="0 0 1080 1350" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="headerGrad" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" style="stop-color:#4527A0;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#311B92;stop-opacity:1" />
        </linearGradient>
    </defs>
    <rect width="1080" height="1350" fill="#EDE7F6" opacity="0.3" />
    <rect width="1080" height="1350" fill="white" />
    
    <rect width="1080" height="120" fill="#4527A0" />
    <foreignObject x="40" y="35" width="1000" height="60">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn', sans-serif; color: white; font-size: 34px; font-weight: bold;">
            {chapter_title}
        </div>
    </foreignObject>
    
    <foreignObject x="60" y="160" width="960" height="140">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn', sans-serif; color: #311B92; font-size: 50px; font-weight: 900; line-height: 1.3;">
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
        color = block.get('color', '#4527A0')
        is_hero = block.get('hero', False)
        
        text_len = len(text)
        height = 190
        if is_hero: height = 280
        if text_len > 120: height += 60
        if text_len > 220: height += 80
        
        card = f'''
        <rect y="{y_offset}" width="960" height="{height}" rx="28" fill="white" style="filter: drop-shadow(0 12px 24px rgba(69,39,160,0.12));" />
        <rect x="0" y="{y_offset}" width="16" height="{height}" rx="8" fill="{color}" />
        
        <foreignObject x="50" y="{y_offset + 35}" width="860" height="{height - 70}">
            <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn', sans-serif;">
                <div style="color: {color}; font-size: 26px; font-weight: 800; margin-bottom: 20px;">{label}</div>
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
    
    <text x="540" y="1310" text-anchor="middle" font-family="'Vazirmatn', sans-serif" font-size="22" font-weight="bold" fill="#4527A0">استخوان‌بندی دموکراسی • ۲۰۲۶</text>
    </svg>
    '''
    
    full_svg = svg_start + cards_svg + svg_end
    
    full_path = os.path.join(output_dir, filename)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(full_svg)
    print(f"Generated: {full_path}")

# Chapter 9 Slides Data
slides_data_ch09 = [
    {
        'filename': 'ch09_slide1.svg',
        'chapter': 'فصل ۹: فاز ۲ — نهادسازی (سال ۳-۵)',
        'title': 'ساختن استخوان‌بندی دموکراسی',
        'blocks': [
            {'label': 'تبیین راهبرد', 'text': 'قانون اساسی کاغذی بیش نیست اگر نهادهایی برای اجرایش وجود نداشته باشد. فاز دوم به ساختن این ستون‌های پایدار اختصاص دارد.', 'color': '#4527A0'},
            {'label': 'اولویت‌های فاز ۲', 'text': 'استقلال کامل قوه قضائیه، استقرار فدرالیسم همبسته و بازسازی نظام آموزشی بر پایه ارزش‌های مدنی.', 'color': '#6200EA', 'hero': True}
        ]
    },
    {
        'filename': 'ch09_slide2.svg',
        'chapter': 'فصل ۹: فاز ۲ — نهادسازی (سال ۳-۵)',
        'title': 'فدرالیسم: پاسخ به تنوع ایرانی',
        'blocks': [
            {'label': 'الگوی پیشنهادی', 'text': 'توزیع قدرت در چهار سطح ملی، منطقه‌ای، استانی و محلی؛ پایانی بر فقر ناشی از تمرکزگرایی ۱۰۰ ساله.', 'color': '#4527A0'},
            {'label': 'پنج منطقه خودمختار', 'text': 'رسمیت دادن به تدریس زبان‌های مادری و خودمدیریت محلی در آذربایجان، کردستان، بلوچستان، و عربستان.', 'color': '#2E7D32', 'hero': True}
        ]
    },
    {
        'filename': 'ch09_slide3.svg',
        'chapter': 'فصل ۹: فاز ۲ — نهادسازی (سال ۳-۵)',
        'title': 'عدالت، نه انتقام: التیام ملی',
        'blocks': [
            {'label': 'عدالت انتقالی', 'text': 'کشف حقیقت و جبران خسارت‌های گذشته برای عبور از ترومای استبداد و رسیدن به آشتی عمیق ملی.', 'color': '#4527A0'},
            {'label': 'درس راهبردی', 'text': 'عدالت انتقالی متوازن، ضامن جلوگیری از تکرار گذشته و حرکت به سوی آینده‌ای مشترک برای همه ایرانیان است.', 'color': '#B71C1C', 'hero': True}
        ]
    },
    {
        'filename': 'ch09_slide4.svg',
        'chapter': 'فصل ۹: فاز ۲ — نهادسازی (سال ۳-۵)',
        'title': 'حاکمیت قانون و استقلال قضا',
        'blocks': [
            {'label': 'سنگر آزادی', 'text': 'استقرار دادگاه قانون اساسی و قوه قضائیه مستقل؛ جایی که حتی قدرتمندترین افراد هم در برابر قانون پاسخگو هستند.', 'color': '#4527A0'},
            {'label': 'اصلاح بوروکراسی', 'text': 'جایگزینی فساد و رانت با نظام اداری شایسته‌سالار و شفاف در خدمت تأمین منافع ملی.', 'color': '#2E7D32'}
        ]
    },
    {
        'filename': 'ch09_slide5.svg',
        'chapter': 'فصل ۹: فاز ۲ — نهادسازی (سال ۳-۵)',
        'title': 'جامعه مدنی: نگهبان دموکراسی',
        'blocks': [
            {'label': 'فرهنگ بالندگی', 'text': 'تقویت سندیکاها، نهادهای مدنی و رسانه‌های آزاد برای نظارت دائمی بر قدرت و جلوگیری از انحراف گذار.', 'color': '#4527A0'},
            {'label': 'پیام نهایی', 'text': 'نهادها، نگهبانان ابدی آزادی هستند. با ساختن نهادهایی استوار، دموکراسی ایران را برای همیشه بیمه می‌کنیم.', 'color': '#F9A825', 'hero': True}
        ]
    }
]

for slide in slides_data_ch09:
    create_svg(slide['filename'], slide['chapter'], slide['title'], slide['blocks'])
