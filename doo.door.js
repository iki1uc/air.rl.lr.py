// doo.door.js — 2x · einmal JS · einmal HTML · TIME TUNNEL
// Partner zu time.tunnel.html
// 2x = JS + HTML = 1 Fach
// DOO DOOR = Tür auf Tür zu · TIME TUNNEL

export const DooDoor = {
  name: "DOO DOOR · TIME TUNNEL",
  dir: 1, // 1 = VOR · -1 = ZURÜCK
  on: true,
  t: 0,
  vor(){ this.dir = 1; this.on = true; return "VOR"; },
  zur(){ this.dir = -1; this.on = true; return "ZURÜCK"; },
  stop(){ this.on = false; return "STOP"; },
  tick(){ if(this.on) this.t += this.dir * 4; return this.t; },
  time(){
    const a = 9 + Math.floor(this.t/100)%90;
    const b = 99 + Math.floor(this.t/50)%900;
    const c = 999 - Math.floor(this.t/10)%900;
    return a + " : " + b + " : " + c;
  },
  door(){
    // 3x Tür: 1x zu · 2x halb · 3x auf
    const m = ((Math.floor(this.t/100)%3)+3)%3 + 1;
    return m === 1 ? "1x TÜR ZU" : m === 2 ? "2x HALB" : "3x TÜR AUF";
  }
};
// Benutzen in time.tunnel.html:
// import { DooDoor } from "./doo.door.js"
// DooDoor.vor() · DooDoor.zur() · DooDoor.stop() · DooDoor.time()
