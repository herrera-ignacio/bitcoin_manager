from reporter import Reporter
from providers.ripio import RipioProvider


def main():
    report_agent = Reporter()
    provider = RipioProvider()
    report_agent.add_provider(provider)
    report_agent.generate_reports(10)


if __name__ == "__main__":
    main()
    print('0000000')
