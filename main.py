from pprint import pprint

import esgvoc.api as ev


def main():
    for dd in [
        "activity",
        "archive",
        "area_label",
        "experiment",
    ]:
        print(dd)
        ev_obj = ev.get_all_terms_in_data_descriptor(dd)
        print(type(ev_obj))
        pprint(ev_obj)


if __name__ == "__main__":
    main()
