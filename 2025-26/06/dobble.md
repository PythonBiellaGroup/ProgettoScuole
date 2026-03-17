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
      background: #f5f5f5;
      border: 2px solid rgba(255,255,255,0.3);
  }

  pre code {
      color: #1a1a1a;
  }

  pre code .hljs-comment,
  pre code .hljs-quote {
    color: #aaaaaa;
    font-style: italic;
  }

  pre code .hljs-string {
    color: #d73a49;
  }

  pre code .hljs-keyword {
    color: #0366d6;
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

# Progetta il tuo gioco
## Esempio: DOBBLE

💻 **III Liceo Scientifico Biella - Scienze Applicate**
🐍 **Python Biella Group**

---
<br>
<br>
<br>

### 1. Tema e personaggi

DOBBLE è un gioco senza personaggi. Il tema è il riconoscimento visivo rapido: il giocatore osserva due carte piene di simboli e deve trovare il simbolo uguale presente su entrambe. Non ci sono nemici che si muovono: la sfida è contro il tempo e contro i propri errori.

**Immagine suggerita:** schermata introduttiva con due carte e simboli colorati.

![width:380px](./dobble_cover_intro.png)

---

<br>
<br>

### 2. Stati del gioco

**Menu iniziale** — il titolo DOBBLE è visibile, ci sono le regole principali, un esempio con due carte e il pulsante START. Il gioco spiega già che bisogna cliccare il simbolo uguale tra le due carte. Il codice mostra questa schermata nello stato `menu` prima che la partita inizi.

![width:300px](./dobble_menu.png)

---

<br>
<br>

### 2. Stati del gioco

**Gioco in corso** — si vedono due carte principali, ognuna con 8 box cliccabili, il messaggio centrale, il numero del round, il punteggio, le vite e il tempo rimasto. Tutta la logica di partita attiva si trova nello stato `gioco`. fileciteturn3file0

![width:300px](./dobble_gioco.png)

---

<br>
<br>

### 2. Stati del gioco

**Vittoria** — quando il giocatore raggiunge il punteggio obiettivo, appare la schermata finale verde con il messaggio “HAI VINTO!” e il pulsante RIGIOCA. La vittoria viene attivata quando `punteggio >= PUNTEGGIO_OBIETTIVO`. fileciteturn3file0

![width:300px](./dobble_vittoria.png)

---

<br>
<br>

### 2. Stati del gioco

**Game Over** — se finiscono le vite, oppure se scade il tempo e non restano vite, il gioco passa allo stato `game_over`, mostrando il punteggio finale, un messaggio di errore e il pulsante RIGIOCA. fileciteturn3file0

![width:300px](./dobble_game_over.png)

---

<br>
<br>
<br>

### 3. Come si vince e come si perde

**Tipo di gioco:** misto tra gioco a obiettivi e gioco a tempo.

**Condizione di vittoria:** raggiungere **N punti**, cioè trovare correttamente N simboli uguali nei round proposti. Il valore può essere impostato in una costante, es. `PUNTEGGIO_OBIETTIVO = 8`. 


---

<br>
<br>
<br>

**Condizione di sconfitta:**
- perdere tutte le **3 vite**;
- sbagliare troppe volte;
- far scadere il tempo del round fino a consumare tutte le vite;
- terminare i round disponibili prima di arrivare al punteggio richiesto. fileciteturn3file0

**Livelli:** non ci sono livelli veri e propri; la difficoltà resta costante, ma la pressione cresce perché ogni round ha un timer di **30 secondi**.

---

<br>
<br>
<br>

### 4. Azioni del giocatore

Il giocatore interagisce esclusivamente con il **mouse**:

- **Click su START** → avvia la partita
- **Click su un box della carta sinistra o destra** → seleziona un simbolo
- **Se il simbolo è corretto** → il punteggio aumenta di 1 e parte un nuovo round
- **Se il simbolo è sbagliato** → si perde una vita e parte un nuovo round
- **Click su RIGIOCA** → riavvia la partita dalla schermata finale

---

<br>
<br>
<br>

### 5. Oggetti del gioco - Carta (elemento principale)

| Aspetto | Dettaglio |
|---|---|
| Cosa fa | Contiene 8 simboli tra cui può esserci quello uguale all'altra carta |
| Come si muove | Non si muove, resta fissa sullo schermo |
| Stati possibili | visibile nel menu / attiva durante il gioco |
| Collisione | Non c'è collisione fisica; il contatto è il click del mouse dentro uno dei box `Rect(...)` |


---

<br>
<br>

### 5. Oggetti del gioco

Le due carte principali sono `carta_sinistra` e `carta_destra`, ognuna suddivisa in 8 aree cliccabili.

**Box cliccabili** — sono le zone rettangolari interne alle carte. Ogni box contiene un simbolo e può ricevere il click del giocatore. Nel codice sono definiti con molti `Rect(...)` separati e raccolti in due liste: `box_carta_sinistra` e `box_carta_destra`.

**Barra superiore** — mostra titolo, round, punti, vite e tempo.

**Area messaggi** — mostra testi come “Trova il simbolo uguale.”, “Corretto!” o “Sbagliato!”.

**Pulsanti** — `START` nel menu e `RIGIOCA` nelle schermate finali.

---

<br>
<br>
<br>

### 6. Grafica

**Sfondo:** colore pieno diverso per ogni schermata:
- blu per il menu,
- azzurro per il gioco,
- verde per la vittoria,
- rosso scuro per il game over. fileciteturn3file0

**Carte:** grandi rettangoli bianchi affiancati.

**Simboli:** immagini già presenti nella cartella `images` con nomi come `sole`, `luna`, `pesce`, `robot`, `banana`. Quando un simbolo ha l'immagine, il gioco usa `screen.blit(...)`; altrimenti scrive il testo.

---

<br>

### 6. Grafica

**Testo:** molto importante per guidare il giocatore. Il codice usa etichette grandi e leggibili per titolo, regole, timer, punteggio e messaggi di stato.

**Immagini esterne utili:** in questa versione servono davvero, perché i simboli vengono mostrati come file immagine se disponibili nella cartella `images`. L'elenco include, tra gli altri, `sole`, `gatto`, `albero`, `luna`, `cane`, `treno`, `fiore`, `chiave`, `robot`, `banana`.

---

<br>
<br>

### 7. Struttura del codice

Il file segue una struttura semplice ma chiara:

- **Costanti iniziali** → dimensioni finestra, tempo round, vite iniziali, punteggio obiettivo
- **`Rect(...)`** → definiscono carte, pulsanti e box cliccabili
- **`draw_*()`** → disegnano le varie schermate
- **`on_mouse_down()`** → intercetta i click del giocatore
- **`controlla_risposta()`** → decide se il click è corretto o sbagliato
- **`update_secondi_mancanti()`** → gestisce il timer del round 

---

<br>
<br>

### 8. Esempio di round

Ogni round è già pronto dentro `rounds_raw` e contiene:
- 8 simboli per la carta sinistra
- 8 simboli per la carta destra
- 1 simbolo comune dichiarato esplicitamente

Esempio: una stringa contiene due gruppi separati da `|` e il terzo pezzo è il simbolo uguale. Poi il codice divide le stringhe con `split("|")` e `split(";")`.

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
