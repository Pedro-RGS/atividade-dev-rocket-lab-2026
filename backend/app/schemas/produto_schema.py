from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, List

class ProdutoCreateResponse(BaseModel):
    id_produto: str
    nome_produto: str
    categoria_produto: Optional[str] = None
    peso_produto_gramas: Optional[float] = Field(None, ge=0)
    comprimento_centimetros: Optional[float] = Field(None, ge=0)
    altura_centimetros: Optional[float] = Field(None, ge=0)
    largura_centimetros: Optional[float] = Field(None, ge=0)

class ProdutoCreateRequest(BaseModel):
    nome_produto: str
    categoria_produto: Optional[str] = None
    peso_produto_gramas: Optional[float] = Field(None, ge=0)
    comprimento_centimetros: Optional[float] = Field(None, ge=0)
    altura_centimetros: Optional[float] = Field(None, ge=0)
    largura_centimetros: Optional[float] = Field(None, ge=0)

class ProdutoListResponse(BaseModel):
    id_produto: str
    nome_produto: str
    categoria_produto: Optional[str]
    preco: float
    url_imagem: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)

class ProdutoUpdate(BaseModel):
    nome_produto: Optional[str] = None
    categoria_produto: Optional[str] = None
    peso_produto_gramas: Optional[float] = Field(None, ge=0)
    comprimento_centimetros: Optional[float] = Field(None, ge=0)
    altura_centimetros: Optional[float] = Field(None, ge=0)
    largura_centimetros: Optional[float] = Field(None, ge=0)

class _MedidasSchema(BaseModel):
    peso_produto_gramas: Optional[float]
    comprimento_centimetros: Optional[float]
    altura_centimetros: Optional[float]
    largura_centimetros: Optional[float]

class _StatisticsSchema(BaseModel):
    total_vendas: int
    total_avaliacoes: int
    media_nota: float

class ProdutoDetalheResponse(ProdutoListResponse):
    medidas: _MedidasSchema
    estatisticas: _StatisticsSchema


