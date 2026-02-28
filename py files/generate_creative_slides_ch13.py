import os

output_dir = r'd:\Code\Books\Transition for Iran\00- Iran in phase of Transition State\images\slides'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def create_economy_ladder_slide(filename, chapter_title):
    svg = f'''<svg width="1080" height="1350" viewBox="0 0 1080 1350" xmlns="http://www.w3.org/2000/svg">
    <rect width="1080" height="1350" fill="#F4F7F6"/>
    
    <!-- Header -->
    <rect x="0" y="0" width="1080" height="100" fill="#006064"/>
    <foreignObject x="0" y="0" width="1080" height="100">
        <div xmlns="http://www.w3.org/1999/xhtml" style="width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; font-family: 'Vazirmatn', sans-serif; font-size: 36px; font-weight: 800; color: white; direction: rtl;">
            {chapter_title}
        </div>
    </foreignObject>

    <text x="540" y="200" text-anchor="middle" font-family="'Vazirmatn'" font-size="52" font-weight="900" fill="#006064">نردبان بازسازی اقتصادی</text>

    <!-- The Ladder -->
    <g transform="translate(140, 300)">
        <!-- Step 3: Prosperity -->
        <g transform="translate(0, 0)">
            <rect width="800" height="200" rx="20" fill="#E0F2F1" stroke="#009688" stroke-width="4"/>
            <text x="760" y="60" text-anchor="end" font-family="'Vazirmatn'" font-size="32" font-weight="900" fill="#004D40">گام ۳: شکوفایی و رقابت (سال ۵ به بعد)</text>
            <foreignObject x="40" y="80" width="720" height="100">
                <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn'; color: #00695C; font-size: 20px;">
                    اقتصاد دانش‌بنیان، صادرات غیرنفتی، حضور در زنجیره ارزش جهانی و رفاه پایدار پایه‌گذاری شده بر تولید.
                </div>
            </foreignObject>
        </g>

        <!-- Connector -->
        <line x1="400" y1="200" x2="400" y2="280" stroke="#009688" stroke-width="8" stroke-dasharray="10 5"/>

        <!-- Step 2: Transition -->
        <g transform="translate(0, 280)">
            <rect width="800" height="200" rx="20" fill="#FFF3E0" stroke="#FF9800" stroke-width="4"/>
            <text x="760" y="60" text-anchor="end" font-family="'Vazirmatn'" font-size="32" font-weight="900" fill="#E65100">گام ۲: آزادسازی و نهادسازی (سال ۱ تا ۵)</text>
            <foreignObject x="40" y="80" width="720" height="100">
                <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn'; color: #BF360C; font-size: 20px;">
                    حذف رانت‌ها، اصلاح نظام بانکی، خصوصی‌سازی واقعی و جذب سرمایه‌گذاری خارجی کلان.
                </div>
            </foreignObject>
        </g>

        <!-- Connector -->
        <line x1="400" y1="480" x2="400" y2="560" stroke="#FF9800" stroke-width="8" stroke-dasharray="10 5"/>

        <!-- Step 1: Survival -->
        <g transform="translate(0, 560)">
            <rect width="800" height="200" rx="20" fill="#FFEBEE" stroke="#C62828" stroke-width="4"/>
            <text x="760" y="60" text-anchor="end" font-family="'Vazirmatn'" font-size="32" font-weight="900" fill="#B71C1C">گام ۱: جراحی اضطراری (۱۰۰ روز تا ۱ سال)</text>
            <foreignObject x="40" y="80" width="720" height="100">
                <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn'; color: #C62828; font-size: 20px;">
                    مهار تورم افسارگسیخته، ثبات‌بخشی به نرخ ارز و توزیع بسته‌های حمایتی معیشتی فوری.
                </div>
            </foreignObject>
        </g>
    </g>

    <!-- Summary Box -->
    <rect x="60" y="1100" width="960" height="160" rx="30" fill="white" stroke="#006064" stroke-width="2" style="filter: drop-shadow(0 5px 15px rgba(0,0,0,0.05))"/>
    <foreignObject x="100" y="1135" width="880" height="100">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn'; color: #263238; font-size: 22px; text-align: center; line-height: 1.6;">
            بدون پیمودن صحیح پله‌های اول، رسیدن به <strong style="color: #00897B;">شکوفایی</strong> غیرممکن است. هر مرحله پیش‌نیاز مرحله بعدی است.
        </div>
    </foreignObject>

    <!-- Slide ID -->
    <circle cx="1020" cy="1300" r="30" fill="#006064"/>
    <text x="1020" y="1310" text-anchor="middle" font-family="'Vazirmatn', sans-serif" font-size="24" font-weight="bold" fill="white">۱۳۱</text>
    </svg>
    '''
    full_path = os.path.join(output_dir, filename)
    with open(full_path, 'wb') as f:
        f.write(svg.encode('utf-8'))
    print(f"Generated economy ladder slide at: {full_path}")

