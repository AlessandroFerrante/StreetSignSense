import os
import yaml
from collections import Counter

# --- CONFIGURAZIONE UTENTE ---
MAIN_DATASET_ROOT = './curveandspeedlimitv12/'
SOURCE_DATASET_ROOT = './curveandspeedlimitv12/train/'
OUTPUT_DATASET_ROOT = './curveandspeedlimitv12/train/mapping'

# Mappatura delle classi
SOURCE_TO_MAIN_NAME_MAPPING = {
    # Segnali di pericolo
    # "Danger Ahead": "warn_other_dangers",
    # "Deer Zone": "warn_wild_animals",
    # "Huddle Road": "warn_poor_road_surface",
    # "Left Curve Ahead": "dangerous_left_curve",
    # "Left Sharp Curve": "left_sharp_curve",
    # "Pedestrian": "warn_crosswalk",
    # "Right Curve Ahead": "dangerous_right_curve",
    # "Right Sharp Curve": "right_sharp_curve",
    # "Road Work": "warn_construction",
    # "RoundAbout": "mand_roundabout",
    # "Slippery Road": "warn_slippery_road",
    # "Traffic Signals Ahead": "warn_traffic_light",
    # "Cycle Zone": "warn_cyclists",

    # # Segnali di divieto
    # "No Entry": "forb_ahead",
    # "No Over Taking Trucks": "forb_overtake_truck",
    # "No Over Taking": "forb_overtake_car",
    # "No Stopping": "forb_stopping",
    # "No Waiting": "forb_no_parking",
    # "Truck Sign": "forb_trucks",
    # 
    # # Limiti di velocità
    # "Speed Limit 100": "forb_speed_over_100",
    # "Speed Limit 120": "forb_speed_over_120",
    # "Speed Limit 20": "forb_speed_over_20",
    # "Speed Limit 30": "forb_speed_over_30",
    # "Speed Limit 50": "forb_speed_over_50",
    # "Speed Limit 60": "forb_speed_over_60",
    # "Speed Limit 70": "forb_speed_over_70",
    # "Speed Limit 80": "forb_speed_over_80",
 
    # # Segnali di precedenza
    # "Give Way": "prio_give_way",
    # "Stop": "prio_stop",
 
    # # Segnali di obbligo
    # "Go Left or Straight": "mand_straigh_left",
    # "Go Right or Straight": "mand_straight_right",
    # "Go Straight": "mand_straight",
    # "Turn Left": "mand_left",
    # "Turn Right": "mand_right",
    # "End of Right Road -Go straight-": "mand_straight",
    # 'speed_limit_20': 'forb_speed_over_20',
    # 'speed_limit_30': 'forb_speed_over_30',
    # 'speed_limit_40': 'forb_speed_over_40',
    # 'speed_limit_50': 'forb_speed_over_50',
    # 'speed_limit_60': 'forb_speed_over_60',
    # 'speed_limit_70': 'forb_speed_over_70',
    # 'speed_limit_80': 'forb_speed_over_80',
    # 'speed_limit_90': 'forb_speed_over_90'

    #'forb_overtake': 'forb_overtake_car',
    #'speedlimit90': 'forb_speed_over_90'

    # 'divietodisosta' : 'forb_no_parking',
    # 'divietodiaccesso' : 'forb_ahead',
    # 'give_way' : 'prio_give_way', 
    # 'mand_around' : 'mand_roundabout', 
    # 'mand_straight' : 'mand_straight', 
    # 'mand_straight_left' : 'mand_straigh_left', 
    # 'stop': 'prio_stop'

    # 'curve_left': 'dangerous_left_curve',
    # 'curve_right': 'dangerous_right_curve',
    # 'forb_truck': 'forb_trucks',
    # 'left_sharpe': 'left_sharp_curve',
    # 'mand_around': 'mand_roundabout',
    # 'mand_pass_left': 'mand_pass_left',
    # 'mand_pass_left_right': 'mand_pass_left_right',
    # 'mand_pass_right': 'mand_pass_right',
    # 'mand_straight': 'mand_straight',
    # 'mand_straight_left': 'mand_straigh_left',
    # 'overtake': 'forb_overtake_car',
    # 'overtake_truck': 'forb_overtake_truck',
    # 'right_sharpe': 'right_sharp_curve',
    # 'speedlimit5': 'forb_speed_over_5',
    # 'speedlimit10': 'forb_speed_over_10',
    # 'speedlimit20': 'forb_speed_over_20',
    # 'speedlimit40': 'forb_speed_over_40',
    # 'speedlimit50': 'forb_speed_over_50',
    # 'speedlimit60': 'forb_speed_over_60',
    # 'speedlimit80': 'forb_speed_over_80',
    # 'speedlimit90': 'forb_speed_over_90',
    # 'speedlimit100': 'forb_speed_over_100',
    # 'speedlimit110': 'forb_speed_over_110',
    # 'speedlimit120': 'forb_speed_over_120',
    # 'speedlimit130': 'forb_speed_over_130',
    # 'traffic_lights': 'warn_traffic_light',
    # 'warn_animals': 'warn_wild_animals',
    # 'warn_other_dangers': 'warn_other_dangers',
    # 'warn_poor_road_surface': 'warn_poor_road_surface',
    # 'warn_round': 'warn_roundabout',
    # 'warn_slippery_road': 'warn_slippery_road',
    # 'warn_speed_bumper': 'warn_speed_bumper'

    # ============= REVERSE MAPPING FOR NEW LABELS V4 ===========
    #'prio_give_way': 'prio_give_way',
    #'prio_stop': 'prio_stop',
    #'prio_priority_road': 'prio_priority_road',
    #'forb_speed_over_5': 'forb_speed_over_5',
    #'forb_speed_over_10': 'forb_speed_over_10',
    #'forb_speed_over_20': 'forb_speed_over_20',
    #'forb_speed_over_30': 'forb_speed_over_30',
    #'forb_speed_over_40': 'forb_speed_over_40',
    #'forb_speed_over_50': 'forb_speed_over_50',
    #'forb_speed_over_60': 'forb_speed_over_60',
    #'forb_speed_over_70': 'forb_speed_over_70',
    #'forb_speed_over_80': 'forb_speed_over_80',
    #'forb_speed_over_90': 'forb_speed_over_90',
    #'forb_speed_over_100': 'forb_speed_over_100',
    #'forb_speed_over_110': 'forb_speed_over_110',
    #'forb_speed_over_120': 'forb_speed_over_120',
    #'forb_speed_over_130': 'forb_speed_over_130',
    #'forb_ahead': 'forb_no_entry',
    #'forb_no_parking': 'forb_no_parking',
    #'forb_stopping': 'forb_no_stopping',
    #'forb_overtake_car': 'forb_overtake_car',
    #'forb_overtake_truck': 'forb_overtake_trucks',
    #'forb_trucks': 'forb_trucks',
    #'forb_left': 'forb_turn_left',
    #'forb_right': 'forb_turn_right',
    #'forb_u_turn': 'forb_u_turn',
    #'forb_weight_over_3.5t':'forb_weight_over_3.5t',
    #'forb_weight_over_7.5t':'forb_weight_over_7.5t',
    #'info_bus_station': 'info_bus_station',
    #'info_crosswalk': 'info_crosswalk',
    #'info_highway': 'info_highway',
    #'info_one_way_traffic': 'info_one_way',
    #'info_parking': 'info_parking',
    #'info_taxi_parking': 'info_taxi_parking',
    #'warn_children': 'warn_children',
    #'warn_construction': 'warn_construction',
    #'warn_crosswalk': 'warn_crosswalk',
    #'warn_cyclists': 'warn_cyclists',
    #'dangerous_left_curve': 'warn_left_curve',
    #'dangerous_right_curve': 'warn_right_curve',
    #'warn_domestic_animals': 'warn_domestic_animals',
    #'warn_other_dangers': 'warn_other_dangers',
    #'warn_poor_road_surface': 'warn_poor_road_surface',
    #'warn_roundabout': 'warn_roundabout',
    #'left_sharp_curve': 'warn_sharp_left_curve',
    #'right_sharp_curve': 'warn_sharp_right_curve',
    #'warn_slippery_road': 'warn_slippery_road',
    #'warn_speed_bumper': 'warn_hump',
    #'warn_traffic_light': 'warn_traffic_light',
    #'warn_tram': 'warn_tram',
    #'warn_two_way_traffic': 'warn_two_way_traffic',
    #'warn_wild_animals': 'warn_wild_animals',
    #'mand_bike_lane': 'mand_bike_lane',
    #'mand_left': 'mand_go_left',
    #'mand_left_right': 'mand_go_left_right',
    #'mand_right': 'mand_go_right',
    #'mand_straight': 'mand_go_straight',
    #'mand_straigh_left': 'mand_go_straight_left',
    #'mand_straight_right': 'mand_go_straight_right',
    #'mand_pass_left': 'mand_pass_left',
    #'mand_pass_left_right': 'mand_pass_left_right',
    #'mand_pass_right': 'mand_pass_right',
    #'mand_roundabout': 'mand_roundabout'
    # ===================================================

    "curve_left": "warn_left_curve",
    "curve_right": "warn_right_curve",
    "forb_truck": "forb_trucks",
    "left_sharpe": "warn_sharp_left_curve",
    "mand_around": "mand_roundabout",
    "mand_pass_left": "mand_pass_left",
    "mand_pass_left_right": "mand_pass_left_right",
    "mand_pass_right": "mand_pass_right",
    "mand_straight": "mand_go_straight",
    "mand_straight_left": "mand_go_straight_left",
    "overtake": "forb_overtake_car",
    "overtake_truck": "forb_overtake_trucks",
    "right_sharpe": "warn_sharp_right_curve",
    "speedlimit10": "forb_speed_over_10",
    "speedlimit100": "forb_speed_over_100",
    "speedlimit110": "forb_speed_over_110",
    "speedlimit120": "forb_speed_over_120",
    "speedlimit130": "forb_speed_over_130",
    "speedlimit20": "forb_speed_over_20",
    "speedlimit40": "forb_speed_over_40",
    "speedlimit5": "forb_speed_over_5",
    "speedlimit50": "forb_speed_over_50",
    "speedlimit60": "forb_speed_over_60",
    "speedlimit80": "forb_speed_over_80",
    "speedlimit90": "forb_speed_over_90",
    "traffic_lights": "warn_traffic_light",
    "warn_animals": "warn_domestic_animals",
    "warn_other_dangers": "warn_other_dangers",
    "warn_poor_road_surface": "warn_poor_road_surface",
    "warn_round": "warn_roundabout",
    "warn_slippery_road": "warn_slippery_road",
    "warn_speed_bumper": "warn_hump"
}

