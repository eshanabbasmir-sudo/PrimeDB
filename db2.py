#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════════
#   PHANTOM INTEL  //  Phone Intelligence Framework  v2.0
#   [ For authorized & educational use only ]
# ═══════════════════════════════════════════════════════════════════

import requests, sys, time, os, json, random, string
from datetime import datetime

# ── ANSI Codes ──────────────────────────────────────────────────────
R   = "\033[1;31m"
G   = "\033[1;32m"
Y   = "\033[1;33m"
B   = "\033[1;34m"
C   = "\033[1;36m"
M   = "\033[1;35m"
W   = "\033[1;37m"
DIM = "\033[2m"
BLK = "\033[1;30m"
RST = "\033[0m"
BG  = "\033[40m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def sleep(n): time.sleep(n)

def rchar():
    return random.choice("ABCDEF0123456789@#$%&*!?<>[]{}|/\\^~")

def glitch_text(text, passes=2):
    """Print text with a glitch/decrypt animation"""
    length = len(text)
    for p in range(passes * length):
        scrambled = ""
        for i, ch in enumerate(text):
            if p >= (passes - 1) * length + i:
                scrambled += ch
            elif ch == " ":
                scrambled += " "
            else:
                scrambled += random.choice("ABCDEF0123456789@#$%!?")
        print(f"\r{C}{scrambled}{RST}", end="", flush=True)
        time.sleep(0.012)
    print(f"\r{W}{text}{RST}")

def matrix_rain(lines=6, width=60, duration=0.04):
    """Mini matrix rain effect"""
    chars = "ﾊﾐﾋｰｳｼﾅﾓﾆｻﾜﾂｵﾘｱﾎﾃﾏｹﾒｴｶｷﾑﾕﾗｾﾈｽﾀﾇﾍ01アイウエオカキクケコ"
    for _ in range(lines):
        row = ""
        for _ in range(width):
            row += random.choice([G, DIM+G, C]) + random.choice(chars)
        print(row + RST)
        time.sleep(duration)

def typewriter(text, delay=0.025, color=W):
    for ch in text:
        print(f"{color}{ch}{RST}", end="", flush=True)
        time.sleep(delay)
    print()

def status_line(msg, status="RUNNING", color=Y):
    ts = datetime.now().strftime("%H:%M:%S")
    print(f"  {DIM}[{ts}]{RST}  {BLK}▶{RST}  {color}{msg:<45}{RST}  [{color}{status}{RST}]")
    sleep(0.15)

def fake_scan_lines():
    modules = [
        ("Loading exploit modules",         G,  "OK"),
        ("Bypassing firewall rules",         Y,  "BYPASSED"),
        ("Injecting payload headers",        C,  "INJECTED"),
        ("Establishing encrypted tunnel",    G,  "SECURE"),
        ("Spoofing origin IP",               M,  "MASKED"),
        ("Connecting to remote nodes",       Y,  "LINKED"),
        ("Authenticating to data nodes",     G,  "AUTH OK"),
        ("Enumerating OSINT vectors",        C,  "ACTIVE"),
        ("Initializing SIM lookup engine",   G,  "READY"),
        ("Initializing CallerID engine",     G,  "READY"),
    ]
    for msg, col, st in modules:
        status_line(msg, st, col)

def hacker_progress(label, width=45):
    """Animated hacking-style progress bar"""
    print(f"\n  {BLK}╔══╗{RST} {Y}{label}{RST}")
    bar_chars = ["░", "▒", "▓", "█"]
    filled = ""
    print(f"  {BLK}╚══╝{RST} ", end="")
    for i in range(width):
        filled += random.choice(["█", "▓"])
        pct = int((i + 1) / width * 100)
        display = f"\r  {BLK}╚══╝{RST} {G}{filled:<{width}}{RST} {W}{pct:>3}%{RST}  {DIM}{rchar()}{rchar()}{rchar()}{RST}"
        print(display, end="", flush=True)
        time.sleep(random.uniform(0.02, 0.055))
    print(f"\r  {BLK}╚══╝{RST} {G}{'█'*width}{RST} {G}100%{RST}  {G}✔ DONE{RST}   ")

