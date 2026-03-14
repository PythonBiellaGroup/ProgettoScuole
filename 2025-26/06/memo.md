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
      background: #f5f5f5;  /* Grigio molto chiaro, quasi bianco */
      border: 2px solid rgba(255,255,255,0.3);
  }

  pre code {
      color: #1a1a1a;  /* Nero */
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
## Esempio: MEMO

💻 **III Liceo Scientifico Biella - Scienze Applicate**
🐍 **Python Biella Group**


---

### 1. Tema e personaggi

MEMO è un gioco senza personaggi. Il tema è la memoria visiva: il giocatore deve ricordare la posizione di carte colorate coperte e trovarne le coppie, ad esempio 6. Non c'è protagonista né nemici — l'unico "avversario" è la propria memoria.

---

<br>

### 2. Stati del gioco

**Inizio** — le carte sono sul tavolo, tutte coperte. Il contatore errori è visibile.

![width:300px](./memo_start.png)

---

<br>

### 2. Stati del gioco

**Gioco in corso** — le carte sono sul tavolo, il giocatore sta cercando le coppie. Il contatore errori è visibile.

![width:300px](./memo_playing.png)

---

<br>

### 2. Stati del gioco

**Vittoria** — tutte e 6 le coppie sono state trovate. Appare un overlay scuro con il messaggio di congratulazioni, il numero di errori commessi e il suggerimento per ricominciare.

![width:300px](./memo_end.png)

---

<br>

### 3. Come si vince e come si perde

**Tipo di gioco:** a obiettivi — bisogna completare un'azione precisa (trovare tutte le coppie).

**Condizione di vittoria:** tutte le 12 carte sono state abbinate correttamente (6 coppie trovate).

**Condizione di sconfitta:** non esiste in questa versione. Il giocatore non può perdere; l'unica "penalità" è l'incremento del contatore errori ogni volta che sceglie due carte diverse. L'obiettivo implicito è finire con il minor numero di errori possibile.

**Livelli:** versione singola, nessuna progressione di difficoltà. Un'estensione possibile sarebbe aumentare il numero di coppie o ridurre il tempo di visibilità delle carte sbagliate.

---

<br>

### 4. Azioni del giocatore

Il giocatore interagisce esclusivamente con il **mouse** e la **tastiera**:

- **Click del mouse su una carta** → la carta si scopre mostrando il suo colore
- **Click su una seconda carta** → confronto automatico con la prima
  - Se i colori coincidono → le carte restano scoperte (coppia trovata)
  - Se i colori sono diversi → le carte si riscoprono dopo una breve pausa, errori +1
- **Tasto Spazio** (solo a fine partita) → avvia una nuova partita

---

<br>
<br>

### 5. Oggetti del gioco - Carta (elemento principale)

| Aspetto | Dettaglio |
|---|---|
| Cosa fa | Mostra o nasconde il suo colore in base allo stato |
| Come si muove | Non si muove — posizione fissa su una griglia 6×2 |
| Stati possibili | coperta / scoperta (temporaneamente) / trovata (definitivamente) |
| Collisione | Non c'è collisione fisica; il "contatto" è il click del mouse sull'area rettangolare della carta |

---

<br>

### 5. Oggetti del gioco

**Contatore errori** — testo che si aggiorna ogni volta che una coppia sbagliata viene selezionata. Diventa rosso non appena si commette il primo errore.

**Overlay di vittoria** — pannello che appare sopra tutto quando tutte le coppie sono scoperte, mostrando il risultato finale.

---

<br>

### 6. Grafica

**Sfondo:** rettangolo pieno di colore uniforme

**Carte coperte:** rettangolo più chiaro per suggerisce una carta da gioco generica.

**Carte scoperte:** rettangolo del colore della coppia (rosso, azzurro, verde, giallo, viola, arancione)

---

<br>

### 6. Grafica

**Testo:** titolo "MEMO" in alto a sinistra chiaro; contatore errori al centro in alto

**Nessuna immagine esterna necessaria** — tutta la grafica può essere disegnata con le primitive di Pygame Zero

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
