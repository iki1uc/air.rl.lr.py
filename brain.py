# VORBEREITUNG — nur kopieren, nicht ausführen müssen
BRAIN = {
    "form": [1,1,1, 1,0,1, 0,0,1],
    "kern": ['A-Q','TRI','NC','FLY','ESS','GEO'],
    "gaps": ['r2c2','r3c1','r3c2'],
    "layers": ['META','KERN','VARIANTE','BSP','DATEN'],
}

# WICHTIG — getrennt, sonst wieder Mist:
HOME_STATE = 40.0   # Temperatur-Ziel
HOME_NODE  = "GEO"  # Struktur-Mitte

# Regel für alle 4 Tabs:
# ALT bleibt Wurzel, NEU ordnet sich unter
# f(f(x)) = f(x)  — nur für HOME
