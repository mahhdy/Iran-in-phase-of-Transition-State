import os

output_dir = r'd:\Code\Books\Transition for Iran\00- Iran in phase of Transition State\images\slides'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def create_creative_hexagon_slide(filename, chapter_title):
    svg = f'''<svg width="1080" height="1350" viewBox="0 0 1080 1350" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="bgGrad" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" style="stop-color:#1A1A2E"/>
            <stop offset="100%" style="stop-color:#0D0D1A"/>
        </linearGradient>
        <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
            <feGaussianBlur stdDeviation="5" result="blur" />
            <feComposite in="SourceGraphic" in2="blur" operator="over" />
        </filter>
    </defs>

    <!-- Background -->
    <rect width="1080" height="1350" fill="url(#bgGrad)"/>
    
    <!-- Header -->
    <rect x="0" y="0" width="1080" height="120" fill="#E65100"/>
    <foreignObject x="0" y="0" width="1080" height="120">
        <div xmlns="http://www.w3.org/1999/xhtml" style="width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; font-family: 'Vazirmatn', sans-serif; font-size: 38px; font-weight: 800; color: white; direction: rtl;">
            {chapter_title}
        </div>
    </foreignObject>

    <!-- Main Question / Hook -->
    <foreignObject x="60" y="160" width="960" height="120">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn', sans-serif; color: #FFCC80; font-size: 52px; font-weight: 900; text-align: center; line-height: 1.2;">
            چرا بحران‌های ما حل نمی‌شوند؟
        </div>
    </foreignObject>

    <!-- Hexagon INFOGRAPHIC -->
    <g transform="translate(540, 750)">
        <!-- Connecting Threads (Systemic Network) -->
        <circle r="300" fill="none" stroke="#2E7D32" stroke-width="1" opacity="0.3" stroke-dasharray="10,5"/>
        <line x1="0" y1="-300" x2="0" y2="300" stroke="#FF7043" stroke-width="2" opacity="0.2"/>
        <line x1="-260" y1="-150" x2="260" y2="150" stroke="#FF7043" stroke-width="2" opacity="0.2"/>
        <line x1="-260" y1="150" x2="260" y2="-150" stroke="#FF7043" stroke-width="2" opacity="0.2"/>

        <!-- Central Node -->
        <circle r="120" fill="#E65100" filter="url(#glow)"/>
        <foreignObject x="-100" y="-60" width="200" height="120">
            <div xmlns="http://www.w3.org/1999/xhtml" style="width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; font-family: 'Vazirmatn', sans-serif; font-size: 32px; font-weight: 900; color: white; text-align: center; direction: rtl;">
                بحران<br/>سیستمی
            </div>
        </foreignObject>

        <!-- 6 Crisis Nodes -->
        <!-- 1. Water (Top) -->
        <g transform="translate(0, -380)">
            <rect x="-140" y="-60" width="280" height="120" rx="15" fill="#1565C0" stroke="white" stroke-width="2"/>
            <foreignObject x="-130" y="-50" width="260" height="100">
                <div xmlns="http://www.w3.org/1999/xhtml" style="width:100%; height:100%; display:flex; flex-direction:column; align-items:center; justify-content:center; color:white; font-family:'Vazirmatn'; direction:rtl;">
                    <div style="font-size:24px; font-weight:800;">بحران آب</div>
                    <div style="font-size:16px;">تهدید وجودی</div>
                </div>
            </foreignObject>
        </g>

        <!-- 2. Energy (Right Top) -->
        <g transform="translate(340, -180)">
            <rect x="-130" y="-60" width="260" height="120" rx="15" fill="#F9A825" stroke="white" stroke-width="2"/>
            <foreignObject x="-120" y="-50" width="240" height="100">
                <div xmlns="http://www.w3.org/1999/xhtml" style="width:100%; height:100%; display:flex; flex-direction:column; align-items:center; justify-content:center; color:white; font-family:'Vazirmatn'; direction:rtl;">
                    <div style="font-size:24px; font-weight:800;">بحران انرژی</div>
                    <div style="font-size:16px;">ناترازی و قاچاق</div>
                </div>
            </foreignObject>
        </g>

        <!-- 3. Economy (Right Bottom) -->
        <g transform="translate(340, 180)">
            <rect x="-130" y="-60" width="260" height="120" rx="15" fill="#2E7D32" stroke="white" stroke-width="2"/>
            <foreignObject x="-120" y="-50" width="240" height="100">
                <div xmlns="http://www.w3.org/1999/xhtml" style="width:100%; height:100%; display:flex; flex-direction:column; align-items:center; justify-content:center; color:white; font-family:'Vazirmatn'; direction:rtl;">
                    <div style="font-size:24px; font-weight:800;">بحران اقتصادی</div>
                    <div style="font-size:16px;">تحریم و تورم</div>
                </div>
            </foreignObject>
        </g>

        <!-- 4. Politics (Bottom) -->
        <g transform="translate(0, 380)">
            <rect x="-140" y="-60" width="280" height="120" rx="15" fill="#C62828" stroke="white" stroke-width="2"/>
            <foreignObject x="-130" y="-50" width="260" height="100">
                <div xmlns="http://www.w3.org/1999/xhtml" style="width:100%; height:100%; display:flex; flex-direction:column; align-items:center; justify-content:center; color:white; font-family:'Vazirmatn'; direction:rtl;">
                    <div style="font-size:24px; font-weight:800;">بحران سیاسی</div>
                    <div style="font-size:16px;">فساد و انسداد</div>
                </div>
            </foreignObject>
        </g>

        <!-- 5. Social (Left Bottom) -->
        <g transform="translate(-340, 180)">
            <rect x="-130" y="-60" width="260" height="120" rx="15" fill="#6A1B9A" stroke="white" stroke-width="2"/>
            <foreignObject x="-120" y="-50" width="240" height="100">
                <div xmlns="http://www.w3.org/1999/xhtml" style="width:100%; height:100%; display:flex; flex-direction:column; align-items:center; justify-content:center; color:white; font-family:'Vazirmatn'; direction:rtl;">
                    <div style="font-size:24px; font-weight:800;">بحران اجتماعی</div>
                    <div style="font-size:16px;">گسست و بی‌اعتمادی</div>
                </div>
            </foreignObject>
        </g>

        <!-- 6. Security (Left Top) -->
        <g transform="translate(-340, -180)">
            <rect x="-130" y="-60" width="260" height="120" rx="15" fill="#37474F" stroke="white" stroke-width="2"/>
            <foreignObject x="-120" y="-50" width="240" height="100">
                <div xmlns="http://www.w3.org/1999/xhtml" style="width:100%; height:100%; display:flex; flex-direction:column; align-items:center; justify-content:center; color:white; font-family:'Vazirmatn'; direction:rtl;">
                    <div style="font-size:24px; font-weight:800;">بحران امنیتی</div>
                    <div style="font-size:16px;">انزوای ژئوپلیتیک</div>
                </div>
            </foreignObject>
        </g>
    </g>

    <!-- Bottom Explainer -->
    <rect x="60" y="1150" width="960" height="120" rx="20" fill="rgba(255,255,255,0.05)" stroke="#607D8B" stroke-dasharray="5,5"/>
    <foreignObject x="80" y="1165" width="920" height="90">
        <div xmlns="http://www.w3.org/1999/xhtml" style="font-family: 'Vazirmatn', sans-serif; color: #B0BEC5; font-size: 20px; text-align: center; direction: rtl; line-height: 1.6;">
            این بحران‌ها جدا از هم نیستند؛ آنها در یک <strong style="color: #FF7043;">شبکه علّی</strong> یکدیگر را تشدید می‌کنند. حل هر کدام نیازمند نگاهی سیستمی به کلِ شبکه است.
        </div>
    </foreignObject>

    <!-- Slide ID -->
    <circle cx="1020" cy="1300" r="30" fill="#E65100"/>
    <text x="1020" y="1310" text-anchor="middle" font-family="'Vazirmatn', sans-serif" font-size="24" font-weight="bold" fill="white">۰۲</text>
    </svg>
    '''
    
    full_path = os.path.join(output_dir, filename)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Generated creative slide at: {full_path}")

