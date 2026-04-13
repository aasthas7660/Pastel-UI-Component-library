import { useState, useEffect, useRef } from "react";

/* =====================================================
   PASTEL UI KIT — Design System Showcase
   ===================================================== */

// ── Design Tokens ──────────────────────────────────────
const clr = {
  lav: ["#F7F5FF","#EDE8FF","#D5CCFF","#B5A8E8","#8B7BD4","#634FC4","#3B2896"],
  ros: ["#FFF0F6","#FFE0EC","#FFC5D9","#F098BE","#D968A0","#B53A76","#7A1F4F"],
  mnt: ["#EFFFF8","#D9FFEE","#B5F5D8","#6ED4A8","#3BBB8A","#199060","#0B4D35"],
  pch: ["#FFF7F0","#FFEDE0","#FFD8C0","#F4A87A","#E07848","#C05020","#7A2E0A"],
  sky: ["#F0F7FF","#DEEEFF","#BCDDFF","#72B4F8","#3A8DE8","#1562CC","#0A3870"],
  gry: ["#FAFAFA","#F5F4F2","#EDEBE6","#D6D3CB","#AEAAA3","#706C64","#2A2825"],
};

const s = {
  bg: "#FEFDFB", sbBg: "#F4F1FF", sbBorder: "#E4DFF5",
  cardBg: "#FFFFFF", prevBg: "#F8F6FE", border: "#E8E3F5",
  txt: "#1C1830", txtSub: "#6A6580", txtMut: "#A49DC0",
  accent: "#7C6EC9", accentHov: "#6358B4", accentLt: "#EDE8FF",
  success: "#3BBB8A", danger: "#E05475", warning: "#E07848", info: "#3A8DE8",
};

// ── Navigation ─────────────────────────────────────────
const NAV = [
  {
    group: "Foundation",
    items: [
      { id: "colors",     label: "Colors"     },
      { id: "typography", label: "Typography" },
      { id: "spacing",    label: "Spacing"    },
    ],
  },
  {
    group: "Components",
    items: [
      { id: "buttons",  label: "Buttons"  },
      { id: "inputs",   label: "Inputs"   },
      { id: "cards",    label: "Cards"    },
      { id: "badges",   label: "Badges"   },
      { id: "avatars",  label: "Avatars"  },
      { id: "tabs",     label: "Tabs"     },
      { id: "toggles",  label: "Toggles"  },
    ],
  },
  {
    group: "Feedback",
    items: [
      { id: "modals",   label: "Modals"   },
      { id: "toasts",   label: "Toasts"   },
      { id: "progress", label: "Progress" },
    ],
  },
];

// ── Helpers ────────────────────────────────────────────
function Section({ id, title, description, children }) {
  return (
    <section
      id={id}
      style={{ marginBottom: 64, scrollMarginTop: 24 }}
    >
      <div style={{ marginBottom: 24, paddingBottom: 16, borderBottom: `1px solid ${s.border}` }}>
        <h2 style={{ fontSize: 22, fontWeight: 800, color: s.txt, margin: "0 0 6px", fontFamily: '"DM Serif Display", serif' }}>
          {title}
        </h2>
        <p style={{ fontSize: 14, color: s.txtSub, margin: 0, lineHeight: 1.5 }}>{description}</p>
      </div>
      {children}
    </section>
  );
}

function Preview({ label, children, code }) {
  const [showCode, setShowCode] = useState(false);
  const [copied, setCopied] = useState(false);
  const copy = () => {
    navigator.clipboard?.writeText(code || "");
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };
  return (
    <div style={{ border: `1px solid ${s.border}`, borderRadius: 12, overflow: "hidden", marginBottom: 16, background: s.cardBg }}>
      {label && (
        <div style={{ padding: "9px 16px", borderBottom: `1px solid ${s.border}`, fontSize: 11, fontWeight: 700, color: s.txtMut, letterSpacing: "0.09em", textTransform: "uppercase" }}>
          {label}
        </div>
      )}
      <div style={{ padding: "32px 28px", background: s.prevBg, display: "flex", flexWrap: "wrap", gap: 12, alignItems: "center", minHeight: 90 }}>
        {children}
      </div>
      {code && (
        <>
          <div style={{ display: "flex", justifyContent: "space-between", padding: "8px 16px", borderTop: `1px solid ${s.border}`, background: s.cardBg }}>
            <button onClick={() => setShowCode(v => !v)} style={{ fontSize: 12, color: s.accent, background: "none", border: "none", cursor: "pointer", fontFamily: "inherit", fontWeight: 600, padding: 0 }}>
              {showCode ? "↑ Hide code" : "↓ Show code"}
            </button>
            {showCode && (
              <button onClick={copy} style={{ fontSize: 12, color: copied ? s.success : s.txtSub, background: "none", border: "none", cursor: "pointer", fontFamily: "inherit" }}>
                {copied ? "✓ Copied!" : "Copy"}
              </button>
            )}
          </div>
          {showCode && (
            <pre style={{ margin: 0, padding: 16, fontSize: 12, lineHeight: 1.65, background: "#1C1830", color: "#D5CCFF", overflowX: "auto", fontFamily: '"JetBrains Mono","Fira Code",monospace' }}>
              {code}
            </pre>
          )}
        </>
      )}
    </div>
  );
}

