---
marp: true
theme: default
paginate: true
backgroundColor: #1a1a1a
backgroundImage: url('file:pbg-desktop-wallpaper.png')
backgroundSize: cover
backgroundPosition: center
color: #fff
style: |
  section {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    padding: 60px;
  }

  h1 {
    font-size: 2em;
    text-align: center;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
  }

  h2 {
    font-size: 1.6em;
    text-align: center;
    margin-bottom: 0.5em;
    text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
  }

  p, li {
    font-size: 0.95em;
    line-height: 1.5;
  }

  blockquote {
    background: rgba(0,0,0,0.3);
    border-left: 5px solid #fff;
    padding: 20px;
    border-radius: 5px;
    font-style: italic;
    color: #fff;
  }

  code {
    background: rgba(0,0,0,0.5);
    padding: 2px 6px;
    border-radius: 3px;
  }

  pre {
    background: #1e1e1e;
    border-radius: 10px;
    padding: 20px;
    overflow: auto;
  }

  pre code {
    background: transparent;
    color: #d4d4d4;
    font-size: 0.9em;
    font-family: Consolas, 'Courier New', monospace;
  }

  pre code .hljs-comment,
  pre code .hljs-quote {
    color: #aaaaaa;
    font-style: italic;
  }

  pre code .hljs-string {
    color: #f1fa8c;
  }

  pre code .hljs-keyword {
    color: #8be9fd;
  }

  pre code .hljs-function .hljs-title {
    color: #50fa7b;
  }

  pre code .hljs-variable {
    color: #ffb86c;
  }

  pre code .hljs-number {
    color: #bd93f9;
  }

  pre code .hljs-operator {
    color: #ff79c6;
  }

  table {
    border-collapse: collapse;
    width: 100%;
    margin: 20px 0;
    background: rgba(0,0,0,0.4);
  }

  th {
    background: rgba(0,0,0,0.6);
    color: #fff;
    padding: 12px;
    text-align: left;
    border: 1px solid rgba(255,255,255,0.2);
    font-weight: bold;
  }

  td {
    background: rgba(0,0,0,0.3);
    color: #fff;
    padding: 12px;
    border: 1px solid rgba(255,255,255,0.2);
  }

  tr:hover td {
    background: rgba(255,255,255,0.1);
  }
  
---

# 🎮 Pygame Zero

## 🌑 Stranger Stars – Salva il tuo personaggio!

💻 **III Liceo Scientifico Biella - Scienze Applicate**
🐍 **Python Biella Group**

---

## Perché questo gioco?

🎯 Con questo gioco vedremo:

