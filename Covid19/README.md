# Graph Analytics on COVID-19 — Big Data Analytics

Analisi di Graph Analytics su dati COVID-19: i paesi vengono modellati come nodi
di un grafo, collegati da relazioni di similarità (`:SIMILAR`) calcolate su feature
epidemiologiche, di mobilità, vaccinali e di risposta governativa. Su questo grafo
si eseguono community detection e query Cypher/GDS per rispondere alle research
question del progetto.

Notebook: `graph_analytics.ipynb`

---

## 1. Requisiti

- **Python 3.11+**
- **Neo4j 5.x** con plugin **Graph Data Science (GDS)** installato e attivo
- I pacchetti Python elencati in `requirements.txt`

---

## 2. Setup ambiente Python

```bash
# dalla cartella del progetto
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Avvio del notebook:

```bash
jupyter lab        # oppure: jupyter notebook
```

---

## 3. Setup Neo4j (obbligatorio)

Il notebook si connette a un'istanza Neo4j locale con plugin GDS.

1. Crea un database Neo4j (Neo4j Desktop o Docker) e installa il plugin **Graph
   Data Science**.
2. Crea/usa un database chiamato **`covid-19`**.
3. Avvia l'istanza su `bolt`/`neo4j` porta **7687**.

Parametri di connessione nel notebook (cella in alto, "NEO4J"):

```python
NEO4J_URI      = "neo4j://127.0.0.1:7687"
NEO4J_USER     = "neo4j"
NEO4J_PASSWORD = "INSERISCI_QUI_LA_TUA_PASSWORD"   # <-- da impostare
NEO4J_DATABASE = "covid-19"
```

---

## 4. Dati

I file CSV si trovano nella cartella **`raw/`** e vengono caricati automaticamente
dal notebook (`RAW = Path("raw")`).

**Fonte:** [Google COVID-19 Open Data](https://health.google.com/covid-19/open-data/)
(tabelle scaricabili da `https://storage.googleapis.com/covid19-open-data/v3/<tabella>.csv`).

File usati dal notebook:

| File                            | Contenuto                                   |
|---------------------------------|---------------------------------------------|
| `index.csv`                     | anagrafica località (chiavi, nomi, ISO)     |
| `epidemiology.csv`              | casi confermati e decessi cumulati          |
| `vaccinations.csv`              | persone completamente vaccinate             |
| `oxford-government-response.csv`| stringency index (risposta governativa)     |
| `mobility.csv`                  | mobilità (workplaces, retail & recreation)  |
| `demographics.csv`              | popolazione, densità, HDI                   |
| `economy.csv`                   | GDP pro capite                              |
| `health.csv`                    | aspettativa di vita, posti letto, ecc.      |

### Sottoinsieme country-level

I dataset originali Google contengono dati a livello nazionale **e**
regionale/sub-regionale, per un totale di ~6.5 GB. Il notebook utilizza
**esclusivamente le righe a livello nazionale** (`aggregation_level == "0"`, 246
paesi): tutto il resto viene scartato in fase di caricamento.

I CSV inclusi in `raw/` sono quindi **già filtrati al solo livello nazionale**
(~29 MB totali). I risultati sono **identici** a quelli ottenibili con i dataset
completi, perché il notebook applica lo stesso filtro.

Per rigenerare i dati completi (opzionale), scaricare le tabelle dalla fonte
Google sopra indicata e sostituirle in `raw/`.

---

## 5. Esecuzione

1. Attivare il venv e avviare Jupyter.
2. Aprire `graph_analytics.ipynb`.
3. Impostare `NEO4J_PASSWORD`.
4. Verificare che Neo4j (con GDS) sia attivo sul database `covid-19`.
5. Eseguire le celle in ordine.

L'ultima cella chiude la connessione e rimuove le proiezioni GDS temporanee.
