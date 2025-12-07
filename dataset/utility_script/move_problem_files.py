import os
import shutil
from pathlib import Path

images_dir = Path("./curveandspeedlimitv3/train/right/images")
labels_dir = Path("./curveandspeedlimitv3/train/right/newlabels")
output_dir = Path("./curveandspeedlimitv3/train/immagini_e_label_con_problemi")

def move_problem_files(image_names: list, source_images_path: Path, source_labels_path: Path, destination_path: Path):
    """
    Sposta le immagini e i loro file di label corrispondenti in una cartella di destinazione.
    """
    if not image_names:
        return

    destination_path.mkdir(exist_ok=True)
    
    print(f"\nSpostamento di {len(image_names)} immagini e dei loro label nella cartella '{destination_path}'...")
    
    for image_name in image_names:
        source_image = source_images_path / image_name
        destination_image = destination_path / image_name

        label_filename = Path(image_name).stem + ".txt"
        source_label = source_labels_path / label_filename
        destination_label = destination_path / label_filename
        
        try:
            shutil.move(source_image, destination_image)
            shutil.move(source_label, destination_label)
        except FileNotFoundError:
            print(f"ATTENZIONE: File non trovato durante lo spostamento: {image_name} o {label_filename}")
        except Exception as e:
            print(f"ERRORE durante lo spostamento di {image_name} e {label_filename}: {e}")

def check_label_files(images_path: Path, labels_path: Path):
    """
    Conta e elenca i file di label mancanti e vuoti.
    """
    if not images_path.is_dir():
        print(f"ERRORE: La cartella delle immagini non è stata trovata: {images_path}")
        return
    if not labels_path.is_dir():
        print(f"ERRORE: La cartella delle etichette non è stata trovata: {labels_path}")
        return

    missing_labels = []
    empty_labels = []

    image_files = [f for f in images_path.iterdir() if f.is_file() and f.suffix.lower() in [".jpg", ".jpeg", ".png", ".bmp", ".webp"]]
    
    total_images = len(image_files)

    if total_images == 0:
        print(f"ATTENZIONE: Nessun file immagine trovato nella cartella: {images_path}")
        return
    
    for image_file in image_files:
        label_filename = image_file.stem + ".txt"
        label_file_path = labels_path / label_filename

        if not label_file_path.exists():
            missing_labels.append(image_file.name)
        else:
            if os.path.getsize(label_file_path) == 0:
                empty_labels.append(image_file.name)

    print("=" * 40)
    print("RAPPORTO SUL CONTROLLO DEI FILE DI LABEL")
    print("=" * 40)
    print(f"Totale immagini trovate: {total_images}")
    print("-" * 40)
    print(f"File di label mancanti: {len(missing_labels)}")
    if missing_labels:
        print("Elenco dei file di label mancanti:")
        for file in missing_labels:
            print(f"  - {file}")
    print("-" * 40)
    print(f"File di label vuoti: {len(empty_labels)}")
    if empty_labels:
        print("Elenco dei file di label vuoti:")
        for file in empty_labels:
            print(f"  - {file}")
    print("=" * 40)

    all_problem_images = missing_labels + empty_labels
    if all_problem_images:
        move_problem_files(all_problem_images, images_dir, labels_dir, output_dir)
        print("Spostamento completato.")
    else:
        print("\nNessun file problematico trovato, nessuna immagine da spostare.")

if __name__ == "__main__":
    check_label_files(images_dir, labels_dir)