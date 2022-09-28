from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from HelloProd.domain.views import ProdMagament
from HelloProd.infrastructure.prodOperation import Prod
from HelloProd.infrastructure.ProdSerializer import ProdSerializer


class ProdApiView(APIView):
    serializer_class = ProdSerializer

    @swagger_auto_schema(
        operation_summary="Query a product detail.",
        operation_description="\
            Get data from Infrastructure layer becasue of\
            just retrieving data from DB without any domain know-how.\
            if no PID input, the API will return all products detail.",
        manual_parameters=[
            openapi.Parameter(
                "pid",
                openapi.IN_QUERY,
                description=("PID of product"),
                type=openapi.TYPE_INTEGER,
                required=False,
            ),
        ],
        responses={200: "SUCCESS"},
    )
    def get(self, request):
        data = dict()
        pid = request.GET.get("pid", None)
        if pid is None:
            data["data"] = Prod().get_all()
        else:
            data["data"] = Prod().get_one(pid)

        return Response(data=data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Delete a product.",
        operation_description="Delete a product by pid.",
        manual_parameters=[
            openapi.Parameter(
                "pid",
                openapi.IN_QUERY,
                description=("PID of product"),
                type=openapi.TYPE_INTEGER,
                required=False,
            ),
        ],
        responses={200: "SUCCESS", 403: "FORBIDDEN"},
    )
    def delete(self, request):
        pid = request.GET.get("pid", None)
        prod = ProdMagament()
        if prod.delete_single_prod(pid):
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

    @swagger_auto_schema(
        operation_summary="Update a product.",
        operation_description="Update the detail of specific product.",
        request_body=serializer_class,
        responses={200: "SUCCESS", 403: "FORBIDDEN"},
    )
    def put(self, request):
        """
        Update a product detail.
        """
        prod = ProdMagament()
        if prod.update(request.data):
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

    @swagger_auto_schema(
        operation_summary="Add a product.",
        operation_description="Add a product.",
        request_body=serializer_class,
        responses={200: "SUCCESS", 403: "FORBIDDEN"},
    )
    def post(self, request):
        """
        Add a new product.
        """
        prod = ProdMagament()
        if prod.add(request.data):
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
