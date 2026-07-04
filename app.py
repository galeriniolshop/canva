import streamlit as st

# Judul Aplikasi
st.title("🎨 Canva Contributor Kawaii Clip Art Generator")
st.write("Generate prompt AI khusus untuk menghasilkan **Kawaii Doodle Clip Art** persis seperti gaya gambar image_ac3aa8.jpg.")

# 1. Pilihan Tema Objek
st.subheader("1. Tentukan Objek Elemen")
theme_type = st.selectbox(
    "Pilih Fokus Tema:",
    ["Back to School / Cute Education", "Cute Stationery & School Life", "Custom Theme (Tulis di bawah)"]
)

# Input objek spesifik yang disesuaikan dengan contoh gambar
custom_subject = st.text_input(
    "Daftar Objek (Pisahkan dengan koma):",
    value="school building, school bus, blackboard easel, backpack, notebooks, crayons with cute faces, scissors, pencils, apple, sports balls with cute faces"
)

# 2. Rumus Gaya Visual Gambar image_ac3aa8.jpg
style_preset = (
    "Cute kawaii doodle clipart style, prominent thick black outlines, bold clean linework, "
    "smooth rounded corners, adorable chibi faces with big shiny black eyes and cute smiles on each object, "
    "2d flat vector illustration look, simple soft shading"
)

# 3. Tombol Generate
if st.button("Generate Kawaii Clip Art Prompt ✨"):
    if not custom_subject:
        st.warning("Mohon isi daftar objek terlebih dahulu!")
    else:
        # Isolasi ketat: nempel langsung di background putih, tanpa border putih luar (no white sticker outline)
        isolation_keywords = (
            "clean clipart sheet, multiple individual elements, neatly scattered, "
            "isolated on a seamless solid pure white background, no outer white sticker borders, "
            "no shadows, professional graphic asset, commercial design, asset for Canva"
        )
        
        # Merangkai prompt akhir
        final_prompt = (
            f"A cute clipart sheet of {theme_type} elements including {custom_subject}. "
            f"{style_preset}, bright pastel colors, {isolation_keywords}, "
            f"high resolution, clear separation between elements "
            f"--no stickers die-cut white-outlines borders drop-shadows photorealistic 3d-render"
        )

        # Menampilkan Hasil
        st.success("Prompt gaya 'Kawaii Clip Art' berhasil dikunci!")
        st.text_area("Salin prompt ini ke Midjourney / DALL-E 3 / Leonardo.ai:", value=final_prompt, height=160)
        
        # Tips Tambahan
        st.info("""
        💡 **Mengapa prompt ini menghasilkan gaya seperti image_ac3aa8.jpg?**
        * **`thick black outlines`**: Menghasilkan garis hitam tebal yang membingkai setiap karakter/objek dengan tegas sehingga mudah di-trace.
        * **`no outer white sticker borders` & `--no white-outlines borders`**: Menghapus total efek stiker (garis putih luar) yang sebelumnya Anda keluhkan, sehingga objek langsung menempel di background putih bersih.
        * **`big shiny black eyes`**: Mengunci gaya mata ikon agar bulat besar dan berkilau khas karakter chibi Jepang.
        """)
