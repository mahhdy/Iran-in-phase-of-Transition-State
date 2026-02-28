import os

output_dir = r'd:\Code\Books\Transition for Iran\00- Iran in phase of Transition State\images\slides'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def create_stability_triangle_slide(filename, chapter_title):
    svg = f'''<svg width="1080" height="1350" viewBox="0 0 1080 1350" xmlns="http://www.w3.org/2000/svg">
    <rect width="1080" height="1350" fill="#ECEFF1"/>
    
    <!-- Background Decor -->
    <path d="M0,0 Q540,100 1080,0 L1080,1350 Q540,1250 0,1350 Z" fill="#263238" opacity="0.03"/>

    <!-- Header -->
    <rect x="0" y="0" width="1080" height="100" fill="#0D47A1"/>
    <foreignObject x="0" y="0" width="1080" height="100">
        <div xmlns="http://www.w3.org/1999/xhtml" style="width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; font-family: 'Vazirmatn', sans-serif; font-size: 36px; font-weight: 800; color: white; direction: rtl;">
            {chapter_title}
        </div>
    </foreignObject>

    <!-- Title -->
    <text x="540" y="200" text-anchor="middle" font-family="'Vazirmatn'" font-size="52" font-weight="900" fill="#01579B">مثلث ثبات در ۲۴ ماه اول</text>

    <!-- The Triangle -->
    <g transform="translate(540, 650)">
        <!-- Sides -->
        <path d="M0,-350 L300,170 L-300,170 Z" fill="none" stroke="#01579B" stroke-width="15" stroke-linejoin="round"/>
        
        <!-- Nodes -->
        <!-- Peak: Security (Order) -->
        <circle cx="0" cy="-350" r="120" fill="#B71C1C" stroke="white" stroke-width="5"/>
        <foreignObject x="-100" y="-410" width="200" height="120">
            <div xmlns="http://www.w3.org/1999/xhtml" style="width:100%; height:100%; display:flex; flex-direction:column; align-items:center; justify-content:center; color:white; font-family:'Vazirmatn'; text-align:center; direction:rtl;">
                <div style="font-size:32px; font-weight:900;">امنیت</div>
                <div style="font-size:16px;">حفظ نظم و مرزها</div>
            </div>
        </foreignObject>

        <!-- Bottom Right: Economy (Livelihood) -->
        <circle cx="300" cy="170" r="120" fill="#1B5E20" stroke="white" stroke-width="5"/>
        <foreignObject x="200" y="110" width="200" height="120">
            <div xmlns="http://www.w3.org/1999/xhtml" style="width:100%; height:100%; display:flex; flex-direction:column; align-items:center; justify-content:center; color:white; font-family:'Vazirmatn'; text-align:center; direction:rtl;">
                <div style="font-size:32px; font-weight:900;">معیشت</div>
                <div style="font-size:16px;">رفاه ملموس و فوری</div>
            </div>
        </foreignObject>

        <!-- Bottom Left: Legitimacy (Accord) -->
        <circle cx="-300" cy="170" r="120" fill="#F9A825" stroke="white" stroke-width="5"/>
        <foreignObject x="-400" y="110" width="200" height="120">
            <div xmlns="http://www.w3.org/1999/xhtml" style="width:100%; height:100%; display:flex; flex-direction:column; align-items:center; justify-content:center; color:white; font-family:'Vazirmatn'; text-align:center; direction:rtl;">
                <div style="font-size:32px; font-weight:900;">مشروعیت</div>
                <div style="font-size:16px;">وفاق و قانون‌گرایی</div>
            </div>
        </foreignObject>

        <!-- Center Message -->
        <text y="0" text-anchor="middle" font-family="'Vazirmatn'" font-size="28" font-weight="900" fill="#01579B">تعادل حیاتی</text>
    </g>

    <!-- Explanation Box -->
    <rect x="60" y="1050" width="960" height="150" rx="30" fill="white" stroke="#01579B" stroke-width="2"/>
    <foreignObject x="100" y="1080" width="880" height="100">
        <div xmlns="http://www.w3.org/1999/xhtml" style="direction: rtl; font-family: 'Vazirmatn'; color: #263238; font-size: 22px; text-align: center; line-height: 1.6;">
            شکست در هر یک از این سه ضلع، کل فرآیند گذار را با خطر <strong style="color: #B71C1C;">فروپاشی</strong> یا <strong style="color: #B71C1C;">بازگشت استبداد</strong> مواجه می‌کند.
        </div>
    </foreignObject>

    <!-- Slide ID -->
    <circle cx="1020" cy="1300" r="30" fill="#0D47A1"/>
    <text x="1020" y="1310" text-anchor="middle" font-family="'Vazirmatn', sans-serif" font-size="24" font-weight="bold" fill="white">۸۱</text>
    </svg>
    '''
    full_path = os.path.join(output_dir, filename)
    with open(full_path, 'wb') as f:
        f.write(svg.encode('utf-8'))
    print(f"Generated stability triangle slide at: {full_path}")