DROP_UNMAPPED = True

# --- SCRIPT PRINCIPALE ---
os.makedirs(os.path.join(OUTPUT_DATASET_ROOT, 'labels'), exist_ok=True)

try:
    main_yaml_path = os.path.join(MAIN_DATASET_ROOT, 'data.yaml')
    source_yaml_path = os.path.join(SOURCE_DATASET_ROOT, 'data.yaml')

    with open(main_yaml_path, 'r') as f:
        main_data = yaml.safe_load(f)
    with open(source_yaml_path, 'r') as f:
        source_data = yaml.safe_load(f)
except FileNotFoundError as e:
    print(f"ERRORE: Impossibile trovare il file data.yaml. Controlla i percorsi forniti.")
    print(f"Dettagli: {e}")
    exit()

main_names = main_data['names']
source_names = source_data['names']

main_name_to_idx = {name: i for i, name in enumerate(main_names)}

target_missing = [dst for dst in SOURCE_TO_MAIN_NAME_MAPPING.values() if dst not in main_name_to_idx]
if target_missing:
    raise ValueError(f"ERRORE: Le seguenti classi di destinazione specificate nella mappa non esistono nel dataset principale: {target_missing}")

source_to_main_idx = {}
for src_name, dst_name in SOURCE_TO_MAIN_NAME_MAPPING.items():
    if src_name not in source_names:
        print(f"ATTENZIONE: La classe di origine '{src_name}' definita nella mappa non esiste nel file data.yaml del dataset di origine. Verrà ignorata.")
        continue
    source_to_main_idx[src_name] = main_name_to_idx[dst_name]

