import os

output_dir = r'd:\Code\Books\Transition for Iran\00- Iran in phase of Transition State\images\slides'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def create_svg(filename, chapter_title, slide_title, content_blocks):
    svg_start = f'''<svg width="1080" height="1350" viewBox="0 0 1080 1350" xmlns="http://www.w3.org/2000/svg">
    <!-- Background Gradient -->
    <defs>
        <linearGradient id="bgGrad" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" style="stop-color:#F5F5F7;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#E9E9EB;stop-opacity:1" />
        </linearGradient>
    </defs>
    <rect width="1080" height="1350" fill="url(#bgGrad)" />
    
    <!-- Top Bar -->
    <rect width="1080" height="100" fill="#1A237E" />
    <foreignObject x="40" y="20" width="1000" height="60">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn', sans-serif; color: #F9A825; font-size: 32px; font-weight: bold;">
            {chapter_title}
        </div>
    </foreignObject>
    
    <!-- Slide Title Section -->
    <foreignObject x="60" y="140" width="960" height="140">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn', sans-serif; color: #1A237E; font-size: 52px; font-weight: 900; line-height: 1.2;">
            {slide_title}
        </div>
    </foreignObject>
    
    <g transform="translate(60, 280)">
    '''
    
    y_offset = 0
    cards_svg = ""
    
    for block in content_blocks:
        label = block.get('label', '')
        text = block.get('text', '')
        color = block.get('color', '#1A237E')
        is_hero = block.get('hero', False)
        
        # Calculate dynamic height
        text_len = len(text)
        height = 180
        if is_hero: height = 260
        if text_len > 100: height += 60
        if text_len > 200: height += 80
        
        card = f'''
        <rect y="{y_offset}" width="960" height="{height}" rx="24" fill="white" style="filter: drop-shadow(0 8px 16px rgba(0,0,0,0.06));" />
        <path d="M 0 {y_offset + 24} Q 0 {y_offset} 24 {y_offset} L 40 {y_offset} L 40 {y_offset + height} L 24 {y_offset + height} Q 0 {y_offset + height} 0 {y_offset + height - 24} Z" fill="{color}" />
        
        <foreignObject x="60" y="{y_offset + 35}" width="860" height="{height - 70}">
            <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn', sans-serif;">
                <div style="color: {color}; font-size: 26px; font-weight: 800; margin-bottom: 20px; text-transform: uppercase; letter-spacing: 1px;">{label}</div>
                <div style="color: #2D3436; font-size: { '42px' if is_hero else '30px' }; font-weight: { '900' if is_hero else '500' }; line-height: 1.6;">
                    {text}
                </div>
            </div>
        </foreignObject>
        '''
        cards_svg += card
        y_offset += height + 40
        
    svg_end = f'''
    </g>
    
    <!-- Branding Footer -->
    <rect x="400" y="1290" width="280" height="40" rx="20" fill="#1A237E" opacity="0.1" />
    <text x="540" y="1318" text-anchor="middle" font-family="'Vazirmatn', sans-serif" font-size="22" font-weight="bold" fill="#1A237E">ایران در مرحله دولت گذار</text>
    </svg>
    '''
    
    full_svg = svg_start + cards_svg + svg_end
    
    full_path = os.path.join(output_dir, filename)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(full_svg)
    print(f"Generated: {full_path}")

# Chapter 3 Slides Data
slides_data_ch03 = [
    {
        'filename': 'ch03_slide1.svg',
        'chapter': 'فصل ۳: مبانی نظری',
        'title': 'لایه‌های دموکراسی: از صندوق تا فرهنگ',
        'blocks': [
            {'label': 'مفهوم بنیادین', 'text': 'دموکراسی صرفاً انتخابات نیست؛ یک نظام چندلایه شامل رعایت حقوق اقلیت‌ها، تفکیک قوا و فرهنگ مداراست.', 'color': '#1A237E'},
            {'label': 'هدف نهایی', 'text': 'تحکیم دموکراسی زمانی رخ می‌دهد که دموکراسی «تنها بازی در شهر» برای همه گروه‌ها باشد.', 'color': '#F9A825', 'hero': True}
        ]
    },
    {
        'filename': 'ch03_slide2.svg',
        'chapter': 'فصل ۳: مبانی نظری',
        'title': 'مدیریت تکثر: وحدت در کثرت',
        'blocks': [
            {'label': 'چالش اصلی', 'text': 'در جوامع متکثر، دموکراسی اکثریتی نباید به استبداد اکثریت بر اقلیت‌های قومی و مذهبی منجر شود.', 'color': '#1A237E'},
            {'label': 'مدل پیشنهادی', 'text': 'فدرالیسم نامتقارن ترکیبی از خودمختاری فرهنگی و یکپارچگی ملی بر پایه هویت مدنی.', 'color': '#2E7D32', 'hero': True}
        ]
    },
    {
        'filename': 'ch03_slide3.svg',
        'chapter': 'فصل ۳: مبانی نظری',
        'title': 'توسعه به‌مثابه آزادی (آمارتیا سن)',
        'blocks': [
            {'label': 'رابطه توسعه و دموکراسی', 'text': 'آزادی‌های سیاسی نه‌تنها هدف توسعه، بلکه ابزار اصلی تحقق آن در حوزه‌های اقتصادی و اجتماعی هستند.', 'color': '#1A237E'},
            {'label': 'یافته کلیدی', 'text': 'هیچ قحطی بزرگی در تاریخ مدرن در یک کشور دموکراتیک با مطبوعات آزاد رخ نداده است.', 'color': '#B71C1C', 'hero': True}
        ]
    },
    {
        'filename': 'ch03_slide4.svg',
        'chapter': 'فصل ۳: مبانی نظری',
        'title': 'نهادهای فراگیر در برابر استخراجی',
        'blocks': [
            {'label': 'چرا ملت‌ها شکست می‌خورند؟', 'text': 'نهادهای فراگیر فرصت برابر و حاکمیت قانون ایجاد می‌کنند، در حالی که نهادهای استخراجی در پی انحصار قدرت و غارت منابع‌اند.', 'color': '#1A237E'},
            {'label': 'مسیر بالندگی', 'text': 'گذار پایدار نیازمند جایگزینی نهادهای استخراجی فعلی با نهادهای فراگیر دموکراتیک است.', 'color': '#2E7D32'}
        ]
    },
    {
        'filename': 'ch03_slide5.svg',
        'chapter': 'فصل ۳: مبانی نظری',
        'title': 'عدالت انتقالی و آشتی ملی',
        'blocks': [
            {'label': 'چهار ستون آشتی', 'text': 'حقیقت‌گویی، تحقق عدالت، جبران خسارت قربانیان و اصلاحات نهادی برای عدم تکرار گذشته.', 'color': '#1A237E'},
            {'label': 'درس تاریخی', 'text': 'آشتی ملی بر پایه حقیقت و انصاف، تنها راه برای عبور از ترومای جمعی و حرکت به سوی آینده مشترک است.', 'color': '#F9A825', 'hero': True}
        ]
    }
]

for slide in slides_data_ch03:
    create_svg(slide['filename'], slide['chapter'], slide['title'], slide['blocks'])
