# https://leetcode.com/problems/validate-ip-address/
# 468-validate-ip-address


class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        query_list = queryIP.split(".")

        if len(query_list) == 4:
            for x in query_list:
                if (
                    (len(x) > 1 and x[0] == "0")
                    or not x.isdigit()
                    or not 0 <= int(x) <= 255
                ):
                    return "Neither"
            return "IPv4"
        elif len(query_list) == 1:
            query_list = queryIP.split(":")
            if len(query_list) != 8:
                return "Neither"
            for x in query_list:
                if not 1 <= len(x) <= 4:
                    return "Neither"
                for char in x:
                    if not char.lower() in "abcdef0123456789":
                        return "Neither"
            return "IPv6"
        return "Neither"
