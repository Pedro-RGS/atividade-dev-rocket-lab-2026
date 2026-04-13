from app.models.avaliacao_pedido import AvaliacaoPedido
from sqlalchemy.orm import Session
from app.utils.base_repository import BaseRepository

class AvaliacaoPedidoRepository(BaseRepository[AvaliacaoPedido]):

  def __init__(self, db: Session):
    super().__init__(db=db, model=AvaliacaoPedido, pk_field="id_avaliacao")
  