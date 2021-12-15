from datetime import datetime
from dateutil.relativedelta import relativedelta

from flask import request, jsonify, Response, make_response

from api.helper.json_encoder import JSONEncoder
from api.app import app, mongo_helper
from api.constants import API_ROUTE
from api.controller.reports import ReportsController

OBJECT = 'report'


@app.route(f'/{API_ROUTE}/{OBJECT}/invoiced_services_current_month/<string:provider_uuid>', methods=['GET'])
def get_invoiced_services_by_provider_uuid_current_month(provider_uuid):
    reports_controller = ReportsController()

    date_today = datetime.today()
    start_date = date_today - relativedelta(months=1)
    start_date = start_date.strftime('%Y-%m-%d')
    end_date = date_today.strftime('%Y-%m-%d')

    return jsonify(reports_controller.get_amount_for_services_in_events(
        provider_uuid, end_date, start_date))


@app.route(f'/{API_ROUTE}/{OBJECT}/invoiced_services_last_month/<string:provider_uuid>', methods=['GET'])
def get_invoiced_services_by_provider_uuid_last_month(provider_uuid):
    reports_controller = ReportsController()

    date_today = datetime.today()
    start_date = date_today - relativedelta(months=2)
    end_date = date_today - relativedelta(months=1)

    start_date = start_date.strftime('%Y-%m-%d')
    end_date = end_date.strftime('%Y-%m-%d')

    return jsonify(reports_controller.get_amount_for_services_in_events(
        provider_uuid, end_date, start_date))


@app.route(f'/{API_ROUTE}/{OBJECT}/services_in_events/<string:provider_uuid>', methods=['GET'])
def get_count_services_in_events_by_provider_uuid(provider_uuid):
    reports_controller = ReportsController()
    return jsonify(reports_controller.get_count_services_in_events(provider_uuid))

@app.route(f'/{API_ROUTE}/{OBJECT}/pending_services_in_events/<string:provider_uuid>', methods=['GET'])
def get_count_pending_services_in_events_by_provider_uuid(provider_uuid):
    reports_controller = ReportsController()
    date_today = datetime.today().strftime('%Y-%m-%d')
    return jsonify(reports_controller.get_count_pending_services_in_events(provider_uuid, date_today))

