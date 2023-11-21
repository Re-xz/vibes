import os
from dotenv import load_dotenv

load_dotenv()

api_id = int(os.getenv("API_ID", "29486311"))
api_hash = os.getenv("API_HASH", "ffdc688dc4eee8d2585cb24155188432")
bot_token = os.getenv("BOT_TOKEN", "")
# =========================================================== #

db_url = os.getenv("DB_URL", "mongodb+srv://kikoy:kikoy6969@cluster0.vooxu.mongodb.net/?retryWrites=true&w=majority")
db_name = os.getenv("DB_NAME", "ctpfess") #bisa diganti sesuai kebutuhan
# =========================================================== #

channel_1 = int(os.getenv("CHANNEL_1", "-1001197188587"))
channel_2 = int(os.getenv("CHANNEL_2", "-1001680642097")) #untuk group comentar user
channel_log = int(os.getenv("CHANNEL_LOG", "-1002037994205"))
# =========================================================== #

id_admin = int(os.getenv("ID_ADMIN", "957521020"))
# =========================================================== #

batas_kirim = int(os.getenv("BATAS_KIRIM", "5"))
# =========================================================== #

biaya_kirim = int(os.getenv("BIAYA_KIRIM", "20"))
# =========================================================== #

hastag = os.getenv("HASTAG", "#ss #aa #ctpboy #ctpask #ctpgirl #ctpspill #ctpstory").replace(" ", "|").lower()
# =========================================================== #

pic_boy = os.getenv("PIC_BOY", "https://telegra.ph/file/c67bd36023648dc777bd9.jpg")
pic_girl = os.getenv("PIC_GIRL", "https://telegra.ph/file/cb885bcbf5081dbd45f27.jpg")
# =========================================================== #

pesan_join = os.getenv("PESAN_JOIN", """
Halo👋 kamu harus bergabung di CHANNEL & GROUP Terlebih dahulu untuk mengirim pesan ke @ctpmenfess

Join Ke Channel & Group Kemudian Tekan /help ⤵️
""")
start_msg = os.getenv("START_MSG", """
Halo {mention} 😍

ctp bot adalah bot autopost, semua pesan yang dikirimkan ke bot ini akan otomatis dikirim ke channel @ctpmenfess, gunakan hastag dibawah untuk mengirim pesan:

#CtpBoy / #CtpGirl : untuk mencari teman, pasangan, partner dll.
#CtpAsk : untuk bertanya.
#CtpSpill : untuk spill sesuatu.
#CtpStory : untuk berbagi cerita/pengalaman.
""")

gagalkirim_msg = os.getenv("GAGAL_KIRIM", """
{mention} pesanmu gagal terkirim 🙅, harap gunakan hastag : 

#CtpBoy / #CtpGirl : untuk mencari teman, pasangan, partner dll.
#CtpAsk : untuk bertanya
#CtpSpill : untuk spill sesuatu
#CtpStory : untuk berbagi cerita/pengalaman.

untuk pertanyaan silahkan gabung @CariTemanPacar_Online
""")