create_stability_triangle_slide('ch08_creative_1.svg', 'فاز ۱: گذار — تثبیت و استقرار (۰ تا ۲۴ ماه)')
# I'll add the transition bodies slide here too
def create_bodies_slide(filename, chapter_title):
    svg = f'''<svg width="1080" height="1350" viewBox="0 0 1080 1350" xmlns="http://www.w3.org/2000/svg">
    <rect width="1080" height="1350" fill="#F8F9FA"/>
    
    <!-- Header -->
    <rect x="0" y="0" width="1080" height="100" fill="#37474F"/>
    <foreignObject x="0" y="0" width="1080" height="100">
        <div xmlns="http://www.w3.org/1999/xhtml" style="width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; font-family: 'Vazirmatn', sans-serif; font-size: 36px; font-weight: 800; color: white; direction: rtl;">
            {chapter_title}
        </div>
    </foreignObject>

    <text x="540" y="200" text-anchor="middle" font-family="'Vazirmatn'" font-size="52" font-weight="900" fill="#212121">ساختار مدیریت گذار</text>

    <!-- Flowchart -->
    <g transform="translate(540, 350)">
        <!-- Top: Council -->
        <rect x="-300" y="0" width="600" height="120" rx="60" fill="#CFD8DC" stroke="#37474F" stroke-width="4"/>
        <text y="75" text-anchor="middle" font-family="'Vazirmatn'" font-size="36" font-weight="900" fill="#37474F">شورای عالی مدیریت گذار</text>
        <text y="105" text-anchor="middle" font-family="'Vazirmatn'" font-size="16" fill="#546E7A">(مرجع مشروعیت و وفاق ملی)</text>

        <!-- Down Arrow 1 -->
        <line x1="0" y1="120" x2="0" y2="200" stroke="#37474F" stroke-width="4" marker-end="url(#arrowhead)"/>
        
        <!-- Middle Row: Two pillars -->
        <g transform="translate(0, 250)">
            <rect x="-480" y="0" width="440" height="150" rx="30" fill="#E1F5FE" stroke="#0288D1" stroke-width="3"/>
            <text x="-260" y="65" text-anchor="middle" font-family="'Vazirmatn'" font-size="28" font-weight="900" fill="#01579B">دولت موقت (اجرائی)</text>
            <text x="-260" y="100" text-anchor="middle" font-family="'Vazirmatn'" font-size="18" fill="#0288D1">اداره امور و امنیت</text>
            
            <rect x="40" y="0" width="440" height="150" rx="30" fill="#FFF3E0" stroke="#F57C00" stroke-width="3"/>
            <text x="260" y="65" text-anchor="middle" font-family="'Vazirmatn'" font-size="28" font-weight="900" fill="#E65100">مجلس مؤسسان (تقنینی)</text>
            <text x="260" y="100" text-anchor="middle" font-family="'Vazirmatn'" font-size="18" fill="#F57C00">تدوین قانون اساسی جدید</text>
        </g>

        <!-- Down Arrows 2 -->
        <path d="M-260,400 L-260,500" stroke="#37474F" stroke-width="4" fill="none" marker-end="url(#arrowhead)"/>
        <path d="M260,400 L260,500" stroke="#37474F" stroke-width="4" fill="none" marker-end="url(#arrowhead)"/>

        <!-- Final Box -->
        <g transform="translate(0, 550)">
            <rect x="-300" y="0" width="600" height="150" rx="75" fill="#E8F5E9" stroke="#2E7D32" stroke-width="5"/>
            <text y="70" text-anchor="middle" font-family="'Vazirmatn'" font-size="44" font-weight="900" fill="#1B5E20">اولین دولت منتخب</text>
            <text y="110" text-anchor="middle" font-family="'Vazirmatn'" font-size="20" fill="#2E7D32">(پایان فاز گذار و آغاز نهادسازی)</text>
        </g>
    </g>

    <!-- Marker def for arrows -->
    <defs>
        <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">
            <polygon points="0 0, 10 3.5, 0 7" fill="#37474F" />
        </marker>
    </defs>

    <!-- Slide ID -->
    <circle cx="1020" cy="1300" r="30" fill="#37474F"/>
    <text x="1020" y="1310" text-anchor="middle" font-family="'Vazirmatn', sans-serif" font-size="24" font-weight="bold" fill="white">۸۲</text>
    </svg>
    '''
    full_path = os.path.join(output_dir, filename)
    with open(full_path, 'wb') as f:
        f.write(svg.encode('utf-8'))
    print(f"Generated bodies slide at: {full_path}")

