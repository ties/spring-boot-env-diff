import json
from collections import defaultdict
from dataclasses import dataclass
from typing import Dict, Generator, Iterable, List, NamedTuple, Optional
from typing.io import TextIO

import click


class PropertyValue(NamedTuple):
    key: str
    value: str
    source: Optional[str] = None

    def describe(self) -> str:
        return f"{self.value} from {self.source}"


def read_env_output(inp: object) -> Generator[PropertyValue, None, None]:
    if "activeProfiles" in inp:
        yield PropertyValue("activeProfiles", inp["activeProfiles"], "<root>")

    for propertySource in inp.get("propertySources", {}):
        source_name = propertySource.get("name", "<unknown>")
        for key, content in propertySource.get("properties", {}).items():
            yield PropertyValue(
                key, content.get("value"), content.get("origin", source_name)
            )


def collect_by_key(pv_pairs: Iterable[PropertyValue]) -> Dict[str, List]:
    """Collect all values per key."""
    effective_pairs: Dict[str, list] = defaultdict(list)

    for property_value in pv_pairs:
        effective_pairs[property_value.key].append(property_value)

    # return a regular dict
    return dict(effective_pairs)


@click.command()
@click.argument(
    "lhs", type=click.File("r")
)  # , help='The left hand side for comparison')
@click.argument(
    "rhs", type=click.File("r")
)  # , help='The right hand side for comparison')
def spring_boot_env_diff(lhs: TextIO, rhs: TextIO):
    """Diff the configuration files in the left hand side and right hand side."""
    lhs_obj = json.load(lhs)
    rhs_obj = json.load(rhs)

    lhs_content = read_env_output(lhs_obj)
    rhs_content = read_env_output(rhs_obj)

    effective_lhs = collect_by_key(lhs_content)
    effective_rhs = collect_by_key(rhs_content)

    for key in effective_lhs.keys():
        try:
            lhs = effective_lhs[key][0]
            rhs = effective_rhs[key][0]
            if lhs.value != rhs.value:
                # if one of the sides is not a string, process as if json like yaml does.
                if not isinstance(lhs.value, str):
                    if json.loads(rhs.value) == lhs.value:
                        continue
                if not isinstance(rhs.value, str):
                    if json.loads(lhs.value) == rhs.value:
                        continue
                print(
                    f"mismatch: {key} in lhs: {lhs.describe()}, while in rhs: {rhs.describe()}"
                )
        except KeyError:
            print(f"{key} not present in rhs. lhs has value {lhs.describe()}")


if __name__ == "__main__":
    """Diff the output of spring boot `/actuator/env` output."""
    spring_boot_env_diff()