LABELS_IN_DIR = os.path.join(SOURCE_DATASET_ROOT, 'labels')
LABELS_OUT_DIR = os.path.join(OUTPUT_DATASET_ROOT, 'labels')

if not os.path.isdir(LABELS_IN_DIR):
    print(f"\nERRORE: La cartella delle etichette di origine non è stata trovata al percorso: {LABELS_IN_DIR}")
    exit()

converted_counts = Counter()
skipped_counts = Counter()
files_processed = 0
files_out = 0

label_files = [f for f in os.listdir(LABELS_IN_DIR) if f.endswith('.txt')]

if not label_files:
    print("ATTENZIONE: Nessun file .txt trovato nella cartella delle etichette di origine.")

for fname in label_files:
    files_processed += 1
    in_path = os.path.join(LABELS_IN_DIR, fname)
    with open(in_path, 'r') as f:
        lines = [ln.strip() for ln in f.readlines() if ln.strip()]

    new_lines = []
    for ln in lines:
        parts = ln.split()
        try:
            cls_idx = int(parts[0])
            bbox = parts[1:]
        except (ValueError, IndexError):
            print(f"ATTENZIONE: Riga malformata nel file '{fname}': '{ln}'. Verrà saltata.")
            continue

        if 0 <= cls_idx < len(source_names):
            src_name = source_names[cls_idx]
            if src_name in source_to_main_idx:
                new_cls_idx = source_to_main_idx[src_name]
                new_lines.append(' '.join([str(new_cls_idx)] + bbox))
                converted_counts[src_name] += 1
            else:
                skipped_counts[src_name] += 1
                if not DROP_UNMAPPED:
                    new_lines.append(ln)
        else:
            print(f"ATTENZIONE: Indice di classe non valido '{cls_idx}' trovato nel file '{fname}'. Verrà saltato.")
            if not DROP_UNMAPPED:
                new_lines.append(ln)

    if new_lines:
        out_path = os.path.join(LABELS_OUT_DIR, fname)
        with open(out_path, 'w') as f:
            f.write('\n'.join(new_lines) + '\n')
        files_out += 1

print("\n== RIEPILOGO DELLA CONVERSIONE ==")
print(f"File di etichette totali elaborati: {files_processed}")
print(f"File di etichette scritti nella cartella di output: {files_out}")

if converted_counts:
    print("\nStatistiche classi CONVERTITE (Origine -> Conteggio BBox):")
    for k, v in sorted(converted_counts.items()):
        print(f"  '{k}': {v} bounding box convertiti in '{SOURCE_TO_MAIN_NAME_MAPPING[k]}'")
if skipped_counts:
    print("\nStatistiche classi IGNORATE (non mappate):")
    for k, v in sorted(skipped_counts.items()):
        print(f"  '{k}': {v} bounding box ignorati")