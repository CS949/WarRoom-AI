from services.moderator import (
generate_moderator_report
)

decision = (
"Should we launch EV charging stations in rural India?"
)

agents = {


"CEO Agent":
"Huge market opportunity.",

"CFO Agent":
"High capital expenditure and uncertain ROI.",

"CTO Agent":
"Grid infrastructure may not be reliable.",

"Marketing Agent":
"Strong brand positioning opportunity.",

"Legal Agent":
"Government approvals required.",

"Risk Agent":
"Demand may remain low for years."


}

report = generate_moderator_report(
decision,
agents
)

print(report)
