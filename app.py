import streamlit as st

# Judul Aplikasi
st.title("🎨 Canva Contributor Flat Icon Generator")
st.write("Generate prompt AI untuk **Flat Clipart Set** tanpa garis tepi hitam dan tanpa gradasi, persis seperti gaya gambar image_f0c37f.png.")

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
        # Karakteristik utama image_f0c37f.png: Flat murni, tanpa outline, sangat mudah di-trace
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
            negative_param = "--no outlines linework black-borders gradients shading shadows stickers die-cut photorealistic 3d-render textured"
        else:
            style_preset = (
                f"{vector_preset}, literal inanimate object representation, clean corporate flat design, "
                f"strictly no faces, no eyes, no mouth"
            )
            negative_param = "--no faces eyes mouth characters outlines linework black-borders gradients shading shadows stickers die-cut photorealistic 3d-render textured"

        # Isolasi ketat tanpa border putih luar dan tanpa tulisan nama agar fokus pada bentuk bersih
        isolation_keywords = (
            "clean vector asset sheet, multiple individual elements, neatly scattered, "
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
        st.success(f"Prompt gaya Flat Vector {'Kawaii' if 'Kawaii' in style_option else 'Non-Kawaii'} berhasil dibuat!")
        st.text_area("Salin prompt ini ke DALL-E 3 / Midjourney v6 / Leonardo.ai:", value=final_prompt, height=200)
        
        # Edukasi Tracing Vektor untuk Gaya Ini
        st.info(f"""
        💡 **Mengapa gaya ini paling sempurna untuk Vektor (SVG)?**
        * **`NO outlines, NO linework`**: Menghilangkan garis hitam penutup. Hasil tracing akan berupa potongan bidang warna yang bersih (*solid paths*) sehingga sangat disukai oleh pengguna Canva karena mudah diubah warnanya secara kustom.
        * **`100% solid flat colors`**: Tanpa adanya gradasi atau bayangan lembut, software seperti Adobe Illustrator atau Vectorizer.ai bisa mengubah gambar ini menjadi SVG dalam hitungan detik dengan akurasi hampir 100% mirip aslinya.
        """)
