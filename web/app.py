import gradio as gr
import llama_cpp

from utils import download, generate_prompt

MAX_TOKENS = 150

model_path = download()
llm = llama_cpp.Llama(model_path=model_path)


def add_text(history, text):
    history = history + [(text, None)]
    return history, ""


def bot(history):
    prompt = generate_prompt(history[-1][0])
    stream = llm(
        prompt,
        max_tokens=MAX_TOKENS,
        stop=["Abaixo está uma instrução que descreve uma tarefa", "###"],
        stream=True,
    )

    i = 0
    for output in stream:
        if not history[-1][1]:
            history[-1][1] = ""

        text = output["choices"][0]["text"]
        # FIXME: This is a hack to remove the first newline
        if (text == "\n") and (i == 0):
            text = ""
            i += 1

        history[-1][1] += text
        yield history


title = """<h1 align="center">🦙🇧🇷 Alpaca Instruct PTBR 7B</h1>"""
sub_title = """<h3 align="center">
    <p>This Gradio application is running the <a target='_blank' href='https://github.com/ggerganov/ggml'>GGML</a> version (<a target='_blank' href='https://github.com/ggerganov/llama.cpp'>LlaMa.cpp</a>) of the "dominguesm/alpaca-lora-ptbr-7b" model</p>
    <p>For more information about the model and training data visit: [<a target='_blank' href='https://huggingface.co/dominguesm/alpaca-lora-ptbr-7b'>🦙🇧🇷 Alpaca LoRa PTBR 7B</a>]</p>
    <p><b>This version of Space does not accept context data, I will be working on this in the next version.</b></p>
    <p><b>IMPORTANT: Due to the hardware chosen for the HF Space, each response can take between 30 and 60 seconds.</b></p>
</h3>"""
description = """
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
"""

with gr.Blocks(
    css="""#col_container {width: 700px; margin-left: auto; margin-right: auto;}
                #chatbot {height: 500px; overflow: auto;}"""
) as alpaca:
    gr.HTML(title)
    gr.HTML(sub_title)

    with gr.Column(elem_id="col_container"):
        chatbot = gr.Chatbot([], label="Alpaca PTBR 7B", elem_id="chatbot")
        with gr.Row():
            with gr.Column(scale=0.85):
                txt = gr.Textbox(
                    show_label=False,
                    placeholder="Enter text and press enter...",
                ).style(container=False)
            with gr.Column(scale=0.15, min_width=0):
                btn = gr.Button("Clear").style(container=False)

    txt.submit(add_text, [chatbot, txt], [chatbot, txt]).then(bot, chatbot, chatbot)
    btn.click(lambda: None, None, chatbot, queue=False)

    gr.Markdown(description)

alpaca.queue(max_size=20).launch()
