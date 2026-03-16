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


# 🐛 Debug Wars: La Vendetta dello StackTrace

**Ovvero: come sopravvivere agli errori Python senza lanciare il PC dalla finestra ma usando Thonny (il nostro fedele alleato)**

<br>

💻 **III Liceo Scientifico Biella - Scienze Applicate**
🐍 **Python Biella Group**

---

# 📋 Oggi imparerete ...

- Cos'è lo **stacktrace** e decifrarlo come veri hacker (spoiler: non è Matrix)
- Cos'è un **debugger** e usarlo come un detective digitale 🕵️
- A non urlare contro il computer quando il codice non funziona
- A capire che "ha funzionato al primo colpo" è un mito urbano

---

<!-- _class: lead -->

# PARTE I
## Lo StackTrace: Il Diario Segreto di Python

*"Caro diario, oggi l'umano ha sbagliato ancora..."*

---

# Cos'è uno StackTrace? 🤔

È il **messaggio d'errore** che Python ti lascia quando il tuo programma esplode.

**Pensalo come:**
- 📝 Una lettera d'addio molto dettagliata
- 🗺️ Una mappa del tesoro (dove X = il tuo errore)
- 🚨 Il rapporto della polizia dopo l'incidente
- 💥 La scatola nera di un aereo che racconta tutto ciò che è successo prima del crash

**Spoiler:** Python è MOLTO specifico.

---

## 🔍 CHALLENGE #1: Il Concatenatore Confuso

```python
def crea_messaggio_compleanno(nome, eta):
    """Crea un messaggio personalizzato di compleanno"""
    messaggio = "Buon compleanno " + nome + "!"
    messaggio = messaggio + " Oggi compi " + eta + " anni!"
    messaggio = messaggio + " Auguroni!"
    return messaggio

# Test
nome_festeggiato = "Mario"
anni = 18

risultato = crea_messaggio_compleanno(nome_festeggiato, anni)
print(risultato)
```

---

## 📋 STACKTRACE #1

```
Traceback (most recent call last):
  File "compleanno.py", line 12, in <module>
    risultato = crea_messaggio_compleanno(nome_festeggiato, anni)
  File "compleanno.py", line 4, in crea_messaggio_compleanno
    messaggio = messaggio + " Oggi compi " + eta + " anni!"
TypeError: can only concatenate str (not "int") to str
```

**Domanda**: Perché Python si rifiuta di unire le stringhe?

---

**Si legge dal BASSO verso l'ALTO!** ⬆️
❌ La parte più bassa dello stacktrace (l'errore più recente) è dove si è verificato il crash, quindi è il primo punto da esaminare.
🧠 Le righe superiori ti aiutano a capire come l'errore si è propagato e ti forniscono un contesto utile per il debug. Puoi risalire nel "flusso" delle chiamate fino a trovare il punto in cui il programma ha preso una piega sbagliata.

---

# 🔍 Decodifichiamo il Messaggio

```python
TypeError: can only concatenate str (not "int") to str
```
**↑ INIZIA DA QUI: Il tipo di errore e cosa è successo**

```python
  File "compleanno.py", line 4, in crea_messaggio_compleanno
    messaggio = messaggio + " Oggi compi " + eta + " anni!"
```
**↑ Dove è esploso tutto (file, riga, funzione)**

```python
Traceback (most recent call last):
  File "compleanno.py", line 12, in <module>
    risultato = crea_messaggio_compleanno(nome_festeggiato, anni)
```
**↑ Come ci siamo arrivati (la "catena di eventi")**

---

## 💡 SOLUZIONE #1

**Problema**: Stiamo cercando di concatenare una **stringa** con un **intero**!

Python non può fare `"Oggi compi " + 18` perché non sa se vuoi:
- `"Oggi compi 18"` (conversione automatica)
- `"Oggi compi " + "18"` (tutto stringa)

**Fix** (3 modi):
```python
# Metodo 1: Converti esplicitamente
messaggio = messaggio + " Oggi compi " + str(eta) + " anni!"

# Metodo 2: Usa f-string (il migliore!)
messaggio = f"{messaggio} Oggi compi {eta} anni!"

# Metodo 3: Usa format()
messaggio = messaggio + " Oggi compi {} anni!".format(eta)
```

**Lezione**: Python è **fortemente tipizzato**. Non mischia i tipi automaticamente!


---

---

## 🎮 MINI-CHALLENGE BONUS

Qual è l'output di questo codice?

```python
numero = "10"
risultato = numero * 3
print(risultato)
```

**A)** 30  
**B)** "101010"  
**C)** Errore  
**D)** "10 10 10"

