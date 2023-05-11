from flask import jsonify
from flask_cors import cross_origin

from webapp.dependencies import dependencies
from webapp.common.base_blueprint import BaseBlueprint
from .business_handler import BusinessHandler
from webapp.common.rest import BaseMethodView


class BusinessBlueprint(BaseBlueprint):
    business_handler: BusinessHandler

    def __init__(self):
        self.business_handler = BusinessHandler(
            **self.get_base_handler_dependencies(),
            business_repository=dependencies.get_business_repository(),
        )

        super().__init__('businesses', __name__, url_prefix='/api/public/v1/businesses/')

        self.add_url_rule(
            '/<int:business_id>',
            view_func=BusinessMethodView.as_view(
                'businesses',
                **self.get_base_method_view_dependencies(),
                business_handler=self.business_handler,
            ),

        )


class BusinessMethodView(BaseMethodView):
    business_handler: BusinessHandler

    def __init__(self, *args, business_handler: BusinessHandler, **kwargs):
        super().__init__(*args, **kwargs)
        self.business_handler = business_handler

    @cross_origin()
    def get(self, business_id: int):
        business = self.business_handler.get_business_by_id(business_id)
        return jsonify(business)
