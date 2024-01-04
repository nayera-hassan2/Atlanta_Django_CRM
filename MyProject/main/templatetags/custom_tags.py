from django import template

register = template.Library()

@register.simple_tag
def empty_table_row(num_cells):
    return ''.join('' for _ in range(num_cells))


def empty_table_structure(header_columns):
    header_row = ''.join(f'<th>{column}</th>' for column in header_columns)
    return f'<thead class="table-dark"><tr>{header_row}</tr></thead><tbody><tr>{"".join("<td></td>" for _ in header_columns)}</tr></tbody>'