// ── Button ─────────────────────────────────────────────
function Btn({ variant = "primary", size = "md", disabled, loading, children, onClick, style: extraStyle }) {
  const base = {
    display: "inline-flex", alignItems: "center", justifyContent: "center", gap: 6,
    fontFamily: "inherit", fontWeight: 700, border: "1.5px solid",
    cursor: disabled || loading ? "not-allowed" : "pointer",
    opacity: disabled ? 0.55 : 1, transition: "all 0.15s", borderRadius: 8, letterSpacing: "0.01em",
  };
  const sz = { sm: { fontSize: 12, padding: "5px 13px", height: 30 }, md: { fontSize: 14, padding: "8px 18px", height: 38 }, lg: { fontSize: 15, padding: "10px 24px", height: 46 } };
  const vt = {
    primary:   { background: s.accent,   borderColor: s.accent,   color: "#FFF"    },
    secondary: { background: s.accentLt, borderColor: s.accentLt, color: s.accent  },
    ghost:     { background: "transparent", borderColor: "transparent", color: s.accent },
    outline:   { background: "transparent", borderColor: s.accent, color: s.accent  },
    danger:    { background: s.danger,   borderColor: s.danger,   color: "#FFF"    },
    success:   { background: s.success,  borderColor: s.success,  color: "#FFF"    },
    soft:      { background: clr.ros[1], borderColor: clr.ros[1], color: clr.ros[5] },
  };
  return (
    <button style={{ ...base, ...sz[size], ...vt[variant], ...extraStyle }} disabled={disabled || loading} onClick={onClick}>
      {loading && (
        <span style={{ display: "inline-block", width: 12, height: 12, border: "2px solid rgba(255,255,255,0.35)", borderTopColor: "#fff", borderRadius: "50%", animation: "spin 0.7s linear infinite" }} />
      )}
      {children}
    </button>
  );
}

// ── Input ──────────────────────────────────────────────
function Input({ label, placeholder, type = "text", prefix, suffix, error, disabled, hint }) {
  const [val, setVal] = useState("");
  const [focused, setFocused] = useState(false);
  return (
    <div style={{ width: "100%", maxWidth: 300 }}>
      {label && <label style={{ display: "block", fontSize: 13, fontWeight: 700, color: s.txt, marginBottom: 5 }}>{label}</label>}
      <div style={{
        display: "flex", alignItems: "center",
        border: `1.5px solid ${error ? s.danger : focused ? s.accent : s.border}`,
        borderRadius: 8, background: disabled ? s.prevBg : "#FFF",
        transition: "border-color 0.15s, box-shadow 0.15s",
        boxShadow: focused ? `0 0 0 3px ${s.accentLt}` : "none",
      }}>
        {prefix && <span style={{ padding: "0 10px", color: s.txtMut, fontSize: 14, flexShrink: 0 }}>{prefix}</span>}
        <input type={type} value={val} onChange={e => setVal(e.target.value)}
          onFocus={() => setFocused(true)} onBlur={() => setFocused(false)}
          placeholder={placeholder} disabled={disabled}
          style={{ flex: 1, border: "none", outline: "none", padding: "9px 12px", fontSize: 14, background: "transparent", color: s.txt, fontFamily: "inherit" }}
        />
        {suffix && <span style={{ padding: "0 10px", color: s.txtMut, fontSize: 14, flexShrink: 0 }}>{suffix}</span>}
      </div>
      {(hint || error) && <p style={{ fontSize: 12, color: error ? s.danger : s.txtSub, margin: "5px 0 0" }}>{error || hint}</p>}
    </div>
  );
}

// ── Badge ──────────────────────────────────────────────
function Badge({ variant = "lavender", size = "md", dot, children }) {
  const map = {
    lavender: { bg: clr.lav[1], color: clr.lav[5] },
    rose:     { bg: clr.ros[1], color: clr.ros[5] },
    mint:     { bg: clr.mnt[1], color: clr.mnt[5] },
    peach:    { bg: clr.pch[1], color: clr.pch[5] },
    sky:      { bg: clr.sky[1], color: clr.sky[5] },
    gray:     { bg: clr.gry[1], color: clr.gry[5] },
  };
  const sz = { sm: { fontSize: 10, padding: "2px 8px" }, md: { fontSize: 12, padding: "3px 10px" }, lg: { fontSize: 13, padding: "4px 14px" } };
  const v = map[variant] || map.lavender;
  return (
    <span style={{ display: "inline-flex", alignItems: "center", gap: 5, borderRadius: 20, fontWeight: 700, background: v.bg, color: v.color, ...sz[size] }}>
      {dot && <span style={{ width: 6, height: 6, borderRadius: "50%", background: v.color, flexShrink: 0 }} />}
      {children}
    </span>
  );
}

// ── Avatar ─────────────────────────────────────────────
function Avatar({ name, size = "md", status, color = "lavender" }) {
  const initials = (name || "?").split(" ").map(w => w[0]).slice(0, 2).join("").toUpperCase();
  const szMap = { xs: 28, sm: 36, md: 44, lg: 56, xl: 72 };
  const sz = szMap[size] || 44;
  const bgMap = {
    lavender: [clr.lav[1], clr.lav[5]], rose: [clr.ros[1], clr.ros[5]],
    mint:     [clr.mnt[1], clr.mnt[5]], peach: [clr.pch[1], clr.pch[5]],
    sky:      [clr.sky[1], clr.sky[5]], gray: [clr.gry[1], clr.gry[5]],
  };
  const [bg, fg] = bgMap[color] || bgMap.lavender;
  const statusClr = { online: "#22C55E", away: "#F59E0B", busy: "#EF4444", offline: clr.gry[3] };
  return (
    <div style={{ position: "relative", display: "inline-flex" }}>
      <div style={{ width: sz, height: sz, borderRadius: "50%", background: bg, color: fg, display: "flex", alignItems: "center", justifyContent: "center", fontSize: Math.round(sz * 0.35), fontWeight: 800, flexShrink: 0 }}>
        {initials}
      </div>
      {status && <span style={{ position: "absolute", bottom: 1, right: 1, width: Math.max(8, sz * 0.25), height: Math.max(8, sz * 0.25), borderRadius: "50%", background: statusClr[status], border: "2px solid #fff" }} />}
    </div>
  );
}

