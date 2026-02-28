import os

output_dir = r'd:\Code\Books\Transition for Iran\00- Iran in phase of Transition State\images\slides'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def create_svg(filename, chapter_title, slide_title, content_blocks):
    svg_start = f'''<svg width="1080" height="1350" viewBox="0 0 1080 1350" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="headerGrad" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" style="stop-color:#2E7D32;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#1B5E20;stop-opacity:1" />
        </linearGradient>
    </defs>
    <rect width="1080" height="1350" fill="#E8F5E9" opacity="0.4" />
    <rect width="1080" height="1350" fill="white" />
    
    <rect width="1080" height="120" fill="#2E7D32" />
    <foreignObject x="40" y="35" width="1000" height="60">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn', sans-serif; color: white; font-size: 34px; font-weight: bold;">
            {chapter_title}
        </div>
    </foreignObject>
    
    <foreignObject x="60" y="160" width="960" height="140">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn', sans-serif; color: #1B5E20; font-size: 50px; font-weight: 900; line-height: 1.3;">
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
        color = block.get('color', '#2E7D32')
        is_hero = block.get('hero', False)
        
        text_len = len(text)
        height = 190
        if is_hero: height = 280
        if text_len > 120: height += 60
        if text_len > 220: height += 80
        
        card = f'''
        <rect y="{y_offset}" width="960" height="{height}" rx="28" fill="white" style="filter: drop-shadow(0 12px 24px rgba(46,125,50,0.12));" />
        <rect x="940" y="{y_offset + 30}" width="12" height="{height - 60}" rx="6" fill="{color}" />
        
        <foreignObject x="50" y="{y_offset + 35}" width="860" height="{height - 70}">
            <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn', sans-serif;">
                <div style="color: {color}; font-size: 26px; font-weight: 800; margin-bottom: 20px; border-left: 8px solid {color}; padding-right: 15px;">{label}</div>
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
    
    <text x="540" y="1310" text-anchor="middle" font-family="'Vazirmatn', sans-serif" font-size="22" font-weight="bold" fill="#2E7D32" opacity="0.5">تنها بازی در شهر • ایران ۱۴۱۰</text>
    </svg>
    '''
    
    full_svg = svg_start + cards_svg + svg_end
    
    full_path = os.path.join(output_dir, filename)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(full_svg)
    print(f"Generated: {full_path}")

# Chapter 10 Slides Data
slides_data_ch10 = [
    {
        'filename': 'ch10_slide1.svg',
        'chapter': 'فصل ۱۰: فاز ۳ — تحکیم (سال ۶-۱۰)',
        'title': 'آزمون پایداری و بلوغ دموکراتیک',
        'blocks': [
            {'label': 'تبیین وضعیت', 'text': 'فاز سوم دوره تثبیت و تعمیق است. دموکراسی زمانی تحکیم می‌شود که فراتر از افراد، به قواعدی خدشه‌ناپذیر تبدیل شود.', 'color': '#2E7D32'},
            {'label': 'هدف راهبردی', 'text': 'موفقیت در اولین انتقال مسالمت‌آمیز قدرت بین احزاب رقیب؛ آزمونی که پایداری نظام جدید را تضمین می‌کند.', 'color': '#1B5E20', 'hero': True}
        ]
    },
    {
        'filename': 'ch10_slide2.svg',
        'chapter': 'فصل ۱۰: فاز ۳ — تحکیم (سال ۶-۱۰)',
        'title': 'آزمون جانشینی مسالمت‌آمیز',
        'blocks': [
            {'label': 'قانون بقا', 'text': 'دموکراسی زمانی بیمه می‌شود که حزب حاکم شکست را بپذیرد و قدرت را بدون تنش به اپوزیسیون واگذار کند.', 'color': '#2E7D32', 'hero': True},
            {'label': 'ارکان ثبات', 'text': 'بی‌طرفی کامل نیروهای مسلح و داوری مستقل نهادهای قضایی در منازعات انتخاباتی.', 'color': '#1A237E'}
        ]
    },
    {
        'filename': 'ch10_slide3.svg',
        'chapter': 'فصل ۱۰: فاز ۳ — تحکیم (سال ۶-۱۰)',
        'title': 'تثبیت اقتصادی و رفاه فراگیر',
        'blocks': [
            {'label': 'شکوفایی ملی', 'text': 'هدف‌گذاری رشد ۵٪+ و مهار تورم زیر ۵٪ در پایان سال دهم گذار؛ رفاه اقتصادی سنگر دفاع از دموکراسی است.', 'color': '#2E7D32'},
            {'label': 'تنوع‌بخشی', 'text': 'کاهش وابستگی به نفت به زیر ۱۵٪ از تولید ناخالص داخلی و جذب سرمایه‌های عظیم بین‌المللی برای بازسازی زیرساخت‌ها.', 'color': '#F9A825', 'hero': True}
        ]
    },
    {
        'filename': 'ch10_slide4.svg',
        'chapter': 'فصل ۱۰: فاز ۳ — تحکیم (سال ۶-۱۰)',
        'title': 'پایداری زیستی: فراتر از بقا',
        'blocks': [
            {'label': 'امنیت تمدنی', 'text': 'احیای محیط‌زیست و توقف کامل بحران‌های وجودی نظیر فرونشست زمین و خشکی تالاب‌ها با حکمرانی علمی.', 'color': '#2E7D32'},
            {'label': 'میراث ماندگار', 'text': 'تضمین پایداری منابع آب برای نسل‌های آینده؛ نشانه‌ای از کارآمدی نظام دموکراتیک در حل مسائل بلندمدت.', 'color': '#00796B', 'hero': True}
        ]
    },
    {
        'filename': 'ch10_slide5.svg',
        'chapter': 'فصل ۱۰: فاز ۳ — تحکیم (سال ۶-۱۰)',
        'title': 'ایران در آستانه فردا: دموکراسی پایدار',
        'blocks': [
            {'label': 'تحلیل نهایی', 'text': 'گذار از دموکراسی انتخاباتی به دموکراسی لیبرال و نهادینه شدن ارزش‌های حقوق شهروندی و مدارای اجتماعی.', 'color': '#2E7D32'},
            {'label': 'پیام امید', 'text': 'ایران در پایان سال دهم، کشوری است که دموکراسی در آن به «تنها بازی در شهر» تبدیل شده است.', 'color': '#1B5E20', 'hero': True}
        ]
    }
]

for slide in slides_data_ch10:
    create_svg(slide['filename'], slide['chapter'], slide['title'], slide['blocks'])
