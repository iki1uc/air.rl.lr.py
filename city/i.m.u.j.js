// i.m.u.j.js — I M U J — SO, MANN, SO SOSSO MACH ICH DAS
// 1, 2, 3, 4, 5, 6, 7 — AN. AUS. EINFACH, MANN.
// Nur JS. Bewegt nichts, loescht nichts, schreibt keine Dateien.
// Zeuge: echte Hash-Kette mit Node crypto, nicht behauptet.
const crypto = require("crypto");
class Zeuge {
  constructor() { this.log = []; }
  schreibe(enter, text) {
    const vorher = this.log.length ? this.log[this.log.length - 1].hash : "0".repeat(64);
    const roh = JSON.stringify({ n: this.log.length + 1, enter, text, vorher });
    const hash = crypto.createHash("sha256").update(roh).digest("hex");
    const z = { n: this.log.length + 1, enter, text, vorher, hash };
    this.log.push(z);
    console.log(`  [${enter}] ${text} | ${hash.slice(0, 8)}...`);
    return z;
  }
  unversehrt() {
    let vorher = "0".repeat(64);
    for (const z of this.log) {
      if (z.vorher !== vorher) return false;
      const roh = JSON.stringify({ n: z.n, enter: z.enter, text: z.text, vorher: z.vorher });
      if (crypto.createHash("sha256").update(roh).digest("hex") !== z.hash) return false;
      vorher = z.hash;
    }
    return true;
  }
}
const Z = new Zeuge();
function i_m_u_j() {
  console.log("I M U J — SO, MANN, SO SOSSO MACH ICH DAS");
  console.log("1, 2, 3, 4, 5, 6, 7");
  console.log("AN. AUS. EINFACH, MANN.");
  Z.schreibe("AN", "An — da");
  Z.schreibe("AUS", "Aus — nicht da");
  Z.schreibe("SCHALTUNG", "An + Aus = Schaltung — beide zusammen");
  Z.schreibe("XI", "XI IX IO OI IQ QI — vor rück auf ab rein raus");
  Z.schreibe("MANN", "IN NI MANN — In Ni Mann — Mehr Mann");
  console.log(`Zeuge: ${Z.log.length} Zeilen, unversehrt=${Z.unversehrt()}. HALT = OFFEN. Echo bleibt. Hall bleibt.`);
  console.log("ECO: I M U J — So, so sosso — An, Aus, Schaltung, XI, Mann.");
}
i_m_u_j();
