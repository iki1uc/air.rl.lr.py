// hbt_pool_codec.js — CODEC · Pentagram Codec · Einfach · Kollidierende Beste · Easy Going JS
// Wir haben Codec. Wir können Codec Pentagrammen. Primatieren sogar.
// Wir machen nur H B T — aber gegen POOL.
// Gegen Pool ist Q = Quant Nutzung, dann F = Faktor, D = Dimension.

export const HBTCodec = {
  // H B T — nur das
  H: 0, B: 0, T: 0,
  // POOL — gegen Pool
  pool: [],
  // Q F D — Quant, Faktor, Dimension
  Q: 0, F: 1, D: 1,

  // CODEC — kodieren
  encode(h, b, t){
    this.H = h; this.B = b; this.T = t;
    // Gegen Pool: H B T gegen Pool prallen lassen
    this.pool = [h, b, t];
    // Q = Quant Nutzung = wie viel vom Pool genutzt wird
    this.Q = (h + b + t) / 3;
    // F = Faktor = Q / 40 (HOME = 40)
    this.F = this.Q / 40;
    // D = Dimension = H B T zusammen = 3D, aber 1 Fach
    this.D = 3;
    return { H: h, B: b, T: t, pool: this.pool, Q: this.Q, F: this.F, D: this.D };
  },

  // CODEC — dekodieren
  decode(code){
    return { H: code.H, B: code.B, T: code.T, spruch: "H B T gegen Pool. Q Quant Nutzung. F Faktor. D Dimension." };
  },

  // PENTAGRAMM CODEC — 5 Ecken in Codec
  pentagrammCodec(){
    const ecken = ["OBEN","RECHTS OBEN","RECHTS UNTEN","LINKS UNTEN","LINKS OBEN"];
    return ecken.map((e, i) => this.encode(i+1, 5-i, i*90));
  },

  // PRIMATIEREN — sogar primatieren, einfach
  primatieren(){
    // Primat = einfachste Form, 1 Fach, 1 Codec
    return this.encode(40, 40, 40);
  },

  // KOLLIERENDE BESTE — Beste kollidiert, bleibt Beste
  kollidieren(a, b){
    // a gegen b, Beste gewinnt, aber beide bleiben
    const beste = Math.max(a.Q || a, b.Q || b);
    return { beste, spruch: "Kollidierende Beste. Easy going. Beide bleiben, Beste oben." };
  },

  urteil(){
    return { halt: "ZIEL", H: this.H, B: this.B, T: this.T, pool: this.pool, Q: this.Q, F: this.F, D: this.D, home: 40, mitte: 41, respo: 360, spruch: "Nur H B T gegen Pool. Q Quant Nutzung. F Faktor. D Dimension. Einfach. Easy going." };
  }
};
// Benutzen:
// HBTCodec.encode(40, 41, 90)
// HBTCodec.pentagrammCodec()
// HBTCodec.primatieren()
