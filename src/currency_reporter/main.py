from .reporter import Reporter
from .providers.ripio import RipioProvider


def main():
    report_agent = Reporter()
    provider = RipioProvider()
    report_agent.add_provider(provider)
    report_agent.generate_reports(10)
