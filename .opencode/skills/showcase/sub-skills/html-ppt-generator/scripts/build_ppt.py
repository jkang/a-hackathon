import os
import sys
import json

def load_template_css():
    # Use the unified template.css from scripts dir
    css_path = os.path.join(os.path.dirname(__file__), 'template.css')
    try:
        with open(css_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Error loading CSS: {e}")
        return ""

def calculate_density(slide):
    """Simple heuristic to determine if font size should be downscaled."""
    text_count = 0
    # Combine relevant content fields
    fields = ['content', 'subtitle', 'col1', 'col2', 'bottom_content']
    for field in fields:
        content = slide.get(field, "")
        if isinstance(content, str):
            text_count += len(content)
    
    # Also count list items/tiles
    for item in slide.get('items', []) + slide.get('tiles', []) + slide.get('steps', []):
        text_count += len(str(item))

    # Threshold for 1280x720 area, roughly 500 chars for Mandarin/English mix
    return "density-high" if text_count > 450 else ""

def build_html(slides_data, css_content):
    title = slides_data.get('title', 'Presentation')
    html = [f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&family=Lato:wght@400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <style>
{css_content}
    </style>
</head>
<body>
"""]

    slides = slides_data.get('slides', [])
    for i, slide in enumerate(slides):
        slide_type = slide.get('type')
        active_class = " active" if i == 0 else ""
        density_class = calculate_density(slide)
        
        container_start = f'    <div class="slide-container{active_class} {density_class}" id="slide{i}">'
        
        if slide_type == 'cover':
            html.append(f"""{container_start}
        <div class="title-layout">
            <h1>{slide.get('title', '')}</h1>
            <p class="subtitle">{slide.get('subtitle', '')}</p>
            <p style="margin-top:20px; color:#94a3b8;"><i class="fa-solid fa-pen-nib"></i> {slide.get('author', '')} &nbsp;&nbsp;|&nbsp;&nbsp; {slide.get('date', '')}</p>
        </div>
    </div>""")
            
        elif slide_type == 'agenda':
            items_html = "\\n".join([f"<li><strong>{item.get('title', '')}</strong><p>{item.get('subtitle', '')}</p></li>" for item in slide.get('items', [])])
            html.append(f"""{container_start}
        <h2 class="slide-title">{slide.get('title', 'Agenda')}</h2>
        <div class="content-area">
            <div class="agenda-layout">
                <ol>
                    {items_html}
                </ol>
            </div>
        </div>
    </div>""")
            
        elif slide_type == 'chapter':
            html.append(f"""{container_start}
        <div class="content-area chapter-layout">
            <span class="chapter-number">{slide.get('chapter_label', 'Chapter')}</span>
            <h2>{slide.get('title', '')}</h2>
            <p class="subtitle">{slide.get('subtitle', '')}</p>
        </div>
    </div>""")

        elif slide_type == 'layout_h_split':
            html.append(f"""
    <div class="slide-container layout-h-split{active_class} {density_class}" id="slide{i}">
        <div class="content-top">
            <h2 class="slide-title">{slide.get('title', '')}</h2>
            <div class="description-text">{slide.get('content', '')}</div>
        </div>
        <div class="image-bottom">
            <div class="img-wrap">
                <img src="{slide.get('image', '')}" alt="Image">
            </div>
        </div>
    </div>""")

        elif slide_type == 'layout_v_split':
            html.append(f"""
    <div class="slide-container layout-v-split{active_class} {density_class}" id="slide{i}">
        <div class="content-left">
            <h2 class="slide-title">{slide.get('title', '')}</h2>
            <div class="description-text">{slide.get('content', '')}</div>
        </div>
        <div class="image-right">
            <div class="img-wrap">
                <img src="{slide.get('image', '')}" alt="Image">
            </div>
        </div>
    </div>""")

        elif slide_type == 'layout_full_media':
            html.append(f"""
    <div class="slide-container layout-full-media{active_class} {density_class}" id="slide{i}">
        <div class="image-main">
            <div class="img-wrap">
                <img src="{slide.get('image', '')}" alt="Image">
            </div>
        </div>
        <div class="description">{slide.get('content', '')}</div>
    </div>""")

        elif slide_type == 'layout_double_stack':
            images = slide.get('images', [])
            imgs_html = "".join([f'<div class="img-wrap"><img src="{img}"></div>' for img in images])
            html.append(f"""
    <div class="slide-container layout-double-stack{active_class} {density_class}" id="slide{i}">
        <div class="content-top">
            <h2 class="slide-title">{slide.get('title', '')}</h2>
            <div class="description-text">{slide.get('content', '')}</div>
        </div>
        <div class="images-container">
            {imgs_html}
        </div>
    </div>""")

        elif slide_type == 'content_two_column':
            html.append(f"""{container_start}
        <h2 class="slide-title">{slide.get('title', '')}</h2>
        <div class="content-area">
            <div class="two-column tiled">
                <div>{slide.get('col1', '')}</div>
                <div>{slide.get('col2', '')}</div>
            </div>
        </div>
    </div>""")

        elif slide_type == 'content_tiled':
            tiles_html = []
            for t in slide.get('tiles', []):
                icon = t.get('icon', 'fa-star')
                if not icon.startswith('fa-'): icon = 'fa-' + icon
                tiles_html.append(f"""
                <div class="tile">
                    <div class="icon"><i class="fa-solid {icon}"></i></div>
                    <h3 style="color:#0f172a; font-size: 22px; margin-bottom:10px;">{t.get('title','')}</h3>
                    <p>{t.get('content','')}</p>
                </div>""")
            html.append(f"""{container_start}
        <h2 class="slide-title">{slide.get('title', '')}</h2>
        <div class="content-area">
            <div class="tiled-content">
                {"".join(tiles_html)}
            </div>
            <div style="width:100%;">{slide.get('bottom_content', '')}</div>
        </div>
    </div>""")

        elif slide_type == 'qa':
            html.append(f"""{container_start}
        <div class="content-area qa-layout">
            <h2>{slide.get('title', 'Q&A')}</h2>
            <p>{slide.get('subtitle', 'Any questions?')}</p>
        </div>
    </div>""")

    js_script = """
    <!-- Controls Panel -->
    <div id="ppt-controls">
        <button id="btn-prev" onclick="prevSlide()" title="上一页"><i class="fa-solid fa-chevron-left"></i></button>
        <div class="page-info">
            <span id="current-page">1</span> / <span id="total-pages">""" + str(len(slides)) + """</span>
        </div>
        <button id="btn-next" onclick="nextSlide()" title="下一页"><i class="fa-solid fa-chevron-right"></i></button>
        <div style="height: 24px; width: 1px; background: #cbd5e1; margin: 0 10px;"></div>
        <div style="display:flex; align-items:center; gap:5px;">
            <input type="number" id="jump-input" min="1" max=\"""" + str(len(slides)) + """\" placeholder="页">
            <button onclick="jumpSlide()" title="跳转" style="font-size: 14px; width: auto; padding: 0 10px; border-radius: 12px; background: #0284c7; color: white;">Go</button>
        </div>
    </div>

    <script>
        const slides = document.querySelectorAll('.slide-container');
        const prevBtn = document.getElementById('btn-prev');
        const nextBtn = document.getElementById('btn-next');
        const currentPageEl = document.getElementById('current-page');
        const jumpInput = document.getElementById('jump-input');
        
        document.getElementById('total-pages').innerText = slides.length;
        jumpInput.max = slides.length;

        let currentSlide = 0;

        function updateUI() {
            slides.forEach((slide, index) => {
                if (index === currentSlide) {
                    slide.classList.add('active');
                } else {
                    slide.classList.remove('active');
                }
            });

            currentPageEl.innerText = currentSlide + 1;
            prevBtn.disabled = currentSlide === 0;
            nextBtn.disabled = currentSlide === slides.length - 1;
        }

        function prevSlide() { if (currentSlide > 0) { currentSlide--; updateUI(); } }
        function nextSlide() { if (currentSlide < slides.length - 1) { currentSlide++; updateUI(); } }
        function jumpSlide() {
            let targetSlide = parseInt(jumpInput.value) - 1;
            if (!isNaN(targetSlide) && targetSlide >= 0 && targetSlide < slides.length) {
                currentSlide = targetSlide; updateUI();
            }
        }

        document.addEventListener('keydown', (e) => {
            if (e.key === 'ArrowRight' || e.key === 'PageDown' || e.key === ' ') nextSlide();
            else if (e.key === 'ArrowLeft' || e.key === 'PageUp') prevSlide();
        });

        updateUI();
    </script>
</body>
</html>
"""
    html.append(js_script)
    return "\\n".join(html)

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 build_ppt.py <input.json> <output.html>")
        sys.exit(1)

    input_json = sys.argv[1]
    output_html = sys.argv[2]

    try:
        with open(input_json, 'r', encoding='utf-8') as f:
            slides_data = json.load(f)
    except Exception as e:
        print(f"Error reading JSON: {e}")
        sys.exit(1)

    css_content = load_template_css()
    final_html = build_html(slides_data, css_content)

    try:
        with open(output_html, 'w', encoding='utf-8') as f:
            f.write(final_html)
        print(f"✅ Presentation compiled successfully: {output_html}")
    except Exception as e:
        print(f"Error writing HTML: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
