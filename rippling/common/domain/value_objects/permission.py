class AccessLevel:
    NONE = 0
    SYSTEM = 1
    EE = 1 << 1
    MANAGER = 1 << 2
    ADMIN = 1 << 3

    # All rippling employees.
    STAFF_USER = 1 << 4

    SUPER_USER = 1 << 5

    @classmethod
    def is_staff_level(cls, access_level):
        return access_level in [cls.STAFF_USER, cls.SUPER_USER]


class Permission:
    NONE = AccessLevel.NONE

    # Rippling internal
    SYSTEM = (
        AccessLevel.SYSTEM
    )  # No one can see this except for our own back-end. Front end cant see this.
    SUPER_USER = SYSTEM | AccessLevel.SUPER_USER  # Just Prasanna.
    STAFF_USER = SUPER_USER | AccessLevel.STAFF_USER  # Just rippling employees.

    MANAGER = STAFF_USER | AccessLevel.MANAGER  # Only the 'manager' can see this row.
    ADMIN = STAFF_USER | AccessLevel.ADMIN  # Only if you are an admin of this company.

    ALL = SUPER_USER | ADMIN | MANAGER | AccessLevel.EE
