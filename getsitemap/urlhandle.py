# compose a valid url from given parameters
class URLHandler:

    def make_sitemap_full_url(self, host: str, sitemap_path: str, http_scheme: str) -> str:
        return "{http_scheme}://{host}{sitemapPath}".format(
            http_scheme=http_scheme,
            host=host,
            sitemapPath=sitemap_path
        )