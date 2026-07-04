import streamlit as st

# Judul Aplikasi
st.title("🎨 Canva Contributor Flat Icon Generator (with Arial Text)")
st.write("Generate prompt AI untuk **Flat Clipart Set** tanpa garis tepi dengan label nama benda menggunakan **Arial font** di bawahnya (seperti gaya image_f0c37f.png).")

# 1. Pilihan Tema & Objek
st.subheader("1. Tentukan Objek Elemen")
theme_type = st.selectbox(
    "Pilih Fokus Tema:",
    ["Back to School / Education", "Cute Science & Math Lab Supplies", "Custom Theme (Tulis di bawah)"]
)

custom_subject = st.text_input(
    "Daftar Objek (Pisahkan dengan koma):",
    value="beaker, hourglass, protractor, pencil holder, notebook, highlighter, ruler, compass, sharpener, scissors, calculator"
)

# 2. OPSI GAYA: Kawaii vs Non-Kawaii
st.subheader("2. Pilihan Gaya Visual")
style_option = st.radio(
    "Pilih Gaya Ikon:",
    ["Kawaii Style (Imut dengan Mata Lingkaran & Senyum)", "Non-Kawaii Style (Polos, Objek Minimalis Murni)"]
)

# 3. Tombol Generate
if st.button("Generate Flat Vector Prompt ✨"):
    if not custom_subject:
        st.warning("Mohon isi daftar objek terlebih dahulu!")
    else:
        # Karakteristik utama flat design tanpa outline
        vector_preset = (
            "minimalist flat vector illustration style, NO outlines, NO linework, "
            "100% solid flat colors, absolutely no gradients, no shading, no shadows, "
            "clean geometric shapes, slightly rounded corners, perfect for auto-tracing"
        )

        if "Kawaii" in style_option:
            style_preset = (
                f"{vector_preset}, adorable simple faces on each item, "
                f"cute black dot eyes with tiny white highlights, simple curved smile mouths, kawaii blushing cheeks"
            )
            negative_param = "--no outlines linework black-borders gradients shading shadows stickers die-cut photorealistic 3d-render textured cursive-fonts handwritten-fonts"
        else:
            style_preset = (
                f"{vector_preset}, literal inanimate object representation, clean corporate flat design, "
                f"strictly no faces, no eyes, no mouth"
            )
            negative_param = "--no faces eyes mouth characters outlines linework black-borders gradients shading shadows stickers die-cut photorealistic 3d-render textured cursive-fonts handwritten-fonts"

        # Menambahkan instruksi teks label bahasa inggris berjenis font Arial tepat di bawah objek
        text_instruction = (
            "each individual item must have its English name text written neatly directly underneath the icon, "
            "the text must use clean sans-serif Arial font, crisp typography, clear legible letters, no cursive"
        )

        # Isolasi ketat tanpa border putih luar
        isolation_keywords = (
            f"clean vector asset sheet, multiple individual elements, neatly scattered, {text_instruction}, "
            "isolated on a seamless solid pure white background, no outer white borders, "
            "clear separation between elements, professional graphic asset, asset for Canva"
        )
        
        # Merangkai prompt akhir
        final_prompt = (
            f"A colorful flat design clipart sheet of {theme_type} elements containing {custom_subject}. "
            f"{style_preset}, bright playful pastel colors, {isolation_keywords}, "
            f"high resolution, crisp edges {negative_param}"
        )

        # Menampilkan Hasil
        st.success(f"Prompt Flat Vector {'Kawaii' if 'Kawaii' in style_option else 'Non-Kawaii'} dengan Teks Arial berhasil dibuat!")
        st.text_area("Salin prompt ini ke DALL-E 3 (paling direkomendasikan untuk teks):", value=final_prompt, height=220)
        
        # Tips Tambahan
        st.info(f"""
        💡 **Tips Menghasilkan Huruf yang Sempurna:**
        * **Gunakan DALL-E 3 (ChatGPT Plus/Bing Image Creator)**: DALL-E 3 sangat patuh pada instruksi jenis huruf seperti `sans-serif Arial font` sehingga teks label nama benda di bawah gambar tidak akan berantakan atau *typo*.
        * **Parameter Negatif Tambahan**: Ditambahkan larangan `--no cursive-fonts handwritten-fonts` untuk mencegah AI menggunakan gaya tulisan tangan atau huruf sambung yang sulit dibaca.
        """)
