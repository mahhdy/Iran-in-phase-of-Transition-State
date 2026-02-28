import os

output_dir = r'd:\Code\Books\Transition for Iran\00- Iran in phase of Transition State\images\slides'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def create_svg(filename, chapter_title, slide_title, content_blocks):
    svg_start = f'''<svg width="1080" height="1350" viewBox="0 0 1080 1350" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="headerGrad" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" style="stop-color:#1A237E;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#283593;stop-opacity:1" />
        </linearGradient>
    </defs>
    <rect width="1080" height="1350" fill="#F0F2F5" />
    
    <rect width="1080" height="120" fill="url(#headerGrad)" />
    <foreignObject x="40" y="35" width="1000" height="60">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn', sans-serif; color: white; font-size: 34px; font-weight: bold;">
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
        color = block.get('color', '#1A237E')
        is_hero = block.get('hero', False)
        
        text_len = len(text)
        height = 190
        if is_hero: height = 280
        if text_len > 120: height += 60
        if text_len > 220: height += 80
        
        card = f'''
        <rect y="{y_offset}" width="960" height="{height}" rx="28" fill="white" style="filter: drop-shadow(0 12px 24px rgba(0,0,0,0.07));" />
        <rect x="940" y="{y_offset + 30}" width="10" height="{height - 60}" rx="5" fill="{color}" />
        
        <foreignObject x="50" y="{y_offset + 35}" width="860" height="{height - 70}">
            <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn', sans-serif;">
                <div style="color: {color}; font-size: 26px; font-weight: 800; margin-bottom: 20px;">{label}</div>
                <div style="color: #2D3436; font-size: { '42px' if is_hero else '32px' }; font-weight: { '900' if is_hero else '500' }; line-height: 1.6;">
                    {text}
                </div>
            </div>
        </foreignObject>
        '''
        cards_svg += card
        y_offset += height + 40
        
    svg_end = f'''
    </g>
    
    <text x="540" y="1310" text-anchor="middle" font-family="'Vazirmatn', sans-serif" font-size="22" font-weight="bold" fill="#BDBDBD">ایران در مسیر بالندگی • ۲۰۲۶</text>
    </svg>
    '''
    
    full_svg = svg_start + cards_svg + svg_end
    
    full_path = os.path.join(output_dir, filename)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(full_svg)
    print(f"Generated: {full_path}")

# Chapter 4 Slides Data
slides_data_ch04 = [
    {
        'filename': 'ch04_slide1.svg',
        'chapter': 'فصل ۴: درس‌های گذارهای موفق',
        'title': 'الگوهای جهانی موفقیت در گذار',
        'blocks': [
            {'label': 'یافته آماری', 'text': 'کشورهای اسپانیا، آفریقای جنوبی، اندونزی و کره جنوبی توانستند از تله‌های مشابه ایران عبور کنند.', 'color': '#1A237E'},
            {'label': 'شاه‌کلید موفقیت', 'text': 'تشکیل «ائتلاف بزرگ» بین اصلاح‌طلبان درون نظام و اپوزیسیون معتدل بیشترین نرخ پایداری را داشته است.', 'color': '#2E7D32', 'hero': True}
        ]
    },
    {
        'filename': 'ch04_slide2.svg',
        'chapter': 'فصل ۴: درس‌های گذارهای موفق',
        'title': 'اسپانیا: معجزه میثاق ملی',
        'blocks': [
            {'label': 'توافق مونکلوا', 'text': 'یک میثاق اقتصادی-سیاسی که در آن همه طرف‌ها برای ثبات کشور از بخشی از خواسته‌های خود گذشتند.', 'color': '#1A237E'},
            {'label': 'درس راهبردی', 'text': 'گذار موفق یک بازی با مجموع صفر نیست؛ بلکه توافقی است که در آن کسی بازنده مطلق نمی‌شود.', 'color': '#F9A825', 'hero': True}
        ]
    },
    {
        'filename': 'ch04_slide3.svg',
        'chapter': 'فصل ۴: درس‌های گذارهای موفق',
        'title': 'آفریقای جنوبی: آشتی بجای انتقام',
        'blocks': [
            {'label': 'عدالت انتقالی', 'text': 'مدل «حقیقت و آشتی» نشان داد که اعتراف به اشتباهات گذشته می‌تواند راه را برای آینده‌ای مشترک باز کند.', 'color': '#1A237E'},
            {'label': 'دستاورد تمدنی', 'text': 'جایگزینی انتقام‌جویی با عدالت ترمیمی، از فروپاشی اجتماعی و جنگ داخلی جلوگیری کرد.', 'color': '#B71C1C', 'hero': True}
        ]
    },
    {
        'filename': 'ch04_slide4.svg',
        'chapter': 'فصل ۴: درس‌های گذارهای موفق',
        'title': 'اندونزی و کره جنوبی: نهادسازی',
        'blocks': [
            {'label': 'مسیر بالندگی', 'text': 'این دو کشور نشان دادند که دموکراسی و رشد اقتصادی می‌توانند در یک چرخه فاضل یکدیگر را تقویت کنند.', 'color': '#1A237E'},
            {'label': 'تحکیم نهادی', 'text': 'ایجاد نهادهای مستقل نظارتی و حاکمیت قانون، ثبات بلندمدت را پس از دوره‌های بحرانی تضمین کرد.', 'color': '#2E7D32'}
        ]
    },
    {
        'filename': 'ch04_slide5.svg',
        'chapter': 'فصل ۴: درس‌های گذارهای موفق',
        'title': 'درس‌های کلیدی برای ایران امروز',
        'blocks': [
            {'label': 'پیشنهاد نهایی', 'text': 'نیاز به مرجعیت ملی میانجی، رسمیت دادن به تنوع قومی و تمرکز بر آبادانی اقتصادی ملموس.', 'color': '#1A237E'},
            {'label': 'پیام امید', 'text': 'گذار یک علم است؛ با یادگیری از تجارب جهانی و طراحی بومی، می‌توانیم از بن‌بست کنونی عبور کنیم.', 'color': '#F9A825', 'hero': True}
        ]
    }
]

for slide in slides_data_ch04:
    create_svg(slide['filename'], slide['chapter'], slide['title'], slide['blocks'])
