# segmentation-cvis

implementation of classical computer vision segmentation algorithms

## estrutura inicial do projeto

```
segmentation-cvis/
├── notebook/
│   └── atividade_segmentacao.ipynb   # notebook principal (limiarização, cores, k-means, morfologia, painel comparativo)
├── src/
│   ├── otsu.py                       # método de Otsu (histograma + somas cumulativas)
│   └── kmeans.py                     # k-means manual no plano a*b* (L*a*b*)
├── images/
│   ├── input/                        # imagens de entrada (ex.: tomates-corke.png, coins.png)
│   └── results/                      # máscaras e figuras exportadas (k-means, painel comparativo, etc.)
├── pyproject.toml                    # dependências e metadados do projeto (uv)
├── uv.lock                           # lockfile das dependências
├── .python-version                   # versão de Python usada no projeto
└── README.md
```

Operações morfológicas (Parte IV) são feitas no notebook com **OpenCV** (`cv2.morphologyEx`), sobre a máscara gerada pelo k-means.

## inicializando:

O setup agora é realizado com uv sync:

1. install uv (se não tiver instalado):

```
curl -LsSf https://astral.sh/uv/install.sh | sh
uv --version
```

2. install dependencies:

```
uv sync
uv venv
```

inicializado a venv, só executar o notebook :)

## to-do – roteiro da atividade (por partes)

### Parte I - Limiarização (Thresholding)

- [x] Converter imagem para tons de cinza e aplicar limiar manual `T`
- [x] Plotar histograma e indicar `T` com linha vertical
- [x] Implementar Otsu manualmente (histograma + somas cumulativas)
- [x] Comparar Otsu manual com função pronta (OpenCV/scikit-image)
- [x] Aplicar limiarização adaptativa (OpenCV) e comparar com limiares globais
- [x] Registrar casos de sucesso e falha em diferentes imagens

### Parte II - Espaços de cor e cromaticidade

- [x] Exibir canais `R`, `G` e `B` separadamente e discutir limitações do RGB
- [x] Converter para `HSV` e segmentar usando canal `H`
- [x] Converter para `L*a*b*` e segmentar usando canais `a*` e `b*`
- [x] Comparar resultados de RGB vs HSV vs L*a*b\*
- [x] Destacar impacto de sombras, reflexos e variações de iluminação

### Parte III - Agrupamento K-Means

- [x] Implementar k-means manual no plano `a*b*` (sem loop pronto de biblioteca)
- [x] Testar diferentes valores de `k` e comparar segmentações
- [x] Mostrar evolução dos centróides em pelo menos 3 momentos (início, meio, fim)
- [x] Plotar dispersão no plano `a*b*` com pixels coloridos por cluster
- [x] Interpretar se os clusters representam classes visuais úteis (tomate, folha, fundo)

### Parte IV - Morfologia e refino

- [x] Escolher a melhor máscara das etapas anteriores
- [x] Aplicar abertura (erosão + dilatação) para remover ruídos isolados
- [x] Aplicar fechamento (dilatação + erosão) para preencher buracos/lacunas
- [x] Avaliar o impacto do tamanho do elemento estruturante
- [x] Comparar preservação de detalhes vs remoção de ruído

### Entrega e apresentação:

- [x] Planejamento da apresentação
- [x] Montar painel comparativo: `Original | Otsu | HSV | K-Means | Pós-processado`
- [x] Incluir visuais de apoio: histogramas, canais de cor, gráfico no plano `a* b*`

## Como colaborar?

1. atualize sua branch `main` local:
   - `git checkout main`
   - `git pull origin main`

2. crie uma nova branch para sua tarefa:
   - Para nova funcionalidade: `git checkout -b feature/nome-da-funcionalidade`
   - Para correção de bug: `git checkout -b fix/descricao-do-bug`

3. faça as alterações no código e teste localmente (notebooks, scripts em `src/`, etc.).

4. adicione e faça commit das mudanças:
   - `git add .`
   - `git commit -m "Descrição curta e clara da mudança"`

5. envie a branch para o repositório remoto:
   - `git push origin feature/nome-da-funcionalidade`

6. abra um Pull Request (PR) para a branch `main`, descrevendo:
   - **O que** foi alterado
   - **Por que** foi alterado
   - Como **reproduzir/testar** os resultados

7. aguarde revisão, faça ajustes se necessário e, após aprovação, faça o merge.
