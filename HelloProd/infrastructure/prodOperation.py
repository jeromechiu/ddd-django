from django.core import exceptions

from .models import MyProd
from .ProdSerializer import ProdSerializer


class Prod:
    def __init__(self) -> None:
        pass

    def get_all(
        self,
    ):
        all_prod = MyProd.objects.values()
        prods = [entry for entry in all_prod]
        return prods

    def get_one(self, pid):
        prod = MyProd.objects.filter(pid=pid).values()
        return prod

    def create(self, data):
        serializer = ProdSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return True
        else:
            return False

    def update(self, data):
        try:
            prod = MyProd.objects.get(name=data["name"])
            serializer = ProdSerializer(data=data)
            if not serializer.is_valid():
                raise exceptions.ValidationError("Payload invalid")
            else:
                serializer.update(instance=prod, validated_data=serializer.data)
                return True

        except MyProd.DoesNotExist:
            return False

    def delete(self, pid):
        try:
            MyProd.objects.get(pid=pid).delete()
            return True
        except MyProd.DoesNotExist:
            return False

    def deletable(self, pid):
        try:
            prod = MyProd.objects.get(pid=pid)
            if prod.deletable:
                return True
            else:
                return False
        except MyProd.DoesNotExist:
            return False