def create_water_tipping_point_slide(filename, chapter_title):
    svg = f'''<svg width="1080" height="1350" viewBox="0 0 1080 1350" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="bgGrad" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" style="stop-color:#0D0D1A"/>
            <stop offset="100%" style="stop-color:#1B0909"/>
        </linearGradient>
        <filter id="glowRed" x="-20%" y="-20%" width="140%" height="140%">
            <feGaussianBlur stdDeviation="8" result="blur" />
            <feComposite in="SourceGraphic" in2="blur" operator="over" />
        </filter>
    </defs>

    <rect width="1080" height="1350" fill="url(#bgGrad)"/>
    
    <!-- Header -->
    <rect x="0" y="0" width="1080" height="100" fill="#B71C1C"/>
    <foreignObject x="0" y="0" width="1080" height="100">
        <div xmlns="http://www.w3.org/1999/xhtml" style="width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; font-family: 'Vazirmatn', sans-serif; font-size: 36px; font-weight: 800; color: white; direction: rtl;">
            بحران آب: تهدید وجودی
        </div>
    </foreignObject>

    <!-- Main Gauge Graphic -->
    <g transform="translate(540, 450)">
        <!-- Gauge Background -->
        <path d="M-300,0 A300,300 0 0,1 300,0" fill="none" stroke="#333" stroke-width="60" stroke-linecap="round"/>
        <!-- Warning Zone -->
        <path d="M100,-282 A300,300 0 0,1 300,0" fill="none" stroke="#FF5252" stroke-width="60" stroke-linecap="round" opacity="0.4"/>
        <!-- Progress -->
        <path d="M-300,0 A300,300 0 0,1 250,-165" fill="none" stroke="#B71C1C" stroke-width="60" stroke-linecap="round" filter="url(#glowRed)"/>
        
        <text y="80" text-anchor="middle" font-family="'Vazirmatn'" font-size="60" font-weight="900" fill="#FF5252">نقطه بی‌بازگشت</text>
        <text y="140" text-anchor="middle" font-family="'Vazirmatn'" font-size="24" fill="#B0BEC5" direction="rtl">ما در حال نزدیک شدن به فاز فروپاشی هستیم</text>
    </g>

    <!-- Consequences Grid -->
    <g transform="translate(60, 650)">
        <rect width="960" height="480" rx="30" fill="rgba(255,255,255,0.03)" stroke="#333"/>
        <text x="920" y="60" text-anchor="end" font-family="'Vazirmatn'" font-size="32" font-weight="900" fill="#FFB74D" direction="rtl">پیامدها تا سال ۲۰۴۰ (بدون تغییر روند):</text>
        
        <g transform="translate(40, 100)">
            <!-- Item 1 -->
            <circle cx="880" cy="40" r="10" fill="#B71C1C"/>
            <foreignObject x="40" y="15" width="820" height="60">
                <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn'; color: white; font-size: 24px;">
                    ۳۰ تا ۵۰ میلیون نفر <strong style="color:#FF5252">مهاجرت اجباری</strong> داخلی
                </div>
            </foreignObject>

            <!-- Item 2 -->
            <circle cx="880" cy="120" r="10" fill="#B71C1C"/>
            <foreignObject x="40" y="95" width="820" height="60">
                <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn'; color: white; font-size: 24px;">
                    نابودی <strong style="color:#FF5252">۷۰٪ اراضی کشاورزی</strong> کشور
                </div>
            </foreignObject>

            <!-- Item 3 -->
            <circle cx="880" cy="200" r="10" fill="#B71C1C"/>
            <foreignObject x="40" y="175" width="820" height="60">
                <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn'; color: white; font-size: 24px;">
                    غیرقابل سکونت شدن <strong style="color:#FF5252">۱۵ تا ۲۰ استان</strong> ایران
                </div>
            </foreignObject>

            <!-- Item 4 -->
            <circle cx="880" cy="280" r="10" fill="#B71C1C"/>
            <foreignObject x="40" y="255" width="820" height="60">
                <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn'; color: white; font-size: 24px;">
                    خسارت اقتصادی سالانه <strong style="color:#FF5252">۵۰+ میلیارد دلار</strong>
                </div>
            </foreignObject>
        </g>
    </g>

    <!-- Call to action -->
    <rect x="240" y="1180" width="600" height="80" rx="40" fill="#B71C1C"/>
    <text x="540" y="1230" text-anchor="middle" font-family="'Vazirmatn'" font-size="28" font-weight="900" fill="white">فرصت برای اقدام «همین حالا» است</text>

    <!-- Slide ID -->
    <circle cx="1020" cy="1300" r="30" fill="#B71C1C"/>
    <text x="1020" y="1310" text-anchor="middle" font-family="'Vazirmatn', sans-serif" font-size="24" font-weight="bold" fill="white">۰۳</text>
    </svg>
    '''
    full_path = os.path.join(output_dir, filename)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Generated creative water slide at: {full_path}")

