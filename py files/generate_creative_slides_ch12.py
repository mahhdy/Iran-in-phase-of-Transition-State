import os

output_dir = r'd:\Code\Books\Transition for Iran\00- Iran in phase of Transition State\images\slides'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def create_mosaic_slide(filename, chapter_title):
    svg = f'''<svg width="1080" height="1350" viewBox="0 0 1080 1350" xmlns="http://www.w3.org/2000/svg">
    <rect width="1080" height="1350" fill="#000814"/>
    
    <!-- Header -->
    <rect x="0" y="0" width="1080" height="100" fill="#FFC300"/>
    <foreignObject x="0" y="0" width="1080" height="100">
        <div xmlns="http://www.w3.org/1999/xhtml" style="width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; font-family: 'Vazirmatn', sans-serif; font-size: 36px; font-weight: 800; color: #000814; direction: rtl;">
            {chapter_title}
        </div>
    </foreignObject>

    <text x="540" y="200" text-anchor="middle" font-family="'Vazirmatn'" font-size="52" font-weight="900" fill="white">کثرت در وحدت: موزاییک ملی</text>

    <!-- Abstract Puzzle Iran Map -->
    <g transform="translate(540, 650) scale(1.2)">
        <!-- The pieces (Simulated) -->
        <path d="M-200,-150 Q-150,-180 -100,-150 L-100,-50 Q-150,-20 -200,-50 Z" fill="#003566" stroke="white" stroke-width="2"/>
        <path d="M-100,-150 Q-50,-120 0,-150 L0,-50 Q-50,-80 -100,-50 Z" fill="#001D3D" stroke="white" stroke-width="2"/>
        <path d="M0,-150 Q50,-180 100,-150 L100,-50 Q50,-20 0,-50 Z" fill="#FFC300" stroke="white" stroke-width="2"/>
        <path d="M100,-150 Q150,-120 200,-150 L200,-50 Q150,-80 100,-50 Z" fill="#FFD60A" stroke="white" stroke-width="2"/>
        
        <path d="M-200,-50 Q-150,-80 -100,-50 L-100,50 Q-150,80 -200,50 Z" fill="#FFD60A" stroke="white" stroke-width="2"/>
        <path d="M-100,-50 Q-50,-20 0,-50 L0,50 Q-50,20 -100,50 Z" fill="#003566" stroke="white" stroke-width="2"/>
        <path d="M0,-50 Q50,-80 0,-50 L0,50 Q50,80 0,50 Z" fill="#001D3D" stroke="white" stroke-opacity="0"/> <!-- Gap fill -->
        <path d="M0,-50 Q50,-20 100,-50 L100,50 Q50,20 0,50 Z" fill="#003566" stroke="white" stroke-width="2"/>
        <path d="M100,-50 Q150,-80 200,-50 L200,50 Q150,80 100,50 Z" fill="#FFC300" stroke="white" stroke-width="2"/>

        <path d="M-200,50 Q-150,20 -100,50 L-100,150 Q-150,180 -200,150 Z" fill="#001D3D" stroke="white" stroke-width="2"/>
        <path d="M-100,50 Q-50,80 0,50 L0,150 Q-50,120 -100,150 Z" fill="#FFC300" stroke="white" stroke-width="2"/>
        <path d="M0,50 Q50,20 100,50 L100,150 Q50,180 0,150 Z" fill="#FFD60A" stroke="white" stroke-width="2"/>
        <path d="M100,50 Q150,80 200,50 L200,150 Q150,120 100,150 Z" fill="#003566" stroke="white" stroke-width="2"/>
    </g>

    <foreignObject x="100" y="900" width="880" height="300">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn'; color: #B0BEC5; font-size: 24px; text-align: center; line-height: 1.8;">
            <strong style="color: #FFC300;">فدرالیسم همساز:</strong> نهادینه کردن تنوع به عنوان یک <strong style="color: white;">منبع قدرت</strong>، نه تهدیدی برای امنیت.<br/>
            همه تکه‌های موزاییک ایران برای تکمیل تصویر نهایی ضروری هستند.
        </div>
    </foreignObject>

    <!-- Slide ID -->
    <circle cx="1020" cy="1300" r="30" fill="#FFC300"/>
    <text x="1020" y="1310" text-anchor="middle" font-family="'Vazirmatn', sans-serif" font-size="24" font-weight="bold" fill="#000814">۱۱۲</text>
    </svg>
    '''
    full_path = os.path.join(output_dir, filename)
    with open(full_path, 'wb') as f:
        f.write(svg.encode('utf-8'))
    print(f"Generated mosaic slide at: {full_path}")

