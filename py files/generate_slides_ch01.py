import os

output_dir = r'd:\Code\Books\Transition for Iran\00- Iran in phase of Transition State\images\slides'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def create_svg(filename, chapter_title, slide_title, content_blocks):
    svg_start = f'''<svg width="1080" height="1350" viewBox="0 0 1080 1350" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="bgGrad" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" style="stop-color:#F8F9FA;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#E9ECEF;stop-opacity:1" />
        </linearGradient>
    </defs>
    <rect width="1080" height="1350" fill="url(#bgGrad)" />
    
    <rect width="1080" height="100" fill="#1A237E" />
    <foreignObject x="40" y="20" width="1000" height="60">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn', sans-serif; color: #F9A825; font-size: 32px; font-weight: bold;">
            {chapter_title}
        </div>
    </foreignObject>
    
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
        
        text_len = len(text)
        height = 180
        if is_hero: height = 260
        if text_len > 100: height += 60
        if text_len > 200: height += 80
        
        card = f'''
        <rect y="{y_offset}" width="960" height="{height}" rx="24" fill="white" style="filter: drop-shadow(0 10px 20px rgba(0,0,0,0.08));" />
        <path d="M 0 {y_offset + 24} Q 0 {y_offset} 24 {y_offset} L 40 {y_offset} L 40 {y_offset + height} L 24 {y_offset + height} Q 0 {y_offset + height} 0 {y_offset + height - 24} Z" fill="{color}" />
        
        <foreignObject x="70" y="{y_offset + 35}" width="850" height="{height - 70}">
            <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn', sans-serif;">
                <div style="color: {color}; font-size: 24px; font-weight: 800; margin-bottom: 20px; opacity: 0.8;">{label}</div>
                <div style="color: #2D3436; font-size: { '44px' if is_hero else '32px' }; font-weight: { '900' if is_hero else '500' }; line-height: 1.5;">
                    {text}
                </div>
            </div>
        </foreignObject>
        '''
        cards_svg += card
        y_offset += height + 40
        
    svg_end = f'''
    </g>
    
    <text x="540" y="1310" text-anchor="middle" font-family="'Vazirmatn', sans-serif" font-size="22" font-weight="bold" fill="#B0B0B0">I R A N • T R A N S I T I O N</text>
    </svg>
    '''
    
    full_svg = svg_start + cards_svg + svg_end
    
    full_path = os.path.join(output_dir, filename)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(full_svg)
    print(f"Generated: {full_path}")

# Chapter 1 Slides Data
slides_data_ch01 = [
    {
        'filename': 'ch01_slide1.svg',
        'chapter': 'فصل ۱: مقدمه - چرا این کتاب؟',
        'title': 'بن‌بست تاریخی و ضرورت گذار',
        'blocks': [
            {'label': 'تبیین مسئله', 'text': 'وضعیت موجود نه پایدار است و نه مطلوب؛ بحران‌های آب، اقتصاد و مشروعیت در حال تعمیق‌اند و ادامه مسیر فعلی به فروپاشی منجر خواهد شد.', 'color': '#1A237E'},
            {'label': 'هدف غایی', 'text': 'گذار دموکراتیک نه‌تنها یک آرمان سیاسی، بلکه تنها راه نجات کالبد ملی ایران از نابودی حتمی است.', 'color': '#B71C1C', 'hero': True}
        ]
    },
    {
        'filename': 'ch01_slide2.svg',
        'chapter': 'فصل ۱: مقدمه - چرا این کتاب؟',
        'title': 'شبکه بحران‌های تمدنی',
        'blocks': [
            {'label': 'آمار تکان‌دهنده', 'text': '۷۰٪ سفره‌های زیرزمینی در خطر نابودی و تورم بالای ۴۰٪ مزمن، ساختارهای زندگی در ایران را به مرتع انفجار رسانده است.', 'color': '#1A237E'},
            {'label': 'تهدید وجودی', 'text': 'بحران آب به تنهایی می‌تواند طی یک دهه آینده منجر به مهاجرت اجباری ده‌ها میلیون ایرانی شود.', 'color': '#F9A825', 'hero': True}
        ]
    },
    {
        'filename': 'ch01_slide3.svg',
        'chapter': 'فصل ۱: مقدمه - چرا این کتاب؟',
        'title': 'دموکراسی بومی‌: راه‌حل میانه',
        'blocks': [
            {'label': 'رویکرد متمایز', 'text': 'این طرح نه کپی‌برداری کور از مدل‌های غربی است و نه توجیه استبداد؛ بلکه دموکراسی بومی ریشه در واقعیات ایران دارد.', 'color': '#1A237E'},
            {'label': 'اصول غیرقابل‌مذاکره', 'text': 'کرامت انسانی، برابری شهروندان در قانون و حق تعیین سرنوشت، ستون‌های ابدی این بنا هستند.', 'color': '#2E7D32', 'hero': True}
        ]
    },
    {
        'filename': 'ch01_slide4.svg',
        'chapter': 'فصل ۱: مقدمه - چرا این کتاب؟',
        'title': 'اصل آبادانی ملموس و فوری',
        'blocks': [
            {'label': 'پیام اصلی', 'text': 'دموکراسی باید «نان» بیاورد تا ریشه بدواند. بهبود وضعیت معیشت در ۱۰۰ روز اول، ضامن بقای گذار است.', 'color': '#1A237E'},
            {'label': 'اولویت راهبردی', 'text': 'تأمین آب، برق، کاهش تورم و حذف فساد سیستماتیک، گام‌های نخست برای کسب اعتماد عمومی هستند.', 'color': '#F9A825', 'hero': True}
        ]
    },
    {
        'filename': 'ch01_slide5.svg',
        'chapter': 'فصل ۱: مقدمه - چرا این کتاب؟',
        'title': 'از چرخه باطل به چرخه فاضل',
        'blocks': [
            {'label': 'استراتژی تغییر', 'text': 'هدف ما جایگزینی «چرخه باطل فساد و بی‌اعتمادی» با «چرخه فاضل شفافیت و بالندگی» است.', 'color': '#1A237E'},
            {'label': 'دعوت به اقدام', 'text': 'گذار ممکن است؛ اگر با دانش، همبستگی و تمرکز بر آبادانی ملموس همین امروز آغاز کنیم.', 'color': '#2E7D32', 'hero': True}
        ]
    }
]

for slide in slides_data_ch01:
    create_svg(slide['filename'], slide['chapter'], slide['title'], slide['blocks'])
