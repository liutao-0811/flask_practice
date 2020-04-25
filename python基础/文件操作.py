import os
print(os.path.abspath('./'))
print(os.path.exists('../../../136643'))
print(os.path.dirname('/users'))

from pathlib import Path
p=Path('.')
print(p.resolve())
print(p.is_dir())
q=Path('./ab/c')
#Path.mkdir(q,parents=True)
