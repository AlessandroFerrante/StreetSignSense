import os
import sys
from collections import defaultdict
import json
import yaml

def load_class_names_from_yaml(yaml_path):
    try:
        with open(yaml_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
            if 'names' in data and isinstance(data['names'], list):
                print(f"Classi trovte in data.yaml")
                return data['names']
            else:
                print(f"Error: 'names' non è valido") #! co 
                return None
    except Exception as e:
        print(f"Error YAML: {e}")
        return None

def load_progressives(progressives_file_path):
    try:
        if os.path.exists(progressives_file_path):
            with open(progressives_file_path, 'r', encoding='utf-8') as f:
                progressives = json.load(f)
                return defaultdict(lambda: 1, {int(k): v for k, v in progressives.items()})
        else:
            return defaultdict(lambda: 1)
    except Exception:
        return defaultdict(lambda: 1)

def save_progressives(progressives_dict, progressives_file_path):
    try:
        with open(progressives_file_path, 'w', encoding='utf-8') as f:
            json.dump(progressives_dict, f, indent=4)
    except Exception as e:
        print(f"Error salvataggio: {e}")

def rename_dataset_files(image_dir, label_dir, class_names, progressives_file_path):
    print("\nLoad...")
    
    class_progressives = load_progressives(progressives_file_path)
    image_extensions = ['.jpg', '.jpeg', '.png']
    renamed_count = 0

    label_files = sorted(os.listdir(label_dir))

    if not label_files:
        print(f"Cartella vuota: '{label_dir}'")
        return

    for label_filename in label_files:
        if not label_filename.endswith('.txt'):
            continue

        base_name = os.path.splitext(label_filename)[0]
        label_path = os.path.join(label_dir, label_filename)

        #? find imsge with label
        image_path = None
        original_ext = None
        for ext in image_extensions:
            potential_image_path = os.path.join(image_dir, base_name + ext)
            if os.path.exists(potential_image_path):
                image_path = potential_image_path
                original_ext = ext
                break
        
        if not image_path:
            continue

        class_counts = defaultdict(list)
        
        try:
            with open(label_path, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    parts = line.strip().split()
                    if not parts: continue
                    class_id = int(parts[0])
                    class_counts[class_id].append(0)
        except Exception as e:
            print(f"Error reading '{label_filename}': {e}")
            continue

        if not class_counts:
            continue

        new_name_parts = []
        sorted_class_ids = sorted(class_counts.keys())

        for class_id in sorted_class_ids:
            if class_id >= len(class_names):
                print(f"ID class invalido: {class_id}") #! an
                new_name_parts = [] 
                break
            
            start_progressive = class_progressives[class_id]
            count = len(class_counts[class_id])
            end_progressive = start_progressive + count

            class_name = class_names[class_id]
            
            #? string progressives (es: 1-2-3)
            progressives = '-'.join(str(i) for i in range(start_progressive, end_progressive))
            new_name_parts.append(f"{class_name}-{progressives}")
            
            class_progressives[class_id] = end_progressive
            
        if not new_name_parts:
            continue

        new_base_name = '~'.join(new_name_parts)
        new_image_path = os.path.join(image_dir, new_base_name + original_ext)
        new_label_path = os.path.join(label_dir, new_base_name + '.txt')

        try:
            os.rename(image_path, new_image_path)
            os.rename(label_path, new_label_path)
            print(f"Rinominato: {base_name} -> {new_base_name}")
            renamed_count += 1
        except OSError as e:
            print(f"Error rename '{base_name}': {e}")

    print(f"\nCompletato. Totale: {renamed_count}")
    save_progressives(class_progressives, progressives_file_path)

def main():
    print("Rinomina Dataset")
    
    image_dir = './test/images'
    label_dir = './test/labels'
    
    yaml_path = os.path.join(os.getcwd(), 'data.yaml')
    progressives_file_path = os.path.join(os.getcwd(), 'progressives.txt')

    if not os.path.isdir(image_dir) or not os.path.isdir(label_dir):
        print("Cartelle non trovate.")
        sys.exit(1)
        
    class_names = load_class_names_from_yaml(yaml_path)
    if class_names is None:
        sys.exit(1)

    rename_dataset_files(image_dir, label_dir, class_names, progressives_file_path)

if __name__ == '__main__':
    main()