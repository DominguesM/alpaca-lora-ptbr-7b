
## 🦙🇧🇷 Alpaca-LoRA-PTBR: Low-Rank LLaMA Instruct-Tuning

<a target="_blank" href="https://colab.research.google.com/github/DominguesM/alpaca-lora-ptbr-7b/blob/main/notebooks/03%20-%20Evaluate.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

</br>

<img align="left" style="margin-right: 20px;" height="120" src="https://huggingface.co/dominguesm/alpaca-lora-ptbr-7b/resolve/main/assets/alpaca_br_juliet_2.jpg">

**This model was trained and made available solely and exclusively for research purposes.**

This repository contains the necessary steps to translate the data originally created by the team responsible for the [Stanford Alpaca](https://github.com/tatsu-lab/stanford_alpaca) and also to fine-tune the LLaMA-7b (Meta) model using the [PEFT-LoRA](https://arxiv.org/pdf/2106.09685.pdf) method to adjust only a small number of (extra) parameters. of the model, greatly reducing computational and storage costs.

As the foundation model has not yet been made openly available by **Meta** [(request form)](https://docs.google.com/forms/d/e/1FAIpQLSfqNECQnMkycAp2jP4Z9TFX0cGR4uf7b_fBxjY_OjhJILlKGA/viewform), it is not included in this repository, but you can easily find them by searching on HuggingFace or here on Github. </br> </br>


Note: `alpaca data.json` can be found in the repository: [Stanford Alpaca](https://github.com/tatsu-lab/stanford_alpaca)


## Example outputs

```
Instruções (Instruction): Me fale sobre alpacas

Alpaca-LoRA-PTBR: 'Alpacas são uma espécie de camelo nativa da América do Sul. Eles '
'são conhecidos por serem pacíficos e tranquilos, e muitas vezes são mantidos '
'como animais de estimação domésticos. Alpacas são conhecidas por seus longos '
'e finos cabelos, que podem ser usados para fazer roupas e cobertores. Eles '
'também podem ser usados para produzir leite e carne.

```

```
Instruções (Instruction): Me explique sobre o que é a Lei Maria da Penha do Brasil.

Alpaca-LoRA-PTBR: 'A Lei Maria da Penha do Brasil é uma lei brasileira que proíbe a '
 'discriminação e a violência contra as mulheres. A lei foi nomeada em '
 'homenagem a Maria da Penha, uma mulher que foi assassinada em 1973 por seu '
 'ex-namorado. A lei foi aprovada em 1985 e proíbe a discriminação e a '
 'violência contra as mulheres. A lei proíbe a discriminação e a violência '
 'contra as mulheres, incluindo a discriminação e a violência de gênero, a '
 'discriminação e a violência sexual, a discriminação e a violência econômica, '
 'a discriminação e a violência física e a discriminação e a violência '
 'psicológica.'


In this case the model missed the following points:

* Maria da Penha Fernandes was not murdered, but suffered an attempted murder.
* Maria da Penha Fernandes is alive.
* The attempted homicide took place in 1983.
* The law was sanctioned in 2006.
```

```
Instruções (Instruction): Dada a fórmula química, calcule a massa molar.

Entrada (Input): CaCl2

Alpaca-LoRA-PTBR: 'A massa molar de cloreto de cálcio é 110,98 g/mol.'

```

```
Instruções (Instruction): Faça quatro perguntas sobre a seguinte passagem:

Entrada (Input): A anatomia de uma abelha é bastante intrincada. Tem três partes do corpo: a cabeça, o tórax e o abdômen. A cabeça consiste em órgãos sensoriais, três olhos simples e dois olhos compostos e vários apêndices. O tórax tem três pares de pernas e dois pares de asas, enquanto o abdômen contém a maioria dos órgãos da abelha, incluindo o sistema reprodutivo e o sistema digestivo.

Alpaca-LoRA-PTBR: '1. Quais são os órgãos sensoriais da cabeça da abelha? 2. Quais '
 'são os órgãos sensoriais do tórax da abelha? 3. Quais são os órgãos '
 'sensoriais do abdômen da abelha? 4. Quais são os órgãos do sistema '
 'reprodutivo da abelha?'

```

```
Instruções (Instruction): Analise o documento jurídico fornecido e explique os pontos-chave.

Entrada (Input): O seguinte é um trecho de um contrato entre duas partes, rotulado como "Empresa A" e "Empresa B": "A Empresa A concorda em fornecer assistência razoável à Empresa B para garantir a precisão das demonstrações financeiras que fornece. Isso inclui permitir à Empresa um acesso razoável ao pessoal e outros documentos que possam ser necessários para a revisão da Empresa B. A Empresa B concorda em manter o documento fornecido pela Empresa A em confiança e não divulgará as informações a terceiros sem a permissão explícita da Empresa A".

Alpaca-LoRA-PTBR: 'Este documento é um contrato entre duas partes, rotulado como '
 '"Empresa A" e "Empresa B". A Empresa A concorda em fornecer assistência '
 'razoável à Empresa B para garantir a precisão das demonstrações financeiras '
 'que fornece. Isso inclui permitir à Empresa um acesso razoável ao pessoal e '
 'outros documentos que possam ser necessários para a revisão da Empresa B. A '
 'Empresa B concorda em manter o documento fornecido pela Empresa A em '
 'confiança e não divulgará as informações a terceiros sem a permissão '
 'explícita da Empresa A.''

```

##  Training procedure

Fine-tuning was done via the Trainer API. The necessary script can be found in the `notebooks` folder

### Training hyperparameters

The following hyperparameters were used during training:

| Hyperparameter | Value |
|----------------|-------|
| Batch size     | 128   |
| Learning rate  | 3e-5  |
| Epochs         | 3     |
| Max length     | 512   |
| Lora R         | 8     |
| Lora Alpha     | 16    |
| Lora Dropout   | 0.5   |

### Training results 

The validation results on the valid split are summarised here below.

|Step |	Training Loss |	Validation Loss|
|-----|---------------|----------------|
|200 |	0.891900 |	0.891723|
|400 |	0.854400 |	0.866401|
|600 |	0.850600 |	0.854273|
|800 |	0.831000 |	0.846825|
|1000 |	0.832000 |	0.842221|

## Ethical considerations ([LLaMA Model Card](https://github.com/facebookresearch/llama))

**Data**
The data used to train the model is collected from various sources, mostly from the Web. As such, it contains offensive, harmful and biased content. We thus expect the model to exhibit such biases from the training data.

**Human life**
The model is not intended to inform decisions about matters central to human life, and should not be used in such a way.

**Mitigations**
We filtered the data from the Web based on its proximity to Wikipedia text and references. For this, we used a Kneser-Ney language model and a fastText linear classifier.

**Risks and harms**
Risks and harms of large language models include the generation of harmful, offensive or biased content. These models are often prone to generating incorrect information, sometimes referred to as hallucinations. We do not expect our model to be an exception in this regard.

**Use cases**
LLaMA is a foundational model, and as such, it should not be used for downstream applications without further investigation and mitigations of risks. These risks and potential fraught use cases include, but are not limited to: generation of misinformation and generation of harmful, biased or offensive content.

## References

* Workout descriptions and script based on work done by [Eric J. Wang](https://github.com/tloen/alpaca-lora)
* Training data based on original [Stanford Alpaca](https://crfm.stanford.edu/2023/03/13/alpaca.html) work
