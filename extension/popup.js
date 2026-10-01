
/* ================= i18n cho Extension ================= */
let EXT_LANG = localStorage.getItem('muse_ext_lang') || 'vi';

const EXT_I18N = {
  vi: {
    btn_lang: "🌐 Tiếng Việt",
    title: "Muse2API Nhập Cookie",
    sub: "Đồng bộ phiên đăng nhập muse.ai từ trình duyệt này sang máy chủ muse2api chỉ với 1 cú click.",
    lbl_base: "Địa chỉ máy chủ (BASE URL)",
    lbl_key: "Khóa API (API Key)",
    lbl_label: "Nhãn tài khoản (Tùy chọn)",
    btn_go: "Đọc và Nhập Cookie",
    steps: "<b>Trước khi bấm hãy xác nhận:</b><br>1. Bạn đã đăng nhập sẵn vào <a href=\"https://muse.ai/\" target=\"_blank\" style=\"color:#4f8cff\">muse.ai</a> trên <b>trình duyệt này</b> (thấy màn hình chat).<br>2. Địa chỉ máy chủ và API Key đã được điền đúng (sao chép ở đầu trang Admin).",
    foot: "Tiện ích chỉ đọc Cookie của muse.ai (bao gồm các khóa httpOnly) qua API <code>chrome.cookies</code> và gửi trực tiếp về máy chủ nội bộ của bạn. Không gửi về bất kỳ máy chủ bên thứ ba nào.",
    err_no_base: "Vui lòng điền địa chỉ máy chủ (BASE URL)",
    err_no_key: "Vui lòng điền API Key",
    msg_reading: "Đang đọc Cookie từ muse.ai…",
    msg_no_cookies: "Không tìm thấy Cookie muse.ai nào.\nHãy mở tab https://muse.ai/ trên trình duyệt này và đăng nhập trước, sau đó bấm lại.",
    msg_missing_core: "Đã đọc được {n} cookie nhưng thiếu các cookie cốt lõi: {missing}\nCó thể bạn chưa đăng nhập hoàn tất trên muse.ai.",
    msg_uploading: "Đã lấy {n} cookie, đang gửi tới {base}…",
    msg_success: "✓ Nhập thành công! Nhãn: {label} (ID: {id})\nHồ tài khoản hiện đã sẵn sàng sử dụng!",
    msg_fail: "Nhập thất bại (HTTP {status}): {err}"
  },
  zh: {
    btn_lang: "🌐 中文",
    title: "Muse2API Cookie 导入",
    sub: "把当前浏览器里 muse.ai 的登录态，一键同步到你的 muse2api 服务。",
    lbl_base: "服务地址（BASE URL）",
    lbl_key: "API Key",
    lbl_label: "账号标签（可留空）",
    btn_go: "读取并导入",
    steps: "<b>用之前先确认两件事：</b><br>1. 你已经在<b>这个浏览器</b>里登录了 <a href=\"https://muse.ai/\" target=\"_blank\" style=\"color:#4f8cff\">muse.ai</a>（能看到聊天界面）。<br>2. 上面的服务地址和 API Key 已填好（在 muse2api 管理页「账号池」页顶部可以复制）。",
    foot: "本扩展只做一件事：用浏览器的 <code>chrome.cookies</code> 接口读取 muse.ai 的 Cookie（能读到 httpOnly 的那些），POST 到你填的服务地址。不收集、不上传到任何第三方服务器。",
    err_no_base: "请先填服务地址",
    err_no_key: "请先填 API Key",
    msg_reading: "正在读取 muse.ai 的 Cookie…",
    msg_no_cookies: "没读到 muse.ai 的 Cookie。请先在这个浏览器里打开并登录 https://muse.ai/ ，再回来点一次。",
    msg_missing_core: "读到 {n} 条 Cookie，但缺核心项：{missing}\n说明这个浏览器还没登录成功。请登录到能看到聊天界面再试。",
    msg_uploading: "读到 {n} 条 Cookie，正在上传到 {base} …",
    msg_success: "✓ 导入成功！账号标签：{label}（ID: {id}）",
    msg_fail: "导入失败（HTTP {status}）：{err}"
  }
};

function applyExtLang(l) {
  EXT_LANG = l || localStorage.getItem('muse_ext_lang') || 'vi';
  localStorage.setItem('muse_ext_lang', EXT_LANG);
  const d = EXT_I18N[EXT_LANG] || EXT_I18N['vi'];
  if ($('langBtn')) $('langBtn').textContent = d.btn_lang;
  if ($('t_title')) $('t_title').textContent = d.title;
  if ($('t_sub')) $('t_sub').textContent = d.sub;
  if ($('t_lbl_base')) $('t_lbl_base').textContent = d.lbl_base;
  if ($('t_lbl_key')) $('t_lbl_key').textContent = d.lbl_key;
  if ($('t_lbl_label')) $('t_lbl_label').textContent = d.lbl_label;
  if ($('go')) $('go').textContent = d.btn_go;
  if ($('t_steps')) $('t_steps').innerHTML = d.steps;
  if ($('t_foot')) $('t_foot').innerHTML = d.foot;
}

