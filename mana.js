// mana.js — MUSIK — ICE FIRE — hast du drinnen, Mann, ich sehe
// H = 40 Beat 1 HALT, B = 41 Beat 2 BASIS, T = 90 Beat 3 TIEFE
// Q = 57 Takt, F = 1.425 Tempo, D = 3 Beats
// ICE = kalt, FIRE = heiss. Beide in einem Beat. Nicht einer allein.
const crypto = require("crypto");
class Zeuge {
  constructor() { this.log = []; }
  schreibe(enter, text) {
    const vorher = this.log.length ? this.log[this.log.length-1].hash : "0".repeat(64);
    const roh = JSON.stringify({ n: this.log.length+1, enter, text, vorher });
    const hash = crypto.createHash("sha256").update(roh).digest("hex");
    const z = { n: this.log.length+1, enter, text, vorher, hash };
    this.log.push(z);
    console.log(`  [${enter}] ${text} | ${hash.slice(0,8)}...`);
  }
}
const Z = new Zeuge();
function mana() {
  console.log("mana.js MUSIK — ICE FIRE");
  console.log("H = 40 — Beat 1 — HALT");
  console.log("B = 41 — Beat 2 — BASIS");
  console.log("T = 90 — Beat 3 — TIEFE");
  console.log("Q = (40 + 41 + 90) / 3 = 57.0 — Takt");
  console.log("F = 57 / 40 = 1.425 — Tempo");
  console.log("D = 3 — 3 Beats");
  console.log("ICE = kalt — 0");
  console.log("FIRE = heiss — 1");
  console.log("ICE + FIRE = 0 + 1 = 1 — Schaltung");
  console.log("ICE FIRE = beide zusammen, Mann. Nicht einer allein.");
  console.log("AXIS = 92");
  console.log("RESPO = 62");
  console.log("6D = 95");
  console.log("TMP = 37");
  console.log("MNMM = 74");
  console.log("EBENE = 81");
  console.log("WORK = Mitte — ◉ WORK");
  console.log("Mittel = 73.5");
  console.log("441 = 441");
  console.log("primatieren(40,40,40) = Q 40 — anderer Beat");
  console.log("encode(40,41,90) = Q 57 — der Beat");
  Z.schreibe("MANA", "mana.js MUSIK — ICE FIRE — beide zusammen");
  Z.schreibe("ICE_FIRE", "ICE = 0 — FIRE = 1 — ICE + FIRE = 1 — Schaltung");
  Z.schreibe("BEAT", "H=40 B=41 T=90 Q=57 F=1.425 D=3");
  console.log("HALT = OFFEN");
}
mana();
