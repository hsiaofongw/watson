import argparse

from urlhandle import URLHandler
from inputhandle import InputHandler
from crawler import Crawler
from sitemap import SiteMapParser


# import default configuration
from config import USER_AGENT
from config import SITEMAP_PATH


# do those when it is invoke from commandline
def main():

    # parse commandline inputs
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "host", 
        help='''your website's domain, for example, google.com'''
    )
    parser.add_argument(
        "--sitemap-path", 
        default=SITEMAP_PATH,

        help='''for example, if your domain is google.com, '''
             '''and sitemap path is /sitemap.xml, then we will'''
             ''' use google.com/sitemap.xml to crawl the sitemap'''
    )
    parser.add_argument(
        "--user-agent", 
        default=USER_AGENT,
        help='''exactly the User-Agent field in request header'''
    )
    parser.add_argument(
        "--use-https", 
        default=True,
        help='''use https to communicate with server, this is default'''
    )
    parser.add_argument(
        "--use-http", 
        default=False,
        help='''use http to communicate with the server'''
    )

    args = parser.parse_args()


    # retrieve parameters from inputs
    input_handler = InputHandler()
    sitemap_path = input_handler.get_sitemap_path(args)
    host = input_handler.get_host(args)
    http_scheme = input_handler.get_http_scheme(args)
    user_agent = input_handler.get_user_agent(args)


    # make full url from parameters
    url_handler = URLHandler()
    full_url_to_crawl = url_handler.make_sitemap_full_url(
        host = host,
        sitemap_path = sitemap_path,
        http_scheme = http_scheme
    )

    # start to crawl the sitemap response
    crawler = Crawler(user_agent)
    sitemap_response = crawler.crawl(full_url_to_crawl)

    # parse sitemap response to url list
    sitemap_parser = SiteMapParser()
    urls = sitemap_parser.parse_to_url_list(sitemap_response)
    
    # print url in the urls line by line
    for url in urls:
        print(url)


# in case it it imported as module, then don't run
if __name__ == '__main__':
    main()