function toggleLang() {
  const next = EXT_LANG === 'vi' ? 'zh' : 'vi';
  applyExtLang(next);
}

/* Muse2API Cookie 导入 —— 读取 muse.ai 的 cookie 并 POST 到 muse2api 服务。
 *
 * 关键点：用 chrome.cookies 而不是 document.cookie。
 * muse.ai 的 4 条核心 cookie（hatch_sess / hatch_gw / hatch_vml /
 * hatch_native_auth_device）都带 httpOnly，网页 JS 读不到，
 * 只有浏览器扩展的 cookies 接口能拿到。
 */

const $ = (id) => document.getElementById(id);
const STORE = 'muse2api_ext_cfg';

const ESSENTIAL = ['hatch_sess', 'hatch_gw', 'hatch_vml', 'hatch_native_auth_device'];

function log(html, cls) {
  const el = $('log');
  el.className = 'show';
  el.innerHTML = cls ? `<span class="${cls}">${html}</span>` : html;
}

/* 规范化服务地址：去掉结尾斜杠和 /v1 后缀 */
function normBase(v) {
  let s = (v || '').trim();
  if (!s) return '';
  if (!/^https?:\/\//i.test(s)) s = 'https://' + s;
  s = s.replace(/\/+$/, '');
  s = s.replace(/\/v1$/i, '');
  return s;
}

async function loadCfg() {
  const o = await chrome.storage.local.get(STORE);
  const c = o[STORE] || {};
  if (c.base) $('base').value = c.base;
  if (c.key) $('key').value = c.key;
  if (c.label) $('label').value = c.label;
  // 没有配置过就尝试从当前标签页猜一个（用户在管理页上时）
  if (!c.base) {
    try {
      const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
      const u = tab && tab.url ? new URL(tab.url) : null;
      if (u && /\/admin/.test(u.pathname)) {
        $('base').value = u.origin;
        const k = new URLSearchParams(u.search).get('key');
        if (k) $('key').value = k;
      }
    } catch (e) { /* 忽略 */ }
  }
}

async function saveCfg() {
  await chrome.storage.local.set({
    [STORE]: {
      base: normBase($('base').value),
      key: $('key').value.trim(),
      label: $('label').value.trim(),
    },
  });
}

async function grabCookies() {
  const all = await chrome.cookies.getAll({ domain: 'muse.ai' });
  const out = {}, exp = {};
  for (const c of all) {
    const dom = (c.domain || '').replace(/^\./, '');
    if (!dom.endsWith('muse.ai')) continue;
    out[c.name] = c.value;
    if (c.expirationDate) exp[c.name] = Math.floor(c.expirationDate);
  }
  return { cookies: out, expires: exp };
}

async function run() {
  const base = normBase($('base').value);
  const key = $('key').value.trim();
  const label = $('label').value.trim();

  const dict = EXT_I18N[EXT_LANG] || EXT_I18N['vi'];
  if (!base) return log(dict.err_no_base, 'bad');
  if (!key) return log(dict.err_no_key, 'bad');

  $('go').disabled = true;
  log(dict.msg_reading);

  try {
    const { cookies, expires } = await grabCookies();
    const names = Object.keys(cookies);
    if (!names.length) {
      return log(dict.msg_no_cookies, 'bad');
    }
    const missing = ESSENTIAL.filter((n) => !(n in cookies));
    if (missing.length) {
      log(dict.msg_missing_core.replace('{n}', names.length).replace('{missing}', missing.join(', ')), 'warn');
      return;
    }

    log(dict.msg_uploading.replace('{n}', names.length).replace('{base}', base));

    const r = await fetch(base + '/admin/accounts', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + key,
      },
      body: JSON.stringify({ label, cookies, expires }),
    });

    const text = await r.text();
    let data;
    try { data = JSON.parse(text); } catch (e) { data = { raw: text }; }

    if (r.status === 401) {
      return log('API Key 不对（服务返回 401）。\n'
                 + '请到管理页「账号池」页顶部复制正确的 API Key。', 'bad');
    }
    if (!r.ok) {
      return log(`导入失败：HTTP ${r.status}\n${text.slice(0, 300)}`, 'bad');
    }

    const a = (data.added && data.added[0]) || {};
    await saveCfg();
    log(`✓ 导入成功\n账号标签：${a.label || label || '(自动)'}\n`
        + `账号 ID：${a.id || '?'}\nCookie 条数：${a.cookie_count || names.length}\n`
        + `有效期到：${a.expires_at ? new Date(a.expires_at * 1000).toLocaleString() : '未知'}\n`
        + (data.warning ? `\n注意：${data.warning}` : ''), 'ok');
  } catch (e) {
    log('出错了：' + (e && e.message ? e.message : String(e))
        + '\n\n常见原因：\n'
        + '· 服务地址填错或服务没启动\n'
        + '· 这个地址不是 https（或证书不被信任）\n'
        + '· 浏览器拦截了跨域请求', 'bad');
  } finally {
    $('go').disabled = false;
  }
}

$('go').addEventListener('click', run);
loadCfg();

applyExtLang(EXT_LANG);
