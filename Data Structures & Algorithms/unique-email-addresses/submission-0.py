class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        
        for email in emails:
            # Split the email into local and domain parts
            local, domain = email.split('@')
            
            # Rule 1: Ignore everything after the first '+' in the local name
            local = local.split('+')[0]
            
            # Rule 2: Remove all periods '.' from the local name
            local = local.replace('.', '')
            
            # Recombine and add to our set of unique emails
            unique_emails.add(local + '@' + domain)
            
        # The number of unique emails is the size of the set
        return len(unique_emails)