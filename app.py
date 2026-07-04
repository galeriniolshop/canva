import streamlit as st

# Judul Aplikasi
st.title("🎨 Canva Contributor Sticker Set Generator")
st.write("Generate prompt AI khusus untuk menghasilkan **Sticker Icon Set** bertema sekolah imut seperti gambar contoh.")

# 1. Pilihan Tema Objek (Disesuaikan dengan gaya "Back to School")
st.subheader("1. Pilih Tema & Objek")
theme_type = st.selectbox(
    "Pilih Fokus Tema:",
    ["Back to School / School Supplies", "Cute Stationery Set", "Custom Theme (Tulis di bawah)"]
)

# Input objek spesifik jika ingin kustom
custom_subject = st.text_input(
    "Daftar Objek Spesifik (Pisahkan dengan koma jika banyak, contoh: pencil, notebook, backpack, calculator):",
    value="pencil, pen, notebook, backpack, pencil case, ruler, eraser, scissors, glue, crayons, calculator, books, apple, globe, sharpener, tape dispenser, sticky notes"
)

# 2. Pengaturan Gaya Visual (Dikunci ke gaya gambar image_a00670.jpg)
st.subheader("2. Pengaturan Gaya (Style)")
style_preset = "Kawaii sticker design, cute cartoon vector style, bold clean outlines, adorable smiley faces on each item, soft chibification"

color_style = st.selectbox(
    "Pilih Palet Warna:",
    ["Bright Pastel colors", "Vibrant & Playful", "Soft Candy tones"]
)

# 3. Tombol Generate
if st.button("Generate Sticker Set Prompt ✨"):
    if not custom_subject:
        st.warning("Mohon isi daftar objek terlebih dahulu!")
    else:
        # Keyword isolasi mutlak untuk Canva Contributor agar background bersih tanpa bayangan
        isolation_keywords = "sticker pack sheet, multiple items set, isolated on a solid clean white background, die-cut, no shadows, professional graphic asset, commercial design, asset for Canva"
        
        # Merangkai prompt akhir
        final_prompt = (
            f"A sticker sheet of {theme_type} elements including {custom_subject}. "
            f"{style_preset}, {color_style}, arrangement of various items, {isolation_keywords}, "
            f"flat design, 2d vector look, high resolution, ultra detailed --no shadows background-gradients photorealistic"
        )

        # Menampilkan Hasil
        st.success("Prompt gaya 'Back to School Kawaii' berhasil dibuat!")
        st.text_area("Salin prompt ini ke Midjourney / DALL-E 3 / Leonardo.ai:", value=final_prompt, height=150)
        
        # Tips Tambahan agar hasilnya mirip gambar
        st.info(f"""
        💡 **Tips Optimasi untuk Hasil seperti image_a00670.jpg:**
        * **Midjourney v6**: Gunakan parameter `--style raw` jika hasilnya terlalu realistis. Kode `--no shadows background-gradients` di akhir prompt akan membantu menjaga background tetap putih polos.
        * **DALL-E 3 (ChatGPT)**: Salin langsung prompt di atas. DALL-E sangat pintar mengenali perintah seperti *"smiley faces on each item"*.
        * **Proses Akhir**: Setelah gambar jadi, Anda tinggal memotong masing-masing ikon menggunakan tools vectorizer atau langsung menghapus background putihnya menjadi transparan (PNG).
        """)
