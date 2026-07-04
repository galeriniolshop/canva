import streamlit as st

# Judul Aplikasi
st.title("🎨 Canva Contributor Clip Art Generator")
st.write("Generate prompt AI untuk **Clip Art / Icon Set** dengan opsi gaya Kawaii atau Non-Kawaii murni tanpa wajah.")

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

# 2. OPSI GAYA: Kawaii vs Non-Kawaii (Koreksi Mutlak)
st.subheader("2. Pilihan Gaya Visual")
style_option = st.radio(
    "Pilih Gaya Ikon:",
    ["Kawaii Style (Imut, Ada Wajah Karakter)", "Non-Kawaii Style (Polos, Objek Murni Tanpa Wajah)"]
)

# 3. Tombol Generate
if st.button("Generate Clip Art Prompt ✨"):
    if not custom_subject:
        st.warning("Mohon isi daftar objek terlebih dahulu!")
    else:
        # Pembedaan Gaya yang Jauh Lebih Tegas
        if "Kawaii" in style_option:
            style_preset = (
                "Cute kawaii doodle clipart style, prominent thick black outlines, bold clean linework, "
                "smooth rounded corners, adorable chibi faces with big shiny black eyes and cute smiles on each object, "
                "2d flat vector illustration look, simple soft shading"
            )
            negative_param = "--no stickers die-cut white-outlines borders drop-shadows photorealistic 3d-render"
        else:
            # Menggunakan istilah mekanis/objek mati agar AI tidak memunculkan karakter hidup
            style_preset = (
                "Standard flat design clipart style, prominent thick black outlines, bold clean linework, "
                "smooth rounded corners, inanimate objects only, realistic item details, literal item representation, "
                "2d flat vector illustration design, simple neat shading"
            )
            # Menambahkan larangan wajah pada parameter negatif agar lebih ampuh di Midjourney/Leonardo
            negative_param = "--no faces eyes mouth characters stickers die-cut white-outlines borders drop-shadows photorealistic 3d-render"

        # Instruksi teks label di bawah objek
        text_instruction = "each item must have its English name text written neatly in a cute simple font directly underneath the icon"

        # Isolasi ketat tanpa border putih luar (mengikuti koreksi gambar sebelumnya)
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
        st.success(f"Prompt gaya {'Kawaii' if 'Kawaii' in style_option else 'Non-Kawaii'} berhasil dibuat!")
        st.text_area("Salin prompt ini ke DALL-E 3 / Midjourney v6:", value=final_prompt, height=180)
        
        # Tips Tambahan
        st.info(f"""
        💡 **Mengapa versi Non-Kawaii sekarang berbeda?**
        * Kata kunci bertema karakter hidup telah dihapus total dari instruksi utama.
        * Ditambahkan frasa **`inanimate objects only`** (hanya benda mati) dan **`literal item representation`** (representasi benda apa adanya).
        * Perintah negatif di ujung prompt ditambahkan parameter khusus: **`--no faces eyes mouth characters`** untuk memblokir AI agar tidak iseng menggambar wajah imut.
        """)