def banner():
    clear()
    matrix_rain(4, 62, 0.03)
    print(f"""
{R}██████╗ {C}██╗  ██╗{R} █████╗ {C}███╗  ██╗{R}████████╗{C}██████╗ {R}███╗  ███╗
{R}██╔══██╗{C}██║  ██║{R}██╔══██╗{C}████╗ ██║{R}╚══██╔══╝{C}██╔══██╗{R}████╗████║
{R}██████╔╝{C}███████║{R}███████║{C}██╔██╗██║{R}   ██║   {C}██║  ██║{R}██╔████╔██║
{R}██╔═══╝ {C}██╔══██║{R}██╔══██║{C}██║╚████║{R}   ██║   {C}██║  ██║{R}██║╚██╔╝██║
{R}██║     {C}██║  ██║{R}██║  ██║{C}██║ ╚███║{R}   ██║   {C}██████╔╝{R}██║ ╚═╝ ██║
{R}╚═╝     {C}╚═╝  ╚═╝{R}╚═╝  ╚═╝{C}╚═╝  ╚══╝{R}   ╚═╝   {C}╚═════╝ {R}╚═╝     ╚═╝{RST}
""")
    print(f"  {DIM}{'─'*62}{RST}")
    print(f"  {G}  ██ {W}PHONE NUMBER INTELLIGENCE FRAMEWORK  {G}██{RST}")
    print(f"  {DIM}  version 2.0  //  Multi-Source OSINT Engine  //  PK Edition{RST}")
    print(f"  {DIM}{'─'*62}{RST}")
    print(f"\n  {R}[!]{RST} {DIM}Use only on numbers you own or have authorization to scan.{RST}\n")
    sleep(0.4)

def boot_sequence():
    print(f"\n  {C}SYSTEM BOOT SEQUENCE INITIATED ...{RST}\n")
    sleep(0.3)
    fake_scan_lines()
    print(f"\n  {G}[✔]{RST} {W}All systems operational. Ready to breach.{RST}\n")
    sleep(0.5)

def section_header(title, icon=""):
    print(f"\n{R}  ╔{'═'*54}╗{RST}")
    print(f"{R}  ║{RST}  {icon}  {C}{title:<50}{RST}  {R}║{RST}")
    print(f"{R}  ╚{'═'*54}╝{RST}")

def field(key, value, icon="▸"):
    tag = f"[{key}]"
    if value and str(value).strip() not in ("", "null", "None", "N/A"):
        print(f"  {BLK}│{RST}  {DIM}{icon}{RST} {Y}{tag:<22}{RST}  {G}{value}{RST}")
    else:
        print(f"  {BLK}│{RST}  {DIM}{icon}{RST} {Y}{tag:<22}{RST}  {DIM}── NULL ──{RST}")

def fake_hex_dump(label):
    """Print a few lines of fake hex data for atmosphere"""
    print(f"\n  {DIM}── raw packet intercept ── {label} ──{RST}")
    for _ in range(3):
        addr = f"0x{random.randint(0x1000,0xFFFF):04X}"
        hexb = " ".join(f"{random.randint(0,255):02X}" for _ in range(16))
        asc  = "".join(chr(random.randint(33,126)) for _ in range(16))
        print(f"  {DIM}{BLK}{addr}{RST}  {DIM}{hexb}{RST}  {DIM}{asc}{RST}")
    print()

def validate_number(raw):
    digits = raw.replace(" ", "").replace("-", "").replace("+", "")
    if not digits.isdigit():
        return None, "Non-digit characters found"
    if digits.startswith("03") and len(digits) == 11:
        return digits, None
    if digits.startswith("923") and len(digits) == 12:
        return "0" + digits[2:], None
    if digits.startswith("92") and len(digits) == 12:
        return "0" + digits[2:], None
    if len(digits) == 10 and digits.startswith("3"):
        return "0" + digits, None
    return digits, None

def fetch_sim_data(number):
    url = f"https://paksimsdata.pro/api.php?number={number}"
    hacker_progress("Breaching SIM operator database")
    fake_hex_dump("SIM NODE")
    try:
        r = requests.get(url, timeout=10,
                         headers={"User-Agent": "Mozilla/5.0"})
        r.raise_for_status()
        return r.json()
    except requests.exceptions.ConnectionError:
        print(f"  {R}[ERR]{RST} SIM API unreachable — host down or blocked")
    except requests.exceptions.Timeout:
        print(f"  {R}[ERR]{RST} SIM API timed out")
    except requests.exceptions.HTTPError as e:
        print(f"  {R}[ERR]{RST} HTTP {e}")
    except json.JSONDecodeError:
        print(f"  {R}[ERR]{RST} Malformed response — JSON decode failed")
    return None

def fetch_caller_name(number):
    if number.startswith("0"):
        intl = "92" + number[1:]
    else:
        intl = number
    url = (f"https://plain-cell-a513.af7u76.workers.dev//app/getnames.jsp"
           f"?cli={intl}&lang=en&is_callerid=true&is_search=false")
    hacker_progress("Cracking caller-ID social records")
    fake_hex_dump("SOCIAL NODE")
    try:
        r = requests.get(url, timeout=10,
                         headers={"User-Agent": "Mozilla/5.0"})
        r.raise_for_status()
        return r.json()
    except requests.exceptions.ConnectionError:
        print(f"  {R}[ERR]{RST} CallerID API unreachable")
    except requests.exceptions.Timeout:
        print(f"  {R}[ERR]{RST} CallerID API timed out")
    except requests.exceptions.HTTPError as e:
        print(f"  {R}[ERR]{RST} HTTP {e}")
    except json.JSONDecodeError:
        print(f"  {R}[ERR]{RST} Malformed response — JSON decode failed")
    return None

