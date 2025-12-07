import os
import shutil
import yaml 

def copy_images_of_class(labels_folder, images_source_folder, destination_folder, yaml_config_filepath, target_class_name):
    """
    Copia le immagini che contengono una specifica classe (identificata dal nome)
    in una cartella di destinazione.
    """
    try:
        os.makedirs(destination_folder, exist_ok=True)
    except Exception as e:
        print(f"Errore: Impossibile creare o accedere alla cartella di destinazione '{destination_folder}': {e}")
        return 

    class_name_to_id = {}
    class_id_to_name = {}
    try:
        with open(yaml_config_filepath, 'r', encoding='utf-8') as f:
            yaml_data = yaml.safe_load(f)

        class_names_list = yaml_data.get('names', [])
        if not class_names_list:
            print(f"Errore: Il file YAML '{yaml_config_filepath}' non contiene una lista di nomi delle classi ('names').")
            return

        class_name_to_id = {name: i for i, name in enumerate(class_names_list)}
        class_id_to_name = {i: name for i, name in enumerate(class_names_list)}

    except FileNotFoundError:
        print(f"Errore  : File YAML di configurazione non trovato a '{yaml_config_filepath}'. Assicurati che il percorso sia corretto.")
        return
    except yaml.YAMLError as e:
        print(f"Errore   durante la lettura del file YAML '{yaml_config_filepath}': {e}")
        return
    except Exception as e:
        print(f"Si è verificato un errore inatteso durante la lettura del YAML: {e}")
        return

    target_class_id = class_name_to_id.get(target_class_name)

    if target_class_id is None:
        print(f"Errore: Il nome della classe target '{target_class_name}' non è stato trovato nel file YAML.")
        print("Classi disponibili nel YAML:")
        for class_id, class_name in sorted(class_id_to_name.items()):
             print(f"  ID {class_id}: '{class_name}'")
        print("Assicurati che il nome della classe target sia scritto esattamente come nel file YAML.")
        return

    if not os.path.isdir(labels_folder):
        print(f"Errore  : La cartella delle etichette '{labels_folder}' non esiste o non è una directory.")
        return

    label_filenames = os.listdir(labels_folder)
    if not label_filenames:
        print(f"Attenzione: Nessun file trovato nella cartella delle etichette '{labels_folder}'. Controlla il percorso.")
        return

    for label_filename in label_filenames:
        if label_filename.endswith(".txt"):
            label_filepath = os.path.join(labels_folder, label_filename)
            base_filename = os.path.splitext(label_filename)[0]

            try:
                with open(label_filepath, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    found_class_in_image = False
                    for i, line in enumerate(lines):
                        parts = line.strip().split()
                        if not parts:
                            continue
                        if len(parts) < 5:
                            print(f"Attenzione: Riga malformata nel file '{label_filename}' (riga {i+1}): '{line.strip()}'. Richiesti almeno 5 elementi (class_id, x, y, w, h). Saltata.")
                            continue
                        try:
                            class_id_in_file = int(parts[0])
                            if class_id_in_file == target_class_id:
                                found_class_in_image = True
                                break 
                        except ValueError:
                            print(f"Attenzione: Impossibile convertire l'ID classe a numero intero nel file '{label_filename}' (riga {i+1}): '{parts[0]}'. Saltata riga.")
                            continue
                        except IndexError:
                             print(f"Attenzione: Manca l'ID classe nella riga '{label_filename}' (riga {i+1}): '{line.strip()}'. Saltata riga.")
                             continue

                    if found_class_in_image:
                        image_found = False
                        common_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.webp']
                        for ext in common_extensions:
                            source_image_path = os.path.join(images_source_folder, base_filename + ext)
                            if os.path.exists(source_image_path):
                                destination_image_path = os.path.join(destination_folder, base_filename + ext)
                                try:
                                    shutil.copy2(source_image_path, destination_image_path)
                                    image_found = True
                                    break 
                                except Exception as copy_e:
                                     print(f"Errore durante la copia del file '{source_image_path}' a '{destination_image_path}': {copy_e}")
                        if not image_found:
                             print(f"[AVVISO] Nessuna immagine per '{base_filename}.txt' trovata nella cartella sorgente '{images_source_folder}' con le estensioni comuni.")

            except FileNotFoundError:
                print(f"Errore: File di etichetta '{label_filepath}' non trovato. Questo non dovrebbe accadere con os.listdir, ma per sicurezza.")
            except Exception as e:
                print(f"Errore durante l'elaborazione del file di etichetta '{label_filename}': {e}")

if __name__ == "__main__":
    test_labels_output_folder = 'labels/'
    test_images_source_folder = './dataset7/Traff./dataset7/TrafficSignLocalizationandDetection/train/icSignLocalizationandDetection/train/images/'
    test_destination_folder = './dataset7/TrafficSignLocalizationandDetection/train/filtered_images_Huddle_Road'
    test_yaml_config_filepath = './dataset7/Custom_data.yaml'
    target_class_name_to_copy = "Huddle Road"

    copy_images_of_class(
        test_labels_output_folder,
        test_images_source_folder,
        test_destination_folder,
        test_yaml_config_filepath,
        target_class_name_to_copy
    )