* gestione del **mouse** per cliccare i personaggi (come per l'Alieno)
* creazione e movimento di più **Actor**
* logica dei **livelli** con difficoltà crescente
* gestione dello **stato di gioco** (scelta, gioco, game over)
* collisioni tramite **collidepoint()** (come per l'Alieno)
* animazioni con **oscillazione sinusoidale**

---

## Anteprima del gioco

<style scoped>
img { display: block; margin: 0 auto; }
</style>

![width:400px](./anteprima-gioco.png)

> Clicca il personaggio giusto tra quelli che cadono!
> Sopravvivi al Sottosopra e raggiungi il livello piu alto che puoi

---
## Configurazione iniziale

```python
from pgzero.actor import Actor
import pgzrun
import random, math

TITLE = "Stranger Stars"
COLORE_TESTO = (255, 255, 255)
WIDTH = 800
HEIGHT = 600
...
LISTA_PERSONAGGI = ["dustin", "lucas", "mike", "undici", "will"]
```
---
## Variabili di Stato

```python
gioco_terminato = False
livello_corrente = 1
fase_scelta_personaggio = True
personaggio_obiettivo = None 
personaggi_da_selezionare = [] 
lista_personaggi_in_gioco = []
modalita_sottosopra = False
timer_sottosopra = random.randint(
    TEMPO_MIN_SOTTOSOPRA, TEMPO_MAX_SOTTOSOPRA
)
```
---

## Schermata iniziale: scelta personaggio

```python
def mostra_schermata_scelta_personaggio():
    global personaggi_da_selezionare

    personaggi_da_selezionare = []
    spaziatura = WIDTH / (len(LISTA_PERSONAGGI) + 1)

    for indice, nome in enumerate(LISTA_PERSONAGGI):
        attore = Actor(nome)
        attore.x = (indice + 1) * spaziatura
        attore.y = HEIGHT / 2

        personaggi_da_selezionare.append(attore)

```

📌 I personaggi vengono disposti in fila e il giocatore sceglie chi salvare.

---

## Funzione `draw()` pt 1

```python
def draw():
    screen.clear()
    disegna_sfondo()

    if modalita_sottosopra:
        screen.blit("sfondo-sottosopra", (-200, -50))
    else:
        screen.blit("sfondo", (-150, -50))

```

Mostra sfondo, testo e personaggi in base allo **stato del gioco**.

---
## Funzione `draw()` pt 2: Scelta Personaggio

```python
if fase_scelta_personaggio:
        screen.draw.text(
            "Scegli il personaggio da salvare",
            center=(CENTRO_X, 100),
            fontsize=40,
            color="white",
        )
        for personaggio in personaggi_da_selezionare:
            personaggio.draw()
        return
```
---
## Funzione `draw()` pt 3: Interfaccia

```python
screen.draw.text(
        f"Livello: {livello_corrente}",
        topleft=(10, 10),
        fontsize=30,
        color="yellow",
    )

    screen.draw.text(
        f"Trova: {personaggio_obiettivo}",
        topright=(WIDTH - 10, 10),
        fontsize=25,
        color="lightblue",
    )

    if modalita_sottosopra:
        screen.draw.text(
            "BENVENUTI NEL SOTTOSOPRA!",
            center=(CENTRO_X, 50),
            fontsize=35,
            color="red",
        )

```
Mostra livello e obiettivo.

---
## Funzione `draw()` pt 4: Disegna Personaggi

```python
    for attore in lista_personaggi_in_gioco:
        attore.draw()

        if attore.image == personaggio_obiettivo:
            screen.draw.circle((attore.x, attore.y), 40, (255, 255, 0))

```
Se è quello da trovare → cerchio giallo!
---
## Funzione `draw()` pt 5: Game Over

```python
if gioco_terminato:
    mostra_messaggio(
            "GAME OVER\nHai raggiunto il livello: " + str(livello_corrente),
            "Clicca per ricominciare...",
        )
    return
```

💀 Game Over se:

* clicchi il personaggio sbagliato
* un personaggio esce dallo schermo
---

## Funzione `update()` completa

```python
def update():
    global lista_personaggi_in_gioco, timer_sottosopra
    if fase_scelta or gioco_terminato:
        return

    if len(lista_personaggi_in_gioco)==0:
        lista_personaggi_in_gioco = genera_personaggi_in_caduta(livello)
        return

    muovi_personaggi()
    gestisci_timer_sottosopra()
```

Logica principale del gioco.

---
## Funzione `update()`: muovere gli actor

```python
def muovi_personaggi():
    for attore in lista_personaggi_in_gioco:
        muovi_verticalmente(attore)
        muovi_orizzontalmente(attore)
        controlla_bordi_orizzontali(attore)
        cambia_direzione_casuale(attore)
```

Il movimento degli actor è definito da 4 funzioni: due di movimento e due di controllo.

---

## Movimento verticale

```python
    if modalita_sottosopra:
        attore.y -= attore.velocita_y
            attiva_game_over()
    else:
        attore.y += attore.velocita_y
        if attore.y > HEIGHT + 80:
            attiva_game_over()
```

Nel Sottosopra il movimento dei personaggi è invertito!

---

## Oscillazione laterale

```python
    angolo = attore.timer * 0.1
    oscillazione = math.sin(angolo) * attore.oscillazione_max

    attore.x += attore.velocita_x + oscillazione

    attore.timer += 1
```

Movimento ondulato → più difficile cliccarli.

---
## Funzioni di controllo

```python
def controlla_bordi_orizzontali(attore):
    if attore.x < 0:
        attore.x = 0
        attore.velocita_x = -attore.velocita_x

    if attore.x > WIDTH:
        attore.x = WIDTH
        attore.velocita_x = -attore.velocita_x

def cambia_direzione_casuale(attore):
    if random.random() < 0.01:
        attore.velocita_x = random.randint(VELOCITA_LATERALE_MIN, VELOCITA_LATERALE_MAX)

```

---

## Click del mouse

```python
def on_mouse_down(pos):
    if fase_scelta:
        gestisci_scelta(pos)
    else:
        gestisci_click_durante_gioco(pos)
```

`collidepoint()` per capire su quale personaggio hai cliccato.

---

## Avanzamento livello

```python
def avanza_livello():
    livello += 1
    lista_personaggi = []
    modalita_sottosopra = False
```

Ogni livello → più personaggi e più veloci.

---

## Logica del Sottosopra

```python
def attiva_sottosopra():
    modalita_sottosopra = not modalita_sottosopra
```

Effetti:

* gravità invertita
* velocità aumentata
* posizioni ribaltate

---

## Game Over

```python
def attiva_game_over():
    gioco_terminato = True
```

Semplice e immediato.

---

## Reset del gioco

```python
def resetta_gioco():
    livello = 1
    gioco_terminato = False
    fase_scelta = True
```

Torna alla schermata iniziale.

---

## Struttura cartelle consigliata

```
stranger_stars/
│ gioco.py
│
├── images/
│   ├── dustin.png
│   ├── mike.png
│   ├── ...
│   ├── sfondo.png
│   └── sfondo-sottosopra.png
└── sounds/
    └── (se usati)
```

---

## Sfida 🤔

*Cosa succede se NON gestisci modalita_sottosopra nei movimenti?*

A) Personaggi invisibili
B) Oscillazione non funziona
C) La gravità non si inverte
D) Il gioco non parte

---

## Soluzione

👉 **Risposta: C**

