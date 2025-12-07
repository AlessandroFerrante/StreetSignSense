import os
import yaml

def modify_labels_by_name(labels_source_folder, destination_folder, data_yaml_path, old_class_name, new_class_index, images_folder):
    """
    Modifica i file di label, sostituendo l'indice di una specifica classe con un nuovo indice,
    basandosi su un elenco di immagini presenti in una cartella separata.
    """
    try:
        with open(data_yaml_path, 'r') as file:
            data_yaml = yaml.safe_load(file)
            class_names = data_yaml.get('names')
            if not class_names:
                print("Errore: la chiave 'names' non è presente nel file YAML.")
                return
    except FileNotFoundError:
        print(f"Errore: il file YAML '{data_yaml_path}' non è stato trovato.")
        return

    try:
        old_class_index = class_names.index(old_class_name)
    except ValueError:
        print(f"Errore: il nome della classe '{old_class_name}' non è stato trovato nel file YAML.")
        return

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for image_filename in os.listdir(images_folder):
        if os.path.isfile(os.path.join(images_folder, image_filename)):
            base_filename, _ = os.path.splitext(image_filename)
            label_filename = base_filename + ".txt"

            label_source_path = os.path.join(labels_source_folder, label_filename)
            destination_path = os.path.join(destination_folder, label_filename)

            if os.path.exists(label_source_path):
                modified_lines = []

                with open(label_source_path, 'r') as file:
                    lines = file.readlines()

                for line in lines:
                    parts = line.strip().split()
                    if parts and len(parts) > 0:
                        try:
                            if int(parts[0]) == old_class_index:
                                parts[0] = str(new_class_index)
                                modified_lines.append(" ".join(parts))
                            else:
                                modified_lines.append(line.strip())
                        except ValueError:
                            modified_lines.append(line.strip())

                with open(destination_path, 'w') as file:
                    file.write("\n".join(modified_lines))
            else:
                print(f"Attenzione: file di label '{label_filename}' non trovato in '{labels_source_folder}'.")

labels_source_folder = "./curveandspeedlimitv3/train/right/labels"
images_folder = "./curveandspeedlimitv3/train/right/images"
destination_folder = "./curveandspeedlimitv3/train/right/newlabels"
data_yaml_path = "./curveandspeedlimitv3/train/right/data.yaml"

old_class = "dangerous_left_curve"
new_index = 58

modify_labels_by_name(labels_source_folder, destination_folder, data_yaml_path, old_class, new_index, images_folder)