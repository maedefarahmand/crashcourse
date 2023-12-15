from pathlib import Path
import json
path=Path('numbers.json')
content=path.read_text()
a=json.loads(content)
print(a)