import streamlit as st

st.set_page_config(
    page_title="Happy Birthday Priya 🌸",
    page_icon="🎂",
    layout="centered"
)

html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;1,400&family=Quicksand:wght@500;700&display=swap" rel="stylesheet">
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Quicksand',sans-serif;background:#0a0010;min-height:100vh;overflow-x:hidden;color:#e8c8ff;}

@keyframes float{0%,100%{transform:translateY(0)}50%{transform:translateY(-10px)}}
@keyframes flicker{0%,100%{opacity:1}45%{opacity:0.85}47%{opacity:0.4}50%{opacity:0.95}80%{opacity:0.9}82%{opacity:0.5}85%{opacity:1}}
@keyframes pulse-glow{0%,100%{box-shadow:0 0 20px #6b0a9a44,0 0 60px #3d006644}50%{box-shadow:0 0 40px #9b30d888,0 0 100px #6b0a9a66}}
@keyframes typewriter{from{width:0}to{width:100%}}
@keyframes blink{0%,100%{opacity:1}50%{opacity:0}}
@keyframes pop{0%{transform:scale(0.3) rotate(-10deg);opacity:0}60%{transform:scale(1.08) rotate(2deg)}100%{transform:scale(1) rotate(0deg);opacity:1}}
@keyframes shimmer{0%{background-position:-200% center}100%{background-position:200% center}}
@keyframes heartbeat{0%,100%{transform:scale(1)}50%{transform:scale(1.25)}}
@keyframes confetti-fall{0%{transform:translateY(-20px) rotate(0deg);opacity:1}100%{transform:translateY(110vh) rotate(720deg);opacity:0}}
@keyframes fog{0%,100%{opacity:0.18;transform:scaleX(1)}50%{opacity:0.32;transform:scaleX(1.08)}}
@keyframes star-twinkle{0%,100%{opacity:0.15;transform:scale(0.8)}50%{opacity:0.9;transform:scale(1.1)}}

.stars-bg{position:fixed;top:0;left:0;width:100%;height:100%;pointer-events:none;z-index:0}
.star{position:absolute;background:#fff;border-radius:50%}
.fog{position:fixed;bottom:0;left:0;width:100%;height:160px;background:linear-gradient(to top,rgba(80,0,120,0.25),transparent);pointer-events:none;z-index:1;animation:fog 6s ease-in-out infinite;}

.mystery-phase{min-height:100vh;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:40px 20px;position:relative;background:#0a0010;}
.candle-wrap{font-size:64px;animation:float 3s ease-in-out infinite;position:relative;z-index:2;filter:drop-shadow(0 0 30px #cc44ff99)}
.mystery-title{font-family:'Playfair Display',serif;font-style:italic;font-size:clamp(28px,6vw,52px);color:#d4a0ff;text-align:center;margin:20px 0 10px;animation:flicker 4s ease-in-out infinite;letter-spacing:3px;text-shadow:0 0 30px #9b30d8,0 0 60px #6b0a9a;position:relative;z-index:2;}
.mystery-sub{font-size:16px;color:#8855aa;letter-spacing:6px;text-transform:uppercase;text-align:center;position:relative;z-index:2;margin-bottom:40px;}

.typewriter-box{background:rgba(80,0,120,0.18);border:1px solid #6b0a9a55;border-radius:16px;padding:28px 32px;max-width:480px;width:100%;text-align:center;position:relative;z-index:2;animation:pulse-glow 4s ease-in-out infinite;margin-bottom:36px;}
.tw-line{font-size:15px;color:#c088ee;line-height:1.9;font-weight:500;overflow:hidden;}
.tw-line span{display:inline-block;overflow:hidden;white-space:nowrap;border-right:2px solid #cc66ff;width:0;}
.tw-line.line1 span{animation:typewriter 3s steps(40) 0.5s forwards, blink 0.7s step-end 3.5s infinite}
.tw-line.line2 span{animation:typewriter 2.5s steps(35) 3.8s forwards, blink 0.7s step-end 6.3s infinite}
.tw-line.line3 span{animation:typewriter 2s steps(30) 6.5s forwards, blink 0.7s step-end 8.5s infinite}

.mystery-orbs{display:flex;gap:24px;position:relative;z-index:2;}
.orb{width:14px;height:14px;border-radius:50%;background:#9b30d8;box-shadow:0 0 16px #cc44ff;animation:heartbeat 2s ease-in-out infinite;}
.orb:nth-child(2){background:#d460ff;animation-delay:0.4s;width:10px;height:10px}
.orb:nth-child(3){background:#7700cc;animation-delay:0.8s;width:16px;height:16px}

.reveal-btn{background:transparent;border:1.5px solid #9b30d8;color:#e0b0ff;border-radius:50px;padding:14px 38px;font-family:'Quicksand',sans-serif;font-size:16px;font-weight:700;cursor:pointer;letter-spacing:2px;text-transform:uppercase;transition:all 0.3s;position:relative;z-index:2;box-shadow:0 0 20px #6b0a9a33;margin-top:32px;opacity:0;pointer-events:none;}
.reveal-btn.visible{opacity:1;pointer-events:all;animation:pulse-glow 2s ease-in-out infinite;}
.reveal-btn:hover{background:#6b0a9a33;color:#fff;box-shadow:0 0 40px #9b30d888}

.transition-overlay{position:fixed;top:0;left:0;width:100%;height:100%;background:#0a0010;z-index:100;display:none;align-items:center;justify-content:center;flex-direction:column;gap:20px;}
.transition-overlay.active{display:flex}
.burst-text{font-family:'Playfair Display',serif;font-size:clamp(32px,8vw,72px);color:#fff;text-align:center;text-shadow:0 0 60px #ff6bae,0 0 120px #cc44ff;opacity:0;transform:scale(0.5);transition:all 0.6s cubic-bezier(0.34,1.56,0.64,1);}

.birthday-phase{display:none;min-height:100vh;flex-direction:column;align-items:center;padding:30px 16px 60px;background:linear-gradient(135deg,#ffe4f0,#fff0fb,#fde8ff);}
.birthday-phase.show{display:flex}
.confetti-wrap{position:fixed;top:0;left:0;width:100%;height:100%;pointer-events:none;z-index:0}
.confetti-piece{position:absolute;border-radius:2px;animation:confetti-fall linear forwards}

.balloons{display:flex;gap:18px;margin-bottom:16px;animation:float 3s ease-in-out infinite;position:relative;z-index:1}
.balloon{width:50px;height:62px;border-radius:50% 50% 50% 50%/45% 45% 55% 55%;display:flex;align-items:center;justify-content:center;font-size:22px;cursor:pointer;transition:transform 0.2s;box-shadow:inset -6px -6px 12px rgba(0,0,0,0.15),inset 3px 3px 8px rgba(255,255,255,0.5);position:relative}
.balloon::after{content:'';position:absolute;bottom:-18px;left:50%;transform:translateX(-50%);width:1.5px;height:18px;background:rgba(0,0,0,0.2)}
.balloon:hover{transform:scale(1.15) rotate(-5deg)}
.b1{background:#ff8fab}.b2{background:#c77dff}.b3{background:#ff9e8c}.b4{background:#74d7ff}.b5{background:#ffcc66}

.hero-card{background:rgba(255,255,255,0.88);border-radius:32px;padding:36px 28px;max-width:500px;width:100%;text-align:center;border:2px solid #ffb3d1;position:relative;z-index:1;animation:pop 0.8s ease both;margin-bottom:24px;}
.cake-emoji{font-size:72px;animation:float 2.5s ease-in-out infinite;display:inline-block;filter:drop-shadow(0 8px 16px rgba(255,120,180,0.3))}
.name-title{font-family:'Playfair Display',serif;font-size:clamp(36px,8vw,52px);background:linear-gradient(90deg,#ff6bae,#c77dff,#ff9e8c,#ff6bae);background-size:200% auto;-webkit-background-clip:text;-webkit-text-fill-color:transparent;animation:shimmer 3s linear infinite;margin:8px 0;}
.bday-sub{font-size:16px;color:#cc6b9e;font-weight:700;letter-spacing:3px;text-transform:uppercase;margin-bottom:16px}
.pop-message{background:linear-gradient(135deg,rgba(255,107,174,0.12),rgba(199,125,255,0.12));border-radius:20px;padding:20px 24px;font-size:16px;color:#8b3a6e;line-height:1.8;font-weight:600;border:1.5px solid #ffb3d1;margin:16px 0;animation:pop 0.6s ease 0.3s both;}
.hearts-row{display:flex;justify-content:center;gap:14px;font-size:26px;margin:14px 0}
.heart{display:inline-block;animation:heartbeat 1.2s ease-in-out infinite}
.heart:nth-child(2){animation-delay:0.2s}.heart:nth-child(3){animation-delay:0.4s}

.wish-cards{display:grid;grid-template-columns:1fr 1fr;gap:14px;max-width:500px;width:100%;margin-bottom:24px;position:relative;z-index:1}
.wish-card{background:rgba(255,255,255,0.9);border-radius:20px;padding:18px 14px;text-align:center;border:1.5px solid #ffcde3;cursor:pointer;transition:transform 0.2s,box-shadow 0.2s;animation:pop 0.7s ease both}
.wish-card:hover{transform:translateY(-5px);box-shadow:0 12px 28px rgba(255,120,180,0.2)}
.wish-card .icon{font-size:30px;display:block;margin-bottom:8px}
.wish-card .label{font-size:14px;color:#c05a8a;font-weight:700}
.wish-card .desc{font-size:12px;color:#d48aaa;margin-top:4px;font-weight:600}

.secret-card{background:rgba(255,255,255,0.92);border-radius:24px;padding:28px 24px;max-width:500px;width:100%;text-align:center;border:2px solid #c77dff;position:relative;z-index:1;animation:pop 0.8s ease 0.5s both;}
.secret-card h3{font-family:'Playfair Display',serif;font-size:22px;color:#c77dff;margin-bottom:12px}
.secret-card p{font-size:15px;color:#7a3d6e;line-height:1.8;font-weight:600}
.footer-note{font-size:13px;color:#cc88b0;font-weight:700;letter-spacing:2px;margin-top:20px;position:relative;z-index:1}
</style>
</head>
<body>

<div class="stars-bg" id="stars"></div>
<div class="fog"></div>

<!-- MYSTERY PHASE -->
<div class="mystery-phase" id="mysteryPhase">
  <div class="candle-wrap">🕯️</div>
  <div class="mystery-title">Something awaits you…</div>
  <div class="mystery-sub">in the shadows tonight</div>
  <div class="typewriter-box">
    <div class="tw-line line1"><span>The night holds a secret it dare not speak…</span></div>
    <div class="tw-line line2"><span>A name whispered softly in the dark…</span></div>
    <div class="tw-line line3"><span>Are you ready to find out? 🕯️</span></div>
  </div>
  <div class="mystery-orbs">
    <div class="orb"></div><div class="orb"></div><div class="orb"></div>
  </div>
  <button class="reveal-btn" id="revealBtn" onclick="startReveal()">✦ Reveal the Secret ✦</button>
</div>

<!-- TRANSITION -->
<div class="transition-overlay" id="transitionOverlay">
  <div class="burst-text" id="burstText">🎉 SURPRISE! 🎉</div>
</div>

<!-- BIRTHDAY PHASE -->
<div class="birthday-phase" id="birthdayPhase">
  <div class="confetti-wrap" id="confettiWrap"></div>
  <div class="balloons">
    <div class="balloon b1">🎀</div>
    <div class="balloon b2">🌸</div>
    <div class="balloon b3">🎂</div>
    <div class="balloon b4">🌷</div>
    <div class="balloon b5">💫</div>
  </div>
  <div class="hero-card">
    <div class="cake-emoji">🎂</div>
    <div class="bday-sub">Happy Birthday</div>
    <div class="name-title">Priya 🌸</div>
    <div class="hearts-row">
      <span class="heart">💖</span><span class="heart">💕</span><span class="heart">💗</span>
    </div>
    <div class="pop-message">
      Today the whole world is a little brighter because it's <em>your</em> day! 🌟
      You deserve every flower, every smile, and all the magic the universe holds. 🎀
    </div>
  </div>
  <div class="wish-cards">
    <div class="wish-card"><span class="icon">🌺</span><div class="label">Joy & Happiness</div><div class="desc">Every single day</div></div>
    <div class="wish-card"><span class="icon">💫</span><div class="label">All Your Dreams</div><div class="desc">Coming true, always</div></div>
    <div class="wish-card"><span class="icon">🍰</span><div class="label">Sweetest Moments</div><div class="desc">Savour every second</div></div>
    <div class="wish-card"><span class="icon">🎀</span><div class="label">Love & Laughter</div><div class="desc">Forever surrounding you</div></div>
  </div>
  <div class="secret-card">
    <h3>💌 A little secret…</h3>
    <p>
      There's someone who thinks you're absolutely extraordinary —<br>
      not just today, but every single day. 🌸<br><br>
      Your smile can fix the worst days. Your laugh is the best sound in the world.
      And honestly? You make everything brighter just by being you. 💕<br><br>
      Happy Birthday, Priya. You are so, so loved. 🌷✨
    </p>
    <div style="font-size:24px;margin-top:16px">💖 🌸 💫 🌷 💕</div>
  </div>
  <div class="footer-note">🌟 Made with love, just for you 🌟</div>
</div>

<script>
const starsBg = document.getElementById('stars');
for(let i=0;i<80;i++){
  const s=document.createElement('div');
  s.className='star';
  const sz=0.5+Math.random()*2.5;
  s.style.cssText=`width:${sz}px;height:${sz}px;left:${Math.random()*100}%;top:${Math.random()*100}%;opacity:${0.1+Math.random()*0.7};animation:star-twinkle ${1.5+Math.random()*3}s ease-in-out infinite;animation-delay:${Math.random()*4}s`;
  starsBg.appendChild(s);
}

setTimeout(()=>{
  document.getElementById('revealBtn').classList.add('visible');
},9000);

function startReveal(){
  const overlay=document.getElementById('transitionOverlay');
  const burst=document.getElementById('burstText');
  overlay.classList.add('active');
  setTimeout(()=>{burst.style.opacity='1';burst.style.transform='scale(1)';},200);
  setTimeout(()=>{overlay.style.background='linear-gradient(135deg,#ff6bae44,#c77dff44)';},800);
  setTimeout(()=>{
    document.getElementById('mysteryPhase').style.display='none';
    overlay.classList.remove('active');
    document.getElementById('birthdayPhase').classList.add('show');
    launchConfetti();
  },2000);
}

function launchConfetti(){
  const wrap=document.getElementById('confettiWrap');
  const colors=['#ff8fab','#c77dff','#ff9e8c','#74d7ff','#ffcc66','#98f5e1','#ffb3de','#fff'];
  for(let i=0;i<80;i++){
    const el=document.createElement('div');
    el.className='confetti-piece';
    el.style.left=Math.random()*100+'%';
    el.style.top='-20px';
    el.style.background=colors[Math.floor(Math.random()*colors.length)];
    const dur=2+Math.random()*3;
    el.style.animationDuration=dur+'s';
    el.style.animationDelay=Math.random()*2+'s';
    el.style.width=(7+Math.random()*8)+'px';
    el.style.height=(7+Math.random()*8)+'px';
    el.style.borderRadius=Math.random()>0.5?'50%':'2px';
    wrap.appendChild(el);
    setTimeout(()=>el.remove(),(dur+2)*1000);
  }
}
</script>
</body>
</html>
"""

# Hide all Streamlit chrome so only the HTML shows
st.markdown("""
<style>
  #MainMenu, header, footer, .stAppDeployButton { display: none !important; }
  .stApp { background: #0a0010; }
  .block-container { padding: 0 !important; max-width: 100% !important; }
  iframe { border: none; }
</style>
""", unsafe_allow_html=True)

st.components.v1.html(html_code, height=900, scrolling=True)
