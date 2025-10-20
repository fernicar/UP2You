# Auto-loaded by Python if present on sys.path. Provides compatibility shims for NumPy 2.x
# so the codebase can run on Python 3.12 environments that default to NumPy >= 2.0.

import numpy as np

# Restore removed aliases used by legacy code
if not hasattr(np, 'bool'):
    np.bool = np.bool_  # type: ignore[attr-defined]
if not hasattr(np, 'int'):
    np.int = int  # type: ignore[attr-defined]
if not hasattr(np, 'float'):
    np.float = float  # type: ignore[attr-defined]
if not hasattr(np, 'complex'):
    np.complex = complex  # type: ignore[attr-defined]
