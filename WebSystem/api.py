from flask import Blueprint, request, jsonify
from IndoorManageSystem.record import record
from IndoorManageSystem.response import response

api_bp = Blueprint("api", __name__)

@api_bp.route("/test")
def test():
    return True

@api_bp.route("/indoorAPI/record", methods=["POST"])
def indoor_record():
    status, error = record(request.get_json())
    
    if error == None: return jsonify({'status': status, "Message": "Record success"})
    return jsonify({'status': status, "Message": str(error)})
    
@api_bp.route("/indoorAPI/response")
def indoor_response():
    return response()