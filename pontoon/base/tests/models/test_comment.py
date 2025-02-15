import pytest

from pontoon.test.factories import (
    ProjectFactory,
    TeamCommentFactory,
    TranslationCommentFactory,
)


@pytest.mark.django_db
def test_serialize_comments():
    tr = TranslationCommentFactory.create()
    team = TeamCommentFactory.create()
    project = ProjectFactory.create()

    assert tr.serialize(project.contact) == {
        "author": tr.author.name_or_email,
        "username": tr.author.username,
        "user_banner": tr.author.banner(tr.translation.locale, project.contact),
        "user_gravatar_url_small": tr.author.gravatar_url(88),
        "created_at": tr.timestamp.strftime("%b %d, %Y %H:%M"),
        "date_iso": tr.timestamp.isoformat(),
        "content": tr.content,
        "pinned": tr.pinned,
        "id": tr.id,
    }

    assert team.serialize(project.contact) == {
        "author": team.author.name_or_email,
        "username": team.author.username,
        "user_banner": team.author.banner(team.locale, project.contact),
        "user_gravatar_url_small": team.author.gravatar_url(88),
        "created_at": team.timestamp.strftime("%b %d, %Y %H:%M"),
        "date_iso": team.timestamp.isoformat(),
        "content": team.content,
        "pinned": team.pinned,
        "id": team.id,
    }
