import os

output_dir = r'd:\Code\Books\Transition for Iran\00- Iran in phase of Transition State\images\slides'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def create_timeline_slide(filename, chapter_title):
    svg = f'''<svg width="1080" height="1350" viewBox="0 0 1080 1350" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#0F2027"/>
            <stop offset="50%" style="stop-color:#203A43"/>
            <stop offset="100%" style="stop-color:#2C5364"/>
        </linearGradient>
    </defs>

    <!-- Background -->
    <rect width="1080" height="1350" fill="url(#bgGrad)"/>
    
    <!-- Header -->
    <rect x="0" y="0" width="1080" height="100" fill="#37474F"/>
    <foreignObject x="0" y="0" width="1080" height="100">
        <div xmlns="http://www.w3.org/1999/xhtml" style="width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; font-family: 'Vazirmatn', sans-serif; font-size: 36px; font-weight: 800; color: white; direction: rtl;">
            {chapter_title}
        </div>
    </foreignObject>

    <!-- Main Title -->
    <foreignObject x="60" y="140" width="960" height="120">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn', sans-serif; color: #4FC3F7; font-size: 52px; font-weight: 900; text-align: center;">
            خط زمانی ۲۵ ساله: از بحران تا کمال
        </div>
    </foreignObject>

    <!-- Timeline Path (Vertical/Stepped) -->
    <g transform="translate(100, 300)">
        <!-- The Line -->
        <path d="M50,0 L50,850" stroke="#4FC3F7" stroke-width="4" stroke-dasharray="10 5" opacity="0.5"/>
        
        <!-- Phase 1: Transition -->
        <g transform="translate(0, 50)">
            <circle cx="50" cy="0" r="15" fill="#C62828"/>
            <rect x="80" y="-40" width="800" height="120" rx="20" fill="rgba(198,40,40,0.15)" stroke="#C62828"/>
            <foreignObject x="100" y="-30" width="760" height="100">
                <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn'; color: white;">
                    <strong style="color: #FF5252; font-size: 24px;">فاز ۱: گذار (۲ سال)</strong><br/>
                    تشکیل دولت موقت، تدوین قانون اساسی و ثبات اولیه
                </div>
            </foreignObject>
        </g>

        <!-- Phase 2: Building -->
        <g transform="translate(0, 220)">
            <circle cx="50" cy="0" r="15" fill="#2E7D32"/>
            <rect x="80" y="-40" width="800" height="120" rx="20" fill="rgba(46,125,50,0.15)" stroke="#2E7D32"/>
            <foreignObject x="100" y="-30" width="760" height="100">
                <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn'; color: white;">
                    <strong style="color: #66BB6A; font-size: 24px;">فاز ۲: نهادسازی (۳ سال)</strong><br/>
                    استقرار نظام فدرال، استقلال قضایی و اصلاحات ساختاری
                </div>
            </foreignObject>
        </g>

        <!-- Phase 3: Consolidation -->
        <g transform="translate(0, 390)">
            <circle cx="50" cy="0" r="15" fill="#F9A825"/>
            <rect x="80" y="-40" width="800" height="120" rx="20" fill="rgba(249,168,37,0.15)" stroke="#F9A825"/>
            <foreignObject x="100" y="-30" width="760" height="100">
                <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn'; color: white;">
                    <strong style="color: #FFD54F; font-size: 24px;">فاز ۳: تحکیم (۵ سال)</strong><br/>
                    آشتی ملی، کاهش ۵۰ درصدی فقر و چرخش مسالمت‌آمیز قدرت
                </div>
            </foreignObject>
        </g>

        <!-- Phase 4: Maturity -->
        <g transform="translate(0, 560)">
            <circle cx="50" cy="0" r="15" fill="#1565C0"/>
            <rect x="80" y="-40" width="800" height="120" rx="20" fill="rgba(21,101,192,0.15)" stroke="#1565C0"/>
            <foreignObject x="100" y="-30" width="760" height="100">
                <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn'; color: white;">
                    <strong style="color: #64B5F6; font-size: 24px;">فاز ۴: بلوغ (۱۰ سال)</strong><br/>
                    توسعه هوشمند، درآمد متوسط بالا و رهبری منطقه‌ای
                </div>
            </foreignObject>
        </g>

        <!-- Phase 5: Excellence -->
        <g transform="translate(0, 730)">
            <circle cx="50" cy="0" r="15" fill="#6A1B9A"/>
            <rect x="80" y="-40" width="800" height="120" rx="20" fill="rgba(106,27,154,0.15)" stroke="#6A1B9A"/>
            <foreignObject x="100" y="-30" width="760" height="100">
                <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn'; color: white;">
                    <strong style="color: #BA68C8; font-size: 24px;">فاز ۵: تعالی (۵ سال)</strong><br/>
                    اقتصاد دانش‌بنیان، توازن زیست‌محیطی و الگوی جهانی دموکراسی
                </div>
            </foreignObject>
        </g>
    </g>

    <!-- Final Destination Label -->
    <rect x="340" y="1180" width="400" height="60" rx="30" fill="#4FC3F7"/>
    <text x="540" y="1220" text-anchor="middle" font-family="'Vazirmatn'" font-size="28" font-weight="900" fill="#0F2027">ایران ۱۴۳۰: سربلند و آزاد</text>

    <!-- Slide ID -->
    <circle cx="1020" cy="1300" r="30" fill="#37474F"/>
    <text x="1020" y="1310" text-anchor="middle" font-family="'Vazirmatn', sans-serif" font-size="24" font-weight="bold" fill="white">۰۱</text>
    </svg>
    '''
    full_path = os.path.join(output_dir, filename)
    with open(full_path, 'wb') as f:
        f.write(svg.encode('utf-8'))
    print(f"Generated timeline slide at: {full_path}")

