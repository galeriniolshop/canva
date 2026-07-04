import streamlit as st

# Judul Aplikasi
st.title("🎨 Canva Contributor Smooth Icon Generator")
st.write("Generate prompt AI untuk ikon berwarna yang **luwes dan tidak kaku** saat diringkas ke bentuk vektor.")

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

# 2. Pengaturan Gaya Visual (Fokus pada kelenturan vektor & warna)
st.subheader("2. Pengaturan Gaya (Style)")
color_preset = st.selectbox(
    "Pilih Gaya Pewarnaan:",
    ["Vibrant colorful with smooth gradients", "Rich pastel colors with soft shading", "Bright playful color palette"]
)

# 3. Tombol Generate
if st.button("Generate Smooth Icon Prompt ✨"):
    if not custom_subject:
        st.warning("Mohon isi daftar objek terlebih dahulu!")
    else:
        # Gaya visual diatur agar garisnya mengalir (fluid) dan tidak kaku/geometris kasar
        style_keywords = (
            f"Cute cartoon icon collection, {color_preset}, fluid curves, smooth dynamic lines, "
            f"organic shapes, no rigid geometric corners, adorable smiley faces on each item, 2d vector art style"
        )
        
        # Isolasi background murni tanpa border putih luar seperti petunjuk sebelumnya
        isolation_keywords = (
            "neatly arranged asset sheet, isolated on a seamless solid white background, "
            "no outer white borders, no outer shadows, clean edges for auto-tracing, commercial design asset"
        )
        
        # Merangkai prompt akhir
        final_prompt = (
            f"An asset sheet of {theme_type} elements containing {custom_subject}. "
            f"{style_keywords}, {isolation_keywords}, high resolution, ultra detailed "
            f"--no stickers die-cut outlines borders shadows jagged-edges 3d-render"
        )

        # Menampilkan Hasil
        st.success("Prompt ikon berwarna & luwes berhasil dibuat!")
        st.text_area("Salin prompt ini ke Midjourney / DALL-E 3 / Leonardo.ai:", value=final_prompt, height=150)
        
        # Tips Tambahan untuk proses Vektorisasi
        st.info("""
        💡 **Tips Agar Vektorisasi (Tracing) Tidak Kaku:**
        * **Gunakan parameter `--no jagged-edges`**: Ini memaksa AI menjaga tepian gambar tetap melengkung halus (*smooth*).
        * **Saat Tracing di Illustrator / Corel / Vectorizer online**: 
          * Naikkan nilai **"Corner Smoothness" / "Smoothness"** pada pengaturan *Image Trace*.
          * Turunkan nilai **"Corners" / "Threshold"** agar software tidak membuat terlalu banyak titik sudut tajam yang kaku.
          * Pilih metode *Color Trace* (bukan Black & White) untuk menangkap gradasi warna halusnya.
        """)
