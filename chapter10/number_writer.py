from pathlib import Path
import json
numbers=[1,2,3,4,5,7]
file=Path('numbers.json')
content=json.dumps(numbers)
file.write_text(content)