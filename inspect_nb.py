import json
from pathlib import Path
p = Path('notebooks/train_colab.ipynb')
text = p.read_text(encoding='utf-8')
print('LEN', len(text))
try:
    nb = json.loads(text)
    print('VALID JSON', type(nb))
    code_cells = [cell for cell in nb.get('cells', []) if cell.get('cell_type') == 'code']
    print('CODE CELLS', len(code_cells))
    for i, cell in enumerate(code_cells[:10]):
        print('CELL', i)
        print(''.join(cell.get('source', [])).strip()[:400])
        print('-----')
except Exception as exc:
    print('JSON ERROR', exc)
