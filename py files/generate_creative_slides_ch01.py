import os

output_dir = r'd:\Code\Books\Transition for Iran\00- Iran in phase of Transition State\images\slides'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def create_deadlock_spiral_slide(filename, chapter_title):
    svg = f'''<svg width="1080" height="1350" viewBox="0 0 1080 1350" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <filter id="glow">
            <feGaussianBlur stdDeviation="5" result="coloredBlur"/>
            <feMerge><feMergeNode in="coloredBlur"/><feMergeNode in="SourceGraphic"/></feMerge>
        </filter>
    </defs>
    <rect width="1080" height="1350" fill="#1a1a1a"/>
    
    <!-- Background Spiral Decor -->
    <path d="M540,700 m-400,0 a400,400 0 1,0 800,0 a400,400 0 1,0 -800,0" fill="none" stroke="#333" stroke-width="1" stroke-dasharray="10 20"/>
    
    <!-- Header -->
    <rect x="0" y="0" width="1080" height="100" fill="#B71C1C"/>
    <foreignObject x="0" y="0" width="1080" height="100">
        <div xmlns="http://www.w3.org/1999/xhtml" style="width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; font-family: 'Vazirmatn', sans-serif; font-size: 36px; font-weight: 800; color: white; direction: rtl;">
            {chapter_title}
        </div>
    </foreignObject>

    <!-- Title -->
    <text x="540" y="200" text-anchor="middle" font-family="'Vazirmatn'" font-size="52" font-weight="900" fill="#EF5350">مارپچِ بن‌بست تاریخی</text>

    <!-- The Spiral Diagram -->
    <g transform="translate(540, 700)">
        <!-- Core Problem -->
        <circle r="120" fill="#311B92" stroke="#B71C1C" stroke-width="5" filter="url(#glow)"/>
        <text y="15" text-anchor="middle" font-family="'Vazirmatn'" font-size="32" font-weight="900" fill="white">انسداد سیستماتیک</text>

        <!-- Spiral Arms -->
        <g class="arms">
            <!-- Crisis 1: Water -->
            <path d="M0,-120 Q100,-250 300,-200" fill="none" stroke="#0277BD" stroke-width="4" stroke-dasharray="5 5"/>
            <circle cx="300" cy="-200" r="80" fill="#01579B" opacity="0.9"/>
            <text x="300" y="-190" text-anchor="middle" font-family="'Vazirmatn'" font-size="24" font-weight="900" fill="white">بحران آب</text>
            
            <!-- Crisis 2: Economy -->
            <path d="M120,0 Q250,100 200,300" fill="none" stroke="#2E7D32" stroke-width="4" stroke-dasharray="5 5"/>
            <circle cx="200" cy="300" r="80" fill="#1B5E20" opacity="0.9"/>
            <text x="200" y="310" text-anchor="middle" font-family="'Vazirmatn'" font-size="24" font-weight="900" fill="white">اقتصاد ناتوان</text>

            <!-- Crisis 3: Social -->
            <path d="M0,120 Q-100,250 -300,200" fill="none" stroke="#F57F17" stroke-width="4" stroke-dasharray="5 5"/>
            <circle cx="-300" cy="200" r="80" fill="#E65100" opacity="0.9"/>
            <text x="-300" y="210" text-anchor="middle" font-family="'Vazirmatn'" font-size="24" font-weight="900" fill="white">گسست اجتماعی</text>
            
            <!-- Crisis 4: Security -->
            <path d="M-120,0 Q-250,-100 -200,-300" fill="none" stroke="#C62828" stroke-width="4" stroke-dasharray="5 5"/>
            <circle cx="-200" cy="-300" r="80" fill="#B71C1C" opacity="0.9"/>
            <text x="-200" y="-290" text-anchor="middle" font-family="'Vazirmatn'" font-size="24" font-weight="900" fill="white">تهدید امنیتی</text>
        </g>
        
        <!-- Converging Arrows inwards -->
        <path d="M220,-200 L140,-130" stroke="#B71C1C" stroke-width="4" marker-end="url(#arrowhead)"/>
        <path d="M140,220 L70,120" stroke="#B71C1C" stroke-width="4" marker-end="url(#arrowhead)"/>
        <path d="M-220,140 L-130,70" stroke="#B71C1C" stroke-width="4" marker-end="url(#arrowhead)"/>
    </g>

    <defs>
        <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">
            <polygon points="0 0, 10 3.5, 0 7" fill="#B71C1C" />
        </marker>
    </defs>

    <!-- Bottom Message -->
    <rect x="100" y="1150" width="880" height="120" rx="20" fill="rgba(183,28,28,0.1)" stroke="#B71C1C"/>
    <foreignObject x="120" y="1170" width="840" height="80">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn'; color: #EF5350; font-size: 24px; text-align: center; line-height: 1.6;">
            وقتی بحران‌ها به هم گره می‌خورند، اصلاحاتِ جزئی دیگر کارساز نیست.<br/>نیاز به یک <strong style="color: white;">تغییر پارادایم</strong> است.
        </div>
    </foreignObject>

    <!-- Slide ID -->
    <circle cx="1020" cy="1300" r="30" fill="#B71C1C"/>
    <text x="1020" y="1310" text-anchor="middle" font-family="'Vazirmatn', sans-serif" font-size="24" font-weight="bold" fill="white">۱۱</text>
    </svg>
    '''
    full_path = os.path.join(output_dir, filename)
    with open(full_path, 'wb') as f:
        f.write(svg.encode('utf-8'))
    print(f"Generated deadlock spiral slide at: {full_path}")

