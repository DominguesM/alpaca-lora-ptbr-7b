import os
import sys
import urllib.request
from typing import Optional

from tqdm.auto import tqdm


class DownloadProgressBar(tqdm):
    def update_to(
        self, b: int = 1, bsize: int = 1, tsize: Optional[int] = None
    ) -> None:
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)


def download() -> str:
    # Get the model URI from the environment
    uri_model = os.environ.get("ALPACA_MODEL_URI")

    # Set the path for the model
    model_path = "./model.bin"

    # If the model path already exists, return it
    if os.path.exists(model_path):
        return model_path

    # Create a progress bar
    with DownloadProgressBar(
        unit="B", unit_scale=True, miniters=1, desc=uri_model.split("/")[-1]
    ) as t:
        # Download the model to the model path
        urllib.request.urlretrieve(
            uri_model, filename=model_path, reporthook=t.update_to
        )

    # Return the model path
    return model_path


def generate_prompt(instruction: str, input: Optional[str] = None) -> str:
    if input:
        return f"""Abaixo está uma instrução que descreve uma tarefa, emparelhada com uma entrada que fornece mais contexto. Escreva uma resposta que conclua adequadamente a solicitação.

### Instruções:
{instruction}

### Entrada:
{input}

### Resposta:"""
    else:
        return f"""Abaixo está uma instrução que descreve uma tarefa. Escreva uma resposta que conclua adequadamente a solicitação.

### Instruções:
{instruction}

### Resposta:"""