// ── Toggle ─────────────────────────────────────────────
function Toggle({ label, defaultChecked = false, color = "lavender" }) {
  const [on, setOn] = useState(defaultChecked);
  const bg = on ? (color === "rose" ? clr.ros[4] : color === "mint" ? clr.mnt[4] : s.accent) : clr.gry[2];
  return (
    <div style={{ display: "flex", alignItems: "center", gap: 10, cursor: "pointer", userSelect: "none" }} onClick={() => setOn(v => !v)}>
      <div style={{ width: 44, height: 24, borderRadius: 12, background: bg, transition: "background 0.2s", position: "relative", flexShrink: 0 }}>
        <div style={{ position: "absolute", top: 3, left: on ? 23 : 3, width: 18, height: 18, borderRadius: "50%", background: "#FFF", transition: "left 0.2s", boxShadow: "0 1px 3px rgba(0,0,0,0.2)" }} />
      </div>
      {label && <span style={{ fontSize: 14, color: s.txt }}>{label}</span>}
    </div>
  );
}

// ── Progress Bar ───────────────────────────────────────
function ProgressBar({ value = 0, color = "lavender", label, showValue }) {
  const clrMap = { lavender: s.accent, rose: s.danger, mint: s.success, peach: s.warning, sky: s.info };
  return (
    <div style={{ width: "100%" }}>
      {(label || showValue) && (
        <div style={{ display: "flex", justifyContent: "space-between", marginBottom: 6 }}>
          {label && <span style={{ fontSize: 13, color: s.txtSub }}>{label}</span>}
          {showValue && <span style={{ fontSize: 13, fontWeight: 700, color: s.txt }}>{value}%</span>}
        </div>
      )}
      <div style={{ height: 8, borderRadius: 4, background: clr.gry[2], overflow: "hidden" }}>
        <div style={{ height: "100%", width: `${value}%`, borderRadius: 4, background: clrMap[color] || s.accent, transition: "width 0.5s ease" }} />
      </div>
    </div>
  );
}

// ── Card ───────────────────────────────────────────────
function Card({ title, description, badge, footer, children, accent, width = 220 }) {
  const accentMap = { lavender: clr.lav[4], rose: clr.ros[4], mint: clr.mnt[4], peach: clr.pch[4], sky: clr.sky[4] };
  return (
    <div style={{ background: s.cardBg, border: `1px solid ${s.border}`, borderRadius: 12, overflow: "hidden", width }}>
      {accent && <div style={{ height: 4, background: accentMap[accent] || s.border }} />}
      <div style={{ padding: 16 }}>
        {badge && <div style={{ marginBottom: 10 }}>{badge}</div>}
        {title && <h3 style={{ fontSize: 15, fontWeight: 800, color: s.txt, margin: "0 0 6px", fontFamily: '"DM Serif Display", serif' }}>{title}</h3>}
        {description && <p style={{ fontSize: 13, color: s.txtSub, margin: 0, lineHeight: 1.55 }}>{description}</p>}
        {children}
      </div>
      {footer && <div style={{ padding: "10px 16px", borderTop: `1px solid ${s.border}`, background: s.prevBg }}>{footer}</div>}
    </div>
  );
}

// ── Modal ──────────────────────────────────────────────
function Modal({ open, onClose, title, children, footer }) {
  useEffect(() => {
    const handler = e => e.key === "Escape" && onClose();
    if (open) document.addEventListener("keydown", handler);
    return () => document.removeEventListener("keydown", handler);
  }, [open]);
  if (!open) return null;
  return (
    <div style={{ position: "fixed", inset: 0, background: "rgba(28,24,48,0.55)", display: "flex", alignItems: "center", justifyContent: "center", zIndex: 1000, padding: 24 }} onClick={onClose}>
      <div style={{ background: "#FFF", borderRadius: 16, padding: "28px 30px", maxWidth: 440, width: "100%", boxShadow: "0 24px 64px rgba(28,24,48,0.18)" }} onClick={e => e.stopPropagation()}>
        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start", marginBottom: 16 }}>
          <h3 style={{ fontSize: 20, fontWeight: 800, color: s.txt, margin: 0, fontFamily: '"DM Serif Display", serif' }}>{title}</h3>
          <button onClick={onClose} style={{ background: "none", border: "none", cursor: "pointer", fontSize: 22, color: s.txtMut, lineHeight: 1, padding: 0, marginLeft: 16, marginTop: -2 }}>×</button>
        </div>
        <div style={{ marginBottom: 22 }}>{children}</div>
        {footer && <div style={{ display: "flex", gap: 8, justifyContent: "flex-end" }}>{footer}</div>}
      </div>
    </div>
  );
}

