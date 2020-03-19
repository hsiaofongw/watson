from argparse import Namespace

# this task is task-specified and should not put it in general use
class InputHandler:

    def get_http_scheme(self, args: Namespace) -> str:
        if hasattr(args, 'use_https') and hasattr(args, 'use_http'):
            if args.use_https:
                return 'https'
            elif args.use_http:
                return 'http'
            else:
                return 'https'
        else:
            return 'http'
    
    def get_sitemap_path(self, args: Namespace) -> str:
        return args.sitemap_path
    
    def get_host(self, args: Namespace) -> str:
        return args.host

    def get_user_agent(self, args: Namespace) -> str:
        return args.user_agent