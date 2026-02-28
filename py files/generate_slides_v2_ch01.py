import os

output_dir = r'd:\Code\Books\Transition for Iran\00- Iran in phase of Transition State\images\slides\v2'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def create_svg_v2(filename, chapter_title, slide_title, content_blocks, theme_colors):
    """
    Highly creative and premium SVG slide generator (V2)
    theme_colors: list of [bg_start, bg_end, accent_color, card_glow]
    """
    c = theme_colors
    
    svg_start = f'''<svg width="1080" height="1350" viewBox="0 0 1080 1350" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="mainBg" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:{c[0]};stop-opacity:1" />
            <stop offset="100%" style="stop-color:{c[1]};stop-opacity:1" />
        </linearGradient>
        <radialGradient id="glow" cx="50%" cy="50%" r="50%" fx="50%" fy="50%">
            <stop offset="0%" style="stop-color:{c[3]};stop-opacity:0.6" />
            <stop offset="100%" style="stop-color:{c[3]};stop-opacity:0" />
        </radialGradient>
        <filter id="softShadow" x="-20%" y="-20%" width="140%" height="140%">
            <feGaussianBlur in="SourceAlpha" stdDeviation="15" />
            <feOffset dx="0" dy="10" result="offsetblur" />
            <feComponentTransfer>
                <feFuncA type="linear" slope="0.3" />
            </feComponentTransfer>
            <feMerge>
                <feMergeNode />
                <feMergeNode in="SourceGraphic" />
            </feMerge>
        </filter>
    </defs>

    <!-- Rich Background -->
    <rect width="1080" height="1350" fill="url(#mainBg)" />
    
    <!-- Abstract Decorative Shapes -->
    <circle cx="900" cy="150" r="250" fill="url(#glow)" opacity="0.8" />
    <circle cx="100" cy="1200" r="300" fill="url(#glow)" opacity="0.5" />
    <path d="M-50,400 Q200,300 400,500 T900,400" fill="none" stroke="white" stroke-width="2" opacity="0.1" />
    <path d="M200,1400 Q500,1100 800,1300" fill="none" stroke="white" stroke-width="2" opacity="0.1" />

    <!-- Glass Header -->
    <rect x="0" y="0" width="1080" height="180" fill="white" opacity="0.05" />
    <foreignObject x="60" y="60" width="960" height="80">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn', sans-serif; color: rgba(255,255,255,0.7); font-size: 28px; font-weight: 300; letter-spacing: 2px; text-transform: uppercase;">
            {chapter_title}
        </div>
    </foreignObject>

    <!-- Main Title (Psychological Anchor) -->
    <foreignObject x="60" y="200" width="960" height="220">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn', sans-serif; color: white; font-size: 64px; font-weight: 900; line-height: 1.2; text-shadow: 0 4px 20px rgba(0,0,0,0.3);">
            {slide_title}
        </div>
    </foreignObject>
    
    <g transform="translate(60, 440)">
    '''
    
    y_offset = 0
    cards_svg = ""
    
    for i, block in enumerate(content_blocks):
        label = block.get('label', '')
        text = block.get('text', '')
        accent = block.get('color', c[2])
        is_hero = block.get('hero', False)
        
        card_h = 240 if not is_hero else 340
        if len(text) > 150: card_h += 80
        
        # Glass card look
        card = f'''
        <g transform="translate(0, {y_offset})" filter="url(#softShadow)">
            <rect width="960" height="{card_h}" rx="40" fill="white" opacity="0.12" />
            <rect width="960" height="{card_h}" rx="40" fill="none" stroke="white" stroke-width="1.5" opacity="0.3" />
            
            <!-- Side Indicator -->
            <rect x="944" y="40" width="8" height="{card_h - 80}" rx="4" fill="{accent}" />
            
            <foreignObject x="60" y="45" width="840" height="{card_h - 90}">
                <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn', sans-serif;">
                    <div style="color: {accent}; font-size: 24px; font-weight: 800; margin-bottom: 20px; opacity: 0.9;">{label}</div>
                    <div style="color: white; font-size: { '42px' if is_hero else '32px' }; font-weight: { '800' if is_hero else '400' }; line-height: 1.6; opacity: 0.95;">
                        {text}
                    </div>
                </div>
            </foreignObject>
        </g>
        '''
        cards_svg += card
        y_offset += card_h + 40
        
    svg_end = f'''
    </g>
    
    <!-- Footer Branding -->
    <text x="540" y="1300" text-anchor="middle" font-family="'Vazirmatn', sans-serif" font-size="20" font-weight="200" fill="white" opacity="0.5" letter-spacing="4">TRANSITION FOR IRAN • 2026</text>
    <path d="M440 1315 L640 1315" stroke="white" stroke-width="1" opacity="0.2" />
    </svg>
    '''
    
    full_svg = svg_start + cards_svg + svg_end
    
    full_path = os.path.join(output_dir, filename)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(full_svg)
    print(f"Generated: {full_path}")

# Chapter 01 (Diagnosis) - Theme: Intense & High Contrast (Midnight Blue to Dark Purple)
ch01_colors = ["#0F0C29", "#302B63", "#00D2FF", "#24243E"]

slides_data_ch01_v2 = [
    {
        'filename': 'ch01_slide1_v2.svg',
        'chapter': 'فصل ۱: تشخیص بحران',
        'title': 'کالبدشکافی یک بحران ساختاری',
        'blocks': [
            {'label': 'واقعیت پیش‌رو', 'text': 'ایران درگیر یک «ابر‌بحران» چندلایه است؛ پیوندی میان بن‌بست سیاسی، فروپاشی اقتصادی و تخریب زیست‌محیطی که بقای ملی را تهدید می‌کند.', 'hero': True},
            {'label': 'ضرورت گذار', 'text': 'بدون تشخیص دقیق ریشه‌های این بیماری، هرگونه تلاشی برای تغییر، تنها به تکرار چرخه‌های گذشته منجر خواهد شد.', 'color': '#00D2FF'}
        ]
    },
    {
        'filename': 'ch01_slide2_v2.svg',
        'chapter': 'فصل ۱: تشخیص بحران',
        'title': 'بحران سه‌گانه: گسست‌های بنیادین',
        'blocks': [
            {'label': 'گسست سیاسی', 'text': 'ناکارآمدیِ نهادینه‌شده و گسستِ عمیق میان دولت و ملت که به بحران مشروعیت بی‌سابقه‌ای انجامیده است.', 'color': '#FF0080'},
            {'label': 'گسست اقتصادی', 'text': 'اقتصادی رانتی و منزوی که تحت فشار تحریم و فساد، توانایی تأمینِ حداقلی‌ترین نیازهای شهروندان را از دست داده است.', 'color': '#00FFAB'}
        ]
    }
]

for slide in slides_data_ch01_v2:
    create_svg_v2(slide['filename'], slide['chapter'], slide['title'], slide['blocks'], ch01_colors)
