# Auto-loaded by Python if present on sys.path. Provides compatibility shims for NumPy 2.x
# so the codebase can run on Python 3.12 environments that default to NumPy >= 2.0.

import numpy as np

# Restore removed aliases used by legacy code (avoid touching when present to prevent warnings)
if 'bool' not in np.__dict__:
    np.bool = np.bool_  # type: ignore[attr-defined]
if 'int' not in np.__dict__:
    np.int = int  # type: ignore[attr-defined]
if 'float' not in np.__dict__:
    np.float = float  # type: ignore[attr-defined]
if 'complex' not in np.__dict__:
    np.complex = complex  # type: ignore[attr-defined]
