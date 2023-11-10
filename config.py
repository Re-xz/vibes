import os
from dotenv import load_dotenv

load_dotenv()

api_id = int(os.getenv("API_ID", "29486311"))
api_hash = os.getenv("API_HASH", "ffdc688dc4eee8d2585cb24155188432")
bot_token = os.getenv("BOT_TOKEN", "")
# =========================================================== #

db_url = os.getenv("DB_URL", "mongodb+srv://kikoy:kikoy6969@cluster0.vooxu.mongodb.net/?retryWrites=true&w=majority")
db_name = os.getenv("DB_NAME", "dxtfess") #bisa diganti sesuai kebutuhan
# =========================================================== #

channel_1 = int(os.getenv("CHANNEL_1", "-1002034769079"))
channel_2 = int(os.getenv("CHANNEL_2", "-1001610283560")) #untuk group comentar user
channel_log = int(os.getenv("CHANNEL_LOG", "-1001710331413"))
# =========================================================== #

id_admin = int(os.getenv("ID_ADMIN", "957521020"))
# =========================================================== #

batas_kirim = int(os.getenv("BATAS_KIRIM", "3"))
# =========================================================== #

biaya_kirim = int(os.getenv("BIAYA_KIRIM", "20"))
# =========================================================== #

hastag = os.getenv("HASTAG", "#ss #aa #DxtBoy #DxtAsk #DxtGirl #DxtSpill #DxtStory").replace(" ", "|").lower()
# =========================================================== #

pic_boy = os.getenv("PIC_BOY", "https://telegra.ph/file/c67bd36023648dc777bd9.jpg")
pic_girl = os.getenv("PIC_GIRL", "https://telegra.ph/file/cb885bcbf5081dbd45f27.jpg")
# =========================================================== #

pesan_join = os.getenv("PESAN_JOIN", """
Halo Sobat DxT 👋

Kamu harus bergabung di CHANNEL & GROUP Terlebih dahulu untuk mengirim pesan ke @dxtmenfess

Join Ke Channel & Group Kemudian Tekan /start ⤵️
""")
start_msg = os.getenv("START_MSG", """
Halo {mention} 😍

DxT Autopost adalah bot autopost, semua pesan yang dikirimkan ke bot ini akan otomatis dikirim ke channel @dxtmenfess, gunakan hastag dibawah untuk mengirim pesan:

#DxtBoy / #DxtGirl : untuk mencari teman, pasangan, partner dll.
#DxtAsk : untuk bertanya.
#DxtSpill : untuk spill sesuatu.
#DxtStory : untuk berbagi cerita/pengalaman.

Contoh :
i have crush on you #DxtSpill
""")

gagalkirim_msg = os.getenv("GAGAL_KIRIM", """
{mention} pesanmu gagal terkirim 🙅, harap gunakan hastag : 

#DxtBoy / #DxtGirl : untuk mencari teman, pasangan, partner dll.
#DxtAsk : untuk bertanya
#DxtSpill : untuk spill sesuatu
#DxtStory : untuk berbagi cerita/pengalaman.

untuk pertanyaan silahkan gabung @Dextructive
""")
