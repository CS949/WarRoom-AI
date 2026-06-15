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

    data = decisions_collection.find()

    for item in data:

        records.append({

            "decision":

            item.get(

                "decision",

                "No Decision"

            ),

            "consensus_score":

            item.get(

                "consensus_score",

                0

            ),

            "conflict_score":

            item.get(

                "conflict_score",

                0

            )

        })

    records.reverse()

    return jsonify(

        records

    )