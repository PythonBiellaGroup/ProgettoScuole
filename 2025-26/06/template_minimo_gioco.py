import pgzrun

# --- 1 & 5. DEFINIZIONE OGGETTI E PERSONAGGI ---
# Creiamo il protagonista, i nemici e gli ostacoli
protagonista = Actor('personaggio_principale', (400, 500))
nemico = Actor('nemico', (400, 100))
ostacoli = [] # Una lista per contenere più oggetti

# --- 2. STATI DEL GIOCO E VARIABILI ---
# Punteggio, vite e lo stato attuale (menu, gioco, game_over)
stato_gioco = "menu"
punteggio = 0
vite = 3

# --- 6. GRAFICA ---
def draw():
    screen.clear()
    
    if stato_gioco == "menu":
        screen.draw.text("PREMI INVIO PER INIZIARE", center=(400, 300))
        
    elif stato_gioco == "in_corso":
        # Disegniamo lo sfondo e i personaggi
        protagonista.draw()
        nemico.draw()
        screen.draw.text(f"Punti: {punteggio}", (10, 10))
        
    elif stato_gioco == "game_over":
        screen.draw.text("GAME OVER! Riprova.", center=(400, 300), color="red")

# --- 3 & 4. LOGICA E AZIONI ---
def update():
    global stato_gioco, punteggio, vite
    
    if stato_gioco == "in_corso":
        # MOVIMENTO (Input da tastiera)
        if keyboard.left:
            protagonista.x -= 5
        if keyboard.right:
            protagonista.x += 5
            
        # LOGICA DEL NEMICO
        nemico.y += 2
        
        # COLLISIONI (Cosa succede quando si toccano?)
        if protagonista.colliderect(nemico):
            vite -= 1
            nemico.pos = (400, 0) # Reset nemico
            
        # CONDIZIONI DI SCONFITTA
        if vite <= 0:
            stato_gioco = "game_over"

# --- INTERAZIONE ESTERNA ---
def on_key_down(key):
    global stato_gioco
    
    # Gestione dei cambi di stato
    if stato_gioco == "menu" and key == keys.RETURN:
        stato_gioco = "in_corso"
    
    # Esempio azione singola: Sparo
    if stato_gioco == "in_corso" and key == keys.SPACE:
        print("Sparo effettuato!")

pgzrun.go()