import os
import shutil
import yaml

def copy_images_of_class_into_categories(labels_folder, images_source_folder, base_destination_folder, yaml_config_filepath, target_class_name):
    """
    Copia le immagini che contengono una specifica classe in due cartelle di destinazione:
    - Una per le immagini con solo la classe target.
    - Una per le immagini con la classe target e altre classi.
    """
    single_class_folder = os.path.join(base_destination_folder, f"only_{target_class_name}")
    multi_class_folder = os.path.join(base_destination_folder, f"with_other_classes")

    try:
        os.makedirs(single_class_folder, exist_ok=True)
        os.makedirs(multi_class_folder, exist_ok=True)
    except Exception as e:
        print(f"Errore critico: Impossibile creare o accedere alle cartelle di destinazione: {e}")
        return

    class_name_to_id = {}
    try:
        with open(yaml_config_filepath, 'r', encoding='utf-8') as f:
            yaml_data = yaml.safe_load(f)
        class_names_list = yaml_data.get('names', [])
        if not class_names_list:
            print(f"Errore: Il file YAML '{yaml_config_filepath}' non contiene una lista di nomi delle classi ('names').")
            return
        class_name_to_id = {name: i for i, name in enumerate(class_names_list)}
    except FileNotFoundError:
        print(f"Errore critico: File YAML di configurazione non trovato a '{yaml_config_filepath}'.")
        return
    except yaml.YAMLError as e:
        print(f"Errore critico durante la lettura del file YAML '{yaml_config_filepath}': {e}")
        return

    target_class_id = class_name_to_id.get(target_class_name)
    if target_class_id is None:
        print(f"Errore: Il nome della classe target '{target_class_name}' non è stato trovato nel file YAML.")
        print("Classi disponibili nel YAML:", sorted(class_name_to_id.keys()))
        return

    if not os.path.isdir(labels_folder):
        print(f"Errore critico: La cartella delle etichette '{labels_folder}' non esiste o non è una directory.")
        return

    label_filenames = os.listdir(labels_folder)
    if not label_filenames:
        print(f"Attenzione: Nessun file trovato nella cartella delle etichette '{labels_folder}'.")
        return

    for label_filename in label_filenames:
        if label_filename.endswith(".txt"):
            label_filepath = os.path.join(labels_folder, label_filename)
            base_filename = os.path.splitext(label_filename)[0]

            try:
                with open(label_filepath, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    classes_in_file = set()
                    for line in lines:
                        parts = line.strip().split()
                        if not parts or len(parts) < 1:
                            continue
                        try:
                            class_id = int(parts[0])
                            classes_in_file.add(class_id)
                        except (ValueError, IndexError):
                            continue

                    found_target_class = target_class_id in classes_in_file
                    found_other_class = False
                    
                    if found_target_class:
                        classes_in_file.discard(target_class_id)
                        if classes_in_file:
                            found_other_class = True

                    if found_target_class and not found_other_class:
                        destination_folder = single_class_folder
                    elif found_target_class and found_other_class:
                        destination_folder = multi_class_folder
                    else:
                        continue

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
                                print(f"Errore durante la copia del file '{source_image_path}': {copy_e}")
                    
                    if not image_found:
                         print(f"[AVVISO] Nessuna immagine per '{base_filename}.txt' trovata nella cartella sorgente.")

            except FileNotFoundError:
                print(f"Errore: File di etichetta '{label_filepath}' non trovato. Saltato.")
            except Exception as e:
                print(f"Errore durante l'elaborazione del file di etichetta '{label_filename}': {e}")

if __name__ == "__main__":
    test_labels_output_folder = './dataset7/TrafficSignLocalizationandDetection/valid/labels'
    test_images_source_folder = './dataset7/TrafficSignLocalizationandDetection/filtered_images_Give_Way'
    test_base_destination_folder = './dataset7/filtered_images'
    test_yaml_config_filepath = './dataset7/Custom_data.yaml'
    target_class_name_to_copy = "Give Way"

    copy_images_of_class_into_categories(
        test_labels_output_folder,
        test_images_source_folder,
        test_base_destination_folder,
        test_yaml_config_filepath,
        target_class_name_to_copy
    )