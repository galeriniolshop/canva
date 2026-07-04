import streamlit as st

# Judul Aplikasi
st.title("🎨 Canva Contributor Element Prompt Generator")
st.write("Generate prompt AI yang siap menghasilkan elemen desain (PNG/Vektor) berkualitas untuk Canva.")

# 1. Pilihan Jenis Elemen
element_type = st.selectbox(
    "Pilih Jenis Elemen:",
    ["3D Renders / Pop-out", "Flat Vector Illustration", "Watercolors", "Line Art / Minimalist", "Sticker Style"]
)

# 2. Input Objek Utama
subject = st.text_input("Objek Utama (Contoh: 'cute cat holding a coffee cup', 'aesthetic tropical leaf'):")

# 3. Pilihan Warna (Palette)
color_style = st.selectbox(
    "Pilih Gaya Warna:",
    ["Pastel colors", "Vibrant & Bold", "Earth tones / Boho", "Neon / Futuristic", "Monochrome", "Custom (Tulis di bawah)"]
)

custom_color = ""
if color_style == "Custom (Tulis di bawah)":
    custom_color = st.text_input("Masukkan warna kustom (Contoh: 'soft pink and mint green'):")

# 4. Tombol Generate
if st.button("Generate Prompt ✨"):
    if not subject:
        st.warning("Mohon isi objek utama terlebih dahulu!")
    else:
        # Menentukan gaya warna yang digunakan
        selected_color = custom_color if color_style == "Custom (Tulis di bawah)" else color_style
        
        # Pengatur kata kunci isolasi agar background putih/transparan mudah dihapus
        isolation_keywords = "isolated on a solid white background, die-cut, no shadows, professional graphic asset, commercial design, asset for Canva"
        
        # Logika pembentukan prompt berdasarkan jenis elemen
        if element_type == "3D Renders / Pop-out":
            prompt = f"3D icon of {subject}, claymation style, smooth glossy texture, {selected_color}, cute and modern, {isolation_keywords}, high resolution, 8k render"
        
        elif element_type == "Flat Vector Illustration":
            prompt = f"Flat vector illustration of {subject}, cute aesthetic, clean lines, geometric shapes, {selected_color}, corporate Memphis style, {isolation_keywords}, SVG style"
        
        elif element_type == "Watercolors":
            prompt = f"Beautiful watercolor illustration of {subject}, soft edges, hand-drawn look, detailed textures, {selected_color}, {isolation_keywords}, artistic and elegant"
        
        elif element_type == "Line Art / Minimalist":
            prompt = f"Minimalist continuous line art of {subject}, elegant and simple, black lines with accent {selected_color} shapes, {isolation_keywords}, aesthetic design"
        
        elif element_type == "Sticker Style":
            prompt = f"Kawaii sticker design of {subject}, thick white outline, bold colors, {selected_color}, cartoon style, fun and playful, {isolation_keywords}"

        # Menampilkan Hasil
        st.success("Prompt berhasil dibuat!")
        st.text_area("Salin prompt di bawah ini untuk Midjourney / DALL-E / Leonardo:", value=prompt, height=100)
        
        # Tips Tambahan untuk Kontributor
        st.info("""
        💡 **Tips Canva Contributor:**
        * Gunakan tools seperti **Photoroom** atau **Remove.bg** untuk menghapus background putih menjadi transparan sebelum di-upload ke Canva.
        * Jika menggunakan Midjourney, Anda bisa menambahkan parameter `--no background gradients` di akhir prompt untuk hasil yang lebih bersih.
        """)
