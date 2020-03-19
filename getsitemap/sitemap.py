
import xmltodict

from typing import List

# get a list of url from sitemap reponse (bytes)
class SiteMapParser:

    def parse_to_url_list(self, sitemap_bytes: bytes) -> List[str]:
        xml_dict = xmltodict.parse(sitemap_bytes)
        urls = list(map(lambda x:x['loc'], xml_dict['urlset']['url']))
        return urls