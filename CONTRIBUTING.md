# 🤝 Guida alla Contribuzione

Grazie per essere interessato a contribuire al progetto **Progetto Scuole**! Ogni contributo è benvenuto, che si tratti di miglioramenti alle presentazioni, aggiunta di nuovi esercizi, correzioni o miglioramenti al codice.

Ci sono molti modi per contribuire al progetto:

- ✅ **Segnalare errori** nelle presentazioni o nel codice
- ✅ **Migliorare documentazione** con esempi o chiarimenti
- ✅ **Creare cheatsheets** su argomenti trattati
- ✅ **Condividere risorse** utili (tutorial, articoli, video)
- ✅ **Aggiungere materiale didattico** (presentazioni, esercizi)
- ✅ **Revisionare contenuti** esistenti
- ✅ **Proporre nuovi moduli** o argomenti
- ✅ **Sviluppare progetti esempio**

Prima di iniziare, assicurati di aver letto e compreso queste linee guida. Sono pensate per mantenere il progetto organizzato e facile da usare per tutti.

## Come Contribuire

### 1. Fork del Repository
Per prima cosa, crea una copia del repository sul tuo account GitHub:
1. Vai alla pagina del repository: [https://github.com/PythonBiellaGroup/ProgettoScuole](https://github.com/PythonBiellaGroup/ProgettoScuole).
2. Clicca sul pulsante **Fork** nell'angolo in alto a destra della pagina.

### 2. Crea un Branch
Crea un branch per la tua feature o correzione. Non lavorare direttamente sulla branch principale (`main`).

```bash
# Per nuove feature
git checkout -b feature/nome-feature

# Per fix di bug
git checkout -b fix/descrizione-bug

# Per documentazione
git checkout -b docs/argomento

# Per esercizi
git checkout -b exercise/modulo-numero
```

**Convenzioni nomi branch:**
- `feature/` - Nuove funzionalità
- `fix/` - Correzioni bug
- `docs/` - Documentazione
- `exercise/` - Soluzioni esercizi
- `refactor/` - Refactoring codice
- `test/` - Aggiunta test

#### 2️⃣ Lavora sul tuo Branch

```bash
# Fai le tue modifiche
# Aggiungi file nuovi o modificati
git add .

# Oppure aggiungi file specifici
git add path/to/file.py
```

#### 3️⃣ Commit delle Modifiche

```bash
# Commit con messaggio descrittivo
git commit -m "tipo: breve descrizione

Descrizione dettagliata opzionale."
```

Vedi [Convenzioni per Commit](#convenzioni-per-commit) per dettagli.

#### 4️⃣ Push del Branch

```bash
# Push sulla TUA fork
git push origin nome-del-tuo-branch
```

#### 5️⃣ Apri una Pull Request

1. Vai su GitHub sulla tua fork
2. Clicca su "Compare & pull request"
3. Compila il template della PR (vedi sotto)
4. Clicca su "Create pull request"

---

## 📝 Standard di Codice

### Python Style Guide

Seguiamo [PEP 8](https://pep8.org/) con alcune eccezioni:

```python
# ✅ BUONO
def calcola_media(numeri):
    """
    Calcola la media di una lista di numeri.
    
    Args:
        numeri (list): Lista di numeri
        
    Returns:
        float: Media dei numeri
    """
    if not numeri:
        return 0
    return sum(numeri) / len(numeri)


# ❌ DA EVITARE
def calcolaMedia(n):
    return sum(n)/len(n)  # Niente docstring, niente controlli
```

### Regole Principali

#### Naming Conventions
- **Variabili e funzioni**: `snake_case`
- **Costanti**: `UPPER_CASE`
- **Classi**: `PascalCase`
- **Moduli**: `lowercase`

```python
# ✅ Corretto
nome_studente = "Mario"
MAX_STUDENTI = 30

class AnalizzatoreDati:
    pass
```

#### Docstrings
Tutti i moduli, classi e funzioni devono avere docstring:

```python
def analizza_dataset(df, colonne=None):
    """
    Analizza un DataFrame Pandas e restituisce statistiche descrittive.
    
    Questa funzione calcola media, mediana, deviazione standard
    per le colonne numeriche specificate.
    
    Args:
        df (pd.DataFrame): DataFrame da analizzare
        colonne (list, optional): Lista colonne da includere.
                                  Default: tutte le colonne numeriche.
    
    Returns:
        pd.DataFrame: DataFrame con statistiche descrittive
        
    Raises:
        ValueError: Se il DataFrame è vuoto
        
    Example:
        >>> import pandas as pd
        >>> df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        >>> risultato = analizza_dataset(df)
        >>> print(risultato)
    """
    if df.empty:
        raise ValueError("DataFrame non può essere vuoto")
    
    # Implementazione...
```

#### Commenti

```python
# ✅ Buoni commenti - spiegano il PERCHÉ
# Usiamo log10 per normalizzare valori con range molto ampio
valore_normalizzato = np.log10(valore)

# ❌ Commenti inutili - ripetono cosa fa il codice
# Incrementa i di 1
i = i + 1
```

#### Import

```python
# ✅ Ordine corretto
# 1. Librerie standard
import os
import sys
from datetime import datetime

# 2. Librerie terze parti
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

# 3. Moduli locali
from utils.preprocessing import pulisci_dati
from config import PERCORSO_DATI
```

### Jupyter Notebooks

Per i notebook:

- ✅ Celle numerate e ordinate logicamente
- ✅ Markdown per spiegazioni tra le celle
- ✅ Output salvati solo per notebook dimostrativi
- ✅ Restart & Run All prima di committare
- ❌ Evita celle con codice duplicato

```python
# ✅ In ogni notebook, prima cella
"""
Titolo del Notebook
==================

Descrizione: Cosa fa questo notebook
Autore: Nome Cognome
Data: 2024-XX-XX
Prerequisiti: cosa serve per eseguirlo
"""
```

---

## 💬 Convenzioni per Commit

### Formato Messaggio

```
tipo(scope): oggetto breve (max 50 caratteri)

Corpo del messaggio opzionale con dettagli.
Spiega cosa è cambiato e perché.

Footer opzionale (riferimenti issue, breaking changes)
```

### Tipi di Commit

| Tipo | Descrizione | Esempio |
|------|-------------|---------|
| `feat` | Nuova funzionalità | `feat(esercizi): aggiungi esercizi NumPy` |
| `fix` | Correzione bug | `fix(slides): correggi typo slide 23` |
| `docs` | Solo documentazione | `docs(readme): aggiorna istruzioni setup` |
| `style` | Formattazione codice | `style(preprocessing): applica PEP 8` |
| `refactor` | Refactoring | `refactor(utils): semplifica funzione` |
| `test` | Aggiunta test | `test(modulo1): aggiungi test unitari` |
| `chore` | Manutenzione | `chore(deps): aggiorna requirements` |

### Esempi di Buoni Commit

```bash
# ✅ Chiaro e descrittivo
git commit -m "feat(modulo2): aggiungi esercizi su Pandas DataFrame

- Aggiunti 5 esercizi di difficoltà crescente
- Inclusi dataset CSV per esercitazioni
- Aggiornato README con istruzioni"

# ✅ Fix con riferimento issue
git commit -m "fix(slides): correggi esempio codice slide 15

Il codice non gestiva il caso di lista vuota.
Aggiunto controllo e test.

Fixes #42"

# ❌ Poco chiaro
git commit -m "fix stuff"

# ❌ Troppo generico
git commit -m "update"
```

---

## 🐛 Segnalare Bug

Hai trovato un bug? Ottimo! Ecco come segnalarlo:

### Prima di Segnalare

- ✅ Cerca tra le [Issues esistenti](https://github.com/PythonBiellaGroup/ProgettoScuole/issues)
- ✅ Verifica che il bug non sia già stato risolto
- ✅ Prova a riprodurre il bug più volte

### Template Issue per Bug

```markdown
## 🐛 Descrizione Bug

Breve descrizione del problema

## 📝 Come Riprodurlo

Step per riprodurre il comportamento:
1. Vai a '...'
2. Esegui '....'
3. Vedi errore '...'

## ✅ Comportamento Atteso

Cosa dovrebbe succedere

## ❌ Comportamento Attuale

Cosa succede invece

## 📸 Screenshot

Se applicabile, aggiungi screenshot

## 💻 Ambiente

- OS: [e.g. Windows 11, macOS 14, Ubuntu 22.04]
- Python: [e.g. 3.11.5]
- Browser: [se rilevante]

## 📎 Informazioni Aggiuntive

Qualsiasi altro contesto utile
```

### Esempio Issue

```markdown
## 🐛 Errore nell'esercizio 3 del modulo Pandas

## 📝 Come Riprodurlo

1. Aprire `esercizi/pandas/esercizio_3.py`
2. Eseguire con dataset fornito `dati.csv`
3. Errore: `KeyError: 'colonna_mancante'`

## ✅ Comportamento Atteso

Il codice dovrebbe gestire colonne mancanti

## ❌ Comportamento Attuale

Solleva KeyError e termina

## 💻 Ambiente

- OS: Windows 11
- Python: 3.11.2
- Pandas: 2.0.1

## 📎 Possibile Soluzione

Aggiungere controllo: `if 'colonna' in df.columns:`
```

---

## 💡 Proporre Miglioramenti

Hai un'idea per migliorare il progetto? Fantastico!

### Template Issue per Feature

```markdown
## 🚀 Feature Request

Breve descrizione della feature

## 💭 Motivazione

Perché questa feature sarebbe utile?
Quale problema risolve?

## 📋 Descrizione Dettagliata

Descrizione completa di come dovrebbe funzionare

## 🎯 Alternativa Considerata

Hai considerato altre soluzioni?

## 📎 Informazioni Aggiuntive

Esempi, mockup, riferimenti...
```

### Esempio Feature Request

```markdown
## 🚀 Aggiungere sezione su Deep Learning

## 💭 Motivazione

Molti studenti sono interessati a reti neurali.
Un'introduzione base con Keras/TensorFlow sarebbe preziosa.

## 📋 Descrizione Dettagliata

Propongo un modulo aggiuntivo (4-6 ore) che copra:
- Concetti base di neural networks
- Implementazione con Keras
- Esempio pratico: classificazione immagini MNIST

## 🎯 Alternativa Considerata

- PyTorch invece di Keras (più complesso per principianti)
- Solo teoria senza pratica (meno coinvolgente)

## 📎 Informazioni Aggiuntive

Posso contribuire creando slide e notebook di esempio.
```

---

## 🔀 Pull Request

### Prima di Aprire una PR

- ✅ Il tuo branch è aggiornato con `main`
- ✅ Il codice segue gli standard
- ✅ Hai testato le modifiche
- ✅ Hai aggiornato la documentazione se necessario
- ✅ Non ci sono conflitti con `main`

### Template Pull Request

```markdown
## 📝 Descrizione

Cosa fa questa PR? Perché è necessaria?

## 🔗 Issue Correlate

Chiude #issue_number
Relativa a #other_issue

## 🎯 Tipo di Modifica

- [ ] Bug fix (non breaking change)
- [ ] Nuova feature (non breaking change)
- [ ] Breaking change (modifica che può rompere codice esistente)
- [ ] Documentazione
- [ ] Refactoring

## ✅ Checklist

- [ ] Il mio codice segue gli standard del progetto
- [ ] Ho commentato il codice dove necessario
- [ ] Ho aggiornato la documentazione
- [ ] Ho testato le modifiche
- [ ] Nessun warning o errore
- [ ] Ho aggiornato CHANGELOG.md (se applicabile)

## 📸 Screenshot

Se applicabile (per modifiche UI, slides, etc.)

## 🧪 Come Testare

Istruzioni per testare le modifiche
```

### Best Practices per PR

#### ✅ FARE

- **Una PR = Una funzionalità/fix**
- Descrizioni chiare e complete
- Commit atomici e significativi
- Rispondere prontamente ai feedback
- Essere aperti a modifiche
- Aggiornare la PR se richiesto

#### ❌ EVITARE

- PR enormi con 50+ file modificati
- Modifiche non correlate nella stessa PR
- Ignorare feedback dei reviewer
- Commit con messaggi tipo "fix", "update"
- Includere file personali (config, secrets)

### Dimensione PR Ideale

```
Piccola:    1-50 righe   ✅ Ottima!
Media:      51-250 righe ✅ Buona
Grande:     251-500 righe ⚠️ Considera split
Molto grande: 500+ righe ❌ Troppo grande, dividi!
```

---

## 👀 Code Review

### Se Stai Reviewando

#### Cosa Controllare

- ✅ Il codice funziona?
- ✅ È leggibile e ben documentato?
- ✅ Segue gli standard del progetto?
- ✅ I test passano?
- ✅ È la soluzione più semplice possibile?

#### Come Dare Feedback

**✅ Feedback Costruttivo:**
```markdown
Ottimo lavoro! Alcuni suggerimenti:

- Considera di estrarre questa logica in una funzione separata
  per migliorare la leggibilità
- Potresti aggiungere un controllo per lista vuota?
- Typo nella docstring: "calcula" → "calcola"

Nel complesso, approccio solido! 👍
```

**❌ Feedback Non Costruttivo:**
```markdown
Questo codice fa schifo. Riscrivilo.
```

#### Tipologie di Commento

- 💡 **Suggerimento**: Idee opzionali
- ❓ **Domanda**: Chiedi chiarimenti
- ⚠️ **Preoccupazione**: Possibili problemi
- 🔴 **Blocco**: Deve essere fixato prima del merge
- ✨ **Complimento**: Evidenzia parti buone!

### Se Ricevi Review

- ✅ Ringrazia per il feedback
- ✅ Chiedi chiarimenti se qualcosa non è chiaro
- ✅ Implementa modifiche ragionevoli
- ✅ Spiega se non sei d'accordo (educatamente)
- ❌ Non prenderla sul personale
- ❌ Non ignorare feedback

**Esempio Risposta:**

```markdown
@reviewer Grazie per il feedback!

✅ Ho estratto la logica in `valida_input()`
✅ Aggiunto controllo per lista vuota
✅ Corretto typo

Per il suggerimento sul pattern Strategy, ho preferito
mantenere l'approccio attuale per semplicità, dato che
è materiale didattico per studenti di terza. Che ne pensi?
```

---

## 🏷️ Etichette (Labels)

Usiamo labels per organizzare Issues e PR:

| Label | Descrizione | Colore |
|-------|-------------|--------|
| `bug` | Qualcosa non funziona | 🔴 Rosso |
| `enhancement` | Nuova feature o miglioramento | 🟢 Verde |
| `documentation` | Documentazione | 🔵 Blu |
| `good first issue` | Buono per nuovi contributor | 🟣 Viola |
| `help wanted` | Cerchiamo aiuto su questo | 🟡 Giallo |
| `question` | Domanda o discussione | 🟠 Arancione |
| `duplicate` | Issue duplicata | ⚪ Grigio |
| `wontfix` | Non verrà implementato | ⚫ Nero |
| `priority-high` | Alta priorità | 🔴 Rosso |
| `priority-low` | Bassa priorità | 🟢 Verde |

---

## 📚 Risorse Utili

### Git e GitHub

- [Git Handbook](https://guides.github.com/introduction/git-handbook/)
- [GitHub Flow](https://guides.github.com/introduction/flow/)
- [How to Write a Git Commit Message](https://chris.beams.io/posts/git-commit/)

### Python Style

- [PEP 8](https://pep8.org/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
- [Real Python - Code Style](https://realpython.com/python-pep8/)

### Documentazione

- [Writing Good Documentation](https://www.writethedocs.org/guide/writing/beginners-guide-to-docs/)
- [Markdown Guide](https://www.markdownguide.org/)

### Testing

- [pytest Documentation](https://docs.pytest.org/)
- [Testing Best Practices](https://realpython.com/python-testing/)

---

## ❓ Domande?

Se hai domande su come contribuire:

1. 💬 Chiedi nelle [Discussions](https://github.com/PythonBiellaGroup/ProgettoScuole/discussions)
2. 📧 Contatta i maintainer: pythonbiellagroup@gmail.com
3. 🐛 Apri una Issue con label `question`

---

## 🎉 Grazie!

Ogni contributo, piccolo o grande, è prezioso per il progetto!

La tua partecipazione aiuta a:
- 📚 Migliorare il materiale didattico
- 🤝 Creare una community attiva
- 🎓 Supportare l'apprendimento di altri studenti
- 💡 Condividere conoscenza

**Insieme rendiamo ProgettoScuole sempre migliore!** 🚀

---

## 📜 Codice di Condotta

Tutti i contributor devono aderire al nostro [Codice di Condotta](CODE_OF_CONDUCT.md).

In sintesi:
- ✅ Sii rispettoso e inclusivo
- ✅ Accetta feedback costruttivo
- ✅ Focalizzati su cosa è meglio per la community
- ❌ No harassment, trolling, o insulti
- ❌ No spam o autopromozione

---

<div align="center">

**Happy Contributing! 🎊**

Made with ❤️ by [PythonBiellaGroup](https://github.com/PythonBiellaGroup)

</div>
