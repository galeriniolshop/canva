import streamlit as st

# Judul Aplikasi
st.title("🎨 Canva Contributor Clip Art Generator")
st.write("Generate prompt AI untuk **Clip Art / Icon Set** yang *Vectorize-Friendly* (mudah dan rapi saat di-*trace* menjadi SVG).")

# 1. Pilihan Tema & Objek
st.subheader("1. Tentukan Objek Elemen")
theme_type = st.selectbox(
    "Pilih Fokus Tema:",
    ["Back to School / Education", "Cute Stationery & School Life", "Custom Theme (Tulis di bawah)"]
)

custom_subject = st.text_input(
    "Daftar Objek (Pisahkan dengan koma):",
    value="school building, school bus, blackboard easel, backpack, notebook, scissors, pencil, apple, basketball, calculator"
)

# 2. OPSI GAYA: Kawaii vs Non-Kawaii
st.subheader("2. Pilihan Gaya Visual")
style_option = st.radio(
    "Pilih Gaya Ikon:",
    ["Kawaii Style (Imut, Ada Wajah Karakter)", "Non-Kawaii Style (Polos, Objek Murni Tanpa Wajah)"]
)

# 3. Tombol Generate
if st.button("Generate Vector-Ready Prompt ✨"):
    if not custom_subject:
        st.warning("Mohon isi daftar objek terlebih dahulu!")
    else:
        # Menambahkan parameter 'vectorize-friendly' dan optimasi tracing warna
        vector_optimization = (
            "vectorize-friendly design, clean solid color fills, sharp color separation, "
            "no complex textures, no mesh gradients, smooth high-contrast edges"
        )

        if "Kawaii" in style_option:
            style_preset = (
                f"Cute kawaii doodle clipart style, prominent thick black outlines, bold clean linework, "
                f"smooth rounded corners, adorable chibi faces with big shiny black eyes and cute smiles on each object, "
                f"2d flat vector illustration look, {vector_optimization}"
            )
            negative_param = "--no faces eyes mouth characters stickers die-cut white-outlines borders drop-shadows photorealistic 3d-render blurs watercolor noise textures"
        else:
            style_preset = (
                f"Standard flat design clipart style, prominent thick black outlines, bold clean linework, "
                f"smooth rounded corners, inanimate objects only, realistic item details, literal item representation, "
                f"2d flat vector illustration design, {vector_optimization}"
            )
            negative_param = "--no faces eyes mouth characters stickers die-cut white-outlines borders drop-shadows photorealistic 3d-render blurs watercolor noise textures"

        # Instruksi teks label di bawah objek
        text_instruction = "each item must have its English name text written neatly in a cute simple font directly underneath the icon"

        # Isolasi ketat tanpa border putih luar
        isolation_keywords = (
            f"clean clipart sheet, multiple individual elements, neatly scattered, {text_instruction}, "
            "isolated on a seamless solid pure white background, no outer white sticker borders, "
            "no shadows, professional graphic asset, commercial design, asset for Canva"
        )
        
        # Merangkai prompt akhir
        final_prompt = (
            f"A colorful clipart sheet of {theme_type} elements containing {custom_subject}. "
            f"{style_preset}, bright pastel colors, {isolation_keywords}, "
            f"high resolution, clear separation between elements {negative_param}"
        )

        # Menampilkan Hasil
        st.success(f"Prompt *Vectorize-Friendly* gaya {'Kawaii' if 'Kawaii' in style_option else 'Non-Kawaii'} berhasil dibuat!")
        st.text_area("Salin prompt ini ke DALL-E 3 / Midjourney v6 / Leonardo.ai:", value=final_prompt, height=200)
        
        # Edukasi Tracing Vektor
        st.info(f"""
        💡 **Mengapa Prompt Ini Bagus untuk Di-trace (Vektor)?**
        * **`clean solid color fills` & `no mesh gradients`**: Memaksa AI memakai warna blok/padat yang tegas. Ini mencegah terciptanya jutaan gradasi warna kecil yang biasanya bikin file SVG jadi bengkak dan pecah saat di-trace.
        * **`sharp color separation`**: Batas antara warna satu dengan warna lainnya dibuat kontras tinggi, sehingga software/web *auto-trace* langsung mengenali garis batasnya dengan akurat.
        * **Parameter Negatif Tambahan**: Ditambahkan larangan `--no blurs watercolor noise textures` untuk menghilangkan efek buram atau tekstur bintik-bintik yang sering merusak hasil vektor.
        """)