def create_federalism_spectrum_slide(filename, chapter_title):
    svg = f'''<svg width="1080" height="1350" viewBox="0 0 1080 1350" xmlns="http://www.w3.org/2000/svg">
    <rect width="1080" height="1350" fill="#F0F2F5"/>
    
    <!-- Header -->
    <rect x="0" y="0" width="1080" height="100" fill="#2E7D32"/>
    <foreignObject x="0" y="0" width="1080" height="100">
        <div xmlns="http://www.w3.org/1999/xhtml" style="width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; font-family: 'Vazirmatn', sans-serif; font-size: 36px; font-weight: 800; color: white; direction: rtl;">
            {chapter_title}
        </div>
    </foreignObject>

    <text x="540" y="200" text-anchor="middle" font-family="'Vazirmatn'" font-size="52" font-weight="900" fill="#1B5E20">تقابل مدل‌ها: چرا فدرالیسم همساز؟</text>

    <!-- The Spectrum Line -->
    <g transform="translate(100, 600)">
        <path d="M0,0 L880,0" stroke="#1B5E20" stroke-width="6" marker-start="url(#dot)" marker-end="url(#dot)"/>
        
        <!-- Left: Extreme Centralism -->
        <g transform="translate(0, 50)">
            <rect x="-80" y="0" width="200" height="150" rx="15" fill="#C62828" opacity="0.1" stroke="#C62828" stroke-width="2"/>
            <foreignObject x="-70" y="10" width="180" height="130">
                <div xmlns="http://www.w3.org/1999/xhtml" style="font-family:Vazirmatn; text-align:center; direction:rtl;">
                    <strong style="color:#B71C1C;">تمرکزگرایی مطلق</strong><br/>تک‌زبانی اجباری<br/>سرکوب هویت‌ها<br/>شکاف مرکز-پیرامون
                </div>
            </foreignObject>
        </g>

        <!-- Right: Separatism -->
        <g transform="translate(760, 50)">
            <rect x="-80" y="0" width="200" height="150" rx="15" fill="#607D8B" opacity="0.1" stroke="#455A64" stroke-width="2"/>
            <foreignObject x="-70" y="10" width="180" height="130">
                <div xmlns="http://www.w3.org/1999/xhtml" style="font-family:Vazirmatn; text-align:center; direction:rtl;">
                    <strong style="color:#37474F;">تجزیه‌طلبی</strong><br/>فروپاشی سرزمینی<br/>تنش‌های مرزی<br/>بی‌ثباتی مزمن
                </div>
            </foreignObject>
        </g>

        <!-- Center: Cohesive Federalism -->
        <g transform="translate(440, -150)">
            <rect x="-150" y="0" width="300" height="200" rx="20" fill="#FFF" stroke="#2E7D32" stroke-width="5" style="filter: drop-shadow(0 10px 10px rgba(0,0,0,0.1))"/>
            <foreignObject x="-130" y="20" width="260" height="160">
                <div xmlns="http://www.w3.org/1999/xhtml" style="font-family:Vazirmatn; text-align:center; direction:rtl;">
                    <strong style="color:#1B5E20; font-size:28px;">فدرالیسم همساز</strong><br/>توزیع عادلانه قدرت<br/>آموزش به زبان مادری<br/>بقا در سایه وحدت
                </div>
            </foreignObject>
            <!-- Needle -->
            <path d="M0,200 L0,300" stroke="#2E7D32" stroke-width="3" stroke-dasharray="5 5"/>
        </g>
    </g>

    <!-- Summary -->
    <rect x="60" y="1050" width="960" height="180" rx="30" fill="#E8F5E9" stroke="#2E7D32" stroke-width="1"/>
    <foreignObject x="100" y="1090" width="880" height="120">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn'; color: #1B5E20; font-size: 22px; text-align: center; line-height: 1.6;">
            فدرالیسم همساز نه یک انتخاب لوکس، بلکه <strong style="color: #C62828;">تنها راه عملی</strong> برای جلوگیری از تجزیه و حفظ تمامیت ارضی ایران در دنیای مدرن است.
        </div>
    </foreignObject>

    <defs>
        <marker id="dot" markerWidth="10" markerHeight="10" refX="5" refY="5">
            <circle cx="5" cy="5" r="5" fill="#1B5E20" />
        </marker>
    </defs>

    <!-- Slide ID -->
    <circle cx="1020" cy="1300" r="30" fill="#2E7D32"/>
    <text x="1020" y="1310" text-anchor="middle" font-family="'Vazirmatn', sans-serif" font-size="24" font-weight="bold" fill="white">۱۲۲</text>
    </svg>
    '''
    full_path = os.path.join(output_dir, filename)
    with open(full_path, 'wb') as f:
        f.write(svg.encode('utf-8'))
    print(f"Generated spectrum slide at: {full_path}")

if __name__ == "__main__":
    create_mosaic_slide('ch12_creative_1.svg', 'فصل ۱۲: مدیریت تنوع قومی و زبانی')
    create_federalism_spectrum_slide('ch12_creative_2.svg', 'فصل ۱۲: مدیریت تنوع قومی و زبانی')