*Pensa prima di rispondere...*

---

## ✅ RISPOSTA BONUS

**Risposta corretta: B) "101010"**

In Python:
- `"abc" * 3` → `"abcabcabc"` (ripete la stringa)
- `10 * 3` → `30` (moltiplica i numeri)

**Morale**: Il tipo di dato è TUTTO!

Se volevi `30`, dovevi fare: `int(numero) * 3`

---

---

## 🔍 CHALLENGE #2: L'Indice Ribelle

```python
def calcola_medie_mensili(temperature):
    """Calcola la media delle temperature per ogni mese"""
    medie = []
    
    # Ci sono 12 mesi nell'anno
    for mese in range(1, 13):
        media_mese = temperature[mese] / 30  # Circa 30 giorni al mese
        medie.append(media_mese)
    
    return medie

# Temperature totali per mese (ipotetico)
temp_mensili = [450, 480, 520, 580, 650, 720, 
                780, 770, 690, 600, 510, 460]

risultato = calcola_medie_mensili(temp_mensili)
print("Medie mensili:", risultato)
```

---

## 📋 STACKTRACE #2

```
Traceback (most recent call last):
  File "temperature.py", line 14, in <module>
    risultato = calcola_medie_mensili(temp_mensili)
  File "temperature.py", line 7, in calcola_medie_mensili
    media_mese = temperature[mese] / 30
IndexError: list index out of range
```

**Domanda**: Perché Python non riesce ad accedere a `temperature[mese]`?

*Indizio: Da dove partono gli indici delle liste in Python?*

---

## 💡 SOLUZIONE #2

**Problema**: `range(1, 13)` genera numeri da 1 a 12, ma gli indici della lista vanno da 0 a 11!

**Visualizziamo**:
```
Lista:   [450, 480, 520, ..., 460]
Indici:    0    1    2   ...  11   ← Vanno da 0 a 11!
Mese:      1    2    3   ...  12   ← range(1,13) genera 1-12
                                    ☠️ temperature[12] NON ESISTE!
```

**Fix**:
```python
# Metodo 1: Parti da 0
for mese in range(12):  # 0, 1, 2, ..., 11
    media_mese = temperature[mese] / 30

# Metodo 2: Sottrai 1
for mese in range(1, 13):
    media_mese = temperature[mese - 1] / 30
```

---

## 🤓 FUN FACT: Off-by-one errors

Gli errori di "off-by-one" sono così comuni che hanno un nome proprio!

**Le due regole fondamentali**:
1. Gli indici in Python partono da **0**
2. `range(n)` genera numeri da **0 a n-1** (non fino a n!)

**Trucco pro**: Disegna la lista su carta con gli indici numerati. Old school, ma funziona sempre!

---

## 🔍 CHALLENGE #3: Il Divisore Zero

```python
def calcola_media_classe(voti):
    """Calcola la media dei voti di una classe"""
    totale = 0
    
    for voto in voti:
        totale = totale + voto
    
    media = totale / len(voti)
    return media

# Test con diverse situazioni
print("Test 1 - Classe normale:")
classe_a = [7, 8, 6, 9, 7, 8]
print(f"Media: {calcola_media_classe(classe_a)}")

print("\nTest 2 - Classe dopo l'influenza:")
classe_b = []  # Tutti assenti!
print(f"Media: {calcola_media_classe(classe_b)}")
```

---

## 📋 STACKTRACE #3

```
Test 1 - Classe normale:
Media: 7.5

Test 2 - Classe dopo l'influenza:
Traceback (most recent call last):
  File "media.py", line 17, in <module>
    print(f"Media: {calcola_media_classe(classe_b)}")
  File "media.py", line 8, in calcola_media_classe
    media = totale / len(voti)
ZeroDivisionError: division by zero
```

**Domanda**: Cosa succede quando dividiamo per zero?

*Risposta breve: Python va in panico* 💥

---

## 💡 SOLUZIONE #3

**Problema**: Lista vuota → `len(voti) = 0` → divisione per zero → 🔥

