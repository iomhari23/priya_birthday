import streamlit as st

# ============================================================
#  🌸  PRIYA'S PHOTOS — paste your Imgur direct URLs below
#
#  LEFT_PHOTO  = hangs LEFT  side of "Happy Birthday"
#  RIGHT_PHOTO = hangs RIGHT side of "Happy Birthday"
#  GALLERY_PHOTOS = extra photos shown in the gallery below
#
#  How to get a direct Imgur URL:
#    1. Go to imgur.com and upload the photo
#    2. Right-click the image → "Copy image address"
#    3. Paste it below (must end with .jpg / .png)
# ============================================================
LEFT_PHOTO   = "https://raw.githubusercontent.com/iomhari23/priya_birthday/main/photoes/left.jpeg"
RIGHT_PHOTO  = "https://raw.githubusercontent.com/iomhari23/priya_birthday/main/photoes/right.jpeg"

GALLERY_PHOTOS = [
    "https://i.imgur.com/GALLERY1.jpg",
    "https://i.imgur.com/GALLERY2.jpg",
    "https://i.imgur.com/GALLERY3.jpg",
]



# ============================================================
#  PAGE CONFIG
# ============================================================
st.set_page_config(
    page_title="Happy Birthday Priya 🌸",
    page_icon="🎂",
    layout="centered"
)

# ============================================================
#  GLOBAL STYLES
# ============================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;1,400&family=Quicksand:wght@500;600;700&display=swap');