def create_oil_trap_slide(filename, chapter_title):
    svg = f'''<svg width="1080" height="1350" viewBox="0 0 1080 1350" xmlns="http://www.w3.org/2000/svg">
    <rect width="1080" height="1350" fill="#212121"/>
    
    <!-- Header -->
    <rect x="0" y="0" width="1080" height="100" fill="#FFC107"/>
    <foreignObject x="0" y="0" width="1080" height="100">
        <div xmlns="http://www.w3.org/1999/xhtml" style="width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; font-family: 'Vazirmatn', sans-serif; font-size: 36px; font-weight: 800; color: #212121; direction: rtl;">
            {chapter_title}
        </div>
    </foreignObject>

    <text x="540" y="220" text-anchor="middle" font-family="'Vazirmatn'" font-size="52" font-weight="900" fill="white">رهایی از «تله نفت»</text>

    <!-- Infographic: Oil Well to Integrated Circuit -->
    <g transform="translate(540, 650)">
        <!-- The Shift Arrow -->
        <path d="M-400,0 L350,0" stroke="#FFC107" stroke-width="60" stroke-linecap="round"/>
        <path d="M350,0 L420,0 L420,-30 L480,0 L420,30 L420,0 Z" fill="#FFC107"/>
        
        <!-- From: Oil -->
        <g transform="translate(-350, 0)">
            <rect x="-80" y="-200" width="160" height="400" rx="20" fill="rgba(0,0,0,0.8)" stroke="#FFC107"/>
            <text y="-140" text-anchor="middle" font-family="'Vazirmatn'" font-size="32" font-weight="900" fill="#FFC107">وضع موجود</text>
            <text y="0" text-anchor="middle" font-family="'Vazirmatn'" font-size="60">🛢️</text>
            <text y="100" text-anchor="middle" font-family="'Vazirmatn'" font-size="24" fill="white">اقتصاد رانتی</text>
            <text y="140" text-anchor="middle" font-family="'Vazirmatn'" font-size="20" fill="#9E9E9E">بسته و منزوی</text>
        </g>

        <!-- To: Knowledge/Tech -->
        <g transform="translate(300, 0)">
            <rect x="-80" y="-200" width="160" height="400" rx="20" fill="rgba(33,150,243,0.2)" stroke="#2196F3" stroke-width="3"/>
            <text y="-140" text-anchor="middle" font-family="'Vazirmatn'" font-size="32" font-weight="900" fill="#2196F3">آرمان نوین</text>
            <text y="0" text-anchor="middle" font-family="'Vazirmatn'" font-size="60">💻</text>
            <text y="100" text-anchor="middle" font-family="'Vazirmatn'" font-size="24" fill="white">اقتصاد پویا</text>
            <text y="140" text-anchor="middle" font-family="'Vazirmatn'" font-size="20" fill="#9E9E9E">جهانی و خلاق</text>
        </g>
    </g>

    <!-- Key point in the middle of arrow -->
    <rect x="440" y="625" width="200" height="50" rx="25" fill="#FFC107"/>
    <text x="540" y="658" text-anchor="middle" font-family="'Vazirmatn'" font-size="20" font-weight="900" fill="#212121">تحول ساختاری</text>

    <!-- Summary -->
    <foreignObject x="100" y="1050" width="880" height="200">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn'; color: #BDBDBD; font-size: 24px; text-align: center; line-height: 1.8;">
            نفت باید از <strong style="color: white;">ابزار بقای قدرت</strong> به <strong style="color: #FFC107;">موتور محرکِ زیرساخت‌ها</strong> تبدیل شود.<br/>
            ثروت ملی متعلق به نسل‌هاست، نه حاکمان.
        </div>
    </foreignObject>

    <!-- Slide ID -->
    <circle cx="1020" cy="1300" r="30" fill="#FFC107"/>
    <text x="1020" y="1310" text-anchor="middle" font-family="'Vazirmatn', sans-serif" font-size="24" font-weight="bold" fill="#212121">۱۳۲</text>
    </svg>
    '''
    full_path = os.path.join(output_dir, filename)
    with open(full_path, 'wb') as f:
        f.write(svg.encode('utf-8'))
    print(f"Generated oil trap slide at: {full_path}")

if __name__ == "__main__":
    create_economy_ladder_slide('ch13_creative_1.svg', 'فصل ۱۳: بازسازی و توسعه اقتصادی')
    create_oil_trap_slide('ch13_creative_2.svg', 'فصل ۱۳: بازسازی و توسعه اقتصادی')