**Matematicamente**: Non puoi dividere per zero! È impossibile!

**Fix**:
```python
def calcola_media_classe(voti):
    if len(voti) == 0:  # Controllo PRIMA di dividere
        print("Errore: nessun voto da calcolare!")
        return 0  # O restituisci None, o solleva un errore
    
    totale = 0
    for voto in voti:
        totale = totale + voto
    
    media = totale / len(voti)
    return media
```

**Lezione**: **Sempre** controllare le liste vuote prima di fare operazioni!

---

## 🎯 CASISTICHE COMUNI DI DIVISIONE PER ZERO

```python
# ERRORE 1: Lista vuota
numeri = []
media = sum(numeri) / len(numeri)  # ☠️

# ERRORE 2: Contatore che rimane a zero
presenti = 0
media = totale_voti / presenti  # ☠️

# ERRORE 3: Input sbagliato
giorni = 0
consumo_giornaliero = consumo_totale / giorni  # ☠️
```

**Regola**: Prima di ogni divisione, chiediti: "Quel numero può essere zero?"

---

## 🏆 CHALLENGE FINALE: Trova tutti e 3!

```python
def analizza_voti(voti_studente_1, voti_studente_2):
    """Confronta i voti di due studenti"""
    
    # Calcola medie
    media_1 = sum(voti_studente_1) / len(voti_studente_1)
    media_2 = sum(voti_studente_2) / len(voti_studente_2)
    
    print("Media studente 1: " + media_1)
    print("Media studente 2: " + media_2)
    
    # Chi ha la media più alta?
    if media_1 > media_2:
        differenza = media_1 - media_2
        print("Studente 1 ha " + differenza + " punti in più")
    else:
        differenza = media_2 - media_1
        print("Studente 2 ha " + differenza + " punti in più")

# Test
alice = [8, 9, 7, 8]
bob = []

analizza_voti(alice, bob)
```

---

## 🤔 Quanti errori ci sono nel codice?

**A)** 1 errore (facile!)  
**B)** 2 errori (medio)  
**C)** 3 errori (difficile!)  
**D)** Il codice funziona perfettamente (fiducia cieca)

*Pensaci bene... ci sono trabocchetti ovunque!*

---

## ✅ RISPOSTA CHALLENGE FINALE

**Errori presenti** (tutti e 3!):

1. **ZeroDivisionError** (riga 5): Bob ha lista vuota → `len(voti_studente_2) = 0`

2. **TypeError** (riga 7): Non puoi concatenare stringhe e numeri float!
   ```python
   print("Media studente 1: " + media_1)  # ☠️
   # Serve: print("Media studente 1: " + str(media_1))
   ```

3. **TypeError** (riga 13 e 17): Stessa cosa per la differenza!
   ```python
   print("Studente 1 ha " + differenza + " punti in più")  # ☠️
   ```

**Se hai trovato tutti e 3, sei un campione del debugging!** 🏆

---

## 🎓 RECAP: Le Regole d'Oro

1. **Leggi lo stacktrace dall'alto verso il basso** (l'errore è in fondo)
2. **Guarda il TIPO di errore**:
   - `TypeError` → hai mescolato tipi incompatibili (str + int)
   - `IndexError` → indice fuori dai limiti della lista
   - `ZeroDivisionError` → hai diviso per zero
3. **Gli indici partono da 0** (non dimenticarlo MAI!)
4. **Valida gli input** (liste vuote, divisioni per zero)
5. **Converti i tipi esplicitamente** (usa `str()`, `int()`, `float()`)

---

## 🛠️ STRATEGIE DI DEBUG PRO

**Quando il codice non funziona**:

1. **Leggi l'errore completo** (non scappare!)
2. **Guarda il numero di riga** indicato
3. **Aggiungi print()** prima dell'errore:
   ```python
   print("Valore di x:", x)
   print("Tipo di x:", type(x))
   ```
4. **Controlla i tipi** delle variabili
5. **Testa con input semplici** prima di quelli complessi

---

## 💬 CITAZIONI MOTIVAZIONALI

> *"Non ho fallito. Ho solo trovato 10.000 modi che non funzionano."*
> — Thomas Edison (che non programmava in Python)

> *"Debugging è come essere il detective in un giallo dove sei anche l'assassino."*
> — Filipe Fortes

