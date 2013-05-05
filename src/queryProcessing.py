class ProcessingQuery(object):
    """Passed among QueryProcessors to process each part of the query.
        sVariables are strings
        proper variables should be set by the processor."""
    
    def __init__(self, product):
        self.sProduct = product
        self.sRango = None
    
    def setRango(self, rango):
        self.sRango = rango

## Query processing classes
class QueryProcessor(object):
    """Abstract class for query processing. processQuery modifies
        the given processingQuery adding proper variables made
        from the sVariables. """
    def processQuery(self, aProcessingQuery):
        raise NotImplementedError()

class ProductQueryProcessor(QueryProcessor):
    def __init__(self, aValidProductsProvider):
        self.validProductsProvider = aValidProductsProvider

    def processQuery(self, aProcessingQuery):
        productList = self.validProductsProvider.products()
        for p in productList:
            if (p.name() == aProcessingQuery.sProduct):
                aProcessingQuery.product = p
        try:
            aProcessingQuery.product
        except AttributeError:
            raise IllegalProduct(aProcessingQuery.sProduct)
        
        return aProcessingQuery

class MultiQueryProcessor(QueryProcessor):
    def __init__(self, aQueryProcessorList):
        self.queryProcessorList = aQueryProcessorList

    def processQuery(self, aProcessingQuery):
        for p in self.queryProcessorList:
            p.processQuery(aProcessingQuery)	
        return p
		
		
## Processing errors
class ProcessingError(Exception):
    """Processing error"""

class IllegalProduct(ProcessingError):
        def __init__(self, sProduct):
            self.sProduct = sProduct

        def __str__(self):
            return self.sProduct + " is not a valid product"
