import textwrap

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
        for i, item in enumerate(ev_obj):
            for idx_f, field in enumerate(type(item).model_fields):
                v = textwrap.wrap(
                    str(getattr(item, field)),
                    subsequent_indent="  ",
                    break_long_words=False,
                )
                prefix = f"     {field}" if idx_f >= 1 else f"{i + 1:3d}. {field}"
                disp_l = [f"{prefix}: {v[0]}"]
                if len(v) > 1:
                    disp_l.extend([f"       {vv}" for vv in v[1:]])

                print(textwrap.indent("\n".join(disp_l), ""))

        print()


if __name__ == "__main__":
    main()
