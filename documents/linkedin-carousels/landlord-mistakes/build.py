"""Build the '5 Mistakes Landlords Make' Facebook graphics (portrait + square)."""
import pathlib
H = pathlib.Path(__file__).parent
BRAND = "A Shameless Marketer"
ITEMS = [("Rent set", "too high"), ("Skipping", "tenant checks"), ("Unclear", "rental terms"),
         ("No photos of", "the condition"), ("Forgetting", "repair costs")]
CSS = """*{box-sizing:border-box;margin:0}body{background:#ccc}
.s{position:relative;overflow:hidden;font-family:Inter,Arial,sans-serif;color:#111;margin-bottom:20px;
background:#F4EBDF;background-image:linear-gradient(#e7ddcf 1px,transparent 1px),linear-gradient(90deg,#e7ddcf 1px,transparent 1px);background-size:45px 45px}
.top{display:flex;justify-content:space-between;align-items:center}
.lab{font-weight:800;letter-spacing:3px;font-size:24px}.logo{background:#FFE000;padding:14px 24px;font-weight:900;font-size:24px}
h1{font-weight:900;letter-spacing:-3px;line-height:1.02}
.hl{background:#F6C9C9;outline:3px solid #D64545;padding:0 14px;position:relative;display:inline-block}
.hl:before,.hl:after{content:"";position:absolute;width:24px;height:24px;border-radius:50%;background:#D64545}
.hl:before{left:-12px;top:-12px}.hl:after{right:-12px;bottom:-12px}
.list div{display:flex;align-items:center;gap:24px;background:#fff;border-left:10px solid #D64545;font-weight:600}
.list b{font-weight:900;color:#D64545}.list strong{font-weight:900}
.take{background:#111;color:#fff;font-weight:900;line-height:1.08;display:inline-block}
.foot{position:absolute;display:flex;justify-content:space-between;align-items:center;font-size:24px;font-weight:700;color:#444}
.pill{background:#fff;border-radius:40px;padding:14px 28px;font-size:26px;font-weight:800;color:#111}
/* portrait */
#p{width:1080px;height:1350px;padding:80px 90px}#p h1{font-size:108px;margin-top:60px;white-space:nowrap}
#p .list{margin-top:56px}#p .list div{padding:20px 28px;margin-bottom:14px;font-size:40px}#p .list b{font-size:48px}
#p .take{margin-top:40px;font-size:52px;padding:30px 38px}#p .foot{left:90px;right:90px;bottom:64px}
/* square */
#q{width:1080px;height:1080px;padding:70px 80px}#q h1{font-size:96px;margin-top:44px}
#q .list{margin-top:36px}#q .list div{padding:14px 24px;margin-bottom:10px;font-size:34px}#q .list b{font-size:40px}
#q .take{margin-top:26px;font-size:40px;padding:22px 30px}#q .foot{left:80px;right:80px;bottom:52px}"""
def card(i):
    rows = "".join(f"<div><b>0{n+1}</b><span>{a} <strong>{b}</strong></span></div>" for n, (a, b) in enumerate(ITEMS))
    return f'''<div class="s" id="{i}"><div class="top"><span class="lab">LANDLORD TIPS</span></div>
<h1>5 <span class="hl">mistakes</span><br>landlords make.</h1><div class="list">{rows}</div>
<div class="take">PLAN BEFORE YOU<br>HAND OVER THE KEYS.</div>
<div class="foot"><span></span><span class="pill">Save this 🔖</span></div></div>'''
(H/"graphic.html").write_text(f'<!doctype html><html><head><meta charset="utf-8"><title>Landlord Mistakes</title><style>{CSS}</style></head><body>{card("p")}</body></html>')
