class QueryFactory:
    def createQuery(self, aProcessingQuery):
        return Query(aProcessingQuery.product)

class Query:
    def __init__(self, product):
        self.product = product

    def __str__(self):
        return "Query [product="+str(self.product)+"]"

            