> *"Il codice che funziona al primo tentativo è sospetto."*
> — Ogni programmatore esperto

---

## 🎮 HOMEWORK CHALLENGE

Crea un programma che:
1. Chiede all'utente di inserire N numeri (usa `input()`)
2. Li salva in una lista
3. Calcola media, massimo e minimo
4. **Gestisce TUTTI i possibili errori**:
   - Lista vuota
   - Input non numerico
   - Divisioni per zero

**Bonus**: Usa `try/except` per gestire gli errori con eleganza!

---

## 🎯 ESERCIZI EXTRA

**Debug questi mini-programmi**:

```python
# Esercizio 1
numeri = [10, 20, 30]
print(numeri[3])

# Esercizio 2
età = 18
messaggio = "Hai " + età + " anni"
print(messaggio)

# Esercizio 3
voti = []
media = sum(voti) / len(voti)
```

*Riesci a trovare e correggere tutti gli errori?*

---

## 🙋 DOMANDE?

**Ricorda**: 
- Non esistono domande stupide
- Solo codice che non compila
- E stacktrace che non leggiamo

**Trucco finale**: Quando sei bloccato, prova a spiegare il problema a un amico (o a un papero di gomma). Spesso la soluzione arriva mentre spieghi!

---

## 🎉 GRAZIE!

Ora siete pronti per:
- ✅ Debuggare come dei professionisti
- ✅ Leggere gli stacktrace senza panico
- ✅ Capire cosa Python sta cercando di dirvi
- ✅ Evitare i 3 errori più comuni
- ✅ Usare `print()` strategicamente

**Keep calm and debug on** 🐛🔧

*P.S. Ricordati: ogni bug che risolvi ti rende un programmatore migliore!*


---


# I Classici Errori che Vedrete 💥

| Errore | Traduzione Umana |
|--------|------------------|
| `SyntaxError` | "Hai scritto male qualcosa, analfabeta!" |
| `NameError` | "Questa variabile non esiste, te la sei sognata?" |
| `TypeError` | "Non puoi sommare patate con carote" |
| `IndexError` | "Lista troppo corta, hai fatto il furbo?" |
| `IndentationError` | "Hai sbagliato ad indentare, controllare prego..." |

---

# Tips per Leggere gli StackTrace 💡

1. **Non farti prendere dal panico** (respira profondamente)
2. **Leggi dal basso verso l'alto** (sì, sempre)
3. **Cerca il nome del TUO file** (ignora roba di librerie esterne)
4. **Guarda il numero di riga** (poi vai a vedere QUELLA riga)
5. **Leggi il messaggio finale** (Python ti dice cosa è andato storto)

**Golden Rule:** Se l'errore non è chiaro, **copia-incolla su Google** (seriamente, lo fanno tutti i programmatori)

---

<!-- _class: lead -->

# PARTE II
## Il Debugger: Il Tuo Superpotere in Thonny

*"Con grandi poteri derivano grandi... eh no, solo debugging"*

---

# Cos'è il Debugging? 🐛

**Debug** = Togliere i "bug" (insetti) dal codice

> **Fun Fact:** Nel 1947 un VERO insetto bloccò un computer. Grace Hopper lo rimosse e scrisse: "First actual case of bug being found"

**Oggi:** I bug sono metaforici (ma altrettanto fastidiosi)

---

# Il debugger: il tuo microscopio 🔬

Il debugger ti permette di:
- ⏸️ **Fermare** il programma durante l'esecuzione
- 👁️ **Guardare** cosa c'è dentro le variabili
- 👣 **Camminare** riga per riga nel codice
- 🕵️ **Capire** dove il programma impazzisce

**In altre parole:** È come mettere il programma in slow-motion

---

# Thonny: Debug Mode 🎮

**Come attivarlo:**
1. Apri il tuo programma in Thonny
2. Clicca sull'icona 🐛 oppure premi `Ctrl+F5`
3. **BOOM!** Sei in debug mode

**Oppure:**
- Clicca sul numero di riga per mettere un **breakpoint** (punto rosso)
- Esegui normalmente (`F5`)
- Il programma si ferma al breakpoint

---

# I Controlli del Debugger 🎮

