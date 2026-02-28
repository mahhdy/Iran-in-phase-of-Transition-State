import os

output_dir = r'd:\Code\Books\Transition for Iran\00- Iran in phase of Transition State\images\slides'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def create_democracy_layers_slide(filename, chapter_title):
    svg = f'''<svg width="1080" height="1350" viewBox="0 0 1080 1350" xmlns="http://www.w3.org/2000/svg">
    <rect width="1080" height="1350" fill="#f8f9fa"/>
    <rect x="0" y="0" width="1080" height="100" fill="#283593"/>
    <foreignObject x="0" y="0" width="1080" height="100">
        <div xmlns="http://www.w3.org/1999/xhtml" style="width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; font-family: 'Vazirmatn', sans-serif; font-size: 36px; font-weight: 800; color: white; direction: rtl;">
            {chapter_title}
        </div>
    </foreignObject>

    <text x="540" y="220" text-anchor="middle" font-family="'Vazirmatn'" font-size="52" font-weight="900" fill="#1A237E">لایه‌های دموکراسی: از پوسته تا هسته</text>

    <!-- The Diamond/Pyramid Layers -->
    <g transform="translate(540, 700)">
        <!-- Layer 4: Culture -->
        <path d="M0,-350 L200,-150 L-200,-150 Z" fill="#FFC107" stroke="#FFA000" stroke-width="4"/>
        <text y="-220" text-anchor="middle" font-family="'Vazirmatn'" font-size="28" font-weight="900" fill="#5D4037">فرهنگ دموکراتیک</text>

        <!-- Layer 3: Institutions -->
        <path d="M-200,-150 L200,-150 L350,50 L-350,50 Z" fill="#64B5F6" stroke="#1E88E5" stroke-width="4"/>
        <text y="-50" text-anchor="middle" font-family="'Vazirmatn'" font-size="28" font-weight="900" fill="#0D47A1">نهادهای مستقل</text>

        <!-- Layer 2: Rights -->
        <path d="M-350,50 L350,50 L500,250 L-500,250 Z" fill="#BBDEFB" stroke="#64B5F6" stroke-width="4"/>
        <text y="150" text-anchor="middle" font-family="'Vazirmatn'" font-size="28" font-weight="900" fill="#0D47A1">حقوق و آزادی‌ها</text>

        <!-- Layer 1: Elections -->
        <path d="M-500,250 L500,250 L400,350 L-400,350 Z" fill="#E3F2FD" stroke="#90CAF9" stroke-width="4"/>
        <text y="310" text-anchor="middle" font-family="'Vazirmatn'" font-size="28" font-weight="900" fill="#0D47A1">انتخابات و رویه‌ها</text>
    </g>

    <foreignObject x="100" y="1100" width="880" height="200">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn'; color: #37474F; font-size: 22px; text-align: center; line-height: 1.8;">
            بدون <strong style="color: #FF8F00;">فرهنگ مدارا</strong> و <strong style="color: #1E88E5;">نهادهای مستقل</strong>، دموکراسی تنها یک پوسته انتخابی شکننده است که به راحتی به استبداد بازمی‌گردد.
        </div>
    </foreignObject>

    <!-- Slide ID -->
    <circle cx="1020" cy="1300" r="30" fill="#283593"/>
    <text x="1020" y="1310" text-anchor="middle" font-family="'Vazirmatn', sans-serif" font-size="24" font-weight="bold" fill="white">۳۱</text>
    </svg>
    '''
    full_path = os.path.join(output_dir, filename)
    with open(full_path, 'wb') as f:
        f.write(svg.encode('utf-8'))
    print(f"Generated democracy layers slide at: {full_path}")

