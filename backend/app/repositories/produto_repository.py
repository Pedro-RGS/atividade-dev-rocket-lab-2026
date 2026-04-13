from sqlalchemy.orm import Session, joinedload
from app.utils.base_repository import BaseRepository
from app.models.produto import Produto

class ProdutoRepository(BaseRepository[Produto]):
  def __init__(self, db: Session):
    super().__init__(db=db, model=Produto, pk_field="id_produto")
  
  def find_by_id(self, id_produto: str):
    return self.db.query(self.model)\
        .options(joinedload(self.model.itens_pedido))\
        .filter(self.model.id_produto == id_produto)\
        .first()

  def find_all(self, limit = 100, offset = 0):
    return self.db.query(self.model)\
          .options(joinedload(self.model.itens_pedido))\
          .limit(limit)\
          .offset(offset)\
          .all()

  def find_by_categoria(self, categoria: str):
    return self.filter_by(categoria_produto=categoria)
  
  def find_by_nome(self, nome: str):
    return self.filter_by(nome_produto=nome)
  
  def find_by_categoria(self, categoria: str):
    return self.filter_by(categoria_produto=categoria)