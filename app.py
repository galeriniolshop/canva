import streamlit as st

# Judul Aplikasi
st.title("🎨 Canva Contributor Element Generator (No Sticker Border)")
st.write("Generate prompt AI khusus untuk menghasilkan **Ikon/Elemen Vektor Bersih** tanpa garis tepi putih luar seperti pada gambar image_a07065.png.")

# 1. Pilihan Tema Objek
st.subheader("1. Pilih Tema & Objek")
theme_type = st.selectbox(
    "Pilih Fokus Tema:",
    ["Back to School / School Supplies", "Cute Stationery Set", "Custom Theme (Tulis di bawah)"]
)

# Input objek spesifik
custom_subject = st.text_input(
    "Daftar Objek Spesifik (Pisahkan dengan koma):",
    value="pencil, pen, notebook, backpack, pencil case, ruler, eraser, scissors, glue, crayons, calculator, books, apple, globe, sharpener, tape dispenser, sticky notes"
)

# 2. Pengaturan Gaya Visual (Menghilangkan unsur stiker dan border luar)
st.subheader("2. Pengaturan Gaya (Style)")
style_preset = "Cute cartoon vector illustration, clean fine lines, dark outlines on object details only, no outer white border, flat 2d design, adorable smiley faces on each item"

color_style = st.selectbox(
    "Pilih Palet Warna:",
    ["Bright Pastel colors", "Vibrant & Playful", "Soft Candy tones"]
)

# 3. Tombol Generate
if st.button("Generate Clean Element Prompt ✨"):
    if not custom_subject:
        st.warning("Mohon isi daftar objek terlebih dahulu!")
    else:
        # Menggunakan 'solid white background' murni tanpa 'die-cut' atau 'sticker sheet' agar tidak memancing AI membuat border putih tambahan
        isolation_keywords = "clippable asset sheet, multiple items collection, isolated on a seamless solid white background, no outer shadows, professional graphic asset, commercial design, asset for Canva"
        
        # Merangkai prompt akhir
        final_prompt = (
            f"An asset sheet of {theme_type} elements containing {custom_subject}. "
            f"{style_preset}, {color_style}, neat arrangement of various items, {isolation_keywords}, "
            f"high resolution, ultra detailed --no stickers die-cut outlines borders shadows background-gradients"
        )

        # Menampilkan Hasil
        st.success("Prompt elemen bersih (tanpa garis tepi putih) berhasil dibuat!")
        st.text_area("Salin prompt ini ke Midjourney / DALL-E 3 / Leonardo.ai:", value=final_prompt, height=150)
        
        # Tips Tambahan
        st.info("""
        💡 **Apa yang diubah untuk menghilangkan garis tepi putih?**
        * Perintah `die-cut` dan `thick white outline` telah dihapus total.
        * Ditambahkan perintah `no outer white border`.
        * Parameter negatif `--no stickers die-cut outlines borders` disisipkan di akhir prompt (khusus Midjourney/Leonardo) untuk memaksa AI memotong objek langsung pada batas warnanya, bukan batas putih stiker.
        """)