def create_legitimacy_gap_slide(filename, chapter_title):
    svg = f'''<svg width="1080" height="1350" viewBox="0 0 1080 1350" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="bgGrad" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" style="stop-color:#1A1A2E"/>
            <stop offset="100%" style="stop-color:#16213E"/>
        </linearGradient>
    </defs>

    <rect width="1080" height="1350" fill="url(#bgGrad)"/>
    
    <!-- Header -->
    <rect x="0" y="0" width="1080" height="100" fill="#3949AB"/>
    <foreignObject x="0" y="0" width="1080" height="100">
        <div xmlns="http://www.w3.org/1999/xhtml" style="width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; font-family: 'Vazirmatn', sans-serif; font-size: 36px; font-weight: 800; color: white; direction: rtl;">
            بحران سیاسی: انسداد و گسست
        </div>
    </foreignObject>

    <!-- Visual: The Gap -->
    <g transform="translate(0, 300)">
        <!-- State Side -->
        <path d="M0,400 L400,400 L450,200 L0,200 Z" fill="#303F9F" opacity="0.8"/>
        <text x="200" y="320" text-anchor="middle" font-family="'Vazirmatn'" font-size="48" font-weight="900" fill="white">حاکمیت</text>
        
        <!-- Society Side -->
        <path d="M1080,400 L680,400 L630,600 L1080,600 Z" fill="#00897B" opacity="0.8"/>
        <text x="880" y="520" text-anchor="middle" font-family="'Vazirmatn'" font-size="48" font-weight="900" fill="white">جامعه</text>

        <!-- The Crack/Gap -->
        <path d="M400,400 L680,400 L640,1000 L360,1000 Z" fill="rgba(0,0,0,0.5)"/>
        <text x="540" y="700" text-anchor="middle" font-family="'Vazirmatn'" font-size="64" font-weight="900" fill="#FF5252" transform="rotate(-15 540 700)">گسست مشروعیت</text>
        
        <!-- Lightning Boltz -->
        <path d="M500,350 L580,450 L520,450 L600,600" fill="none" stroke="#FFD700" stroke-width="4"/>
    </g>

    <!-- Breakdown Details -->
    <g transform="translate(60, 950)">
        <!-- Box 1 -->
        <rect x="0" y="0" width="450" height="180" rx="20" fill="rgba(255,255,255,0.05)" stroke="#3949AB"/>
        <foreignObject x="20" y="20" width="410" height="140">
            <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn'; color: white; font-size: 20px; text-align: center;">
                <strong style="color: #9FA8DA;">بحران کارآمدی</strong><br/>
                ناتوانی در حل مسائل روزمره<br/>
                فساد سیستماتیک و رانت‌خواری
            </div>
        </foreignObject>

        <!-- Box 2 -->
        <rect x="510" y="0" width="450" height="180" rx="20" fill="rgba(255,255,255,0.05)" stroke="#00897B"/>
        <foreignObject x="530" y="20" width="410" height="140">
            <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn'; color: white; font-size: 20px; text-align: center;">
                <strong style="color: #80CBC4;">بحران بازنمایی</strong><br/>
                انسداد مجاری مشارکت<br/>
                سرکوب جامعه مدنی و احزاب
            </div>
        </foreignObject>
    </g>

    <!-- Slide ID -->
    <circle cx="1020" cy="1300" r="30" fill="#3949AB"/>
    <text x="1020" y="1310" text-anchor="middle" font-family="'Vazirmatn', sans-serif" font-size="24" font-weight="bold" fill="white">۰۴</text>
    </svg>
    '''
    full_path = os.path.join(output_dir, filename)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Generated creative legacy gap slide at: {full_path}")

if __name__ == "__main__":
    create_creative_hexagon_slide('ch02_creative_1.svg', 'فصل ۲: تحلیل وضعیت موجود (تشخیص)')
    create_water_tipping_point_slide('ch02_creative_2.svg', 'فصل ۲: تحلیل وضعیت موجود (تشخیص)')
    create_legitimacy_gap_slide('ch02_creative_3.svg', 'فصل ۲: تحلیل وضعیت موجود (تشخیص)')
