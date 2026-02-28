import os

output_dir = r'd:\Code\Books\Transition for Iran\00- Iran in phase of Transition State\images\slides'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def create_svg(filename, chapter_title, slide_title, content_blocks):
    svg_start = f'''<svg width="1080" height="1350" viewBox="0 0 1080 1350" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="headerGrad" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" style="stop-color:#C62828;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#8E24AA;stop-opacity:1" />
        </linearGradient>
    </defs>
    <rect width="1080" height="1350" fill="#F8BBD0" opacity="0.2" />
    <rect width="1080" height="1350" fill="white" />
    
    <rect width="1080" height="120" fill="url(#headerGrad)" />
    <foreignObject x="40" y="35" width="1000" height="60">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn', sans-serif; color: white; font-size: 34px; font-weight: bold;">
            {chapter_title}
        </div>
    </foreignObject>
    
    <foreignObject x="60" y="160" width="960" height="140">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn', sans-serif; color: #880E4F; font-size: 50px; font-weight: 900; line-height: 1.3;">
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
        color = block.get('color', '#8E24AA')
        is_hero = block.get('hero', False)
        
        text_len = len(text)
        height = 190
        if is_hero: height = 280
        if text_len > 120: height += 60
        if text_len > 220: height += 80
        
        card = f'''
        <rect y="{y_offset}" width="960" height="{height}" rx="28" fill="white" style="filter: drop-shadow(0 12px 24px rgba(136,14,79,0.12));" />
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
    
    <text x="540" y="1310" text-anchor="middle" font-family="'Vazirmatn', sans-serif" font-size="22" font-weight="bold" fill="#880E4F">نقشه راه ایران نوین • ۲۰۲۶</text>
    </svg>
    '''
    
    full_svg = svg_start + cards_svg + svg_end
    
    full_path = os.path.join(output_dir, filename)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(full_svg)
    print(f"Generated: {full_path}")

# Executive Summary Slides Data
slides_data_ch00 = [
    {
        'filename': 'ch00_slide1.svg',
        'chapter': 'خلاصه مدیریتی: از بحران تا بالندگی',
        'title': 'نقشه راه ۲۵ ساله ایران نوین',
        'blocks': [
            {'label': 'تبیین راهبرد', 'text': 'گذار به دموکراسی پایدار، کارآمد و مرفه بر پایه اصل «آبادانی ملموس و فوری»؛ جایی که رفاه شهروندان ضامن بقای آزادی است.', 'color': '#C62828'},
            {'label': 'چشم‌انداز کلان', 'text': 'پایان عصر استبداد و انزوا؛ گذار ۵ مرحله‌ای برای بازسازی کالبدی، اقتصادی و اجتماعی ایران در ربع قرن آینده.', 'color': '#8E24AA', 'hero': True}
        ]
    },
    {
        'filename': 'ch00_slide2.svg',
        'chapter': 'خلاصه مدیریتی: از بحران تا بالندگی',
        'title': 'چشم‌انداز ایران ۱۴۳۰ (افق ۲۵ ساله)',
        'blocks': [
            {'label': 'رؤیای تحقق‌یافته', 'text': 'ایرانی با درآمد سرانه بالای ۱۵ هزار دلار، رشد ۵٪ پایدار، احیای نیمی از منابع آب و رتبه «آزاد» در شاخص‌های جهانی.', 'color': '#8E24AA', 'hero': True},
            {'label': 'جایگاه جهانی', 'text': 'الگوی منطقه‌ای دموکراسی، هاب فناوری خاورمیانه و عضو محترم و مؤثر در تمام نهادهای پیشرفته بین‌المللی.', 'color': '#2E7D32'}
        ]
    },
    {
        'filename': 'ch00_slide3.svg',
        'chapter': 'خلاصه مدیریتی: از بحران تا بالندگی',
        'title': 'پنج فاز گذار ملی',
        'blocks': [
            {'label': 'نقشه راه زمانی', 'text': '۱. گذار (۲ سال)، ۲. نهادسازی (۳ سال)، ۳. تحکیم (۵ سال)، ۴. بلوغ (۱۰ سال)، و ۵. تعالی (۵ سال).', 'color': '#8E24AA'},
            {'label': 'دستاورد نهایی', 'text': 'از تشکیل دولت موقت و تدوین قانون اساسی تا تبدیل شدن به قدرت اول اقتصادی و علمی منطقه با دموکراسی برگشت‌ناپذیر.', 'color': '#C62828', 'hero': True}
        ]
    },
    {
        'filename': 'ch00_slide4.svg',
        'chapter': 'خلاصه مدیریتی: از بحران تا بالندگی',
        'title': '۱۰۰ روز اول: پنجره فرصت طلایی',
        'blocks': [
            {'label': 'ده اقدام فوری', 'text': 'آزادی زندانیان سیاسی، آتش‌بس سیاسی، بسته حمایت معیشتی و آغاز مذاکرات برای رفع کامل تحریم‌های ویرانگر.', 'color': '#8E24AA', 'hero': True},
            {'label': 'اعتمادسازی', 'text': 'مردم باید تغییر را «ببینند» و «احساس کنند» تا از فرآیند گذار در برابر مخاطرات و بازگشت اقتدارگرایی محافظت کنند.', 'color': '#1A237E'}
        ]
    },
    {
        'filename': 'ch00_slide5.svg',
        'chapter': 'خلاصه مدیریتی: از بحران تا بالندگی',
        'title': 'چرخه فضیلت: ایران فردا',
        'blocks': [
            {'label': 'تحول بنیادین', 'text': 'جایگزینی چرخه باطل فقر و استبداد با چرخه فاضل رفاه، مشروعیت و ثبات؛ ریشه‌کنی فساد و مدیریت هوشمند تنوع.', 'color': '#8E24AA'},
            {'label': 'پیام امید', 'text': 'ایمان به تغییر، اراده برای ساختن؛ دموکراسی نه یک رؤیا، بلکه تنها مسیر ممکن برای سربلندی ملت ایران است.', 'color': '#C62828', 'hero': True}
        ]
    }
]

for slide in slides_data_ch00:
    create_svg(slide['filename'], slide['chapter'], slide['title'], slide['blocks'])
