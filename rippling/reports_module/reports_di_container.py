from injector import Binder, Module

from reports_module.modules.embedded_report.embedded_report_di import (
    EmbeddedReportModule,
)
from .modules.connected_report.connected_report_di import ConnectedReportModule


class ReportsDIContainer(Module):
    def configure(self, binder: Binder):
        binder.install(ConnectedReportModule())
        binder.install(EmbeddedReportModule())
