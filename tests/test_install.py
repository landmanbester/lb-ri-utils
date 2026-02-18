def test_import():
    import lb_ri_utils

    assert hasattr(lb_ri_utils, "__version__")


def test_version_is_string():
    from lb_ri_utils import __version__

    assert isinstance(__version__, str)
