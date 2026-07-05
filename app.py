import streamlit as st
import random

# =====================================================
# JUDUL
# =====================================================

st.title("🎨 Canva Contributor Unique Asset Generator")
st.write(
    "Generate prompt AI untuk Canva Contributor dengan variasi style otomatis "
    "agar hasil lebih unik, tidak monoton, dan mengurangi kemungkinan mirip aset lain."
)

# =====================================================
# PILIHAN TEMA
# =====================================================

st.subheader("1. Tentukan Objek Elemen")

theme_type = st.selectbox(
    "Pilih Fokus Tema:",
    [
        "Back to School / Education",
        "Cute Science & Math Lab Supplies",
        "Custom Theme (Tulis di bawah)"
    ]
)

custom_subject = st.text_input(
    "Daftar Objek (Pisahkan dengan koma):",
    value="beaker, hourglass, protractor, pencil holder, notebook, highlighter, ruler, compass, sharpener, scissors, calculator"
)

# =====================================================
# GAYA
# =====================================================

st.subheader("2. Pilihan Gaya Visual")

style_option = st.radio(
    "Pilih Gaya:",
    [
        "Kawaii Style (Imut)",
        "Non-Kawaii Style (Polos)"
    ]
)

# =====================================================
# DATABASE STYLE ACAK
# =====================================================

visual_styles = [
    "playful geometric cut-paper style",
    "modern abstract flat illustration style",
    "organic blob shape vector style",
    "retro educational graphic style",
    "soft Scandinavian flat style",
    "creative asymmetrical vector style",
    "mid-century modern illustration style",
    "editorial infographic style",
    "chunky colorful shape style",
    "creative classroom poster style",
    "Japanese stationery inspired style",
    "modern museum educational style",
    "playful preschool learning style",
    "creative learning material style",
    "vibrant educational branding style"
]

color_palettes = [
    "coral, teal, mustard and navy",
    "lavender, mint, peach and sky blue",
    "terracotta, sage green and cream",
    "turquoise, orange, pink and yellow",
    "indigo, aqua, lime and coral",
    "soft candy colors",
    "retro 70s colors",
    "warm autumn colors",
    "vibrant tropical colors",
    "modern muted colors",
    "playful kindergarten colors",
    "fresh educational colors",
    "bright cheerful colors",
    "colorful Scandinavian palette",
    "creative pastel palette"
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
    "playful accents",
    "tiny geometric decorations",
    "floating symbols",
    "creative abstract details",
    "mini graphic accents",
    "small decorative elements"
]

creative_modifiers = [
    "inspired by Scandinavian children's books",
    "inspired by modern educational infographics",
    "inspired by contemporary editorial graphics",
    "inspired by Japanese stationery design",
    "inspired by playful classroom posters",
    "inspired by geometric paper cut art",
    "inspired by modern learning materials",
    "inspired by colorful museum graphics",
    "inspired by trendy preschool visuals",
    "inspired by creative STEM education branding",
    "inspired by Montessori learning materials",
    "inspired by educational flash cards",
    "inspired by premium learning resources",
    "inspired by modern children's publishing",
    "inspired by educational toy packaging"
]

layout_styles = [
    "neatly scattered layout",
    "balanced composition",
    "organic free arrangement",
    "grid inspired arrangement",
    "dynamic floating composition",
    "editorial asset sheet layout",
    "creative marketplace presentation",
    "modern vector collection layout",
    "playful arrangement",
    "professional asset board layout"
]

# =====================================================
# GENERATE
# =====================================================

