"""Build the 'AI agent for real estate' LinkedIn carousel (simple version).

Usage: python3 build.py && node shot.js
"""
import pathlib

H = pathlib.Path(__file__).parent
BRAND = "A Shameless Marketer"
C = {"p": ("#DCC8F2", "#9B6BD6"), "g": ("#C9EDD6", "#2FB36A"), "b": ("#CDE6FA", "#3D9BE0")}


def chips(*items):
    return '<div class="chips">' + "".join(f"<span>{i}</span>" for i in items) + "</div>"


def flow(*items):
    return '<div class="flow">' + '<em>→</em>'.join(f"<span>{i}</span>" for i in items) + "</div>"


S = [
    dict(a="p", label="THE AGENT QUESTION", h=["Too much", "admin?"], band="Let an agent do it.",
         proof='<div class="emoji">📱 💬 📄</div>', take="SELL MORE.<br>TYPE LESS."),
    dict(a="g", label="THE BASICS", h=["AI agent =", "helper."], band="You set the rules. It runs them.",
         proof=flow("Lead", "Sort", "Reply"), take="WRITE THE STEPS.<br>DONE."),
    dict(a="b", label="THE LEAD REPLY", h=["Reply in", "1 minute."], band="Even at a viewing.",
         proof='<div class="vs"><div><small>Before</small>Hours</div><div class="on"><small>After</small>1 min</div></div>',
         take="FAST REPLY<br>WINS."),
    dict(a="p", label="THE LISTING MATCH", h=["New unit?", "Matched."], band="It finds the right buyer.",
         proof=chips("Lead A ✅", "Lead B ❌", "Lead C ✅"), take="YOUR LIST<br>WORKS FOR YOU."),
    dict(a="g", label="THE FOLLOW-UP", h=["Never", "forget", "a lead."], band="Day 3. Day 7. Day 14.",
         proof='<div class="dots"><i></i><b></b><i></i><b></b><i></i></div>', take="FOLLOW-UP<br>IS A SYSTEM."),
    dict(a="b", label="THE PAPERWORK", h=["Stop", "chasing", "documents."], band="It reminds the client.",
         proof=chips("✅ IC", "✅ Payslip", "⏳ Bank statement"), take="LET IT NAG.<br>YOU CLOSE."),
    dict(a="p", label="THE LIMITS", h=["It", "can't", "build trust."], band="That's still your job.",
         proof=chips("✅ Admin", "❌ Advice", "❌ Negotiation"), take="AUTOMATE TASKS.<br>NOT PEOPLE."),
    dict(a="g", label="THE START", h=["Start with", "one", "task."], band="Not ten. One.",
         proof='<div class="cta">Comment “AGENT” 👇</div>', take="SMALL AGENT.<br>BIG TIME SAVED."),
]

CSS = """*{box-sizing:border-box;margin:0}body{background:#ccc}
.s{width:1080px;height:1350px;position:relative;overflow:hidden;font-family:Inter,Arial,sans-serif;color:#111;
background:#F4EBDF;background-image:linear-gradient(#e7ddcf 1px,transparent 1px),linear-gradient(90deg,#e7ddcf 1px,transparent 1px);
background-size:45px 45px;padding:80px 90px;margin-bottom:20px}
.top{display:flex;justify-content:space-between;align-items:center}
.lab{font-weight:800;letter-spacing:3px;font-size:24px}
.logo{background:#FFE000;padding:14px 24px;font-weight:900;font-size:24px}
h1{font-size:132px;line-height:1.02;font-weight:900;letter-spacing:-4px;margin-top:110px}
.hl{background:var(--l);padding:0 14px;position:relative;outline:3px solid var(--d);display:inline-block;line-height:1.05}
.hl:before,.hl:after{content:"";position:absolute;width:24px;height:24px;border-radius:50%;background:var(--d)}
.hl:before{left:-12px;top:-12px}.hl:after{right:-12px;bottom:-12px}
.band{display:inline-block;background:var(--d);color:#fff;font-size:48px;font-weight:800;padding:14px 26px;margin-top:44px}
.proof{margin-top:70px;font-size:40px;font-weight:700}
.emoji{font-size:110px;letter-spacing:20px}
.flow{display:flex;align-items:center;gap:22px}.flow span{background:#fff;border:3px solid var(--d);padding:22px 34px;border-radius:18px}
.flow em{font-style:normal;color:var(--d);font-size:56px}
.chips{display:flex;flex-wrap:wrap;gap:18px}.chips span{background:#fff;padding:20px 30px;border-radius:60px;border:3px solid var(--d)}
.vs{display:flex;gap:24px}.vs div{background:#fff;padding:26px 40px;border-radius:18px;font-size:56px;font-weight:900}
.vs small{display:block;font-size:24px;color:#777;font-weight:600}.vs .on{background:var(--l);outline:3px solid var(--d)}
.dots{display:flex;align-items:center;width:640px}.dots i{width:48px;height:48px;border-radius:50%;background:var(--d)}
.dots b{flex:1;height:6px;background:var(--d)}
.cta{display:inline-block;background:#fff;border:4px dashed var(--d);padding:24px 36px;font-size:52px;font-weight:900}
.take{position:absolute;left:90px;bottom:160px;background:#111;color:#fff;font-weight:900;font-size:58px;line-height:1.08;padding:34px 40px}
.num{position:absolute;right:70px;bottom:120px;font-size:380px;font-weight:900;color:var(--l);line-height:1;letter-spacing:-12px;z-index:0}
.take,.foot{z-index:1}
.foot{position:absolute;left:90px;right:90px;bottom:64px;display:flex;justify-content:space-between;align-items:center;font-size:24px;font-weight:700;color:#444}
.pill{background:#fff;border-radius:40px;padding:14px 28px;font-size:28px;font-weight:800;color:#111}"""


def slide(i, s):
    l, d = C[s["a"]]
    parts = s["h"]
    if len(parts) == 2:
        h = f'{parts[0]}<br><span class="hl">{parts[1]}</span>'
    else:
        h = f'{parts[0]} <span class="hl">{parts[1]}</span><br>{parts[2]}'
    pill = "Follow for more →" if i == 8 else "Swipe →"
    return f'''<div class="s" id="s{i}" style="--l:{l};--d:{d}">
<div class="top"><span class="lab">{s["label"]} • 0{i}</span><span class="logo">{BRAND}</span></div>
<h1>{h}</h1><div class="band">{s["band"]}</div><div class="proof">{s["proof"]}</div>
<div class="num">0{i}</div><div class="take">{s["take"]}</div>
<div class="foot"><span>{BRAND}</span><span class="pill">0{i}/08 {pill}</span></div></div>'''


html = ('<!doctype html><html><head><meta charset="utf-8"><title>AI Agent Carousel</title>'
        f'<style>{CSS}</style></head><body>{"".join(slide(i + 1, s) for i, s in enumerate(S))}</body></html>')
(H / "carousel.html").write_text(html)
