from github import Github
g=Github("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")
repos = g.get_repos()
for repo in repos:
    print(repo.name)
a=g.repo.create_file('json.txt')
