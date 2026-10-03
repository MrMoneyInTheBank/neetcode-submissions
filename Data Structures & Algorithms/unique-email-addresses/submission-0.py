class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def encode(email):
            local, domain = email.split("@", maxsplit=1)
            local = email.split("+", maxsplit=1)[0]
            local = "".join([c for c in local if c != "."])
        
            return local + "@" + domain
        
        emails = [encode(e) for e in emails]

        return len(set(emails))