def create_cycle_slide(filename, chapter_title):
    svg = f'''<svg width="1080" height="1350" viewBox="0 0 1080 1350" xmlns="http://www.w3.org/2000/svg">
    <rect width="1080" height="1350" fill="#FCFCFC"/>
    
    <!-- Top Half: Virtuous Cycle -->
    <g transform="translate(540, 350)">
        <text y="-250" text-anchor="middle" font-family="'Vazirmatn'" font-size="44" font-weight="900" fill="#00796B">چرخه فاضل (سناریوی گذار)</text>
        <rect x="-150" y="-40" width="300" height="80" rx="10" fill="#E0F2F2" stroke="#00897B" stroke-width="2"/>
        <text text-anchor="middle" y="10" font-family="'Vazirmatn'" font-size="28" font-weight="900" fill="#004D40">آبادانی ملموس</text>
        <path d="M160,0 A160,160 0 1,1 -160,0 A160,160 0 1,1 160,0" fill="none" stroke="#26A69A" stroke-width="6" stroke-dasharray="10 5"/>
        <circle cx="160" cy="0" r="10" fill="#26A69A"/>
        <foreignObject x="180" y="-40" width="200" height="80"><div xmlns="http://www.w3.org/1999/xhtml" style="font-family:'Vazirmatn'; font-size:20px; color:#00695C; font-weight:700; direction:rtl;">اعتماد عمومی</div></foreignObject>
        <circle cx="0" cy="160" r="10" fill="#26A69A"/>
        <foreignObject x="-100" y="180" width="200" height="80"><div xmlns="http://www.w3.org/1999/xhtml" style="font-family:'Vazirmatn'; font-size:20px; color:#00695C; font-weight:700; text-align:center;">ثبات سیاسی</div></foreignObject>
        <circle cx="-160" cy="0" r="10" fill="#26A69A"/>
        <foreignObject x="-380" y="-40" width="200" height="80"><div xmlns="http://www.w3.org/1999/xhtml" style="font-family:'Vazirmatn'; font-size:20px; color:#00695C; font-weight:700;">تحکیم دموکراسی</div></foreignObject>
    </g>

    <line x1="100" y1="675" x2="980" y2="675" stroke="#EEE" stroke-width="10" stroke-linecap="round"/>

    <g transform="translate(540, 1030)">
        <text y="-250" text-anchor="middle" font-family="'Vazirmatn'" font-size="44" font-weight="900" fill="#C62828">چرخه باطل (وضع موجود)</text>
        <rect x="-150" y="-40" width="300" height="80" rx="10" fill="#FFEBEE" stroke="#C62828" stroke-width="2"/>
        <text text-anchor="middle" y="10" font-family="'Vazirmatn'" font-size="28" font-weight="900" fill="#B71C1C">بحران معیشت</text>
        <path d="M160,0 A160,160 0 1,1 -160,0 A160,160 0 1,1 160,0" fill="none" stroke="#EF5350" stroke-width="6" stroke-dasharray="10 5"/>
        <circle cx="160" cy="0" r="10" fill="#EF5350"/>
        <foreignObject x="180" y="-40" width="200" height="80"><div xmlns="http://www.w3.org/1999/xhtml" style="font-family:'Vazirmatn'; font-size:20px; color:#B71C1C; font-weight:700; direction:rtl;">نارضایتی</div></foreignObject>
        <circle cx="0" cy="160" r="10" fill="#EF5350"/>
        <foreignObject x="-100" y="180" width="200" height="80"><div xmlns="http://www.w3.org/1999/xhtml" style="font-family:'Vazirmatn'; font-size:20px; color:#B71C1C; font-weight:700; text-align:center;">بی‌ثباتی / سرکوب</div></foreignObject>
        <circle cx="-160" cy="0" r="10" fill="#EF5350"/>
        <foreignObject x="-380" y="-40" width="200" height="80"><div xmlns="http://www.w3.org/1999/xhtml" style="font-family:'Vazirmatn'; font-size:20px; color:#B71C1C; font-weight:700;">انسداد سیاسی</div></foreignObject>
    </g>
    </svg>
    '''
    full_path = os.path.join(output_dir, filename)
    with open(full_path, 'wb') as f:
        f.write(svg.encode('utf-8'))
    print(f"Generated cycle slide at: {full_path}")

