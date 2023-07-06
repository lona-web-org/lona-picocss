import pytest


def _setup_django():
    from django.contrib.auth.models import User

    User.objects.create_user(
        'admin',
        'admin@example.org',
        'admin',
        is_staff=True,
        is_superuser=True,
    )


@pytest.fixture
async def test_django_project(
        event_loop,
        lona_project_context,
        transactional_db,
):

    import os

    import test_django_project

    context = await lona_project_context(
        project_root=os.path.dirname(
            os.path.dirname(test_django_project.__file__),
        ),
        settings=['settings.py'],
    )

    await event_loop.run_in_executor(None, _setup_django)

    yield context
