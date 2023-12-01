from typing import Dict, Any

from common.domain.value_objects.permission import Permission


class DocumentBase:
    meta: Dict[str, Any] = {
        "abstract": True,
        "strict": False,
        "alertable": False,
        "alert_inheritance": False,
        "permission": {
            "read": Permission.ADMIN,
            "list": Permission.ADMIN,
        },
    }