| Pulsante | Nome | Cosa fa |
|----------|------|---------|
| ▶️ | Run | "Vai fino al prossimo breakpoint" |
| ⏭️ | Step Over | "Esegui questa riga e vai alla prossima" |
| ⏬ | Step Into | "Entra dentro questa funzione" |
| ⏫ | Step Out | "Esci da questa funzione" |
| ⏸️ | Pause | "Fermati ORA!" |

---

# Breakpoint 🚩

<br>

Ovvero i checkpoint del codice: "Python, fermati QUI che devo controllare una cosa"

```python
def calcola_sconto(prezzo, percentuale):
    # 🔴 BREAKPOINT QUI (riga 2)
    sconto = prezzo * percentuale / 100
    # 🔴 BREAKPOINT QUI (riga 4)
    prezzo_finale = prezzo - sconto
    return prezzo_finale
```

**Quando il programma arriva al breakpoint:**
- Si ferma
- Puoi vedere i valori delle variabili
- Puoi decidere cosa fare dopo

---

# Le Variabili nel Debugger 👀

Quando sei in debug mode, Thonny ti mostra:

**Pannello "Variables":**
```
prezzo = 100
percentuale = 20
sconto = ??? (non ancora calcolato)
```

**Puoi:**
- Vedere i valori in TEMPO REALE
- Capire se sono corretti
- Scoprire dove il tuo cervello ha fallito

---

# 🎯 SFIDA: Debug Detective

```python
def trova_massimo(numeri):
    massimo = 0
    for num in numeri:
        if num > massimo:
            massimo = num
    return massimo

lista = [-5, -2, -10, -1]
risultato = trova_massimo(lista)
print(f"Massimo: {risultato}")
```

**Problema:** Dovrebbe stampare `-1`, ma stampa `0`

**Missione:** Usa il debugger mentalmente. Dov'è il bug?

---

# Soluzione SFIDA 🎓
<br>

**Il bug:** `massimo = 0` all'inizio!

Se TUTTI i numeri sono negativi, nessuno è > 0
Quindi `massimo` resta 0 (SBAGLIATO!)

```python
# SOLUZIONE ?
def trova_massimo(numeri):
    massimo = numeri[0]  # Parti dal primo numero!
    for num in numeri[1:]:
        if num > massimo:
            massimo = num
    return massimo
```

**Con il debugger:** Avresti visto `massimo` restare 0 nel loop

---

# 🖨️ Metodo "barbaro" del "print" 
<br>
A volte il debugger è troppo. 
Soluzione veloce che a volte è sufficiente:

```python
def calcola_media(voti):
    print(f"DEBUG: voti ricevuti = {voti}")  # ??
    
    totale = sum(voti)
    print(f"DEBUG: totale = {totale}")  # ??
    
    media = totale / len(voti)
    print(f"DEBUG: media = {media}")  # ??
    
    return media
```

**Pro:** Veloce e intuitivo
**Contro:** Dovrai cancellare tutti i print dopo (o dimenticartene e consegnare così al prof 😅)

---

# Strategia di Debug Professionale 🎯

1. **Riproduci l'errore** (deve succedere SEMPRE, non "a volte")
2. **Leggi lo stacktrace** (ora sai come fare!)
3. **Formula un'ipotesi** (cosa PENSI sia il problema)
4. **Usa il debugger** (verifica la tua ipotesi)
5. **Testa la soluzione** (funziona davvero?)

**Regola d'oro:** Un bug alla volta. Non correggere 10 cose insieme.

---

# 🎯 SFIDA FINALE: Il Mistero del Codice

```python
def saluta_classe(studenti):
    for i in range(len(studenti)):
        nome = studenti[i]
        if nome == "Prof":
            print("Buongiorno, Professore!")
        else:
            print(f"Ciao {nome}!")

classe = ["Alice", "Bob", "Prof", "Diana"]
saluta_classe(classe)
```

**Sembra giusto, ma...** cosa succederebbe se `studenti = []`?

**Usa il debugger mentale!**

---

# Soluzione SFIDA FINALE 💡

**Problema:** Se `studenti = []`, il loop non trova problemi...
**MA** se modifichi il codice così:

```python
def saluta_classe(studenti):
    for i in range(len(studenti) + 1):  # +1 qui!
        nome = studenti[i]  # ?? IndexError!
```

**Con il debugger:** Vedresti `i` diventare troppo grande

**Soluzione Pythonica:**
```python
for nome in studenti:  # Più semplice!
    # ...
```

