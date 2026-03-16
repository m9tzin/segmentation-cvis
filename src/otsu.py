import numpy as np

def otsu_threshold(img_gray):
    hist, _ = np.histogram(img_gray.flatten(), bins=256, range=(0, 256))

    # Normaliza o histograma para obter probabilidades por intensidade
    prob = hist / img_gray.size

    intensidades = np.arange(256)

    melhor_t = 0
    menor_variancia = float('inf')

    for t in range(256):
        w0 = prob[:t].sum()  # peso da classe 0 (fundo)
        w1 = prob[t:].sum()  # peso da classe 1 (objeto)

        if w0 == 0 or w1 == 0:
            continue

        mean0 = (prob[:t] * intensidades[:t]).sum() / w0
        mean1 = (prob[t:] * intensidades[t:]).sum() / w1

        var0 = (prob[:t] * (intensidades[:t] - mean0)**2).sum() / w0
        var1 = (prob[t:] * (intensidades[t:] - mean1)**2).sum() / w1

        variancia_intra = w0 * var0 + w1 * var1

        # Atualiza o melhor limiar se encontrou variância menor
        if variancia_intra < menor_variancia:
            menor_variancia = variancia_intra
            melhor_t = t

    return melhor_t