from HelloProd.infrastructure.prodOperation import Prod


class ProdMagament:
    def __init__(self) -> None:
        self.prod = Prod

    def delete_single_prod(self, pid):
        if self.prod().deletable(pid):
            self.prod().delete(pid)
            return True
        else:
            return False

    def add(self, data):
        return self.prod().create(data)

    def update(self, data):
        return self.prod().update(data)
