import os

output_dir = r'd:\Code\Books\Transition for Iran\00- Iran in phase of Transition State\images\slides'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def create_svg(filename, chapter_title, slide_title, content_blocks):
    svg_start = f'''<svg width="1080" height="1350" viewBox="0 0 1080 1350" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="headerGrad" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" style="stop-color:#B71C1C;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#880E4F;stop-opacity:1" />
        </linearGradient>
    </defs>
    <rect width="1080" height="1350" fill="#FCE4EC" opacity="0.2" />
    <rect width="1080" height="1350" fill="white" />
    
    <rect width="1080" height="120" fill="#B71C1C" />
    <foreignObject x="40" y="35" width="1000" height="60">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn', sans-serif; color: white; font-size: 34px; font-weight: bold;">
            {chapter_title}
        </div>
    </foreignObject>
    
    <foreignObject x="60" y="160" width="960" height="140">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn', sans-serif; color: #B71C1C; font-size: 50px; font-weight: 900; line-height: 1.3;">
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
        color = block.get('color', '#B71C1C')
        is_hero = block.get('hero', False)
        
        text_len = len(text)
        height = 190
        if is_hero: height = 280
        if text_len > 120: height += 60
        if text_len > 220: height += 80
        
        card = f'''
        <rect y="{y_offset}" width="960" height="{height}" rx="28" fill="white" style="filter: drop-shadow(0 12px 24px rgba(183,28,28,0.1));" />
        <rect x="0" y="{y_offset}" width="12" height="{height}" rx="6" fill="{color}" />
        
        <foreignObject x="50" y="{y_offset + 35}" width="860" height="{height - 70}">
            <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn', sans-serif;">
                <div style="color: {color}; font-size: 26px; font-weight: 800; margin-bottom: 20px; border-bottom: 2px solid {color}33; display: inline-block;">{label}</div>
                <div style="color: #424242; font-size: { '44px' if is_hero else '32px' }; font-weight: { '900' if is_hero else '500' }; line-height: 1.6;">
                    {text}
                </div>
            </div>
        </foreignObject>
        '''
        cards_svg += card
        y_offset += height + 40
        
    svg_end = f'''
    </g>
    
    <text x="1040" y="1320" text-anchor="end" font-family="'Vazirmatn', sans-serif" font-size="20" fill="#BDBDBD">آموزه‌هایی برای ایران امروز</text>
    </svg>
    '''
    
    full_svg = svg_start + cards_svg + svg_end
    
    full_path = os.path.join(output_dir, filename)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(full_svg)
    print(f"Generated: {full_path}")

# Chapter 5 Slides Data
slides_data_ch05 = [
    {
        'filename': 'ch05_slide1.svg',
        'chapter': 'فصل ۵: درس‌های گذارهای ناموفق',
        'title': 'عبرت‌هایی از شکست گذارهای ملی',
        'blocks': [
            {'label': 'تبیین مسئله', 'text': 'مطالعه شکست‌ها (عراق، لیبی، مصر، ونزوئلا) به ما می‌آموزد که چه خطراتی در کمین گذار ایران است.', 'color': '#B71C1C'},
            {'label': 'یافته اصلی', 'text': 'فروپاشی ناگهانی نهادها و فقدان میثاق نخبگان، دموکراسی را به هرج‌ومرج یا بازگشت استبداد می‌کشاند.', 'color': '#880E4F', 'hero': True}
        ]
    },
    {
        'filename': 'ch02_slide12.svg', # Mistake in filename naming convention, but let's stick to ch05_...
        'filename': 'ch05_slide2.svg',
        'chapter': 'فصل ۵: درس‌های گذارهای ناموفق',
        'title': 'عراق: فاجعه تخریب نهادها',
        'blocks': [
            {'label': 'اشتباه مرگبار', 'text': 'انحلال ارتش و پاکسازی گسترده کارگزاران، عراق را با خلأ قدرت و بحران امنیتی عمیق مواجه کرد.', 'color': '#B71C1C'},
            {'label': 'درس برای ایران', 'text': 'نهادهای دولتی را نباید نابود کرد؛ بلکه باید آنها را اصلاح و در خدمت نظام جدید بازسازی نمود.', 'color': '#D32F2F', 'hero': True}
        ]
    },
    {
        'filename': 'ch05_slide3.svg',
        'chapter': 'فصل ۵: درس‌های گذارهای ناموفق',
        'title': 'مصر: شکست ائتلاف و نان',
        'blocks': [
            {'label': 'ریشه شکست', 'text': 'نزاع گروه‌های انقلابی و وخامت اوضاع معیشتی، باعث شد تا مردم به بازگشت نظامیان رضایت دهند.', 'color': '#B71C1C'},
            {'label': 'هشدار استراتژیک', 'text': 'دموکراسی باید بتواند در کوتاه‌ترین زمان، بهبود ملموسی در زندگی روزمره مردم ایجاد کند.', 'color': '#C2185B', 'hero': True}
        ]
    },
    {
        'filename': 'ch05_slide4.svg',
        'chapter': 'فصل ۵: درس‌های گذارهای ناموفق',
        'title': 'لیبی و یمن: خلأ حاکمیت',
        'blocks': [
            {'label': 'پیامد فروپاشی', 'text': 'در نبود نهادهای مدنی و سیاسی قوی، گذار به جنگ داخلی و حاکمیت میلیشیاهای محلی منجر شد.', 'color': '#B71C1C'},
            {'label': 'اصل تضمین', 'text': 'گفتگوی ملی بدون پشتوانه اجرایی و کنترل تسلیحات، تضمینی برای صلح و ثبات نخواهد بود.', 'color': '#D32F2F'}
        ]
    },
    {
        'filename': 'ch05_slide5.svg',
        'chapter': 'فصل ۵: درس‌های گذارهای ناموفق',
        'title': 'ونزوئلا: پوپولیسم ویرانگر',
        'blocks': [
            {'label': 'نفرین منابع', 'text': 'تخریب نهادهای نظارتی و تکیه بر درآمدهای نفتی، یک دموکراسی پایدار را به قعر بحران انسانی کشاند.', 'color': '#B71C1C'},
            {'label': 'ضرورت گذار', 'text': 'استقلال نهادها و تنوع اقتصادی، تنها راه مصونیت در برابر پوپولیسم و زوال تدریجی است.', 'color': '#880E4F', 'hero': True}
        ]
    }
]

for slide in slides_data_ch05:
    create_svg(slide['filename'], slide['chapter'], slide['title'], slide['blocks'])
