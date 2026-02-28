import os

output_dir = r'd:\Code\Books\Transition for Iran\00- Iran in phase of Transition State\images\slides'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def create_svg(filename, chapter_title, slide_title, content_blocks):
    svg_start = f'''<svg width="1080" height="1350" viewBox="0 0 1080 1350" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="headerGrad" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" style="stop-color:#FF6D00;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#E65100;stop-opacity:1" />
        </linearGradient>
    </defs>
    <rect width="1080" height="1350" fill="#FFF3E0" opacity="0.4" />
    <rect width="1080" height="1350" fill="white" />
    
    <rect width="1080" height="120" fill="#E65100" />
    <foreignObject x="40" y="35" width="1000" height="60">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn', sans-serif; color: white; font-size: 34px; font-weight: bold;">
            {chapter_title}
        </div>
    </foreignObject>
    
    <foreignObject x="60" y="160" width="960" height="140">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn', sans-serif; color: #BF360C; font-size: 50px; font-weight: 900; line-height: 1.3;">
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
        color = block.get('color', '#E65100')
        is_hero = block.get('hero', False)
        
        text_len = len(text)
        height = 190
        if is_hero: height = 280
        if text_len > 120: height += 60
        if text_len > 220: height += 80
        
        card = f'''
        <rect y="{y_offset}" width="960" height="{height}" rx="28" fill="white" style="filter: drop-shadow(0 12px 24px rgba(230,81,0,0.12));" />
        <circle cx="920" cy="{y_offset + 50}" r="15" fill="{color}" />
        
        <foreignObject x="50" y="{y_offset + 35}" width="850" height="{height - 70}">
            <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn', sans-serif;">
                <div style="color: {color}; font-size: 26px; font-weight: 800; margin-bottom: 20px; letter-spacing: 1px;">{label}</div>
                <div style="color: #3E2723; font-size: { '44px' if is_hero else '32px' }; font-weight: { '900' if is_hero else '500' }; line-height: 1.6;">
                    {text}
                </div>
            </div>
        </foreignObject>
        '''
        cards_svg += card
        y_offset += height + 40
        
    svg_end = f'''
    </g>
    
    <text x="540" y="1310" text-anchor="middle" font-family="'Vazirmatn', sans-serif" font-size="22" font-weight="bold" fill="#E65100" opacity="0.6">ایران برای همه ایرانیان • ۲۰۲۶</text>
    </svg>
    '''
    
    full_svg = svg_start + cards_svg + svg_end
    
    full_path = os.path.join(output_dir, filename)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(full_svg)
    print(f"Generated: {full_path}")

# Chapter 12 Slides Data
slides_data_ch12 = [
    {
        'filename': 'ch12_slide1.svg',
        'chapter': 'فصل ۱۲: مدیریت تنوع قومی-فرهنگی',
        'title': 'وحدت در کثرت: گنجینه ایرانی',
        'blocks': [
            {'label': 'تبیین مسئله', 'text': 'ایران سرزمین همه ایرانیان است. تنوع قومی نه‌تنها یک تهدید نیست، بلکه ثروتی است که دموکراسی ما را غنی و پایدار می‌کند.', 'color': '#E65100'},
            {'label': 'فلسفه فدرالیسم', 'text': 'مدل «فدرالیسم همبسته»: تضمین حقوق فرهنگی-زبانی اقوام در عین حفظ تمامیت ارضی و وحدت ملی.', 'color': '#2E7D32', 'hero': True}
        ]
    },
    {
        'filename': 'ch12_slide2.svg',
        'chapter': 'فصل ۱۲: مدیریت تنوع قومی-فرهنگی',
        'title': 'پایان همگون‌سازی اجباری',
        'blocks': [
            {'label': 'درس تاریخ', 'text': 'تجربه ۱۰۰ سال اخیر نشان داده که سرکوب هویت قومی تنها به شکاف و بی‌اعتمادی دامن زده است. وقت تغییر پارادایم است.', 'color': '#E65100', 'hero': True},
            {'label': 'شهروندی برابر', 'text': 'نفی هرگونه نگاه «مرکز-پیرامونی»؛ تمام اقوام ایرانی باید خود را شریک برابر در قدرت و ثروت ملی بدانند.', 'color': '#1A237E'}
        ]
    },
    {
        'filename': 'ch12_slide3.svg',
        'chapter': 'فصل ۱۲: مدیریت تنوع قومی-فرهنگی',
        'title': 'ساختار فدرال و مناطق خودمختار',
        'blocks': [
            {'label': 'توزیع قدرت', 'text': 'استقرار ۵ منطقه خودمختار با پارلمان‌های محلی برای آذربایجان، کردستان، بلوچستان، عرب‌خوزستان و ترکمن‌صحرا.', 'color': '#E65100'},
            {'label': 'مجلس اقوام', 'text': 'تشکیل لایه دوم پارلمان ملی برای صیانت از حقوق مناطق و جلوگیری از تمرکزگرایی مجدد در بدنه حکومت.', 'color': '#BF360C', 'hero': True}
        ]
    },
    {
        'filename': 'ch12_slide4.svg',
        'chapter': 'فصل ۱۲: مدیریت تنوع قومی-فرهنگی',
        'title': 'حقوق زبانی: ثروت چندصدایی',
        'blocks': [
            {'label': 'سیاست زبانی', 'text': 'آموزش به زبان مادری در مدارس مناطق قومی در کنار تقویت زبان ملی (فارسی) به عنوان پیونددهنده کل ایران.', 'color': '#E65100'},
            {'label': 'هویت فرهنگی', 'text': 'رسمیت یافتن زبان‌های آذری، کردی، عربی، بلوچی و ترکمنی در حوزه‌های اداری، قضایی و رسانه‌ای مناطق خود.', 'color': '#2E7D32', 'hero': True}
        ]
    },
    {
        'filename': 'ch12_slide5.svg',
        'chapter': 'فصل ۱۲: مدیریت تنوع قومی-فرهنگی',
        'title': 'عدالت اقتصادی: جبران نابرابری',
        'blocks': [
            {'label': 'توسعه متوازن', 'text': 'توزیع عادلانه درآمدهای نفت، گاز و معادن؛ سهم مستقیم ۲۵ درصدی استان‌های تولیدکننده برای آبادانی محلی.', 'color': '#E65100'},
            {'label': 'صندوق همبستگی', 'text': 'سرمایه‌گذاری ۱۶۵ میلیارد دلاری در مناطق محروم برای محو فقر پنهان و ساختن ایرانی شکوفا در تمام مرزها.', 'color': '#F9A825', 'hero': True}
        ]
    }
]

for slide in slides_data_ch12:
    create_svg(slide['filename'], slide['chapter'], slide['title'], slide['blocks'])
