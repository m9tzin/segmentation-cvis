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

## TODO – algoritmos a implementar

- [ ] Limiarização manual com histograma em tons de cinza
- [ ] Implementação manual do método de Otsu
- [ ] Comparação com Otsu usando função pronta (OpenCV / scikit-image)
- [ ] Limiarização adaptativa (OpenCV)
- [ ] Visualização dos canais R, G, B e análise das limitações do espaço RGB
- [ ] Conversão para HSV e limiarização no canal H
- [ ] Conversão para L\*a\*b\* e limiarização usando canais a\* e b\*
- [ ] Implementação manual do k-means no plano a\*b\*
- [ ] Análise de k-means variando o número de clusters (k)
- [ ] Visualização da evolução dos centróides no plano a\*b\*
- [ ] Pós-processamento morfológico: abertura (erosão + dilatação)
- [ ] Pós-processamento morfológico: fechamento (dilatação + erosão)
- [ ] Análise comparativa final: Original × Otsu × HSV × K-means × Pós-processado


## Como colaborar?

1. faça um fork (se estiver usando GitHub) ou clone o repositório:
   - `git clone <url-do-repositorio>`
   - `cd segmentation-cvis`

2. atualize sua branch `main` local:
   - `git checkout main`
   - `git pull origin main`

3. crie uma nova branch para sua tarefa:
   - Para nova funcionalidade: `git checkout -b feature/nome-da-funcionalidade`
   - Para correção de bug: `git checkout -b fix/descricao-do-bug`

4. faça as alterações no código e teste localmente (notebooks, scripts em `src/`, etc.).

5. adicione e faça commit das mudanças:
   - `git add .`
   - `git commit -m "Descrição curta e clara da mudança"`

6. envie a branch para o repositório remoto:
   - `git push origin feature/nome-da-funcionalidade`

7. abra um Pull Request (PR) para a branch `main`, descrevendo:
   - **O que** foi alterado
   - **Por que** foi alterado
   - Como **reproduzir/testar** os resultados

8. aguarde revisão, faça ajustes se necessário e, após aprovação, faça o merge.