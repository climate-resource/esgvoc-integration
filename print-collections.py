import textwrap

import esgvoc.api as ev


def main():
    fail_if_empty = True
    # fail_if_empty = False

    for collection in [
        "activity",
        "archive",
        "area_label",
        "branded_suffix",
        "branded_variable",
        "contributor",
        "contributor_member",
        "conventions",
        "creation_date",
        "data_specs_version",
        "directory_date",
        "drs_specs",
        "experiment",
        "forcing_index",
        "frequency",
        "grid",
        "horizontal_label",
        "initialization_index",
        "license",
        "mip_era",
        "nominal_resolution",
        "physics_index",
        "product",
        "realization_index",
        "realm",
        "region",
        "source",
        "temporal_label",
        "time_range",
        "tracking_id",
        "variable",
        "variant_label",
        "vertical_label",
    ]:
        print(collection)
        ev_obj = ev.get_all_terms_in_collection("cmip7", collection)
        if fail_if_empty and not ev_obj:
            msg = f"{collection=} is empty"
            raise ValueError(msg)

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
