
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="MTA Server Panel")

@app.get("/", response_class=HTMLResponse)
def home():
    return HTMLResponse(content="""
<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>پنل سرور MTA</title>
<style>
body{margin:0;background:#101827;color:#fff;font-family:Tahoma,sans-serif}
header{background:#18243a;padding:24px;text-align:center}
main{max-width:850px;margin:25px auto;padding:16px}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:15px}
.card{background:#1c2b43;padding:22px;border-radius:14px}
.status{color:#ffca65}
</style>
</head>
<body>
<header>
<h1>پنل سرور MTA</h1>
<p>سرور اختصاصی من</p>
</header>
<main>
<h2>حالت‌های بازی</h2>
<div class="grid">
<div class="card"><h3>Roleplay</h3><p>شغل و پول مجازی</p></div>
<div class="card"><h3>Freeroam</h3><p>رانندگی آزاد</p></div>
<div class="card"><h3>Race</h3><p>مسابقه ماشین‌ها</p></div>
<div class="card"><h3>Drift</h3><p>دریفت و تیونینگ</p></div>
</div>
<div class="card" style="margin-top:18px">
<h3>وضعیت سرور بازی</h3>
<p class="status">در انتظار اتصال به سرور واقعی MTA</p>
<p>این وب‌سایت پنل نمایشی است و خودش میزبان بازی نیست.</p>
</div>
</main>
</body>
</html>
""")
