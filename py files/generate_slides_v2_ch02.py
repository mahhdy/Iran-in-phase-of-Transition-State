import os

output_dir = r'd:\Code\Books\Transition for Iran\00- Iran in phase of Transition State\images\slides\v2'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Reuse the same creative engine but with a NEW THEME for Chapter 02 (Vision)
def create_svg_v2(filename, chapter_title, slide_title, content_blocks, theme_colors):
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
            <feComponentTransfer><feFuncA type="linear" slope="0.3" /></feComponentTransfer>
            <feMerge><feMergeNode /><feMergeNode in="SourceGraphic" /></feMerge>
        </filter>
    </defs>

    <rect width="1080" height="1350" fill="url(#mainBg)" />
    <circle cx="900" cy="150" r="250" fill="url(#glow)" opacity="0.8" />
    <circle cx="100" cy="1200" r="300" fill="url(#glow)" opacity="0.5" />
    <path d="M-50,400 Q200,300 400,500 T900,400" fill="none" stroke="white" stroke-width="2" opacity="0.2" />

    <rect x="0" y="0" width="1080" height="180" fill="white" opacity="0.1" />
    <foreignObject x="60" y="60" width="960" height="80">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn', sans-serif; color: rgba(255,255,255,0.8); font-size: 28px; font-weight: 300;">{chapter_title}</div>
    </foreignObject>

    <foreignObject x="60" y="200" width="960" height="220">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn', sans-serif; color: white; font-size: 64px; font-weight: 900; line-height: 1.2;">{slide_title}</div>
    </foreignObject>
    
    <g transform="translate(60, 440)">
    '''
    
    y_offset = 0
    cards_svg = ""
    for block in content_blocks:
        label = block.get('label', '')
        text = block.get('text', '')
        accent = block.get('color', c[2])
        is_hero = block.get('hero', False)
        card_h = 240 if not is_hero else 340
        if len(text) > 150: card_h += 80
        
        card = f'''
        <g transform="translate(0, {y_offset})" filter="url(#softShadow)">
            <rect width="960" height="{card_h}" rx="40" fill="white" opacity="0.15" />
            <rect width="960" height="{card_h}" rx="40" fill="none" stroke="white" stroke-width="1.5" opacity="0.4" />
            <rect x="944" y="40" width="8" height="{card_h - 80}" rx="4" fill="{accent}" />
            <foreignObject x="60" y="45" width="840" height="{card_h - 90}">
                <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn', sans-serif;">
                    <div style="color: {accent}; font-size: 24px; font-weight: 800; margin-bottom: 20px;">{label}</div>
                    <div style="color: white; font-size: { '42px' if is_hero else '32px' }; font-weight: { '800' if is_hero else '400' }; line-height: 1.6;">{text}</div>
                </div>
            </foreignObject>
        </g>
        '''
        cards_svg += card
        y_offset += card_h + 40
        
    svg_end = f'''
    </g>
    <text x="540" y="1300" text-anchor="middle" font-family="'Vazirmatn', sans-serif" font-size="20" font-weight="200" fill="white" opacity="0.6" letter-spacing="4">TRANSITION FOR IRAN • 2026</text>
    </svg>
    '''
    full_path = os.path.join(output_dir, filename)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(svg_start + cards_svg + svg_end)
    print(f"Generated: {full_path}")

# Chapter 02 (Vision) - Theme: Celestial & Hopeful (Deep Sea to Sky Blue)
ch02_colors = ["#2b5876", "#4e4376", "#FFD700", "#ffffff"] # Blue-purple bg, Gold accent

slides_data_ch02_v2 = [
    {
        'filename': 'ch02_slide1_v2.svg',
        'chapter': 'فصل ۲: نظریه گذار و مدل آرمانی',
        'title': 'ساختن آینده‌ای که شایسته آنیم',
        'blocks': [
            {'label': 'رؤیای مشترک', 'text': 'هدف ما تنها تغییر قدرت نیست، بلکه استقرار نظمی است که در آن کرامت انسان، عدالت اجتماعی و آزادی‌های بنیادین، متونِ لایتغیرِ میثاق ملی باشند.', 'hero': True},
            {'label': 'گذار آگاهانه', 'text': 'ما به دنبال گذاری هستیم که از بطن جامعه برخیزد و با دانش و بصیرت، بنای استبداد را با نهادهای دموکراتیک جایگزین کند.', 'color': '#FFD700'}
        ]
    }
]

for slide in slides_data_ch02_v2:
    create_svg_v2(slide['filename'], slide['chapter'], slide['title'], slide['blocks'], ch02_colors)
