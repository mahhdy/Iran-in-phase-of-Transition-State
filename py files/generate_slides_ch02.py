import os

# Create directory for slides
output_dir = r'd:\Code\Books\Transition for Iran\00- Iran in phase of Transition State\images\slides'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def create_svg(filename, chapter_title, slide_title, content_blocks):
    """
    chapter_title: String for the top bar
    slide_title: Main heading for the slide
    content_blocks: List of dicts with 'label', 'text', 'color'
    """
    
    # SVG Template 1080x1350
    svg_start = f'''<svg width="1080" height="1350" viewBox="0 0 1080 1350" xmlns="http://www.w3.org/2000/svg">
    <!-- Background -->
    <rect width="1080" height="1350" fill="#F5F5F7" />
    
    <!-- Header Bar -->
    <rect width="1080" height="100" fill="#1A237E" />
    <foreignObject x="40" y="20" width="1000" height="60">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn', sans-serif; color: white; font-size: 32px; font-weight: bold;">
            {chapter_title}
        </div>
    </foreignObject>
    
    <!-- Slide Title -->
    <foreignObject x="60" y="140" width="960" height="120">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn', sans-serif; color: #1A237E; font-size: 48px; font-weight: 800; line-height: 1.2;">
            {slide_title}
        </div>
    </foreignObject>
    
    <g transform="translate(60, 260)">
    '''
    
    y_offset = 0
    cards_svg = ""
    
    for block in content_blocks:
        label = block.get('label', '')
        text = block.get('text', '')
        color = block.get('color', '#1A237E')
        is_hero = block.get('hero', False)
        
        height = 200 if not is_hero else 280
        if len(text) > 150: height += 100
        
        card = f'''
        <rect y="{y_offset}" width="960" height="{height}" rx="20" fill="white" filter="drop-shadow(0 4px 6px rgba(0,0,0,0.05))" />
        <rect y="{y_offset}" width="15" height="{height}" rx="2" fill="{color}" />
        
        <foreignObject x="40" y="{y_offset + 30}" width="880" height="{height - 60}">
            <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn', sans-serif;">
                <div style="color: {color}; font-size: 24px; font-weight: bold; margin-bottom: 15px;">{label}</div>
                <div style="color: #424242; font-size: { '44px' if is_hero else '28px' }; font-weight: { '800' if is_hero else '500' }; line-height: 1.5;">
                    {text}
                </div>
            </div>
        </foreignObject>
        '''
        cards_svg += card
        y_offset += height + 40
        
    svg_end = f'''
    </g>
    
    <!-- Footer -->
    <text x="540" y="1310" text-anchor="middle" font-family="'Vazirmatn', sans-serif" font-size="20" fill="#9E9E9E">ایران در گذار - طرح پیشنهادی کالبدی</text>
    </svg>
    '''
    
    full_svg = svg_start + cards_svg + svg_end
    
    full_path = os.path.join(output_dir, filename)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(full_svg)
    print(f"Generated: {full_path}")

# Chapter 2 Slides Data
slides_data = [
    {
        'filename': 'ch02_slide1.svg',
        'chapter': 'فصل ۲: تشخیص وضعیت',
        'title': 'بحران‌های شش‌گانه: یک شبکه علّی',
        'blocks': [
            {'label': 'یافته اصلی', 'text': 'کشور با شش بحران به‌هم‌پیوسته (آب، انرژی، اقتصاد، سیاست، اجتماع و امنیت) روبروست که یکدیگر را تشدید می‌کنند.', 'color': '#1A237E'},
            {'label': 'وضعیت سیستمی', 'text': 'بحران فراتر از یک بخش خاص است؛ کل سیستم در حالت بی‌ثباتی قرار دارد.', 'color': '#F9A825', 'hero': True}
        ]
    },
    {
        'filename': 'ch02_slide2.svg',
        'chapter': 'فصل ۲: تشخیص وضعیت',
        'title': 'بحران آب: تهدید وجودی',
        'blocks': [
            {'label': 'داده‌های نگران‌کننده', 'text': '۷۱٪ از سفره‌های آب زیرزمینی کشور در وضعیت بحرانی یا ممنوعه قرار دارند.', 'color': '#1A237E'},
            {'label': 'پیش‌بینی ۲۰۴۰', 'text': '۳۰ تا ۵۰ میلیون نفر آوارگی اقلیمی در صورت ادامه روند فعلی برداشت مازاد.', 'color': '#B71C1C', 'hero': True}
        ]
    },
    {
        'filename': 'ch02_slide3.svg',
        'chapter': 'فصل ۲: تشخیص وضعیت',
        'title': 'اقتصاد در تله انسداد',
        'blocks': [
            {'label': 'ریشه بحران', 'text': 'ترکیب تورم مزمن، فساد سیستماتیک و تحریم‌های بین‌المللی، قدرت خرید را نابود کرده است.', 'color': '#1A237E'},
            {'label': 'تعریف کلیدی', 'text': '«اقتصاد دستوری» مانع اصلی هرگونه رقابت سالم و شکوفایی است.', 'color': '#F9A825'}
        ]
    },
    {
        'filename': 'ch02_slide4.svg',
        'chapter': 'فصل ۲: تشخیص وضعیت',
        'title': 'سرمایه اجتماعی و بی‌اعتمادی',
        'blocks': [
            {'label': 'شکاف ملت-دولت', 'text': 'بی‌اعتمادی تاریخی و انسداد سیاسی سیستم را در برابر اصلاحات خودکار ناتوان کرده است.', 'color': '#1A237E'},
            {'label': 'شاخص کلیدی', 'text': 'کاهش شدید مشارکت و اعتماد عمومی به نهادهای سنتی حاکمیتی.', 'color': '#2E7D32'}
        ]
    },
    {
        'filename': 'ch02_slide5.svg',
        'chapter': 'فصل ۲: تشخیص وضعیت',
        'title': 'فرصت‌ها در دل بحران',
        'blocks': [
            {'label': 'تحلیل SWOT', 'text': 'جمعیت جوان تحصیل‌کرده، موقعیت ژئوپلیتیک و منابع غنی، ستون‌های گذار هستند.', 'color': '#2E7D32'},
            {'label': 'پیشنهاد راهبردی', 'text': 'گذار ممکن است، اما نیازمند اقدام فوری، هماهنگ و تغییر پارادایم است.', 'color': '#F9A825', 'hero': True}
        ]
    }
]

for slide in slides_data:
    create_svg(slide['filename'], slide['chapter'], slide['title'], slide['blocks'])

