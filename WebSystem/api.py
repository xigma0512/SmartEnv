from flask import Blueprint, request, jsonify
from IndoorManageSystem.record import record as indoor_record
from IndoorManageSystem.response import response as indoor_response
from OutdoorManageSystem.record import record as outdoor_record
from OutdoorManageSystem.response import response as outdoor_response

api_bp = Blueprint("api", __name__)

@api_bp.route("/test")
def test():
    return True

@api_bp.route("/indoorAPI/record", methods=["POST"])
def indoorAPI_record():
    status, error = indoor_record(request.get_json())
    
    if error == None: return jsonify({'status': status, "Message": "Record success"})
    return jsonify({'status': status, "Message": str(error)}),500
    
@api_bp.route("/indoorAPI/data")
def indoorAPI_data():
    return indoor_response()


@api_bp.route("/outdoorAPI/record", methods=["POST"])
def outdoorAPI_record():
    status, error = outdoor_record(request.get_json())
    
    if error == None: return jsonify({'status': status, "Message": "Record success"})
    return jsonify({'status': status, "Message": str(error)}),500 ## 要給錯誤代碼 sensor看代碼確認有沒有OK
    
@api_bp.route("/outdoorAPI/data")
def outdoorAPI_data():
    return outdoor_response()
