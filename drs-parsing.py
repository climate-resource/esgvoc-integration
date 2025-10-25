from pprint import pprint

from esgvoc.apps.drs.validator import DrsValidator


def main():
    validator = DrsValidator("cmip7", pedantic=True)

    in_dir = "MIP-DRS7/CMIP7/CMIP/IPSL/DEMO/piControl/r1i1p1f1/global/mon/tas/tavg-h2m-hxy-u/g99/20251031"
    report = validator.validate_directory(in_dir)
    if report.errors:
        raise ValueError(report.errors)

    extracted_terms = report.mapping_used
    print(f"{in_dir=} ")
    pprint(extracted_terms)

    in_file = (
        "tas_tavg-h2m-hxy-u_mon_global_g99_DEMO_historical_r1i1p1f1_185001-202112.nc"
    )
    report = validator.validate_file_name(in_file)
    if report.errors:
        raise ValueError(report.errors)

    extracted_terms = report.mapping_used
    print()
    print(f"{in_file=} ")
    pprint(extracted_terms)


if __name__ == "__main__":
    main()
