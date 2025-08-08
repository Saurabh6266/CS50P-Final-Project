from project import get_personal_info, get_linkedin, get_github


def test_get_personal_info(monkeypatch):
    # Simulate user input for name, phone, and email
    inputs = iter(["John Doe", "+91 9876543210", "john@example.com"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    name, phone, email = get_personal_info()
    assert name == "John Doe"
    assert "+91" in phone
    assert email == "john@example.com"


def test_get_linkedin(monkeypatch):
    # Simulate user saying yes and entering a LinkedIn URL
    inputs = iter(["yes", "https://linkedin.com/in/johndoe"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    linkedin_id = get_linkedin()
    assert linkedin_id == "https://linkedin.com/in/johndoe"


def test_get_github(monkeypatch):
    # Simulate user saying no to GitHub
    inputs = iter(["no"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    github_profile = get_github()
    assert github_profile == ""
