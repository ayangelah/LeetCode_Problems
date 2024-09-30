from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        # key: url/subdomain value: number of visits
        # iterate through cpdomains and for each, we iterate through to the top level domain and increment counts for all domains above subdomain
        domain_dict = {}
        for domain in cpdomains:
            domain_tuple = domain.split(' ')
            curr_domain = domain_tuple[1].split('.')
            while curr_domain:
                temp = '.'.join(curr_domain)
                if temp not in domain_dict:
                    domain_dict[temp] = int(domain_tuple[0])
                else:
                    domain_dict[temp] += int(domain_tuple[0])
                curr_domain.pop(0)
        result_list = []
        for i in domain_dict.items():
            result_list.append(f"{i[1]} {i[0]}")
        return result_list