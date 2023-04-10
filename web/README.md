---
title: Alpaca Ptbr 7b
emoji: 🦙
colorFrom: gray
colorTo: gray
sdk: gradio
sdk_version: 3.24.1
app_file: app.py
pinned: true
models: ["dominguesm/alpaca-lora-ptbr-7b"]
datasets: ["dominguesm/alpaca-data-pt-br"]
license: cc-by-4.0
---

<h1 align="center">🦙🇧🇷 Alpaca Instruct PTBR 7B - GRADIO DEMO</h1>

<h3 align="center">
    <p>This Gradio application is running the <a target='_blank' href='https://github.com/ggerganov/ggml'>GGML</a> version (<a target='_blank' href='https://github.com/ggerganov/llama.cpp'>LlaMa.cpp</a>) of the "dominguesm/alpaca-lora-ptbr-7b" model</p>
    <p>For more information about the model and training data visit: [<a target='_blank' href='https://huggingface.co/dominguesm/alpaca-lora-ptbr-7b'>🦙🇧🇷 Alpaca LoRa PTBR 7B</a>]</p>
    <p><b>This version of Space does not accept context data, I will be working on this in the next version.</b></p>
    <p><b>IMPORTANT: Due to the hardware chosen for the HF Space, each response can take between 30 and 60 seconds.</b></p>
</h3>

\n
This model was trained following the "instructions" format, where each instruction has a response, not having a memory about facts that occurred in other responses. Each response is unique to a single statement.\n
Example conversation:\n

```
User: Explique a evolução para uma criança de 6 anos. 
Alpaca-PTBR: A evolução é o processo pelo qual as espécies mudam
             e se adaptam ao ambiente em torno dela, permitindo que
             elas sobrevivam e se multiplicem. Os seres humanos
             foram parte deste processo de seleção natural desde
             o início da história. De acordo com os físicos, a 
             primeira linha de desenvolvimento dos primatas foi 
             na África e, eventualmente, os seres humanos 
             pôs-se na mesma faixa e se ajustou ao seu ambiente em torno dela.

```

### Important notes:
* The model is case-sensitive, so it is important to use the correct case for the words.
* The model is trained to answer in Portuguese, so it is important to use the correct Portuguese words.
* The model is trained to answer in the "instructions" format, so it is important to use the correct format.
* The model have a limit of 150 tokens per response.
* **The model does not make any kind of content filter, use it at your own risk.**