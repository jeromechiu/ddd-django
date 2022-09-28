from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from HelloProd.domain.views import ProdMagament
from HelloProd.infrastructure.prodOperation import Prod


class ProdApiView(APIView):

    """
    Get data from Infrastructure layer
     becasue of just retrieving data
     from DB without any domain know-how
    """

    def get(self, request):
        data = dict()
        pid = request.GET.get("pid", None)
        if pid is None:
            data["data"] = Prod().get_all()
        else:
            data["data"] = Prod().get_one(pid)

        return Response(data=data, status=status.HTTP_200_OK)

    """
    Here, we set a condition. If product cannot be deleted,
     the request will be reject by returing 403 forbidden
    """

    def delete(self, request):
        pid = request.GET.get("pid", None)
        prod = ProdMagament()
        if prod.delete_single_prod(pid):
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

    def put(self, request):
        prod = ProdMagament()
        if prod.update(request.data):
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

    def post(self, request):
        prod = ProdMagament()
        if prod.add(request.data):
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
