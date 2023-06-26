from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class NavItem:
    title: str = ''
    url: str = ''
    icon: str = ''
    nav_items: list[NavItem] = field(default_factory=list)


def get_debug_navigation(server, request):
    return [

        # settings
        NavItem(
            title='Settings',
            url=server.reverse('picocss__settings'),
            icon='settings',
        ),

        # components
        NavItem(
            title='Components',
            icon='box',
            nav_items=[
                NavItem(
                    title='Typography',
                    url=server.reverse('picocss__components__typography'),
                ),
                NavItem(
                    title='Icons',
                    url=server.reverse('picocss__components__icons'),
                ),
                NavItem(
                    title='Cards',
                    url=server.reverse('picocss__components__cards'),
                ),
                NavItem(
                    title='Forms',
                    url=server.reverse('picocss__components__forms'),
                ),
                NavItem(
                    title='Buttons',
                    url=server.reverse('picocss__components__buttons'),
                ),
                NavItem(
                    title='Progress',
                    url=server.reverse('picocss__components__progress'),
                ),
                NavItem(
                    title='Tabs',
                    url=server.reverse('picocss__components__tabs'),
                ),
                NavItem(
                    title='Modal',
                    url=server.reverse('picocss__components__modal'),
                ),
                NavItem(
                    title='Scroller',
                    url=server.reverse('picocss__components__scroller'),
                ),
            ],
        ),

        # error pages
        NavItem(
            title='Error Pages',
            icon='alert-triangle',
            nav_items=[
                NavItem(
                    title='Forbidden Error',
                    url=server.reverse('picocss__forbidden_error'),
                ),
                NavItem(
                    title='Not Found Error',
                    url=server.reverse('picocss__not_found_error'),
                ),
                NavItem(
                    title='Internal Error',
                    url=server.reverse('picocss__internal_error'),
                ),
            ],
        ),
    ]


def get_django_auth_navigation(server, request):
    from django.urls import reverse

    nav_items = []

    # user urls
    if request.user.is_authenticated:
        sub_nav_items = [
            NavItem(
                title='Change Password',
                url=reverse('password_change'),
            ),
            NavItem(
                title='Logout',
                url=reverse('logout'),
            ),
        ]

        if request.user.is_staff:
            sub_nav_items.append(
                NavItem(
                    title='Django Admin',
                    url=reverse('admin:index'),
                ),
            )

        nav_items.append(
            NavItem(
                title=request.user.get_username(),
                icon='user',
                nav_items=sub_nav_items,
            ),
        )

    # login url
    else:
        nav_items.append(
            NavItem(
                title='Login',
                url=reverse('login'),
            ),
        )

    return nav_items
