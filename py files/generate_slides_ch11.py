import os

output_dir = r'd:\Code\Books\Transition for Iran\00- Iran in phase of Transition State\images\slides'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def create_svg(filename, chapter_title, slide_title, content_blocks):
    svg_start = f'''<svg width="1080" height="1350" viewBox="0 0 1080 1350" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="headerGrad" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" style="stop-color:#311B92;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#6200EA;stop-opacity:1" />
        </linearGradient>
    </defs>
    <rect width="1080" height="1350" fill="#F3E5F5" opacity="0.3" />
    <rect width="1080" height="1350" fill="white" />
    
    <rect width="1080" height="120" fill="#6200EA" />
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
        color = block.get('color', '#6200EA')
        is_hero = block.get('hero', False)
        
        text_len = len(text)
        height = 190
        if is_hero: height = 280
        if text_len > 120: height += 60
        if text_len > 220: height += 80
        
        card = f'''
        <rect y="{y_offset}" width="960" height="{height}" rx="28" fill="white" style="filter: drop-shadow(0 12px 24px rgba(98,0,234,0.12));" />
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
    
    <text x="540" y="1310" text-anchor="middle" font-family="'Vazirmatn', sans-serif" font-size="22" font-weight="bold" fill="#6200EA">میراث ما برای قرن پانزدهم • ۲۰۲۶</text>
    </svg>
    '''
    
    full_svg = svg_start + cards_svg + svg_end
    
    full_path = os.path.join(output_dir, filename)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(full_svg)
    print(f"Generated: {full_path}")

# Chapter 11 Slides Data
slides_data_ch11 = [
    {
        'filename': 'ch11_slide1.svg',
        'chapter': 'فصل ۱۱: فاز ۴ و ۵ — بلوغ و تعالی',
        'title': 'افق روشن کمال دموکراتیک',
        'blocks': [
            {'label': 'تبیین راهبرد', 'text': 'از «ساختن دموکراسی» به «زندگی آگاهانه در دموکراسی»؛ فازهای پایانی، دوران درونی‌سازی آزادی به عنوان یک عادت شهروندی است.', 'color': '#6200EA'},
            {'label': 'هدف نهایی', 'text': 'ایرانی آباد، آزاد و سربلند در جامعه جهانی با کیفیت زندگی هم‌تراز با توسعه‌یافته‌ترین کشورهای جهان.', 'color': '#2E7D32', 'hero': True}
        ]
    },
    {
        'filename': 'ch11_slide2.svg',
        'chapter': 'فصل ۱۱: فاز ۴ و ۵ — بلوغ و تعالی',
        'title': 'فاز ۴: بلوغ نهادی و فرهنگی',
        'blocks': [
            {'label': 'چشم‌انداز بلوغ', 'text': 'درونی‌سازی ارزش‌های دموکراتیک در فرهنگ عمومی و پختگی کامل نهادهای حاکمیتی در سال‌های ۱۱ تا ۱۵ گذار.', 'color': '#6200EA', 'hero': True},
            {'label': 'شاخص موفقیت', 'text': 'دموکراسی برگشت‌ناپذیر؛ زمانی که هیچ بازیگر بانفوذی دیگر به بازگشت استبداد به عنوان یک گزینه نمی‌اندیشد.', 'color': '#1A237E'}
        ]
    },
    {
        'filename': 'ch11_slide3.svg',
        'chapter': 'فصل ۱۱: فاز ۴ و ۵ — بلوغ و تعالی',
        'title': 'فاز ۵: تعالی و پیشتازی ملی',
        'blocks': [
            {'label': 'رؤیای تحقق‌یافته', 'text': 'ایران در سال‌های ۱۶ تا ۲۵ گذار، به هاب فناوری و گردشگری منطقه و الگوی گذار صلح‌آمیز در جهان تبدیل می‌شود.', 'color': '#6200EA'},
            {'label': 'دستاورد اقتصادی', 'text': 'گذار کامل به اقتصاد دانش‌بنیان و رسیدن به برابری فرصت‌ها و رفاه عادلانه برای تمام اقشار جامعه.', 'color': '#F9A825', 'hero': True}
        ]
    },
    {
        'filename': 'ch11_slide4.svg',
        'chapter': 'فصل ۱۱: فاز ۴ و ۵ — بلوغ و تعالی',
        'title': 'رهبری منطقه‌ای و صلح پایدار',
        'blocks': [
            {'label': 'دیپلماسی نوین', 'text': 'نقش‌آفرینی سازنده در ثبات خاورمیانه و هدایت همکاری‌های اقتصادی و محیط‌زیستی بین کشورهای همسایه.', 'color': '#6200EA'},
            {'label': 'امنیت درونی', 'text': 'تثبیت جایگاه ایران به عنوان عضو محترم جامعه بین‌الملل و رفع دائمی هرگونه تهدید موجودیتی علیه ملت.', 'color': '#2E7D32', 'hero': True}
        ]
    },
    {
        'filename': 'ch11_slide5.svg',
        'chapter': 'فصل ۱۱: فاز ۴ و ۵ — بلوغ و تعالی',
        'title': 'میراث برای نسل‌های آینده',
        'blocks': [
            {'label': 'پایان گذار', 'text': 'تحویل کشوری دموکراتیک، مرفه و سبز به آیندگان؛ دموکراسی نه یک مقصد، بلکه مسیری ابدی برای بالندگی است.', 'color': '#6200EA'},
            {'label': 'پیام نهایی', 'text': 'ایرانی آزاد برای همیشه؛ میراثی که با دانش، صبر و همبستگی ربع قرن برای آن کوشیدیم.', 'color': '#F9A825', 'hero': True}
        ]
    }
]

for slide in slides_data_ch11:
    create_svg(slide['filename'], slide['chapter'], slide['title'], slide['blocks'])
