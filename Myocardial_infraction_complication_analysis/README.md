# Analisi delle Complicanze dell'Infarto Miocardico

Questo progetto analizza un dataset clinico relativo a pazienti con infarto miocardico, con l'obiettivo di studiare le complicanze post-infarto e identificare quali caratteristiche cliniche, elettrocardiografiche e di laboratorio sono più associate a esiti avversi.

Il lavoro è strutturato come un'analisi esplorativa e predittiva in Python, con notebook Jupyter, preprocessing dei dati, analisi delle variabili mancanti, correlazioni, riduzione dimensionale e classificazione.

## Obiettivo del progetto

Il dataset viene utilizzato per rispondere a quattro domande di ricerca principali:

1. Quali caratteristiche alla dimissione/ingresso ospedaliero sono associate all'esito letale?
2. Un'anti-morbo/aritmia preesistente aumenta il rischio di complicanze aritmiche post-infarto?
3. Esistono differenze di rischio tra uomini e donne?
4. I valori di laboratorio (ad esempio potassio, CPK, ALT) sono utili nella previsione delle complicanze più gravi?

## Dataset

Il dataset utilizzato è il database "Myocardial Infarction Complications" dell'UCI, composto da:

- circa 1700 pazienti
- 111 feature di input
- 12 target/complicazioni possibili
- valori mancanti codificati come `?`

### File principali

- `Raw/MI.data`: dataset grezzo
- `Studies/Myocardial infarction complications Database.csv`: versione della base dati in formato tabellare
- `Studies/Myocardial infarction complications Database description.pdf`: descrizione del dataset
- `Studies/Descriptive statistics.pdf`: statistiche descrittive del database
- `plan.md`: piano di analisi e metodologia del progetto
- `tabular_analysis.ipynb`: notebook principale con analisi e modelli

## Struttura del repository

```text
Myocardial_infraction_complication_analysis/
├── Raw/
│   └── MI.data
├── Studies/
│   ├── Descriptive statistics.pdf
│   ├── Myocardial infarction complications Database description.pdf
│   └── Myocardial infarction complications Database.csv
├── .gitignore
├── plan.md
├── README.md
├── requirements.txt
├── tabular_analysis.ipynb
├── venv/
└── .claude/
```

## Analisi svolta

Nel notebook principale vengono trattati i seguenti passaggi:

- importazione dei dati e definizione delle colonne
- normalizzazione dei valori mancanti (`?` → `NaN`)
- organizzazione delle feature in gruppi semantici:
  - anamnesi
  - condizioni cliniche alla presentazione
  - valori di laboratorio
  - morfologia ECG
  - farmaci/terapie
- esclusione di variabili considerate leakage di dati, in particolare quelle relative a trattamenti somministrati dopo l'ammissione
- analisi descrittiva delle variabili e distribuzioni
- valutazione della missingness
- analisi di correlazione e multicollinearità
- confronto tra feature e target prioritari
- riduzione dimensionale tramite PCA/UMAP
- preprocessing per imputation e scaling
- classificazione con modelli di machine learning
- valutazione delle prestazioni mediante metriche appropriate per dataset sbilanciati

## Requisiti

Il progetto richiede un ambiente Python con le librerie riportate in `requirements.txt`, tra cui:

- pandas
- numpy
- scikit-learn
- scipy
- matplotlib
- seaborn
- xgboost
- imbalanced-learn
- umap-learn

## Setup rapido

### 1. Creare un ambiente virtuale

```bash
cd "<percorso-del-progetto>"
python3 -m venv venv
source venv/bin/activate
```

### 2. Installare le dipendenze

```bash
pip install -r requirements.txt
```

### 3. Avviare il notebook

```bash
jupyter notebook
```

oppure:

```bash
jupyter lab
```

Aprire poi `tabular_analysis.ipynb` e eseguire le celle in ordine.

## Note importanti

- Il dataset presenta molti valori mancanti, soprattutto in variabili di laboratorio ed ECG.
- Le colonne relative a trattamenti e interventi post-ammissione sono state escluse per evitare data leakage.
- I target sono altamente sbilanciati, quindi non è sufficiente valutare la sola accuracy: si usano metriche come AUC, precision, recall, F1 e analisi di prevalenza.
- L'analisi è orientata al contesto clinico: i risultati sono interpretati in relazione agli effetti fisiologici e alle complicanze dell'infarto.

## Risultato atteso

Il progetto mira a costruire una base analitica per capire quali fattori clinici e di laboratorio siano associati alle complicanze più severe dell'infarto, e se sia possibile costruire un modello predittivo utile per supportare la valutazione del rischio.

## Autore

Il notebook principale è stato sviluppato da Manuel Testoni (matricola 219155).

## Licenza

Il progetto è stato sviluppato a scopo accademico e di analisi dati. Per eventuali vincoli specifici si rimanda alla documentazione fornita dal dataset originale e ai documenti presenti nella cartella `Studies`.