def create_100days_slide(filename, chapter_title):
    svg = f'''<svg width="1080" height="1350" viewBox="0 0 1080 1350" xmlns="http://www.w3.org/2000/svg">
    <rect width="1080" height="1350" fill="#ECEFF1"/>
    <rect x="0" y="0" width="1080" height="100" fill="#FF8F00"/>
    <foreignObject x="0" y="0" width="1080" height="100"><div xmlns="http://www.w3.org/1999/xhtml" style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; font-family:'Vazirmatn'; font-size:36px; font-weight:800; color:white; direction:rtl;">{chapter_title}</div></foreignObject>
    <text x="540" y="180" text-anchor="middle" font-family="'Vazirmatn'" font-size="48" font-weight="900" fill="#E65100">۱۰ اقدام فوری در ۱۰۰ روز اول</text>
    <g transform="translate(60, 250)">
        {"".join([f'<rect x="{(i%2)*510}" y="{(i//2)*180}" width="450" height="160" rx="20" fill="white" stroke="#FF8F00"/><circle cx="{(i%2)*510 + (450 if i%2==0 else 0)}" cy="{(i//2)*180 + 80}" r="30" fill="#FF8F00"/><text x="{(i%2)*510 + (450 if i%2==0 else 0)}" y="{(i//2)*180 + 90}" text-anchor="middle" font-family="Vazirmatn" font-size="28" font-weight="900" fill="white">{i+1}</text>' for i in range(10)])}
        <foreignObject x="20" y="20" width="400" height="100"><div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn; font-size:22px; color:#263238;"><strong>دولت موقت فراگیر</strong></div></foreignObject>
        <foreignObject x="530" y="20" width="400" height="100"><div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn; font-size:22px; color:#263238;"><strong>آتش‌بس سیاسی</strong></div></foreignObject>
        <foreignObject x="20" y="200" width="400" height="100"><div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn; font-size:22px; color:#263238;"><strong>آزادی زندانیان</strong></div></foreignObject>
        <foreignObject x="530" y="200" width="400" height="100"><div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn; font-size:22px; color:#263238;"><strong>بسته معیشتی</strong></div></foreignObject>
        <foreignObject x="20" y="380" width="400" height="100"><div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn; font-size:22px; color:#263238;"><strong>برنامه آب اضطراری</strong></div></foreignObject>
        <foreignObject x="530" y="380" width="400" height="100"><div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn; font-size:22px; color:#263238;"><strong>کنترل قاچاق سوخت</strong></div></foreignObject>
        <foreignObject x="20" y="560" width="400" height="100"><div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn; font-size:22px; color:#263238;"><strong>محاکمه مفسدان</strong></div></foreignObject>
        <foreignObject x="530" y="560" width="400" height="100"><div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn; font-size:22px; color:#263238;"><strong>آزادی رسانه‌ها</strong></div></foreignObject>
        <foreignObject x="20" y="740" width="400" height="100"><div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn; font-size:22px; color:#263238;"><strong>اعلان انتخابات</strong></div></foreignObject>
        <foreignObject x="530" y="740" width="400" height="100"><div xmlns="http://www.w3.org/1999/xhtml" style="direction:rtl; font-family:Vazirmatn; font-size:22px; color:#263238;"><strong>مذاکره تحریم</strong></div></foreignObject>
    </g>
    </svg>
    '''
    full_path = os.path.join(output_dir, filename)
    with open(full_path, 'wb') as f:
        f.write(svg.encode('utf-8'))
    print(f"Generated sprint slide at: {full_path}")