#MainMenu, header, footer, .stAppDeployButton { display: none !important; }
.stApp { background: #0a0010 !important; }
.block-container { padding: 0.5rem 0.5rem 2rem !important; max-width: 100% !important; }
iframe { border: none !important; }

.section-title {
    font-family: 'Playfair Display', serif;
    font-style: italic;
    font-size: 26px;
    color: #d4a0ff;
    text-align: center;
    text-shadow: 0 0 20px #9b30d8;
    margin: 6px 0 4px;
}
.section-sub {
    font-family: 'Quicksand', sans-serif;
    font-size: 12px;
    letter-spacing: 5px;
    color: #8855aa;
    text-align: center;
    text-transform: uppercase;
    margin-bottom: 18px;
}
.wish-card {
    background: rgba(80,0,120,0.18);
    border: 1px solid #6b0a9a55;
    border-radius: 16px;
    padding: 16px 20px;
    margin-bottom: 12px;
    font-family: 'Quicksand', sans-serif;
}
.wish-name  { font-size: 14px; font-weight: 700; color: #cc88ff; margin-bottom: 4px; }
.wish-msg   { font-size: 15px; color: #e8c8ff; line-height: 1.7; }
.wish-time  { font-size: 11px; color: #7744aa; margin-top: 6px; }
.empty-box {
    background: rgba(80,0,120,0.12);
    border: 1px dashed #6b0a9a66;
    border-radius: 16px;
    padding: 28px;
    text-align: center;
    font-family: 'Quicksand', sans-serif;
    color: #8855aa;
    font-size: 14px;
    letter-spacing: 1px;
    margin-bottom: 16px;
}
div[data-testid="stImage"] img {
    border-radius: 18px !important;
    border: 2px solid #9b30d866 !important;
    box-shadow: 0 0 24px #6b0a9a55 !important;
    object-fit: cover !important;
    width: 100% !important;
}
.stTextInput > div > div > input,
.stTextArea > div > div > textarea {
    background: rgba(80,0,120,0.22) !important;
    border: 1px solid #6b0a9a88 !important;
    color: #e8c8ff !important;
    border-radius: 12px !important;
    font-family: 'Quicksand', sans-serif !important;
    font-size: 15px !important;
}
.stTextInput > div > div > input::placeholder,
.stTextArea > div > div > textarea::placeholder { color: #7744aa !important; }
.stTextInput label, .stTextArea label {
    color: #cc88ff !important;
    font-family: 'Quicksand', sans-serif !important;
    font-weight: 700 !important;
    font-size: 14px !important;
}
.stButton > button {
    background: linear-gradient(135deg, #9b30d8, #cc44ff) !important;
    color: white !important;
    border: none !important;
    border-radius: 50px !important;
    font-family: 'Quicksand', sans-serif !important;
    font-weight: 700 !important;
    letter-spacing: 2px !important;
    padding: 12px 32px !important;
    width: 100% !important;
    font-size: 15px !important;
}
</style>
""", unsafe_allow_html=True)

# ============================================================
#  Build dynamic photo HTML snippets (safe — not inside f-string)
# ============================================================
left_src  = LEFT_PHOTO  if "REPLACE" not in LEFT_PHOTO  else ""
right_src = RIGHT_PHOTO if "REPLACE" not in RIGHT_PHOTO else ""

if left_src:
    left_photo_html = "<img class='polaroid-img' src='" + left_src + "' alt='Priya'/>"
else:
    left_photo_html = "<div class='polaroid-placeholder'><span style='font-size:28px'>🌸</span><span>Add photo</span></div>"

if right_src:
    right_photo_html = "<img class='polaroid-img' src='" + right_src + "' alt='Priya'/>"
else:
    right_photo_html = "<div class='polaroid-placeholder'><span style='font-size:28px'>💕</span><span>Add photo</span></div>"

# ============================================================
#  MAIN HTML — stored as plain string, NO f-string
#  Dynamic parts injected via .replace() at the bottom
# ============================================================
main_html = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;1,400&family=Quicksand:wght@500;700&display=swap" rel="stylesheet">
<style>
* { margin:0; padding:0; box-sizing:border-box; }
body { font-family:'Quicksand',sans-serif; background:#0a0010; overflow-x:hidden; color:#e8c8ff; }

@keyframes float      { 0%,100%{ transform:translateY(0); }       50%{ transform:translateY(-10px); } }
@keyframes floatLeft  { 0%,100%{ transform:rotate(-4deg) translateY(0); }  50%{ transform:rotate(-4deg) translateY(-8px); } }
@keyframes floatRight { 0%,100%{ transform:rotate(4deg)  translateY(0); }  50%{ transform:rotate(4deg)  translateY(-8px); } }
@keyframes flicker    { 0%,100%{opacity:1} 45%{opacity:.85} 47%{opacity:.4} 50%{opacity:.95} 80%{opacity:.9} 82%{opacity:.5} 85%{opacity:1} }
@keyframes pulse-glow { 0%,100%{ box-shadow:0 0 20px #6b0a9a44,0 0 60px #3d006644; } 50%{ box-shadow:0 0 40px #9b30d888,0 0 100px #6b0a9a66; } }
@keyframes typewriter { from{ width:0; } to{ width:100%; } }
@keyframes blink      { 0%,100%{opacity:1} 50%{opacity:0} }
@keyframes pop        { 0%{transform:scale(.3) rotate(-10deg);opacity:0} 60%{transform:scale(1.08) rotate(2deg)} 100%{transform:scale(1) rotate(0);opacity:1} }
@keyframes shimmer    { 0%{background-position:-200% center} 100%{background-position:200% center} }
@keyframes heartbeat  { 0%,100%{transform:scale(1)} 50%{transform:scale(1.25)} }
@keyframes cffall     { 0%{transform:translateY(-20px) rotate(0);opacity:1} 100%{transform:translateY(110vh) rotate(720deg);opacity:0} }
@keyframes fog        { 0%,100%{opacity:.18} 50%{opacity:.32} }
@keyframes twinkle    { 0%,100%{opacity:.15;transform:scale(.8)} 50%{opacity:.9;transform:scale(1.1)} }
@keyframes slideInL   { 0%{transform:translateX(-80px) rotate(-4deg);opacity:0} 100%{transform:translateX(0) rotate(-4deg);opacity:1} }
@keyframes slideInR   { 0%{transform:translateX(80px)  rotate(4deg);opacity:0}  100%{transform:translateX(0) rotate(4deg);opacity:1} }

/* STARS + FOG */
.stars-bg { position:fixed;top:0;left:0;width:100%;height:100%;pointer-events:none;z-index:0; }
.star      { position:absolute;background:#fff;border-radius:50%; }
.fog       { position:fixed;bottom:0;left:0;width:100%;height:160px;
             background:linear-gradient(to top,rgba(80,0,120,.25),transparent);
             pointer-events:none;z-index:1;animation:fog 6s ease-in-out infinite; }

/* ── MYSTERY ── */
.mystery-phase { min-height:100vh;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:40px 20px;position:relative; }
.candle-wrap   { font-size:60px;animation:float 3s ease-in-out infinite;z-index:2;filter:drop-shadow(0 0 30px #cc44ff99); }
.mystery-title { font-family:'Playfair Display',serif;font-style:italic;font-size:clamp(24px,5vw,46px);
                 color:#d4a0ff;text-align:center;margin:18px 0 8px;animation:flicker 4s ease-in-out infinite;
                 letter-spacing:3px;text-shadow:0 0 30px #9b30d8,0 0 60px #6b0a9a;z-index:2; }
.mystery-sub   { font-size:14px;color:#8855aa;letter-spacing:5px;text-transform:uppercase;text-align:center;z-index:2;margin-bottom:32px; }
.tw-box        { background:rgba(80,0,120,.18);border:1px solid #6b0a9a55;border-radius:16px;
                 padding:24px 28px;max-width:460px;width:100%;text-align:center;z-index:2;
                 animation:pulse-glow 4s ease-in-out infinite;margin-bottom:28px; }
.tw-line       { font-size:15px;color:#c088ee;line-height:2;font-weight:500;overflow:hidden; }
.tw-line span  { display:inline-block;overflow:hidden;white-space:nowrap;border-right:2px solid #cc66ff;width:0; }
.tw-line.l1 span { animation:typewriter 3s steps(40) .5s forwards, blink .7s step-end 3.5s infinite; }
.tw-line.l2 span { animation:typewriter 2.5s steps(35) 3.8s forwards, blink .7s step-end 6.3s infinite; }
.tw-line.l3 span { animation:typewriter 2s steps(30) 6.5s forwards, blink .7s step-end 8.5s infinite; }
.m-orbs        { display:flex;gap:22px;z-index:2;margin-bottom:4px; }
.orb           { border-radius:50%;background:#9b30d8;box-shadow:0 0 16px #cc44ff;animation:heartbeat 2s ease-in-out infinite; }
.reveal-btn    { background:transparent;border:1.5px solid #9b30d8;color:#e0b0ff;border-radius:50px;
                 padding:13px 36px;font-family:'Quicksand',sans-serif;font-size:15px;font-weight:700;
                 cursor:pointer;letter-spacing:2px;text-transform:uppercase;transition:all .3s;z-index:2;
                 box-shadow:0 0 20px #6b0a9a33;margin-top:28px;opacity:0;pointer-events:none; }
.reveal-btn.visible { opacity:1;pointer-events:all;animation:pulse-glow 2s ease-in-out infinite; }
.reveal-btn:hover   { background:#6b0a9a33;color:#fff;box-shadow:0 0 40px #9b30d888; }

/* ── TRANSITION ── */
.t-overlay  { position:fixed;top:0;left:0;width:100%;height:100%;background:#0a0010;z-index:100;
              display:none;align-items:center;justify-content:center; }
.t-overlay.active { display:flex; }
.burst      { font-family:'Playfair Display',serif;font-size:clamp(28px,7vw,64px);color:#fff;text-align:center;
              text-shadow:0 0 60px #ff6bae,0 0 120px #cc44ff;opacity:0;transform:scale(.5);
              transition:all .6s cubic-bezier(.34,1.56,.64,1); }

/* ── BIRTHDAY ── */
.bday-phase { display:none;flex-direction:column;align-items:center;
              padding:0 0 40px;background:linear-gradient(135deg,#ffe4f0,#fff0fb,#fde8ff);min-height:100vh; }
.bday-phase.show { display:flex; }
.cf-wrap    { position:fixed;top:0;left:0;width:100%;height:100%;pointer-events:none;z-index:0; }
.cf-piece   { position:absolute;animation:cffall linear forwards; }

/* ── ROPE & POLAROIDS ── */
.rope-section    { width:100%;position:relative;display:flex;flex-direction:column;align-items:center; }
.rope-svg        { width:100%;height:22px;overflow:visible; }
.rope-svg line   { stroke:#8B6914;stroke-width:2.5;stroke-linecap:round; }
.rope-svg circle { fill:#6B4F10; }
.polaroids-row   { width:100%;display:flex;align-items:flex-start;justify-content:space-between;
                   position:relative;z-index:3;padding:0 12px;margin-top:-10px; }
.string-wrap     { display:flex;flex-direction:column;align-items:center; }
.clip            { font-size:14px;margin-bottom:-4px;filter:drop-shadow(0 1px 2px rgba(0,0,0,.3)); }
.string          { width:2px;height:28px;background:linear-gradient(to bottom,#8B6914,#A07820); }

.polaroid        { background:#fff;padding:14px 14px 52px;
                   box-shadow:0 12px 32px rgba(0,0,0,.22),0 3px 8px rgba(0,0,0,.14);width:220px; }
.polaroid-img    { width:192px;height:210px;object-fit:cover;display:block; }
.polaroid-placeholder { width:192px;height:210px;display:flex;align-items:center;justify-content:center;
                        flex-direction:column;gap:8px;font-size:13px;font-weight:700;color:#cc88b0;letter-spacing:.5px;
                        background:linear-gradient(135deg,#ffeef6,#f3e8ff); }
.polaroid-label  { text-align:center;font-family:'Quicksand',sans-serif;font-size:13px;
                   color:#cc88b0;font-weight:700;margin-top:8px;letter-spacing:1px; }
.left-wrap       { animation:slideInL 1s ease .3s both;transform-origin:top center; }
.right-wrap      { animation:slideInR 1s ease .3s both;transform-origin:top center; }
.left-wrap  .polaroid { animation:floatLeft  4s ease-in-out 1.5s infinite;transform:rotate(-5deg); }
.right-wrap .polaroid { animation:floatRight 4s ease-in-out 1.5s infinite;transform:rotate(5deg); }

/* ── HERO CENTRE ── */
.hero-center { flex:1;display:flex;flex-direction:column;align-items:center;justify-content:flex-start;padding-top:10px;z-index:2;min-width:0; }
.balloons    { display:flex;gap:12px;margin-bottom:8px;animation:float 3s ease-in-out infinite; }
.balloon     { width:42px;height:54px;border-radius:50% 50% 50% 50%/45% 45% 55% 55%;
               display:flex;align-items:center;justify-content:center;font-size:17px;
               transition:transform .2s;box-shadow:inset -5px -5px 10px rgba(0,0,0,.15),inset 3px 3px 7px rgba(255,255,255,.5);position:relative; }
.balloon::after { content:'';position:absolute;bottom:-13px;left:50%;transform:translateX(-50%);width:1.5px;height:13px;background:rgba(0,0,0,.2); }
.balloon:hover  { transform:scale(1.15) rotate(-5deg); }
.b1{background:#ff8fab}.b2{background:#c77dff}.b3{background:#ff9e8c}.b4{background:#74d7ff}.b5{background:#ffcc66}
.cake-e   { font-size:52px;animation:float 2.5s ease-in-out infinite;display:inline-block;filter:drop-shadow(0 8px 16px rgba(255,120,180,.3)); }
.name-t   { font-family:'Playfair Display',serif;font-size:clamp(26px,5vw,42px);
            background:linear-gradient(90deg,#ff6bae,#c77dff,#ff9e8c,#ff6bae);background-size:200% auto;
            -webkit-background-clip:text;-webkit-text-fill-color:transparent;animation:shimmer 3s linear infinite;
            margin:6px 0;text-align:center; }
.bday-sub { font-size:12px;color:#cc6b9e;font-weight:700;letter-spacing:3px;text-transform:uppercase;margin-bottom:8px;text-align:center; }
.hearts   { display:flex;justify-content:center;gap:8px;font-size:20px;margin:6px 0; }
.heart    { display:inline-block;animation:heartbeat 1.2s ease-in-out infinite; }
.heart:nth-child(2){animation-delay:.2s}.heart:nth-child(3){animation-delay:.4s}

/* ── CARDS ── */
.hero-card  { background:rgba(255,255,255,.88);border-radius:28px;padding:22px 18px;
              max-width:460px;width:calc(100% - 32px);text-align:center;border:2px solid #ffb3d1;
              z-index:1;animation:pop .8s ease both;margin:14px 16px 0; }
.pop-msg    { background:linear-gradient(135deg,rgba(255,107,174,.12),rgba(199,125,255,.12));
              border-radius:16px;padding:14px 16px;font-size:14px;color:#8b3a6e;line-height:1.8;
              font-weight:600;border:1.5px solid #ffb3d1;margin:10px 0; }
.w-cards    { display:grid;grid-template-columns:1fr 1fr;gap:10px;max-width:460px;
              width:calc(100% - 32px);margin:14px 16px 0;z-index:1; }
.wcard      { background:rgba(255,255,255,.9);border-radius:16px;padding:14px 10px;text-align:center;
              border:1.5px solid #ffcde3;cursor:pointer;transition:transform .2s,box-shadow .2s;animation:pop .7s ease both; }
.wcard:hover{ transform:translateY(-4px);box-shadow:0 10px 24px rgba(255,120,180,.2); }
.wcard .icon{ font-size:24px;display:block;margin-bottom:5px; }
.wcard .lbl { font-size:12px;color:#c05a8a;font-weight:700; }
.wcard .dsc { font-size:11px;color:#d48aaa;margin-top:2px;font-weight:600; }
.secret-card{ background:rgba(255,255,255,.92);border-radius:22px;padding:22px 18px;max-width:460px;
              width:calc(100% - 32px);text-align:center;border:2px solid #c77dff;z-index:1;
              animation:pop .8s ease .4s both;margin:14px 16px 0; }
.secret-card h3 { font-family:'Playfair Display',serif;font-size:19px;color:#c77dff;margin-bottom:10px; }
.secret-card p  { font-size:14px;color:#7a3d6e;line-height:1.8;font-weight:600; }
.scroll-hint{ font-size:12px;color:#cc88b0;font-weight:700;letter-spacing:2px;text-align:center;
              animation:float 2s ease-in-out infinite;z-index:1;margin-top:10px; }
.footer-note{ font-size:12px;color:#cc88b0;font-weight:700;letter-spacing:2px;margin-top:14px;z-index:1; }

/* ── MUSIC BAR ── */
.music-bar  { position:fixed;bottom:18px;right:18px;z-index:200;
              background:rgba(20,0,40,.88);backdrop-filter:blur(12px);
              border:1px solid #9b30d866;border-radius:50px;
              padding:9px 16px;display:flex;align-items:center;gap:10px;
              box-shadow:0 8px 24px rgba(0,0,0,.4);font-family:'Quicksand',sans-serif; }
.music-icon { font-size:17px;animation:heartbeat 1.5s ease-in-out infinite; }
.music-lbl  { font-size:12px;color:#e0b0ff;font-weight:700;letter-spacing:1px; }
.music-btn  { background:none;border:1px solid #9b30d8;color:#e0b0ff;border-radius:50px;
              padding:4px 12px;font-family:'Quicksand',sans-serif;font-size:11px;
              font-weight:700;cursor:pointer;letter-spacing:1px;transition:all .2s; }
.music-btn:hover { background:#6b0a9a44; }
</style>
</head>
<body>

<div class="stars-bg" id="starsEl"></div>
<div class="fog"></div>

<!-- MYSTERY -->
<div class="mystery-phase" id="mysteryPhase">
  <div class="candle-wrap">&#x1F56F;&#xFE0F;</div>
  <div class="mystery-title">Something awaits you&hellip;</div>
  <div class="mystery-sub">in the shadows tonight</div>
  <div class="tw-box">
    <div class="tw-line l1"><span>The night holds a secret it dare not speak&hellip;</span></div>
    <div class="tw-line l2"><span>A name whispered softly in the dark&hellip;</span></div>
    <div class="tw-line l3"><span>Are you ready to find out? &#x1F56F;&#xFE0F;</span></div>
  </div>
  <div class="m-orbs">
    <div class="orb" style="width:13px;height:13px"></div>
    <div class="orb" style="width:9px;height:9px;background:#d460ff"></div>
    <div class="orb" style="width:15px;height:15px;background:#7700cc"></div>
  </div>
  <button class="reveal-btn" id="revealBtn" onclick="startReveal()">&#x2736; Reveal the Secret &#x2736;</button>
</div>

<!-- TRANSITION -->
<div class="t-overlay" id="tOverlay">
  <div class="burst" id="burstEl">&#x1F389; SURPRISE! &#x1F389;</div>
</div>

<!-- BIRTHDAY -->
<div class="bday-phase" id="bdayPhase">
  <div class="cf-wrap" id="cfWrap"></div>

  <!-- ROPE SECTION -->
  <div class="rope-section">
    <svg class="rope-svg" viewBox="0 0 800 22" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">
      <line x1="0" y1="11" x2="800" y2="11"/>
      <circle cx="150" cy="11" r="3.5"/>
      <circle cx="400" cy="11" r="3.5"/>
      <circle cx="650" cy="11" r="3.5"/>
    </svg>

    <div class="polaroids-row" style="padding:0 24px;align-items:flex-start;justify-content:space-between;">

      <!-- LEFT polaroid -->
      <div class="string-wrap" style="align-items:center;">
        <div class="clip">&#x1F4CE;</div>
        <div class="string" style="height:32px;"></div>
        <div class="left-wrap">
          <div class="polaroid">
            __LEFT_PHOTO_HTML__
            <div class="polaroid-label">Priya &#x1F338;</div>
          </div>
        </div>
      </div>

      <!-- CENTRE -->
      <div class="hero-center">
        <div class="balloons">
          <div class="balloon b1">&#x1F380;</div>
          <div class="balloon b2">&#x1F338;</div>
          <div class="balloon b3">&#x1F382;</div>
          <div class="balloon b4">&#x1F337;</div>
          <div class="balloon b5">&#x1F4AB;</div>
        </div>
        <div class="cake-e">&#x1F382;</div>
        <div class="bday-sub">Happy Birthday</div>
        <div class="name-t">Priya &#x1F338;</div>
        <div class="hearts">
          <span class="heart">&#x1F496;</span>
          <span class="heart">&#x1F495;</span>
          <span class="heart">&#x1F497;</span>
        </div>
      </div>

      <!-- RIGHT polaroid -->
      <div class="string-wrap" style="align-items:center;">
        <div class="clip">&#x1F4CE;</div>
        <div class="string" style="height:32px;"></div>
        <div class="right-wrap">
          <div class="polaroid">
            __RIGHT_PHOTO_HTML__
            <div class="polaroid-label">Always &#x1F495;</div>
          </div>
        </div>
      </div>

    </div>
  </div>

  <!-- Message card -->
  <div class="hero-card">
    <div class="pop-msg">
      Today the whole world is a little brighter because it&apos;s <em>your</em> day! &#x1F31F;
      You deserve every flower, every smile, and all the magic the universe holds. &#x1F380;
    </div>
  </div>

  <!-- Wish cards -->
  <div class="w-cards">
    <div class="wcard"><span class="icon">&#x1F33A;</span><div class="lbl">Joy &amp; Happiness</div><div class="dsc">Every single day</div></div>
    <div class="wcard"><span class="icon">&#x1F4AB;</span><div class="lbl">All Your Dreams</div><div class="dsc">Coming true, always</div></div>
    <div class="wcard"><span class="icon">&#x1F370;</span><div class="lbl">Sweetest Moments</div><div class="dsc">Savour every second</div></div>
    <div class="wcard"><span class="icon">&#x1F380;</span><div class="lbl">Love &amp; Laughter</div><div class="dsc">Forever surrounding you</div></div>
  </div>

  <!-- Heartfelt message card -->
  <div class="secret-card">
    <h3>&#x1F48C; just for you, Priya&hellip;</h3>
    <p>
      this page is something special &mdash;<br>
      made for someone special. &#x1F338;<br><br>
      i don&apos;t fully know why, but my heart just knows &mdash;<br>
      you are special to me.<br>
      even if you don&apos;t think so yourself,<br>
      even if you don&apos;t see it &mdash;<br><br>
      <em>i do .</em> &#x1F495;<br><br>
      <em>YOU KNOW WHAT U MEAN TO ME .</em> &#x1F495;<br><br>
      happy birthday, Priya.<br>
      the world is a little warmer because you&apos;re in it. &#x1F337;&#x2728;
    </p>
    <div style="font-size:22px;margin-top:16px">&#x1F496; &#x1F338; &#x1F4AB; &#x1F337; &#x1F495;</div>
  </div>

  <div class="footer-note" style="margin-top:18px;margin-bottom:10px">&#x1F31F; Made with love, just for you &#x1F31F;</div>
</div>

<!-- MUSIC BAR -->
<div class="music-bar" id="musicBar" style="display:none">
  <span class="music-icon">&#x1F3B5;</span>
  <span class="music-lbl">Sweet melody for Priya</span>
  <button class="music-btn" id="musicBtn" onclick="toggleMusic()">&#x23F8; Pause</button>
</div>

<!-- Personal song -->
<audio id="bgAudio" loop>
  <source src="https://raw.githubusercontent.com/iomhari23/priya_birthday/main/to_u.mp3" type="audio/mpeg">
</audio>

<script>
/* Generate stars */
(function() {
  var sb = document.getElementById('starsEl');
  for (var i = 0; i < 80; i++) {
    var s = document.createElement('div');
    s.className = 'star';
    var z = 0.5 + Math.random() * 2.5;
    s.style.cssText = 'width:' + z + 'px;height:' + z + 'px;left:' + (Math.random()*100) + '%;top:' + (Math.random()*100) + '%;opacity:' + (0.1 + Math.random()*0.7) + ';animation:twinkle ' + (1.5+Math.random()*3) + 's ease-in-out infinite;animation-delay:' + (Math.random()*4) + 's';
    sb.appendChild(s);
  }
})();

/* Show reveal button after typing finishes */
setTimeout(function() {
  document.getElementById('revealBtn').classList.add('visible');
}, 9000);

function startReveal() {
  var ov = document.getElementById('tOverlay');
  var bt = document.getElementById('burstEl');
  ov.classList.add('active');
  setTimeout(function() { bt.style.opacity='1'; bt.style.transform='scale(1)'; }, 200);
  setTimeout(function() { ov.style.background='linear-gradient(135deg,#ff6bae44,#c77dff44)'; }, 800);
  setTimeout(function() {
    document.getElementById('mysteryPhase').style.display = 'none';
    ov.classList.remove('active');
    document.getElementById('bdayPhase').classList.add('show');
    launchConfetti();
    startMusic();
  }, 2000);
}

function launchConfetti() {
  var w = document.getElementById('cfWrap');
  var c = ['#ff8fab','#c77dff','#ff9e8c','#74d7ff','#ffcc66','#98f5e1','#ffb3de'];
  for (var i = 0; i < 90; i++) {
    var el = document.createElement('div');
    el.className = 'cf-piece';
    el.style.left = (Math.random()*100) + '%';
    el.style.top  = '-20px';
    el.style.background = c[Math.floor(Math.random()*c.length)];
    var d = 2 + Math.random()*3;
    el.style.animationDuration = d + 's';
    el.style.animationDelay   = (Math.random()*2) + 's';
    el.style.width  = (7+Math.random()*8) + 'px';
    el.style.height = (7+Math.random()*8) + 'px';
    el.style.borderRadius = Math.random()>.5 ? '50%' : '2px';
    w.appendChild(el);
    (function(e,dur){ setTimeout(function(){ e.remove(); }, (dur+2)*1000); })(el,d);
  }
}

function startMusic() {
  var a = document.getElementById('bgAudio');
  var bar = document.getElementById('musicBar');
  a.volume = 0.45;
  a.play().then(function() {
    bar.style.display = 'flex';
  }).catch(function() {
    bar.style.display = 'flex';
    document.getElementById('musicBtn').textContent = '\u25B6 Play';
  });
}

function toggleMusic() {
  var a = document.getElementById('bgAudio');
  var btn = document.getElementById('musicBtn');
  if (a.paused) { a.play(); btn.innerHTML = '&#x23F8; Pause'; }
  else          { a.pause(); btn.innerHTML = '&#x25B6; Play'; }
}
</script>
</body>
</html>
""".replace("__LEFT_PHOTO_HTML__", left_photo_html).replace("__RIGHT_PHOTO_HTML__", right_photo_html)

st.components.v1.html(main_html, height=900, scrolling=True)

st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)

# ============================================================
#  GALLERY
# ============================================================
st.markdown('<div class="section-title">&#x1F338; More Memories</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">moments worth keeping forever</div>', unsafe_allow_html=True)

valid_gallery = [p for p in GALLERY_PHOTOS if "REPLACE" not in p and p.strip()]

if valid_gallery:
    cols = st.columns(min(len(valid_gallery), 3))
    for idx, url in enumerate(valid_gallery):
        with cols[idx % 3]:
            try:
                st.image(url, use_container_width=True)
            except Exception:
                st.markdown('<div class="empty-box">Could not load image</div>', unsafe_allow_html=True)
else:
    st.markdown("""
    <div class="empty-box">
        &#x1F4F8; Add Priya&apos;s photo URLs to <b style="color:#cc88ff">GALLERY_PHOTOS</b> in app.py<br><br>
        <span style="font-size:12px;color:#6633aa;">
        Upload to <b>imgur.com</b> &#x2192; right-click &#x2192; Copy image address
        </span>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)