def create_window_opportunity_slide(filename, chapter_title):
    svg = f'''<svg width="1080" height="1350" viewBox="0 0 1080 1350" xmlns="http://www.w3.org/2000/svg">
    <rect width="1080" height="1350" fill="#ffffff"/>
    
    <!-- Background Gradient -->
    <defs>
        <linearGradient id="skyGrad" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" style="stop-color:#E3F2FD"/>
            <stop offset="100%" style="stop-color:#BBDEFB"/>
        </linearGradient>
    </defs>
    <rect width="1080" height="1350" fill="url(#skyGrad)"/>

    <!-- Header -->
    <rect x="0" y="0" width="1080" height="100" fill="#1976D2"/>
    <foreignObject x="0" y="0" width="1080" height="100">
        <div xmlns="http://www.w3.org/1999/xhtml" style="width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; font-family: 'Vazirmatn', sans-serif; font-size: 36px; font-weight: 800; color: white; direction: rtl;">
            {chapter_title}
        </div>
    </foreignObject>

    <text x="540" y="220" text-anchor="middle" font-family="'Vazirmatn'" font-size="52" font-weight="900" fill="#0D47A1">پنجره فرصت: همگرایی نیروها</text>

    <!-- The Window Visual -->
    <g transform="translate(140, 350)">
        <!-- Window Frame -->
        <rect width="800" height="600" fill="white" stroke="#1976D2" stroke-width="20" rx="10"/>
        <line x1="400" y1="0" x2="400" y2="600" stroke="#1976D2" stroke-width="10"/>
        <line x1="0" y1="300" x2="800" y2="300" stroke="#1976D2" stroke-width="10"/>
        
        <!-- Quadrant 1: Youth -->
        <foreignObject x="40" y="40" width="320" height="220">
            <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn'; color: #0D47A1; text-align: center;">
                <div style="font-size: 80px;">🎓</div>
                <div style="font-size: 28px; font-weight: 900;">نسل جدید</div>
                <div style="font-size: 18px;">آگاه، جهانی و مطالبه‌گر</div>
            </div>
        </foreignObject>

        <!-- Quadrant 2: Civil Society -->
        <foreignObject x="440" y="40" width="320" height="220">
            <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn'; color: #0D47A1; text-align: center;">
                <div style="font-size: 80px;">🤝</div>
                <div style="font-size: 28px; font-weight: 900;">جامعه مدنی</div>
                <div style="font-size: 18px;">شبکه‌های همبستگی پنهان</div>
            </div>
        </foreignObject>

        <!-- Quadrant 3: Tech -->
        <foreignObject x="40" y="340" width="320" height="220">
            <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn'; color: #0D47A1; text-align: center;">
                <div style="font-size: 80px;">📱</div>
                <div style="font-size: 28px; font-weight: 900;">انقلاب دیجیتال</div>
                <div style="font-size: 18px;">شکستن انحصارِ روایت</div>
            </div>
        </foreignObject>

        <!-- Quadrant 4: Global -->
        <foreignObject x="440" y="340" width="320" height="220">
            <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn'; color: #0D47A1; text-align: center;">
                <div style="font-size: 80px;">🌍</div>
                <div style="font-size: 28px; font-weight: 900;">ژئوپلیتیک</div>
                <div style="font-size: 18px;">نیاز جهان به ثبات ایران</div>
            </div>
        </foreignObject>
    </g>

    <!-- Sunlight Ray behind the window -->
    <path d="M540,1350 L140,350 L940,350 Z" fill="#FFD600" opacity="0.1"/>

    <foreignObject x="100" y="1050" width="880" height="150">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn'; color: #1565C0; font-size: 26px; text-align: center; line-height: 1.6; font-weight: 700;">
            این پنجره تا ابد باز نمی‌ماند.<br/>هر تأخیر، هزینه‌ی گذار را به صورت تصاعدی بالا می‌برد.
        </div>
    </foreignObject>

    <!-- Slide ID -->
    <circle cx="1020" cy="1300" r="30" fill="#1976D2"/>
    <text x="1020" y="1310" text-anchor="middle" font-family="'Vazirmatn', sans-serif" font-size="24" font-weight="bold" fill="white">۱۲</text>
    </svg>
    '''
    full_path = os.path.join(output_dir, filename)
    with open(full_path, 'wb') as f:
        f.write(svg.encode('utf-8'))
    print(f"Generated opportunity window slide at: {full_path}")

if __name__ == "__main__":
    create_deadlock_spiral_slide('ch01_creative_1.svg', 'فصل ۱: مقدمه — چرا این کتاب؟')
    create_window_opportunity_slide('ch01_creative_2.svg', 'فصل ۱: مقدمه — چرا این کتاب؟')
