# Approfondimento su MongoDB — Big Data Analytics

Approfondimento sperimentale su **MongoDB** come sistema NoSQL documentale, condotto
su un dataset Kaggle di programmi di allenamento (605k righe). L'intera analisi gira
contro un **replica set a 3 nodi** in Docker e risponde a quattro research question:

- **RQ1 — Modellazione:** dal CSV piatto ai documenti annidati (embedding vs referencing),
  con confronto su storage e pattern di accesso.
- **RQ2 — Aggregation framework:** analytics direttamente sui documenti
  (`$unwind`, `$group`, `$map`, `$facet`).
- **RQ3 — Indici:** `COLLSCAN` vs `IXSCAN`, indici composti e covered query,
  misurati con `explain("executionStats")`.
- **RQ4 — Teorema CAP:** write/read concern, read preference e failover del primary
  osservato dal vivo sul replica set.

Notebook: `fitness_exercise_analysis.ipynb`

---

## 1. Requisiti

- **Python 3.11+**
- **Docker** (con Docker Compose v2) in esecuzione
- I pacchetti Python elencati in `requirements.txt`

---

## 2. Setup ambiente Python

```bash
# dalla cartella del progetto
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Configurazione della connessione: copiare `.env.example` in `.env`
(contiene la connection string del replica set, non serve modificarla):

```bash
cp .env.example .env
```

---

## 3. Setup replica set MongoDB (obbligatorio)

Il notebook si connette a un replica set `rs0` a **3 nodi** definito in
`docker-compose.yml` (porte 27017/27018/27019). I tre `mongod` condividono il
network namespace del servizio ausiliario `mongo-net`, quindi i membri sono
raggiungibili come `localhost:2701x` sia tra container sia dall'host —
**nessuna modifica a `/etc/hosts`**.

```bash
# 1. avvio dei container
docker compose up -d

# 2. inizializzazione del replica set (solo la prima volta)
docker compose exec mongo1 mongosh --port 27017 --quiet /rs-init.js

# 3. verifica: 3 membri, 1 PRIMARY
docker compose exec mongo1 mongosh --port 27017 --quiet \
  --eval 'rs.status().members.forEach(m => print(m.name, m.stateStr))'
```

> **Nota:** la porta 27017 deve essere libera sull'host. Se è attivo un MongoDB
> locale (es. `brew services stop mongodb-community`) va fermato prima.

Teardown completo (container **e** volumi dati):

```bash
docker compose down -v
```

---

## 4. Dati

Il dataset **non è incluso nel repository** (294 MB, cartella `archive/` in
`.gitignore`). Va scaricato da Kaggle:

**Fonte:** [Fitness Exercises Dataset — Kaggle](https://www.kaggle.com/)
*(dataset: programmi di allenamento Boostcamp — `programs_detailed_boostcamp_kaggle.csv`)*

Posizionare il file in:

```
Fitness_Exercise_Analysis/
└── archive/
    └── programs_detailed_boostcamp_kaggle.csv   (605.033 righe)
```

| Colonne principali | Contenuto |
|---|---|
| `title`, `description` | identità del programma (2.598 programmi unici) |
| `level`, `goal` | liste di livelli/obiettivi del programma |
| `equipment`, `program_length`, `time_per_workout` | metadati del programma |
| `week`, `day` | posizione dell'esercizio nella gerarchia |
| `exercise_name`, `sets`, `reps`, `intensity` | dettaglio del singolo esercizio |

Il CSV è piatto (una riga per esercizio, metadati del programma duplicati):
la gerarchia *programma → settimana → giorno → esercizio* viene ricostruita
nel notebook (RQ1).

---

## 5. Esecuzione

1. Avviare il replica set e inizializzare `rs0` (sezione 3).
2. Attivare il venv e avviare Jupyter (`jupyter lab` o `jupyter notebook`).
3. Aprire `fitness_exercise_analysis.ipynb`.
4. Eseguire le celle **in ordine**: §2 importa i 605k documenti (~1 min),
   §3 costruisce la collection annidata `programs`, §5 crea e misura gli indici,
   §6 esegue il **failover dal vivo** (ferma e riavvia un container via
   `docker stop`/`docker start`, serve Docker attivo).

L'ultima cella chiude la connessione al replica set.
