from flask import Blueprint
from flask import jsonify

from services.database import (
    decisions_collection
)

history_bp = Blueprint(
"history",
__name__
)

@history_bp.route(
"/api/history",
methods=["GET"]
)
def history():

    records = []

    for item in decisions_collection.find():

        records.append({

            "decision":
            item.get(
                "decision"
            ),

            "consensus_score":
            item.get(
                "consensus_score"
            ),

            "conflict_score":
            item.get(
                "conflict_score"
            )

        })

    return jsonify(
        records
    )
