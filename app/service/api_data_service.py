
class ApiDataService:
    def getData(self, endpoint, params):
      print(params.get('test'))
      return "Response from " + endpoint + " endpoint"