def display_sim(data, number):
    section_header("SIM / OPERATOR INTELLIGENCE", "📶")
    if not data:
        print(f"\n  {R}  [✗] ZERO records extracted from SIM node{RST}")
        return
    print(f"  {DIM}  ── decrypting payload ──{RST}")
    sleep(0.3)
    field("NUMBER",      data.get("number")     or number,           "📱")
    field("OWNER NAME",  data.get("name"),                           "👤")
    field("CNIC",        data.get("cnic"),                           "🪪")
    field("OPERATOR",    data.get("operator")   or data.get("sim"),  "📡")
    field("REGION",      data.get("region")     or data.get("city"), "🗺️")
    field("PROVINCE",    data.get("province"),                       "🏙️")
    field("STATUS",      data.get("status"),                         "🔘")
    field("REG DATE",    data.get("reg_date")   or data.get("date"), "📅")
    field("ADDRESS",     data.get("address"),                        "🏠")
    field("CONN TYPE",   data.get("type") or data.get("connection_type"), "🔗")
    known = {"number","name","cnic","operator","sim","region","city",
             "province","status","reg_date","date","address","type","connection_type"}
    for k, v in data.items():
        if k not in known and v:
            field(k.upper(), str(v), "ℹ️")

def display_caller(data, number):
    section_header("CALLER-ID / SOCIAL INTELLIGENCE", "📛")
    if not data:
        print(f"\n  {R}  [✗] ZERO records extracted from CallerID node{RST}")
        return
    print(f"  {DIM}  ── decrypting payload ──{RST}")
    sleep(0.3)
    entries = data if isinstance(data, list) else [data]
    for idx, e in enumerate(entries, 1):
        if len(entries) > 1:
            print(f"\n  {M}  ── Record #{idx} ──{RST}")
        field("NAME",       e.get("name")    or e.get("displayName"), "👤")
        field("SCORE",      e.get("score"),                           "⭐")
        field("SOURCE",     e.get("source"),                          "🌐")
        field("SPAM SCORE", e.get("spamScore"),                       "⚠️")
        field("CATEGORY",   e.get("category"),                        "🏷️")
        field("COUNTRY",    e.get("country") or e.get("countryCode"), "🌍")
        field("CARRIER",    e.get("carrier"),                         "📡")
        field("LINE TYPE",  e.get("lineType"),                        "📞")
        known = {"name","displayName","score","source","spamScore",
                 "category","country","countryCode","carrier","lineType"}
        for k, v in e.items():
            if k not in known and v:
                field(k.upper(), str(v), "ℹ️")

def final_report(number, sim_ok, caller_ok):
    ts = datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
    print(f"\n{R}  ╔{'═'*54}╗{RST}")
    print(f"{R}  ║{RST}  {W}  SCAN COMPLETE — MISSION REPORT{RST}{'':>20}{R}║{RST}")
    print(f"{R}  ╠{'═'*54}╣{RST}")
    print(f"{R}  ║{RST}  {Y}  Target   {RST}: {W}{number:<40}{RST}  {R}║{RST}")
    print(f"{R}  ║{RST}  {Y}  SIM Data {RST}: {G if sim_ok else R}{'EXTRACTED' if sim_ok else 'FAILED':<40}{RST}  {R}║{RST}")
    print(f"{R}  ║{RST}  {Y}  CallerID {RST}: {G if caller_ok else R}{'EXTRACTED' if caller_ok else 'FAILED':<40}{RST}  {R}║{RST}")
    print(f"{R}  ║{RST}  {Y}  Time     {RST}: {DIM}{ts:<40}{RST}  {R}║{RST}")
    print(f"{R}  ╚{'═'*54}╝{RST}")
    print(f"\n  {DIM}  [ PHANTOM INTEL — Terminate session? Press ENTER ]{RST}  ", end="")
    input()

def main():
    banner()
    boot_sequence()

    if len(sys.argv) > 1:
        raw = sys.argv[1]
    else:
        print(f"  {R}┌──[{RST}{W}PHANTOM{RST}{R}@intel]─[~]{RST}")
        print(f"  {R}└──$ {RST}", end="")
        raw = input().strip()

    number, err = validate_number(raw)
    if err:
        print(f"\n  {R}[✗] INVALID TARGET: {err}{RST}\n")
        sys.exit(1)

    print(f"\n  {G}[✔]{RST} Target acquired  →  {R}{number}{RST}")
    print(f"  {Y}[*]{RST} Launching multi-vector intelligence sweep ...\n")
    sleep(0.6)

    sim_data    = fetch_sim_data(number)
    caller_data = fetch_caller_name(number)

    display_sim(sim_data, number)
    display_caller(caller_data, number)
    final_report(number, bool(sim_data), bool(caller_data))

if __name__ == "__main__":
    main()
