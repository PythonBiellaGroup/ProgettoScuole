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
## 🎵 Tony alla ricerca della musica

💻 **III Liceo Scientifico Biella - Scienze Applicate**  
🐍 **Python Biella Group**

---

# Perché questo gioco?

🎯 In questo progetto impariamo:

- movimento manuale tramite **tastiera**  
- gestione dello **stato del gioco**  
- timer e **clock.schedule()**  
- collisioni con **colliderect()**  
- aggiornamento degli sprite (immagini)
- suoni, punteggi, game over  

Tutto in poche righe.

---

# Anteprima del gioco

<style scoped>
img {
  display: block;
  margin: -10px auto 0 auto;
}
</style>

![width:500px](./gioco-anteprima.png)

<br>

> Tony deve raccogliere quante più note musicali possibili prima che scada il tempo!

---

# Il codice completo (parte 1)

```python
from pgzero.actor import Actor
from pgzero.clock import clock
from pgzero.keyboard import keyboard
import pgzrun
from random import randint

TITLE = "tony alla ricerca della musica"
WIDTH = 600
HEIGHT = 500

punteggio = 0
ha_preso_nota = False
game_over = False
````

---

# Il codice completo (parte 2)

```python
tony = Actor("tony")
tony.pos = 100, 100

nota = Actor("nota musicale")

def draw():
    screen.blit("sfondo", (0, 0))
    nota.draw()
    tony.draw()
    screen.draw.text("Note imparate: " + str(punteggio),
                     color="black", topleft=(10, 10))

    if game_over:
        screen.fill("pink")
        screen.draw.text(
            "Tempo scaduto! Note messe insieme: " + str(punteggio),
            midtop=(WIDTH / 2, 10),
            fontsize=40,
            color="red",
        )
```

---

# Il codice completo (parte 3)

```python
def piazza_nota():
    nota.x = randint(70, (WIDTH - 70))
    nota.y = randint(70, (HEIGHT - 70))

def tempo_scaduto():
    global game_over
    game_over = True

def torna_concentrato():
    tony.image = "tony"
```

---

# Il codice completo (parte 4)

```python
def update():
    global punteggio

    if keyboard.left:
        tony.x -= 5
    if keyboard.right:
        tony.x += 5
    if keyboard.up:
        tony.y -= 5
    if keyboard.down:
        tony.y += 5

    nota_presa = tony.colliderect(nota)

    if nota_presa:
        punteggio += 10
        tony.image = "tony2"
        sounds.tonyaudio2.play()
        piazza_nota()
        clock.schedule(torna_concentrato, 1.0)

piazza_nota()
clock.schedule(tempo_scaduto, 10.0)
pgzrun.go()
```

---

# Come funziona Actor.move?

![width:600px](./schema-coordinate.png)

* `(0, 0)` è **in alto a sinistra**
* X aumenta → destra
* Y aumenta → in basso

`tony.x += 5` → Tony si muove a destra
`tony.y -= 5` → Tony sale

---

# Movimento con keyboard

```python
if keyboard.left:
    tony.x -= 5
```

📌 **Didattica**:

* La tastiera è un *oggetto globale* gestito da Pygame Zero
* Ogni frame viene controllato se un tasto è premuto
* `update()` gira ~60 volte al secondo

---

# Collisioni: collidepoint vs colliderect

![width:700px](./collide-points.png)

### Nel nostro gioco usiamo:

```python
nota_presa = tony.colliderect(nota)
```

✔️ controlla se i due rettangoli si sovrappongono
✔️ perfetto per sprite “regolari”

---

# Punteggio: gestione dello stato

```python
punteggio += 10
```

📌 Concetti didattici:

* Lo **stato del gioco** è l’insieme delle variabili che descrivono cosa sta succedendo
* Variabili come `punteggio`, `game_over`, `tony.image` rappresentano lo stato
* `update()` lo modifica
* `draw()` lo rappresenta sullo schermo

---

# Clock: programmare il futuro 🔮

Utilizziamo tre funzioni del clock:

---

## 1️⃣ `clock.schedule_interval()`

Chiama una funzione ogni tot secondi.
Non serve in questo gioco, ma è fondamentale per animazioni periodiche.

---

## 2️⃣ `clock.schedule()`

```python
clock.schedule(torna_concentrato, 1.0)
```

❗ significa:

> “tra un secondo, torna all’immagine originale”.

---

## 3️⃣ `clock.schedule(tempo_scaduto, 10.0)`

Dopo 10 secondi → **game over**

💡 *Il clock è uno strumento formidabile per creare giochi a tempo.*

---

# Game Over: come funziona davvero?

```python
if game_over:
    screen.fill("pink")
    screen.draw.text("Tempo scaduto!", ...)
```

🧠 Concetti didattici:

* Non esiste un “blocco del gioco”
* Semplicemente: **non raccogli più note**
* E `draw()` mostra un layout alternativo
* È una macchina a stati molto semplice

---

# Suoni: feedback immediato

```python
sounds.tonyaudio2.play()
```

💬 Didattica:

* Pygame Zero carica automaticamente i suoni da `/sounds/`
* Retroazione immediata = miglior esperienza utente
* Utile per gamification e motivazione

---

# Posizionamento casuale della nota

```python
nota.x = randint(70, WIDTH - 70)
```

🎯 Perché ±70?

* evita che la nota finisca mezzo fuori schermo
* centrato sulla dimensione dell’immagine (es. 128 px)

---

# Sfida 🤔

*Cosa succede se togli `clock.schedule(tempo_scaduto, 10.0)`?*

A) Il gioco non parte
B) Non finisce mai
C) Succede un bug grafico
D) Tony diventa immortale

---

# Soluzione

**Risposta: B!**

Senza il timer il gioco continua all’infinito.
Ottimo per Tony, meno per la didattica.

---

# Debugging tips 🐛

* Tony non si muove → controlla `keyboard`
* La nota non si vede → immagine mancante
* Suono non parte → file audio errato
* Il gioco “non finisce” → timer non schedulato

---

# Struttura consigliata delle cartelle

```
tony_musica/
│
├── gioco.py
├── images/
│   ├── tony.png
│   ├── tony2.png
│   ├── nota musicale.png
│   └── sfondo.png
└── sounds/
    ├── tonyaudio2.wav
```

---

# Conclusione

Hai imparato:

* Movimento a tastiera
* Collisioni con Actor
* Clock e timer
* Gestione dello stato
* Grafica, suoni, punteggio

> “Programmare giochi è il modo più divertente per capire la logica.”


