from services.agents import run_agent

AGENT_ROLES = {

    "CEO Agent":
    """
Focus on growth, market expansion,
competitive advantage and vision.
""",

    "CFO Agent":
    """
Focus on costs, ROI,
profitability and cash flow.
Be conservative.
""",

    "CTO Agent":
    """
Focus on technology,
infrastructure, scalability,
engineering complexity.
""",

    "Marketing Agent":
    """
Focus on customer demand,
brand positioning,
market adoption.
""",

    "Legal Agent":
    """
Focus on regulations,
compliance,
liability and legal risks.
""",

    "Risk Agent":
    """
Focus on worst-case scenarios,
operational risks,
economic risks and failure modes.
Be skeptical.
""",

    "Sustainability Agent":
    """
Focus on sustainability,
environmental impact,
social responsibility
and long-term benefits.
""",

    "Ethics Agent":
    """
Focus on ethics,
fairness,
transparency,
human impact
and responsible AI.
"""

}

def run_all_agents(
    decision,
    context=""
):

    results = {}

    for name, role in AGENT_ROLES.items():

        results[name] = run_agent(

            role,

            decision,

            context

        )

    return results

