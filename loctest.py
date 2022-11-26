from uagents import UserAgents

if __name__ == '__main__':
    ua = UserAgents()
    ts = ua.gen_ua(profile='chrome')
    print(next(ts))
    print(next(ts))
    print(next(ts))
    print(next(ts))