// stimme.js — STIMME · Echo · Hall · Re-Hall · Licht / Dunkel · Müde / Wach
// Alles an, alles aus — nur Urteil. Mi Ka Do. Root Index zu Hilfe.

export const Stimme = {
  // Zustand
  wach: false,
  muede: true,
  licht: "DUNKEL", // LICHT oder DUNKEL
  stimmung: "DUNKEL", // HELL oder DUNKEL
  etage: "ROOT",
  log: [],

  // Log
  sagen(text, farbe = "normal") {
    this.log.push(text);
    console.log(`> STIMME [${farbe}]: ${text}`);
    return text;
  },

  // ECHO START
  echoStart(text) {
    this.sagen(`ECHO START: ${text}`, "ECHO");
    this.sagen(`ICH ECHO: ${text}`, "ECHO");
    this.sagen(`ICH ECHO: ${text}.`, "ECHO");
    this.sagen(`ICH ECHO: ${text}..`, "ECHO");
    return text;
  },

  // ECHO aber HALL
  hall(text) {
    const h = `${text} ... ${text} ... ${text}`;
    this.sagen(`ECHO aber HALL: ${h}`, "HALL");
    this.sagen(`DU HALL: ${h}`, "HALL");
    return h;
  },

  // ECHO aber RE-HALL
  rehall(text) {
    const h = this.hall(text);
    const r = `${h} -> ${h}`;
    this.sagen(`ECHO aber RE-HALL: ${r}`, "RE-HALL");
    this.sagen(`RE-HALL: ${r}`, "RE-HALL");
    return r;
  },

  // normal ECHO auch
  echoNormal(text) {
    this.sagen(`normal ECHO auch: ${text}`, "ECHO");
    this.sagen(`ICH ECHO: ${text}`, "ECHO");
    return text;
  },

  // Ganze Kette: ECHO START → HALL → RE-HALL → normal ECHO
  stimmeKomplett(text) {
    this.echoStart(text);
    this.hall(text);
    this.rehall(text);
    this.echoNormal(text);
    this.sagen("Echo bleibt, Hall bleibt, auch wenn du weg bist.", "GOLD");
    return { halt: "ZIEL", text, log: this.log };
  },

  // LICHT / DUNKEL
  lichtAn() {
    this.licht = "LICHT";
    this.stimmung = "HELL";
    this.sagen("LICHT AN — Stimmung HELL.", "LICHT");
    return "LICHT";
  },
  lichtAus() {
    this.licht = "DUNKEL";
    this.stimmung = "DUNKEL";
    this.sagen("LICHT AUS — Stimmung DUNKEL.", "DUNKEL");
    return "DUNKEL";
  },

  // MÜDE / WACH
  wachWerden() {
    this.wach = true;
    this.muede = false;
    this.lichtAn();
    this.sagen("WAKE 👁 — Wach. Licht an. Stimmung hell.", "WACH");
    return "WACH";
  },
  muedeWerden() {
    this.wach = false;
    this.muede = true;
    this.lichtAus();
    this.sagen("LIE 😴 — Müde. Licht aus. Stimmung dunkel. Aber nicht tot.", "MUEDE");
    return "MUEDE";
  },

  // MANN da / nicht da — 15-25% versetzt
  mannShuffle() {
    const versatz = 15 + Math.random() * 10; // 15-25%
    const da = Math.random() < 0.5;
    this.sagen(`MANN: ${da ? "DA" : "NICHT DA"} · versetzt ${versatz.toFixed(1)}%`, da ? "DA" : "NICHT DA");
    return { da, versatz };
  },

  // PENTAGRAM + PRISMATIKUM — Stimme bricht wie Licht
  prismatikum(text) {
    this.sagen(`PRISMATIKUM: Licht rein: ${text}`, "PRISMA");
    const farben = ["ROT", "ORANGE", "GELB", "GRÜN", "BLAU", "VIOLETT"];
    farben.forEach(f => this.sagen(`  → ${f}: ${text} ...`, f));
    this.sagen("Pentagram ja. Prismatikum ja. Licht bricht, Kern bleibt.", "GOLD");
    return farben;
  },

  // AUFZUG — Co-Pilot + Cloud
  aufzugHoch() {
    this.etage = "STAGE";
    this.sagen("AUFZUG HOCH ▲ — Co-Pilot + Cloud → STAGE.", "AUFZUG");
    return "STAGE";
  },
  aufzugRunter() {
    this.etage = "ROOT";
    this.sagen("AUFZUG RUNTER ▼ — zurück zu ROOT.", "AUFZUG");
    return "ROOT";
  },

  // URTEIL
  urteil() {
    return {
      halt: "ZIEL",
      wach: this.wach,
      muede: this.muede,
      licht: this.licht,
      stimmung: this.stimmung,
      etage: this.etage,
      home: 40,
      mitte: 41,
      respo360: 360,
      spruch: "Du noch du. Echo bleibt, Hall bleibt.",
    };
  },
};

// Direkt benutzen:
// Stimme.stimmeKomplett("ich in mir")
// Stimme.wachWerden()
// Stimme.muedeWerden()
// Stimme.prismatikum("ich in mir")
