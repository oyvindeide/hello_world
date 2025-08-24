import sys
from typing import Dict, Any

import ert
from ert import ForwardModelStepDocumentation, ForwardModelStepPlugin
from everest.plugins import hookimpl


class HelloWorld(ForwardModelStepPlugin):
    def __init__(self) -> None:
        super().__init__(
            name="hello_world",
            command=[
                "hello_world",
            ],
        )

    @staticmethod
    def documentation() -> ForwardModelStepDocumentation | None:
        return ForwardModelStepDocumentation(
            description="My very own custom print job",
            examples="""
Argument examples
~~~~~~~~~~~~~~~~~

This will print something to the terminal, always prepended with:
Hello world:

.. code-block:: bash

  hello_world Oyvind

Output:

.. code-block:: console

  Hello world: Oyvind
""",
        )

@ert.plugin(name="hello_world")
def installable_forward_model_steps():
    return [
        HelloWorld
    ]


@hookimpl
def get_forward_model_documentations() -> Dict[str, Any]:
    job = HelloWorld()
    return {"Hello world": {
        "cmd_name": job.name,
        "examples": job.documentation().examples,
        "full_job_name": "Hello world",
    }}


def main():
    name = sys.argv[1]
    print("Hello world:", name)