def create_vision_pillars_slide(filename, chapter_title):
    svg = f'''<svg width="1080" height="1350" viewBox="0 0 1080 1350" xmlns="http://www.w3.org/2000/svg">
    <rect width="1080" height="1350" fill="#20232A"/>
    <rect x="0" y="0" width="1080" height="100" fill="#61DAFB"/>
    <foreignObject x="0" y="0" width="1080" height="100"><div xmlns="http://www.w3.org/1999/xhtml" style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; font-family:'Vazirmatn'; font-size:36px; font-weight:800; color:#20232A; direction:rtl;">{chapter_title}</div></foreignObject>
    <text x="540" y="180" text-anchor="middle" font-family="'Vazirmatn'" font-size="56" font-weight="900" fill="white">ستون‌های ایران ۱۴۳۰</text>
    <g transform="translate(90, 350)">
        {"".join([f'<rect width="150" height="600" x="{i*185 + 15}" fill="{["#3F51B5","#009688","#FF9800","#4CAF50","#673AB7"][i]}" opacity="0.8"/><rect width="180" height="40" x="{i*185}" y="-40" fill="{["#3F51B5","#009688","#FF9800","#4CAF50","#673AB7"][i]}"/><rect width="180" height="40" x="{i*185}" y="600" fill="{["#3F51B5","#009688","#FF9800","#4CAF50","#673AB7"][i]}"/>' for i in range(5)])}
    </g>
    <g transform="translate(90, 1000)">
        <foreignObject x="0" y="0" width="180" height="150"><div xmlns="http://www.w3.org/1999/xhtml" style="font-family:Vazirmatn; color:white; text-align:center; font-size:20px; direction:rtl;"><strong>سیاسی</strong><br/>دموکراسی آزاد</div></foreignObject>
        <foreignObject x="185" y="0" width="180" height="150"><div xmlns="http://www.w3.org/1999/xhtml" style="font-family:Vazirmatn; color:white; text-align:center; font-size:20px; direction:rtl;"><strong>اقتصادی</strong><br/>رشد پایدار</div></foreignObject>
        <foreignObject x="370" y="0" width="180" height="150"><div xmlns="http://www.w3.org/1999/xhtml" style="font-family:Vazirmatn; color:white; text-align:center; font-size:20px; direction:rtl;"><strong>اجتماعی</strong><br/>عدالت اجتماعی</div></foreignObject>
        <foreignObject x="555" y="0" width="180" height="150"><div xmlns="http://www.w3.org/1999/xhtml" style="font-family:Vazirmatn; color:white; text-align:center; font-size:20px; direction:rtl;"><strong>محیط زیست</strong><br/>احیای منابع</div></foreignObject>
        <foreignObject x="740" y="0" width="180" height="150"><div xmlns="http://www.w3.org/1999/xhtml" style="font-family:Vazirmatn; color:white; text-align:center; font-size:20px; direction:rtl;"><strong>منطقه‌ای</strong><br/>ثبات و صلح</div></foreignObject>
    </g>
    </svg>
    '''
    full_path = os.path.join(output_dir, filename)
    with open(full_path, 'wb') as f:
        f.write(svg.encode('utf-8'))
    print(f"Generated vision slide at: {full_path}")

if __name__ == "__main__":
    create_timeline_slide('ch00_creative_1.svg', 'خلاصه مدیریتی: از بحران تا بالندگی')
    create_cycle_slide('ch00_creative_2.svg', 'خلاصه مدیریتی: از بحران تا بالندگی')
    create_100days_slide('ch00_creative_3.svg', 'خلاصه مدیریتی: از بحران تا بالندگی')
    create_vision_pillars_slide('ch00_creative_4.svg', 'خلاصه مدیریتی: از بحران تا بالندگی')
