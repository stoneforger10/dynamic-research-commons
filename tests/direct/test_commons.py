import hashlib
import time

import pytest


def h(value):
    return hashlib.sha256(value.encode()).hexdigest()


def test_owner_and_composition_preflight(direct_vm, direct_deploy, direct_alice, direct_bob):
    c = direct_deploy("contracts/DynamicResearchCommons.py")
    direct_vm.sender = direct_alice
    c.create_space("lab", "Open Lab")
    c.register_object("lab", "idea", "idea", "https://example.com/idea", h("idea"))
    c.register_object("lab", "method", "method", "https://example.com/method", h("method"))
    s = c.get_space("lab")
    assert s["sequence"] == 0
    with direct_vm.expect_revert("exact object composition required"):
        c.resolve_composition("lab", "bad", "idea,idea", 0, int(time.time()) + 300)
    with direct_vm.prank(direct_bob), direct_vm.expect_revert("space owner required"):
        c.connect_objects("lab", "edge", "idea", "method", "uses")
