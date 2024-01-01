import os
from dotenv import load_dotenv

load_dotenv()

api_id = int(os.getenv("API_ID", "29486311"))
api_hash = os.getenv("API_HASH", "ffdc688dc4eee8d2585cb24155188432")
bot_token = os.getenv("BOT_TOKEN", "")
# =========================================================== #

db_url = os.getenv("DB_URL", "mongodb+srv://kikoy:kikoy6969@cluster0.vooxu.mongodb.net/?retryWrites=true&w=majority")
db_name = os.getenv("DB_NAME", "vibes") #bisa diganti sesuai kebutuhan
# =========================================================== #

channel_1 = int(os.getenv("CHANNEL_1", "-1001642440731"))
channel_2 = int(os.getenv("CHANNEL_2", "-1001270258384")) #untuk group comentar user
channel_log = int(os.getenv("CHANNEL_LOG", "-1002110504220"))
# =========================================================== #

id_admin = int(os.getenv("ID_ADMIN", "957521020"))
# =========================================================== #

batas_kirim = int(os.getenv("BATAS_KIRIM", "5"))
# =========================================================== #

biaya_kirim = int(os.getenv("BIAYA_KIRIM", "20"))
# =========================================================== #

hastag = os.getenv("HASTAG", "#qq #aa #vibeboy #vibegirl #vibespill #vibestory").replace(" ", "|").lower()
# =========================================================== #

pic_boy = os.getenv("PIC_BOY", "https://telegra.ph/fwbboy-12-03")
pic_girl = os.getenv("PIC_GIRL", "https://telegra.ph/fwbgirl-12-03")
# =========================================================== #

pesan_join = os.getenv("PESAN_JOIN", """
Kamu harus join di CHANNEL & GROUP yang ada dibawah untuk dapat mengirim pesan.
""")
start_msg = os.getenv("START_MSG", """
Halo {mention} 😍

vibesfess bot adalah bot promote yang dapat digunakan untuk mencari teman, pacar, dll serta dapat digunakan untuk mengirim menfess, gunakan hastag dibawah untuk mengirim pesan:

#VibeBoy / #VibeGirl : untuk mencari teman, pasangan, partner dll.
#VibeSpill : untuk spill sesuatu.
#VibeStory : untuk berbagi cerita/pengalaman.
""")

gagalkirim_msg = os.getenv("GAGAL_KIRIM", """
{mention} pesanmu gagal terkirim 🙅, harap gunakan hastag : 

#VibeBoy / #VibeGirl : untuk mencari teman, pasangan, partner dll.
#VibeSpill : untuk spill sesuatu
#VibeStory : untuk berbagi cerita/pengalaman.

bot create by @flyxre
""")
