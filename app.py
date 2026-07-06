import streamlit as st
import random

# =====================================================
# JUDUL
# =====================================================

st.set_page_config(
    page_title="Canva Contributor Generator",
    page_icon="🎨",
    layout="wide"
)

st.title("🎨 Canva Contributor Unique Asset Generator")

st.caption(
    "Optimized for AI generation with EXACTLY 20 icons in a perfect 5×4 grid. "
    "Every icon is designed to fit inside a 500×500px crop area for Illustrator slicing."
)

st.write(
    "Generate prompt Canva Contributor dengan variasi style otomatis "
    "agar hasil lebih unik, tidak monoton, dan lebih mudah dipotong menjadi "
    "20 elemen terpisah."
)

# =====================================================
# TEMA
# =====================================================

st.subheader("1. Tentukan Objek")

theme_type = st.selectbox(
    "Pilih Tema",
    [
        "Back to School / Education",
        "Cute Science & Math Lab Supplies",
        "Custom Theme (Tulis Sendiri)"
    ]
)

custom_subject = st.text_input(
    "Masukkan 20 Objek (pisahkan dengan koma)",
    value="beaker, microscope, ruler, notebook, calculator, pencil, scissors, globe, backpack, compass, protractor, marker, eraser, sharpener, clipboard, test tube, magnifying glass, graduation cap, textbook, chalkboard"
)

# =====================================================
# STYLE
# =====================================================

st.subheader("2. Pilih Style")

style_option = st.radio(
    "Gaya Visual",
    [
        "Kawaii Style (Imut)",
        "Non-Kawaii Style (Polos)"
    ]
)

# =====================================================
# RANDOM STYLE DATABASE
# =====================================================

visual_styles = [
    "premium commercial clipart style",
    "layered paper cut illustration style",
    "modern educational clipart style",
    "storybook illustration style",
    "Scandinavian children's book artwork",
    "premium classroom resource illustration",
    "Montessori learning material artwork",
    "Japanese stationery inspired clipart",
    "modern editorial illustration style",
    "creative vector collage style",
    "soft dimensional vector artwork",
    "bold geometric clipart style",
    "premium Canva marketplace illustration",
    "handcrafted educational artwork",
    "modern flashcard illustration style",
    "playful commercial clipart style",
    "clean layered vector illustration",
    "premium infographic artwork",
    "contemporary children's illustration",
    "commercial best seller clipart style"
]

color_palettes = [
    "coral teal mustard and navy",
    "lavender mint peach and sky blue",
    "terracotta sage green and cream",
    "turquoise orange pink and yellow",
    "indigo aqua lime and coral",
    "soft candy colors",
    "retro seventies colors",
    "warm autumn colors",
    "vibrant tropical colors",
    "modern muted colors",
    "playful kindergarten palette",
    "fresh educational palette",
    "bright cheerful colors",
    "Scandinavian pastel palette",
    "creative modern palette"
]

decorative_elements = [
    "tiny stars",
    "sparkles",
    "abstract dots",
    "confetti pieces",
    "floating geometric shapes",
    "simple swirls",
    "small flowers",
    "mini hearts",
    "educational doodles",
    "playful accents"
]

creative_modifiers = [
    "inspired by Scandinavian children's books",
    "inspired by Japanese stationery design",
    "inspired by Montessori learning materials",
    "inspired by educational flash cards",
    "inspired by classroom posters",
    "inspired by museum graphics",
    "inspired by premium educational resources",
    "inspired by toy packaging design",
    "inspired by preschool learning materials",
    "inspired by modern editorial graphics"
]

# =====================================================
# GENERATE
# =====================================================

