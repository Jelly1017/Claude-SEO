"""Build the 'Zero leads / reverse thinking' LinkedIn carousel.

Usage: python3 build.py && node shot.js
"""
import pathlib

H = pathlib.Path(__file__).parent
BRAND = "A Shameless Marketer"
C = {"p": ("#DCC8F2", "#9B6BD6"), "g": ("#C9EDD6", "#2FB36A"), "b": ("#CDE6FA", "#3D9BE0")}


def chips(*items):
    return '<div class="chips">' + "".join(f"<span>{i}</span>" for i in items) + "</div>"


def rows(*items):
    return '<div class="rows">' + "".join(f"<div>{i}</div>" for i in items) + "</div>"


def flow(*items):
    return '<div class="flow">' + '<em>→</em>'.join(f"<span>{i}</span>" for i in items) + "</div>"


S = [
    dict(a="p", label="THE LEAD QUESTION", h=["Want more", "leads?"], band="Ask the opposite question.",
         proof='<div class="emoji">❓ 🔄</div>', take="THINK<br>BACKWARDS."),
    dict(a="g", label="THE IDEA", h=["Flip the", "question."], band="From Alex Hormozi's books.",
         proof=rows("❌ How do I get more leads?", "✅ How do I get <b>zero</b> leads?"), take="AVOID FAILURE<br>FIRST."),
    dict(a="b", label="THE ZERO-LEAD PLAN", h=["How to get", "zero leads:"], band="Hide from the world.",
         proof=chips("❌ No website", "❌ No SEO", "❌ No social"), take="NO ONE CAN<br>FIND YOU."),
    dict(a="p", label="THE ZERO-LEAD PLAN", h=["How to get", "zero leads:"], band="Give no reason to stay.",
         proof=chips("❌ No free guide", "❌ No landing page", "❌ No clear offer"), take="NO ONE KNOWS<br>WHAT YOU SELL."),
    dict(a="g", label="THE ZERO-LEAD PLAN", h=["How to get", "zero leads:"], band="Never talk to anyone.",
         proof=chips("❌ No email list", "❌ No partners", "❌ No referrals"), take="NO ONE<br>REMEMBERS YOU."),
    dict(a="b", label="THE FLIP", h=["Now do the", "opposite."], band="That's your lead plan.",
         proof=rows("No website → <b>Build one</b>", "No offer → <b>Make it clear</b>", "No list → <b>Start one</b>"),
         take="THE ANSWER WAS<br>THERE ALL ALONG."),
    dict(a="p", label="THE SYSTEM", h=["Leads need a", "funnel."], band="Not just one page.",
         proof=chips("1 Get seen", "2 Free guide", "3 Landing page", "4 Follow-up", "5 Sale"),
         take="STOP WAITING<br>FOR REFERRALS."),
    dict(a="g", label="THE START", h=["Pick", "one", "gap."], band="Fix it this week.",
         proof='<div class="cta">Comment “FUNNEL” 👇</div>', take="ONE FIX.<br>MORE LEADS."),
]

CSS = """*{box-sizing:border-box;margin:0}body{background:#ccc}
.s{width:1080px;height:1350px;position:relative;overflow:hidden;font-family:Inter,Arial,sans-serif;color:#111;
background:#F4EBDF;background-image:linear-gradient(#e7ddcf 1px,transparent 1px),linear-gradient(90deg,#e7ddcf 1px,transparent 1px);
background-size:45px 45px;padding:80px 90px;margin-bottom:20px}
.top{display:flex;justify-content:space-between;align-items:center}
.lab{font-weight:800;letter-spacing:3px;font-size:24px}
.logo{background:#FFE000;padding:14px 24px;font-weight:900;font-size:24px}
h1{font-size:132px;line-height:1.02;font-weight:900;letter-spacing:-4px;margin-top:70px}
.hl{background:var(--l);padding:0 14px;position:relative;outline:3px solid var(--d);display:inline-block;line-height:1.05}
.hl:before,.hl:after{content:"";position:absolute;width:24px;height:24px;border-radius:50%;background:var(--d)}
.hl:before{left:-12px;top:-12px}.hl:after{right:-12px;bottom:-12px}
.band{display:inline-block;background:var(--d);color:#fff;font-size:48px;font-weight:800;padding:14px 26px;margin-top:44px}
.proof{margin-top:56px;font-size:40px;font-weight:700;position:relative;z-index:2}
.emoji{font-size:110px;letter-spacing:20px}
.flow{display:flex;align-items:center;gap:22px}.flow span{background:#fff;border:3px solid var(--d);padding:22px 34px;border-radius:18px}
.flow em{font-style:normal;color:var(--d);font-size:56px}
.chips{display:flex;flex-wrap:wrap;gap:18px}.chips span{background:#fff;padding:20px 30px;border-radius:60px;border:3px solid var(--d)}
.vs{display:flex;gap:24px}.vs div{background:#fff;padding:26px 40px;border-radius:18px;font-size:56px;font-weight:900}
.vs small{display:block;font-size:24px;color:#777;font-weight:600}.vs .on{background:var(--l);outline:3px solid var(--d)}
.dots{display:flex;align-items:center;width:640px}.dots i{width:48px;height:48px;border-radius:50%;background:var(--d)}
.dots b{flex:1;height:6px;background:var(--d)}
.rows div{background:#fff;border-left:8px solid var(--d);padding:18px 26px;margin-bottom:12px;font-weight:600}.rows b{font-weight:900}
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


html = ('<!doctype html><html><head><meta charset="utf-8"><title>Zero Leads Carousel</title>'
        f'<style>{CSS}</style></head><body>{"".join(slide(i + 1, s) for i, s in enumerate(S))}</body></html>')
(H / "carousel.html").write_text(html)