def create_federal_layers_slide(filename, chapter_title):
    svg = f'''<svg width="1080" height="1350" viewBox="0 0 1080 1350" xmlns="http://www.w3.org/2000/svg">
    <rect width="1080" height="1350" fill="#f0f4f8"/>
    <rect x="0" y="0" width="1080" height="100" fill="#1565C0"/>
    <foreignObject x="0" y="0" width="1080" height="100"><div xmlns="http://www.w3.org/1999/xhtml" style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; font-family:Vazirmatn; font-size:36px; font-weight:800; color:white; direction:rtl;">{chapter_title}</div></foreignObject>
    <text x="540" y="200" text-anchor="middle" font-family="'Vazirmatn'" font-size="52" font-weight="900" fill="#1565C0">ساختار چهارلایه حکومت</text>
    <g transform="translate(540, 300)">
        <rect x="-500" y="0" width="1000" height="140" rx="70" fill="#0D47A1"/><text y="60" text-anchor="middle" font-family="Vazirmatn" font-size="32" font-weight="900" fill="white">سطح ملی (فدرال)</text><text y="100" text-anchor="middle" font-family="Vazirmatn" font-size="18" fill="white">دفاع، سیاست خارجی، پول ملی</text>
        <path d="M0,140 L0,200" stroke="#1565C0" stroke-width="5" marker-end="url(#arrowhead)"/>
        <rect x="-400" y="200" width="800" height="140" rx="70" fill="#1976D2"/><text y="260" text-anchor="middle" font-family="Vazirmatn" font-size="32" font-weight="900" fill="white">سطح منطقه‌ای (ایالت‌ها)</text><text y="300" text-anchor="middle" font-family="Vazirmatn" font-size="18" fill="white">آموزش، توسعه محلی، پلیس منطقه‌ای</text>
        <path d="M0,340 L0,400" stroke="#1565C0" stroke-width="5" marker-end="url(#arrowhead)"/>
        <rect x="-300" y="400" width="600" height="140" rx="70" fill="#1E88E5"/><text y="460" text-anchor="middle" font-family="Vazirmatn" font-size="32" font-weight="900" fill="white">سطح استانی</text><text y="500" text-anchor="middle" font-family="Vazirmatn" font-size="18" fill="white">خدمات تخصصی، راه‌ها، بهداشت</text>
        <path d="M0,540 L0,600" stroke="#1565C0" stroke-width="5" marker-end="url(#arrowhead)"/>
        <rect x="-200" y="600" width="400" height="140" rx="70" fill="#42A5F5"/><text y="660" text-anchor="middle" font-family="Vazirmatn" font-size="32" font-weight="900" fill="white">سطح محلی</text><text y="700" text-anchor="middle" font-family="Vazirmatn" font-size="18" fill="white">شهرداری‌ها، خدمات شهری</text>
    </g>
    <defs><marker id="arrowhead" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto"><polygon points="0 0, 10 3.5, 0 7" fill="#1565C0" /></marker></defs>
    </svg>'''
    full_path = os.path.join(output_dir, filename)
    with open(full_path, 'wb') as f: f.write(svg.encode('utf-8'))
    print(f"Generated federal layers slide at: {full_path}")

create_federal_layers_slide('ch09_creative_1.svg', 'فصل ۹: فاز ۲ — نهادسازی (سال ۳-۵)')

create_bodies_slide('ch08_creative_2.svg', 'فاز ۱: گذار — تثبیت و استقرار (۰ تا ۲۴ ماه)')
