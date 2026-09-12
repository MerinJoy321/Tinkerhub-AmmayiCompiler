// frontend/js/ammayi.js — Centralized Ammayi frontend utilities

const API_BASE = (function() {
  const saved = localStorage.getItem('ammayi_api_base');
  return saved || 'http://localhost:8000';
})();

/**
 * 4 AMMAYI EXPRESSIONS
 * Centralized mapping per AGENTS.md & API contract:
 * 0–2 → unimpressed
 * 3–4 → disappointed
 * 5–7 → furious
 * 8+  → done
 */
function getAmmayiExpression(angerLevel) {
  const level = Number(angerLevel) || 0;
  if (level <= 2) return 'unimpressed';
  if (level <= 4) return 'disappointed';
  if (level <= 7) return 'furious';
  return 'done';
}

const AMMAYI_EXPRESSION_ASSETS = {
  unimpressed: 'assets/expressions/unimpressed.png',
  disappointed: 'assets/expressions/disappointed.png',
  furious: 'assets/expressions/furious.png',
  done: 'assets/expressions/done.png'
};

function getAmmayiExpressionSrc(angerLevel) {
  const expr = getAmmayiExpression(angerLevel);
  return AMMAYI_EXPRESSION_ASSETS[expr] || AMMAYI_EXPRESSION_ASSETS.unimpressed;
}

/**
 * Audio playback helper
 * ammayi_response.audio may be null. Frontend gracefully handles null.
 * When a valid audio path is provided, plays via API_BASE.
 */
function playAmmayiAudio(audioPath, onStart, onEnd) {
  if (!audioPath) {
    console.log('[Ammayi Audio] No audio asset available (audio is null).');
    if (onStart) onStart();
    setTimeout(() => { if (onEnd) onEnd(); }, 1200);
    return;
  }
  const fullUrl = audioPath.startsWith('http')
    ? audioPath
    : `${API_BASE}${audioPath.startsWith('/') ? '' : '/'}${audioPath}`;

  try {
    const audio = new Audio(fullUrl);
    if (onStart) onStart();
    audio.onended = () => { if (onEnd) onEnd(); };
    audio.onerror = (e) => {
      console.warn('[Ammayi Audio] Audio file not found or playback error:', fullUrl);
      if (onEnd) onEnd();
    };
    audio.play().catch(err => {
      console.warn('[Ammayi Audio] Autoplay or playback restricted:', err.message);
      if (onEnd) onEnd();
    });
  } catch (e) {
    console.warn('[Ammayi Audio] Error initializing audio:', e);
    if (onEnd) onEnd();
  }
}

/**
 * Session storage helpers
 */
function getSessionId() {
  return localStorage.getItem('ammayi_session_id') || null;
}

function setSessionId(id) {
  if (id) {
    localStorage.setItem('ammayi_session_id', id);
  }
}

function getCachedState() {
  try {
    const raw = localStorage.getItem('ammayi_cached_state');
    return raw ? JSON.parse(raw) : null;
  } catch (e) {
    return null;
  }
}

function setCachedState(state) {
  if (state) {
    localStorage.setItem('ammayi_cached_state', JSON.stringify(state));
  }
}

/**
 * Settings Modal Setup
 */
function openSettingsModal() {
  let modal = document.getElementById('ammayi-settings-modal');
  if (!modal) {
    modal = document.createElement('div');
    modal.id = 'ammayi-settings-modal';
    modal.className = 'fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60 backdrop-blur-sm';
    modal.innerHTML = `
      <div class="clay-card rounded-3xl p-6 md:p-8 max-w-md w-full bg-[#FFF9ED] border-[3px] border-[#392A27] shadow-[0_8px_0px_#392A27] space-y-5">
        <div class="flex items-center justify-between border-b-2 border-[#392A27]/20 pb-3">
          <div class="flex items-center gap-2">
            <span class="text-2xl">⚙️</span>
            <h3 class="font-['Bricolage_Grotesque'] text-xl font-extrabold text-[#392A27]">AMMAYI SETTINGS</h3>
          </div>
          <button onclick="closeSettingsModal()" class="w-8 h-8 rounded-xl bg-[#FFE8DE] border-2 border-[#392A27] font-bold text-[#873F4B] flex items-center justify-center text-sm shadow-[0_2px_0px_#392A27] hover:bg-[#F4B6A6]">✕</button>
        </div>

        <div class="space-y-4 font-mono text-xs text-[#392A27]">
          <div>
            <label class="block font-bold text-[#873F4B] mb-1">BACKEND API BASE URL</label>
            <input id="settings-api-url" type="text" class="w-full bg-[#FFF1D6] border-2 border-[#392A27] rounded-xl px-3 py-2 text-xs font-mono text-[#392A27] focus:outline-none focus:border-[#873F4B]" value="${API_BASE}">
            <span class="text-[10px] text-[#392A27]/60 block mt-1">Default: http://localhost:8000</span>
          </div>

          <div>
            <label class="block font-bold text-[#873F4B] mb-1">ACTIVE SESSION ID</label>
            <div class="p-2.5 bg-[#FFF1D6] rounded-xl border border-[#392A27]/30 text-[11px] break-all select-all font-mono">
              ${getSessionId() || 'No session initialized yet'}
            </div>
          </div>

          <div>
            <label class="block font-bold text-[#873F4B] mb-1">SHARMAJI BENCHMARK</label>
            <div class="p-2.5 bg-[#FFF1D6] rounded-xl border border-[#392A27]/30 text-[11px]">
              Son: Google Zurich (Staff L6) • 48 LPA • Status: Unmatched
            </div>
          </div>
        </div>

        <div class="pt-3 border-t-2 border-[#392A27]/20 flex flex-wrap items-center justify-between gap-3">
          <button onclick="clearSessionMemory()" class="clay-btn px-4 py-2 bg-[#ba1a1a]/20 text-[#ba1a1a] border-2 border-[#ba1a1a] rounded-xl font-mono text-xs font-bold hover:bg-[#ba1a1a]/30">
            Reset Session ID
          </button>
          <div class="flex items-center gap-2">
            <button onclick="saveSettings()" class="clay-btn px-5 py-2 bg-[#F2C35B] text-[#392A27] rounded-xl font-mono text-xs font-bold border-2 border-[#392A27]">
              Save Settings
            </button>
          </div>
        </div>
      </div>
    `;
    document.body.appendChild(modal);
  } else {
    modal.classList.remove('hidden');
    const input = document.getElementById('settings-api-url');
    if (input) input.value = API_BASE;
  }
}

function closeSettingsModal() {
  const modal = document.getElementById('ammayi-settings-modal');
  if (modal) modal.classList.add('hidden');
}

function saveSettings() {
  const input = document.getElementById('settings-api-url');
  if (input) {
    const val = input.value.trim();
    if (val) {
      localStorage.setItem('ammayi_api_base', val);
    }
  }
  closeSettingsModal();
  window.location.reload();
}

function clearSessionMemory() {
  localStorage.removeItem('ammayi_session_id');
  localStorage.removeItem('ammayi_cached_state');
  closeSettingsModal();
  window.location.reload();
}
