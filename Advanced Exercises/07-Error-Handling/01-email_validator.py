class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


valid_domains = [".com", ".bg", ".org", ".net"]
email = input()
while not email == "End":
    name = email[:email.find('@')]
    domain = email[email.find('.'):]
    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")
    if '@' not in email:
        raise MustContainAtSymbolError("Email must contain @")
    if domain not in valid_domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    print("Email is valid")
    email = input()
