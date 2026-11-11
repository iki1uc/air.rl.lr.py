main.axiom.html
  → zeigt die Raute, 14 Knoten, quer + diagonal
  → ruft STEP.js

STEP.js
  → sagt, welcher Schritt als Nächstes kommt
  → STEP 0 = ◉ ROOT
  → STEP 1 = 3 KERN
  → STEP 2 = 9 RICHTUNG
  → STEP 3 = ◎ ORBIT-KERN
  → …
  → STEP 13 = 3 ↺ RÜCKLAUF

plugins/ctrl-bus.js
  → nimmt den Schritt und setzt ihn als CTRL-Patch
  → applyPatch({ dr: 81 }) für 81 ARBEIT
  → applyPatch({ fusion: { blitz: 1 } }) für Fusion
  → Hooks melden Fehler, schlucken sie nicht

main.board.html
  → zeigt, was der Bus gesetzt hat
  → Coverage 96 / 88 / 74 / 92 / 31 / 18, Balance 0.18 CRITICAL
  → HALT = OFFEN oder ZIEL
