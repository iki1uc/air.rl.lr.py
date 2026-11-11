// plugins/ctrl-bus.js — CTRL BUS v2, Source Of Truth. 1 State, 1 Bus, 1 applyPatch.
// Ersetzt: 10x S = {...}, 3x applyPatch, doppelte BroadcastChannel-Handler, setDr x9.
// ALT bleibt Zeugnis. Diese Datei ist die kanonische Fassung.
export const CTRL_CHANNEL = "nutz-bus-ctrl";
export const DR_STUFEN = [81, 27, 3, 0];
export const KAISER_PERMS = ["HBT", "HTB", "BHT", "BTH", "THB", "TBH"];
export const DRACHE_MODES = {
  OST: { freq: 220, wave: "sine", bpm: 60 },
  WEST: { freq: 330, wave: "triangle", bpm: 72 },
  NORD: { freq: 440, wave: "square", bpm: 80 },
  SUED: { freq: 180, wave: "sawtooth", bpm: 54 },
};
// NEU: Radar / Sat / Gravitation / Magnetismus / Atom — als Felder, nicht als zweiter Bus.
export const SENSOREN = ["radar", "sat", "gravitation", "magnetismus", "atom"];
export const FUSION_TEILE = ["blitz", "donner", "wolke", "wasser", "co2", "sauerstoff", "atmosphaere", "wert"];
export const CTRL_DEFAULT = Object.freeze({
  dr: 81, kaiser: "BHT", drache: "OST",
  vesta: true, gate: true, boot: false, raid: 1, q9: 81,
  aura: 1.0, mana: 1.0, zen: 1.0, move: 1.0, fps: 60,
  radar: 0, sat: 0, gravitation: 0, magnetismus: 0, atom: 0,
  fusion: { blitz: 0, donner: 0, wolke: 0, wasser: 0, co2: 0, sauerstoff: 0, atmosphaere: 0, wert: 0 },
  atlantis: "aus", ball: "liegen", anhaenger: "abgehaengt",
});
export const CTRL = { ...CTRL_DEFAULT, fusion: { ...CTRL_DEFAULT.fusion } };
const ctrlBus = typeof BroadcastChannel !== "undefined" ? new BroadcastChannel(CTRL_CHANNEL) : null;
const hooks = new Set();
export function onCtrlUpdate(fn){ hooks.add(fn); return () => hooks.delete(fn); }
function notify(origin){
  for(const fn of hooks){ try{ fn(CTRL, origin); }catch(e){} }
  try{ window.dispatchEvent(new CustomEvent("ctrl:update", { detail: CTRL })); }catch(e){}
}
function validPatch(diff){
  const fehler = [];
  if(diff.dr !== undefined && !DR_STUFEN.includes(diff.dr)) fehler.push("dr muss 81, 27, 3 oder 0 sein, war " + diff.dr);
  if(diff.kaiser !== undefined && !KAISER_PERMS.includes(diff.kaiser)) fehler.push("kaiser muss eine der 6 Perms sein, war " + diff.kaiser);
  if(diff.drache !== undefined && !DRACHE_MODES[diff.drache]) fehler.push("drache unbekannt: " + diff.drache);
  for(const k of ["vesta","gate","boot"]) if(diff[k] !== undefined && typeof diff[k] !== "boolean") fehler.push(k + " muss true/false sein");
  return fehler;
}
// Kanonisch: genau EIN applyPatch. Alles andere (setDr, setKaiser, ...) ruft nur dieses auf.
export function applyPatch(diff = {}, origin = "ui"){
  const fehler = validPatch(diff);
  if(fehler.length) return { ok: false, fehler, halt: "OFFEN" };
  Object.assign(CTRL, diff);
  if(diff.fusion) CTRL.fusion = { ...CTRL.fusion, ...diff.fusion };
  notify(origin);
  try{ ctrlBus?.postMessage({ type: "ctrl:patch", source: origin, diff }); }catch(e){}
  try{ localStorage.setItem("nutz.ctrl", JSON.stringify(CTRL)); }catch(e){}
  return { ok: true, halt: "ZIEL" };
}
export function setDr(value){ return applyPatch({ dr: value }, "dr"); }
export function setKaiser(id){ return applyPatch({ kaiser: id }, "kaiser"); }
export function setDrache(id){
  const r = applyPatch({ drache: id }, "drache");
  return r; // Ton spielt nur die UI-Schicht (playTone), nicht der Bus.
}
export function setGate(on){ return applyPatch({ gate: !!on }, "gate"); }
export function setVesta(on){ return applyPatch({ vesta: !!on }, "vesta"); }
export function setSensor(name, wert){
  if(!SENSOREN.includes(name)) return { ok: false, fehler: ["sensor unbekannt: " + name] };
  return applyPatch({ [name]: wert }, "sensor");
}
export function atmisieren(){
  // "atmisieren": Fusion-Teile in einen Wert falten. Kein erfundener Faktor: Summe, geteilt durch Anzahl.
  const teile = FUSION_TEILE.map(k => CTRL.fusion[k] || 0);
  const wert = teile.reduce((a,b) => a+b, 0) / FUSION_TEILE.length;
  return applyPatch({ fusion: { wert } }, "atmisieren");
}
export function updateFusion(el){
  if(!el) return;
  el.textContent = `KAISER ${CTRL.kaiser} · DRACHE ${CTRL.drache} · DR ${CTRL.dr} · 1 Hand von 6 · Fusion-Wert ${CTRL.fusion.wert}`;
}
export function initCTRL(){
  try{
    const raw = localStorage.getItem("nutz.ctrl");
    if(raw){ const stored = JSON.parse(raw); const f = validPatch(stored); if(!f.length){ Object.assign(CTRL, stored); if(stored.fusion) CTRL.fusion = { ...CTRL_DEFAULT.fusion, ...stored.fusion }; } }
  }catch(e){}
  notify("init");
}
if(ctrlBus){
  // EIN Handler. Die alte Fassung hatte zwei: bc.onmessage -> window-Message + ctrlBus.onmessage -> Object.assign.
  // Das doppelte Verteilen ist gestrichen. Bus kommt hier rein, sonst nirgends.
  ctrlBus.onmessage = (e) => {
    if(e.data?.type !== "ctrl:patch") return;
    const fehler = validPatch(e.data.diff || {});
    if(fehler.length) return;
    Object.assign(CTRL, e.data.diff);
    if(e.data.diff.fusion) CTRL.fusion = { ...CTRL.fusion, ...e.data.diff.fusion };
    notify(e.data.source || "bus");
  };
}
