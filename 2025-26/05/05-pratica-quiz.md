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

# 🤖 Quizzone - il codice per vincere
## Game Design & Data Analysis con Pygame Zero

💻 **III Liceo Scientifico Biella - Scienze Applicate**
🐍 **Python Biella Group**

---

## 🎯 Obiettivi del Progetto

In questa lezione analizzeremo un sistema di **Quiz Evoluto** che integra:

1.  **Manipolazione Dati**: Utilizzo di `Polars` e `csv` per la lettura ed il salvataggio dei dati in un csv.
2.  **Nuova Gestione Stati di Gioco**: Gestione della fase di input (Nickname) e del Game Loop.
3.  **Analisi del Tempo**: Misurazione del tempo di risposta in millisecondi tramite il delta-time (`dt`).

---

## 📊 Polars: Caricamento e Shuffle

Leggiamo i dati in modo casuale usando **Polars**.

```python
def carica_e_mischia():
    # Caricamento ultra-veloce del CSV
    df = pl.read_csv("domande.csv", truncate_ragged_lines=True)
   
    # Rimescolamento dell'intero DataFrame (fraction=1.0)
    df_shuffled = df.sample(fraction=1.0, shuffle=True)
   
    # Conversione in lista di dizionari per Pygame Zero
    lista_domande = df_shuffled.to_dicts()

```
---

## ⏱️ La Fisica del Tempo: `update(dt)`

Il gioco distingue tra due tipi di tempo:

1. **Tempo Logico (`tick`)**: Scandisce i secondi del timer (es. 15 secondi per rispondere).
2. **Tempo Reale (`update`)**: Misura quanto è stato veloce il giocatore.

```python
def update(dt):
    global millisecondi_trascorsi
    if not game_over and not entering_name:
        # dt è il tempo (frazione di secondo) tra due frame
        millisecondi_trascorsi += int(dt * 1000)

```

Il calcolo della barra del timer usa una proporzione lineare:


---

## ⌨️ Gestione Input: Nickname

Il gioco inizia in uno stato di "attesa input". Usiamo l'evento `on_key_down` per costruire una stringa dinamica:

```python
if entering_name:
    if key == keys.BACKSPACE:
        nome_utente = nome_utente[:-1] # Rimuove l'ultimo carattere
    elif key == keys.RETURN:
        start_game() # Passa alla fase di gioco
    else:
        # Aggiunge il carattere digitato
        nome_utente += key.name

```
---

## ⌨️ Le fasi di gioco
### Struttura degli Stati

* `entering_name = True`: Menu iniziale.
* `entering_name = False`: Quiz attivo.
* `game_over = True`: Schermata risultati.

---

## 💾 Salvataggio Risposte

Il cuore del progetto è la **persistenza dei dati**. Ogni risposta viene salvata in un file unico per giocatore: `nome_risposte.csv`.

| nome_utente | id_domanda | numero_risposta | tempo_risposta (ms) |
| --- | --- | --- | --- |
| ... | 42 | 2 | 1450 |
| ... | 12 | 1 | 890 |

```python
def salva_risposta(nome, id_domanda, numero_risposta, tempo_risposta):
    with open(nome_file_risposte, mode="a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([nome, id_domanda, numero_risposta, tempo_risposta])
```

---

## 🎨 UI: Styled Rectangles & Textbox

Per ottenere un look migliore, il codice utilizza una funzione di disegno personalizzata per creare un effetto ombra:

```python
def draw_styled_rect(rect, color):
    # Disegna l'ombra (spostata di 4 pixel)
    screen.draw.filled_rect(Rect(rect.x + 4, rect.y + 4, rect.w, rect.h), COLOR_SHADOW)
    # Disegna il rettangolo principale
    screen.draw.filled_rect(rect, color)

```

**`screen.draw.textbox`**: Uno strumento potente di Pygame Zero che adatta automaticamente il testo all'interno di un `Rect`, gestendo a capo e centraggio.

---

## 🔍 Logica di Navigazione (Collisioni)

Quando l'utente clicca, dobbiamo capire **quale** opzione ha scelto. Usiamo un ciclo `enumerate` sulla lista di `answer_boxes`:

```python
def on_mouse_down(pos):
    for i, box in enumerate(answer_boxes):
        if box.collidepoint(pos):
            numero_risposta = i + 1
            salva_risposta(nome_utente, id_domanda, numero_risposta, tempo_ms)
            prossima_domanda()
```
> **Nota**: Il sistema è progettato per essere "cieco". Non sa se la risposta è corretta; l'analisi della correttezza verrà fatta in una fase di **Post-Processing** sui dati salvati.

---

## 🚀 Possibili Evoluzioni


1. **Analisi Real-time**: Usa Polars durante il `game_over` per calcolare la media dei tempi di risposta e mostrarla al giocatore.
2. **Effetti Sonori**: Aggiungi un feedback audio per il click o per il tempo che scorre (tic-toc).
3. **Difficoltà Dinamica**: Accorcia `TEMPO_DOMANDA` man mano che il giocatore procede.

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
