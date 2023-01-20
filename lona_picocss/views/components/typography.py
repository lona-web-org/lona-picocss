import textwrap

from lona import View

from lona_picocss.html import (
    Table,
    THead,
    TBody,
    HTML,
    Card,
    Pre,
    H1,
    H2,
    H3,
    H4,
    H5,
    H6,
    Tr,
    Th,
    Td,
    Br,
    A,
    P,
)


class TypographyView(View):
    def handle_request(self, request):
        self.set_title('Typography')

        return HTML(
            H1('Typography'),

            H2('Headings'),
            Card(
                H1('Heading 1'),
                H2('Heading 2'),
                H3('Heading 3'),
                H4('Heading 4'),
                H5('Heading 5'),
                H6('Heading 6'),
            ),

            H2('Paragraph'),
            P("""
                Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed
                diam nonumy eirmod tempor invidunt ut labore et dolore magna
                aliquyam erat, sed diam voluptua. At vero eos et accusam et
                justo duo dolores et ea rebum. Stet clita kasd gubergren, no
                sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem
                ipsum dolor sit amet, consetetur sadipscing elitr, sed diam
                nonumy eirmod tempor invidunt ut labore et dolore magna
                aliquyam erat, sed diam voluptua. At vero eos et accusam et
                justo duo dolores et ea rebum. Stet clita kasd gubergren, no
                sea takimata sanctus est Lorem ipsum dolor sit amet.
            """),

            H2('Links'),
            A('Primary Link', href='#'),
            Br(),
            A('Secondary Link', href='#', secondary=True),
            Br(),
            A('Contrast Link', href='#', contrast=True),

            H2('Pre'),
            Pre(textwrap.dedent("""
                Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed
                diam nonumy eirmod tempor invidunt ut labore et dolore magna
                aliquyam erat, sed diam voluptua. At vero eos et accusam et
                justo duo dolores et ea rebum. Stet clita kasd gubergren, no
                sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem
                ipsum dolor sit amet, consetetur sadipscing elitr, sed diam
                nonumy eirmod tempor invidunt ut labore et dolore magna
                aliquyam erat, sed diam voluptua. At vero eos et accusam et
                justo duo dolores et ea rebum. Stet clita kasd gubergren, no
                sea takimata sanctus est Lorem ipsum dolor sit amet.
            """).strip()),

            H2('Table'),
            Table(
                THead(
                    Tr(
                        Th('Column 1'),
                        Th('Column 2'),
                        Th('Column 3'),
                        Th('Column 4'),
                    ),
                ),
                TBody(
                    Tr(
                        Td('Row 1, Column 1'),
                        Td('Row 1, Column 2'),
                        Td('Row 1, Column 3'),
                        Td('Row 1, Column 4'),
                    ),
                    Tr(
                        Td('Row 2, Column 1'),
                        Td('Row 2, Column 2'),
                        Td('Row 2, Column 3'),
                        Td('Row 2, Column 4'),
                    ),
                    Tr(
                        Td('Row 3, Column 1'),
                        Td('Row 3, Column 2'),
                        Td('Row 3, Column 3'),
                        Td('Row 3, Column 4'),
                    ),
                ),
            )
        )
