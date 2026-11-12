from data.projects import GITHUB, PROJECTS, by_slug


def test_catalog_matches_public_repos():
    slugs = [project["slug"] for project in PROJECTS]
    assert slugs == ["fraud", "fund-facts", "retail", "voice"]
    assert len(slugs) == len(set(slugs))


def test_every_project_points_at_this_github_account():
    pages = set()
    for project in PROJECTS:
        assert project["repo"].startswith(GITHUB + "/")
        assert project["page"].startswith("pages/")
        assert project["title"]
        assert project["proof"]
        pages.add(project["page"])
    assert len(pages) == len(PROJECTS)


def test_lookup():
    assert by_slug("fund-facts")["repo"].endswith("groww-ai-hdfc-mf-facts")