if st.button("Generate Unique Prompt ✨"):

    if not custom_subject:
        st.warning("Mohon isi daftar objek terlebih dahulu!")

    else:

        selected_style = random.choice(visual_styles)
        selected_palette = random.choice(color_palettes)
        selected_decor = random.choice(decorative_elements)
        selected_modifier = random.choice(creative_modifiers)
        selected_layout = random.choice(layout_styles)

        # =================================================
        # BASE STYLE
        # =================================================

        vector_preset = (
            f"{selected_style}, "
            f"{selected_modifier}, "
            f"100% solid flat vector artwork, "
            f"NO outlines, "
            f"NO linework, "
            f"NO gradients, "
            f"NO shadows, "
            f"NO shading, "
            f"clean vector shapes, "
            f"creative asymmetrical construction, "
            f"distinctive silhouettes, "
            f"non-generic stock design, "
            f"unique visual identity, "
            f"using {selected_palette}, "
            f"decorated with {selected_decor}"
        )

        # =================================================
        # KAWAII / NON KAWAII
        # =================================================

        if "Kawaii" in style_option:

            style_preset = (
                f"{vector_preset}, "
                f"cute tiny faces, "
                f"simple dot eyes, "
                f"small smiling mouths, "
                f"subtle blush cheeks, "
                f"adorable expression variety"
            )

            negative_param = (
                "--no outlines "
                "--no linework "
                "--no gradients "
                "--no shadows "
                "--no photorealistic "
                "--no 3d render "
                "--no realistic textures "
                "--no stickers "
                "--no die-cut border"
            )

        else:

            style_preset = (
                f"{vector_preset}, "
                f"strictly no faces, "
                f"no eyes, "
                f"no mouth, "
                f"clean object representation"
            )

            negative_param = (
                "--no faces "
                "--no eyes "
                "--no mouth "
                "--no characters "
                "--no outlines "
                "--no linework "
                "--no gradients "
                "--no shadows "
                "--no photorealistic "
                "--no 3d render "
                "--no realistic textures"
            )

        # =================================================
        # LABEL
        # =================================================

        text_instruction = (
            "each object must have its English name written directly below the icon, "
            "clean Arial font, "
            "professional sans-serif typography, "
            "center aligned label, "
            "clear readable text"
        )

        # =================================================
        # ANTI DUPLIKAT
        # =================================================

        uniqueness_instruction = (
            "every object must have a completely unique silhouette, "
            "completely different proportions, "
            "different color combinations, "
            "different decorative treatment, "
            "different shape construction, "
            "avoid generic stock icon appearance, "
            "avoid repetitive shapes, "
            "avoid repeated compositions, "
            "avoid template-based designs, "
            "every element must feel handcrafted and exclusive"
        )

        # =================================================
        # ISOLATION
        # =================================================

        isolation_keywords = (
            f"{selected_layout}, "
            f"{text_instruction}, "
            f"clean vector asset sheet, "
            f"isolated on pure white background, "
            f"clear spacing between objects, "
            f"professional graphic asset collection, "
            f"Canva marketplace ready"
        )

        # =================================================
        # FINAL PROMPT
        # =================================================

        final_prompt = (
            f"A highly original colorful flat design clipart sheet featuring "
            f"{theme_type} elements containing {custom_subject}. "
            f"{style_preset}. "
            f"{uniqueness_instruction}. "
            f"{isolation_keywords}. "
            f"commercial Canva Contributor quality, "
            f"professional vector artwork, "
            f"high resolution, "
            f"crisp edges, "
            f"SVG friendly, "
            f"auto-trace friendly, "
            f"{negative_param}"
        )

        # =================================================
        # OUTPUT
        # =================================================

        st.success("Prompt berhasil dibuat!")

        st.text_area(
            "Copy Prompt:",
            value=final_prompt,
            height=350
        )

        st.info(
            """
Tips Canva Contributor:

✅ Hindari membuat semua set dengan warna yang sama.

✅ Hindari bentuk lingkaran membulat yang identik di semua icon.

✅ Buat minimal 100+ variasi tema berbeda.

✅ Gunakan random style agar setiap generate berbeda.

✅ Semakin unik siluet objek, semakin kecil kemungkinan dianggap mirip aset lain.

✅ Sangat cocok untuk produksi massal element Canva Contributor.
            """
        )
