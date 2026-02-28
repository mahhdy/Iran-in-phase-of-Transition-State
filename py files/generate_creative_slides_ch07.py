import os

output_dir = r'd:\Code\Books\Transition for Iran\00- Iran in phase of Transition State\images\slides'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def create_compass_slide(filename, chapter_title):
    svg = f'''<svg width="1080" height="1350" viewBox="0 0 1080 1350" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <radialGradient id="compassGrad" cx="50%" cy="50%" r="50%">
            <stop offset="0%" style="stop-color:#FFD700; stop-opacity:0.2" />
            <stop offset="100%" style="stop-color:#000; stop-opacity:0" />
        </radialGradient>
    </defs>
    <rect width="1080" height="1350" fill="#121212"/>
    
    <!-- Background Glow -->
    <circle cx="540" cy="700" r="400" fill="url(#compassGrad)"/>

    <!-- Header -->
    <rect x="0" y="0" width="1080" height="100" fill="#FFC107"/>
    <foreignObject x="0" y="0" width="1080" height="100">
        <div xmlns="http://www.w3.org/1999/xhtml" style="width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; font-family: 'Vazirmatn', sans-serif; font-size: 36px; font-weight: 800; color: #121212; direction: rtl;">
            {chapter_title}
        </div>
    </foreignObject>

    <!-- Main Title -->
    <text x="540" y="200" text-anchor="middle" font-family="'Vazirmatn'" font-size="52" font-weight="900" fill="white">قطب‌نمای ارزش‌های ملی</text>

    <!-- Compass Drawing -->
    <g transform="translate(540, 700)">
        <!-- Outer Circle -->
        <circle r="320" fill="none" stroke="#FFC107" stroke-width="2" opacity="0.3"/>
        <circle r="340" fill="none" stroke="#FFC107" stroke-width="1" stroke-dasharray="5 10"/>
        
        <!-- North: Secularism -->
        <g transform="translate(0, -320)">
            <circle r="80" fill="#1A237E" stroke="#FFC107" stroke-width="3"/>
            <foreignObject x="-70" y="-40" width="140" height="80">
                <div xmlns="http://www.w3.org/1999/xhtml" style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; color:white; font-family:'Vazirmatn'; font-weight:800; font-size:24px; text-align:center;">سکولاریسم</div>
            </foreignObject>
        </g>

        <!-- South: Federalism -->
        <g transform="translate(0, 320)">
            <circle r="80" fill="#1B5E20" stroke="#FFC107" stroke-width="3"/>
            <foreignObject x="-70" y="-40" width="140" height="80">
                <div xmlns="http://www.w3.org/1999/xhtml" style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; color:white; font-family:'Vazirmatn'; font-weight:800; font-size:24px; text-align:center;">فدرالیسم</div>
            </foreignObject>
        </g>

        <!-- East: Democracy -->
        <g transform="translate(320, 0)">
            <circle r="80" fill="#0D47A1" stroke="#FFC107" stroke-width="3"/>
            <foreignObject x="-70" y="-40" width="140" height="80">
                <div xmlns="http://www.w3.org/1999/xhtml" style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; color:white; font-family:'Vazirmatn'; font-weight:800; font-size:24px; text-align:center;">دموکراسی</div>
            </foreignObject>
        </g>

        <!-- West: Social Justice -->
        <g transform="translate(-320, 0)">
            <circle r="80" fill="#B71C1C" stroke="#FFC107" stroke-width="3"/>
            <foreignObject x="-70" y="-40" width="140" height="80">
                <div xmlns="http://www.w3.org/1999/xhtml" style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; color:white; font-family:'Vazirmatn'; font-weight:800; font-size:24px; text-align:center;">عدالت</div>
            </foreignObject>
        </g>

        <!-- Center Star -->
        <polygon points="0,-100 20,-20 100,0 20,20 0,100 -20,20 -100,0 -20,-20" fill="#FFC107" opacity="0.8"/>
        <text y="10" text-anchor="middle" font-family="'Vazirmatn'" font-size="20" font-weight="900" fill="#121212">ایران</text>
    </g>

    <!-- Bottom Note -->
    <foreignObject x="100" y="1150" width="880" height="100">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn'; color: #FFCC80; font-size: 22px; text-align: center; line-height: 1.6;">
            این چهار رکن، تضمین‌کننده ثبات و بقای پیمان پایدار شهروندی در ایران نوین هستند.
        </div>
    </foreignObject>

    <!-- Slide ID -->
    <circle cx="1020" cy="1300" r="30" fill="#FFC107"/>
    <text x="1020" y="1310" text-anchor="middle" font-family="'Vazirmatn', sans-serif" font-size="24" font-weight="bold" fill="#121212">۷۱</text>
    </svg>
    '''
    full_path = os.path.join(output_dir, filename)
    with open(full_path, 'wb') as f:
        f.write(svg.encode('utf-8'))
    print(f"Generated compass slide at: {full_path}")