// ── Toast ──────────────────────────────────────────────
function ToastItem({ toast, onRemove }) {
  const [visible, setVisible] = useState(false);
  useEffect(() => {
    requestAnimationFrame(() => setVisible(true));
    const t = setTimeout(() => { setVisible(false); setTimeout(() => onRemove(toast.id), 250); }, 3500);
    return () => clearTimeout(t);
  }, []);
  const cfg = {
    success: { border: clr.mnt[3], color: clr.mnt[5], icon: "✓", iconBg: s.success },
    error:   { border: clr.ros[3], color: clr.ros[5], icon: "✕", iconBg: s.danger  },
    warning: { border: clr.pch[3], color: clr.pch[5], icon: "!", iconBg: s.warning },
    info:    { border: clr.sky[3], color: clr.sky[5], icon: "i", iconBg: s.info    },
  };
  const c = cfg[toast.type] || cfg.info;
  return (
    <div style={{ display: "flex", alignItems: "flex-start", gap: 10, background: "#FFF", border: `1px solid ${c.border}`, borderLeft: `4px solid ${c.color}`, borderRadius: 10, padding: "12px 14px", boxShadow: "0 4px 20px rgba(28,24,48,0.1)", minWidth: 270, maxWidth: 340, transition: "all 0.25s", opacity: visible ? 1 : 0, transform: visible ? "translateX(0)" : "translateX(20px)" }}>
      <span style={{ width: 20, height: 20, borderRadius: "50%", background: c.iconBg, color: "#FFF", display: "flex", alignItems: "center", justifyContent: "center", fontSize: 10, fontWeight: 800, flexShrink: 0, marginTop: 1 }}>{c.icon}</span>
      <div style={{ flex: 1 }}>
        <p style={{ margin: 0, fontSize: 13, fontWeight: 700, color: s.txt }}>{toast.title}</p>
        {toast.msg && <p style={{ margin: "2px 0 0", fontSize: 12, color: s.txtSub, lineHeight: 1.4 }}>{toast.msg}</p>}
      </div>
      <button onClick={() => onRemove(toast.id)} style={{ background: "none", border: "none", cursor: "pointer", color: s.txtMut, fontSize: 18, lineHeight: 1, padding: 0, flexShrink: 0 }}>×</button>
    </div>
  );
}

// ── Tabs ───────────────────────────────────────────────
function Tabs({ tabs, renderContent }) {
  const [active, setActive] = useState(tabs[0]?.id);
  return (
    <div style={{ width: "100%", maxWidth: 420 }}>
      <div style={{ display: "flex", gap: 2, background: s.prevBg, padding: 4, borderRadius: 10, marginBottom: 16 }}>
        {tabs.map(t => (
          <button key={t.id} onClick={() => setActive(t.id)} style={{ flex: 1, padding: "7px 12px", borderRadius: 7, border: "none", background: active === t.id ? "#FFF" : "transparent", color: active === t.id ? s.accent : s.txtSub, fontWeight: active === t.id ? 700 : 500, fontSize: 13, cursor: "pointer", fontFamily: "inherit", boxShadow: active === t.id ? "0 1px 5px rgba(28,24,48,0.08)" : "none", transition: "all 0.15s" }}>
            {t.label}
          </button>
        ))}
      </div>
      <div style={{ padding: "14px 16px", background: "#FFF", borderRadius: 8, border: `1px solid ${s.border}`, fontSize: 13, color: s.txtSub, lineHeight: 1.55, minHeight: 56 }}>
        {renderContent(active)}
      </div>
    </div>
  );
}

// ── Color Swatch ───────────────────────────────────────
function Swatch({ name, shades }) {
  const stops = ["50", "100", "200", "300", "400", "500", "600"];
  return (
    <div style={{ marginBottom: 20 }}>
      <p style={{ fontSize: 11, fontWeight: 800, color: s.txtSub, marginBottom: 7, textTransform: "uppercase", letterSpacing: "0.09em" }}>{name}</p>
      <div style={{ display: "flex", gap: 5 }}>
        {shades.map((hex, i) => (
          <div key={i} style={{ flex: 1, display: "flex", flexDirection: "column", alignItems: "center", gap: 4 }}>
            <div style={{ width: "100%", paddingBottom: "70%", borderRadius: 6, background: hex, border: i === 0 ? `1px solid ${s.border}` : "none" }} />
            <span style={{ fontSize: 10, color: s.txtMut }}>{stops[i]}</span>
          </div>
        ))}
      </div>
    </div>
  );
}

// ── Spacing Tokens ─────────────────────────────────────
const SPACES = [
  { name: "2xs", val: 4  }, { name: "xs",  val: 8  }, { name: "sm", val: 12 },
  { name: "md",  val: 16 }, { name: "lg",  val: 24 }, { name: "xl", val: 32 },
  { name: "2xl", val: 48 }, { name: "3xl", val: 64 },
];

