# Implementação manual do k-means no plano a*b* do espaço L*a*b*.

import operator

import numpy as np
import cv2


def kmeans_ab(img_rgb, k, max_iter=100, tol=1e-4, seed=42):
    """
    K-means manual no plano a*b* do espaco L*a*b*.

    Parâmetros
    ----------
    img_rgb : ndarray (H, W, 3) uint8
        Imagem em RGB.
    k : int
        Número de clusters.
    max_iter : int
        Iterações máximas.
    tol : float
        Tolerância de convergência (deslocamento máximo dos centroides).
    seed : int
        Semente para reprodutibilidade.

    Retorna
    -------
    labels : ndarray (H, W) int
        Rótulo 0..k-1 por pixel.
    centroids : ndarray (k, 2)
        Centroides finais no plano a*b*.
    history : list of (iter_number, labels_i, centroids_i)
        Snapshots em 3 momentos: início, meio e convergência.
    """
    H, W = img_rgb.shape[:2]

    lab = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2LAB).astype(np.float64)
    ab = lab[:, :, 1:3].reshape(-1, 2)
    N = ab.shape[0]

    try:
        k = operator.index(k)
    except TypeError:
        raise ValueError(
            f"k must be an integer between 1 and N (N={N}), got k={k!r}"
        ) from None
    if not (1 <= k <= N):
        raise ValueError(
            f"k must be an integer between 1 and N (N={N}), got k={k!r}"
        )

    rng = np.random.RandomState(seed)
    indices = rng.choice(N, size=k, replace=False)
    centroids = ab[indices].copy()

    all_snapshots = []
    labels_flat = np.zeros(N, dtype=np.int32)

    for it in range(max_iter):
        dists = np.linalg.norm(ab[:, None, :] - centroids[None, :, :], axis=2)
        labels_flat = np.argmin(dists, axis=1)

        all_snapshots.append(
            (it, labels_flat.reshape(H, W).copy(), centroids.copy())
        )

        new_centroids = np.empty_like(centroids)
        for j in range(k):
            members = ab[labels_flat == j]
            if len(members) == 0:
                new_centroids[j] = centroids[j]
            else:
                new_centroids[j] = members.mean(axis=0)

        shift = np.linalg.norm(new_centroids - centroids, axis=1).max()
        centroids = new_centroids

        if shift < tol:
            # Rótulos devem corresponder aos centróides já atualizados
            dists = np.linalg.norm(ab[:, None, :] - centroids[None, :, :], axis=2)
            labels_flat = np.argmin(dists, axis=1)
            all_snapshots.append(
                (it + 1, labels_flat.reshape(H, W).copy(), centroids.copy())
            )
            break

    # Última atualização de centróides sem nova atribuição (ex.: parada por max_iter)
    dists = np.linalg.norm(ab[:, None, :] - centroids[None, :, :], axis=2)
    labels_flat = np.argmin(dists, axis=1)

    total = len(all_snapshots)
    pick = [0, total // 2, total - 1]
    pick = sorted(set(pick))
    history = [all_snapshots[i] for i in pick]

    labels = labels_flat.reshape(H, W)
    return labels, centroids, history
