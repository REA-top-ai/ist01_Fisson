# Logs parser
import json


def record_to_dict(log: str) -> dict:
    parts = log.split("|")
    log_dict = {"date": parts[0], "level": parts[1]}
    message = parts[2].split(" ")
    for msg in message:
        keyval = msg.split("=")
        log_dict[keyval[0]] = int(keyval[1]) if keyval[1].isnumeric() else keyval[1]
    return log_dict


def logs_to_list(logs: list, json_file: str = None) -> list[dict]:
    logs_list = [record_to_dict(rec) for rec in logs]

    if json_file:
        with open(json_file, "w") as file:
            json.dump(logs_list, file, indent=4)
    return logs_list

def filter_logs(logs: list, **filters) -> list[dict]:
    logs_list = logs_to_list(logs)
    logs_filtered = []
    for log in logs_list:
        for key, value in filters.items():
            if key not in log or log[key] != value:
                break
        else:
            logs_filtered.append(log)
    return logs_filtered

def aggregate_logs(logs: list, aggregate_field: str, sum_key: str = "amount",  **filters) -> tuple:
    logs_list = filter_logs(logs, **filters)
    aggregates = {}
    for log in logs_list:
        if aggregate_field not in log:
            continue
        field = log[aggregate_field]
        if field not in aggregates:
            aggregates[field] = {"count": 1, sum_key: log.get(sum_key, 0)}
        else:
            aggregates[field]["count"] += 1
            aggregates[field][sum_key] += log.get(sum_key, 0)

    count = 0
    summ = 0
    for value in aggregates.values():
        count += value["count"]
        summ += value[sum_key]

    return count, summ, aggregates

def aggregate_by_level(logs: list, **filters) -> tuple:
    return aggregate_logs(logs, "level", **filters)

def aggregate_by_user(logs: list, **filters) -> tuple:
    return aggregate_logs(logs, "user", **filters)

def amount_for_failed(logs: list, **filters) -> tuple:
    _, summ, _ = aggregate_logs(logs, "amount", action="payment", status="fail")
    return summ

def print_records(records: list) -> None:
    for record in records:
        print(record)


all_logs = [
    "2025-02-01 10:15:33|INFO|user=anna action=login status=success ip=10.0.0.1",
    "2025-02-01 10:17:10|ERROR|user=bob action=payment status=fail amount=120",
    "2025-02-01 10:20:01|INFO|user=anna action=logout status=success",
    "2025-02-01 10:22:45|WARNING|user=anna action=payment status=fail amount=300",
    "2025-02-01 10:30:12|ERROR|user=tom action=login status=fail ip=10.0.0.5"
]

print("---- FAIL ONLY ----")
print_records(filter_logs(all_logs, status="fail"))
print("")

print("---- ONLY ERRORS ----")
print_records(filter_logs(all_logs, level="ERROR"))
print("")

print("---- ONLY anna ----")
print_records(filter_logs(all_logs, user="anna"))
print("")

print("---- COUNT BY LEVEL ----")
count, amount, aggregate = aggregate_by_level(all_logs)
print(f"all records: {count}, amount: {amount}")
for key, val in aggregate.items():
    print(f"{key}: {val}")
