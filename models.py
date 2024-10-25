from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class VwRegulatorio(Base):
    __tablename__ = 'vw_regulatorio'
    id = Column(String, primary_key=True)
    gmid = Column(String)
    sap_description = Column(String)
    family = Column(String)
    global_franchise = Column(String)
    n_record_ms_sap = Column(String)

class BaseCliente(Base):
    id = Column(String, primary_key=True) 
    gmid = Column(String) 
    sit = Column(String) 
    bu_local = Column(String) 
    family = Column(String) 
    apresentacao = Column(String) 
    stock_floor_m1_cd = Column(String) 
    stock_floor_m1_pos = Column(String) 
    sellout_m1 = Column(String) 
    sellout_m2 = Column(String) 
    sellout_m3 = Column(String) 
    avg_so_3m = Column(String) 
    stock_floor_m1__dcpos = Column(String)    
    __tablename__ = 'base_cliente'

class BaseId(Base):
    bu_local = Column(String)
    familia = Column(String)
    apresentacao = Column(String)
    id = Column(String, primary_key=True)
    declarado_ci_ = Column(String)
    declarado_avg_so_ = Column(String)
    declarado_so = Column(String)
    declarado_sit = Column(String)
    __tablename__ = 'base_id'
    
class Previsao(Base):
    id = Column(String, primary_key=True)
    lmid = Column(String)
    apresentacao = Column(String)
    bu_local = Column(String)
    família = Column(String)
    forecast_mês = Column(String)
    livre = Column(String)
    qualidade = Column(String)
    trânsito = Column(String)
    quantidade_prevista_1 = Column(String)
    data_prevista_1 = Column(String)
    quantidade_prevista_2 = Column(String)
    data_prevista_2 = Column(String)
    quantidade_prevista_3 = Column(String)
    data_prevista_3 = Column(String)
    plant = Column(String)
    __tablename__ = 'previsao'

class DescMedicamentos(Base):
    id = Column(String, primary_key=True)
    assunto = Column(String)
    tipo_de_descontinuacao = Column(String)
    data_da_peticao = Column(String)
    reativacao_data_de_entrada = Column(String)
    motivo = Column(String)
    empresa = Column(String)
    produto = Column(String)
    princípio_ativo = Column(String)    
    __tablename__ = 'desc_medicamentos'

class VwSop(Base):
    __tablename__ = 'vw_sop'
    id = Column(String, primary_key=True)
    code_sap_lmid = Column(String)
    gmid = Column(String)
    sap_description = Column(String)
    family = Column(String)
    bu_local = Column(String)

# Continue mapeando as outras tabelas da mesma forma
