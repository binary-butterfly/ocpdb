from webapp.public_api.base_handler import PublicApiBaseHandler
from webapp.repositories import BusinessRepository


class BusinessHandler(PublicApiBaseHandler):
    business_repository: BusinessRepository

    def __init__(self, *args, business_repository: BusinessRepository, **kwargs):
        super().__init__(*args, **kwargs)
        self.business_repository = business_repository

    def get_business_by_id(self, business_id: int):
        business = self.business_repository.fetch_by_id(business_id)
        return business

    def get_business_by_name(self, business_name: str):
        business = self.business_repository.fetch_business_by_name(business_name)
        return business

    def get_businesses(self):
        businesses = self.business_repository.fetch_businesses()
        return businesses

