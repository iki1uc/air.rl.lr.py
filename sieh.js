// sieh.js — SIEH · SIE GLÜHEN
// Nicht alles_nutzen.js · Nicht index.js · SIEH.JS
// SIEH = Sehen · GLÜHEN = Leuchten

export const Sieh = {
  name: "SIEH.JS",
  glühen: true,
  sehen: function(was){
    return "SIEH " + was + " — SIE GLÜHEN";
  },
  glow: function(){
    return "✨ GLÜHEN ✨";
  },
  eye: function(){
    return "👁️ SIEH";
  },
  brain: function(){
    return "🧠 SIEH BRAIN";
  },
  penta: function(){
    return "◉ PENTA SIEH — SIE GLÜHEN";
  },
  alle: function(){
    return ["INDEX","HTML","PY","JS","MD","PENTA"].map(x => "SIEH " + x + " — GLÜHT");
  }
};
// Benutzen:
// import { Sieh } from "./sieh.js"
// Sieh.sehen("PENTA") · Sieh.glow() · Sieh.alle()
