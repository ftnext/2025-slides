# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "rich",
# ]
# ///
import random

from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel


def main():
    console = Console()
    choices = ["A", "B", "C", "D"]
    console.rule("[bold green]4択クイズランダム回答アプリ")

    console.print("Press Ctrl+C or Ctrl+D to exit.\n")

    try:
        while True:
            _ = Prompt.ask("[cyan]Enterで鉛筆を転がす[/cyan]", default="")
            choice = random.choice(choices)
            panel = Panel(
                f"[bold yellow]{choice}[/bold yellow]",
                title="鉛筆で出たのは",
                border_style="magenta",
            )
            console.print(panel)

    except (KeyboardInterrupt, EOFError):
        console.print("\n[bold red]Exiting.[/bold red]")


if __name__ == "__main__":
    main()
