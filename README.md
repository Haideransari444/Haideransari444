
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Syne',sans-serif;background:transparent}
.wrap{max-width:700px;margin:0 auto;padding:8px 0 32px}

.hero{background:#060F0A;border-radius:16px;padding:36px 36px 28px;margin-bottom:12px;position:relative;overflow:hidden}
.hero-grid{position:absolute;inset:0;background-image:repeating-linear-gradient(0deg,rgba(16,185,129,0.04) 0,rgba(16,185,129,0.04) 1px,transparent 1px,transparent 40px),repeating-linear-gradient(90deg,rgba(16,185,129,0.04) 0,rgba(16,185,129,0.04) 1px,transparent 1px,transparent 40px)}
.hero-accent{position:absolute;top:-60px;right:-60px;width:220px;height:220px;border-radius:50%;background:#065F46;opacity:0.35}
.hero-accent2{position:absolute;bottom:-40px;left:60px;width:140px;height:140px;border-radius:50%;background:#059669;opacity:0.15}
.status{display:inline-flex;align-items:center;gap:7px;background:rgba(16,185,129,0.12);border:1px solid rgba(16,185,129,0.25);border-radius:99px;padding:4px 12px;margin-bottom:20px}
.status-dot{width:7px;height:7px;border-radius:50%;background:#10B981}
.status-text{font-family:'JetBrains Mono',monospace;font-size:11px;color:#6EE7B7;letter-spacing:0.5px}
.hero-name{font-size:46px;font-weight:800;color:#fff;line-height:1.1;letter-spacing:-1.5px;margin-bottom:8px;position:relative}
.hero-name em{font-style:normal;color:#10B981}
.hero-sub{font-size:14px;color:#4B5563;font-weight:400;margin-bottom:22px;letter-spacing:0.2px}
.hero-sub span{color:#6B7280}
.pill-row{display:flex;gap:8px;flex-wrap:wrap}
.pill{font-family:'JetBrains Mono',monospace;font-size:11px;padding:5px 12px;border-radius:6px;font-weight:500}
.pill-g{background:rgba(16,185,129,0.12);color:#34D399;border:1px solid rgba(16,185,129,0.22)}
.pill-e{background:rgba(5,150,105,0.1);color:#6EE7B7;border:1px solid rgba(5,150,105,0.2)}
.pill-w{background:rgba(255,255,255,0.04);color:#6B7280;border:1px solid rgba(255,255,255,0.08)}

.card{background:#080F0B;border:1px solid #0D2318;border-radius:14px;padding:22px 24px;margin-bottom:12px}
.card-label{font-family:'JetBrains Mono',monospace;font-size:10px;color:#1F4D36;letter-spacing:1.5px;text-transform:uppercase;margin-bottom:14px}

.row2{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:12px}
.row2 .card{margin-bottom:0}

.proj-item{padding:12px 0;border-bottom:1px solid #0D2318}
.proj-item:last-child{border-bottom:none;padding-bottom:0}
.proj-item:first-of-type{padding-top:0}
.proj-name{font-size:14px;font-weight:600;color:#D1FAE5;margin-bottom:3px}
.proj-desc{font-size:12px;color:#374151;line-height:1.5;margin-bottom:7px}
.tag-row{display:flex;gap:5px;flex-wrap:wrap}
.tag{font-family:'JetBrains Mono',monospace;font-size:10px;color:#059669;background:rgba(5,150,105,0.1);padding:2px 8px;border-radius:4px}

.skill-col{margin-bottom:14px}
.skill-col:last-child{margin-bottom:0}
.skill-col-title{font-family:'JetBrains Mono',monospace;font-size:10px;color:#1F4D36;letter-spacing:1px;margin-bottom:8px}
.skill-chip{font-family:'JetBrains Mono',monospace;font-size:11px;padding:4px 10px;border-radius:5px;color:#6B7280;background:#060F0A;border:1px solid #0D2318;display:inline-block;margin:0 4px 4px 0}

.bio-card{background:#080F0B;border:1px solid #0D2318;border-radius:14px;padding:22px 24px;margin-bottom:12px}
.bio-text{font-size:13px;color:#4B5563;line-height:1.75}
.bio-text strong{color:#34D399;font-weight:500}

.connect-card{background:#080F0B;border:1px solid #0D2318;border-radius:14px;padding:22px 24px}
.connect-grid{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:14px}
.clink{display:flex;align-items:center;gap:10px;padding:10px 14px;border-radius:9px;border:1px solid #0D2318;background:#060F0A;text-decoration:none;transition:border-color 0.2s}
.clink:hover{border-color:#059669}
.clink-icon{width:28px;height:28px;border-radius:7px;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.clink-icon svg{width:14px;height:14px}
.clink-name{font-size:13px;font-weight:600;color:#A7F3D0}
.clink-handle{font-family:'JetBrains Mono',monospace;font-size:10px;color:#1F4D36;margin-top:1px}

.footer-bar{display:flex;align-items:center;justify-content:center;gap:8px;padding-top:20px}
.footer-line{flex:1;height:1px;background:#0D2318}
.footer-text{font-family:'JetBrains Mono',monospace;font-size:10px;color:#1F4D36}
</style>

<div class="wrap">
  <div class="hero">
    <div class="hero-grid"></div>
    <div class="hero-accent"></div>
    <div class="hero-accent2"></div>
    <div style="position:relative">
      <div class="status">
        <div class="status-dot"></div>
        <span class="status-text">open to collabs</span>
      </div>
      <div class="hero-name">muzammil<br><em>haider</em></div>
      <div class="hero-sub">cs student <span>Â·</span> ai/ml engineer <span>Â·</span> full-stack dev</div>
      <div class="pill-row">
        <span class="pill pill-g">NUML University</span>
        <span class="pill pill-e">CGPA 3.60 / 4.0</span>
        <span class="pill pill-w">Islamabad, PK</span>
      </div>
    </div>
  </div>

  <div class="bio-card">
    <p class="bio-text">passionate about building <strong>intelligent systems</strong> that actually solve real problems. currently deep in <strong>neural networks</strong>, <strong>nlp research</strong>, and crafting scalable apps people love to use.</p>
  </div>

  <div class="row2">
    <div class="card">
      <div class="card-label">projects</div>
      <div class="proj-item">
        <div class="proj-name">alif â€” ai tutor</div>
        <div class="proj-desc">adaptive learning with voice interaction & real-time analytics</div>
        <div class="tag-row"><span class="tag">fastapi</span><span class="tag">pytorch</span><span class="tag">gemini</span></div>
      </div>
      <div class="proj-item">
        <div class="proj-name">qanoon â€” legal ai</div>
        <div class="proj-desc">intelligent document analysis for pakistani law</div>
        <div class="tag-row"><span class="tag">langchain</span><span class="tag">transformers</span><span class="tag">spacy</span></div>
      </div>
      <div class="proj-item">
        <div class="proj-name">easy-terminal</div>
        <div class="proj-desc">natural language to shell commands with safety validation</div>
        <div class="tag-row"><span class="tag">openai</span><span class="tag">nlp</span><span class="tag">shell</span></div>
      </div>
      <div class="proj-item">
        <div class="proj-name">mario-rl</div>
        <div class="proj-desc">reinforcement learning mastering super mario bros</div>
        <div class="tag-row"><span class="tag">sb3</span><span class="tag">gym</span><span class="tag">ppo</span></div>
      </div>
    </div>

    <div class="card">
      <div class="card-label">tech stack</div>
      <div class="skill-col">
        <div class="skill-col-title">// ai Â· ml</div>
        <span class="skill-chip">pytorch</span><span class="skill-chip">tensorflow</span><span class="skill-chip">langchain</span><span class="skill-chip">transformers</span><span class="skill-chip">opencv</span><span class="skill-chip">openai</span>
      </div>
      <div class="skill-col">
        <div class="skill-col-title">// web dev</div>
        <span class="skill-chip">fastapi</span><span class="skill-chip">django</span><span class="skill-chip">react</span><span class="skill-chip">tailwind</span><span class="skill-chip">streamlit</span>
      </div>
      <div class="skill-col">
        <div class="skill-col-title">// tools</div>
        <span class="skill-chip">python</span><span class="skill-chip">docker</span><span class="skill-chip">postgresql</span><span class="skill-chip">redis</span><span class="skill-chip">linux</span><span class="skill-chip">git</span>
      </div>
    </div>
  </div>

  <div class="connect-card">
    <div class="card-label">connect</div>
    <div class="connect-grid">
      <a class="clink" href="https://github.com/haideransari444">
        <div class="clink-icon" style="background:rgba(16,185,129,0.12)">
          <svg viewBox="0 0 24 24" fill="none" stroke="#10B981" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"/></svg>
        </div>
        <div><div class="clink-name">github</div><div class="clink-handle">haideransari444</div></div>
      </a>
      <a class="clink" href="https://linkedin.com/in/muzamil-haider-89286329b">
        <div class="clink-icon" style="background:rgba(52,211,153,0.1)">
          <svg viewBox="0 0 24 24" fill="none" stroke="#34D399" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"/><rect x="2" y="9" width="4" height="12"/><circle cx="4" cy="4" r="2"/></svg>
        </div>
        <div><div class="clink-name">linkedin</div><div class="clink-handle">muzamil-haider</div></div>
      </a>
      <a class="clink" href="mailto:muzamilhaider444@gmail.com">
        <div class="clink-icon" style="background:rgba(110,231,183,0.08)">
          <svg viewBox="0 0 24 24" fill="none" stroke="#6EE7B7" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
        </div>
        <div><div class="clink-name">email</div><div class="clink-handle">muzamilhaider444</div></div>
      </a>
      <a class="clink" href="https://x.com/nfak_ism_">
        <div class="clink-icon" style="background:rgba(5,150,105,0.1)">
          <svg viewBox="0 0 24 24" fill="none" stroke="#059669" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M23 3a10.9 10.9 0 0 1-3.14 1.53 4.48 4.48 0 0 0-7.86 3v1A10.66 10.66 0 0 1 3 4s-4 9 5 13a11.64 11.64 0 0 1-7 2c9 5 20 0 20-11.5a4.5 4.5 0 0 0-.08-.83A7.72 7.72 0 0 0 23 3z"/></svg>
        </div>
        <div><div class="clink-name">twitter</div><div class="clink-handle">nfak_ism_</div></div>
      </a>
    </div>
  </div>

  <div class="footer-bar">
    <div class="footer-line"></div>
    <span class="footer-text">always building something cool</span>
    <div class="footer-line"></div>
  </div>
</div>
