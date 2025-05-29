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
    console.rule("[bold green]Random Choice Generator")
    console.print(
        "Each iteration, enter a seed (integer) to reseed, or press Enter to keep the previous state."
    )
    console.print("Press Ctrl+C or Ctrl+D to exit.\n")

    try:
        while True:
            seed_input = Prompt.ask("[cyan]Seed[/cyan]", default="")
            if seed_input:
                try:
                    seed = int(seed_input)
                except ValueError:
                    console.print(
                        "[red]Invalid seed.[/red] Please enter a valid integer.\n"
                    )
                    continue
                random.seed(seed)

            choice = random.choice(choices)
            panel = Panel(
                f"[bold yellow]{choice}[/bold yellow]",
                title="Your Choice",
                border_style="magenta",
            )
            console.print(panel)

    except (KeyboardInterrupt, EOFError):
        console.print("\n[bold red]Exiting.[/bold red]")


if __name__ == "__main__":
    main()