// ── Main App ───────────────────────────────────────────
export default function UIKit() {
  const [activeNav, setActiveNav] = useState("colors");
  const [modalOpen, setModalOpen] = useState(false);
  const [toasts, setToasts] = useState([]);
  const toastId = useRef(0);

  const addToast = (type, title, msg) => {
    setToasts(t => [...t, { id: toastId.current++, type, title, msg }]);
  };
  const removeToast = id => setToasts(t => t.filter(x => x.id !== id));

  const scrollTo = id => {
    setActiveNav(id);
    document.getElementById(id)?.scrollIntoView({ behavior: "smooth", block: "start" });
  };

  // Scrollspy
  useEffect(() => {
    const allIds = NAV.flatMap(g => g.items.map(i => i.id));
    const observer = new IntersectionObserver(
      entries => {
        entries.forEach(e => { if (e.isIntersecting) setActiveNav(e.target.id); });
      },
      { threshold: 0.25, rootMargin: "-10% 0px -60% 0px" }
    );
    allIds.forEach(id => { const el = document.getElementById(id); if (el) observer.observe(el); });
    return () => observer.disconnect();
  }, []);

  return (
    <>
      <style>{`
        @import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=Nunito:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');
        *, *::before, *::after { box-sizing: border-box; }
        html, body { margin: 0; padding: 0; background: ${s.bg}; font-family: 'Nunito', sans-serif; }
        @keyframes spin { to { transform: rotate(360deg); } }
        ::-webkit-scrollbar { width: 5px; height: 5px; }
        ::-webkit-scrollbar-track { background: transparent; }
        ::-webkit-scrollbar-thumb { background: ${clr.lav[2]}; border-radius: 3px; }
      `}</style>

      <div style={{ display: "flex", minHeight: "100vh" }}>

        {/* ── Sidebar ── */}
        <aside style={{ width: 224, flexShrink: 0, background: s.sbBg, borderRight: `1px solid ${s.sbBorder}`, position: "fixed", top: 0, left: 0, bottom: 0, overflowY: "auto", zIndex: 10 }}>
          {/* Logo */}
          <div style={{ padding: "22px 20px", borderBottom: `1px solid ${s.sbBorder}`, display: "flex", alignItems: "center", gap: 10 }}>
            <div style={{ width: 34, height: 34, borderRadius: 9, background: `linear-gradient(140deg, ${clr.lav[4]} 0%, ${clr.ros[3]} 100%)`, display: "flex", alignItems: "center", justifyContent: "center", fontSize: 15, fontWeight: 900, color: "#FFF", flexShrink: 0, letterSpacing: "-0.02em" }}>P</div>
            <div>
              <div style={{ fontSize: 14, fontWeight: 800, color: s.txt, lineHeight: 1.1 }}>Pastel UI</div>
              <div style={{ fontSize: 10, color: s.txtMut, letterSpacing: "0.05em" }}>Design System v1.0</div>
            </div>
          </div>

          {/* Nav groups */}
          {NAV.map(group => (
            <div key={group.group} style={{ padding: "16px 12px 6px" }}>
              <div style={{ fontSize: 10, fontWeight: 900, color: s.txtMut, textTransform: "uppercase", letterSpacing: "0.1em", padding: "0 8px", marginBottom: 4 }}>
                {group.group}
              </div>
              {group.items.map(item => {
                const isActive = activeNav === item.id;
                return (
                  <button key={item.id} onClick={() => scrollTo(item.id)} style={{ display: "flex", alignItems: "center", width: "100%", padding: "7px 10px", borderRadius: 7, border: "none", background: isActive ? clr.lav[1] : "transparent", color: isActive ? clr.lav[5] : s.txtSub, fontSize: 13, fontWeight: isActive ? 700 : 500, cursor: "pointer", textAlign: "left", fontFamily: "inherit", transition: "all 0.12s", gap: 8 }}>
                    {isActive && <span style={{ width: 3, height: 14, borderRadius: 2, background: clr.lav[4], flexShrink: 0 }} />}
                    {!isActive && <span style={{ width: 3, flexShrink: 0 }} />}
                    {item.label}
                  </button>
                );
              })}
            </div>
          ))}

          {/* Footer */}
          <div style={{ position: "absolute", bottom: 0, left: 0, right: 0, padding: "14px 20px", borderTop: `1px solid ${s.sbBorder}`, background: s.sbBg }}>
            <p style={{ margin: 0, fontSize: 11, color: s.txtMut, lineHeight: 1.4 }}>Built with React & ❤</p>
          </div>
        </aside>

        {/* ── Content ── */}
        <main style={{ marginLeft: 224, flex: 1, padding: "44px 52px 80px", maxWidth: 980, minWidth: 0 }}>

          {/* Hero */}
          <div style={{ marginBottom: 56 }}>
            <div style={{ display: "inline-flex", alignItems: "center", gap: 6, background: clr.lav[1], color: clr.lav[5], padding: "4px 12px", borderRadius: 20, fontSize: 11, fontWeight: 800, marginBottom: 18, letterSpacing: "0.06em", textTransform: "uppercase" }}>
              ✦ Component Showcase
            </div>
            <h1 style={{ fontSize: 42, fontWeight: 900, color: s.txt, margin: "0 0 14px", fontFamily: '"DM Serif Display", serif', lineHeight: 1.05, letterSpacing: "-0.01em" }}>
              Pastel UI Kit
            </h1>
            <p style={{ fontSize: 16, color: s.txtSub, margin: "0 0 28px", maxWidth: 520, lineHeight: 1.65 }}>
              A refined, accessible design system built for modern web apps — warm, inviting, and production-ready out of the box.
            </p>
            <div style={{ display: "flex", gap: 10, flexWrap: "wrap" }}>
              {["Colors", "Typography", "Buttons", "Inputs", "Cards", "Badges", "Modals", "Toasts"].map(t => (
                <span key={t} style={{ fontSize: 12, fontWeight: 600, color: s.txtSub, background: s.prevBg, padding: "4px 10px", borderRadius: 6, border: `1px solid ${s.border}` }}>{t}</span>
              ))}
            </div>
          </div>

          {/* ── Foundation ── */}

          <Section id="colors" title="Color Palette" description="Five harmonious pastel ramps with seven stops each — consistent hierarchy from lightest fill to deepest text.">
            <Preview label="All Swatches">
              <div style={{ width: "100%" }}>
                <Swatch name="Lavender" shades={clr.lav} />
                <Swatch name="Rose"     shades={clr.ros} />
                <Swatch name="Mint"     shades={clr.mnt} />
                <Swatch name="Peach"    shades={clr.pch} />
                <Swatch name="Sky"      shades={clr.sky} />
              </div>
            </Preview>
            <Preview label="Semantic Tokens">
              <div style={{ display: "flex", flexWrap: "wrap", gap: 10 }}>
                {[
                  { label: "Accent",  bg: s.accent,  text: "#FFF" },
                  { label: "Success", bg: s.success, text: "#FFF" },
                  { label: "Danger",  bg: s.danger,  text: "#FFF" },
                  { label: "Warning", bg: s.warning, text: "#FFF" },
                  { label: "Info",    bg: s.info,    text: "#FFF" },
                ].map(({ label, bg, text }) => (
                  <div key={label} style={{ padding: "8px 16px", borderRadius: 8, background: bg, color: text, fontSize: 13, fontWeight: 700 }}>{label}</div>
                ))}
              </div>
            </Preview>
          </Section>

          <Section id="typography" title="Typography" description="DM Serif Display for expressive headings paired with Nunito for warm, approachable body text.">
            <Preview label="Type Scale">
              <div style={{ width: "100%" }}>
                {[
                  { label: "Display",  fam: '"DM Serif Display", serif', size: 38, wt: 400, sample: "Design, crafted with care" },
                  { label: "H1",       fam: "inherit",                   size: 30, wt: 800, sample: "Page Heading"            },
                  { label: "H2",       fam: "inherit",                   size: 22, wt: 800, sample: "Section Heading"         },
                  { label: "H3",       fam: "inherit",                   size: 17, wt: 700, sample: "Sub-Section"             },
                  { label: "Body",     fam: "inherit",                   size: 15, wt: 400, sample: "Regular paragraph text for comfortable reading at length." },
                  { label: "Small",    fam: "inherit",                   size: 13, wt: 400, sample: "Secondary information and helper text." },
                  { label: "Label",    fam: "inherit",                   size: 11, wt: 800, sample: "UPPERCASE LABEL · 0.09EM TRACKING" },
                  { label: "Mono",     fam: '"JetBrains Mono", monospace', size: 13, wt: 400, sample: 'const theme = "pastel";' },
                ].map(({ label, fam, size, wt, sample }) => (
                  <div key={label} style={{ display: "flex", alignItems: "baseline", gap: 16, padding: "10px 0", borderBottom: `1px solid ${s.border}` }}>
                    <span style={{ fontSize: 10, fontWeight: 900, color: s.txtMut, textTransform: "uppercase", letterSpacing: "0.07em", width: 50, flexShrink: 0 }}>{label}</span>
                    <span style={{ fontFamily: fam, fontSize: size, fontWeight: wt, color: s.txt, lineHeight: 1.2, letterSpacing: label === "Label" ? "0.09em" : "normal" }}>{sample}</span>
                  </div>
                ))}
              </div>
            </Preview>
          </Section>

          <Section id="spacing" title="Spacing Scale" description="A consistent 4px-base spacing system for predictable layouts and rhythm.">
            <Preview label="Spacing Tokens">
              <div style={{ width: "100%", display: "flex", flexDirection: "column", gap: 12 }}>
                {SPACES.map(({ name, val }) => (
                  <div key={name} style={{ display: "flex", alignItems: "center", gap: 14 }}>
                    <span style={{ fontSize: 12, fontWeight: 700, color: s.txtSub, width: 34, flexShrink: 0 }}>{name}</span>
                    <div style={{ width: val, height: 20, borderRadius: 4, background: clr.lav[2], flexShrink: 0 }} />
                    <span style={{ fontSize: 11, color: s.txtMut }}>{val}px / {(val/16).toFixed(3).replace(/0+$/, "").replace(/\.$/, "")}rem</span>
                  </div>
                ))}
              </div>
            </Preview>
          </Section>

          {/* ── Components ── */}

          <Section id="buttons" title="Buttons" description="Six semantic button variants, three sizes, plus loading and disabled states.">
            <Preview label="Variants" code={`<Btn>Primary</Btn>\n<Btn variant="secondary">Secondary</Btn>\n<Btn variant="outline">Outline</Btn>\n<Btn variant="ghost">Ghost</Btn>\n<Btn variant="danger">Danger</Btn>\n<Btn variant="success">Success</Btn>`}>
              <Btn>Primary</Btn>
              <Btn variant="secondary">Secondary</Btn>
              <Btn variant="outline">Outline</Btn>
              <Btn variant="ghost">Ghost</Btn>
              <Btn variant="danger">Danger</Btn>
              <Btn variant="success">Success</Btn>
            </Preview>
            <Preview label="Sizes" code={`<Btn size="sm">Small</Btn>\n<Btn size="md">Medium</Btn>\n<Btn size="lg">Large</Btn>`}>
              <Btn size="sm">Small</Btn>
              <Btn size="md">Medium</Btn>
              <Btn size="lg">Large</Btn>
            </Preview>
            <Preview label="States" code={`<Btn loading>Saving…</Btn>\n<Btn disabled>Disabled</Btn>`}>
              <Btn loading>Saving…</Btn>
              <Btn disabled>Disabled</Btn>
              <Btn variant="secondary" loading>Loading</Btn>
            </Preview>
          </Section>

          <Section id="inputs" title="Inputs" description="Form fields with prefix/suffix support, validation states, and focus rings.">
            <Preview label="Default" code={`<Input label="Full Name" placeholder="Jane Doe" />`}>
              <Input label="Full Name" placeholder="Jane Doe" />
            </Preview>
            <Preview label="With Affix" code={`<Input label="Price" prefix="$" suffix="USD" placeholder="0.00" />`}>
              <Input label="Price" prefix="$" suffix="USD" placeholder="0.00" />
            </Preview>
            <Preview label="Hint & Error" code={`<Input label="Password" type="password" hint="Min 8 characters" />\n<Input label="Email" error="Invalid email address." />`}>
              <Input label="Password" type="password" placeholder="••••••••" hint="Must be at least 8 characters." />
              <Input label="Email" placeholder="you@example.com" error="Please enter a valid email address." />
            </Preview>
            <Preview label="Disabled">
              <Input label="Read-only field" placeholder="Cannot edit this" disabled />
            </Preview>
          </Section>

          <Section id="cards" title="Cards" description="Flexible content containers with optional color accents, badges, and footers.">
            <Preview label="Variants">
              <Card
                title="Getting Started"
                description="Install and configure the design system in your project within minutes."
                badge={<Badge variant="mint" dot>New</Badge>}
                footer={<Btn size="sm" variant="outline">Read docs →</Btn>}
              />
              <Card
                accent="rose"
                title="Analytics Report"
                description="Monthly active users grew 24% this quarter across all channels."
                badge={<Badge variant="rose">↑ 24%</Badge>}
                footer={
                  <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
                    <span style={{ fontSize: 11, color: s.txtMut }}>Updated 2h ago</span>
                    <Btn size="sm" variant="ghost">Details</Btn>
                  </div>
                }
              />
              <Card
                accent="sky"
                title="Sara Kim"
                description="Lead designer with 5+ years of experience in product design systems."
                badge={
                  <div style={{ display: "flex", alignItems: "center", gap: 8 }}>
                    <Avatar name="Sara Kim" size="sm" color="sky" />
                    <Badge variant="sky" dot>Online</Badge>
                  </div>
                }
              />
            </Preview>
          </Section>

          <Section id="badges" title="Badges" description="Compact labels for status, categories, and metadata.">
            <Preview label="Colors" code={`<Badge variant="lavender">Lavender</Badge>\n<Badge variant="rose">Rose</Badge>`}>
              <Badge variant="lavender">Lavender</Badge>
              <Badge variant="rose">Rose</Badge>
              <Badge variant="mint">Mint</Badge>
              <Badge variant="peach">Peach</Badge>
              <Badge variant="sky">Sky</Badge>
              <Badge variant="gray">Gray</Badge>
            </Preview>
            <Preview label="With Dot Indicator">
              <Badge variant="mint" dot>Active</Badge>
              <Badge variant="rose" dot>Offline</Badge>
              <Badge variant="peach" dot>Away</Badge>
              <Badge variant="sky" dot>Syncing</Badge>
              <Badge variant="gray" dot>Archived</Badge>
            </Preview>
            <Preview label="Sizes">
              <Badge variant="lavender" size="sm">Small</Badge>
              <Badge variant="lavender" size="md">Medium</Badge>
              <Badge variant="lavender" size="lg">Large</Badge>
            </Preview>
          </Section>

          <Section id="avatars" title="Avatars" description="User identity components with initials, status indicators, and group stacking.">
            <Preview label="Sizes">
              <Avatar name="A B" size="xs" color="lavender" />
              <Avatar name="Beth Row" size="sm" color="rose" />
              <Avatar name="Carlos M" size="md" color="mint" />
              <Avatar name="Diana P" size="lg" color="peach" />
              <Avatar name="Evan S" size="xl" color="sky" />
            </Preview>
            <Preview label="Status Indicators">
              {[
                { name: "Anna L", color: "lavender", status: "online"  },
                { name: "Ben T",  color: "rose",     status: "away"    },
                { name: "Cara H", color: "mint",     status: "busy"    },
                { name: "Dan W",  color: "sky",      status: "offline" },
              ].map(a => (
                <div key={a.name} style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: 6 }}>
                  <Avatar {...a} size="md" />
                  <span style={{ fontSize: 11, color: s.txtSub, textTransform: "capitalize" }}>{a.status}</span>
                </div>
              ))}
            </Preview>
            <Preview label="Group Stack">
              <div style={{ display: "flex", alignItems: "center", gap: 0 }}>
                {[
                  { name: "Alice B", color: "lavender" },
                  { name: "Bob C",   color: "rose"     },
                  { name: "Carol D", color: "mint"     },
                  { name: "Dave E",  color: "peach"    },
                ].map((a, i) => (
                  <div key={i} style={{ marginLeft: i > 0 ? -8 : 0, border: "2.5px solid #FFF", borderRadius: "50%", zIndex: 4 - i }}>
                    <Avatar name={a.name} size="sm" color={a.color} />
                  </div>
                ))}
                <div style={{ marginLeft: -8, width: 36, height: 36, borderRadius: "50%", background: clr.gry[1], border: "2.5px solid #FFF", display: "flex", alignItems: "center", justifyContent: "center", fontSize: 11, fontWeight: 800, color: clr.gry[5] }}>+4</div>
                <span style={{ marginLeft: 12, fontSize: 13, color: s.txtSub }}>8 team members</span>
              </div>
            </Preview>
          </Section>

          <Section id="tabs" title="Tabs" description="Pill-style tab navigation for switching between content panels.">
            <Preview label="Interactive Tabs" code={`<Tabs tabs={[...]} renderContent={id => <div>{id}</div>} />`}>
              <Tabs
                tabs={[{ id: "overview", label: "Overview" }, { id: "analytics", label: "Analytics" }, { id: "settings", label: "Settings" }]}
                renderContent={id => ({
                  overview:  "Overview — A high-level summary of your project's key metrics and recent activity.",
                  analytics: "Analytics — Detailed charts and breakdowns across sessions, users, and conversions.",
                  settings:  "Settings — Configure preferences, notifications, integrations, and access controls.",
                }[id])}
              />
            </Preview>
          </Section>

          <Section id="toggles" title="Toggles" description="Smooth animated switches for boolean preferences and settings.">
            <Preview label="Toggle Controls" code={`<Toggle label="Enable notifications" />\n<Toggle label="Dark mode" defaultChecked />`}>
              <div style={{ display: "flex", flexDirection: "column", gap: 16 }}>
                <Toggle label="Enable notifications" />
                <Toggle label="Auto-save drafts" defaultChecked />
                <Toggle label="Show online status" color="mint" />
                <Toggle label="Marketing emails" color="rose" defaultChecked />
              </div>
            </Preview>
          </Section>

          {/* ── Feedback ── */}

          <Section id="modals" title="Modals" description="Accessible overlay dialogs for confirmations, alerts, and form interactions.">
            <Preview label="Open Modal Demo">
              <Btn onClick={() => setModalOpen(true)}>Open Modal</Btn>
              <p style={{ fontSize: 13, color: s.txtMut, margin: 0 }}>Click button → modal opens with backdrop • press Esc to close</p>
            </Preview>
          </Section>

          <Section id="toasts" title="Toasts" description="Auto-dismissing notifications with animated entry and four semantic variants.">
            <Preview label="Trigger Toasts" code={`addToast('success', 'Saved!', 'Your changes were saved.')\naddToast('error', 'Failed', 'Something went wrong.')`}>
              <Btn variant="success" size="sm" onClick={() => addToast("success", "Changes saved!", "Your profile was updated successfully.")}>Success</Btn>
              <Btn variant="danger"  size="sm" onClick={() => addToast("error",   "Upload failed",  "File size exceeds the 5 MB limit.")}>Error</Btn>
              <Btn variant="secondary" size="sm" onClick={() => addToast("warning", "Low storage",  "You have only 200 MB remaining.")}>Warning</Btn>
              <Btn variant="outline"  size="sm" onClick={() => addToast("info",    "Pro tip",       "Drag cards to reorder your dashboard.")}>Info</Btn>
            </Preview>
          </Section>

          <Section id="progress" title="Progress" description="Visual progress indicators for uploads, loading states, and task completion.">
            <Preview label="Progress Bars" code={`<ProgressBar value={75} color="lavender" label="Storage" showValue />`}>
              <div style={{ width: "100%", display: "flex", flexDirection: "column", gap: 16 }}>
                <ProgressBar value={75} color="lavender" label="Storage used"      showValue />
                <ProgressBar value={48} color="rose"     label="Monthly budget"    showValue />
                <ProgressBar value={93} color="mint"     label="Tasks complete"    showValue />
                <ProgressBar value={30} color="peach"    label="Profile setup"     showValue />
                <ProgressBar value={62} color="sky"      label="API rate limit"    showValue />
              </div>
            </Preview>
          </Section>

        </main>
      </div>

      {/* Modal */}
      <Modal
        open={modalOpen}
        onClose={() => setModalOpen(false)}
        title="Confirm Action"
        footer={[
          <Btn key="cancel"   variant="ghost"   onClick={() => setModalOpen(false)}>Cancel</Btn>,
          <Btn key="confirm"  variant="primary"
            onClick={() => {
              setModalOpen(false);
              addToast("success", "Action confirmed!", "The operation completed successfully.");
            }}
          >Confirm</Btn>,
        ]}
      >
        <p style={{ margin: "0 0 12px", fontSize: 14, color: s.txtSub, lineHeight: 1.65 }}>
          Are you sure you want to proceed? This will apply your selected changes and cannot be undone.
        </p>
        <div style={{ padding: "10px 14px", background: clr.pch[0], border: `1px solid ${clr.pch[2]}`, borderRadius: 8 }}>
          <p style={{ margin: 0, fontSize: 12, color: clr.pch[5], fontWeight: 600 }}>⚠ This will affect all members in your workspace.</p>
        </div>
      </Modal>

      {/* Toast Container */}
      <div style={{ position: "fixed", bottom: 24, right: 24, display: "flex", flexDirection: "column", gap: 8, zIndex: 2000 }}>
        {toasts.map(t => <ToastItem key={t.id} toast={t} onRemove={removeToast} />)}
      </div>
    </>
  );
}
