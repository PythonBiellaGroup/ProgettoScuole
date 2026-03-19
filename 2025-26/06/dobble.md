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

  .two-col {
    display: flex;
    align-items: flex-start;
    gap: 28px;
  }

  .col-text {
    flex: 1 1 64%;
  }

  .col-image {
    flex: 0 0 32%;
    display: flex;
    justify-content: center;
    align-items: flex-start;
  }

  .col-image img {
    width: 100%;
    max-width: 320px;
    height: auto;
  }
---

# Progetta il tuo gioco
## Esempio: DOBBLE

**III Liceo Scientifico Biella - Scienze Applicate**  
**Python Biella Group**

---

# 1. Tema e personaggi

<div class="two-col">
<div class="col-text">

DOBBLE e' un gioco di osservazione e velocita'.

- Non ci sono personaggi da muovere nello spazio.
- Il protagonista e' il giocatore, che deve osservare due carte piene di simboli.
- La sfida consiste nel trovare il simbolo uguale presente su entrambe le carte.
- Il ritmo deve essere rapido: il gioco deve dare la sensazione di una prova di attenzione e riflessi.

**Idea chiave:** il divertimento nasce dalla capacita' di riconoscere in fretta il collegamento corretto tra due insiemi di simboli.

</div>
<div class="col-image">
<img src="./dobble_cover_intro.png" alt="Copertina Dobble">
</div>
</div>

---

# 2. Stati del gioco

<div class="two-col">
<div class="col-text">

Il gioco puo' essere diviso in momenti chiari:

- **Menu iniziale:** mostra il titolo, spiega in poche righe cosa bisogna fare e invita a iniziare.
- **Gioco in corso:** il giocatore vede due carte, le informazioni utili della partita e puo' selezionare un simbolo.
- **Vittoria:** appare quando il giocatore raggiunge l'obiettivo richiesto.
- **Game Over:** appare quando il giocatore non ha piu' possibilita' di continuare.

Ogni stato deve essere facile da riconoscere a colpo d'occhio, sia nei colori sia nei messaggi.

</div>
<div class="col-image">
<img src="./dobble_menu.png" alt="Menu Dobble">
</div>
</div>

---

# 3. Condizioni di vittoria e sconfitta

<div class="two-col">
<div class="col-text">

Come si vince:

- Il giocatore deve accumulare un certo numero di risposte corrette.
- Ogni volta che individua il simbolo comune, ottiene un punto e passa a una nuova coppia di carte.

Come si perde:

- Se seleziona un simbolo sbagliato, perde una vita.
- Se non risponde entro il tempo disponibile per il round, perde una vita.
- Quando le vite finiscono, la partita termina.

Il gioco deve quindi combinare tre elementi:

- osservazione
- precisione
- gestione del tempo

</div>
<div class="col-image">
<img src="./dobble_game_over.png" alt="Game Over Dobble">
</div>
</div>

---

# 4. Le azioni del giocatore

<div class="two-col">
<div class="col-text">

L'interazione principale e' semplice e immediata:

- osservare le due carte
- confrontare i simboli presenti
- cliccare il simbolo che compare su entrambe

Il gioco deve restituire subito un feedback:

- se la scelta e' corretta, il giocatore avanza
- se la scelta e' sbagliata, subisce una penalita'
- se il tempo scade, il round viene considerato perso

L'obiettivo dell'interfaccia e' far capire tutto in pochi secondi, senza comandi complessi.

</div>
<div class="col-image">
<img src="./dobble_gioco.png" alt="Partita Dobble">
</div>
</div>

---

# 5. Definire gli oggetti del gioco

Gli elementi fondamentali sono:

- **Due carte di gioco:** ciascuna contiene un insieme di simboli.
- **Simboli:** immagini o icone facilmente distinguibili tra loro.
- **Timer del round:** indica quanto tempo resta per rispondere.
- **Punteggio:** mostra i successi ottenuti.
- **Vite:** rappresentano gli errori ancora concessi.
- **Messaggi di feedback:** comunicano se la risposta e' corretta, sbagliata o se il tempo e' terminato.
- **Pulsanti:** servono per iniziare una nuova partita o rigiocare.

Regola fondamentale del design del round:

- tra le due carte deve esserci sempre uno e un solo simbolo in comune

Questo e' il cuore del gioco, indipendentemente da come verra' implementato.

---

# 6. Pensare alla grafica

<div class="two-col">
<div class="col-text">

La grafica deve aiutare la lettura rapida:

- sfondo semplice e ordinato
- due carte ben separate e bilanciate nello schermo
- simboli grandi e riconoscibili
- area informativa con tempo, vite e punteggio
- colori diversi per distinguere menu, partita, vittoria e sconfitta

Conviene progettare anche queste schermate:

- una schermata iniziale con regole essenziali
- una schermata finale di vittoria
- una schermata finale di sconfitta

La grafica non deve distrarre: deve rendere immediata la ricerca del simbolo comune.

</div>
<div class="col-image">
<img src="./dobble_vittoria.png" alt="Vittoria Dobble">
</div>
</div>

---

# Obiettivo del progetto

Chi dovra' realizzare questo gioco dovra' costruire una versione personale di DOBBLE che rispetti queste idee:

- confronto visivo tra due carte
- un solo simbolo comune per round
- risposte tramite selezione del giocatore
- punti, vite e tempo come regole principali
- schermate chiare dall'inizio alla fine della partita

L'implementazione concreta puo' cambiare, ma il funzionamento del gioco deve restare questo.

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

> *"C'e' sempre qualcosa da imparare per migliorarci e crescere... insieme!"*
