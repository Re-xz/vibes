import os
from dotenv import load_dotenv

load_dotenv()

api_id = int(os.getenv("API_ID", "29486311"))
api_hash = os.getenv("API_HASH", "ffdc688dc4eee8d2585cb24155188432")
bot_token = os.getenv("BOT_TOKEN", "")
# =========================================================== #

db_url = os.getenv("DB_URL", "mongodb+srv://kikoy:kikoy6969@cluster0.vooxu.mongodb.net/?retryWrites=true&w=majority")
db_name = os.getenv("DB_NAME", "fwbx") #bisa diganti sesuai kebutuhan
# =========================================================== #

channel_1 = int(os.getenv("CHANNEL_1", "-1001197188587"))
channel_2 = int(os.getenv("CHANNEL_2", "-1001680642097")) #untuk group comentar user
channel_log = int(os.getenv("CHANNEL_LOG", "-1002109996381"))
# =========================================================== #

id_admin = int(os.getenv("ID_ADMIN", "957521020"))
# =========================================================== #

batas_kirim = int(os.getenv("BATAS_KIRIM", "2"))
# =========================================================== #

biaya_kirim = int(os.getenv("BIAYA_KIRIM", "20"))
# =========================================================== #

hastag = os.getenv("HASTAG", "#fwbgirl #fwbboy #fwbspill #fwbstory").replace(" ", "|").lower()
# =========================================================== #

pic_boy = os.getenv("PIC_BOY", "https://telegra.ph/fwbboy-12-03")
pic_girl = os.getenv("PIC_GIRL", "https://telegra.ph/fwbgirl-12-03")
# =========================================================== #

pesan_join = os.getenv("PESAN_JOIN", """
Kamu harus join di CHANNEL & GROUP yang ada dibawah untuk dapat mengirim pesan ke @friendwithbenefitx
""")
start_msg = os.getenv("START_MSG", """
Halo {mention} 😍

fwbbase bot adalah bot promote yang dapat digunakan untuk mencari teman, pacar, dll serta dapat digunakan untuk mengirim menfess, gunakan hastag dibawah untuk mengirim pesan:

#FwbBoy / #FwbGirl : untuk mencari teman, pasangan, partner dll.
#FwbSpill : untuk spill sesuatu.
#FwbStory : untuk berbagi cerita/pengalaman.
""")

gagalkirim_msg = os.getenv("GAGAL_KIRIM", """
{mention} pesanmu gagal terkirim 🙅, harap gunakan hastag : 

#FwbBoy / #FwbGirl : untuk mencari teman, pasangan, partner dll.
#FwbSpill : untuk spill sesuatu
#FwbStory : untuk berbagi cerita/pengalaman.

jangan lupa join @caripartnerfwb
""")
