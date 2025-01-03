# Simulazione del LMC in Python
## main.py

`main.py` è un programma che simula l'esecuzione di un programma assembly per il Little Man Computer (LMC). 
Questo script permette di eseguire un file assembly e di specificare una coda di input. L'esecuzione avviene in due modalità: completa oppure passo passo.

## Come Eseguire `main.py`

### Sintassi
```bash
python main.py --file <nome_file_assembly> [--input <coda_input>] [--mode <modalità>]
```
### Parametri

| Argomento      | Obbligatorio | Descrizione                                                                 |
|----------------|--------------|-----------------------------------------------------------------------------|
| `--file`       | Sì           | Il file contenente le istruzioni assembly (esempio: `quine.lmc`).           |
| `--input`      | No           | La coda di input, specificata come numeri interi separati da virgole (es: `5,10,15`). |
| `--mode`       | No           | La modalità di esecuzione (`all` o `steps`). Default: `all`.                |

### Modalità di Esecuzione
* `all`: il programma viene eseguito dall'inizio alla fine. Rimane ispezionabile solo lo stato finale del LMC.
* `steps`: il programma viene eseguito passo passo. Ad ogni passo viene stampato lo stato del LMC. L'utente deve premere INVIO per procedere con l'esecuzione dell'istruzione successiva.

