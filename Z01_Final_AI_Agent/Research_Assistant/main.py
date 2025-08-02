from dotenv import load_dotenv
from src.workflow import Workflow

load_dotenv()


def main():
    workflow = Workflow()
    print("Research Agent")

    while True:
        topic = input("\n🔍 What do you want to research?: ").strip()

        # Check if the user wants to quit the agent or make another query
        if topic.lower() in {"quit", "exit"}:
            break

        # If there is a query run the agent
        if topic:
            result = workflow.run(topic)
            print(f"\n📊 Research report for: {topic}")
            print("=" * 60)

            # Print final report
            if result.report:
                print("Research Report: ")
                print("-" * 40)
                print(result.report)

if __name__ == "__main__":
    main()