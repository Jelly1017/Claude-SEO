"""Build the 'AI agent for real estate' LinkedIn carousel as HTML + PNGs."""
import json, pathlib
H = pathlib.Path(__file__).parent
C = {"p": ("#D9C2F0", "#A77BD8"), "g": ("#C6EBD3", "#3DBE7A"), "b": ("#C5E3FA", "#5BAFE8")}
S = [
 dict(n=1,a="p",label="THE AGENT QUESTION",pre="Agents lose hours to",hl="admin",post="every day.",band="But who said you have to do it?",
  body="Replying to leads, sending listings, chasing documents. Most of it is the same task, every day.",
  take="YOU WERE HIRED TO SELL, NOT TO COPY-PASTE.",proof='<div class="big">📱💬📄</div><div class="cap">The same 4 tasks, every single day</div>'),
 dict(n=2,a="g",label="THE SIMPLE DEFINITION",pre="An AI agent is just a",hl="helper",post="with rules.",band="Not a robot. A routine.",
  body="It reads a message, decides the next step, and does it using your tools: WhatsApp, Google Sheets, email.",
  take="IF YOU CAN WRITE THE STEPS, AN AGENT CAN RUN THEM.",
  proof='<div class="flow"><div>Trigger<small>New lead</small></div>→<div>Decide<small>Qualify</small></div>→<div>Act<small>Reply + log</small></div></div>'),
 dict(n=3,a="b",label="THE LEAD REPLY",pre="Leads go",hl="cold",post="while you're at a viewing.",band="Agent fix: reply in under 1 minute.",
  body="The agent answers new enquiries, asks 3 questions (budget, area, move-in date) and saves the answers to your sheet.",
  take="FIRST TO REPLY OFTEN WINS THE LEAD.",
  proof='<div class="cards"><div><b>Before</b>Reply in hours</div><div class="hot"><b>After</b>Under 1 min, 24/7</div></div>'),
 dict(n=4,a="p",label="THE LISTING MATCH",pre="Stop",hl="scrolling",post="your own listings.",band="Agent fix: match buyers to units.",
  body="A new unit comes in. The agent checks your buyer list and drafts a message to each buyer who fits.",
  take="YOUR DATABASE SHOULD WORK WHILE YOU SLEEP.",
  proof='<table><tr><th>Buyer</th><th>Budget</th><th>Area</th><th>Match</th></tr><tr><td>Lead A</td><td>RM600k</td><td>Mont Kiara</td><td>✅</td></tr><tr><td>Lead B</td><td>RM450k</td><td>Cheras</td><td>❌</td></tr><tr><td>Lead C</td><td>RM650k</td><td>Mont Kiara</td><td>✅</td></tr></table>'),
 dict(n=5,a="g",label="THE FOLLOW-UP",pre="Most deals die in",hl="silence.",post="",band="Agent fix: never forget a follow-up.",
  body="The agent tracks every lead and nudges you, or the client, on day 3, 7 and 14.",
  take="FOLLOW-UP IS A SYSTEM, NOT A MOOD.",
  proof='<div class="tl"><div><b>Day 1</b>Viewing</div><div><b>Day 3</b>"Any questions?"</div><div><b>Day 7</b>Similar unit</div><div><b>Day 14</b>Market update</div></div>'),
 dict(n=6,a="b",label="THE PAPERWORK",pre="Chasing",hl="documents",post="eats your week.",band="Agent fix: checklist + reminders.",
  body="The agent sends each client a list, ticks off what arrives and reminds them about what's missing.",
  take="LET THE AGENT NAG. YOU CLOSE.",
  proof='<div class="check"><div>✅ IC</div><div>✅ Payslip</div><div>⏳ Bank statement</div><div>⏳ EPF statement</div></div>'),
 dict(n=7,a="p",label="THE LIMITS",pre="Agents",hl="can't",post="replace trust.",band="Know where to draw the line.",
  body="",take="AUTOMATE THE ROUTINE. KEEP THE RELATIONSHIP.",
  proof='<div class="check"><div>✅ Replies, sorting, reminders, drafts</div><div>❌ Pricing advice, negotiation, legal answers</div><div>⚠️ Check anything sent under your name</div></div>'),
 dict(n=8,a="g",label="THE START",pre="Start with",hl="one",post="task.",band="Not ten. One.",
  body="Pick the job you repeat most this week. Write the steps on paper. That's your first agent.<br><b>Comment \"AGENT\" for my starter setup.</b>",
  take="SMALL AGENT. BIG HOURS BACK.",
  proof='<div class="check"><div>1. WhatsApp Business auto-reply</div><div>2. Google Sheets</div><div>3. ChatGPT / Claude + Zapier or Make</div></div>'),
]
CSS = """*{box-sizing:border-box;margin:0}body{background:#ddd}
.s{width:1080px;height:1350px;position:relative;overflow:hidden;font-family:Inter,Arial,sans-serif;color:#111;
background:#F3E9DC;background-image:linear-gradient(#e6dccd 1px,transparent 1px),linear-gradient(90deg,#e6dccd 1px,transparent 1px);background-size:40px 40px;padding:70px 80px;margin-bottom:20px}
.top{display:flex;justify-content:space-between;align-items:center;font-weight:800;letter-spacing:2px;font-size:26px}
.logo{background:#FFE000;padding:16px 26px;font-size:26px;letter-spacing:0}
h1{font-size:104px;line-height:1.02;font-weight:900;letter-spacing:-3px;margin-top:60px}
.hl{background:var(--l);padding:0 12px;position:relative;outline:3px solid var(--d)}
.hl:before,.hl:after{content:"";position:absolute;width:22px;height:22px;border-radius:50%;background:var(--d)}
.hl:before{left:-11px;top:-11px}.hl:after{right:-11px;bottom:-11px}
.band{display:inline-block;background:var(--d);color:#fff;font-size:50px;font-weight:800;padding:12px 22px;margin-top:36px}
.line{width:110px;height:5px;background:var(--d);margin:40px 0 28px}
.body{font-size:34px;line-height:1.35;color:#333;max-width:880px}
.proof{margin-top:36px;font-size:32px;position:relative;z-index:1}
.take{position:absolute;left:80px;bottom:150px;background:#111;color:#fff;font-weight:900;font-size:44px;line-height:1.1;padding:28px 32px;max-width:560px}
.foot{position:absolute;left:80px;right:80px;bottom:60px;display:flex;justify-content:space-between;align-items:center;font-size:22px;color:#444}
.pill{background:#fff;border-radius:40px;padding:14px 28px;font-size:28px;font-weight:700;color:#111}
.big{font-size:120px}.cap{font-size:30px;color:#555}
.flow{display:flex;gap:20px;align-items:center;font-size:44px;font-weight:800}
.flow div{background:var(--l);padding:20px 26px;border-radius:16px}.flow small{display:block;font-size:24px;font-weight:500}
.cards{display:flex;gap:24px}.cards div{flex:1;background:#fff;padding:28px;border-radius:16px;font-size:34px}
.cards b{display:block;font-size:26px;color:#666}.cards .hot{background:var(--l);font-weight:800}
table{border-collapse:separate;border-spacing:0 8px;width:100%;font-size:30px}th{text-align:left;color:#666;font-size:24px;padding:0 16px}
td{background:#fff;padding:16px}tr td:last-child{background:var(--l);text-align:center}
.tl{display:flex;gap:14px}.tl div{flex:1;background:#fff;padding:20px;border-radius:14px;border-top:8px solid var(--d);font-size:26px}.tl b{display:block;font-size:30px}
.check div{background:#fff;padding:16px 22px;margin-bottom:10px;border-left:8px solid var(--d);font-size:32px}
.cta{margin-top:20px;background:var(--d);color:#fff;font-weight:800;padding:18px 24px;display:inline-block}
.deco{position:absolute;z-index:0;right:80px;bottom:150px;width:280px;height:200px;display:flex;align-items:flex-end;gap:14px}
.deco i{flex:1;background:var(--l);border:3px solid var(--d);border-radius:6px 6px 0 0}"""
def slide(s):
    l,d = C[s["a"]]
    body = f'<div class="body">{s["body"]}</div>' if s["body"] else ""
    return f'''<div class="s" id="s{s["n"]}" style="--l:{l};--d:{d}">
<div class="top"><span>{s["label"]} • 0{s["n"]}</span><span class="logo">YOUR BRAND</span></div>
<h1>{s["pre"]} <span class="hl">{s["hl"]}</span> {s["post"]}</h1>
<div class="band">{s["band"]}</div><div class="line"></div>{body}
<div class="proof">{s["proof"]}</div>
<div class="deco"><i style="height:45%"></i><i style="height:80%"></i><i style="height:60%"></i><i style="height:100%"></i></div>
<div class="take">{s["take"]}</div>
<div class="foot"><span>AI agents for real estate • Practical guide</span><span class="pill">0{s["n"]}/08 {"Follow for more" if s["n"]==8 else "Swipe"} →</span></div></div>'''
html = f'<!doctype html><html><head><meta charset="utf-8"><title>AI Agent Carousel</title><style>{CSS}</style></head><body>{"".join(map(slide,S))}</body></html>'
(H/"carousel.html").write_text(html)
