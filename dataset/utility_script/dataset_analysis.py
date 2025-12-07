import glob
import yaml
import os
import pandas as pd

def read_yaml_classes(yaml_path):
    """Legge un file YAML e mappa gli ID delle classi ai loro nomi."""
    try:
        with open(yaml_path, 'r') as f:
            data = yaml.safe_load(f)

        nomi_classi = data.get('names', [])
        class_map = {i: name for i, name in enumerate(nomi_classi)}
        return class_map
    except FileNotFoundError:
        print(f"ERRORE: File YAML non trovato al percorso {yaml_path}")
        return None
    except Exception as e:
        print(f"ERRORE nella lettura del file YAML: {e}")
        return None

def analyze_dataset(dataset_path, yaml_path):
    """Conta le occorrenze delle classi nei file di etichette (.txt)."""
    class_names = read_yaml_classes(yaml_path)
    if not class_names:
        return {}

    class_counts = {class_id: 0 for class_id in class_names.keys()}

    label_search_path = os.path.join(dataset_path, "**", "*.txt")
    label_files = glob.glob(label_search_path, recursive=True)

    if not label_files:
        print(f"ATTENZIONE: Nessun file .txt trovato in {dataset_path}")
        
    # Processa tutti i file di etichette
    for file_path in label_files:
        try:
            with open(file_path, 'r') as f:
                for line in f:
                    parts = line.strip().split()
                    if not parts:
                        continue

                    class_id = int(parts[0])

                    if class_id in class_counts:
                        class_counts[class_id] += 1
        except (ValueError, IndexError):
            continue

    print(f"\nConteggio classi per {dataset_path}: {sum(class_counts.values())} occorrenze totali.")
    return class_counts

def calculate_total_occurrences(counts_dataset, yaml_path, output_csv_file="dataset_analysis.csv"):
    """Somma i conteggi di occorrenza, crea un report e lo salva in CSV."""
    class_names = read_yaml_classes(yaml_path)
    if not class_names:
        return

    total_counts = {class_id: 0 for class_id in class_names.keys()}

    for _, counts in counts_dataset.items():
        for class_id, count in counts.items():
            if class_id in total_counts:
                total_counts[class_id] += count

    output_data = []
    grand_total = 0
    
    for class_id, total_count in sorted(total_counts.items()):
        class_name = class_names.get(class_id, f"Classe {class_id} (sconosciuta)")
        row = {
            "Class ID": class_id,
            "Class Name": class_name,
            "Total Occurrences": total_count
        }
        for name, counts in counts_dataset.items():
            row[name] = counts.get(class_id, 0)
        output_data.append(row)
        grand_total += total_count

    df = pd.DataFrame(output_data)
    
    total_row = {"Class ID": "TOTAL", "Class Name": "", "Total Occurrences": grand_total}
    for name, counts in counts_dataset.items():
        total_row[name] = sum(counts.values())
        
    df = pd.concat([df, pd.DataFrame([total_row])], ignore_index=True)

    try:
        df.to_csv(output_csv_file, index=False)
        print("\n" + "=" * 60)
        print(f"REPORT COMPLETATO: Dati salvati in '{output_csv_file}'")
        print("=" * 60)
        
        print("\nRISULTATI RIASSUNTIVI (Conteggi Totali per Classe):")
        print(df.to_string(index=False))
        
    except Exception as e:
        print(f"ERRORE durante il salvataggio del file CSV: {e}")


if __name__ == '__main__':
    YAML_PATH = 'data.yaml'
    
    TEST_PATH = './test/labels'
    TRAIN_PATH = './train/labels'
    VALID_PATH = './valid/labels'

    test_counts = analyze_dataset(TEST_PATH, YAML_PATH)
    train_counts = analyze_dataset(TRAIN_PATH, YAML_PATH)
    valid_counts = analyze_dataset(VALID_PATH, YAML_PATH)
    
    all_dataset_counts = {
        "Test": test_counts,
        "Train": train_counts,
        "Valid": valid_counts
    }
    
    calculate_total_occurrences(all_dataset_counts, YAML_PATH)