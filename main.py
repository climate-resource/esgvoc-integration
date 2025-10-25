from pprint import pprint

import esgvoc.api as ev


def main():
    for collection in [
        "activity",
        "archive",
        "area_label",
        "branded_suffix",
        "contributor",
        "directory_date",
        "drs_specs",
        "experiment",
        "frequency",
        "grid",
        "mip_era",
        "region",
        "source",
        "time_range",
        "variable",
        "variant_label",
    ]:
        print(collection)
        ev_obj = ev.get_all_terms_in_collection("cmip7", collection)
        print(type(ev_obj))
        pprint(ev_obj)


if __name__ == "__main__":
    main()
