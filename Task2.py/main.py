import os
import csv
import json
import pickle

__all__ = ['scan_files', 'create_json_file', 'create_csv_file', 'create_binary_file']


def scan_files(path: str) -> list:
    scan_list = list(os.walk(path))
    res_list = []

    for dir in scan_list:
        temp_list_files = os.listdir(dir[0])
        for file in temp_list_files:
            temp_dict = {"name": file, "parent": dir[0].split('\\')[-1]}
            full_path_file = os.path.join(dir[0], file)
            if os.path.isdir(full_path_file):
                temp_dict["type"] = "dir"
            elif os.path.isfile(full_path_file):
                temp_dict["type"] = "file"
            else:
                temp_dict["type"] = "unknown"

            temp_dict["size"] = os.path.getsize(full_path_file)
            res_list.append(temp_dict)

    return res_list


def create_json_file(data: list):
    with(
        open('json_dump_file.json', 'w', encoding='utf-8') as f1,
        open('json_dumps_file.json', 'w', encoding='utf-8') as f2
    ):
        json.dump(data, f1)

        temp_str = json.dumps(data, ensure_ascii=False, indent=2, separators=('#', '| '), sort_keys=True)
        json.dump(temp_str, f2)


def create_csv_file(data: list):
    with open('csv_file.csv', 'w', newline='', encoding='utf-8') as f:
        csv_writer = csv.DictWriter(f, fieldnames=["name", "parent", "type", "size"], dialect='excel', quotechar='|',
                                    quoting=csv.QUOTE_MINIMAL)
        csv_writer.writeheader()
        csv_writer.writerows(data)


def create_binary_file(data: list):
    with(
        open('pickle_dump_file', 'wb') as f1,
        open('pickle_dumps_file', 'wb') as f2
    ):
        pickle.dump(data, f1)
        temp_str = pickle.dumps(data, protocol=pickle.DEFAULT_PROTOCOL)
        pickle.dump(temp_str, f2)