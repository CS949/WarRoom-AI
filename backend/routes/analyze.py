from flask import Blueprint
from flask import request
from flask import jsonify

import json

from services.agent_runner import (
    run_all_agents
)

from services.moderator import (
    generate_moderator_report
)

from services.consensus import (
    calculate_scores
)

from services.database import (
    decisions_collection
)

from services.foundry_iq import (
    get_foundry_context
)

analyze_bp = Blueprint(
    "analyze",
    __name__
)

@analyze_bp.route(
    "/api/analyze",
    methods=["POST"]
)

def analyze():

    try:

        data = request.get_json()

        if data is None:

            return jsonify({

                "success": False,

                "error":
                "No JSON data received."

            }),400

        if isinstance(
            data,
            str
        ):

            data = json.loads(
                data
            )

        decision = data.get(
            "decision",
            ""
        )

        if not decision:

            return jsonify({

                "success": False,

                "error":
                "Decision is required."

            }),400

        foundry_context = (
            get_foundry_context(
                decision
            )
        )

        agents = run_all_agents(

            decision,

            foundry_context

        )

        moderator_report = (

            generate_moderator_report(

                decision,

                agents

            )

        )

        consensus_score, conflict_score = (

            calculate_scores(

                agents

            )

        )

        decisions_collection.insert_one({

            "decision":
            decision,

            "foundry_context":
            foundry_context,

            "agents":
            agents,

            "moderator":
            moderator_report,

            "consensus_score":
            consensus_score,

            "conflict_score":
            conflict_score

        })

        return jsonify({

            "success": True,

            "decision":
            decision,

            "foundry_context":
            foundry_context,

            "agents":
            agents,

            "moderator":
            moderator_report,

            "consensus_score":
            consensus_score,

            "conflict_score":
            conflict_score

        })

    except Exception as e:

        return jsonify({

            "success": False,

            "error":
            str(e)

        }),500