def create_political_spectrum_slide(filename, chapter_title):
    svg = f'''<svg width="1080" height="1350" viewBox="0 0 1080 1350" xmlns="http://www.w3.org/2000/svg">
    <rect width="1080" height="1350" fill="#ffffff"/>
    <rect x="0" y="0" width="1080" height="100" fill="#4B0082"/>
    <foreignObject x="0" y="0" width="1080" height="100">
        <div xmlns="http://www.w3.org/1999/xhtml" style="width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; font-family: 'Vazirmatn', sans-serif; font-size: 36px; font-weight: 800; color: white; direction: rtl;">
            {chapter_title}
        </div>
    </foreignObject>

    <text x="540" y="220" text-anchor="middle" font-family="'Vazirmatn'" font-size="52" font-weight="900" fill="#4B0082">طیف نظام‌های سیاسی</text>

    <!-- The Spectrum Scale -->
    <g transform="translate(90, 600)">
        <defs>
            <linearGradient id="spectrumShadow" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" style="stop-color:#C62828"/>
                <stop offset="50%" style="stop-color:#FFD600"/>
                <stop offset="100%" style="stop-color:#2E7D32"/>
            </linearGradient>
        </defs>
        <rect width="900" height="40" rx="20" fill="url(#spectrumShadow)"/>
        
        <!-- Nodes -->
        <g transform="translate(0, 0)">
            <circle cy="20" r="10" fill="white"/>
            <text y="70" text-anchor="middle" font-family="Vazirmatn" font-size="20" font-weight="900" fill="#C62828">توتالیتر</text>
        </g>
        <g transform="translate(225, 0)">
            <circle cy="20" r="10" fill="white"/>
            <text y="70" text-anchor="middle" font-family="Vazirmatn" font-size="20" font-weight="900" fill="#B71C1C">اقتدارگرای بسته</text>
        </g>
        <g transform="translate(450, 0)">
            <circle cy="20" r="10" fill="white"/>
            <text y="70" text-anchor="middle" font-family="Vazirmatn" font-size="20" font-weight="900" fill="#F57F17">اقتدارگرای رقابتی</text>
            <!-- Important Highlight -->
            <rect x="-100" y="-120" width="200" height="60" rx="10" fill="#FFF" stroke="#F57F17" stroke-width="2"/>
            <text y="-85" text-anchor="middle" font-family="Vazirmatn" font-size="18" font-weight="800" fill="#E65100">وضعیت فعلی؟</text>
        </g>
        <g transform="translate(675, 0)">
            <circle cy="20" r="10" fill="white"/>
            <text y="70" text-anchor="middle" font-family="Vazirmatn" font-size="20" font-weight="900" fill="#2E7D32">دموکراسی انتخاباتی</text>
        </g>
        <g transform="translate(900, 0)">
            <circle cy="20" r="10" fill="white"/>
            <text y="70" text-anchor="middle" font-family="Vazirmatn" font-size="20" font-weight="900" fill="#1B5E20">دموکراسی لیبرال</text>
        </g>
    </g>

    <!-- Info Boxes -->
    <g transform="translate(90, 850)">
        <rect width="400" height="200" rx="20" fill="#FFEBEE"/>
        <foreignObject x="20" y="20" width="360" height="160">
            <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: Vazirmatn; font-size: 18px; color: #C62828;">
                <strong>اقتدارگرایی رقابتی:</strong><br/>انتخاباتی وجود دارد اما زمین بازی ناعادلانه است. رسانه‌ها و نهادهای قانونی در انحصار یک گروه کوچک قرار دارند.
            </div>
        </foreignObject>

        <rect x="500" width="400" height="200" rx="20" fill="#E8F5E9"/>
        <foreignObject x="520" y="20" width="360" height="160">
            <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: Vazirmatn; font-size: 18px; color: #2E7D32;">
                <strong>دموکراسی لیبرال:</strong><br/>علاوه بر صندوق رای، حاکمیت قانون، تفکیک قوا و حقوق اقلیت‌ها تضمین شده است.
            </div>
        </foreignObject>
    </g>

    <!-- Slide ID -->
    <circle cx="1020" cy="1300" r="30" fill="#4B0082"/>
    <text x="1020" y="1310" text-anchor="middle" font-family="'Vazirmatn', sans-serif" font-size="24" font-weight="bold" fill="white">۳۲</text>
    </svg>
    '''
    full_path = os.path.join(output_dir, filename)
    with open(full_path, 'wb') as f:
        f.write(svg.encode('utf-8'))
    print(f"Generated political spectrum slide at: {full_path}")

if __name__ == "__main__":
    create_democracy_layers_slide('ch03_creative_1.svg', 'فصل ۳: مبانی نظری — دموکراسی، تنوع، توسعه')
    create_political_spectrum_slide('ch03_creative_2.svg', 'فصل ۳: مبانی نظری — دموکراسی، تنوع، توسعه')