---
<br>

# Errori Comuni dei Programmatori Junior 🤦

1. **Non leggere l'errore** ("Tanto non capisco" ❌)
2. **Cambiare codice a caso** ("Forse se metto +1 qui..." ❌)
3. **Non testare dopo ogni modifica** (poi hai 10 errori insieme ❌)
4. **Arrendersi troppo presto** ("È impossibile!" ❌)
5. **Non chiedere aiuto** (Orgoglio? Nel 2025? ❌)

**Remember:** Anche i professionisti debuggano per ore!

---

# Tools Avanzati (Bonus) 🚀

**In Thonny:**
- **Highlight Syntax Errors:** Sottolinea errori di sintassi in rosso
- **Assistant:** Suggerimenti automatici (a volte utili!)
- **Variables view:** Vedi TUTTO quello che succede

**Fuori da Thonny:**
- `pdb` (Python Debugger integrato)
- Logging (invece di print)
- Unit tests (prevenire invece di curare)

---

# La Filosofia del Debug 🧘

> "Debugging is twice as hard as writing the code in the first place. Therefore, if you write the code as cleverly as possible, you are, by definition, not smart enough to debug it."
> — Brian Kernighan

**Traduzione:** Scrivi codice SEMPLICE.
Il te-stesso-del-futuro ti ringrazierà.

---

# Checklist del Buon Debugger ✅

- [ ] Ho letto TUTTO lo stacktrace?
- [ ] Ho capito QUALE riga genera l'errore?
- [ ] Ho usato il debugger per vedere le variabili?
- [ ] Ho testato la mia ipotesi?
- [ ] Ho cercato su Google/StackOverflow?
- [ ] Ho chiesto aiuto dopo 30+ minuti bloccato?
- [ ] Ho imparato qualcosa da questo errore?

**Se hai 7/7:** Sei pronto per il mondo reale! 🎓

---

# Mini-Dizionario Debug 📖

- **Bug:** Errore nel codice
- **Debug:** Processo di rimozione degli errori
- **Debugger:** Tool per fare debug
- **Breakpoint:** Punto dove fermare l'esecuzione
- **Step Over:** Esegui riga corrente
- **Step Into:** Entra nella funzione
- **StackTrace:** Storia di come siamo arrivati all'errore
- **RTFM:** Read The Friendly Manual (leggete i messaggi d'errore!)

---

# 🎯 ESERCIZIO PER CASA

**Trova i 3 bug in questo codice:**

```python
def calcola_media_classe(voti_studenti):
    totale = 0
    contatore = 0
    for voti in voti_studenti:
        for voto in voti:
            totale += voto
            contatore += 1
    return totale / contatore

classe_3A = [ [8, 7, 9],     [6, 6, 7],
              [],  # Studente assente!
              [9, 9, 10] ]

media = calcola_media_classe(classe_3A)
print(f"Media: {media}")
```

---

# Hints per l'Esercizio 💡

1. **Cosa succede con lo studente assente?**
   - Il suo array è vuoto `[]`
   - Pensa al loop...

2. **Usa il debugger!**
   - Metti un breakpoint nel loop
   - Guarda `totale` e `contatore`

3. **Cosa succede se TUTTA la classe è assente?**
   - `contatore = 0`
   - `totale / contatore = ?` 💥

---

# Conclusioni 🎓

**Ricordate:**
- Gli errori sono NORMALI (capita anche ai professionisti)
- Lo stacktrace è tuo AMICO (imparate a leggerlo!)
- Il debugger è un SUPERPOTERE (usatelo!)
- Google è tuo ALLEATO (seriamente, usatelo)

**"Talk is cheap. Show me the code."** — Linus Torvalds

---

# Risorse Extra 📚

- **Documentazione Python:** docs.python.org
- **StackOverflow:** La Bibbia dei programmatori
- **Thonny Docs:** thonny.org
- **Real Python:** realpython.com/python-debugging-pdb/

**E ricordate:** Ogni errore è un'opportunità per imparare!

(O almeno così dicono per farci sentire meglio)

---

# Fine! 🎉

**Adesso andate a debuggare qualcosa!**

*P.S.: Se trovate un modo per debuggare la vita, fateci sapere* 😅

```python
while True:
    try:
        learn_from_mistakes()
    except Exception as e:
        print("Si cresce così!")
```

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