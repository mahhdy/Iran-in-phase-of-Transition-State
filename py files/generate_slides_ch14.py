import os

output_dir = r'd:\Code\Books\Transition for Iran\00- Iran in phase of Transition State\images\slides'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def create_svg(filename, chapter_title, slide_title, content_blocks):
    svg_start = f'''<svg width="1080" height="1350" viewBox="0 0 1080 1350" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="headerGrad" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" style="stop-color:#388E3C;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#1B5E20;stop-opacity:1" />
        </linearGradient>
    </defs>
    <rect width="1080" height="1350" fill="#F1F8E9" opacity="0.4" />
    <rect width="1080" height="1350" fill="white" />
    
    <rect width="1080" height="120" fill="#1B5E20" />
    <foreignObject x="40" y="35" width="1000" height="60">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn', sans-serif; color: white; font-size: 34px; font-weight: bold;">
            {chapter_title}
        </div>
    </foreignObject>
    
    <foreignObject x="60" y="160" width="960" height="140">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn', sans-serif; color: #1B5E20; font-size: 50px; font-weight: 900; line-height: 1.3;">
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
        color = block.get('color', '#1B5E20')
        is_hero = block.get('hero', False)
        
        text_len = len(text)
        height = 190
        if is_hero: height = 280
        if text_len > 120: height += 60
        if text_len > 220: height += 80
        
        card = f'''
        <rect y="{y_offset}" width="960" height="{height}" rx="28" fill="white" style="filter: drop-shadow(0 12px 24px rgba(27,94,32,0.12));" />
        <rect x="940" y="{y_offset + 30}" width="16" height="{height - 60}" rx="8" fill="{color}" />
        
        <foreignObject x="50" y="{y_offset + 35}" width="860" height="{height - 70}">
            <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn', sans-serif;">
                <div style="color: {color}; font-size: 26px; font-weight: 800; margin-bottom: 20px; font-variant: small-caps;">{label}</div>
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
    
    <text x="540" y="1310" text-anchor="middle" font-family="'Vazirmatn', sans-serif" font-size="22" font-weight="bold" fill="#1B5E20">صداقت با زمین، امنیت ملی ماست • ۲۰۲۶</text>
    </svg>
    '''
    
    full_svg = svg_start + cards_svg + svg_end
    
    full_path = os.path.join(output_dir, filename)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(full_svg)
    print(f"Generated: {full_path}")

# Chapter 14 Slides Data
slides_data_ch14 = [
    {
        'filename': 'ch14_slide1.svg',
        'chapter': 'فصل ۱۴: بحران آب و محیط زیست',
        'title': 'بحران آب: تهدید موجودیت تمدنی',
        'blocks': [
            {'label': 'تبیین وضعیت', 'text': 'بحران آب تنها یک مسئله فنی نیست؛ یک بحران امنیت ملی است که بقای تمدن چند هزار ساله ایران را به مخاطره انداخته است.', 'color': '#1B5E20'},
            {'label': 'واقعیت تکان‌دهنده', 'text': 'کسری سالانه ۱۵-۲۰ میلیارد مترمکعب آب زیرزمینی و فرونشست ۳۶ سانتی‌متری زمین در پایتخت؛ زنگ خطر فروپاشی کالبدی.', 'color': '#B71C1C', 'hero': True}
        ]
    },
    {
        'filename': 'ch14_slide2.svg',
        'chapter': 'فصل ۱۴: بحران آب و محیط زیست',
        'title': 'مرگ دشت‌ها و فرونشست زمین',
        'blocks': [
            {'label': 'فاجعه خاموش', 'text': 'فرونشست زمین در ۳۵۰ دشت ایران؛ پدیده‌ای برگشت‌ناپذیر که زیرساخت‌ها، راه‌آهن و میراث باستانی ما را می‌بلعد.', 'color': '#1B5E20', 'hero': True},
            {'label': 'علت اصلی', 'text': 'استخراج بی‌رویه آب‌های زیرزمینی برای کشاورزی سنتی که بیش از ۹۲٪ کل منابع آب قابل استحصال کشور را می‌بلعد.', 'color': '#E65100'}
        ]
    },
    {
        'filename': 'ch14_slide3.svg',
        'chapter': 'فصل ۱۴: بحران آب و محیط زیست',
        'title': 'ارومیه و هامون: مرثیه‌ای برای حیات',
        'blocks': [
            {'label': 'نابودی تالاب‌ها', 'text': 'خشک‌شدن ۸۰٪ دریاچه ارومیه و مرگ کامل هامون و بختگان؛ آغاز عصر طوفان‌های نمک و تهدید سلامت میلیون‌ها ایرانی.', 'color': '#1B5E20'},
            {'label': 'اولتیماتوم ملی', 'text': 'احیای ارومیه و تالاب‌ها نماد اراده مدیریت دموکراتیک برای بازگرداندن توازن به زیست‌بوم ایران و تأمین امنیت غذایی است.', 'color': '#1976D2', 'hero': True}
        ]
    },
    {
        'filename': 'ch14_slide4.svg',
        'chapter': 'فصل ۱۴: بحران آب و محیط زیست',
        'title': 'راهبرد نجات: حکمرانی نوین آب',
        'blocks': [
            {'label': 'مدیریت تقاضا', 'text': 'کاهش ۴۰٪ مصرف در بخش کشاورزی و انتقال به الگوی کشت نوین مبتنی بر آمایش سرزمین و دانش جهانی.', 'color': '#1B5E20'},
            {'label': 'عرضه پایدار', 'text': 'سرمایه‌گذاری روی شیرین‌سازی آب دریا برای جنوب و بازچرخانی ۱۰۰٪ فاضلاب شهری برای صنایع و فضای سبز.', 'color': '#2E7D32', 'hero': True}
        ]
    },
    {
        'filename': 'ch14_slide5.svg',
        'chapter': 'فصل ۱۴: بحران آب و محیط زیست',
        'title': 'حق نفس پاک برای نسل‌های آینده',
        'blocks': [
            {'label': 'اقتصاد سبز', 'text': 'گذار به انرژی‌های پاک و مبارزه جدی با آلودگی هوای کلان‌شهرها برای پایان دادن به خفگی تدریجی ساکنان شهرهای بزرگ.', 'color': '#1B5E20'},
            {'label': 'تعهد ملی', 'text': 'نجات محیط زیست، نجات ایران است. میراثی سبز و پایدار؛ این تنها قولی است که باید به آیندگان وفا کنیم.', 'color': '#F9A825', 'hero': True}
        ]
    }
]

for slide in slides_data_ch14:
    create_svg(slide['filename'], slide['chapter'], slide['title'], slide['blocks'])
