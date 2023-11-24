from flask import Blueprint
from src.migrate.migrate import initDB

sttcttdb= Blueprint('sttcttdb', __name__)

sttcttdb.route('/sttcttdb', methods=['GET'])(initDB)