Il Sottosopra funziona solo se invertiamo manualmente il movimento verticale.

---

## Possibili estensioni

💡 Idee per migliorare Stranger Stars:

* effetti sonori
* boss finale
* punteggio e classifica
* modalità "infinita"
* difficoltà personalizzabile

---

## 🌑 Hai imparato!

* gestione mouse
* oscillazioni sinusoidali
* logica livelli
* inversione gravità
* gestione stati

> "Il Sottosopra non è mai stato così programmabile!"

---

<style scoped>
img { display: block; margin: 0 auto; }
</style>

## Buon divertimento con Stranger Stars!

![width:300px](./pbg-qr-code.png)

---

## Approfondimento: Costanti del Sottosopra

```python
TEMPO_MIN_SOTTOSOPRA = 3
TEMPO_MAX_SOTTOSOPRA = 10
VELOCITA_SOTTOSOPRA_MULT = 1.3
```

📌 **Cosa significano?**

* Il Sottosopra si attiva ogni intervallo casuale tra 3 e 10 secondi.
* Quando arriva, i personaggi diventano **il 30% più veloci**.
* Rende il gioco meno prevedibile e più difficile.

---

## Approfondimento: Velocità dei personaggi

```python
attore.velocita_base = random.uniform(
    livello_corrente * VELOCITA_BASE_MIN,
    livello_corrente * VELOCITA_BASE_MAX
)
```

🎓 **Spiegazione didattica:**

* La velocità aumenta con il livello.
* Ogni livello moltiplica la velocità minima e massima.
* Risultato: livelli alti = personaggi rapidissimi!

---

## Oscillazione: perché usare `math.sin()`?

```python
osc = math.sin(attore.timer * 0.1) * attore.oscillazione_max
```

🧠 **La sinusoide produce:**

* movimento morbido
* variazione continua
* effetto ondeggiante
* imprevedibilità

> È la stessa matematica usata in animazioni, onde, audio e oscillatori.

---

## Rimbalzo ai bordi

```python
if attore.x < 0:
    attore.x = 0
    attore.velocita_x = -attore.velocita_x
```

📌 Serve a evitare che i personaggi escano dallo schermo.
📌 Il rimbalzo rende l’animazione più naturale.

---

## Cambio direzione casuale

```python
if random.random() < 0.01:
    attore.velocita_x = random.randint(-3, 3)
```

🎲 1% di probabilità ad ogni frame.

* Aggiunge caos.
* Evita movimenti troppo “perfetti”.
* Rende il gioco meno memorizzabile.

---

## Come funziona il timer del Sottosopra

```python
timer_sottosopra -= 1/60
```

⏱️ Perché 1/60?

* update() viene chiamato **60 volte al secondo**.
* Ogni chiamata togliamo 1/60.
* Dopo ~60 chiamate → 1 secondo.

È una forma di *cronometro senza usare clock.schedule()*.

---

## Generare i personaggi corretti

```python
def scegli_personaggi_livello(num_extra):
    lista = [personaggio_obiettivo]
    altri = [p for p in LISTA_PERSONAGGI if p != personaggio_obiettivo]
    for _ in range(num_extra):
        lista.append(random.choice(altri))
```

🧩 **Cosa fa?**

* Garantisce che il personaggio da cliccare sia presente.
* Aggiunge “falsi” per aumentare difficoltà.

---

## Gestione scelta iniziale

```python
if attore.collidepoint(pos):
    personaggio_obiettivo = attore.image
    fase_scelta_personaggio = False
```

👌 Semplice e intuitivo:

* clic = immagine selezionata
* si passa allo stato “gioco”

---

## Gestione click durante il gioco

```python
if attore.image == personaggio_obiettivo:
    avanza_livello()
else:
    attiva_game_over()
```

⚠️ **Due soli casi:**

1. Giusto → avanti
2. Sbagliato → game over

---

## Avanzamento livello

```python
livello_corrente += 1
lista_personaggi_in_gioco = []
modalita_sottosopra = False
```

🔄 Resetta tutto per il prossimo round.
🎚️ Difficoltà cresce automaticamente.

---

## Ribaltamento verticale

```python
nuova_y = HEIGHT - attore.y
attore.y = nuova_y
```

🌑 Effetto “mondo invertito”:

* y = 100 → y = 500
* y = 400 → y = 200

Così i personaggi “saltano” dall’altro lato dello schermo!

---

## Messaggi centrali

```python
mostra_messaggio(titolo, sottotitolo)
```

Usato per:

* game over
* vittoria
* restart

📌 Semplifica la gestione del testo.

---

## Come appare graficamente il Sottosopra?

* sfondo rosso/scuro
* testo di avviso
* gravità invertita
* velocità aumentata
* personaggi ribaltati

📘 Ottimo esempio di **modalità di gioco alternativa**.

---

## Ciclo finale

```python
mostra_schermata_scelta_personaggio()
pgzrun.go()
```

✨ Pygame Zero gestisce il loop:

* draw()
* update()
* on_mouse_down()

Tu devi solo scrivere la logica.
