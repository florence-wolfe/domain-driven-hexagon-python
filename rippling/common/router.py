from __future__ import absolute_import
import copy
from rest_framework.routers import SimpleRouter


class Router(SimpleRouter):
    """
    Map http methods to actions defined on the bulk mixins.
    """

    def register(self, *args, **kwargs):
        if "base_name" in kwargs:
            kwargs["basename"] = kwargs["base_name"]
            del kwargs["base_name"]
        super(SimpleRouter, self).register(*args, **kwargs)

    routes = copy.deepcopy(SimpleRouter.routes)