def create_citizen_transition_slide(filename, chapter_title):
    svg = f'''<svg width="1080" height="1350" viewBox="0 0 1080 1350" xmlns="http://www.w3.org/2000/svg">
    <rect width="1080" height="1350" fill="#F5F5F5"/>
    
    <!-- Background Elements -->
    <path d="M0,600 C300,500 700,700 1080,600 L1080,1350 L0,1350 Z" fill="#E0E0E0" opacity="0.3"/>

    <!-- Header -->
    <rect x="0" y="0" width="1080" height="100" fill="#3F51B5"/>
    <foreignObject x="0" y="0" width="1080" height="100">
        <div xmlns="http://www.w3.org/1999/xhtml" style="width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; font-family: 'Vazirmatn', sans-serif; font-size: 36px; font-weight: 800; color: white; direction: rtl;">
            {chapter_title}
        </div>
    </foreignObject>

    <!-- Title -->
    <text x="540" y="200" text-anchor="middle" font-family="'Vazirmatn'" font-size="52" font-weight="900" fill="#1A237E">از «رعیّت» به «شهروند»</text>

    <!-- The Great Transition Arrow -->
    <g transform="translate(60, 450)">
        <path d="M0,150 L840,150 L840,100 L960,175 L840,250 L840,200 L0,200 Z" fill="#3F51B5"/>
        
        <!-- Left Side: Subject -->
        <g transform="translate(50, 20)">
            <circle cx="0" cy="0" r="100" fill="#BDBDBD"/>
            <text y="15" text-anchor="middle" font-family="'Vazirmatn'" font-size="40" font-weight="900" fill="#424242">رعیّت</text>
            <rect x="-80" y="120" width="160" height="120" rx="10" fill="white" stroke="#BDBDBD"/>
            <foreignObject x="-70" y="130" width="140" height="100">
                <div xmlns="http://www.w3.org/1999/xhtml" style="font-family:'Vazirmatn'; color:#616161; font-size:16px; text-align:center; direction:rtl;">
                    اطاعت کورکورانه<br/>ترس از قدرت<br/>بی‌ارادگی سیاسی
                </div>
            </foreignObject>
        </g>

        <!-- Right Side: Citizen -->
        <g transform="translate(800, 20)">
            <circle cx="0" cy="0" r="100" fill="#FFC107"/>
            <text y="15" text-anchor="middle" font-family="'Vazirmatn'" font-size="40" font-weight="900" fill="#1A237E">شهروند</text>
            <rect x="-80" y="120" width="160" height="120" rx="10" fill="white" stroke="#FFC107"/>
            <foreignObject x="-70" y="130" width="140" height="100">
                <div xmlns="http://www.w3.org/1999/xhtml" style="font-family:'Vazirmatn'; color:#1A237E; font-size:16px; text-align:center; direction:rtl;">
                    مشارکت فعال<br/>حق و مسئولیت<br/>اراده ملی
                </div>
            </foreignObject>
        </g>

        <!-- The Shift (Middle) -->
        <text x="450" y="130" text-anchor="middle" font-family="'Vazirmatn'" font-size="28" font-weight="900" fill="#3F51B5">بلوغ و آگاهی سیاسی</text>
    </g>

    <!-- Summary Box -->
    <rect x="60" y="950" width="960" height="200" rx="30" fill="white" stroke="#3F51B5" stroke-width="2" stroke-dasharray="10 5"/>
    <foreignObject x="100" y="990" width="880" height="140">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn'; color: #1A237E; font-size: 24px; text-align: center; line-height: 1.6;">
            بنیان دموکراسی نه در صندوق رای، بلکه در ذهن شهروندی نهفته است که می‌داند <strong style="color: #FF8F00;">صاحبِ حق</strong> است و در برابر سرنوشت خود <strong style="color: #FF8F00;">مسئول</strong>.
        </div>
    </foreignObject>

    <!-- Slide ID -->
    <circle cx="1020" cy="1300" r="30" fill="#3F51B5"/>
    <text x="1020" y="1310" text-anchor="middle" font-family="'Vazirmatn', sans-serif" font-size="24" font-weight="bold" fill="white">۷۲</text>
    </svg>
    '''
    full_path = os.path.join(output_dir, filename)
    with open(full_path, 'wb') as f:
        f.write(svg.encode('utf-8'))
    print(f"Generated citizen transition slide at: {full_path}")

if __name__ == "__main__":
    create_compass_slide('ch07_creative_1.svg', 'فصل ۷: چشم‌انداز، اصول و میثاق ملی')
    create_citizen_transition_slide('ch07_creative_2.svg', 'فصل ۷: چشم‌انداز، اصول و میثاق ملی')
