# Fabio Tiberio SM3201378
from converter import Converter
import argparse
from pathlib import Path

def main():

    # Parser argomenti riga di comando
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="File con le istruzioni in assembly (es. quine.lmc")
    parser.add_argument("--input", help="Coda di input (es 5,10,15)")
    parser.add_argument("--mode", choices=["all", "steps"], default="all", help="Modalità di esecuzione: 'all' (esegue tutto) o 'steps' (esegue passo dopo passo).")
    args = parser.parse_args()


    try:
        if not Path(f"./files/{args.file}").exists():
            print("Errore: il nome del file specificato non esiste")
            return

        converter = Converter(f"./files/{args.file}")
        instructions = converter.load_memory()

        resolved_instructions = converter.resolve_labels(instructions)

        machine_codes = converter.get_machine_codes(resolved_instructions)
        # print(machine_codes)

        # FASE PREPARATORIA
        if args.input:
            # Leggi input:
            # - Se l'input non è vuoto
            # - Converti in intero l'input
            input_queue = [int(x) for x in args.input.split(",") if x.strip()]

            converter.feed_lmc(machine_codes, input_queue)
        else:
            converter.feed_lmc(machine_codes)

        # FASE DI ESECUZIONE
        if args.mode == "all":
            converter.run_lmc()
            print("Programma terminato con la seguente coda di output:", converter.get_results())
            input("Premi INVIO per ispezionare il LMC\n")
            print(converter.summary())

        elif args.mode == "steps":
            while converter.can_continue():
                summary = converter.summary()
                print(summary)
                input("Premi INVIO per eseguire il prossimo passo...")
                converter.run_lmc_step()
            print("Programma terminato con la seguente coda di output:", converter.get_results())
    except ValueError:
        print("Errore: inserire numeri interi separati da virgole")
        return
    except Exception as e:
        print(f"Errore ${e}")


if __name__ == "__main__":
    main()