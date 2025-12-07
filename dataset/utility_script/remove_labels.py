import yaml
import os

def filter_dataset(data_yaml_path, labels_dir, desired_classes_names):
    """
    Filtra un dataset rimuovendo le classi non desiderate dai file di etichette.
    """
    with open(data_yaml_path, 'r') as f:
        data_yaml = yaml.safe_load(f)

    class_names = data_yaml['names']
    class_name_to_id = {name: i for i, name in enumerate(class_names)}
    
    desired_class_ids = [class_name_to_id[name] for name in desired_classes_names if name in class_name_to_id]
    
    if not desired_class_ids:
        print("Nessuna delle classi desiderate è stata trovata nel file data.yaml.")
        return

    for filename in os.listdir(labels_dir):
        if filename.endswith('.txt'):
            filepath = os.path.join(labels_dir, filename)
            
            with open(filepath, 'r') as f:
                lines = f.readlines()
            
            new_lines = []
            for line in lines:
                parts = line.strip().split()
                if not parts:
                    continue
                
                class_id = int(parts[0])
                
                if class_id in desired_class_ids:
                    new_lines.append(line)
            
            with open(filepath, 'w') as f:
                f.writelines(new_lines)

if __name__ == "__main__":
    DATA_YAML_PATH = './V6_Traffic_Signs/data.yaml'
    LABELS_DIRECTORY = './V6_Traffic_Signs/train/mand_round/labels'
    DESIRED_CLASSES = [
        'warn_construction', 'warn_roundabout', 'mand_go_left_right', 
        'mand_go_right', 'mand_go_straight', 'mand_go_straight_left', 
        'mand_go_straight_right', 'mand_pass_left', 'mand_pass_left_right', 
        'mand_pass_right', 'mand_roundabout'
    ]

    filter_dataset(DATA_YAML_PATH, LABELS_DIRECTORY, DESIRED_CLASSES)