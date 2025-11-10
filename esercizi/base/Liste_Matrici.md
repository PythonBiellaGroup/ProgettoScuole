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

# Esercizi su liste e matrici

<br>
<br>

**Livello BASE**
🐍 **Python Biella Group**

---

## 🛒 Esercizio 1: La Lista della Spesa Infinita 

**Scenario:** Sei al supermercato con tua nonna che ha una memoria... creativa. Continua ad aggiungere cose alla lista mentre fate la spesa!

**Istruzioni:**
Scrivi un programma che:
1. Crea una lista vuota chiamata `carrello`
2. Usa un ciclo `while` per chiedere all'utente di inserire prodotti da comprare
3. Aggiunge ogni prodotto al carrello
4. Si ferma solo quando l'utente scrive "basta" (nonna finalmente soddisfatta!)
5. Alla fine stampa tutti i prodotti acquistati e il totale degli articoli

---

<br>

**Esempio di output:**
```
Cosa mettiamo nel carrello? pasta
Cosa mettiamo nel carrello? nutella
Cosa mettiamo nel carrello? 10 pizze surgelate
Cosa mettiamo nel carrello? basta

=== SCONTRINO DELLA NONNA ===
1. pasta
2. nutella
3. 10 pizze surgelate
Totale articoli: 3
```
---

## 📚 Esercizio 2: Battaglia Navale... dei Voti! 

**Scenario:** Il professore ha una strana tabella con i voti di 4 studenti in 3 materie. Vuole sapere chi è il secchione supremo!

**Istruzioni:**
Data questa matrice di voti:
```python
voti = [
    [8, 7, 9],   # Mario
    [6, 5, 7],   # Luigi
    [10, 9, 10], # Peach (la secchiona)
    [7, 8, 8]    # Bowser (studia di nascosto)
]
studenti = ["Mario", "Luigi", "Peach", "Bowser"]
```

---

Scrivi un programma che:
1. Usa un ciclo `for` per calcolare la media di ogni studente
2. Stampa il nome di ogni studente con la sua media
3. Trova e stampa chi ha la media più alta (il secchione supremo!)

**Suggerimento:** Per ogni studente, usa un altro ciclo `for` per sommare i suoi voti!

---

## 🥐 Esercizio 3 — “Il Fornaio Distratto”

### Trama
Il fornaio Pasticcini ha preparato una lista di **brioches** con le quantità vendute in un giorno.  
Purtroppo… si è *dimenticato di sommare tutto!* 😅  
Aiutalo tu!

### Dati iniziali
```python
vendite = [12, 5, 8, 3, 10, 0, 6]  # quantità vendute nei 7 giorni
```

---

**Istruzioni:**
1. Usa un **ciclo `for`** per calcolare il totale delle brioches vendute.  
2. Calcola anche la **media giornaliera** (totale diviso per 7).  
3. Stampa il risultato in modo simpatico, ad esempio:
   ```
   Il fornaio ha venduto 44 brioches in una settimana!
   Media giornaliera: 6.29 brioches (approssimato)
   ```

---

## 🧟 Esercizio 4 — “L’Invasione dei Mostriciattoli"
<br>

### Trama
Hai una **matrice 3×3** che rappresenta un mini schermo di gioco.  
Ogni cella contiene un numero:  
- `0` = vuoto  
- `1` = c’è un **mostriciattolo! 👾**

### Dati iniziali
```python
campo = [
    [0, 1, 0],
    [1, 0, 1],
    [0, 0, 1]
]
```
---

<br>
<br>

**Istruzioni:**
1. Usa un **doppio ciclo `for`** per contare quanti mostriciattoli (`1`) ci sono in tutto il campo.  
2. Stampa:
   ```
   Mostriciattoli trovati: 4
   ```
3. Poi, stampa la posizione di ciascun mostriciattolo, ad esempio:
   ```
   Mostriciattolo a riga 0, colonna 1
   Mostriciattolo a riga 1, colonna 0
   ...
   ```
