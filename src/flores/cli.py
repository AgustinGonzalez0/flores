from __future__ import annotations

from .agent import Agent


def main() -> None:
    agent = Agent(name="flores")
    print("Flores agent ready. Type 'exit' to quit.")

    while True:
        user_input = input("You: ")
        if user_input.strip().lower() in {"exit", "quit"}:
            print("Goodbye.")
            break
        print(f"Agent: {agent.run(user_input)}")


if __name__ == "__main__":
    main()
