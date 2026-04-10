# segmentation-cvis

implementation of classical computer vision segmentation algorithms

## estrutura inicial do projeto

```
segmentation-cvis/
├── notebook/
│   └── atividade_segmentacao.ipynb   # notebook principal da atividade
├── src/
│   ├── otsu.py                       # implementação do método de Otsu
│   ├── kmeans.py                     # implementação do k-means em L*a*b*
│   └── morphology.py                 # operações morfológicas de refino
├── images/
│   ├── input/                        # imagens de entrada (ex.: tomate.png)
│   └── results/                      # resultados de segmentação e figuras
├── requirements.txt
└── README.md
```

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

- [ ] Escolher a melhor máscara das etapas anteriores
- [ ] Aplicar abertura (erosão + dilatação) para remover ruídos isolados
- [ ] Aplicar fechamento (dilatação + erosão) para preencher buracos/lacunas
- [ ] Avaliar o impacto do tamanho do elemento estruturante
- [ ] Comparar preservação de detalhes vs remoção de ruído

### Entrega e apresentação:

- [ ] Montar painel comparativo: `Original | Otsu | HSV | K-Means | Pós-processado`
- [ ] Incluir visuais de apoio: histogramas, canais de cor, gráfico no plano `a*b*`
- [ ] Preparar respostas objetivas para todas as reflexões do roteiro:
  - Parte I: quando Otsu falha? como a janela local da adaptativa afeta ruído/detalhes?
  - Parte II: qual espaço de cor foi mais robusto a sombras/reflexos e por quê?
  - Parte III: quando usar apenas cromaticidade ajuda e quando perde informação?
  - Parte IV: trade-off do elemento estruturante (suavização vs preservação de contorno)
- [ ] Fechar com conclusão comparativa: robustez, custo computacional e cenários ideais

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
