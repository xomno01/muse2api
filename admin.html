<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title id="pageTitle">muse2api · Bảng Điều Khiển Tài Khoản</title>
<style>
  :root{
    --bg:#0a0e17; --bg2:#0e1421; --panel:#121a2b; --panel2:#0f1626;
    --line:#20293d; --line2:#2b3550; --text:#e7eaf3; --muted:#8590a8;
    --accent:#4f8cff; --accent2:#2563eb; --ok:#34d399; --bad:#f87171;
    --warn:#fbbf24; --purple:#a78bfa; --radius:12px;
  }
  *{box-sizing:border-box}
  body{
    margin:0;background:radial-gradient(1200px 600px at 15% -10%,#152140 0%,var(--bg) 55%) no-repeat,var(--bg);
    color:var(--text);font:14px/1.6 "Segoe UI",system-ui,-apple-system,"Microsoft YaHei",sans-serif;
    min-height:100vh;
  }
  a{color:var(--accent);text-decoration:none}
  code,kbd,pre{font-family:ui-monospace,SFMono-Regular,Consolas,"Cascadia Mono",monospace}

  /* ---------- 顶栏 ---------- */
  header{
    position:sticky;top:0;z-index:20;backdrop-filter:blur(14px);
    background:rgba(10,14,23,.82);border-bottom:1px solid var(--line);
  }
  .hwrap{max-width:1280px;margin:0 auto;padding:14px 22px;display:flex;align-items:center;gap:16px;flex-wrap:wrap}
  .logo{display:flex;align-items:center;gap:10px;font-weight:650;font-size:17px;letter-spacing:.2px}
  .logo .dot{width:10px;height:10px;border-radius:50%;background:linear-gradient(135deg,var(--accent),var(--purple));box-shadow:0 0 14px rgba(79,140,255,.8)}
  .logo small{color:var(--muted);font-weight:400;font-size:12px;margin-left:2px}
  .pills{display:flex;gap:8px;flex-wrap:wrap;margin-left:auto;align-items:center}
  .pill{
    display:inline-flex;align-items:center;gap:6px;font-size:12px;padding:5px 11px;border-radius:999px;
    background:var(--panel);border:1px solid var(--line);color:var(--muted);white-space:nowrap
  }
  .pill b{color:var(--text);font-weight:600}
  .pill .led{width:7px;height:7px;border-radius:50%;background:var(--muted)}
  .pill.on .led{background:var(--ok);box-shadow:0 0 8px var(--ok)}
  .pill.off .led{background:var(--bad);box-shadow:0 0 8px var(--bad)}

  .keybox{display:flex;align-items:center;gap:6px;background:var(--panel);border:1px solid var(--line);border-radius:9px;padding:4px 6px 4px 11px}
  .keybox input{background:transparent;border:0;color:var(--text);outline:none;width:210px;font-size:12.5px;font-family:ui-monospace,monospace}
  .keybox button{padding:5px 10px;font-size:12px}

  /* ---------- 布局 ---------- */
  main{max-width:1280px;margin:0 auto;padding:22px}
  nav.tabs{display:flex;gap:6px;margin-bottom:20px;flex-wrap:wrap;border-bottom:1px solid var(--line);padding-bottom:0}
  nav.tabs button{
    background:transparent;border:0;border-bottom:2px solid transparent;color:var(--muted);
    padding:10px 16px;font-size:14px;cursor:pointer;border-radius:8px 8px 0 0;transition:.15s
  }
  nav.tabs button:hover{color:var(--text);background:rgba(255,255,255,.03)}
  nav.tabs button.active{color:var(--text);border-bottom-color:var(--accent);font-weight:600}
  .tab{display:none}.tab.active{display:block;animation:fade .18s ease}
  @keyframes fade{from{opacity:0;transform:translateY(4px)}to{opacity:1;transform:none}}

  /* ---------- 卡片 ---------- */
  .card{background:linear-gradient(180deg,var(--panel) 0%,var(--panel2) 100%);border:1px solid var(--line);border-radius:var(--radius);padding:18px;margin-bottom:16px}
  .card>h3{margin:0 0 4px;font-size:14.5px;display:flex;align-items:center;gap:8px}
  .card>h3 .tag{font-size:11px;font-weight:500;color:var(--muted);background:var(--bg2);border:1px solid var(--line);border-radius:6px;padding:1px 7px}
  .hint{color:var(--muted);font-size:12.5px;margin:2px 0 12px}
  .row{display:flex;gap:12px;flex-wrap:wrap;align-items:flex-end}
  .row>div{flex:1;min-width:170px}
  .copyline{display:flex;gap:7px;align-items:center}
  .copyline input{flex:1;font-family:ui-monospace,monospace;font-size:12.5px}

  /* ---------- 分步引导 ---------- */
  .stepbox{display:flex;gap:13px;align-items:flex-start;padding:15px 0;border-bottom:1px solid rgba(32,41,61,.6)}
  .stepbox:last-child{border-bottom:0;padding-bottom:0}
  .stepbox:first-of-type{padding-top:4px}
  .stepno{flex:0 0 26px;width:26px;height:26px;border-radius:50%;background:var(--accent2);color:#fff;
    display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:650;margin-top:1px}
  .btnlike{display:inline-flex;align-items:center;gap:6px;background:var(--accent2);color:#fff;
    border-radius:9px;padding:9px 16px;font-size:13px;text-decoration:none;transition:.15s}
  .btnlike:hover{background:#3b82f6;color:#fff}
  .btnlike.ghostlike{background:transparent;border:1px solid var(--line);color:var(--text)}
  .btnlike.ghostlike:hover{background:rgba(255,255,255,.05);border-color:#37415a;color:var(--text)}
  .olsteps{margin:8px 0 0;padding-left:0;list-style:none;counter-reset:ols}
  .olsteps>li{position:relative;padding:5px 0 5px 30px;font-size:12.5px;color:var(--muted);line-height:1.8;counter-increment:ols}
  .olsteps>li::before{content:counter(ols);position:absolute;left:0;top:6px;width:19px;height:19px;border-radius:50%;
    background:var(--bg2);border:1px solid var(--line);color:var(--text);font-size:11px;font-weight:650;
    display:flex;align-items:center;justify-content:center}
  .olsteps>li>b{color:var(--text)}
  .olsteps>li>code{background:var(--bg2);border:1px solid var(--line);border-radius:5px;padding:1px 6px;font-size:12px;color:var(--accent)}
  kbd{display:inline-block;background:var(--bg2);border:1px solid var(--line);border-bottom-width:2px;
    border-radius:5px;padding:1px 7px;font-size:11.5px;color:var(--text);line-height:1.6;white-space:nowrap}

  /* ---------- 统计 ---------- */
  .stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:12px;margin-bottom:16px}
  .stat{background:linear-gradient(180deg,var(--panel) 0%,var(--panel2) 100%);border:1px solid var(--line);border-radius:var(--radius);padding:15px 17px}
  .stat .k{color:var(--muted);font-size:12px;margin-bottom:4px}
  .stat .v{font-size:25px;font-weight:650;letter-spacing:.4px}
  .stat.g .v{color:var(--ok)}.stat.r .v{color:var(--bad)}.stat.y .v{color:var(--warn)}.stat.b .v{color:var(--accent)}

  /* ---------- 表单 ---------- */
  label{display:block;font-size:12.5px;color:var(--muted);margin-bottom:5px}
  input[type=text],input[type=number],textarea,select{
    width:100%;background:var(--bg2);color:var(--text);border:1px solid var(--line);border-radius:9px;
    padding:9px 12px;font-size:13px;outline:none;transition:.15s;font-family:inherit
  }
  textarea{font-family:ui-monospace,monospace;resize:vertical;line-height:1.55}
  input:focus,textarea:focus,select:focus{border-color:var(--accent);box-shadow:0 0 0 3px rgba(79,140,255,.13)}
  button{
    background:var(--accent2);color:#fff;border:0;border-radius:9px;padding:9px 16px;
    font-size:13px;cursor:pointer;transition:.15s;font-family:inherit;white-space:nowrap
  }
  button:hover{background:#3b82f6}
  button:active{transform:translateY(1px)}
  button:disabled{opacity:.45;cursor:not-allowed}
  button.ghost{background:transparent;border:1px solid var(--line);color:var(--text)}
  button.ghost:hover{background:rgba(255,255,255,.05);border-color:#37415a}
  button.danger{background:transparent;border:1px solid rgba(248,113,113,.4);color:var(--bad)}
  button.danger:hover{background:rgba(248,113,113,.12)}
  button.mini{padding:4px 10px;font-size:12px;border-radius:7px}
  button.primary-lg{padding:11px 24px;font-size:13.5px}

  /* ---------- 表格 ---------- */
  .tblwrap{overflow-x:auto;border:1px solid var(--line);border-radius:var(--radius)}
  table{width:100%;border-collapse:collapse;font-size:13px}
  th{background:var(--bg2);color:var(--muted);font-weight:500;font-size:12px;text-align:left;padding:10px 13px;white-space:nowrap;border-bottom:1px solid var(--line)}
  td{padding:11px 13px;border-bottom:1px solid rgba(32,41,61,.6);vertical-align:middle}
  tbody tr:last-child td{border-bottom:0}
  tbody tr:hover{background:rgba(79,140,255,.045)}
  .mono{font-family:ui-monospace,monospace;font-size:12px;color:var(--muted)}
  .ellip{max-width:260px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;display:inline-block;vertical-align:middle}
  .badge{display:inline-flex;align-items:center;gap:5px;font-size:11.5px;padding:3px 9px;border-radius:999px;border:1px solid;white-space:nowrap}
  .badge.ok{color:var(--ok);border-color:rgba(52,211,153,.35);background:rgba(52,211,153,.1)}
  .badge.bad{color:var(--bad);border-color:rgba(248,113,113,.35);background:rgba(248,113,113,.1)}
  .badge.warn{color:var(--warn);border-color:rgba(251,191,36,.35);background:rgba(251,191,36,.1)}
  .badge.mute{color:var(--muted);border-color:var(--line);background:var(--bg2)}
  .badge.info{color:var(--accent);border-color:rgba(79,140,255,.35);background:rgba(79,140,255,.1)}
  .acts{display:flex;gap:6px;flex-wrap:wrap}
  .empty{text-align:center;color:var(--muted);padding:34px 10px;font-size:13px}

  /* ---------- 媒体库 ---------- */
  .grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(190px,1fr));gap:14px}
  .tile{background:var(--bg2);border:1px solid var(--line);border-radius:var(--radius);overflow:hidden;transition:.18s}
  .tile:hover{border-color:#37415a;transform:translateY(-2px)}
  .tile .thumb{height:150px;background:#060911;display:flex;align-items:center;justify-content:center;overflow:hidden}
  .tile .thumb img,.tile .thumb video{width:100%;height:100%;object-fit:contain;display:block}
  .tile .meta{padding:9px 11px;font-size:11.5px;color:var(--muted)}
  .tile .meta .nm{font-family:ui-monospace,monospace;color:var(--text);font-size:11px;word-break:break-all}
  .tile .meta .ac{display:flex;gap:6px;margin-top:7px}

  /* ---------- 结果预览 ---------- */
  .result{margin-top:14px;padding:14px;background:var(--bg2);border:1px dashed var(--line);border-radius:var(--radius);display:none}
  .result.show{display:block}
  .result img,.result video{max-width:100%;max-height:420px;border-radius:9px;display:block;margin-top:10px;background:#060911}
  pre.out{background:#060911;border:1px solid var(--line);border-radius:9px;padding:12px;overflow:auto;max-height:280px;font-size:12px;color:#9fe8c0;margin:10px 0 0;white-space:pre-wrap;word-break:break-all}

  /* ---------- 提示条 ---------- */
  #toasts{position:fixed;right:20px;bottom:20px;z-index:99;display:flex;flex-direction:column;gap:9px;align-items:flex-end}
  .toast{background:var(--panel);border:1px solid var(--line);border-left:3px solid var(--accent);border-radius:10px;padding:11px 15px;font-size:13px;max-width:380px;box-shadow:0 12px 34px rgba(0,0,0,.55);animation:slide .2s ease}
  .toast.ok{border-left-color:var(--ok)}.toast.bad{border-left-color:var(--bad)}.toast.warn{border-left-color:var(--warn)}
  @keyframes slide{from{opacity:0;transform:translateX(18px)}to{opacity:1;transform:none}}

  /* ---------- 文档 ---------- */
  .doc h4{margin:20px 0 8px;font-size:13.5px;color:var(--text)}
  .doc h4:first-child{margin-top:0}
  pre.code{background:#060911;border:1px solid var(--line);border-radius:9px;padding:14px;overflow:auto;font-size:12.5px;line-height:1.65;color:#cfe3ff;position:relative}
  pre.code .cp{position:absolute;top:8px;right:8px;font-size:11px;padding:3px 9px;background:var(--panel);border:1px solid var(--line);color:var(--muted);border-radius:6px;cursor:pointer}
  pre.code .cp:hover{color:var(--text)}
  .k{color:var(--purple)}.s{color:#7ee2a8}.c{color:#5b6478}
  .spin{display:inline-block;width:13px;height:13px;border:2px solid rgba(255,255,255,.25);border-top-color:#fff;border-radius:50%;animation:sp .7s linear infinite;vertical-align:-2px;margin-right:6px}
  @keyframes sp{to{transform:rotate(360deg)}}
  .live{display:inline-flex;align-items:center;gap:5px;font-size:11.5px;color:var(--muted)}
  .live .led{width:6px;height:6px;border-radius:50%;background:var(--ok);animation:bl 1.6s infinite}
  @keyframes bl{0%,100%{opacity:1}50%{opacity:.25}}

  /* ---------- 未登录提示条 ---------- */
  .banner{display:none;align-items:flex-start;gap:13px;background:linear-gradient(90deg,rgba(251,191,36,.14),rgba(251,191,36,.03));
    border:1px solid rgba(251,191,36,.42);border-radius:var(--radius);padding:15px 18px;margin-bottom:16px;font-size:13.5px;line-height:1.75}
  .banner.show{display:flex}
  .banner .ic{font-size:20px;line-height:1.2}
  .banner b{color:var(--warn)}
  .banner code{background:rgba(0,0,0,.35);padding:2px 7px;border-radius:5px;color:#7dd3fc;font-size:12.5px}
  .keybox.miss{border-color:rgba(251,191,36,.75);box-shadow:0 0 0 3px rgba(251,191,36,.12);animation:pulse 1.8s infinite}
  @keyframes pulse{0%,100%{box-shadow:0 0 0 3px rgba(251,191,36,.12)}50%{box-shadow:0 0 0 5px rgba(251,191,36,.05)}}
  .keybox .lbl{font-size:11.5px;color:var(--muted);padding-left:4px;white-space:nowrap}
  .keybox.ok .lbl{color:var(--ok)}
  .keybox.miss .lbl{color:var(--warn)}
  .updpill-alert{border-color:rgba(251,191,36,.8)!important;background:rgba(251,191,36,.15)!important;color:var(--warn)!important;animation:pulse 1.6s infinite}
</style>
</head>
<body>

<header>
  <div class="hwrap">
    <div class="logo">
      <span class="dot"></span>muse2api <small data-i18n="logo_sub">Hạn ngạch Muse Web · Reverse Proxy API</small>
      <a href="https://github.com/czg86389-hub/muse2api" target="_blank" class="pill" style="margin-left:10px;text-decoration:none;color:var(--text);border-color:var(--line2);cursor:pointer" title="GitHub Repo">
        <svg viewBox="0 0 16 16" width="14" height="14" fill="currentColor" style="vertical-align:-2px"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path></svg>
        <b data-i18n="github_repo">GitHub Repo</b>
      </a>
      <a href="https://linux.do/" target="_blank" class="pill" style="text-decoration:none;color:var(--text);border-color:var(--line2);cursor:pointer" title="LINUX DO 社区">
        🤝 <b>LINUX DO</b>
      </a>
      <button class="ghost mini" onclick="toggleRepoPanel()" id="btnRepoTop" style="display:inline-flex;align-items:center;gap:5px;border-radius:999px;padding:4px 11px;font-size:12px" title="Kiểm tra phiên bản">
        📦 <span id="repoTopTxt" data-i18n="version_check">Kiểm tra cập nhật</span>
      </button>
    </div>
    <div class="pills">
      <button class="pill" id="btnLang" onclick="toggleLang()" style="cursor:pointer;background:var(--panel2);border:1px solid var(--accent);color:var(--text);font-weight:600;padding:5px 12px;gap:6px" title="Chuyển đổi ngôn ngữ / 切换语言">
        🌐 <b id="langTxt">Tiếng Việt</b>
      </button>
      <span class="pill" id="pSvc"><span class="led"></span><span data-i18n="lbl_svc">Dịch vụ</span> <b>—</b></span>
      <span class="pill" id="pAcc"><span class="led"></span><span data-i18n="lbl_acc">Tài khoản</span> <b>—</b></span>
      <span class="pill" id="pBr"><span class="led"></span><span data-i18n="lbl_br">Trình duyệt</span> <b>—</b></span>
      <span class="live" id="live"><span class="led"></span><span data-i18n="auto_refresh">Tự động làm mới</span></span>
      <span class="keybox" id="keyBox">
        <span class="lbl" id="keyLbl">API Key</span>
        <input id="key" type="password" placeholder="Dán khóa m2a_..." autocomplete="off" data-i18n-placeholder="key_placeholder">
        <button class="ghost mini" onclick="saveKey()" data-i18n="btn_save">Lưu</button>
      </span>
    </div>
  </div>
</header>

<main>
  <!-- 实时新版本更新通知横幅（当官方仓库有新提交/新版本时自动向所有已部署用户弹出） -->
  <div class="banner" id="updateBanner" style="border-color:rgba(79,140,255,.65);background:linear-gradient(90deg,rgba(79,140,255,.16),rgba(167,139,250,.05));align-items:center;justify-content:space-between;flex-wrap:wrap">
    <div style="display:flex;gap:12px;align-items:flex-start;flex:1;min-width:260px">
      <span class="ic">🔔</span>
      <div>
        <b style="color:#60a5fa">检测到 muse2api 官方仓库发布了新版本更新！</b>
        <span id="updBannerVer" class="badge info" style="margin-left:8px">新版本</span><br>
        <span id="updBannerMsg" style="color:var(--muted);font-size:13px">官方仓库已有新功能或性能优化提交，点击右侧按钮即可一键在线升级（自动保留本地 .env 密钥与账号池数据）。</span>
      </div>
    </div>
    <div style="display:flex;gap:8px;align-items:center;flex-wrap:wrap">
      <button onclick="upgradeNow()" id="btnBannerUpgrade">⚡ 一键在线升级并重启</button>
      <button class="ghost mini" onclick="toggleRepoPanel()">查看更新内容</button>
      <button class="ghost mini" onclick="dismissUpdateBanner()">暂不提醒</button>
    </div>
  </div>

  <!-- 版本状态与官方仓库更新中心面板 -->
  <div class="card" id="repoPanel" style="display:none;border-color:rgba(79,140,255,.45);margin-bottom:16px">
    <h3>
      <svg viewBox="0 0 16 16" width="15" height="15" fill="currentColor"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path></svg>
      官方仓库版本检测与在线热升级
      <a href="https://github.com/czg86389-hub/muse2api" target="_blank" class="tag" style="color:var(--accent)">czg86389-hub/muse2api ↗</a>
      <span id="repoBadge" class="badge info" style="margin-left:auto">检测中…</span>
    </h3>
    <div class="hint" id="repoStatusDesc">正在实时对比本地版本与 GitHub 官方仓库最新版本…（在线升级自动保留 <code>.env</code> 密钥与 <code>data/</code> 账号池及媒体数据）</div>
    <div id="repoCommitsBox" style="margin-top:10px;background:var(--bg2);border:1px solid var(--line);border-radius:9px;padding:10px 14px;font-size:12.5px"></div>
    <div style="margin-top:12px;display:flex;gap:8px;flex-wrap:wrap;align-items:center">
      <button onclick="upgradeNow()" id="btnRepoPull">⚡ 一键从 GitHub 在线更新并重启</button>
      <button class="ghost" onclick="loadRepoStatus(true)">🔍 立即重新检测更新</button>
      <a href="https://github.com/czg86389-hub/muse2api/commits/main" target="_blank" class="btnlike ghostlike" style="padding:7px 13px;font-size:12.5px">查看 GitHub 完整提交记录 ↗</a>
    </div>
  </div>

  <div class="banner" id="authBanner">
    <span class="ic">🔑</span>
    <div>
      <b data-i18n="auth_banner_title">Cần nhập API Key trước để tải dữ liệu</b><br>
      <span style="color:var(--muted)" data-i18n-html="auth_banner_desc">
        API Key là mật khẩu truy cập của dịch vụ này nhằm bảo vệ hạn ngạch tài khoản Muse của bạn.<br>
        Nó <b style="color:var(--text)">không phải</b> mật khẩu tài khoản muse.ai, mà là chuỗi ký tự ngẫu nhiên (bắt đầu bằng <code>m2a_</code>) được tạo ra khi khởi chạy máy chủ.<br>
        Hãy dán khóa vào ô góc trên bên phải rồi bấm "Lưu" —— trình duyệt sẽ ghi nhớ cho những lần sau.
      </span>
    </div>
  </div>

  <nav class="tabs">
    <button class="active" data-t="pool" data-i18n="tab_pool">Hồ tài khoản</button>
    <button data-t="cookie" data-i18n="tab_cookie">Lấy Cookie</button>
    <button data-t="tasks" data-i18n="tab_tasks">Lịch sử tác vụ</button>
    <button data-t="media" data-i18n="tab_media">Kho Media</button>
    <button data-t="play" data-i18n="tab_play">Kiểm thử API</button>
    <button data-t="docs" data-i18n="tab_docs">Tài liệu kết nối</button>
    <a href="/kol" target="_blank" style="margin-left:auto;text-decoration:none"><button type="button" style="background:linear-gradient(135deg,#ec4899,#8b5cf6);color:#fff;border-radius:8px;font-weight:600;padding:6px 14px;border:none;cursor:pointer;display:inline-flex;align-items:center;gap:6px">✨ MuseKOL Studio</button></a>
  </nav>

  <!-- ==================== 账号池 ==================== -->
  <section class="tab active" id="tab-pool">
    <div class="warnbar" id="expWarn" style="display:none">
      <span id="expWarnText"></span>
      <button class="ghost mini" onclick="goTab('cookie')">去重新登录</button>
    </div>
    <div class="card" style="border-color:rgba(79,140,255,.4)">
      <h3><span data-i18n="conn_title">Thông tin kết nối</span> <span class="tag" data-i18n="conn_tag">Điền 2 giá trị này vào Client</span></h3>
      <div class="hint" data-i18n="conn_hint">Điền hai mục bên dưới vào dự án hoặc phần mềm AI của bạn. BASE URL là tiền tố địa chỉ API.</div>
      <div class="row">
        <div style="flex:3">
          <label data-i18n="lbl_base_url">BASE URL (Địa chỉ API)</label>
          <div class="copyline">
            <input type="text" id="inBase" readonly>
            <button class="ghost mini" onclick="copyEl('inBase')" data-i18n="btn_copy">Sao chép</button>
          </div>
        </div>
        <div style="flex:3">
          <label data-i18n="lbl_api_key">API Key (Khóa truy cập)</label>
          <div class="copyline">
            <input type="text" id="inKey" readonly>
            <button class="ghost mini" onclick="toggleKey()" id="keyEye" data-i18n="btn_show">Hiện</button>
            <button class="ghost mini" onclick="copyKey()" data-i18n="btn_copy">Sao chép</button>
            <button class="danger mini" onclick="rotateKey()" data-i18n="btn_rotate">Tạo mới Key</button>
          </div>
        </div>
      </div>
      <div class="hint" style="margin:11px 0 0" data-i18n-html="model_hint">
        Tên Model: <code>muse-spark</code> (trò chuyện/code), <code>muse-image</code> (vẽ ảnh), <code>muse-video</code> (sinh video). Xem chi tiết tại tab "Tài liệu kết nối".
      </div>
    </div>

    <div class="stats">
      <div class="stat b"><div class="k" data-i18n="stat_total">Tổng tài khoản</div><div class="v" id="sTotal">0</div></div>
      <div class="stat g"><div class="k" data-i18n="stat_ok">Khả dụng</div><div class="v" id="sOk">0</div></div>
      <div class="stat r"><div class="k" data-i18n="stat_bad">Bất thường</div><div class="v" id="sBad">0</div></div>
      <div class="stat y"><div class="k" data-i18n="stat_dis">Đã tắt</div><div class="v" id="sDis">0</div></div>
      <div class="stat"><div class="k" data-i18n="stat_media">Tệp media</div><div class="v" id="sMedia">0</div></div>
    </div>

    <div class="card">
      <h3><span data-i18n="add_acc_title">Thêm tài khoản</span> <span class="tag" data-i18n="add_acc_tag">Hỗ trợ hàng loạt</span></h3>
      <div class="hint" data-i18n-html="add_acc_hint">
        Sao chép chuỗi Cookie của <b>muse.ai</b> từ trình duyệt dán vào đây. Cookie cốt lõi:
        <code>hatch_sess</code>, <code>hatch_gw</code>, <code>hatch_vml</code>, <code>hatch_native_auth_device</code>.
        Khi nhập hàng loạt mỗi dòng 1 tài khoản, định dạng <code>Nhãn | Chuỗi_Cookie</code> (Nhãn có thể bỏ qua).
      </div>
      <div class="row">
        <div style="max-width:230px">
          <label data-i18n="lbl_acc_label">Nhãn tài khoản (Nhập lẻ)</label>
          <input type="text" id="newLabel" placeholder="Ví dụ: muse-chinh" data-i18n-placeholder="ph_label">
        </div>
        <div style="flex:3">
          <label data-i18n="lbl_cookie_str">Chuỗi Cookie</label>
          <textarea id="newCookie" rows="4" placeholder="hatch_sess=...; hatch_gw=...; hatch_vml=...&#10;Hoặc nhập nhiều dòng:&#10;acc-01 | hatch_sess=...; hatch_gw=...&#10;acc-02 | hatch_sess=...; hatch_gw=..." data-i18n-placeholder="ph_cookie"></textarea>
        </div>
      </div>
      <div style="margin-top:12px;display:flex;gap:10px;flex-wrap:wrap">
        <button class="primary-lg" onclick="addAccount(false)" data-i18n="btn_import_acc">Nhập tài khoản</button>
        <button class="ghost" onclick="document.getElementById('newCookie').value='';" data-i18n="btn_clear">Xóa trắng</button>
      </div>
    </div>

    <div class="card">
      <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:10px;margin-bottom:8px">
        <div style="display:flex;align-items:center;gap:10px">
          <h3 style="margin:0"><span data-i18n="list_title">Danh sách tài khoản</span> <span class="tag" id="poolCount">0</span></h3>
          <span class="badge ok" id="keepaliveBadge" style="font-size:11px" data-i18n="ka_badge">● Tự động bảo trì & xoay vòng (30 phút)</span>
        </div>
        <div style="display:flex;gap:8px">
          <button class="secondary" id="btnKeepaliveAll" onclick="keepaliveAll()" style="font-size:12px;padding:6px 14px" data-i18n="btn_ka_all">⚡ Bảo trì ngay toàn bộ tài khoản</button>
        </div>
      </div>
      <div class="hint" data-i18n-html="list_hint">Hệ thống đã kích hoạt <b>bảo trì ngầm mỗi 30 phút</b> và <b>xoay vòng tài khoản thông minh (LRU)</b>; Nút "Kiểm tra" sẽ mở trình duyệt thật để xác thực phiên.</div>
      <div class="tblwrap"><table>
        <thead><tr>
          <th data-i18n="th_label">Nhãn</th><th data-i18n="th_id">Mã ID</th><th data-i18n="th_status">Trạng thái</th><th data-i18n="th_exp">Hạn dùng</th><th data-i18n="th_quota">Hạn ngạch</th><th data-i18n="th_enable">Bật/Tắt</th><th>Cookie</th>
          <th data-i18n="th_last">Dùng gần nhất</th><th data-i18n="th_note">Ghi chú</th><th style="min-width:250px" data-i18n="th_acts">Thao tác</th>
        </tr></thead>
        <tbody id="poolBody"><tr><td colspan="10" class="empty" data-i18n="loading">Đang tải…</td></tr></tbody>
      </table></div>
    </div>
  </section>

  <!-- ==================== 获取 Cookie ==================== -->
  <section class="tab" id="tab-cookie">
    <div class="card" style="border-color:rgba(52,211,153,.45)">
      <h3><span data-i18n="ck_c1_title">Cách 1: Tiện ích mở rộng Chrome</span> <span class="tag" data-i18n="ck_c1_tag">Khuyên dùng · Không cần dòng lệnh · Đa nền tảng</span></h3>
      <div class="hint" data-i18n-html="ck_c1_hint">
        Sử dụng một tiện ích mở rộng nhỏ để đồng bộ ngay phiên đăng nhập <b>muse.ai đang có trên máy bạn</b> sang máy chủ muse2api.
        Không cần cài đặt Python, không cần mở terminal hay gõ lệnh.<br>
        <b>Tại sao bắt buộc dùng tiện ích</b>: 4 cookie cốt lõi của muse.ai đều mang cờ <code>httpOnly</code>, các đoạn script trên Console F12 (<code>document.cookie</code>) không thể đọc được; chỉ có API <code>chrome.cookies</code> của tiện ích mới lấy được.
      </div>

      <div class="stepbox">
        <div class="stepno">1</div>
        <div>
          <b data-i18n="ck_s1_title">Tải và giải nén tiện ích</b>
          <div class="hint" style="margin:4px 0 9px" data-i18n-html="ck_s1_hint">
            Giải nén vào một thư mục cố định trên máy bạn, ví dụ: <code>D:\muse2api-extension</code> hoặc dùng ngay thư mục <code>extension/</code> có sẵn trong repo.
          </div>
          <a class="btnlike" href="/admin/extension" download data-i18n="ck_s1_dl">⬇ Tải muse2api-extension.zip</a>
          <button class="ghost mini" onclick="loadExtFiles()" data-i18n="ck_s1_files">Xem danh sách tệp</button>
          <span class="hint" id="extFiles" style="margin-left:8px"></span>
        </div>
      </div>

      <div class="stepbox">
        <div class="stepno">2</div>
        <div>
          <b data-i18n="ck_s2_title">Cài tiện ích vào trình duyệt đang dùng</b>
          <div class="hint" style="margin:4px 0 9px" data-i18n="ck_s2_hint">
            Thực hiện trên Chrome (hoặc Edge / Brave / Cốc Cốc):
          </div>
          <ol class="olsteps">
            <li data-i18n-html="ck_s2_l1">Nhập <code>chrome://extensions</code> vào thanh địa chỉ rồi nhấn Enter</li>
            <li data-i18n-html="ck_s2_l2">Bật công tắc <b>Chế độ cho nhà phát triển (Developer mode)</b> ở góc trên bên phải</li>
            <li data-i18n-html="ck_s2_l3">Nhấp vào nút <b>Tải tiện ích đã giải nén (Load unpacked)</b> ở góc trên bên trái</li>
            <li data-i18n-html="ck_s2_l4">Chọn thư mục <b>extension</b> (chọn cả thư mục, không phải chọn từng tệp bên trong)</li>
          </ol>
        </div>
      </div>

      <div class="stepbox">
        <div class="stepno">3</div>
        <div>
          <b data-i18n="ck_s3_title">Mở muse.ai và bấm biểu tượng tiện ích để nhập Cookie</b>
          <div class="hint" style="margin:4px 0 9px" data-i18n-html="ck_s3_hint">
            Mở tab <code>https://muse.ai/</code> trên chính trình duyệt đó (đang thấy màn hình chat), nhấp vào biểu tượng Tiện ích trên thanh công cụ, xác nhận 2 thông tin bên dưới rồi bấm <b>"Đọc và Nhập Cookie"</b>.
          </div>
          <div class="row">
            <div style="flex:3">
              <label data-i18n="lbl_ex_base">BASE URL (Điền vào tiện ích)</label>
              <div class="copyline">
                <input type="text" id="exBase" readonly>
                <button class="ghost mini" onclick="copyEl('exBase')" data-i18n="btn_copy">Sao chép</button>
              </div>
            </div>
            <div style="flex:3">
              <label data-i18n="lbl_ex_key">API Key (Điền vào tiện ích)</label>
              <div class="copyline">
                <input type="text" id="exKey" readonly>
                <button class="ghost mini" onclick="copyExKey()" data-i18n="btn_copy">Sao chép</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="card">
      <h3><span data-i18n="ck_m2_title">Cách 2: Sao chép thủ công từ DevTools Network</span> <span class="tag" data-i18n="ck_m2_tag">Không cần cài đặt · Dự phòng</span></h3>
      <div class="hint">
        不想装扩展的话，可以手动把 cookie 串抠出来。关键是用
        <b>「网络」面板的请求标头</b>，而不是 Console —— 请求头里的
        <code>cookie:</code> 一行<b>包含 httpOnly 的那几条</b>，Console 读不到。
      </div>
      <ol class="olsteps" style="margin-top:10px">
        <li>在你自己的浏览器里打开并登录 <code>https://muse.ai/</code>，停在聊天界面</li>
        <li>按 <kbd>F12</kbd> 打开开发者工具，切到 <b>网络 / Network</b> 面板</li>
        <li>按 <kbd>F5</kbd> 刷新页面，让请求列表出现内容</li>
        <li>点列表里<b>任意一条 muse.ai 的请求</b>（第一个就行）</li>
        <li>右侧找到 <b>标头 / Headers</b> → 往下滚到 <b>请求标头 / Request Headers</b></li>
        <li>找到以 <code>cookie:</code> 开头的那一行，<b>把冒号后面的整串复制</b>
            （从 <code>hatch_sess=</code> 开始，一直到行尾）</li>
        <li>粘到下面「方式三」的输入框里，点导入</li>
      </ol>
      <div class="hint" style="margin-top:10px;color:var(--warn)">
        注意：是<b>请求标头</b>里的 <code>cookie:</code>，不是「响应标头」。
        响应标头里的 <code>set-cookie</code> 只有部分 cookie，会缺东西。
      </div>
    </div>

    <div class="card">
      <h3><span data-i18n="ck_m3_title">Cách 3: Dán trực tiếp / Dùng Script Python</span> <span class="tag" data-i18n="ck_m3_tag">Nâng cao</span></h3>
      <div class="hint">已经拿到 cookie 串的话，直接粘在这里导入（方式二手动复制的串也粘这里）。</div>
      <div class="row" style="margin-top:10px">
        <div style="max-width:230px">
          <label>账号标签</label>
          <input type="text" id="mLabel" placeholder="例如 acc-01">
        </div>
        <div style="flex:3">
          <label>Cookie 字符串</label>
          <textarea id="mCookie" rows="3" placeholder="hatch_sess=...; hatch_gw=...; hatch_vml=...; hatch_native_auth_device=..."></textarea>
        </div>
      </div>
      <div style="margin-top:12px">
        <button class="primary-lg" onclick="addAccount(true)">导入账号</button>
      </div>

      <div class="hint" style="margin-top:18px;padding-top:14px;border-top:1px solid var(--line)">
        如果你习惯命令行、或者想用独立浏览器登录（不碰日常浏览器），也可以用这个脚本。
        它只用 Python 标准库，<b>不需要 pip 安装任何东西</b>。
      </div>
      <div class="row" style="margin-top:10px">
        <div style="flex:2">
          <label>① 下载脚本</label>
          <div class="copyline">
            <a class="btnlike ghostlike" href="/admin/cookie-helper?download=1" download>⬇ get_muse_cookie.py</a>
            <a class="btnlike ghostlike" href="/admin/cookie-helper" target="_blank">查看源码</a>
          </div>
        </div>
        <div style="flex:4;min-width:0">
          <label>② 运行（地址和密钥已帮你填好）</label>
          <pre class="code" id="cmdBox"><span class="cp" onclick="copyCmd()">复制</span><span id="cmdText">正在生成命令…</span></pre>
        </div>
      </div>
      <div class="hint" style="margin-top:8px">
        ③ 在弹出的浏览器窗口里登录 muse.ai → 脚本自动抓取并上传 → 自动关窗。
      </div>
    </div>

    <div class="card">
      <h3><span data-i18n="ck_ttl_title">Giải thích về thời hạn hiệu lực của Cookie</span> <span class="tag" data-i18n="ck_ttl_tag">Thực nghiệm</span></h3>
      <div class="hint" style="margin:0 0 12px">
        实测 muse.ai 各条 cookie 的有效期（不同账号可能略有差异）：
      </div>
      <div class="tblwrap"><table>
        <thead><tr><th>cookie</th><th>httpOnly</th><th>实测有效期</th><th>作用</th></tr></thead>
        <tbody>
          <tr><td class="mono">hatch_sess</td><td>是</td><td><b style="color:var(--ok)">约 30 天</b></td><td>主会话，决定能不能登录</td></tr>
          <tr><td class="mono">hatch_gw</td><td>是</td><td><b style="color:var(--ok)">约 1 年</b></td><td>网关令牌</td></tr>
          <tr><td class="mono">hatch_vml</td><td>是</td><td><b style="color:var(--bad)">约 2 天</b></td><td>短效校验令牌，<b>决定账号寿命</b></td></tr>
          <tr><td class="mono">hatch_native_auth_device</td><td>是</td><td><b style="color:var(--ok)">约 30 天</b></td><td>设备标识（匿名访客也有，不是登录凭证）</td></tr>
        </tbody>
      </table></div>
      <div class="hint" style="margin:12px 0 0;line-height:1.85">
        <b>账号实际能活多久？</b>取决于最早过期的那条核心 cookie，也就是
        <code>hatch_vml</code> —— 大约 <b>2 天</b>。<br>
        <b style="color:var(--warn)">注意：这个 2 天不会因为「用得多」而延长。</b>
        本服务每次生成完成后确实会把 muse.ai 新下发的 cookie 读回来写进账号池
        （所以你会看到「有效期」列的数值有更新），但核心 cookie 的到期时间
        <b>不会被推后</b>（已做生成前后对照实验确认）。<br>
        <b>所以：大约每 2 天要重新导入一次。</b>好在很快 —— 点一下扩展图标就行。<br>
        <b>建议一次多导几个账号</b>：账号池按「最久未用」轮转，多账号既更稳，
        也能把重导摊开（每天导一个，而不是所有账号同时失效）。<br>
        <b>什么时候要重导？</b>账号列表里「有效期」变成
        <span class="badge bad">已过期</span>、状态变成
        <span class="badge bad">异常</span>，或出现「缺核心」标记时。
      </div>
    </div>
  </section>

  <!-- ==================== 任务记录 ==================== -->
  <section class="tab" id="tab-tasks">
    <div class="card">
      <h3><span data-i18n="task_title">Lịch sử tác vụ sinh nội dung</span> <span class="tag" id="taskCount">0</span></h3>
      <div class="hint" data-i18n="task_hint">Sinh video là tác vụ bất đồng bộ, trạng thái chuyển từ queued → processing → completed / failed.</div>
      <div style="margin-bottom:12px;display:flex;gap:9px">
        <button class="ghost mini" onclick="loadTasks()" data-i18n="btn_refresh">Làm mới</button>
        <button class="danger mini" onclick="clearTasks()" data-i18n="btn_clear_all">Xóa tất cả</button>
      </div>
      <div class="tblwrap"><table>
        <thead><tr>
          <th data-i18n="th_task_id">Mã tác vụ</th><th data-i18n="th_task_type">Loại</th><th data-i18n="th_task_prompt">Câu lệnh (Prompt)</th><th data-i18n="th_task_status">Trạng thái</th>
          <th data-i18n="th_task_time">Thời gian</th><th data-i18n="th_task_created">Thời điểm tạo</th><th data-i18n="th_task_result">Kết quả / Lỗi</th><th data-i18n="th_acts">Thao tác</th>
        </tr></thead>
        <tbody id="taskBody"><tr><td colspan="8" class="empty" data-i18n="loading">Đang tải…</td></tr></tbody>
      </table></div>
    </div>
  </section>

  <!-- ==================== 媒体库 ==================== -->
  <section class="tab" id="tab-media">
    <div class="card">
      <h3><span data-i18n="media_title">Kho lưu trữ Media</span> <span class="tag" id="mediaCount">0</span></h3>
      <div class="hint" data-i18n="media_hint">Tất cả hình ảnh và video đã sinh và lưu trên đĩa, có thể tải về trực tiếp hoặc dùng link cho các ứng dụng khác.</div>
      <div style="margin-bottom:14px"><button class="ghost mini" onclick="loadMedia()" data-i18n="btn_refresh">Làm mới</button></div>
      <div class="grid" id="mediaGrid"><div class="empty" data-i18n="loading">Đang tải…</div></div>
    </div>
  </section>

  <!-- ==================== 接口测试 ==================== -->
  <section class="tab" id="tab-play">
    <div class="card">
      <h3><span data-i18n="test_img_title">Thử nghiệm sinh ảnh trực tuyến</span> <span class="tag">POST /v1/images/generations</span></h3>
      <div class="hint" data-i18n="test_img_hint">Gọi trực tiếp muse.ai để vẽ, ảnh trả về trong khoảng 10–30 giây.</div>
      <div class="row">
        <div style="flex:3"><label data-i18n="lbl_prompt">Câu lệnh (Prompt)</label>
          <input type="text" id="imgPrompt" value="一只戴宇航头盔的柴犬，赛博朋克风格，霓虹灯背景" data-i18n-value="test_img_val"></div>
        <div style="max-width:140px"><label data-i18n="lbl_ratio">Tỷ lệ</label>
          <select id="imgSize"><option>1:1</option><option>16:9</option><option>9:16</option><option>4:3</option><option>3:4</option></select></div>
      </div>
      <div style="margin-top:12px"><button class="primary-lg" id="imgBtn" onclick="runImage()" data-i18n="btn_gen_img">Bắt đầu sinh ảnh</button></div>
      <div class="result" id="imgRes"></div>
    </div>

    <div class="card">
      <h3><span data-i18n="test_vid_title">Thử nghiệm sinh video trực tuyến</span> <span class="tag">POST /v1/videos</span></h3>
      <div class="hint" data-i18n="test_vid_hint">Tác vụ bất đồng bộ, thường mất 60–120 giây để hoàn thành, trang web sẽ tự động theo dõi tiến độ.</div>
      <div class="row">
        <div style="flex:3"><label data-i18n="lbl_prompt">Câu lệnh (Prompt)</label>
          <input type="text" id="vidPrompt" value="一只橙色小猫在草地上慢慢走动，阳光明媚" data-i18n-value="test_vid_val"></div>
        <div style="max-width:110px"><label data-i18n="lbl_duration">Thời lượng (giây)</label>
          <input type="number" id="vidDur" value="5" min="1" max="30"></div>
        <div style="max-width:140px"><label data-i18n="lbl_ratio">Tỷ lệ</label>
          <select id="vidSize"><option>16:9</option><option>9:16</option><option>1:1</option></select></div>
      </div>
      <div style="margin-top:12px"><button class="primary-lg" id="vidBtn" onclick="runVideo()" data-i18n="btn_gen_vid">Bắt đầu sinh video</button></div>
      <div class="result" id="vidRes"></div>
    </div>
  </section>

  <!-- ==================== 接入文档 ==================== -->
  <section class="tab" id="tab-docs">
    <div class="card doc">
      <h3>接入说明</h3>
      <div class="hint">
        接口与 OpenAI 风格对齐，下游项目只需改 <code>base_url</code> 和 <code>api_key</code>。
        <br>BASE URL：<code id="dBase">—</code>
      </div>

      <h4>1. 可用模型</h4>
      <div class="tblwrap"><table>
        <thead><tr><th>模型 ID</th><th>用途</th><th>接口</th></tr></thead>
        <tbody>
          <tr><td class="mono">muse-spark</td><td>文本 / 代码对话（支持流式）</td><td class="mono">POST /v1/chat/completions<br>POST /v1/responses</td></tr>
          <tr><td class="mono">muse-image</td><td>文生图 / 图像编辑</td><td class="mono">POST /v1/images/generations</td></tr>
          <tr><td class="mono">muse-video</td><td>文生视频 / 图生视频</td><td class="mono">POST /v1/videos → GET /v1/videos/{id}</td></tr>
        </tbody>
      </table></div>
      <div class="hint" style="margin-top:6px">
        这三个就是 Muse 系列的真实能力：<b>Muse Spark</b>（语言 / 代码）、<b>Muse Image</b>（生图）、
        <b>Muse Video</b>（生视频）。muse.ai 网页是自动路由的 agent、界面没有模型选择器，
        所以 <code>model</code> 字段只用于兼容下游 —— 传 <code>gpt-4o</code>、
        <code>claude-sonnet-4</code>、<code>dall-e-3</code> 等常见名字会自动映射到对应能力。
      </div>

      <h4>2. 对话 / 写代码</h4>
      <pre class="code"><span class="cp" onclick="cp(this)">复制</span><span class="c"># 非流式</span>
curl -X POST <span class="s">"BASE/v1/chat/completions"</span> \
  -H <span class="s">"Authorization: Bearer $MUSE2API_KEY"</span> \
  -H <span class="s">"Content-Type: application/json"</span> \
  -d <span class="s">'{"model":"muse-spark","messages":[{"role":"user","content":"写一个 Python 快排"}]}'</span>

<span class="c"># 流式：加 "stream":true，返回标准 SSE（data: {...} / data: [DONE]）</span></pre>

      <h4>3. 生图（curl）</h4>
      <pre class="code"><span class="cp" onclick="cp(this)">复制</span>curl -X POST <span class="s">"BASE/v1/images/generations"</span> \
  -H <span class="s">"Authorization: Bearer $MUSE2API_KEY"</span> \
  -H <span class="s">"Content-Type: application/json"</span> \
  -d <span class="s">'{"prompt":"一只戴宇航头盔的柴犬","size":"1:1","response_format":"url"}'</span>

<span class="c"># 返回</span>
{<span class="k">"created"</span>:1790148495,<span class="k">"data"</span>:[{
  <span class="k">"revised_prompt"</span>:<span class="s">"一只戴宇航头盔的柴犬"</span>,
  <span class="k">"url"</span>:<span class="s">"http://your-server:18610/v1/media/xxxx.webp"</span>,
  <span class="k">"kind"</span>:<span class="s">"image"</span>,<span class="k">"bytes"</span>:23860}]}

<span class="c"># url 是完整绝对地址，可直接给下游渲染 / 下载；/v1/media/* 无需鉴权。</span>
<span class="c"># 想要 base64 就传 "response_format":"b64_json"。</span></pre>

      <h4>4. 生视频（curl，异步）</h4>
      <pre class="code"><span class="cp" onclick="cp(this)">复制</span><span class="c"># ① 创建任务</span>
curl -X POST <span class="s">"BASE/v1/videos"</span> \
  -H <span class="s">"Authorization: Bearer $MUSE2API_KEY"</span> \
  -H <span class="s">"Content-Type: application/json"</span> \
  -d <span class="s">'{"prompt":"一只小猫在草地上走动","duration":5,"size":"16:9"}'</span>
<span class="c"># → {"id":"task_xxx","status":"queued"}</span>

<span class="c"># ② 轮询结果</span>
curl <span class="s">"BASE/v1/videos/task_xxx"</span> -H <span class="s">"Authorization: Bearer $MUSE2API_KEY"</span>
<span class="c"># → {"status":"succeeded","result":{"url":"/v1/media/xxx.mp4"}}</span></pre>

      <h4>5. Python（openai SDK 兼容）</h4>
      <pre class="code"><span class="cp" onclick="cp(this)">复制</span><span class="k">from</span> openai <span class="k">import</span> OpenAI
<span class="k">import</span> time

client = OpenAI(base_url=<span class="s">"BASE/v1"</span>, api_key=<span class="s">"m2a_..."</span>)

<span class="c"># 生图</span>
r = client.images.generate(model=<span class="s">"muse-image"</span>, prompt=<span class="s">"一只戴宇航头盔的柴犬"</span>)
<span class="k">print</span>(r.data[<span class="s">0</span>].url)

<span class="c"># 生视频（走原生接口，因为是异步任务）</span>
<span class="k">import</span> requests
t = requests.post(<span class="s">"BASE/v1/videos"</span>, json={<span class="s">"prompt"</span>:<span class="s">"小猫走动"</span>,<span class="s">"duration"</span>:<span class="s">5</span>},
                  headers={<span class="s">"Authorization"</span>:<span class="s">"Bearer m2a_..."</span>}).json()
<span class="k">while</span> <span class="k">True</span>:
    s = requests.get(<span class="s">f"BASE/v1/videos/{t['id']}"</span>,
                     headers={<span class="s">"Authorization"</span>:<span class="s">"Bearer m2a_..."</span>}).json()
    <span class="k">if</span> s[<span class="s">"status"</span>] <span class="k">in</span> (<span class="s">"succeeded"</span>,<span class="s">"failed"</span>): <span class="k">break</span>
    time.sleep(<span class="s">5</span>)
<span class="k">print</span>(s)</pre>

      <h4>6. 管理接口</h4>
      <div class="tblwrap"><table>
        <thead><tr><th>方法</th><th>路径</th><th>说明</th></tr></thead>
        <tbody>
          <tr><td class="mono">GET</td><td class="mono">/admin/status</td><td>服务总览 + 账号池 + 最近任务</td></tr>
          <tr><td class="mono">GET</td><td class="mono">/admin/accounts</td><td>账号列表</td></tr>
          <tr><td class="mono">POST</td><td class="mono">/admin/accounts</td><td>添加账号（单条 / batch 批量文本）</td></tr>
          <tr><td class="mono">PATCH</td><td class="mono">/admin/accounts/{id}</td><td>改标签 / 启用禁用</td></tr>
          <tr><td class="mono">DELETE</td><td class="mono">/admin/accounts/{id}</td><td>删除账号</td></tr>
          <tr><td class="mono">POST</td><td class="mono">/admin/accounts/{id}/test</td><td>真实校验会话有效性（顺带刷新额度）</td></tr>
          <tr><td class="mono">POST</td><td class="mono">/admin/accounts/{id}/quota</td><td>实时读取该账号剩余额度</td></tr>
          <tr><td class="mono">POST</td><td class="mono">/admin/accounts/{id}/cookies</td><td>更新该账号 cookie</td></tr>
          <tr><td class="mono">GET</td><td class="mono">/admin/tasks</td><td>任务记录</td></tr>
          <tr><td class="mono">GET</td><td class="mono">/admin/media</td><td>媒体库列表</td></tr>
        </tbody>
      </table></div>

      <h4>7. 鉴权</h4>
      <div class="hint" style="margin:0">
        除 <code>/healthz</code>、<code>/readyz</code>、<code>/v1/media/*</code> 外，其余接口均需
        <code>Authorization: Bearer &lt;API Key&gt;</code>。API Key 在服务器
        <code>/opt/muse2api/.env</code> 的 <code>MUSE2API_KEY</code> 中配置。
      </div>

      <h4>8. 接入各类客户端 / 智能体</h4>
      <div class="hint">
        凡是支持「自定义 OpenAI 兼容端点」的客户端，都只填三个值就能用：
      </div>
      <div class="tblwrap" style="margin-top:8px"><table>
        <thead><tr><th>配置项</th><th>填什么</th></tr></thead>
        <tbody>
          <tr><td>Base URL / API 地址</td><td class="mono">http://&lt;你的服务器IP或域名&gt;:18610/v1</td></tr>
          <tr><td>API Key</td><td class="mono">m2a_...（本页顶部「接入信息」里那个）</td></tr>
          <tr><td>模型名</td><td class="mono">muse-spark</td></tr>
        </tbody>
      </table></div>

      <div class="hint" style="margin-top:14px">
        <b>模型名随便填也能用</b>：常见名字（<code>gpt-4o</code>、<code>gpt-5</code>、
        <code>claude-sonnet-4</code>、<code>deepseek-chat</code>、<code>gemini-2.5-pro</code> 等）
        会自动映射到对应能力；完全没见过的名字会原样透传，muse.ai 那边本来就是自动路由，
        不影响结果。
      </div>

      <h4 style="margin-top:18px">按客户端类型看能不能用</h4>
      <div class="tblwrap"><table>
        <thead><tr><th>客户端类型</th><th>依赖能力</th><th>状态</th></tr></thead>
        <tbody>
          <tr><td>对话 / 聊天类（桌面端、Web UI、浏览器插件）</td><td class="mono">POST /v1/chat/completions</td><td><span class="badge ok">✅ 可用</span></td></tr>
          <tr><td>流式输出（打字机效果）</td><td class="mono">stream:true（标准 SSE）</td><td><span class="badge ok">✅ 可用</span></td></tr>
          <tr><td>代码补全 / 内联补全插件</td><td class="mono">POST /v1/chat/completions</td><td><span class="badge ok">✅ 可用</span></td></tr>
          <tr><td>翻译 / 总结 / 解释类工具</td><td class="mono">POST /v1/chat/completions</td><td><span class="badge ok">✅ 可用</span></td></tr>
          <tr><td>画图类客户端</td><td class="mono">POST /v1/images/generations</td><td><span class="badge ok">✅ 可用</span></td></tr>
          <tr><td>视频生成客户端</td><td class="mono">POST /v1/videos（异步轮询）</td><td><span class="badge ok">✅ 可用</span></td></tr>
          <tr><td>需要「工具调用」的自主 Agent 模式</td><td class="mono">tool_calls / function calling</td><td><span class="badge warn">⚠️ 不可用</span></td></tr>
        </tbody>
      </table></div>

      <div class="hint" style="margin-top:8px">
        <b>关于「工具调用」这条限制（重要，已实测）：</b><br>
        muse.ai 的网页助手对「输出伪工具调用 JSON」有明确的对齐拒绝策略 —— 实测原话是
        「我不会按这种 JSON 格式输出'伪工具调用'——我没有 get_weather 这个工具」。
        用三种不同措辞、不同位置的提示词协议去适配，全部失败。<br>
        所以：依赖 <code>tool_calls</code> 的<b>自主 Agent 模式</b>（自动读写文件、执行命令那一类）接不了；
        但所有<b>问答式</b>用法 —— 对话、写代码、解释、翻译、总结、生图、生视频 —— <b>全部完全可用</b>。<br>
        客户端若强行带上 <code>tools</code> 字段，接口不会报错，会忽略工具声明、按普通对话正常回答。
      </div>
    </div>
  </section>
</main>

<footer style="max-width:1280px;margin:18px auto 32px;padding:12px 24px;text-align:center;color:var(--muted);font-size:12px;border-top:1px solid var(--line)">
  <span>开源仓库：<a href="https://github.com/czg86389-hub/muse2api" target="_blank" style="color:var(--acc);text-decoration:none">GitHub · muse2api</a></span>
  <span style="margin:0 10px">·</span>
  <span>社区认可与友情链接：<a href="https://linux.do/" target="_blank" style="color:var(--acc);text-decoration:none;font-weight:600">LINUX DO 社区 (https://linux.do/)</a></span>
</footer>

<div id="toasts"></div>

<script>
/* ================= ĐA NGÔN NGỮ (I18N: VIETNAMESE / CHINESE) ================= */
let LANG = localStorage.getItem('muse2api_lang') || 'vi';

const I18N = {
  vi: {
    doc_title: "muse2api · Bảng Điều Khiển Tài Khoản",
    logo_sub: "Hạn ngạch Muse Web · Reverse Proxy API",
    github_repo: "GitHub Repo",
    version_check: "Kiểm tra cập nhật",
    lbl_svc: "Dịch vụ",
    lbl_acc: "Tài khoản",
    lbl_br: "Trình duyệt",
    auto_refresh: "Tự động làm mới",
    key_placeholder: "Dán khóa m2a_...",
    btn_save: "Lưu",
    tab_pool: "Hồ tài khoản",
    tab_cookie: "Lấy Cookie",
    tab_tasks: "Lịch sử tác vụ",
    tab_media: "Kho Media",
    tab_play: "Kiểm thử API",
    tab_docs: "Tài liệu kết nối",
    auth_banner_title: "Cần nhập API Key trước để tải dữ liệu",
    auth_banner_desc: "API Key là mật khẩu truy cập của dịch vụ này nhằm bảo vệ hạn ngạch tài khoản Muse của bạn.<br>Nó <b style=\"color:var(--text)\">không phải</b> mật khẩu tài khoản muse.ai, mà là chuỗi ký tự ngẫu nhiên (bắt đầu bằng <code>m2a_</code>) được tạo ra khi khởi chạy máy chủ.<br>Hãy dán khóa vào ô góc trên bên phải rồi bấm \"Lưu\" —— trình duyệt sẽ ghi nhớ cho những lần sau.",
    conn_title: "Thông tin kết nối",
    conn_tag: "Điền 2 giá trị này vào Client",
    conn_hint: "Điền hai mục bên dưới vào dự án hoặc phần mềm AI của bạn. BASE URL là tiền tố địa chỉ API.",
    lbl_base_url: "BASE URL (Địa chỉ API)",
    lbl_api_key: "API Key (Khóa truy cập)",
    btn_copy: "Sao chép",
    btn_show: "Hiện",
    btn_hide: "Ẩn",
    btn_rotate: "Tạo mới Key",
    model_hint: "Tên Model: <code>muse-spark</code> (trò chuyện/code), <code>muse-image</code> (vẽ ảnh), <code>muse-video</code> (sinh video). Xem chi tiết tại tab \"Tài liệu kết nối\".",
    stat_total: "Tổng tài khoản",
    stat_ok: "Khả dụng",
    stat_bad: "Bất thường",
    stat_dis: "Đã tắt",
    stat_media: "Tệp media",
    add_acc_title: "Thêm tài khoản",
    add_acc_tag: "Hỗ trợ hàng loạt",
    add_acc_hint: "Sao chép chuỗi Cookie của <b>muse.ai</b> từ trình duyệt dán vào đây. Cookie cốt lõi: <code>hatch_sess</code>, <code>hatch_gw</code>, <code>hatch_vml</code>, <code>hatch_native_auth_device</code>. Khi nhập hàng loạt mỗi dòng 1 tài khoản, định dạng <code>Nhãn | Chuỗi_Cookie</code> (Nhãn có thể bỏ qua).",
    lbl_acc_label: "Nhãn tài khoản (Nhập lẻ)",
    ph_label: "Ví dụ: muse-chinh",
    lbl_cookie_str: "Chuỗi Cookie",
    ph_cookie: "hatch_sess=...; hatch_gw=...; hatch_vml=...\nHoặc nhập nhiều dòng:\nacc-01 | hatch_sess=...; hatch_gw=...\nacc-02 | hatch_sess=...; hatch_gw=...",
    btn_import_acc: "Nhập tài khoản",
    btn_clear: "Xóa trắng",
    list_title: "Danh sách tài khoản",
    ka_badge: "● Tự động bảo trì & xoay vòng (30 phút)",
    btn_ka_all: "⚡ Bảo trì ngay toàn bộ tài khoản",
    list_hint: "Hệ thống đã kích hoạt <b>bảo trì ngầm mỗi 30 phút</b> và <b>xoay vòng tài khoản thông minh (LRU)</b>; Nút \"Kiểm tra\" sẽ mở trình duyệt thật để xác thực phiên.",
    th_label: "Nhãn",
    th_id: "Mã ID",
    th_status: "Trạng thái",
    th_exp: "Hạn dùng",
    th_quota: "Hạn ngạch",
    th_enable: "Bật/Tắt",
    th_last: "Dùng gần nhất",
    th_note: "Ghi chú",
    th_acts: "Thao tác",
    loading: "Đang tải…",
    empty_pool: "Chưa có tài khoản nào. Hãy chuyển sang tab \"Lấy Cookie\" theo 3 bước để nạp tài khoản.",
    act_test: "Kiểm tra",
    act_ka: "Bảo trì",
    act_quota: "Quota",
    act_enable: "Bật",
    act_disable: "Tắt",
    act_rename: "Đổi tên",
    act_update_ck: "Đổi Cookie",
    act_delete: "Xóa",
    badge_ok: "● Khả dụng",
    badge_bad: "● Bất thường",
    badge_unchecked: "○ Chưa kiểm tra",
    badge_disabled: "Đã tắt",
    badge_miss_core: "Thiếu cookie lõi",
    badge_on: "Bật",
    badge_off: "Tắt",
    exp_never: "Chưa rõ",
    exp_expired: "Đã hết hạn",
    exp_left_d: "Còn {d} ngày",
    exp_left_h: "Còn {h} giờ",
    task_title: "Lịch sử tác vụ sinh nội dung",
    task_hint: "Sinh video là tác vụ bất đồng bộ, trạng thái chuyển từ queued → processing → completed / failed.",
    btn_refresh: "Làm mới",
    btn_clear_all: "Xóa tất cả",
    th_task_id: "Mã tác vụ",
    th_task_type: "Loại",
    th_task_prompt: "Câu lệnh (Prompt)",
    th_task_status: "Trạng thái",
    th_task_time: "Thời gian",
    th_task_created: "Thời điểm tạo",
    th_task_result: "Kết quả / Lỗi",
    media_title: "Kho lưu trữ Media",
    media_hint: "Tất cả hình ảnh và video đã sinh và lưu trên đĩa, có thể tải về trực tiếp hoặc dùng link cho các ứng dụng khác.",
    test_img_title: "Thử nghiệm sinh ảnh trực tuyến",
    test_img_hint: "Gọi trực tiếp muse.ai để vẽ, ảnh trả về trong khoảng 10–30 giây.",
    lbl_prompt: "Câu lệnh (Prompt)",
    lbl_ratio: "Tỷ lệ",
    btn_gen_img: "Bắt đầu sinh ảnh",
    test_vid_title: "Thử nghiệm sinh video trực tuyến",
    test_vid_hint: "Tác vụ bất đồng bộ, thường mất 60–120 giây để hoàn thành, trang web sẽ tự động theo dõi tiến độ.",
    lbl_duration: "Thời lượng (giây)",
    btn_gen_vid: "Bắt đầu sinh video",
    test_img_val: "Một chú chó Shiba đội mũ phi hành gia, phong cách cyberpunk, ánh sáng neon rực rỡ",
    test_vid_val: "Một chú mèo con màu cam đi dạo chậm rãi trên thảm cỏ xanh mướt, ánh nắng chan hòa"
  },
  zh: {
    doc_title: "muse2api · 账号池控制台",
    logo_sub: "Muse 网页额度 · 反代 API",
    github_repo: "GitHub 仓库",
    version_check: "版本检测",
    lbl_svc: "服务",
    lbl_acc: "账号",
    lbl_br: "浏览器",
    auto_refresh: "自动刷新",
    key_placeholder: "粘贴 m2a_ 开头的密钥",
    btn_save: "保存",
    tab_pool: "账号池",
    tab_cookie: "获取 Cookie",
    tab_tasks: "任务记录",
    tab_media: "媒体库",
    tab_play: "接口测试",
    tab_docs: "接入文档",
    auth_banner_title: "需要先填入 API Key，页面才能读到数据",
    auth_banner_desc: "API Key 是这个服务自己的「访问密码」，用来防止别人白用你的 Muse 账号额度。<br>它<b style=\"color:var(--text)\">不是</b> Muse 的账号密码，是部署时自动生成的一串随机字符（以 <code>m2a_</code> 开头）。<br>把它粘贴到右上角的输入框，点「保存」即可 —— 浏览器会记住，下次不用再输。",
    conn_title: "接入信息",
    conn_tag: "下游项目填这两个值",
    conn_hint: "把下面两项填进你的项目就能调用。BASE URL 就是接口地址前缀。",
    lbl_base_url: "BASE URL（接口地址）",
    lbl_api_key: "API Key（访问密钥）",
    btn_copy: "复制",
    btn_show: "显示",
    btn_hide: "隐藏",
    btn_rotate: "重新生成",
    model_hint: "模型名：<code>muse-spark</code>（对话/代码）、<code>muse-image</code>（生图）、<code>muse-video</code>（生视频）。完整调用示例见「接入文档」页签。",
    stat_total: "账号总数",
    stat_ok: "可用",
    stat_bad: "异常",
    stat_dis: "已禁用",
    stat_media: "媒体文件",
    add_acc_title: "添加账号",
    add_acc_tag: "支持批量",
    add_acc_hint: "从浏览器复制 <b>muse.ai</b> 的 Cookie 字符串粘贴进来即可。关键 cookie：<code>hatch_sess</code>、<code>hatch_gw</code>、<code>hatch_vml</code>。批量导入时每行一个账号，格式 <code>标签 | cookie串</code>（标签可省略）。",
    lbl_acc_label: "账号标签（单条导入用）",
    ph_label: "例如 muse-main",
    lbl_cookie_str: "Cookie 字符串",
    ph_cookie: "hatch_sess=...; hatch_gw=...; hatch_vml=...\n或批量：\nacc-01 | hatch_sess=...; hatch_gw=...\nacc-02 | hatch_sess=...; hatch_gw=...",
    btn_import_acc: "导入账号",
    btn_clear: "清空",
    list_title: "账号列表",
    ka_badge: "● 自动保活轮转中 (30m)",
    btn_ka_all: "⚡ 一键保活所有账号",
    list_hint: "系统已开启<b>后台每 30 分钟静默保活</b>与<b>多账号公平轮转（LRU）</b>；「测试」会真实打开 muse.ai 验证会话。",
    th_label: "标签",
    th_id: "账号 ID",
    th_status: "状态",
    th_exp: "有效期",
    th_quota: "额度",
    th_enable: "启用",
    th_last: "最后使用",
    th_note: "备注",
    th_acts: "操作",
    loading: "加载中…",
    empty_pool: "还没有账号。去「获取 Cookie」页签按三步导入一个",
    act_test: "测试",
    act_ka: "保活",
    act_quota: "额度",
    act_enable: "启用",
    act_disable: "禁用",
    act_rename: "改名",
    act_update_ck: "更新Cookie",
    act_delete: "删除",
    badge_ok: "● 可用",
    badge_bad: "● 异常",
    badge_unchecked: "○ 未检测",
    badge_disabled: "已禁用",
    badge_miss_core: "缺核心",
    badge_on: "开",
    badge_off: "关",
    exp_never: "未知",
    exp_expired: "已过期",
    exp_left_d: "剩 {d} 天",
    exp_left_h: "剩 {h} 小时",
    task_title: "生成任务记录",
    task_hint: "生视频是异步任务，状态会从 queued → processing → succeeded / failed。",
    btn_refresh: "刷新",
    btn_clear_all: "清空全部",
    th_task_id: "任务 ID",
    th_task_type: "类型",
    th_task_prompt: "提示词",
    th_task_status: "状态",
    th_task_time: "耗时",
    th_task_created: "创建时间",
    th_task_result: "结果 / 错误",
    media_title: "媒体库",
    media_hint: "所有已生成并落盘的图片 / 视频，可直接下载或把链接给下游项目使用。",
    test_img_title: "在线生图测试",
    test_img_hint: "真实调用 muse.ai 生成，图片约 10–30 秒返回。",
    lbl_prompt: "提示词",
    lbl_ratio: "比例",
    btn_gen_img: "开始生成图片",
    test_vid_title: "在线生视频测试",
    test_vid_hint: "异步任务，一般 60–120 秒完成，页面会自动轮询进度。",
    lbl_duration: "时长(秒)",
    btn_gen_vid: "开始生成视频",
    test_img_val: "一只戴宇航头盔的柴犬，赛博朋克风格，霓虹灯背景",
    test_vid_val: "一只橙色小猫在草地上慢慢走动，阳光明媚"
  }
};

function t(k, fallback) {
  const dict = I18N[LANG] || I18N['vi'];
  if (dict && dict[k] !== undefined) return dict[k];
  return fallback !== undefined ? fallback : k;
}

function applyLang(lang) {
  LANG = lang || localStorage.getItem('muse2api_lang') || 'vi';
  localStorage.setItem('muse2api_lang', LANG);
  const dict = I18N[LANG] || I18N['vi'];
  
  document.querySelectorAll('[data-i18n]').forEach(el => {
    const k = el.dataset.i18n;
    if (dict[k] !== undefined) el.textContent = dict[k];
  });
  document.querySelectorAll('[data-i18n-html]').forEach(el => {
    const k = el.dataset.i18nHtml;
    if (dict[k] !== undefined) el.innerHTML = dict[k];
  });
  document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
    const k = el.dataset.i18nPlaceholder;
    if (dict[k] !== undefined) el.placeholder = dict[k];
  });
  document.querySelectorAll('[data-i18n-value]').forEach(el => {
    const k = el.dataset.i18nValue;
    if (dict[k] !== undefined) el.value = dict[k];
  });
  
  document.title = t('doc_title');
  const btnTxt = $('langTxt');
  if (btnTxt) btnTxt.textContent = LANG === 'vi' ? 'Tiếng Việt' : '中文';
  
  if (typeof renderKey === 'function') renderKey();
  if (typeof loadStatus === 'function') loadStatus();
  if (typeof loadPool === 'function') loadPool();
}

function toggleLang() {
  const next = LANG === 'vi' ? 'zh' : 'vi';
  applyLang(next);
  toast(LANG === 'vi' ? 'Đã chuyển sang Tiếng Việt 🇻🇳' : '已切换至中文 🇨🇳', 'ok');
}

/* ================= 基础 ================= */
const $ = id => document.getElementById(id);
const KEY_STORE = 'muse2api_key';
let KEY = localStorage.getItem(KEY_STORE) || new URLSearchParams(location.search).get('key') || '';
$('key').value = KEY;
$('dBase').textContent = location.origin + '/v1';

/* 登录状态：控制提示条和 Key 输入框高亮 */
let authOK = null;
function setAuth(ok){
  if (authOK === ok) return;
  authOK = ok;
  $('authBanner').classList.toggle('show', !ok);
  $('keyBox').classList.toggle('ok', ok);
  $('keyBox').classList.toggle('miss', !ok);
  $('keyLbl').textContent = ok ? (LANG === 'vi' ? '✓ Đã kết nối' : '✓ 已登录') : (LANG === 'vi' ? 'Cần API Key' : 'API Key 必填');
}

function saveKey(){
  KEY = $('key').value.trim();
  localStorage.setItem(KEY_STORE, KEY);
  if (!KEY){ setAuth(false); toast('已清除 API Key', 'warn'); return; }
  toast('API Key 已保存到本机浏览器，下次打开自动带上', 'ok');
  authOK = null;                 // 强制重新判定
  applyLang(LANG);
refreshAll();
}

function toast(msg, kind){
  const d = document.createElement('div');
  d.className = 'toast ' + (kind || '');
  d.textContent = msg;
  $('toasts').appendChild(d);
  setTimeout(() => { d.style.opacity = '0'; d.style.transition = '.3s'; }, 3600);
  setTimeout(() => d.remove(), 4000);
}

async function api(path, opts){
  opts = opts || {};
  opts.headers = Object.assign({'Content-Type':'application/json'}, opts.headers || {});
  if (KEY) opts.headers['Authorization'] = 'Bearer ' + KEY;
  const r = await fetch(path, opts);
  const txt = await r.text();
  let data; try { data = JSON.parse(txt); } catch(e){ data = null; }
  if (r.status === 401){
    setAuth(false);
    throw new Error('API Key 未填写或填写错误');
  }
  setAuth(true);
  if (!r.ok) {
    let msg = '';
    if (data) {
      if (typeof data.detail === 'string') msg = data.detail;
      else if (typeof data.message === 'string') msg = data.message;
      else if (data.error) msg = typeof data.error === 'string' ? data.error : (data.error.message || JSON.stringify(data.error));
    }
    if (!msg && txt) {
      if (txt.includes('502 Bad Gateway') || txt.includes('nginx')) {
        msg = '反向代理超时 (Nginx 502 Bad Gateway，通常是 Nginx proxy_read_timeout 默认 60s 太短，请将反代超时调至 600s)';
      } else {
        msg = txt.slice(0, 150);
      }
    }
    throw new Error(msg || ('HTTP ' + r.status));
  }
  return data;
}

function esc(s){
  return String(s == null ? '' : s).replace(/[&<>"']/g, c =>
    ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
}
function fmtBytes(n){
  if (!n && n !== 0) return '—';
  if (n < 1024) return n + ' B';
  if (n < 1048576) return (n/1024).toFixed(1) + ' KB';
  return (n/1048576).toFixed(2) + ' MB';
}
function fmtTime(ts){
  if (!ts) return '—';
  const d = new Date(ts * 1000);
  const p = n => String(n).padStart(2,'0');
  return `${d.getFullYear()}-${p(d.getMonth()+1)}-${p(d.getDate())} ${p(d.getHours())}:${p(d.getMinutes())}:${p(d.getSeconds())}`;
}
function ago(ts){
  if (!ts) return LANG === 'vi' ? 'Chưa dùng' : '从未';
  const s = Math.max(0, Math.floor(Date.now()/1000) - ts);
  if (s < 60) return LANG === 'vi' ? s + ' giây trước' : s + ' 秒前';
  if (s < 3600) return LANG === 'vi' ? Math.floor(s/60) + ' phút trước' : Math.floor(s/60) + ' 分钟前';
  if (s < 86400) return LANG === 'vi' ? Math.floor(s/3600) + ' giờ trước' : Math.floor(s/3600) + ' 小时前';
  return LANG === 'vi' ? Math.floor(s/86400) + ' ngày trước' : Math.floor(s/86400) + ' 天前';
}
function cp(el){
  const t = el.parentElement.innerText.replace(/^复制\n?/, '');
  navigator.clipboard.writeText(t).then(() => toast('已复制', 'ok'));
}

/* ================= 页签 ================= */
function goTab(name){
  const b = document.querySelector(`nav.tabs button[data-t="${name}"]`);
  if (b) b.click();
}
document.querySelectorAll('nav.tabs button').forEach(b => {
  b.onclick = () => {
    document.querySelectorAll('nav.tabs button').forEach(x => x.classList.remove('active'));
    document.querySelectorAll('.tab').forEach(x => x.classList.remove('active'));
    b.classList.add('active');
    $('tab-' + b.dataset.t).classList.add('active');
    if (b.dataset.t === 'tasks') loadTasks();
    if (b.dataset.t === 'media') loadMedia();
    if (b.dataset.t === 'cookie') $('cmdText').textContent = buildCmd($('inBase').value);
  };
});

/* ================= 接入信息 / API Key ================= */
let realKey = '';
let keyShown = false;

async function loadApikey(){
  try{
    const d = await api('/admin/apikey');
    realKey = d.api_key || '';
    $('inBase').value = d.base_url || (location.origin + '/v1');
    renderKey();
    fillExtFields(d.base_url);
    $('cmdText').textContent = buildCmd(d.base_url);
  }catch(e){
    $('inBase').value = location.origin + '/v1';
    fillExtFields(location.origin);
    $('cmdText').textContent = '（先在右上角填入 API Key，这里会生成完整命令）';
  }
}

function maskKey(k){
  if (!k) return '';
  return k.length <= 14 ? k : k.slice(0, 8) + '••••••••••••••' + k.slice(-4);
}
function renderKey(){
  $('inKey').value = keyShown ? realKey : maskKey(realKey);
  $('keyEye').textContent = keyShown ? (LANG === 'vi' ? 'Ẩn' : '隐藏') : (LANG === 'vi' ? 'Hiện' : '显示');
}
function toggleKey(){ keyShown = !keyShown; renderKey(); }

function buildCmd(baseUrl){
  const root = (baseUrl || location.origin).replace(/\/v1\/?$/, '').replace(/\/+$/, '');
  return `python get_muse_cookie.py --base ${root} --key ${realKey || '你的API_KEY'} --label muse-01`;
}

async function copyText(v){
  if (!v) return toast('没有可复制的内容', 'warn');
  try{
    await navigator.clipboard.writeText(v);
    toast('已复制到剪贴板', 'ok');
  }catch(e){
    const ta = document.createElement('textarea');   // 非 https 时的兜底
    ta.value = v; ta.style.position = 'fixed'; ta.style.opacity = '0';
    document.body.appendChild(ta); ta.select();
    try { document.execCommand('copy'); toast('已复制到剪贴板', 'ok'); }
    catch(_){ toast('复制失败，请手动选中复制', 'warn'); }
    ta.remove();
  }
}
async function copyEl(id){ await copyText($(id).value); }
async function copyKey(){ await copyText(realKey); }
async function copyCmd(){ await copyText($('cmdText').textContent); }
async function copyExKey(){ await copyText($('exKey').value); }

/* 扩展方案：把 BASE URL / API Key 填进页面上的复制框 */
function fillExtFields(baseUrl){
  const root = (baseUrl || location.origin)
    .replace(/\/v1\/?$/i, '').replace(/\/+$/, '');
  if ($('exBase')) $('exBase').value = root;
  if ($('exKey')) $('exKey').value = realKey || '';
}
async function loadExtFiles(){
  const el = $('extFiles');
  if (!el) return;
  el.textContent = '读取中…';
  try{
    const d = await api('/admin/extension/files');
    const files = d.files || [];
    el.innerHTML = files.length
      ? `包含 ${files.length} 个文件：` + files.map(f => `<code>${esc(f)}</code>`).join('、')
      : '（扩展目录为空，请检查部署）';
  }catch(e){
    el.textContent = '读取失败：' + e.message;
  }
}

async function rotateKey(){
  if (!confirm('重新生成 API Key？\n\n旧 Key 会立即失效，已经接入的下游项目必须同步更新，否则会报 401。')) return;
  try{
    const d = await api('/admin/apikey/rotate', {method:'POST'});
    realKey = d.api_key;
    KEY = d.api_key;
    localStorage.setItem(KEY_STORE, KEY);
    $('key').value = KEY;
    keyShown = true; renderKey();
    $('cmdText').textContent = buildCmd($('inBase').value);
    toast('已生成新 Key 并立即生效，本页已自动更新', 'ok');
  }catch(e){ toast('生成失败：' + e.message, 'bad'); }
}

/* ================= 额度显示 ================= */
function quotaBadge(a){
  const q = a.quota;
  if (!q || !q.found){
    return '<span class="badge mute" title="还没查过。点「操作」里的「额度」实时查询">未查</span>';
  }
  const pct = (q.weekly_used_pct != null) ? q.weekly_used_pct : null;
  const cls = pct == null ? 'info' : pct < 50 ? 'ok' : pct < 80 ? 'warn' : 'bad';
  const plan = (q.plan || '').replace(/\s*plan\s*$/i, '') || '—';
  let title = `计划：${q.plan || '?'}`;
  if (q.weekly_reset) title += `\n周限额重置：${q.weekly_reset}`;
  if (pct != null) title += `\n周用量：已用 ${pct}%`;
  if (q.extra_left) title += `\n额外代币：剩 ${q.extra_left}（已用 ${q.extra_used_pct ?? '?'}%）`;
  if (q.checked_at) title += `\n查询时间：${fmtTime(q.checked_at)}`;
  const main = pct != null ? `${plan} · 已用 ${pct}%` : plan;
  const sub = q.extra_left ? `<div class="mono" style="font-size:11px;color:var(--muted);margin-top:2px">+${esc(q.extra_left)}</div>` : '';
  return `<span class="badge ${cls}" title="${esc(title)}">${esc(main)}</span>${sub}`;
}

async function queryQuota(aid, btn){
  if (btn){ btn.disabled = true; btn.textContent = '查询中…'; }
  try{
    const q = await api(`/admin/accounts/${aid}/quota`, {method:'POST'});
    if (q.found){
      const extra = q.extra_left ? `，额外剩 ${q.extra_left}` : '';
      toast(`额度：${q.plan || '?'}，周用量已用 ${q.weekly_used_pct ?? '?'}%${extra}`, 'ok');
    }else{
      toast('设置面板里没有读到额度数据（可能是页面结构变了）', 'warn');
    }
    loadPool();
  }catch(e){
    toast('额度查询失败：' + e.message, 'bad');
    if (btn){ btn.disabled = false; btn.textContent = '额度'; }
  }
}

/* ================= 有效期显示 ================= */
function expiryBadge(a){
  const ts = a && a.expires_at;
  if (!ts) return '<span class="badge mute" title="未记录有效期">未知</span>';
  const est = a.expires_estimated
    ? '（按 hatch_vml 约 2 天寿命推算，未取到精确 expires）'
    : '（hatch_vml 实测到期时间）';
  const left = ts - Math.floor(Date.now() / 1000);
  if (left <= 0) return `<span class="badge bad" title="Hết hạn lúc: ${fmtTime(ts)}">${t('exp_expired')}</span>`;
  const days = left / 86400;
  const numD = days >= 10 ? Math.round(days) : days.toFixed(1);
  const numH = Math.max(1, Math.floor(left / 3600));
  const txt = days >= 1
    ? (LANG === 'vi' ? `Còn ${numD} ngày` : `剩 ${numD} 天`)
    : (LANG === 'vi' ? `Còn ${numH} giờ` : `剩 ${numH} 小时`);
  const cls = days < 1 ? 'bad' : days < 3 ? 'warn' : 'ok';
  return `<span class="badge ${cls}" title="Hết hạn: ${fmtTime(ts)}">${txt}</span>`;
}

/* ================= 账号池 ================= */
let accounts = [];

async function loadPool(){
  try{
    const d = await api('/admin/accounts');
    accounts = d.accounts || [];
    const st = d.stats || {};
    $('sTotal').textContent = st.total ?? accounts.length;
    $('sOk').textContent    = st.healthy ?? 0;
    $('sBad').textContent   = st.error ?? 0;
    $('sDis').textContent   = st.disabled ?? 0;
    $('poolCount').textContent = accounts.length;
    $('pAcc').className = 'pill ' + (accounts.length ? 'on' : 'off');
    $('pAcc').innerHTML = `<span class="led"></span>${t('lbl_acc')} <b>${accounts.length}</b>`;

    // 快过期 / 已过期提醒。hatch_vml 只有约 2 天寿命，且不会因为使用而延长，
    // 所以这里是刚需提醒，不是锦上添花。
    const now = Math.floor(Date.now() / 1000);
    const soon = accounts.filter(a => a.enabled && a.expires_at &&
                                      a.expires_at - now < 12 * 3600);
    const bar = $('expWarn');
    if (soon.length){
      const dead = soon.filter(a => a.expires_at <= now).length;
      const names = soon.slice(0, 4).map(a => esc(a.label)).join('、') +
                    (soon.length > 4 ? ` 等 ${soon.length} 个` : '');
      $('expWarnText').innerHTML = dead
        ? `⚠️ <b>${dead} 个账号已过期</b>，${soon.length - dead ? `另有 ${soon.length - dead} 个即将过期（${names}）` : names}。` +
          `过期的账号无法生成，请重新登录一次（约 30 秒）。`
        : `⏳ <b>${names}</b> 的有效期不足 12 小时。muse.ai 的会话约 2 天到期且不会因使用而延长，` +
          `建议现在重新登录一次，避免生成时突然失败。`;
      bar.style.display = '';
    }else{
      bar.style.display = 'none';
    }

    if (!accounts.length){
      $('poolBody').innerHTML = `<tr><td colspan="10" class="empty">${t('empty_pool')}</td></tr>`;
      return;
    }
    $('poolBody').innerHTML = accounts.map(a => {
      const ok = a.ok;
      const badge = !a.enabled ? `<span class="badge mute">${t('badge_disabled')}</span>`
                  : ok === true  ? `<span class="badge ok">${t('badge_ok')}</span>`
                  : ok === false ? `<span class="badge bad">${t('badge_bad')}</span>`
                  : `<span class="badge warn">${t('badge_unchecked')}</span>`;
      const miss = a.essential_ok ? '' : ` <span class="badge bad" title="Thiếu cookie cốt lõi">${t('badge_miss_core')}</span>`;
      return `<tr>
        <td><b>${esc(a.label)}</b></td>
        <td class="mono">${esc(a.id)}</td>
        <td>${badge}${miss}</td>
        <td>${expiryBadge(a)}</td>
        <td>${quotaBadge(a)}</td>
        <td>${a.enabled ? `<span class="badge ok">${t('badge_on')}</span>` : `<span class="badge mute">${t('badge_off')}</span>`}</td>
        <td class="mono">${a.cookie_count}</td>
        <td class="mono" title="${a.last_used ? fmtTime(a.last_used) : ''}">${ago(a.last_used)}</td>
        <td class="mono ellip" title="${esc(a.note||'')}">${esc(a.note || '—')}</td>
        <td><div class="acts">
          <button class="ghost mini" onclick="testAcc('${a.id}')">${t('act_test')}</button>
          <button class="ghost mini" onclick="keepaliveOne('${a.id}')" title="Bảo trì phiên ngầm">${t('act_ka')}</button>
          <button class="ghost mini" onclick="queryQuota('${a.id}', this)">${t('act_quota')}</button>
          <button class="ghost mini" onclick="toggleAcc('${a.id}', ${!a.enabled})">${a.enabled ? t('act_disable') : t('act_enable')}</button>
          <button class="ghost mini" onclick="renameAcc('${a.id}','${esc(a.label)}')">${t('act_rename')}</button>
          <button class="ghost mini" onclick="updateCookies('${a.id}')">${t('act_update_ck')}</button>
          <button class="danger mini" onclick="delAcc('${a.id}','${esc(a.label)}')">${t('act_delete')}</button>
        </div></td>
      </tr>`;
    }).join('');
  }catch(e){
    $('poolBody').innerHTML = authOK === false
      ? '<tr><td colspan="10" class="empty">🔑 请先在右上角填入 API Key 并点「保存」</td></tr>'
      : `<tr><td colspan="10" class="empty">加载失败：${esc(e.message)}</td></tr>`;
  }
}

async function addAccount(fromManual){
  const labelEl = $(fromManual ? 'mLabel' : 'newLabel');
  const ckEl    = $(fromManual ? 'mCookie' : 'newCookie');
  const label = labelEl.value.trim();
  const raw = ckEl.value.trim();
  if (!raw) return toast('请先粘贴 Cookie', 'warn');
  const lines = raw.split('\n').map(s => s.trim()).filter(Boolean);
  const body = (lines.length > 1) ? {batch: raw} : {label: label, cookie_header: raw};
  try{
    const r = await api('/admin/accounts', {method:'POST', body: JSON.stringify(body)});
    if (r.warning) toast(r.warning, 'warn');
    else toast(`成功导入 ${r.count} 个账号`, 'ok');
    ckEl.value = ''; labelEl.value = '';
    loadPool();
  }catch(e){ toast('导入失败：' + e.message, 'bad'); }
}

async function testAcc(id){
  toast('正在真实打开 muse.ai 校验会话…');
  try{
    const r = await api(`/admin/accounts/${id}/test`, {method:'POST'});
    toast((r.ok ? '✓ ' : '✗ ') + r.message, r.ok ? 'ok' : 'bad');
    loadPool();
  }catch(e){ toast('测试失败：' + e.message, 'bad'); }
}

async function keepaliveOne(id){
  toast('正在为该账号执行会话静默续期…');
  try{
    const r = await api(`/admin/accounts/${id}/keepalive`, {method:'POST'});
    toast(r.ok ? `✓ 账号保活成功，新到期时间已更新` : `✗ 保活失败: ${r.error||'未知错误'}`, r.ok ? 'ok' : 'bad');
    loadPool();
  }catch(e){ toast('保活失败：' + e.message, 'bad'); }
}

async function keepaliveAll(){
  const btn = $('btnKeepaliveAll');
  if (btn) { btn.disabled = true; btn.innerText = '保活执行中…'; }
  toast('正在唤醒无头浏览器，为账号池执行静默续期与保活…', 'warn');
  try{
    const r = await api('/admin/accounts/keepalive?force=true', {method:'POST'});
    if (r.status === 'busy') {
      toast('保活任务正在后台运行中，请稍候查看', 'warn');
    } else {
      toast(`✓ 成功保活 ${r.refreshed_count || 0} 个账号，跳过 ${r.skipped_count || 0} 个`, 'ok');
    }
    loadPool();
  }catch(e){ toast('保活执行失败：' + e.message, 'bad'); }
  finally{
    if (btn) { btn.disabled = false; btn.innerText = '⚡ 一键保活所有账号'; }
  }
}

async function toggleAcc(id, enabled){
  try{
    await api(`/admin/accounts/${id}`, {method:'PATCH', body: JSON.stringify({enabled})});
    toast(enabled ? '已启用' : '已禁用', 'ok'); loadPool();
  }catch(e){ toast('操作失败：' + e.message, 'bad'); }
}

async function renameAcc(id, old){
  const label = prompt('新的账号标签：', old);
  if (label === null || !label.trim()) return;
  try{
    await api(`/admin/accounts/${id}`, {method:'PATCH', body: JSON.stringify({label: label.trim()})});
    toast('标签已更新', 'ok'); loadPool();
  }catch(e){ toast('改名失败：' + e.message, 'bad'); }
}

async function updateCookies(id){
  const v = prompt('粘贴该账号最新的 Cookie 字符串：');
  if (!v || !v.trim()) return;
  try{
    const r = await api(`/admin/accounts/${id}/cookies`, {method:'POST', body: JSON.stringify({cookie_header: v.trim()})});
    toast(`Cookie 已更新（${r.cookie_count} 条）`, 'ok'); loadPool();
  }catch(e){ toast('更新失败：' + e.message, 'bad'); }
}

async function delAcc(id, label){
  if (!confirm(`确定删除账号「${label}」？此操作不可撤销。`)) return;
  try{
    await api(`/admin/accounts/${id}`, {method:'DELETE'});
    toast('已删除', 'ok'); loadPool();
  }catch(e){ toast('删除失败：' + e.message, 'bad'); }
}

/* ================= 任务记录 ================= */
async function loadTasks(){
  try{
    const d = await api('/admin/tasks?limit=60');
    const ts = d.tasks || [];
    $('taskCount').textContent = ts.length;
    if (!ts.length){ $('taskBody').innerHTML = '<tr><td colspan="8" class="empty">暂无任务记录</td></tr>'; return; }
    $('taskBody').innerHTML = ts.map(t => {
      const cls = (t.status === 'succeeded' || t.status === 'completed') ? 'ok' : t.status === 'failed' ? 'bad'
                : t.status === 'processing' ? 'info' : 'warn';
      let out = '—';
      if (t.result && t.result.url) out = `<a href="${esc(t.result.url)}" target="_blank">查看结果</a> <span class="mono">${fmtBytes(t.result.bytes)}</span>`;
      else if (t.error) out = `<span style="color:var(--bad)">${esc(t.error).slice(0,120)}</span>`;
      return `<tr>
        <td class="mono">${esc(t.id)}</td>
        <td>${t.kind === 'video' ? '<span class="badge info">视频</span>' : '<span class="badge info">图片</span>'}</td>
        <td><span class="ellip" title="${esc(t.prompt)}">${esc(t.prompt)}</span></td>
        <td><span class="badge ${cls}">${esc(t.status)}</span></td>
        <td class="mono">${t.elapsed ? t.elapsed + 's' : '—'}</td>
        <td class="mono">${fmtTime(t.created_at)}</td>
        <td>${out}</td>
        <td><button class="danger mini" onclick="delTask('${t.id}')">删</button></td>
      </tr>`;
    }).join('');
  }catch(e){
    $('taskBody').innerHTML = `<tr><td colspan="8" class="empty">加载失败：${esc(e.message)}</td></tr>`;
  }
}
async function delTask(id){
  try{ await api('/admin/tasks/' + id, {method:'DELETE'}); loadTasks(); }
  catch(e){ toast('删除失败：' + e.message, 'bad'); }
}
async function clearTasks(){
  if (!confirm('确定清空全部任务记录？（已生成的媒体文件不会被删除）')) return;
  try{
    const r = await api('/admin/tasks/clear', {method:'POST', body: JSON.stringify({keep: 0})});
    toast(`已清空 ${r.removed} 条记录`, 'ok'); loadTasks();
  }catch(e){ toast('清空失败：' + e.message, 'bad'); }
}

/* ================= 媒体库 ================= */
async function loadMedia(){
  try{
    const d = await api('/admin/media');
    const ms = d.media || [];
    $('mediaCount').textContent = ms.length;
    $('sMedia').textContent = ms.length;
    if (!ms.length){ $('mediaGrid').innerHTML = '<div class="empty">还没有生成任何媒体文件</div>'; return; }
    $('mediaGrid').innerHTML = ms.map(m => `
      <div class="tile">
        <div class="thumb">${m.kind === 'video'
          ? `<video src="${esc(m.url)}" muted playsinline preload="metadata"></video>`
          : `<img src="${esc(m.url)}" loading="lazy" alt="">`}</div>
        <div class="meta">
          <div class="nm" title="${esc(m.name)}">${esc(m.name)}</div>
          <div style="margin-top:3px">${fmtBytes(m.bytes)} · ${fmtTime(m.mtime)}</div>
          <div class="ac">
            <a class="badge info" href="${esc(m.url)}" target="_blank">打开</a>
            <a class="badge mute" href="${esc(m.url)}" download>下载</a>
          </div>
        </div>
      </div>`).join('');
  }catch(e){ $('mediaGrid').innerHTML = `<div class="empty">加载失败：${esc(e.message)}</div>`; }
}

/* ================= 在线测试 ================= */
async function runImage(){
  const btn = $('imgBtn'), box = $('imgRes');
  const prompt = $('imgPrompt').value.trim();
  if (!prompt) return toast('请输入提示词', 'warn');
  btn.disabled = true; btn.innerHTML = '<span class="spin"></span>生成中…';
  box.className = 'result show';
  box.innerHTML = '<span class="spin"></span>正在提交图片任务，生成期间会持续查询状态…';
  const t0 = Date.now();
  try{
    let r = await api('/v1/images/tasks', {method:'POST',
      body: JSON.stringify({prompt, size: $('imgSize').value, timeout:600})});
    const taskId = r.id;
    const deadline = Date.now() + 15 * 60 * 1000;
    let failures = 0;
    while (r.status !== 'completed') {
      if (Date.now() >= deadline) throw new Error('等待超过 15 分钟，请在任务记录查看结果，勿重复提交');
      if (r.status === 'failed') throw new Error(r.error || '图片生成失败');
      box.textContent = `任务 ${taskId} · ${r.status} · 已等待 ${Math.floor((Date.now()-t0)/1000)} 秒`;
      await new Promise(resolve => setTimeout(resolve, 3000));
      try {
        r = await api('/v1/images/tasks/' + encodeURIComponent(taskId));
        failures = 0;
      } catch (e) {
        if (++failures >= 6) throw new Error('状态查询暂时失败，请在任务记录查看，勿重复提交');
      }
    }
    const it = r.data[0];
    box.innerHTML = `<b style="color:var(--ok)">✓ 生成成功</b>
      <span class="mono" style="color:var(--muted);margin-left:10px">${((Date.now()-t0)/1000).toFixed(1)}s · ${fmtBytes(it.bytes)}</span>
      <img src="${esc(it.url)}" alt="">
      <pre class="out">${esc(JSON.stringify(r, null, 2))}</pre>`;
    loadMedia();
  }catch(e){
    box.innerHTML = `<b style="color:var(--bad)">✗ 生成失败</b><pre class="out">${esc(e.message)}</pre>`;
  }finally{ btn.disabled = false; btn.textContent = '开始生成图片'; }
}

async function runVideo(){
  const btn = $('vidBtn'), box = $('vidRes');
  const prompt = $('vidPrompt').value.trim();
  if (!prompt) return toast('请输入提示词', 'warn');
  btn.disabled = true; btn.innerHTML = '<span class="spin"></span>生成中…';
  box.className = 'result show';
  box.innerHTML = '<span class="spin"></span>正在创建视频任务…';
  const t0 = Date.now();
  try{
    const t = await api('/v1/videos', {method:'POST', body: JSON.stringify({
      prompt, duration: parseInt($('vidDur').value) || 5, size: $('vidSize').value})});
    const tick = async () => {
      const s = await api('/v1/videos/' + t.id);
      const el = ((Date.now()-t0)/1000).toFixed(0);
      if (s.status === 'succeeded' || s.status === 'completed'){
        const vurl = (s.result && s.result.url) || s.url || '';
        const vbytes = (s.result && s.result.bytes) || 0;
        box.innerHTML = `<b style="color:var(--ok)">✓ 生成成功</b>
          <span class="mono" style="color:var(--muted);margin-left:10px">${el}s · ${fmtBytes(vbytes)}</span>
          <video src="${esc(vurl)}" controls playsinline></video>
          <pre class="out">${esc(JSON.stringify(s, null, 2))}</pre>`;
        btn.disabled = false; btn.textContent = '开始生成视频';
        loadMedia(); loadTasks();
      }else if (s.status === 'failed'){
        box.innerHTML = `<b style="color:var(--bad)">✗ 生成失败</b><pre class="out">${esc(s.error||'')}</pre>`;
        btn.disabled = false; btn.textContent = '开始生成视频';
      }else{
        box.innerHTML = `<span class="spin"></span>任务 ${esc(s.status)} · 已等待 ${el}s（视频通常 60–120 秒）…`;
        setTimeout(tick, 4000);
      }
    };
    tick();
  }catch(e){
    box.innerHTML = `<b style="color:var(--bad)">✗ 创建任务失败</b><pre class="out">${esc(e.message)}</pre>`;
    btn.disabled = false; btn.textContent = '开始生成视频';
  }
}

/* ================= 官方仓库实时更新检测、弹窗通知与一键升级 ================= */
let _notifiedSha = localStorage.getItem('muse2api_notified_sha') || '';
let _dismissedSha = localStorage.getItem('muse2api_dismissed_sha') || '';
let _lastRepoStatus = null;

function toggleRepoPanel(){
  const el = $('repoPanel');
  if (!el) return;
  const show = el.style.display === 'none';
  el.style.display = show ? 'block' : 'none';
  if (show) loadRepoStatus(false);
}

function dismissUpdateBanner(){
  if (_lastRepoStatus && _lastRepoStatus.remote_sha){
    _dismissedSha = _lastRepoStatus.remote_sha;
    localStorage.setItem('muse2api_dismissed_sha', _dismissedSha);
  }
  $('updateBanner').classList.remove('show');
}

async function loadRepoStatus(force){
  try{
    let s = await api('/admin/update/check' + (force ? '?force=true' : ''));
    // 若服务端网络无法直连 GitHub API，则由用户浏览器端直接请求 GitHub API 兜底检测
    if (!s.remote_sha){
      try{
        const gr = await fetch('https://api.github.com/repos/czg86389-hub/muse2api/commits?sha=main&per_page=5');
        if (gr.ok){
          const commits = await gr.json();
          if (Array.isArray(commits) && commits.length){
            s.remote_sha = (commits[0].sha || '').slice(0, 7);
            s.remote_msg = ((commits[0].commit || {}).message || '').split('\n')[0];
            s.recent_commits = commits.map(c => ({
              sha: (c.sha || '').slice(0, 7),
              message: ((c.commit || {}).message || '').split('\n')[0],
              date: ((c.commit || {}).committer || {}).date || '',
              url: c.html_url || 'https://github.com/czg86389-hub/muse2api'
            }));
            if (s.local_sha && s.remote_sha && s.local_sha !== s.remote_sha){
              s.has_update = true;
              s.up_to_date = false;
            }
          }
        }
      }catch(_){}
    }
    _lastRepoStatus = s;
    const badge = $('repoBadge');
    const topBtn = $('btnRepoTop');
    const topTxt = $('repoTopTxt');
    const desc = $('repoStatusDesc');
    const box = $('repoCommitsBox');
    const banner = $('updateBanner');
    const lVer = 'v' + (s.local_version || '1.5.0');
    const rVer = 'v' + (s.remote_version || s.local_version || '1.5.0');

    if (s.has_update){
      badge.className = 'badge warn';
      badge.textContent = `🔔 发现新版本 ${rVer} (${s.remote_sha || 'latest'})`;
      topBtn.classList.add('updpill-alert');
      topBtn.innerHTML = `🔔 <span id="repoTopTxt">发现新更新 (${esc(s.remote_sha || rVer)})</span>`;
      $('updBannerVer').textContent = `${lVer} (${s.local_sha || '旧版'}) → ${rVer} (${s.remote_sha || '最新'})`;
      $('updBannerMsg').innerHTML = `最新仓库提交：<b>${esc(s.remote_msg || '性能优化与功能更新')}</b> · 点击右侧「⚡ 一键在线升级并重启」即可自动拉取更新（保留本地配置与账号数据）。`;
      if (_dismissedSha !== s.remote_sha){
        banner.classList.add('show');
      }
      if (_notifiedSha !== s.remote_sha && s.remote_sha){
        _notifiedSha = s.remote_sha;
        localStorage.setItem('muse2api_notified_sha', _notifiedSha);
        toast(`🔔 官方仓库发布了新更新 (${s.remote_sha})：${s.remote_msg || '点击顶部一键升级'}`, 'warn');
      }
    } else {
      badge.className = 'badge ok';
      badge.textContent = `✓ 已是最新 ${lVer} (${s.local_sha || 'main'})`;
      topBtn.classList.remove('updpill-alert');
      topBtn.innerHTML = `📦 <span id="repoTopTxt">${esc(lVer)} · 已是最新</span>`;
      banner.classList.remove('show');
    }

    desc.innerHTML = `当前已部署版本：<code>${esc(lVer)}</code>（Commit: <code>${esc(s.local_sha || '—')}</code>） · ` +
      `GitHub 官方仓库最新：<code>${esc(rVer)}</code>（Commit: <code>${esc(s.remote_sha || '—')}</code> ${esc(s.remote_msg || '')}）`;

    let html = '';
    if (Array.isArray(s.highlights) && s.highlights.length){
      html += `<div style="margin-bottom:8px"><b style="color:var(--text)">✨ 当前版本核心特性 (${esc(rVer)})：</b><ul style="margin:4px 0 0 18px;padding:0;color:var(--muted)">` +
        s.highlights.map(h => `<li>${esc(h)}</li>`).join('') + `</ul></div>`;
    }
    if (Array.isArray(s.recent_commits) && s.recent_commits.length){
      html += `<div><b style="color:var(--text)">📜 官方仓库最近提交动态：</b><div style="margin-top:5px;display:flex;flex-direction:column;gap:4px">` +
        s.recent_commits.slice(0, 5).map(c =>
          `<div style="display:flex;gap:8px;align-items:center"><a href="${esc(c.url)}" target="_blank" class="mono" style="color:var(--accent)">[${esc(c.sha)}]</a><span>${esc(c.message)}</span><span class="mono" style="margin-left:auto">${esc((c.date||'').replace('T',' ').replace('Z',''))}</span></div>`
        ).join('') + `</div></div>`;
    }
    if (box) box.innerHTML = html || '<span style="color:var(--muted)">暂无提交记录</span>';
    if (force) toast(s.has_update ? '🔔 检测到新版本更新！' : '✓ 当前已是官方仓库最新版本', s.has_update ? 'warn' : 'ok');
  }catch(e){
    if ($('repoBadge')) { $('repoBadge').className = 'badge mute'; $('repoBadge').textContent = '待鉴权'; }
  }
}

async function upgradeNow(){
  if (!confirm('确定立即从 GitHub 官方仓库 (czg86389-hub/muse2api) 拉取最新代码并自动重启服务吗？\n\n（注：本地 .env 密钥、账号池 Cookie 和已生成的媒体文件均会自动保留，不受任何影响）')) return;
  const btn1 = $('btnRepoPull'), btn2 = $('btnBannerUpgrade');
  if (btn1) { btn1.disabled = true; btn1.innerHTML = '<span class="spin"></span>正在在线更新…'; }
  if (btn2) { btn2.disabled = true; btn2.innerHTML = '<span class="spin"></span>正在在线更新…'; }
  try{
    const r = await api('/admin/update/upgrade', {method: 'POST', body: JSON.stringify({restart: true})});
    toast('✓ ' + (r.message || '更新完成') + '，服务正在重启，就绪后将自动刷新页面…', 'ok');
    $('updateBanner').classList.remove('show');
    let tries = 0;
    const waitReady = async () => {
      tries++;
      try{
        const hr = await fetch('/healthz?t=' + Date.now(), {cache: 'no-store'});
        if (hr.ok) { location.reload(); return; }
      }catch(_){}
      if (tries < 20) setTimeout(waitReady, 1000);
      else location.reload();
    };
    setTimeout(waitReady, 2500);
  }catch(e){
    toast('在线更新失败：' + e.message, 'bad');
    if (btn1) { btn1.disabled = false; btn1.textContent = '⚡ 一键从 GitHub 在线更新并重启'; }
    if (btn2) { btn2.disabled = false; btn2.textContent = '⚡ 一键在线升级并重启'; }
  }
}

/* ================= 总览刷新 ================= */
async function loadStatus(){
  try{
    const d = await api('/admin/status');
    $('pSvc').className = 'pill on';
    $('pSvc').innerHTML = '<span class="led"></span>' + t('lbl_svc') + ' <b>' + (LANG === 'vi' ? 'Hoạt động' : '正常') + '</b>';
    $('pBr').className = 'pill ' + (d.browser_running ? 'on' : 'off');
    $('pBr').innerHTML = `<span class="led"></span>${t('lbl_br')} <b>${d.browser_running ? (LANG === 'vi' ? 'Đang chạy' : '运行中') : (LANG === 'vi' ? 'Nghỉ' : '空闲')}</b>`;
    $('sMedia').textContent = d.media_count ?? 0;
    if (d.base_url){ $('dBase').textContent = d.base_url; $('inBase').value = d.base_url; }
  }catch(e){
    if (authOK === false){
      $('pSvc').className = 'pill';
      $('pSvc').innerHTML = '<span class="led"></span>' + t('lbl_svc') + ' <b>' + (LANG === 'vi' ? 'Chờ đăng nhập' : '待登录') + '</b>';
    } else {
      $('pSvc').className = 'pill off';
      $('pSvc').innerHTML = '<span class="led"></span>' + t('lbl_svc') + ' <b>' + esc(e.message).slice(0,28) + '</b>';
    }
  }
}

function refreshAll(){ loadStatus(); loadPool(); loadApikey(); loadRepoStatus(false); }

applyLang(LANG);
refreshAll();
setInterval(() => {
  loadStatus(); loadPool();
  if ($('tab-tasks').classList.contains('active')) loadTasks();
}, 8000);
setInterval(() => {
  loadRepoStatus(false);
}, 60000);
</script>
</body>
</html>
