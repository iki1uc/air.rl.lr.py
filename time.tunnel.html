<!doctype html>
<html lang="de"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>TIME TUNNEL · TUNNELN</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{background:#000;color:#e8f0ff;font-family:Consolas,monospace;text-align:center;overflow:hidden;height:100vh}
h1{position:fixed;top:14px;left:50%;transform:translateX(-50%);font-size:14px;letter-spacing:8px;color:#f0d080;z-index:10}
#sub{position:fixed;top:34px;left:50%;transform:translateX(-50%);font-size:10px;letter-spacing:3px;color:#8aa0b0;z-index:10}
canvas{position:fixed;inset:0;width:100%;height:100%}
#time{position:fixed;bottom:16px;left:50%;transform:translateX(-50%);font-size:22px;letter-spacing:6px;color:#5cf0ff;z-index:10}
#btns{position:fixed;bottom:52px;left:50%;transform:translateX(-50%);z-index:10}
button{background:#0a1420;color:#f0d080;border:1px solid rgba(240,208,128,.4);padding:8px 14px;border-radius:999px;cursor:pointer;font-family:inherit;letter-spacing:2px;margin:4px}
button.on{background:#f0d080;color:#000}
</style></head><body>
<h1>TIME TUNNEL</h1>
<div id="sub">TUNNELN · 9 99 999 · ZEIT FÄHRT</div>
<canvas id="c"></canvas>
<div id="btns"><button id="bVor" class="on">VOR ▶</button><button id="bZur">ZURÜCK ◀</button><button id="bStop">STOP</button></div>
<div id="time">9 : 99 : 999</div>
<script>
let c=document.getElementById("c"); let ctx=c.getContext("2d");
let W,H,cx,cy; let dir=1; let on=true; let t=0;
function resize(){ W=window.innerWidth; H=window.innerHeight; c.width=W; c.height=H; cx=W/2; cy=H/2; }
resize(); window.addEventListener("resize",resize);
function draw(){
  ctx.fillStyle="rgba(0,0,0,0.25)"; ctx.fillRect(0,0,W,H);
  let maxR=Math.max(W,H);
  for(let i=0;i<24;i++){
    let rr=((i*40 + t*2) % (maxR*0.8));
    let alpha=1 - rr/(maxR*0.8);
    ctx.strokeStyle="rgba(92,240,255,"+alpha+")";
    ctx.lineWidth=2;
    ctx.beginPath(); ctx.arc(cx,cy,rr,0,Math.PI*2); ctx.stroke();
    ctx.strokeStyle="rgba(240,208,128,"+(alpha*0.6)+")";
    ctx.beginPath(); ctx.arc(cx,cy,rr*0.92,0,Math.PI*2); ctx.stroke();
  }
  // Kern
  let coreR=20+Math.sin(t*0.05)*8;
  let g=ctx.createRadialGradient(cx,cy,0,cx,cy,coreR*4);
  g.addColorStop(0,"rgba(255,255,255,1)");
  g.addColorStop(0.4,"rgba(240,208,128,.8)");
  g.addColorStop(1,"rgba(0,0,0,0)");
  ctx.fillStyle=g; ctx.beginPath(); ctx.arc(cx,cy,coreR*4,0,Math.PI*2); ctx.fill();
  document.getElementById("time").textContent = (9 + Math.floor(t/100)%90) + " : " + (99 + Math.floor(t/50)%900) + " : " + (999 - Math.floor(t/10)%900);
  if(on) t+=dir*4;
  requestAnimationFrame(draw);
}
document.getElementById("bVor").onclick=()=>{dir=1;on=true;document.getElementById("bVor").classList.add("on");document.getElementById("bZur").classList.remove("on");document.getElementById("bStop").classList.remove("on");};
document.getElementById("bZur").onclick=()=>{dir=-1;on=true;document.getElementById("bZur").classList.add("on");document.getElementById("bVor").classList.remove("on");document.getElementById("bStop").classList.remove("on");};
document.getElementById("bStop").onclick=()=>{on=false;document.getElementById("bStop").classList.add("on");document.getElementById("bVor").classList.remove("on");document.getElementById("bZur").classList.remove("on");};
draw();
</script>
</body></html>