if st.button("✨ Generate Prompt"):

    if not custom_subject.strip():

        st.warning("Masukkan daftar objek terlebih dahulu")

    else:

        selected_style = random.choice(visual_styles)
        selected_palette = random.choice(color_palettes)
        selected_decor = random.choice(decorative_elements)
        selected_modifier = random.choice(creative_modifiers)

        # =================================================
        # VECTOR STYLE
        # =================================================

        vector_preset = f"""
{selected_style},

{selected_modifier},

premium commercial clipart artwork,

modern layered vector illustration,

clean paper cut inspired design,

soft dimensional appearance,

large bold color blocks,

strong recognizable silhouettes,

clean closed shapes,

minimal anchor points,

easy vectorization,

easy SVG conversion,

easy Adobe Illustrator editing,

easy Vector Magic tracing,

subtle depth using layered shapes,

simple highlight elements,

simple shadow elements,

balanced composition,

professional commercial artwork,

high demand marketplace style,

premium Canva Contributor quality,

premium Adobe Stock quality,

exclusive handcrafted appearance,

not flat icon style,

not app icon style,

not ui icon style,

not logo style,

not sticker style,

not generic stock icon pack,

each object designed as a standalone illustration,

high click through appeal,

modern marketplace trend aesthetic,

distinctive visual identity,

using {selected_palette},

decorated with {selected_decor}
"""

        # =================================================
        # KAWAII / NON KAWAII
        # =================================================

        if "Kawaii" in style_option:

            style_preset = f"""
            {vector_preset},
            cute tiny faces,
            simple dot eyes,
            smiling mouths,
            blush cheeks,
            adorable expression variety
            """

            negative_prompt = """
--no outlines
--no strokes
--no linework
--no realistic gradients
--no mesh gradients
--no realistic shadows
--no photorealistic lighting
--no realistic textures
--no photorealistic
--no 3d render
--no stickers
--no die cut border
--no overlapping objects
--no cropped icons
--no oversized icons
--no merged icons
--no scene composition
--no background illustration
"""

        else:

            style_preset = f"""
            {vector_preset},
            strictly no faces,
            no eyes,
            no mouth,
            clean object representation
            """

            negative_prompt = """
            --no faces
            --no eyes
            --no mouth
            --no characters
            --no outlines
            --no strokes
            --no linework
            --no gradients
            --no shadows
            --no realistic textures
            --no photorealistic
            --no 3d render
            --no overlapping objects
            --no cropped icons
            --no oversized icons
            --no merged icons
            --no scene composition
            --no background illustration
            """

        # =================================================
        # LABEL
        # =================================================

        label_instruction = """
        each object must have its English name written below the icon,
        Arial font only,
        center aligned,
        readable typography,
        consistent font size,
        single line label,
        professional appearance
        """

        # =================================================
        # UNIQUENESS
        # =================================================

       uniqueness_instruction = """
every object must have a completely unique silhouette,

different proportions,

different shape construction,

different color combinations,

different decorative treatment,

different visual hierarchy,

different shape language,

different perspective angle,

avoid repetitive icon structures,

avoid copy paste appearance,

avoid generic stock appearance,

avoid template based design,

avoid identical compositions,

some objects front view,

some objects angled view,

some objects three quarter view,

every icon visually distinct from all others,

individually illustrated appearance,

premium commercial clipart quality,

exclusive handcrafted feeling
"""

        # =================================================
        # GRID 5 X 4
        # =================================================

        grid_instruction = """
        EXACTLY 20 separate icons only,
        strict 5 columns by 4 rows grid layout,
        one icon per grid cell,
        perfectly aligned grid,
        equal spacing between all cells,
        each icon centered inside its own square area,
        each icon occupies approximately 65 to 70 percent of the available cell size,
        large white margins around every icon,
        large padding between icons,
        no overlapping elements,
        no touching edges,
        no cropped objects,
        no floating decorations between cells,
        all icons fully visible,
        square canvas divided into twenty equal sections,
        suitable for individual 500x500 pixel export,
        consistent icon scale,
        consistent visual weight,
        clean white background
        """

        # =================================================
        # FINAL PROMPT
        # =================================================

        final_prompt = f"""
Create a professional Canva Contributor clipart sheet.

Theme:
{theme_type}

Objects:
{custom_subject}

Create EXACTLY 20 separate icons.

Display all icons in a strict 5 columns × 4 rows grid.

One object per cell.

Each icon must fit completely inside its own square area.

Each icon should occupy only 65 to 70 percent of the available cell size.

Leave large empty margins around every icon.

Designed specifically for individual 500x500 pixel cropping and export.

No object may cross cell boundaries.

No decorative elements between cells.

{style_preset}

{label_instruction}

{uniqueness_instruction}

{grid_instruction}

Commercial Canva Contributor quality.

Premium marketplace asset sheet.

Professional vector artwork.

SVG friendly.

Adobe Illustrator friendly.

Vector Magic friendly.

Auto trace friendly.

Crisp edges.

Clean shapes.

Pure white background.

{negative_prompt}
"""

        st.success("Prompt berhasil dibuat")

        st.text_area(
            "Copy Prompt",
            final_prompt,
            height=650
        )

        st.info(
            """
✅ Tepat 20 icon

✅ Grid 5×4 rapi

✅ Cocok dipotong menjadi 20 artboard 500×500 px

✅ Icon tidak saling menempel

✅ Label Arial otomatis

✅ Cocok untuk Canva Contributor

✅ Cocok untuk Adobe Stock

✅ SVG Friendly

✅ Vector Magic Friendly
            """
        )
