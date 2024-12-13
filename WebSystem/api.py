from flask import Blueprint, request, jsonify
from IndoorManageSystem.record import record as indoor_record
from IndoorManageSystem.response import response as indoor_response

api_bp = Blueprint("api", __name__)

@api_bp.route("/test")
def test():
    return True

@api_bp.route("/indoorAPI/record", methods=["POST"])
def indoorAPI_record():
    status, error = indoor_record(request.get_json())
    
    if error == None: return jsonify({'status': status, "Message": "Record success"})
    return jsonify({'status': status, "Message": str(error)})
    
@api_bp.route("/indoorAPI/realtime_data")
def indoorAPI_realtime_data():
    return indoor_response()