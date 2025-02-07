import csv
from typing import List, Dict


def loadCSVAsDict(csvPath: str) -> List[Dict[str, str]]:
    """Load CSV file and return as list of dictionaries."""
    with open(csvPath, 'r', encoding='utf-8') as f:
        file_data = csv.reader(f)
        headers = next(file_data)
        return [dict(zip(headers, i)) for i in file_data]