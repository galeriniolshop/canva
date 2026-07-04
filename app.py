import streamlit as st

# Judul Aplikasi
st.title("🎨 Canva Contributor Kawaii Clip Art Generator (With Text)")
st.write("Generate prompt AI untuk **Kawaii Doodle Clip Art** lengkap dengan label nama di bawah setiap ikon, persis seperti gaya gambar image_ac3aa8.jpg.")

# 1. Pilihan Tema Objek
st.subheader("1. Tentukan Objek Elemen")
theme_type = st.selectbox(
    "Pilih Fokus Tema:",
    ["Back to School / Cute Education", "Cute Stationery & School Life", "Custom Theme (Tulis di bawah)"]
)

# Input objek spesifik
custom_subject = st.text_input(
    "Daftar Objek (Pisahkan dengan koma):",
    value="school building, school bus, blackboard easel, backpack, notebook, scissors, pencil, apple, basketball, calculator"
)

# 2. Rumus Gaya Visual Gambar image_ac3aa8.jpg + Tambahan Teks Label
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
        # Menambahkan instruksi teks label bahasa inggris yang rapi di bawah objek
        text_instruction = "each item must have its English name text written neatly in a cute simple font directly underneath the icon"

        # Isolasi ketat: nempel langsung di background putih, tanpa border putih luar
        isolation_keywords = (
            f"clean clipart sheet, multiple individual elements, neatly scattered, {text_instruction}, "
            "isolated on a seamless solid pure white background, no outer white sticker borders, "
            "no shadows, professional graphic asset, commercial design, asset for Canva"
        )
        
        # Merangkai prompt akhir
        final_prompt = (
            f"A cute clipart sheet of {theme_type} elements containing {custom_subject}. "
            f"{style_preset}, bright pastel colors, {isolation_keywords}, "
            f"high resolution, clear separation between elements "
            f"--no stickers die-cut white-outlines borders drop-shadows photorealistic 3d-render"
        )

        # Menampilkan Hasil
        st.success("Prompt dengan label nama berhasil dibuat!")
        st.text_area("Salin prompt ini ke DALL-E 3 / Midjourney v6:", value=final_prompt, height=180)
        
        # Tips Tambahan untuk Teks AI
        st.info("""
        💡 **Tips Menggunakan Teks pada AI:**
        * **Gunakan DALL-E 3**: Untuk menghasilkan teks/tulisan yang tepat dan tidak typo, **DALL-E 3** adalah pilihan terbaik dibanding Midjourney.
        * **Fungsi untuk Canva**: Label nama di bawah ikon ini sangat berguna bagi pembeli di Canva sebagai elemen edukasi anak-anak atau *flashcard*. Saat di-vektorisasi, pastikan teks ikut ter-trace dengan rapi.
        """)
