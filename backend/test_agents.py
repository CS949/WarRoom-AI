from services.agent_runner import (
run_all_agents
)

decision = (
"Should we launch EV charging stations in rural India?"
)

agents = run_all_agents(
decision
)

for name, opinion in agents.items():


    print("\n")
    print("=" * 50)
    print(name)
    print("=" * 50)

    print(opinion)

