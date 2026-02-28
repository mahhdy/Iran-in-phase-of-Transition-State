import os

output_dir = r'd:\Code\Books\Transition for Iran\00- Iran in phase of Transition State\images\slides'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def create_svg(filename, chapter_title, slide_title, content_blocks):
    svg_start = f'''<svg width="1080" height="1350" viewBox="0 0 1080 1350" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="headerGrad" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" style="stop-color:#00796B;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#004D40;stop-opacity:1" />
        </linearGradient>
    </defs>
    <rect width="1080" height="1350" fill="#E0F2F1" opacity="0.4" />
    <rect width="1080" height="1350" fill="white" />
    
    <rect width="1080" height="120" fill="#00796B" />
    <foreignObject x="40" y="35" width="1000" height="60">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn', sans-serif; color: white; font-size: 34px; font-weight: bold;">
            {chapter_title}
        </div>
    </foreignObject>
    
    <foreignObject x="60" y="160" width="960" height="140">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn', sans-serif; color: #004D40; font-size: 50px; font-weight: 900; line-height: 1.3;">
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
        color = block.get('color', '#00796B')
        is_hero = block.get('hero', False)
        
        text_len = len(text)
        height = 190
        if is_hero: height = 280
        if text_len > 120: height += 60
        if text_len > 220: height += 80
        
        card = f'''
        <rect y="{y_offset}" width="960" height="{height}" rx="28" fill="white" style="filter: drop-shadow(0 12px 24px rgba(0,121,107,0.1));" />
        <circle cx="920" cy="{y_offset + 50}" r="15" fill="{color}" />
        
        <foreignObject x="50" y="{y_offset + 35}" width="850" height="{height - 70}">
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
    
    <text x="540" y="1310" text-anchor="middle" font-family="'Vazirmatn', sans-serif" font-size="22" font-weight="bold" fill="#00796B" opacity="0.3">طرح جامع مدیریت منابع حیاتی • ۲۰۲۶</text>
    </svg>
    '''
    
    full_svg = svg_start + cards_svg + svg_end
    
    full_path = os.path.join(output_dir, filename)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(full_svg)
    print(f"Generated: {full_path}")

# Chapter 6 Slides Data
slides_data_ch06 = [
    {
        'filename': 'ch06_slide1.svg',
        'chapter': 'فصل ۶: درس‌های مدیریت آب',
        'title': 'بحران آب ایران: بن‌بستی که راه دارد',
        'blocks': [
            {'label': 'تبیین مسئله', 'text': '۷۰٪ سفره‌های زیرزمینی ایران در وضعیت بحرانی است؛ اما تجارب جهانی نشان می‌دهد که با تغییر پارادایم می‌توان از این فروپاشی جلوگیری کرد.', 'color': '#00796B'},
            {'label': 'اولویت راهبردی', 'text': 'مدیریت تقاضا و ارتقای بهره‌وری در کشاورزی، بسیار حیاتی‌تر و پایدارتر از پروژه‌های بزرگ انتقال آب است.', 'color': '#F9A825', 'hero': True}
        ]
    },
    {
        'filename': 'ch06_slide2.svg',
        'chapter': 'فصل ۶: درس‌های مدیریت آب',
        'title': 'اسرائیل: معجزه در بیابان',
        'blocks': [
            {'label': 'فناوری‌های تحول‌آفرین', 'text': 'اسرائیل با بازچرخانی ۸۷٪ فاضلاب و ابداع آبیاری قطره‌ای، از کمبود مطلق به مازاد آب و صادرات محصول رسید.', 'color': '#00796B'},
            {'label': 'یافته کلیدی', 'text': 'شیرین‌سازی آب دریا امروزه ۷۰٪ آب شرب اسرائیل را تأمین می‌کند؛ مدلی که در جنوب ایران نیز قابل تحقق است.', 'color': '#2E7D32', 'hero': True}
        ]
    },
    {
        'filename': 'ch06_slide3.svg',
        'chapter': 'فصل ۶: درس‌های مدیریت آب',
        'title': 'سنگاپور: امنیت در قطره‌های آب',
        'blocks': [
            {'label': 'استراتژی چهار شیر', 'text': 'سنگاپور با تنوع‌بخشی به منابع و استفاده از فناوری اسمز معکوس (NEWater)، وابستگی خود را به خارج قطع کرد.', 'color': '#00796B'},
            {'label': 'درس فرهنگی', 'text': 'آموزش عمومی و شفافیت در کیفیت آب بازچرخانی‌شده، کلید پذیرش آن در سبد مصرفی جامعه بود.', 'color': '#1A237E'}
        ]
    },
    {
        'filename': 'ch06_slide4.svg',
        'chapter': 'فصل ۶: درس‌های مدیریت آب',
        'title': 'بازارهای آب و توازن زیستی',
        'blocks': [
            {'label': 'الگوی استرالیا', 'text': 'تخصیص آب بر اساس ارزش اقتصادی و زیست‌محیطی در استرالیا، از هدررفت منابع در دوره‌های خشکسالی طولانی جلوگیری کرد.', 'color': '#00796B'},
            {'label': 'اصلاح قیمت‌گذاری', 'text': 'آب ارزان نیست؛ قیمت‌گذاری واقعی قوی‌ترین محرک برای اصلاح الگوی کشت و صرفه‌جویی است.', 'color': '#B71C1C', 'hero': True}
        ]
    },
    {
        'filename': 'ch06_slide5.svg',
        'chapter': 'فصل ۶: درس‌های مدیریت آب',
        'title': 'برنامه اقدام برای نجات ایران',
        'blocks': [
            {'label': 'گام‌های نخست', 'text': 'نصب کنتورهای هوشمند، بازچرخانی فاضلاب در شهرهای بزرگ و توسعه شیرین‌سازی در سواحل مکران و خلیج‌فارس.', 'color': '#00796B'},
            {'label': 'پیام نهایی', 'text': 'نجات آب، نجات ایران است. با اراده سیاسی و بهره‌گیری از دانش جهانی، گذار به پایداری ممکن است.', 'color': '#F9A825', 'hero': True}
        ]
    }
]

for slide in slides_data_ch06:
    create_svg(slide['filename'], slide['chapter'], slide['title'], slide['blocks'])
