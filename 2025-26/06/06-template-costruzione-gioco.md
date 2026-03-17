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
  
---

# 🎮 Progettare un Gioco in Python
## (Template per PyGame Zero)

💻 **Da un'idea al codice... passo dopo passo!**

---

# 1️⃣ Scegliere il Tema e i Personaggi

Chi sarà il protagonista della tua avventura? 🦸‍♂️

- **Un solo protagonista:** (es. il gioco dell'Alieno o di Tony Effe)
- **Più personaggi:** (es. il gioco di Stranger Things)
- **Eroi vs Nemici:** Una sfida epica (es. gioco di Harry Potter)
- **Nessun personaggio:** Un'interfaccia pura (es. un gioco a Quiz 🧠)

---

# 2️⃣ Definire gli Stati del Gioco

Come si evolve la partita dall'inizio alla fine? 🔄
Bisogna gestire i diversi "momenti" del gioco:

- 🏠 **Menu iniziale** (Schermata del titolo)
- 🕹️ **Gioco in corso** (L'azione vera e propria)
- ⏸️ **Pausa** (Per riprendere fiato)
- 🏆 **Vittoria** (Schermata di trionfo!)
- 💀 **Game Over** (Ritenta, sarai più fortunato)

---

# 3️⃣ Condizioni di Vittoria e Sconfitta

Come si vince? 🥇
- 💯 **A punteggio:** Si vince raggiungendo una soglia.
- ⏱️ **A tempo:** Devi resistere fino allo scadere del timer.
- 🎯 **A obiettivi:** Bisogna completare azioni specifiche.
- 📈 **A livelli:** Si passa da sfide facili a sfide più difficili.

Come si perde? 💔
- Perdita di tutte le **vite**
- **Tempo** scaduto prima dell'obiettivo

---

# 4️⃣ Le Azioni del Giocatore

Come interagisce l'utente con il mondo di gioco? ⌨️🖱️

Abbiamo diverse opzioni a disposizione:
- 🏃‍♂️ **Movimento:** Spostare il personaggio con le frecce.
- ⌨️ **Tastiera:** Premere tasti specifici per compiere azioni.
- 🖱️ **Mouse:** Click su pulsanti o nemici a schermo.
- 🤔 **Scelte:** Selezionare risposte o percorsi alternativi.

---

# 5️⃣ Definire gli Oggetti del Gioco

Quali elementi popolano il tuo mondo? 📦

- 🟢 **Giocatore** (L'avatar controllato dall'utente)
- 🔴 **Nemici** (Chi cerca di ostacolarti)
- 🧱 **Ostacoli / Muri** (Elementi dell'ambiente)

**Per ogni elemento chiediti:**
1. Cosa fa?
2. Come si muove?
3. Cosa succede se *collide* (sbatte) contro altri oggetti? 💥

---

# 6️⃣ Pensare alla Grafica

L'occhio vuole la sua parte! 🎨
Quali "assets" (risorse visive) ti servono?

- 🖼️ **Sfondo:** L'ambientazione del gioco.
- 👾 **Personaggi:** Sprite per eroi e nemici.
- 🗡️ **Oggetti / Prop:** Monete, armi, ostacoli.
- 💖 **Icone:** Per l'interfaccia (es. cuori per le vite).
- 📝 **Testo:** Font chiari per menu e punteggi.

---

# L'Anatomia di PyGameZsero
## I pezzi fondamentali del tuo codice

Dovrete sicuramente usare:

- **`draw()`**: Il pittore 🎨. Viene chiamata automaticamente per ridisegnare lo schermo. Qui usi `screen.clear()` e i metodi degli Actor.
- **`update()`**: Il cervello 🧠. Viene chiamata 60 volte al secondo. Qui gestisci la logica, il movimento e le collisioni (es. `alieno.x += 2`).

> **Ricorda:** In `draw()` si visualizza, in `update()` si calcola!
---

<br>
<br>
<br>

- **`on_key_down(key)`**: L'orecchio 👂. Si attiva solo nel momento esatto in cui premi un tasto. Ottimo per azioni singole (saltare, sparare).
- **`Actor("nome_immagine")`**: Il protagonista 🎭. Crea l'oggetto di gioco usando un'immagine dalla cartella `images`.
- **`screen.collidepoint()`**: Il sensore 💥. Controlla se il mouse o un oggetto ha toccato un punto specifico.
* **`on_mouse_down(pos, button)`**: L'orecchio 👂(pt 2).Gestisce i click del mouse. 
* **`animate(actor, pos=(x,y), duration=1)`**: La funzione "magica" ✨: muove un oggetto da dove si trova a una nuova posizione in modo fluido, senza dover scrivere calcoli complessi in `update`.
---
# 🚀 Pronti a programmare?

> *"Un buon gioco nasce prima sulla carta, e poi prende vita nel codice!"*

Ora che abbiamo il piano, apriamo l'editor e iniziamo a scrivere con **PyGame Zero**! 🐍🎮

---
<style scoped>
img {
  display: block;
  margin: 0 auto;
}
</style>

## Grazie per l'attenzione...

<br>

![width:300px](./pbg-qr-code.png)

> *"C'è sempre qualcosa da imparare per migliorarci e crescere…**insieme!**"*