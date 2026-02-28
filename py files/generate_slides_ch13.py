import os

output_dir = r'd:\Code\Books\Transition for Iran\00- Iran in phase of Transition State\images\slides'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def create_svg(filename, chapter_title, slide_title, content_blocks):
    svg_start = f'''<svg width="1080" height="1350" viewBox="0 0 1080 1350" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="headerGrad" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" style="stop-color:#004D40;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#00695C;stop-opacity:1" />
        </linearGradient>
    </defs>
    <rect width="1080" height="1350" fill="#E0F2F1" opacity="0.3" />
    <rect width="1080" height="1350" fill="white" />
    
    <rect width="1080" height="120" fill="#00695C" />
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
        color = block.get('color', '#00695C')
        is_hero = block.get('hero', False)
        
        text_len = len(text)
        height = 190
        if is_hero: height = 280
        if text_len > 120: height += 60
        if text_len > 220: height += 80
        
        card = f'''
        <rect y="{y_offset}" width="960" height="{height}" rx="28" fill="white" style="filter: drop-shadow(0 12px 24px rgba(0,105,92,0.12));" />
        <rect x="0" y="{y_offset + 30}" width="16" height="{height - 60}" rx="8" fill="{color}" />
        
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
    
    <text x="540" y="1310" text-anchor="middle" font-family="'Vazirmatn', sans-serif" font-size="22" font-weight="bold" fill="#00695C">اقتصاد سالم، دموکراسی پایدار • ۲۰۲۶</text>
    </svg>
    '''
    
    full_svg = svg_start + cards_svg + svg_end
    
    full_path = os.path.join(output_dir, filename)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(full_svg)
    print(f"Generated: {full_path}")

# Chapter 13 Slides Data
slides_data_ch13 = [
    {
        'filename': 'ch13_slide1.svg',
        'chapter': 'فصل ۱۳: بازسازی اقتصادی و رهایی از تحریم',
        'title': 'اقتصاد سالم: سنگر دفاع از آزادی',
        'blocks': [
            {'label': 'تبیین راهبرد', 'text': 'دموکراسی بدون رفاه اقتصادی شکننده است. هدف ما «آبادانی ملموس» است تا مردم بهبود را در زندگی روزمره حس کنند.', 'color': '#00695C'},
            {'label': 'اولویت اول', 'text': 'تثبیت اقتصاد کلان، مهار تورم ناشی از انزوا و بازگشت به بازارهای جهانی برای شکوفایی پتانسیل‌های پنهان ایران.', 'color': '#2E7D32', 'hero': True}
        ]
    },
    {
        'filename': 'ch13_slide2.svg',
        'chapter': 'فصل ۱۳: بازسازی اقتصادی و رهایی از تحریم',
        'title': 'رهایی از زنجیر تحریم‌ها',
        'blocks': [
            {'label': 'واقعیت تلخ', 'text': 'تحریم‌های ۳۸۰۰ گانه عامل اصلی قطع ارتباط با سیستم مالی جهانی و سقوط ارزش پول ملی در دهه‌های اخیر بوده است.', 'color': '#B71C1C', 'hero': True},
            {'label': 'گام نخست', 'text': 'رفع کامل تحریم‌ها از طریق دیپلماسی فعال و بازگشت به چرخه تجارت بین‌الملل برای جذب سرمایه‌های عظیم خارجی.', 'color': '#1A237E'}
        ]
    },
    {
        'filename': 'ch13_slide3.svg',
        'chapter': 'فصل ۱۳: بازسازی اقتصادی و رهایی از تحریم',
        'title': 'گذار به اقتصاد دانش‌بنیان',
        'blocks': [
            {'label': 'تحول ساختاری', 'text': 'پایان وابستگی به نفت و گذار به اقتصادی متنوع، فناورانه و رقابتی با تکیه بر نیروی انسانی نخبه و جوان ایران.', 'color': '#00695C'},
            {'label': 'اصلاح بوروکراسی', 'text': 'خصوصی‌سازی واقعی، اصلاح نظام بانکی ورشکسته و ریشه‌کنی فساد سیستماتیک برای ایجاد شفافیت و رقابت.', 'color': '#1B5E20', 'hero': True}
        ]
    },
    {
        'filename': 'ch13_slide4.svg',
        'chapter': 'فصل ۱۳: بازسازی اقتصادی و رهایی از تحریم',
        'title': 'عدالت توزیعی و رفاه فراگیر',
        'blocks': [
            {'label': 'توسعه متوازن', 'text': 'توزیع عادلانه ثروت و فرصت‌ها بین مرکز و پیرامون برای محو فقر و ایجاد امنیت اقتصادی برای تمام اقشار جامعه.', 'color': '#00695C'},
            {'label': 'شاخص موفقیت', 'text': 'کاهش ضریب جینی به زیر ۰.۳۲ و تضمین رشد پایدار بالای ۵٪ سالانه برای رسیدن به استانداردهای رفاه جهانی.', 'color': '#2E7D32', 'hero': True}
        ]
    },
    {
        'filename': 'ch13_slide5.svg',
        'chapter': 'فصل ۱۳: بازسازی اقتصادی و رهایی از تحریم',
        'title': 'ایران: هاب شکوفایی خاورمیانه',
        'blocks': [
            {'label': 'چشم‌انداز', 'text': 'تبدیل شدن به قدرت برتر اقتصادی منطقه با بهره‌گیری از موقعیت استراتژیک و برقراری پیوندهای عمیق تجاری با جهان.', 'color': '#00695C'},
            {'label': 'پیام نهایی', 'text': 'بازسازی اقتصاد، نگهبان آزادی ایران است. ایرانی آباد و مقتدر، تضمین‌کننده کرامت هر شهروند خواهد بود.', 'color': '#F9A825', 'hero': True}
        ]
    }
]

for slide in slides_data_ch13:
    create_svg(slide['filename'], slide['chapter'], slide['title'], slide['blocks'])
