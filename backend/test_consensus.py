from services.agent_runner import (
run_all_agents
)

from services.consensus import (
calculate_scores
)

decision = (
"Should we launch EV charging stations in rural India?"
)

agents = run_all_agents(
decision
)

consensus, conflict = (
calculate_scores(
agents
)
)

print(
"Consensus:",
consensus
)

print(
"Conflict:",
conflict
)
