import os
import shutil

def move_files_based_on_list(source_folder_images, source_folder_labels, list_folder, destination_folder_images, destination_folder_labels):
    """
    Sposta le immagini e i loro file di etichetta corrispondenti che si trovano
    nella cartella di riferimento.

    Args:
        source_folder_images (str): La cartella da cui spostare le immagini (es. la cartella originale 'images').
        source_folder_labels (str): La cartella da cui spostare i file di etichetta (es. la cartella originale 'labels').
        list_folder (str): La cartella che contiene la lista dei nomi dei file da spostare.
                           (es. la cartella 'only_prio_give_way').
        destination_folder_images (str): La cartella di destinazione per le immagini.
        destination_folder_labels (str): La cartella di destinazione per le etichette.
    """
    print(f"Inizio operazione di spostamento file.")
    print(f"Cartella di origine immagini: {source_folder_images}")
    print(f"Cartella di origine etichette: {source_folder_labels}")
    print(f"Cartella di riferimento per la lista file: {list_folder}")
    print(f"Cartella di destinazione immagini: {destination_folder_images}")
    print(f"Cartella di destinazione etichette: {destination_folder_labels}")

    try:
        os.makedirs(destination_folder_images, exist_ok=True)
        os.makedirs(destination_folder_labels, exist_ok=True)
        print("Cartelle di destinazione create/verificate.")
    except Exception as e:
        print(f"Errore critico: Impossibile creare le cartelle di destinazione: {e}")
        return

    # Ottieni la lista dei nomi di base dei file dalla cartella di riferimento
    if not os.path.isdir(list_folder):
        print(f"Errore: La cartella di riferimento '{list_folder}' non esiste o non è una directory.")
        return

    file_list = [os.path.splitext(f)[0] for f in os.listdir(list_folder) if os.path.isfile(os.path.join(list_folder, f))]
    if not file_list:
        print(f"Attenzione: Nessun file trovato nella cartella di riferimento '{list_folder}'. Nessun file verrà spostato.")
        return

    print(f"Trovati {len(file_list)} nomi di base di file da spostare.")
    
    moved_count = 0
    skipped_count = 0

    for base_filename in file_list:
        image_moved = False
        common_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.webp']
        for ext in common_extensions:
            source_image_path = os.path.join(source_folder_images, base_filename + ext)
            if os.path.exists(source_image_path):
                destination_image_path = os.path.join(destination_folder_images, base_filename + ext)
                try:
                    shutil.move(source_image_path, destination_image_path)
                    print(f"[OK] Spostato immagine: {base_filename + ext}")
                    image_moved = True
                    moved_count += 1
                    break  
                except Exception as e:
                    print(f"Errore durante lo spostamento dell'immagine '{source_image_path}': {e}")
                    
                    
        if not image_moved:
            print(f"[AVVISO] Immagine per '{base_filename}' non trovata nella cartella sorgente. Saltata.")
            skipped_count += 1
            
        source_label_path = os.path.join(source_folder_labels, base_filename + ".txt")
        if os.path.exists(source_label_path):
            destination_label_path = os.path.join(destination_folder_labels, base_filename + ".txt")
            try:
                shutil.move(source_label_path, destination_label_path)
                print(f"[OK] Spostato etichetta: {base_filename + '.txt'}")
            except Exception as e:
                print(f"Errore durante lo spostamento dell'etichetta '{source_label_path}': {e}")
        # else:
            # print(f"[AVVISO] File di etichetta per '{base_filename}' non trovato. Saltato.")


    print(f"\n== RIEPILOGO SPOSTAMENTO ==")
    print(f"File di base da spostare trovati: {len(file_list)}")
    print(f"Immagini e etichette spostate con successo: {moved_count}")
    print(f"File non trovati/saltati: {skipped_count}")
    print("Operazione completata!")

# --- Esempio di utilizzo ---
if __name__ == "__main__":
    #  # cartella 'images' e 'labels' 
    #  test_source_images_folder
    #  = './V2_Traffic_Signs/valid/images'
    #  test_source_labels_folder = './V2_Traffic_Signs/valid/labels'
    #  
    #  # cartella che contiene i file da spostare
    #  test_list_folder = './dataset/filtered_images/only_prio_give_way'
    #  
    #  # nuove cartelle di destinazione immagini e etichette spostate
    #  test_destination_images_folder = './dataset/valid/archived/give_way/images'
    #  test_destination_labels_folder = './dataset/valid/archived/give_way/labels'

    test_source_images_folder = './V6_Traffic_Signs/valid/OLD_warn_left_curve'
    test_source_labels_folder = './V6_Traffic_Signs/valid/labels'  
    # La cartella creata dallo script precedente che contiene i file da spostare
    test_list_folder = './V6_Traffic_Signs/valid/OLD_warn_left_curve'
    # nuove cartelle di destinazione per immagini e etichette spostate
    test_destination_images_folder = './V6_Traffic_Signs/valid/OLD_warn_left_curve/images'
    test_destination_labels_folder = './V6_Traffic_Signs/valid/OLD_warn_left_curve/labels'

    move_files_based_on_list(
        test_source_images_folder,
        test_source_labels_folder,
        test_list_folder,
        test_destination_images_folder,
        test_destination_labels_folder
    )
    print("Script di spostamento file completato.")
