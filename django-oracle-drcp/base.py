import cx_Oracle
from django.core.exceptions import ImproperlyConfigured
from django.db.backends.oracle.base import DatabaseWrapper as DjDatabaseWrapper


class DatabaseWrapper(DjDatabaseWrapper):
    def __init__(self, *args, **kwargs):
        super(DatabaseWrapper, self).__init__(*args, **kwargs)
        default_pool = {"min": 20, "max": 50, "increment": 1}
        pool_config = self.settings_dict.get("POOL", default_pool)
        if set(pool_config.keys()) != {"min", "max", "increment"}:
            raise ImproperlyConfigured(
                "POOL database option requires 'min', 'max', and 'increment'"
            )
        if not all(isinstance(val, int) for val in pool_config.values()):
            raise ImproperlyConfigured("POOL database option values must be numeric")

        self.pool = cx_Oracle.SessionPool(
            user=self.settings_dict["USER"],
            password=self.settings_dict["PASSWORD"],
            dsn=self.settings_dict["NAME"],
            **pool_config
        )

    def get_new_connection(self, conn_params):
        return self.pool.acquire()

    def _close(self):
        if self.connection is not None:
            with self.wrap_database_errors:
                return self.pool.release(self.connection)
