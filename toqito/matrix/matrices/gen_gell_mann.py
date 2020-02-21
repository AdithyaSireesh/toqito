"""Produces a generalized Gell-Mann operator."""
from typing import Union
import numpy as np
from scipy import sparse


def gen_gell_mann(ind_1: int,
                  ind_2: int,
                  dim: int,
                  is_sparse: bool = False
                  ) -> Union[np.ndarray, sparse.lil_matrix]:
    """
    Produce a generalized Gell-Mann operator.

    Construct a `dim`-by-`dim` Hermitian operator. These matrices span the
    entire space of `dim`-by-`dim` matrices as `ind_1` and `ind_2` range from 0
    to `dim-1`, inclusive, and they generalize the Pauli operators when `dim =
    2` and the Gell-Mann operators when `dim = 3`.

    :param ind_1: A non-negative integer from 0 to `dim-1` (inclusive).
    :param ind_2: A non-negative integer from 0 to `dim-1` (inclusive).
    :param dim: The dimension of the Gell-Mann operator.
    :param is_sparse: If set to `True`, the returned Gell-Mann operator is a
                      sparse lil_matrix and if set to `False`, the returned
                      Gell-Mann operator is a dense numpy array.
    :return: The Gell-Mann operator.
    """
    if ind_1 == ind_2:
        if ind_1 == 0:
            gm_op = sparse.eye(dim)
        else:
            scalar = np.sqrt(2/(ind_1*(ind_1+1)))
            diag = np.ones((ind_1, 1))
            diag = np.append(diag, -ind_1)
            diag = scalar * np.append(diag, np.zeros((dim-ind_1-1, 1)))

            gm_op = sparse.lil_matrix((dim, dim))
            gm_op.setdiag(diag)
            
    else:
        e_mat = sparse.lil_matrix((dim, dim))
        e_mat[ind_1, ind_2] = 1
        if ind_1 < ind_2:
            gm_op = e_mat + e_mat.conj().T
        else:
            gm_op = 1j*e_mat - 1j*e_mat.conj().T

    if not is_sparse:
        return gm_op.todense()
    return gm_op

