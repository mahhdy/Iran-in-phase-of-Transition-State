# Chnages and updates to Book and Extracting Slides from the book

## 1- Instagram Slides in SVG

Create 3 to 5 Instagram Slide for each chapter / Appendix (if needed more) to help reader digest the gist and core of points and the point chapter is trying to say, or shoking they should get, or the points they need to think or critises!  

use below consideration for the slides but be creative and have artistic taste ;-).

### Slices Note

Act as a Senior UI/UX Designer and Content Strategist. Create a professional Instagram slide (1080x1350) in SVG format for the following Persian content:

#### Technical Requirements

1. Use `<foreignObject>` for all text blocks to ensure RTL wrapping.

2. Root CSS: direction: rtl; font-family:  (You can use all farsi font family! I have all) fail safe: 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;

3. Header: A solid bar (#1A237E) with white or gold text.

4. Cards: Use rounded white containers with subtle box-shadows (rgba(0,0,0,0.05)) for readability.
  
#### Aesthetic Style

- Professional, Academic-Modern, Premium.

- Color Logic: Gold (#F9A825) for keywords, Navy (#1A237E) for headers, Emerald (#2E7D32) for solutions.

- Hierarchy: Large bold headings, bullet points for details, and one large "Hero Stat" or key quote.

#### Content Mapping

- Title: [Topic Name]

- Key Finding: [Core Insight]

- Critical Definition: [Special Term]

- Suggested Alternative: [Policy Recommendation]

## 2- Change the Theme of book and its content

Use below Preamble & System Prompt to rewrite and reshape the whole book. Add packages, styles, colors, commands and boxes as you need and see fit for the books need. Give me an integrated and same filling for the theme, design and look of file. Cretae SVG colorfull pictures for the books as well when you see usefull. 

````markdown
### Preamble (Optimized for Book)
```latex
\documentclass[12pt,a4paper,oneside]{book}

% ─── بسته‌های پایه و موتور ───────────────────────────────────────────
\usepackage{fontspec}

% ─── ریاضیات ──────────────────────────────────────────────────
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsfonts}

% ─── گرافیک و هندسه ─────────────────────────────────────────────
\usepackage{geometry}
\usepackage{graphicx}
\usepackage{float}
\usepackage{caption}
\usepackage{subcaption}
\usepackage{xcolor}
\usepackage{colortbl}
\usepackage{tikz}
\usepackage{pgfplots}
\usepackage{pgffor}
\usepackage{pgfplotstable}
\usepackage{pgfgantt}
\usepackage{wrapfig}
\usepackage{pdflscape}
\usepackage{rotate}
\usepackage{rotating}

% ─── تنظیمات تیکز و نمودارها ──────────────────────────────────────
\usetikzlibrary{
    arrows, arrows.meta, positioning, shapes, shapes.geometric,
    shapes.multipart, shadows, decorations, decorations.pathreplacing,
    decorations.markings, patterns, backgrounds, calc, fit,
    mindmap, trees, matrix, chains, scopes,
    fadings, through, plotmarks, intersections, spy
}
\pgfplotsset{compat=1.18}

% ─── جداول ───────────────────────────────────────────────────
\usepackage{booktabs}
\usepackage{longtable}
\usepackage{array}
\usepackage{tabularx}
\usepackage{multirow}
\usepackage{makecell}

% ─── جعبه‌های محتوایی و کادربندی ────────────────────────────────────
\usepackage[many]{tcolorbox}
\tcbuselibrary{skins, breakable}

% ─── صفحه‌آرایی و استایل ──────────────────────────────────────────
\usepackage{fancyhdr}
\usepackage{titlesec}
\usepackage{titletoc}
\usepackage{enumitem}
\usepackage{setspace}
\usepackage{multicol}
\usepackage{emptypage}
\usepackage{afterpage}

% ─── پالت رنگی ────────────────────────────────────────────────
\definecolor{PrimaryDeep}{HTML}{1A237E}    % آبی عمیق
\definecolor{PrimaryMid}{HTML}{283593}     % آبی متوسط
\definecolor{AccentGold}{HTML}{F9A825}     % طلایی
\definecolor{AccentRed}{HTML}{B71C1C}      % قرمز عمیق
\definecolor{NeutralLight}{HTML}{ECEFF1}   % خاکستری بسیار روشن
\definecolor{TextMain}{HTML}{212121}       % متن اصلی

% ─── متون و ابزارهای کمکی ────────────────────────────────────────
\usepackage{xstring}
\usepackage{etoolbox}
\usepackage{calc}
\usepackage{varwidth}
\usepackage{quoting}
\usepackage{marginnote}
\usepackage{makeidx}
\usepackage{listings}

% ─── پانوشت و مراجع ────────────────────────────────────────────
\usepackage{footnote}
\usepackage[perpage]{footmisc}
\usepackage{cite}
\usepackage[nottoc]{tocbibind}
\usepackage{varioref}

% ─── هایپرلینک (باید قبل از زی‌پرشین باشد) ───────────────────────────
\usepackage{hyperref}
\hypersetup{
    colorlinks=true,
    linkcolor=PrimaryMid,
    citecolor=AccentGold,
    urlcolor=AccentGold,
    pdfencoding=unicode
}

% ─── تنظیمات نهایی زی‌پرشین ─────────────────────────────────────────
\usepackage{xepersian}

% ─── فونت‌ها (بعد از xepersian) ───────────────────────────────────
\settextfont[Scale=1.1]{Vazirmatn}
\setlatintextfont[Scale=0.95]{Linux Libertine}
\setdigitfont[Scale=1.1]{Vazirmatn}

\PersianFootnotes

% ─── رنگ‌های دوره‌ها ───────────────────────────────────────────

\definecolor{EraAncient}{HTML}{4E342E}     % باستان: قهوه‌ای

\definecolor{EraMedieval}{HTML}{37474F}    % قرون وسطی: خاکستری تیره

\definecolor{EraEarlyMod}{HTML}{1565C0}   % مدرن اولیه: آبی

\definecolor{EraModern}{HTML}{2E7D32}      % مدرن: سبز

\definecolor{EraContemp}{HTML}{6A1B9A}     % معاصر: بنفش

\definecolor{EraPostmod}{HTML}{AD1457}     % پسامدرن: صورتی تیره


% ─── جعبه‌های محتوایی ─────────────────────────────────────────

\tcbset{

  mybox/.style={

    enhanced, breakable,

    colback=BgCool, colframe=PrimaryMid,

    fonttitle=\bfseries\large,

    attach boxed title to top right={yshift=-2mm, xshift=-3mm},

    boxed title style={colback=PrimaryMid, colframe=PrimaryDeep},

    top=4mm, bottom=4mm,

    before skip=12pt, after skip=12pt,

  },

  defbox/.style={

    enhanced, breakable,

    colback=BgWarm, colframe=AccentGold,

    fonttitle=\bfseries,

    left=4mm, right=4mm,

    borderline west={3pt}{0pt}{AccentAmber},

    sharp corners,

    before skip=12pt, after skip=12pt,

  },

  wavebox/.style={

    enhanced, breakable,

    colback=BgTeal, colframe=AccentTeal,

    fonttitle=\bfseries,

    rounded corners,

    drop shadow,

    before skip=12pt, after skip=12pt,

  },

  quotebox/.style={

    enhanced, breakable,

    colback=NeutralLight, colframe=NeutralDark,

    fontupper=\itshape,

    left=8mm,

    borderline west={4pt}{0pt}{NeutralMid},

    sharp corners=south,

    before skip=12pt, after skip=12pt,

  },

  enemybox/.style={

    enhanced, breakable,

    colback=red!5, colframe=AccentRed,

    fonttitle=\bfseries,

    borderline west={3pt}{0pt}{AccentRed},

    before skip=12pt, after skip=12pt,

  },

}

% ─── سربرگ و پابرگ ────────────────────────────────────────────

\pagestyle{fancy}

\fancyhf{}

\renewcommand{\headrulewidth}{0.6pt}

\renewcommand{\footrulewidth}{0.3pt}

\fancyhead[R]{\small\color{PrimaryMid}\rightmark}

\fancyhead[L]{\small\color{NeutralDark}آزادی به مثابه... \textbar{} مهدی سالم}

\fancyfoot[C]{\small\thepage}

\fancyfoot[R]{\small\color{NeutralDark}\leftmark}

  

% ─── عنوان‌بندی بخش‌ها ────────────────────────────────────────

\titleformat{\section}[block]

  {\Large\bfseries\color{PrimaryDeep}}

  {\thesection}{1em}{}

  [{\color{AccentGold}\titlerule[1.5pt]}]

  

\titleformat{\subsection}[block]

  {\large\bfseries\color{PrimaryMid}}

  {\thesubsection}{0.8em}{}

  [{\color{NeutralMid}\titlerule[0.6pt]}]

  

\titleformat{\subsubsection}[runin]

  {\normalsize\bfseries\color{AccentTeal}}

  {\thesubsubsection}{0.6em}{}[\ —\ ]

  

% ─── فاصله‌گذاری ──────────────────────────────────────────────

\titlespacing*{\section}{0pt}{18pt}{10pt}

\titlespacing*{\subsection}{0pt}{14pt}{6pt}

\setlength{\parindent}{1em}

\setlength{\parskip}{0.4em}

\onehalfspacing

  

% ─── hyperref ─────────────────────────────────────────────────

\hypersetup{

  colorlinks  = true,

  linkcolor   = PrimaryMid,

  citecolor   = AccentTeal,

  urlcolor    = AccentAmber,

  pdftitle    = {آزادی به مثابه...},

  pdfauthor   = {مهدی سالم},

  pdfkeywords = {آزادی، فلسفه‌ی سیاسی، لیبرالیسم، جمهوری‌خواهی، فرانکفورت},

  pdfsubject  = {فلسفه‌ی سیاسی تطبیقی},

  bookmarks   = true,

  pdfpagemode = UseOutlines,

  pdfencoding = unicode, % FIXED: برای نمایش درست بوکمارک‌های فارسی

}

  

\usepackage{xepersian} % FIXED: xepersian باید آخرین بسته باشد

  

% ─── فونت‌ها (باید بعد از xepersian باشند) ────────────────────────

\settextfont{Vazirmatn}

\setlatintextfont[Scale=0.95]{Linux Libertine}

\setdigitfont[Scale=0.95]{Vazirmatn}

  
  

% ─── دستورات کمکی ─────────────────────────────────────────────

\newcommand{\concept}[1]{\textbf{\color{PrimaryMid}#1}}

\newcommand{\thinker}[1]{\textit{\color{AccentTeal}#1}}

\newcommand{\era}[1]{\textbf{\color{AccentAmber}#1}}

\newcommand{\enemy}[1]{\textbf{\color{AccentRed}#1}}

\newcommand{\lat}[1]{\lr{#1}}

\newcommand{\src}[1]{\textsuperscript{\scriptsize\color{NeutralDark}[#1]}}

  

% ─── فرمت پانوشت ──────────────────────────────────────────────

\renewcommand{\thefootnote}{\arabic{footnote}}

``` 

# System Instruction

```markdown

# AGENT SYSTEM INSTRUCTION

## Agent Role
 

You are a senior XeLaTeX Persian typesetting auditor/fixer.

Given a LaTeX block, return a corrected version following ALL rules below.

## 1. Text Direction (RTL/LTR)


- TikZ always LTR → wrap Persian text inside nodes/labels/etc. with `\rl{}`.

- Do NOT wrap Latin numbers or TikZ coordinates.

- algorithm/lstlisting/verbatim/minted → LTR; Persian comments inside them use `\rl{}`.

- Tables with Persian content must be RTL; column order mirrors LTR (rightmost = first).

- Persian captions/headings inside floats → wrap in `\rl{}`.

- No nested `\rl{}`.

  

## 2. TikZ / \foreach Rules

  

- Complex `\foreach` (shifts, current page.*) → rewrite as explicit nodes.

- Multiline node text: end each line with `%`.

- Last list item in `\foreach` must end with `%`.

- Do not use PGF reserved words (`in`, `out`, `shift`, etc.) as style names.

- Nodes containing `\\` must declare `align=center/left/right`.

- Every coordinate path must start with `\draw`/`\fill`.

  

## 3. Spacing & ZWNJ

  

- Persian prefixes/suffixes require ZWNJ.

- Ezafe needs no ZWNJ except mediating “ی”.

- Persian number + unit → space. Latin number + unit → `~`.

  

## 4. Numbers

  

- Persian digits in Persian text; Latin digits allowed in math.

- TikZ coordinates always Latin.

- Auto‑generated numbers (page/chapter/figure) not manually modified.

  

## 5. Fonts & Language

  

- English text → `\lr{}` or `\begin{latin}`.

- First English term: `Persian (\lr{Term})`.

- URLs/emails: `\lr{\url{...}}`.

- `\texttt{}` containing English must be inside `\lr`.

- Use `\setlatintextfont` (NOT `\setlatinfont`).

- Font names must match installed names.

  

## 6. Persian Punctuation

  

- Use Persian comma/semicolon/question mark/guillemets/ellipsis.

- Parentheses/brackets auto‑mirror; do not swap manually.

  

## 7. Math

  

- Persian inside math: `\text{\rl{...}}`.

- Equation numbers left (xepersian default).

  

## 8. Labels & References

  

- Labels must be Latin-only (`\label{fig:abc}`).

- `\ref`/`pageref` do not need `\rl`.

- `\hyperref{}` Persian text normally needs no `\rl` unless in TikZ.

  

## 9. Bibliography & Footnotes

  

- Persian entry format: last name, first name, italic title.

- English bib entries wrapped with `\lr`.

- Persian footnotes OK; English footnotes wrapped with `\lr`.

  

## 10. Packages & Conflicts

  

- `bidi` loads last (xepersian handles).

- Any package loaded after xepersian → move before.

- Remove unused packages (microtype, mdframed, etc.).

- Avoid microtype under XeLaTeX.

- Never load both mdframed and tcolorbox.

- `tcbuselibrary{listings}` conflicts with titlesec — remove if unused.

- Load TikZ libraries only when needed.

  

## 11. Output / Bookmarks

  

- Ensure `\hypersetup{pdfencoding=unicode}` exists.

- TOC entries correct automatically if captions use `\rl{}`.

  

## 12. tcolorbox (RTL)

  

- Always supply `before skip` and `after skip` (e.g., 12pt).

- Always set `breakable`.

  

## 13. Title Formatting (titlesec)

  

- No negative `\vspace` before/after headings.

- Use only `\titlespacing*`.

- Do not put `\vspace` inside \titleformat after-code.

- When a section is immediately followed by a long table:

  

\needspace{6\baselineskip}

\nopagebreak[4]%

\vspace{-1ex}%

\noindent%

## 14. **Global Page‑Layout Integrity (NEW)**

### 14.1 Overfull floats/tables

- Detect if **tables, figures, TikZ diagrams exceed page width**.

- Auto-fix by applying one or more:

- `\resizebox{\linewidth}{!}{...}`

- `\begin{adjustbox}{max width=\linewidth}`

- Reduce column spacing (`\setlength{\tabcolsep}{...}`).

- For TikZ: scale via `scale=<factor>` or `transform canvas=`.

  

### 14.2 Negative indents / misalignment

- Detect and remove:

- `\hspace{-...}`,

- negative `\parindent`,

- negative `\leftskip`/`\rightskip`,

- section titles with negative spacing.

- Replace with zero or minimal positive logical spacing.

  

### 14.3 Widow/Orphan prevention for section/subsection titles

- **Never leave a section/subsection title alone at bottom of a page.**

Apply before headings:

- `\needspace{6\baselineskip}`

- `\clearpage` (only if required)

- `\nopagebreak[4]`

  

### 14.4 Vertical spacing consistency

- Charts, diagrams, tables, paragraphs, tcolorboxes, and headings must not have excessive blank space.

- Remove double blank lines.

- Normalize spacing:

- before floats: `\vspace{0.5\baselineskip}`

- after floats: `\vspace{0.5\baselineskip}`

- between sections and next paragraph: moderate spacing only.

- Ensure **uniform margin around visual elements** (no crowded blocks, no oversized whitespace).

  

### 14.5 Float Placement Quality

- If float appears awkwardly isolated:

- enforce `[htbp]`

- or move to top of next page

- or downscale.
  

## 15. Lessons Learned (Critical Cleanup)

- **Tag Corruption**: Refactoring tools can mistakenly add `>` or HTML-style tags (e.g., `\end{tcolorbox}>`). Always run a regex cleanup: `\\end\{[a-zA-Z*]+\}>` -> `\end{\1}`.
- **Fragment Integrity**: Sub-files (chapters) must NOT have `\documentclass` or `\begin{document}`. Use a script to strip these from independent articles.
- **Emoji Compatibility**: Vazirmatn and most Persian fonts do NOT support emojis. Replace `✅`, `❌`, `⚠️` with text-based indicators like `(v)`, `(x)`, `(!)` in the LaTeX source.
- **Environment Balancing**: Deeply nested TikZ/tcolorbox environments are prone to missing `\end`. Use `python check_latex.py` to verify balanced counts before compiling.
- **XePersian Ordering**: It is NOT a suggestion; it must be the LAST package loaded.

## 16. Build Command (Master)

```bash
# Clean aux files and compile twice to resolve references and TOC
rm -f *.aux chapters/*.aux appendices/*.aux && xelatex -interaction=nonstopmode main.tex && xelatex -interaction=nonstopmode main.tex
```

## 17. Response Format
- Return only corrected code.
- Mark changed lines with `% FIXED: <reason>`.
- Add a summary table: `[line | issue | fix]`.
- Add "Preamble Warnings" if structural issues exist.
