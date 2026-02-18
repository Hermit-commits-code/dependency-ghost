import pytest
import requests
import os
import sys

from skopos import check_for_typosquatting, check_for_updates,check_identity

def test_check_identity_flags_suspicious_email():
    # Brand-jacking attempt: 'google-auth' maintained by a generic gmail
    mock_data = {"info": {"author_email": "attacker@gmail.com"}}
    passed, meta = check_identity("google-auth", mock_data)
    assert passed is False
    assert "gmail.com" in meta["email"]

def test_check_identity_allows_official_email():
    # Legit: 'google-auth' maintained by google.com
    mock_data = {"info": {"author_email": "admin@google.com"}}
    passed, meta = check_identity("google-auth", mock_data)
    assert passed is True

def test_check_for_updates_handles_offline(mocker):
    # Simulate a connection timeout
    mocker.patch("requests.get", side_effect=requests.exceptions.ConnectTimeout)
    
    # v0.22: check_for_updates should gracefully handle network failures
    try:
        check_for_updates("0.22.0")
    except Exception as e:
        pytest.fail(f"check_for_updates crashed on network error: {e}")

def test_whitelist_bypass(mocker):
    # This is complex because we are mocking the 'open' call globally
    mocker.patch("skopos.checker.os.path.exists", return_value=True)
    mocker.patch("skopos.checker.verify_whitelist_integrity", return_value=True)
    mocker.patch("sys.argv", ["skopos", "check", "safe-pkg"])
    
    mock_get = mocker.patch("skopos.checker.requests.get")
    
    # Use side_effect to handle binary vs string reads for the whitelist
    def mock_open_logic(*args, **kwargs):
        if 'b' in args[1] if len(args) > 1 else 'b' in kwargs.get('mode', ''):
             return mocker.mock_open(read_data=b"safe-pkg\n").return_value
        return mocker.mock_open(read_data="safe-pkg\n").return_value

    mocker.patch("skopos.checker.open", side_effect=mock_open_logic)

    from skopos.checker import main
    try:
        main()
    except SystemExit:
        pass

    urls_called = [call.args[0] for call in mock_get.call_args_list]
    # Verify we SKIPPED the forensic check for 'safe-pkg' because it's whitelisted
    assert not any("safe-pkg" in url for url in urls_called)