class MyMiddleware1:
    def process_response(self, request, response, spider):
        # I will handle some unexpected request results here uniformly,
        # and then throw an error to prevent my spider from processing this result.
        if len(response.body) < 10000:
            raise Exception('Bad data!')

        return response


class MyMiddleware2:
    def _track(self, msg):
        pass

    def process_exception(self, request, exception, spider):
        # Then I hope to uniformly record these errors in the next layer of middleware.
        # But this middleware will not receive the previous middleware process_ Exceptions generated in response.
        self._track(str(type(exception)))
