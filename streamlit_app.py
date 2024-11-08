import streamlit as st

# Sahifa boshida menyuni va sahifalarni sozlash
menu_options = ["Bosh sahifa", "Biz bilan bog'lanish", "Mentorlar", "Kurslar", "Biz haqimizda"]
selected_option = st.sidebar.radio("Sahifalar", menu_options)

# CSS orqali faqat fon qo'shish
background_css = '''
    <style>
    .stApp {
        background-image: url("https://pcparch.com/media/pages/work/petronas-towers/47ab7ab432-1722322153/petronas-towers-tower-top.jpg");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        color: white;
    }
    </style>
'''

custom_title = '''
    <style>
    .big-title {
        font-size: 60px;
        font-weight: bold;
        color: black;
        text-align: center;
        margin-top: 20px;
    }
    </style>
    <h1 class="big-title">Renessans</h1>
'''

# CSS ni qo'shish
st.markdown(background_css, unsafe_allow_html=True)

# Sahifani tanlaganda turli kontentlarni ko'rsatish
if selected_option == "Bosh sahifa":
    st.title("Renessans-kelajak bilim bilan yaratiladi!")
    st.write(" ")
    st.write(" ")
    st.write("'Renessans' o'quv markazi bilimga chanqoq, iqtidorli yoshlarni va abituriyentlarni quyidagi")
    st.write("fanlardan o'quv mashg'ulotlariga taklif qiladi:")
    st.write(" ")
    st.write("•MATEMATIKA (2-11-sinlar uchun) ")
    st.write("•INGLIZ TILI (2-11-sinflar uchun)")
    st.write("•IELTS va CEFR")
    st.write("•ONA TILI va ADABIYOT")
    st.write("•KIMYO")
    st.write("•BIOLOGIYA")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write("OLIY TA'LIM MUASSASALARI, PREZIDENT MAKTABLARI, AL-XORAZMIY MAKTABI va")
    st.write("IXTISOSLASHTIRILGAN MAKTABLARga tayyoraglik ko'rmoqchi bo'lgan o'quvchilar uchun")
    st.write("kuchaytirilgan va qo'shimcha dars soatlari mavjud!")
    st.write(" ")
    st.write(" ")
    st.title("O‘quv kurslarimiz afzalliklari:")
    st.write("•Har bir bolaga individual e'tibor")
    st.write("•Temir intizom va talabchanlik")
    st.write("•Ota-onalar bilan bolalar o‘zlashtirishi yuzasidan doimiy muloqotda bo‘lish")
    st.write("•Har bir mavzu yuzasidan chuqurlashtirilgan test sinovlari")
    st.write("•Har oylik blok test sinovlari")

elif selected_option == "Biz bilan bog'lanish":
    st.title("Murojat uchun:")
    st.write("📞 +998 (90) 006-30-10")
    st.write("📞 +998 (99) 728-30-10")
    st.write("📱 @Renessans3010")
    st.write(" ")
    st.write(" ")
    st.write("Manzil:")
    st.write("📍 Parkent tumani, Nomdanak qishlog'i, Chinorli ko'chasi 17-uy.")
    st.write("Shu linkga bosing: https://maps.app.goo.gl/9Vw9n4Nrh6qWR24N8")

elif selected_option == "Mentorlar":
    st.title("Mentorlar")
    st.write("Bu sahifada o'quv markazimizdagi barcha mentorlar haqida ma'lumot olishingiz mumkin.")

elif selected_option == "Kurslar":
    st.title("Kurslarimiz:")
    st.title("MATEMATIKADAN MILLIY SERTIFIKAT guruhlari")
    st.write("Talablar:")
    st.write("✅ Kamida trigonometriya mavzusigacha yaxshi bilishi kerak")
    st.write("✅ O'ziga ishongan va ilmga chanqoq")
    st.write("Kurs afzalliklari:")
    st.write("➕ Haftada 3 marotaba 6 soatdan")
    st.write("➕ O'tilgan mavzular bo'yicha haftaning yakshanba kunlari milliy sertifikat namunasidagi testlar")
    st.write("➕ Saralangan o'quvchilar bilan birga ta'lim olish")
    st.write("Kurs mentori: Xolmatov Oybek")
    st.write("Kurs kunlari:")
    st.write("📆 SESHANBA, PAYSHANBA va SHANBA")
    st.write("⏰ Kurs vaqti: 14:00-20:00")
    st.write("Kurs narxi: 250.000 so‘m")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.title("8-9-10-sinflar uchun matematika darslari")
    st.write("Kurs mentori:  Ahmadjon")
    st.write("Kurs kunlari:")
    st.write("📆 SESHANBA, PAYSHANBA va SHANBA")
    st.write("⏰ Kurs vaqti: 8:00-10:00")
    st.write("Kurs narxi: 200.000 so‘m")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.title("Ingliz tilidan IELTS va CEFR ga tayyorlov guruhlari")
    st.write("Kurs mentori: Normatov Haydar")
    st.write("Kurs kunlari:")
    st.write("📆 SESHANBA, PAYSHANBA va SHANBA")
    st.write("⏰ Kurs vaqti:")
    st.write("'Intermediate' guruhlar uchun: 14:00-16:00")
    st.write("'Elementary' guruhlar uchun: 16:00-18:00")
    st.write("Kurs narxi: 250.000 so‘m")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.title(" INGLIZ TILI dan yangi guruhlari")
    st.title("2-3-sinflar uchun ingliz tilidan darslar")
    st.write("Kurs kunlari:")
    st.write("📆 DUSHANBA, CHORSHANBA va JUMA")
    st.write("⏰ Dars vaqti: 14:00-16:00")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.title("ONA TILI va ADABIYOT")
    st.write("Kurs afzalliklari:")
    st.write("• 2 ta ustoz nazoratida tayyorgarlik")
    st.write("• Qiziqarli dars mashg'ulotlari")
    st.write("• Har bir bolaga individual yondashuv")
    st.write("Kurs kunlari:")
    st.write("📆 CHORSHANBA,JUMA va YAKSHANBA")
    st.write("⏰ Kurs vaqti: 16:00-18:00")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.title("BIOLOGIYA")
    st.write("Kurs mentori: Mirkomolov Ibrohim")
    st.write("Kurs kunlari:")
    st.write("📆 CHORSHANBA,JUMA va YAKSHANBA")
    st.write("⏰ Kurs vaqti:")
    st.write("Chorshanba: 14:00-16:00")
    st.write("Juma: 14:00-16:00")
    st.write("Yakshanba: 8:00-10:00")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.title("Kimyo")
    st.write("Kurs mentori: Mirkomolov Ibrohim")
    st.write("Kurs kunlari:")
    st.write("📆 CHORSHANBA,JUMA va YAKSHANBA")
    st.write("⏰ Kurs vaqti:")
    st.write("Chorshanba: 16:00-18:00")
    st.write("Juma: 16:00-18:00")
    st.write("Yakshanba: 10:00-12:00")



elif selected_option == "Biz haqimizda":
    st.title("Biz haqimizda")
    st.write("Bu Renessans o'quv markazi shaxsiy vebsahifasi.")
