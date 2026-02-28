import os

output_dir = r'd:\Code\Books\Transition for Iran\00- Iran in phase of Transition State\images\slides'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def create_svg(filename, chapter_title, slide_title, content_blocks):
    svg_start = f'''<svg width="1080" height="1350" viewBox="0 0 1080 1350" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="headerGrad" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" style="stop-color:#FFD600;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#F9A825;stop-opacity:1" />
        </linearGradient>
    </defs>
    <rect width="1080" height="1350" fill="#FFFDE7" opacity="0.5" />
    <rect width="1080" height="1350" fill="white" />
    
    <rect width="1080" height="120" fill="#F9A825" />
    <foreignObject x="40" y="35" width="1000" height="60">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn', sans-serif; color: #1A237E; font-size: 34px; font-weight: bold;">
            {chapter_title}
        </div>
    </foreignObject>
    
    <foreignObject x="60" y="160" width="960" height="140">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn', sans-serif; color: #1A237E; font-size: 50px; font-weight: 900; line-height: 1.3;">
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
        color = block.get('color', '#F9A825')
        is_hero = block.get('hero', False)
        
        text_len = len(text)
        height = 190
        if is_hero: height = 280
        if text_len > 120: height += 60
        if text_len > 220: height += 80
        
        card = f'''
        <rect y="{y_offset}" width="960" height="{height}" rx="28" fill="white" style="filter: drop-shadow(0 12px 24px rgba(249,168,37,0.12));" />
        <rect x="940" y="{y_offset}" width="20" height="{height}" rx="10" fill="{color}" />
        
        <foreignObject x="50" y="{y_offset + 35}" width="860" height="{height - 70}">
            <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn', sans-serif;">
                <div style="color: {color}; font-size: 26px; font-weight: 800; margin-bottom: 20px; font-style: italic;">{label}</div>
                <div style="color: #1A237E; font-size: { '44px' if is_hero else '32px' }; font-weight: { '900' if is_hero else '500' }; line-height: 1.6;">
                    {text}
                </div>
            </div>
        </foreignObject>
        '''
        cards_svg += card
        y_offset += height + 40
        
    svg_end = f'''
    </g>
    
    <text x="540" y="1310" text-anchor="middle" font-family="'Vazirmatn', sans-serif" font-size="22" font-weight="bold" fill="#F9A825">ایران ۱۴۲۹: افق روشنایی</text>
    </svg>
    '''
    
    full_svg = svg_start + cards_svg + svg_end
    
    full_path = os.path.join(output_dir, filename)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(full_svg)
    print(f"Generated: {full_path}")

# Chapter 7 Slides Data
slides_data_ch07 = [
    {
        'filename': 'ch07_slide1.svg',
        'chapter': 'فصل ۷: چشم‌انداز و اصول راهنما',
        'title': 'ترسیم مقصد: ایران ۱۴۲۹',
        'blocks': [
            {'label': 'فلسفه چشم‌انداز', 'text': 'گذار دموکراتیک بدون مقصدی روشن، سفری در تاریکی است. ایران ۱۴۲۹ تصویری از ایرانی مرفه و دموکراتیک در افق ۲۵ ساله است.', 'color': '#1A237E'},
            {'label': 'ارکان اصلی', 'text': 'حاکمیت کامل ملی، عدالت توزیعی، و احیای محیط‌زیست؛ ستون‌های ایران نوین در افق پیش‌رو.', 'color': '#F9A825', 'hero': True}
        ]
    },
    {
        'filename': 'ch07_slide2.svg',
        'chapter': 'فصل ۷: چشم‌انداز و اصول راهنما',
        'title': 'بیانیه چشم‌انداز: میثاق فردا',
        'blocks': [
            {'label': 'تعهد ملی', 'text': '«هر شهروند ایرانی فارغ از قومیت، جنسیت و باور، از حقوق برابر برخوردار است و حکومت پاسخگو و شفاف خواهد بود.»', 'color': '#1A237E', 'hero': True},
            {'label': 'جایگاه جهانی', 'text': 'ایران در ۱۴۲۹، عضو محترم جامعه جهانی و الگوی توسعه صلح‌آمیز در منطقه خواهد بود.', 'color': '#2E7D32'}
        ]
    },
    {
        'filename': 'ch07_slide3.svg',
        'chapter': 'فصل ۷: چشم‌انداز و اصول راهنما',
        'title': 'ده اصل بنیادین نظام نوین',
        'blocks': [
            {'label': 'ستون‌های تغییر', 'text': 'اصولی چون حاکمیت ملی، کثرت‌گرایی، تفکیک قوا و عدالت انتقالی؛ سنگ‌بنای غیرقابل‌تغییر قانون اساسی نوین.', 'color': '#1A237E'},
            {'label': 'خط قرمز', 'text': 'نفی هرگونه مطلقه بودن قدرت؛ حاکمیت منحصراً از آنِ مردم و برآمده از صندوق رأی آزاد است.', 'color': '#B71C1C', 'hero': True}
        ]
    },
    {
        'filename': 'ch07_slide4.svg',
        'chapter': 'فصل ۷: چشم‌انداز و اصول راهنما',
        'title': 'مدیریت تنوع: ایران برای همه',
        'blocks': [
            {'label': 'گنجینه ملی', 'text': 'تنوع قومی و فرهنگی ثروت ماست. مدیریت تکثر از طریق فدرالیسم همبسته و خودمدیریت محلی اقوام.', 'color': '#1A237E'},
            {'label': 'بیانیه حقوق', 'text': 'تضمین حقوق برابر برای آذری، کرد، لر، عرب، بلوچ، ترکمن و همه هویت‌های ایرانی زیر سقف میهن.', 'color': '#2E7D32', 'hero': True}
        ]
    },
    {
        'filename': 'ch07_slide5.svg',
        'chapter': 'فصل ۷: چشم‌انداز و اصول راهنما',
        'title': 'شاخص‌های بالندگی ۱۴۲۹',
        'blocks': [
            {'label': 'اهداف سنجش‌پذیر', 'text': 'ارتقای شاخص دموکراسی به بالای ۷، کاهش سهم نفت در اقتصاد به زیر ۲۰٪ و احیای کامل منابع آب زیرزمینی.', 'color': '#1A237E'},
            {'label': 'آغاز سفر', 'text': 'گذار ممکن است؛ اگر با ایمانی راسخ به تغییر و برنامه‌ای دانش‌بنیان، از همین امروز آغاز کنیم.', 'color': '#F9A825', 'hero': True}
        ]
    }
]

for slide in slides_data_ch07:
    create_svg(slide['filename'], slide['chapter'], slide['title'], slide['blocks'])
