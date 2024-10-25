from flask_restx import Namespace, Resource
from models import VwRegulatorio, VwSop, BaseCliente, BaseId, Previsao, DescMedicamentos  # Importe os modelos necessários
from db import get_db_session

api = Namespace('data', description='Operações com dados do banco de dados')

@api.route('/vw_regulatorio')
class RegulatorioList(Resource):
    def get(self):
        session = get_db_session()
        try:
            result = session.query(VwRegulatorio).all()
            return [{'id': r.id, 'gmid': r.gmid, 'sap_description': r.sap_description, 'family': r.family, 'global_franchise': r.global_franchise, 'n_record_ms_sap':r.n_record_ms_sap} for r in result], 200
        except Exception as e:
            return {"message": str(e)}, 500
        finally:
            session.close()

@api.route('/vw_sop')
class SopList(Resource):
    def get(self):
        session = get_db_session()
        try:
            result = session.query(VwSop).all()
            return [{'id': r.id, 'gmid': r.gmid, 'code_sap_lmid': r.code_sap_lmid, 'family': r.family, 'sap_description': r.sap_description, 'bu_local':r.bu_local} for r in result], 200
        except Exception as e:
            return {"message": str(e)}, 500
        finally:
            session.close()

@api.route('/base_cliente')
class BaseClienteList(Resource):
    def get(self):
        session = get_db_session()
        try:
            result = session.query(BaseCliente).all()
            return [{
                'id': r.id,
                'gmid': r.gmid,
                'sit': r.sit,
                'bu_local': r.bu_local,
                'family': r.family,
                'apresentacao': r.apresentacao,
                'stock_floor_m1_cd': r.stock_floor_m1_cd,
                'stock_floor_m1_pos': r.stock_floor_m1_pos,
                'sellout_m1': r.sellout_m1,
                'sellout_m2': r.sellout_m2,
                'sellout_m3': r.sellout_m3,
                'avg_so_3m': r.avg_so_3m,
                'stock_floor_m1__dcpos': r.stock_floor_m1__dcpos
                } for r in result], 200
        except Exception as e:
            return {"message": str(e)}, 500
        finally:
            session.close()

@api.route('/base_id')
class BaseIdList(Resource):
    def get(self):
        session = get_db_session()
        try:
            result = session.query(BaseId).all()
            return [{
                'bu_local': r.bu_local,
                'familia': r.familia,
                'apresentacao': r.apresentacao,
                'id': r.id,
                'declarado_ci_': r.declarado_ci_,
                'declarado_avg_so_': r.declarado_avg_so_,
                'declarado_so': r.declarado_so,
                'declarado_sit': r.declarado_sit,
                } for r in result], 200
        except Exception as e:
            return {"message": str(e)}, 500
        finally:
            session.close()

@api.route('/previsao')
class PrevisaoList(Resource):
    def get(self):
        session = get_db_session()
        try:
            result = session.query(Previsao).all()
            return [{
                'lmid': r.lmid,
                'apresentacao': r.apresentacao,
                'bu_local': r.bu_local,
                'família': r.família,
                'forecast_mês': r.forecast_mês,
                'livre': r.livre,
                'qualidade': r.qualidade,
                'trânsito': r.trânsito,
                'quantidade_prevista_1': r.quantidade_prevista_1,
                'data_prevista_1': r.data_prevista_1,
                'quantidade_prevista_2': r.quantidade_prevista_2,
                'data_prevista_2': r.data_prevista_2,
                'quantidade_prevista_3': r.quantidade_prevista_3,
                'data_prevista_3': r.data_prevista_3,
                'plant': r.plant,
                } for r in result], 200
        except Exception as e:
            return {"message": str(e)}, 500
        finally:
            session.close()

@api.route('/desc_medicamentos')
class DescMedicamentosList(Resource):
    def get(self):
        session = get_db_session()
        try:
            result = session.query(DescMedicamentos).all()
            return [{
                'assunto': r.assunto,
                'tipo_de_descontinuacao': r.tipo_de_descontinuacao,
                'data_da_peticao': r.data_da_peticao,
                'reativacao_data_de_entrada': r.reativacao_data_de_entrada,
                'motivo': r.motivo,
                'empresa': r.empresa,
                'produto': r.produto,
                'princípio_ativo': r.princípio_ativo,
            } for r in result], 200
        except Exception as e:
            return {"message": str(e)}, 500
        finally:
            session.close()
