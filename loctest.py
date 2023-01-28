from uagents import UserAgents

if __name__ == '__main__':
    ua = UserAgents(profile='chrome')
    while True:
        print(ua.return_ua())