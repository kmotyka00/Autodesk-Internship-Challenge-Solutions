import json

def update_operations_runtimes(runtimes, entry):
    # Check if operation is specified
    if 'operation' not in entry:
        return

    # Check is operation is in result dictionary
    if entry['operation'] not in runtimes:
        runtimes[entry['operation']] = 0

    # Check if operation runtime is an integer
    if type(entry['length']) is not int:
        return

    runtimes[entry['operation']] += entry['length']

def update_softwares_runtimes(runtimes, entry):
    # Check if operation is specified
    if 'software' not in entry:
        return

    # Check is operation is in result dictionary
    if entry['software'] not in runtimes:
        runtimes[entry['software']] = 0

    # Check if operation runtime is an integer
    if type(entry['length']) is not int:
        return

    runtimes[entry['software']] += entry['length']

def parse_json(path: str):
    
    with open(path) as file:
        runtime_entries = json.load(file)

    operations_runtimes = dict()
    software_runtimes = dict()

    for entry in runtime_entries:

        update_operations_runtimes(operations_runtimes, entry)
        update_softwares_runtimes(software_runtimes, entry)

    print(f"\nOperation which takes longest time: {get_longest_operation(operations_runtimes)}")
    print(f"Softwares sorted by runtime descending: {sort_softwares_by_runtime(software_runtimes)}\n")

def get_longest_operation(runtimes):
    return max(runtimes, key=runtimes.get)

def sort_softwares_by_runtime(runtimes):
    return sorted(runtimes.keys(), key=lambda x:x[1])

def main():
    path = "C:\\Users\\kacpe\\Desktop\\Internship 2023 Challenge\\Option2-Python\\p_ex_1_runtime_parsing.json"
    parse_json(path)

if __name__ == "__main__":
    main()