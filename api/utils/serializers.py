from rest_framework import serializers
from rest_framework.utils.serializer_helpers import ReturnDict
from utils import models

class ThemeDictSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        result = super().to_representation(data)

        processed_theme = {}

        for res in result:
            category_name = res["category_name"]

            if category_name not in processed_theme:
                processed_theme[category_name] = {}

            processed_theme[category_name][res["name"]] = res["color"]

        return processed_theme

    @property
    def data(self):
        # ListSerializer.data envolve o resultado em ReturnList, que reduziria o dict às chaves
        return ReturnDict(self.to_representation(self.instance), serializer=self)


class ThemeSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(
        source="category.name",
        read_only=True,
    )

    class Meta:
        model = models.Theme
        fields = ["name", "color", "category_name"]
        list_serializer_class = ThemeDictSerializer