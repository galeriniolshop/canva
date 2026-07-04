import streamlit as st

# Judul Aplikasi
st.title("🎨 Canva Contributor Clip Art Generator")
st.write("Generate prompt AI untuk **Clip Art / Icon Set** dengan opsi gaya Kawaii atau Non-Kawaii, dikunci tanpa border putih luar seperti gaya image_ac3aa8.jpg.")

# 1. Pilihan Tema & Objek
st.subheader("1. Tentukan Objek Elemen")
theme_type = st.selectbox(
    "Pilih Fokus Tema:",
    ["Back to School / Cute Education", "Cute Stationery & School Life", "Custom Theme (Tulis di bawah)"]
)

custom_subject = st.text_input(
    "Daftar Objek (Pisahkan dengan koma):",
    value="school building, school bus, blackboard easel, backpack, notebook, scissors, pencil, apple, basketball, calculator"
)

# 2. OPSI GAYA: Kawaii vs Non-Kawaii
st.subheader("2. Pilihan Gaya Visual")
style_option = st.radio(
    "Pilih Gaya Ikon:",
    ["Kawaii Style (Imut, Menggemaskan dengan Wajah)", "Non-Kawaii Style (Bersih, Minimalis & Profesional)"]
)

# 3. Tombol Generate
if st.button("Generate Clip Art Prompt ✨"):
    if not custom_subject:
        st.warning("Mohon isi daftar objek terlebih dahulu!")
    else:
        # Menentukan base style berdasarkan pilihan user
        if "Kawaii" in style_option:
            style_preset = (
                "Cute kawaii doodle clipart style, prominent thick black outlines, bold clean linework, "
                "smooth rounded corners, adorable chibi faces with big shiny black eyes and cute smiles on each object, "
                "2d flat vector illustration look, simple soft shading"
            )
        else:
            style_preset = (
                "Modern minimal clipart style, prominent thick black outlines, bold clean linework, "
                "smooth rounded corners, object only, NO faces, NO eyes, NO mouth, clean and professional look, "
                "2d flat vector illustration design, simple neat shading"
            )

        # Instruksi teks label di bawah objek
        text_instruction = "each item must have its English name text written neatly in a cute simple font directly underneath the icon"

        # Isolasi ketat tanpa border putih luar (mengikuti koreksi image_a07065.png & image_ac3aa8.jpg)
        isolation_keywords = (
            f"clean clipart sheet, multiple individual elements, neatly scattered, {text_instruction}, "
            "isolated on a seamless solid pure white background, no outer white sticker borders, "
            "no shadows, professional graphic asset, commercial design, asset for Canva"
        )
        
        # Merangkai prompt akhir
        final_prompt = (
            f"A colorful clipart sheet of {theme_type} elements containing {custom_subject}. "
            f"{style_preset}, bright pastel colors, {isolation_keywords}, "
            f"high resolution, clear separation between elements "
            f"--no stickers die-cut white-outlines borders drop-shadows photorealistic 3d-render"
        )

        # Menampilkan Hasil
        st.success(f"Prompt gaya {'Kawaii' if 'Kawaii' in style_option else 'Non-Kawaii'} berhasil dibuat!")
        st.text_area("Salin prompt ini ke DALL-E 3 / Midjourney v6:", value=final_prompt, height=180)
        
        # Tips Tambahan
        st.info(f"""
        💡 **Info Gaya Baru:**
        * **Jika memilih Non-Kawaii**: Prompt otomatis menambahkan instruksi ketat `NO faces, NO eyes, NO mouth` agar AI fokus menggambar bentuk objek aslinya saja secara bersih dan minimalis namun tetap mempertahankan garis luar hitam tebal yang luwes saat di-vektorisasi.
        * **Rekomendasi Generator**: Gunakan **DALL-E 3** agar teks label nama di bawah objek tercetak dengan ejaan yang sempurna.
        """)
